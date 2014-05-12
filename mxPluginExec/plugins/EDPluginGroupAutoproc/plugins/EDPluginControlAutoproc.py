# coding: utf8
#
#    Project: Autoproc
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author: Thomas Boeglin
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

__author__="Thomas Boeglin"
__license__ = "GPLv3+"
__copyright__ = "ESRF"


WS_URL='http://ispyb.esrf.fr:8080/ispyb-ejb3/ispybWS/ToolsForCollectionWebService?wsdl'

import os
import os.path
import time
import sys
import json
import traceback
import shutil
import socket
from stat import *

from EDPluginControl import EDPluginControl
from EDVerbose import EDVerbose

from EDFactoryPlugin import edFactoryPlugin

# try the suds from the system
try:
    import suds
except ImportError:
    EDVerbose.warning('Suds not installed system wide, will try the EDNA bundled one')
    edFactoryPlugin.loadModule("EDInstallSudsv0_4")

import suds


from XSDataCommon import XSDataFile, XSDataBoolean, XSDataString
from XSDataCommon import  XSDataInteger, XSDataTime, XSDataFloat

from XSDataAutoproc import XSDataAutoprocInput
from XSDataAutoproc import XSDataResCutoff
from XSDataAutoproc import XSDataMinimalXdsIn
from XSDataAutoproc import XSDataXdsGenerateInput
from XSDataAutoproc import XSDataXdsOutputFile
from XSDataAutoproc import XSDataXscaleInput
from XSDataAutoproc import XSDataXscaleInputFile
from XSDataAutoproc import XSDataAutoprocInput
from XSDataAutoproc import XSDataAutoprocImport

edFactoryPlugin.loadModule('XSDataISPyBv1_4')
# plugin input/output
from XSDataISPyBv1_4 import XSDataInputStoreAutoProc
from XSDataISPyBv1_4 import XSDataResultStoreAutoProc

# dimple stuff

# this depends on the CCTBX modules so perhaps we could make running
# dimple dependent on whether those are installed or not
edFactoryPlugin.loadModule('XSDataCCP4DIMPLE')
from XSDataCCP4DIMPLE import CCP4DataInputControlPipelineCalcDiffMap
from XSDataCCP4DIMPLE import HKL, XYZ, CCP4MTZColLabels, CCP4LogFile

edFactoryPlugin.loadModule('EDPluginControlDIMPLEPipelineCalcDiffMapv10.py')

# what actually goes inside
from XSDataISPyBv1_4 import AutoProcContainer, AutoProc, AutoProcScalingContainer
from XSDataISPyBv1_4 import AutoProcScaling, AutoProcScalingStatistics
from XSDataISPyBv1_4 import AutoProcIntegrationContainer, AutoProcIntegration
from XSDataISPyBv1_4 import AutoProcProgramContainer, AutoProcProgram
from XSDataISPyBv1_4 import AutoProcProgramAttachment
from XSDataISPyBv1_4 import Image
from XSDataISPyBv1_4 import XSDataInputStoreAutoProc

# status updates
from XSDataISPyBv1_4 import AutoProcStatus
from XSDataISPyBv1_4 import  XSDataInputStoreAutoProcStatus

from xdscfgparser import parse_xds_file, dump_xds_file

import autoproclog
autoproclog.LOG_SERVER='rnice655:5000'

WAIT_FOR_FRAME_TIMEOUT=240 #max uses 50*5

# We used to go through the results directory and add all files to the
# ispyb upload. Now some files should not be uploaded, so we'll
# discriminate by extension for now
ISPYB_UPLOAD_EXTENSIONS=['.lp', '.mtz', '.log', '.inp', '.mtz.gz']

class EDPluginControlAutoproc(EDPluginControl):
    """
    Runs the part of the autoproc pipeline that has to be run on the
    cluster.
    """


    def __init__( self ):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataAutoprocInput)

    def configure(self):
        EDPluginControl.configure(self)
        self.ispyb_user = self.config.get('ispyb_user')
        self.ispyb_password = self.config.get('ispyb_password')

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlAutoproc.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.input_file, "No XDS input file")

        # save the root path (where the initial xds.inp is) for later use
        self.root_dir = os.path.abspath(os.path.dirname(self.dataInput.input_file.path.value))

        # at least check for the xds input file existence before
        # trying to start anything even if the first xds run does it
        # anyway
        if not os.path.isfile(self.dataInput.input_file.path.value):
            EDVerbose.ERROR('the specified input file does not exist')
            self.setFailure()
            # setFailure does not prevent preProcess/process/etc from running
            raise Exception('EDNA FAILURE')
        else:
            # copy it to our dir and modify our input
            newpath = os.path.join(self.getWorkingDirectory(),
                                   os.path.basename(self.dataInput.input_file.path.value))
            shutil.copyfile(self.dataInput.input_file.path.value,
                            newpath)
            self.dataInput.input_file.path = XSDataString(newpath)

    def preProcess(self, _edObject = None):
        EDPluginControl.preProcess(self)
        self.DEBUG('EDPluginControlAutoproc.preProcess starting')
        self.DEBUG('running on {0}'.format(socket.gethostname()))
        try:
            self.DEBUG('system load avg: {0}'.format(os.getloadavg()))
        except OSError:
            pass

        # for info to send to the autoproc stats server
        self.custom_stats = dict(creation_time=time.time(),
                                 processing_type='edna fastproc',
                                 datacollect_id=self.dataInput.data_collection_id.value,
                                 comments='running on {0}'.format(socket.gethostname()))




        data_in = self.dataInput

        # Check if the spacegroup needs to be converted to a number
        # (ie it's a symbolic thing)
        sgnumber = None
        if data_in.spacegroup is not None:
            try:
                sgnumber = int(data_in.spacegroup.value)
            except ValueError:
                # strip all whitespace and upcase the whole thing
                cleanedup = data_in.spacegroup.value.replace(' ', '').upper()
                if cleanedup in SPACE_GROUP_NUMBERS:
                    sgnumber = SPACE_GROUP_NUMBERS[cleanedup]


        xds_in = XSDataMinimalXdsIn()
        xds_in.input_file = data_in.input_file.path
        if sgnumber is not None:
            xds_in.spacegroup = XSDataInteger(sgnumber)
        xds_in.unit_cell = data_in.unit_cell

        self.log_file_path = os.path.join(self.root_dir, 'stats.json')
        self.DEBUG('will log timing information to {0}'.format(self.log_file_path))
        self.stats = dict()

        # Get the image prefix from the directory name
        # XXX: This is horrible
        try:
            self.image_prefix = '_'.join(os.path.basename(self.root_dir).split('_')[1:-1])
        except Exception:
            self.image_prefix = ''

        self.results_dir = os.path.join(self.root_dir, 'results', 'fast_processing')
        try:
            os.makedirs(self.results_dir)
        except OSError: # it most likely exists
            EDVerbose.ERROR('Error creating the results directory: {0}'.format(traceback.format_exc()))

        # Copy the vanilla XDS input file to the results dir
        infile_dest = os.path.join(self.results_dir, self.image_prefix + '_input_XDS.INP')
        shutil.copy(self.dataInput.input_file.path.value,
                    infile_dest)

        # Ensure the autoproc ids directory is there
        self.autoproc_ids_dir = os.path.join(self.results_dir, 'fastproc_integration_ids')
        try:
            os.makedirs(self.autoproc_ids_dir)
        except OSError: # it's there
            EDVerbose.ERROR('Error creating the autoproc ids directory: {0}'.format(traceback.format_exc()))


        # we'll need the low res limit later on
        lowres = data_in.low_resolution_limit
        if lowres is not None:
            self.low_resolution_limit = lowres.value
        else:
            self.low_resolution_limit = 50

        res_override = data_in.res_override
        if res_override is not None:
            self.res_override = res_override.value
        else:
            # XXX: default to 0?
            self.res_override = None

        # check the number of images (must be > 8) and get the first
        # image name to wait for. Also modify the XDS.INP file to
        # reflect these values, if specified
        conf = parse_xds_file(data_in.input_file.path.value)


        # Make the [XY]-GEO_CORR paths absolute
        if 'X-GEO_CORR=' in conf:
            xgeo = os.path.abspath(os.path.join(self.root_dir,
                                                conf['X-GEO_CORR='][0]))
            if not os.path.exists(xgeo):
                self.DEBUG('geometry file {0} does not exist, removing'.format(xgeo))
                del conf['X-GEO_CORR=']
            else:
                conf['X-GEO_CORR='] = xgeo

        if 'Y-GEO_CORR=' in conf:
            ygeo = os.path.abspath(os.path.join(self.root_dir,
                                                conf['Y-GEO_CORR='][0]))
            if not os.path.exists(ygeo):
                self.DEBUG('geometry file {0} does not exist, removing'.format(ygeo))
                del conf['Y-GEO_CORR=']
            else:
                conf['Y-GEO_CORR='] = ygeo

        dump_xds_file(data_in.input_file.path.value, conf)

        resrange = conf.get('INCLUDE_RESOLUTION_RANGE=')

        if resrange is not None:
            if self.low_resolution_limit is not None:
                resrange[0] = self.low_resolution_limit
            if self.res_override is not None:
                resrange[1] = self.res_override
            conf['INCLUDE_RESOLUTION_RANGE='] = resrange
            dump_xds_file(data_in.input_file.path.value, conf)


        data_range = conf.get('DATA_RANGE=')
        # we'll need that for the very last part ( file import )
        self.data_range = data_range
        if data_range is not None:
            start_image = data_range[0]
            end_image = data_range[1]
            if end_image - start_image < 8:
                self.ERROR('there are fewer than 8 images, aborting')
                self.setFailure()
                return

        template = conf['NAME_TEMPLATE_OF_DATA_FRAMES='][0]
        self.DEBUG('template for images is {0}'.format(template))
        # fix the path if it's not absolute
        if not os.path.isabs(template):
            self.DEBUG('file template {0} is not absolute'.format(template))
            base_dir = os.path.abspath(os.path.dirname(data_in.input_file.path.value))
            template = os.path.normpath(os.path.join(self.root_dir, template))
            conf['NAME_TEMPLATE_OF_DATA_FRAMES=']=template
            self.DEBUG('file template fixed to {0}'.format(template))
            self.DEBUG('dumping back the file to {0}'.format(data_in.input_file.path.value))
            dump_xds_file(data_in.input_file.path.value, conf)

        first_image = _template_to_image(template, start_image)

        self.xds_first = self.loadPlugin("EDPluginControlRunXdsFastProc")
        self.xds_first.dataInput = xds_in

        self.generate = self.loadPlugin("EDPluginXDSGenerate")

        self.first_res_cutoff = self.loadPlugin("EDPluginResCutoff")
        self.res_cutoff_anom = self.loadPlugin("EDPluginResCutoff")
        self.res_cutoff_noanom = self.loadPlugin("EDPluginResCutoff")

        self.parse_xds_anom = self.loadPlugin("EDPluginParseXdsOutput")
        self.parse_xds_noanom = self.loadPlugin("EDPluginParseXdsOutput")

        self.xscale_generate = self.loadPlugin("EDPluginControlXscaleGenerate")

        self.store_autoproc_anom = self.loadPlugin('EDPluginISPyBStoreAutoProcv1_4')
        self.store_autoproc_noanom = self.loadPlugin('EDPluginISPyBStoreAutoProcv1_4')

        self.file_conversion = self.loadPlugin('EDPluginControlAutoprocImport')

        self.dimple = self.loadPlugin('EDPluginControlDIMPLEPipelineCalcDiffMapv10')

        self.DEBUG('EDPluginControlAutoproc.preProcess finished')

    def process(self, _edObject = None):
        EDPluginControl.process(self)
        self.DEBUG('EDPluginControlAutoproc.process starting')

        process_start = time.time()


        # get our two integration IDs
        try:
            self.integration_id_noanom = create_integration_id(self.dataInput.data_collection_id.value)
        except Exception, e:
            EDVerbose.ERROR('could not get integration ID: \n{0}'.format(traceback.format_exc(e)))
            self.integration_id_noanom = None

        try:
            self.integration_id_anom = create_integration_id(self.dataInput.data_collection_id.value)
        except Exception, e:
            EDVerbose.ERROR('could not get integration ID: \n{0}'.format(traceback.format_exc(e)))
            self.integration_id_anom = None

        # first XDS plugin run with supplied XDS file
        EDVerbose.screen('STARTING XDS run...')

        t0=time.time()
        self.xds_first.executeSynchronous()

        self.stats['first_xds'] = time.time()-t0
        with open(self.log_file_path, 'w') as f:
            json.dump(self.stats, f)
        self.custom_stats['xds_runtime']=self.stats['first_xds']

        log_to_ispyb([self.integration_id_noanom, self.integration_id_anom],
                     'Indexing', 'Launched', 'first xds run')

        if self.xds_first.isFailure():
            EDVerbose.ERROR('first XDS run failed')
            self.setFailure()
            log_to_ispyb([self.integration_id_noanom, self.integration_id_anom],
                         'Indexing',
                         'Failed',
                         'first xds run failed after {0}s'.format(self.stats['first_xds']))
            return
        else:
            EDVerbose.screen('FINISHED first XDS run')
            log_to_ispyb([self.integration_id_noanom, self.integration_id_anom],
                         'Indexing',
                         'Successful',
                         'first xds run finished after {0}s'.format(self.stats['first_xds']))
        EDVerbose.screen('FINISHED first XDS run')


        # use the cell dimensions and spacegroup from XDS to create a
        # file in the results directory
        filename = '_'.join([str(self.xds_first.dataOutput.sg_number.value),
                             str(self.xds_first.dataOutput.cell_a.value),
                             str(self.xds_first.dataOutput.cell_b.value),
                             str(self.xds_first.dataOutput.cell_c.value),
                             str(self.xds_first.dataOutput.cell_alpha.value),
                             str(self.xds_first.dataOutput.cell_beta.value),
                             str(self.xds_first.dataOutput.cell_gamma.value)])
        try:
            os.mknod(os.path.join(self.results_dir, filename), 0755)
        except OSError: #file exists
            pass

        # Copy the XDS.INP file that was used for the successful run
        # to the results directory
        tmppath = os.path.join(self.results_dir, self.image_prefix + '_successful_XDS.INP')
        shutil.copy(os.path.join(self.xds_first.dataOutput.xds_run_directory.value, 'XDS.INP'),
                    tmppath)

        # Copy the INTEGRATE.LP file as well
        integrate_path = os.path.join(self.results_dir, self.image_prefix + '_INTEGRATE.LP')
        try:
            shutil.copy(os.path.join(self.xds_first.dataOutput.xds_run_directory.value,
                                     'INTEGRATE.LP'),
                        integrate_path)
        except (IOError, OSError):
            EDVerbose.ERROR('failed to copy INTEGRATE.LP file ({0}) to the results dir'.format(integrate_path))


        log_to_ispyb([self.integration_id_noanom, self.integration_id_anom],
                     'Indexing', 'Launched', 'start of res cutoff')

        # apply the first res cutoff with the res extracted from the first XDS run
        EDVerbose.screen('STARTING first resolution cutoff')
        t0=time.time()
        xdsresult = self.xds_first.dataOutput

        # for the custom stats
        self.custom_stats['overall_i_over_sigma']=xdsresult.total_completeness.isig.value
        self.custom_stats['overall_r_value']=xdsresult.total_completeness.rfactor.value
        self.custom_stats['inner_i_over_sigma']=xdsresult.completeness_entries[0].isig.value
        self.custom_stats['inner_r_value']=xdsresult.completeness_entries[0].rfactor.value
        self.custom_stats['i_over_sigma']=xdsresult.completeness_entries[-1].isig.value
        self.custom_stats['r_value']=xdsresult.completeness_entries[-1].rfactor.value


        res_cutoff_in = XSDataResCutoff()
        res_cutoff_in.xds_res = xdsresult
        res_cutoff_in.completeness_entries = xdsresult.completeness_entries
        res_cutoff_in.detector_max_res = self.dataInput.detector_max_res

        #XXX: remove from the data model as it is just pass-through?
        res_cutoff_in.total_completeness = xdsresult.total_completeness
        res_cutoff_in.completeness_cutoff = self.dataInput.completeness_cutoff
        res_cutoff_in.isig_cutoff = XSDataFloat(1.0)
        #res_cutoff_in.isig_cutoff = self.dataInput.isig_cutoff
        res_cutoff_in.r_value_cutoff = self.dataInput.r_value_cutoff
        res_cutoff_in.cc_half_cutoff = self.dataInput.cc_half_cutoff
        self.first_res_cutoff.dataInput = res_cutoff_in
        self.first_res_cutoff.executeSynchronous()

        self.stats['first_res_cutoff'] = time.time()-t0

        if self.first_res_cutoff.isFailure():
            EDVerbose.ERROR("res cutoff failed")
            log_to_ispyb([self.integration_id_noanom, self.integration_id_anom],
                         'Indexing',
                         'Failed',
                         'res cutoff failed in {0}s'.format(self.stats['first_res_cutoff']))
            self.setFailure()
            return
        else:
            EDVerbose.screen('FINISHED first resolution cutoff')
            log_to_ispyb([self.integration_id_anom, self.integration_id_noanom],
                         'Indexing',
                         'Successful',
                         'res cutoff finished in {0}s'.format(self.stats['first_res_cutoff']))


        with open(self.log_file_path, 'w') as f:
            json.dump(self.stats, f)

        resolution = self.first_res_cutoff.dataOutput.res

        # for the generate w/ and w/out anom we have to specify where
        # the first XDS plugin run took place
        xds_run_directory = os.path.abspath(self.xds_first.dataOutput.xds_run_directory.value)
        EDVerbose.screen("the xds run took place in {0}".format(xds_run_directory))
        generate_input = XSDataXdsGenerateInput()
        generate_input.resolution = resolution
        generate_input.previous_run_dir = XSDataString(xds_run_directory)
        self.generate.dataInput = generate_input

        log_to_ispyb([self.integration_id_anom, self.integration_id_noanom],
                     'Scaling', 'Launched', 'start of anom/noanom generation')

        self.DEBUG('STARTING anom/noanom generation')
        t0=time.time()
        self.generate.executeSynchronous()
        self.stats['anom/noanom_generation'] = time.time()-t0

        with open(self.log_file_path, 'w') as f:
            json.dump(self.stats, f)

        self.DEBUG('FINISHED anom/noanom generation')

        if self.generate.isFailure():
            EDVerbose.ERROR('generating w/ and w/out anom failed')
            self.setFailure()
            log_to_ispyb([self.integration_id_anom, self.integration_id_noanom],
                         'Scaling',
                         'Failed',
                         'anom/noanom generation failed in {0}s'.format(self.stats['anom/noanom_generation']))
            return
        else:
            EDVerbose.screen('generating w/ and w/out anom finished')
            log_to_ispyb([self.integration_id_anom, self.integration_id_noanom],
                         'Scaling',
                         'Successful',
                         'anom/noanom generation finished in {0}s'.format(self.stats['anom/noanom_generation']))

        # Copy the integrate and xds_ascii files to the results directory (for
        # max)
        shutil.copy(self.generate.dataOutput.hkl_anom.value, os.path.join(self.results_dir, 'XDS_ASCII.HKL'))
        shutil.copy(self.generate.dataOutput.integrate_anom.value, os.path.join(self.results_dir, 'INTEGRATE.HKL'))


        # we can now use the xds output parser on the two correct.lp
        # files, w/ and w/out anom
        parse_anom_input = XSDataXdsOutputFile()
        parse_anom_input.correct_lp = XSDataFile()
        parse_anom_input.correct_lp.path = self.generate.dataOutput.correct_lp_anom

        # this one is the same as the first XDS run since they share
        # the same directory
        gxparm_file_anom = XSDataFile()
        gxparm_file_anom.path = self.generate.dataOutput.gxparm
        parse_anom_input.gxparm = gxparm_file_anom

        self.parse_xds_anom.dataInput = parse_anom_input

        self.parse_xds_anom.executeSynchronous()

        if self.parse_xds_anom.isFailure():
            EDVerbose.ERROR('parsing the xds generated w/ anom failed')
            self.setFailure()
            return

        # now the other one w/out anom
        parse_noanom_input = XSDataXdsOutputFile()
        parse_noanom_input.correct_lp = XSDataFile()
        parse_noanom_input.correct_lp.path = self.generate.dataOutput.correct_lp_no_anom

        gxparm_file_noanom = XSDataFile()
        gxparm_file_noanom.path = self.generate.dataOutput.gxparm
        parse_noanom_input.gxparm = gxparm_file_noanom

        self.parse_xds_noanom.dataInput = parse_noanom_input
        self.parse_xds_noanom.executeSynchronous()

        if self.parse_xds_noanom.isFailure():
            EDVerbose.ERROR('parsing the xds generated w/ anom failed')
            self.setFailure()
            return

        # we now can apply the res cutoff on the anom and no anom
        # outputs. Note that this is not done in parallel, like the
        # xds parsing


        log_to_ispyb([self.integration_id_anom, self.integration_id_noanom],
                     'Scaling', 'Launched', 'start of anom/noanom resolution cutoffs')

        # XXX completeness_cutoff/res_override and isig_cutoff still
        # missing
        res_cutoff_anom_in = XSDataResCutoff()
        res_cutoff_anom_in.detector_max_res = self.dataInput.detector_max_res
        res_cutoff_anom_in.xds_res = self.parse_xds_anom.dataOutput
        res_cutoff_anom_in.completeness_entries = self.parse_xds_anom.dataOutput.completeness_entries
        res_cutoff_anom_in.total_completeness = self.parse_xds_anom.dataOutput.total_completeness
        # pass in global cutoffs
        res_cutoff_anom_in.completeness_cutoff = self.dataInput.completeness_cutoff
        res_cutoff_anom_in.isig_cutoff = XSDataFloat(1.0)
        #res_cutoff_anom_in.isig_cutoff = self.dataInput.isig_cutoff
        res_cutoff_anom_in.r_value_cutoff = self.dataInput.r_value_cutoff
        res_cutoff_anom_in.cc_half_cutoff = self.dataInput.cc_half_cutoff
        self.res_cutoff_anom.dataInput = res_cutoff_anom_in

        self.DEBUG('STARTING anom res cutoff')
        t0=time.time()
        self.res_cutoff_anom.executeSynchronous()
        self.stats['res_cutoff_anom'] = time.time()-t0

        with open(self.log_file_path, 'w') as f:
            json.dump(self.stats, f)

        if self.res_cutoff_anom.isFailure():
            EDVerbose.ERROR('res cutoff for anom data failed')
            self.setFailure()
            log_to_ispyb(self.integration_id_anom,
                         'Scaling',
                         'Failed',
                         'anom resolution cutoffs failed in {0}s'.format(self.stats['res_cutoff_anom'] + self.stats['res_cutoff_anom']))
            return
        else:
            self.screen('FINISHED anom res cutoff')
            log_to_ispyb(self.integration_id_anom,
                         'Scaling',
                         'Successful',
                         'anom resolution cutoffs finished in {0}s'.format(self.stats['res_cutoff_anom'] + self.stats['res_cutoff_anom']))

        self.DEBUG('FINISHED anom res cutoff')

        # same for non anom
        res_cutoff_noanom_in = XSDataResCutoff()
        res_cutoff_noanom_in.detector_max_res = self.dataInput.detector_max_res
        res_cutoff_noanom_in.xds_res = self.parse_xds_noanom.dataOutput
        res_cutoff_noanom_in.completeness_entries = self.parse_xds_noanom.dataOutput.completeness_entries
        res_cutoff_noanom_in.total_completeness = self.parse_xds_noanom.dataOutput.total_completeness
        # pass in global cutoffs
        res_cutoff_noanom_in.completeness_cutoff = self.dataInput.completeness_cutoff
        res_cutoff_noanom_in.isig_cutoff = XSDataFloat(1.0)
        #res_cutoff_noanom_in.isig_cutoff = self.dataInput.isig_cutoff
        res_cutoff_noanom_in.r_value_cutoff = self.dataInput.r_value_cutoff
        res_cutoff_noanom_in.cc_half_cutoff = self.dataInput.cc_half_cutoff
        self.res_cutoff_noanom.dataInput = res_cutoff_noanom_in

        self.DEBUG('STARTING noanom res cutoff')
        t0=time.time()
        self.res_cutoff_noanom.executeSynchronous()
        self.stats['res_cutoff_noanom'] = time.time()-t0

        with open(self.log_file_path, 'w') as f:
            json.dump(self.stats, f)

        if self.res_cutoff_noanom.isFailure():
            EDVerbose.ERROR('res cutoff for non anom data failed')
            self.setFailure()
            log_to_ispyb(self.integration_id_noanom,
                         'Scaling',
                         'Failed',
                         'noanom resolution cutoffs failed in {0}s'.format(self.stats['res_cutoff_anom'] + self.stats['res_cutoff_noanom']))
            return
        else:
            self.screen('FINISHED noanom res cutoff')
            log_to_ispyb(self.integration_id_noanom,
                         'Scaling',
                         'Successful',
                         'noanom resolution cutoffs finished in {0}s'.format(self.stats['res_cutoff_anom'] + self.stats['res_cutoff_noanom']))



        # now we just have to run XScale to generate w/ and w/out
        # anom, merged and unmerged

        # We use another control plugin for that to isolate the whole thing
        xscale_generate_in = XSDataXscaleInput()

        input_file = XSDataXscaleInputFile()
        input_file.path_anom = self.generate.dataOutput.hkl_anom
        input_file.path_noanom = self.generate.dataOutput.hkl_no_anom
        input_file.res = self.res_cutoff_anom.dataOutput.res

        xscale_generate_in.xds_files = [input_file]
        xscale_generate_in.unit_cell_constants = self.parse_xds_anom.dataOutput.unit_cell_constants
        xscale_generate_in.sg_number = self.parse_xds_anom.dataOutput.sg_number
        xscale_generate_in.bins = self.res_cutoff_anom.dataOutput.bins


        self.xscale_generate.dataInput = xscale_generate_in
        self.DEBUG('STARTING xscale generation')
        log_to_ispyb([self.integration_id_anom, self.integration_id_noanom],
                     'Scaling', 'Launched', 'start of xscale generation')

        t0=time.time()
        self.xscale_generate.executeSynchronous()
        self.stats['xscale_generate']=time.time()-t0

        with open(self.log_file_path, 'w') as f:
            json.dump(self.stats, f)

        if self.xscale_generate.isFailure():
            EDVerbose.ERROR('xscale generation failed')
            log_to_ispyb([self.integration_id_anom, self.integration_id_noanom],
                         'Scaling',
                         'Failed',
                         'xscale generation failed in {0}s'.format(self.stats['xscale_generate']))
            return
        else:
            EDVerbose.screen('xscale anom/merge generation finished')
            log_to_ispyb([self.integration_id_anom, self.integration_id_noanom],
                         'Scaling',
                         'Successful',
                         'xscale generation finished in {0}s'.format(self.stats['xscale_generate']))

        # Copy the generated files to the results dir
        attrs = ['lp_anom_merged', 'lp_noanom_merged',
                 'lp_anom_unmerged', 'lp_noanom_unmerged']
        xscale_logs = [getattr(self.xscale_generate.dataOutput, attr)
                       for attr in attrs]
        xscale_logs = [log.value for log in xscale_logs if log is not None]
        for log in xscale_logs:
            target = os.path.join(self.results_dir,
                                  '_'.join([self.image_prefix, os.path.basename(log)]))
            try:
                shutil.copyfile(log, target)
            except IOError:
                self.ERROR('Could not copy {0} to {1}'.format(log, target))



        import_in = XSDataAutoprocImport()
        import_in.input_anom = self.xscale_generate.dataOutput.hkl_anom_unmerged
        import_in.input_noanom = self.xscale_generate.dataOutput.hkl_noanom_unmerged
        import_in.dataCollectionID = self.dataInput.data_collection_id
        import_in.start_image = XSDataInteger(self.data_range[0])
        import_in.end_image = XSDataInteger(self.data_range[1])

        # XXX: is this the right place to get the res from?
        import_in.res = self.res_cutoff_anom.dataOutput.res

        # XXX: This is optional but seems required by aimless
        import_in.nres = self.dataInput.nres

        import_in.output_directory = XSDataString(self.results_dir)

        try:
            import_in.image_prefix = XSDataString(self.image_prefix)
        except:
            self.DEBUG('could not determine image prefix from directory "{0}"'.format(self.root_dir))

        self.file_conversion.dataInput = import_in

        t0 = time.time()
        self.file_conversion.executeSynchronous()
        self.stats['autoproc_import']=time.time()-t0

        with open(self.log_file_path, 'w') as f:
            json.dump(self.stats, f)

        if self.file_conversion.isFailure():
            EDVerbose.ERROR("file import failed")


        self.custom_stats['total_time']=time.time() - process_start
        try:
            autoproclog.log(**self.custom_stats)
        except Exception, e:
            EDVerbose.screen('could not logs stats to custom log server')
            EDVerbose.screen(traceback.format_exc())


        # Now onto DIMPLE

        # create a startup script
        # This is ugly
        script_template = '''#!/bin/sh

if [ $# -eq 1 ]; then
        ssh mxnice /scisoft/bin/cctbx_python_debian6.sh /scisoft/bin/run-dimple-autoproc.py {root_dir} `readlink -f "$1"`;
else
        ssh mxnice /scisoft/bin/cctbx_python_debian6.sh /scisoft/bin/run-dimple-autoproc.py {root_dir} {dcid}
fi
'''
        dimple_script = script_template.format(dcid=self.dataInput.data_collection_id.value,
                                               root_dir=self.root_dir)
        script_path = os.path.join(self.root_dir, 'dimple.sh')
        with open(script_path, 'w') as f:
            f.write(dimple_script)
        os.chmod(script_path, S_IRUSR|S_IWUSR|S_IRGRP|S_IROTH|S_IXUSR|S_IXGRP|S_IXOTH)


        # we need a PDB file either in ispyb or in the image directory
        c = suds.client.Client(WS_URL, username=self.ispyb_user, password=self.ispyb_password)
        pdb_file = c.service.getPdbFilePath(self.dataInput.data_collection_id.value)
        if pdb_file is None:
            EDVerbose.screen('No pdb file in ispyb, trying the toplevel dir {0}'.format(self.root_dir))
        for f in os.listdir(self.root_dir):
            if f.endswith('.pdb'):
                pdb_file = os.path.join(self.root_dir, f)
                break

        # We need these 2 variables for the coot script below
        dimple_out = os.path.join(self.results_dir, '{0}_dimple_out.pdb'.format(self.image_prefix))
        dimple_mtzout = os.path.join(self.results_dir, '{0}_dimple_out.mtz'.format(self.image_prefix))

        # To indicate if dimple ran successfully. Perhaps there's a
        # way to do it with edplugin's various isStarted, isFailure,
        # isWhatever
        dimple_did_run = False

        if pdb_file is None:
            EDVerbose.WARNING('No pdb file found, not running dimple')
        else:
            EDVerbose.screen('Using pdb file {0}'.format(pdb_file))
            dimple_in = CCP4DataInputControlPipelineCalcDiffMap()
            dimple_in.XYZIN = XYZ(path=XSDataString(pdb_file))

            # We'll put the results in the results directory as well

            dimple_in.XYZOUT = XYZ(path=XSDataString(dimple_out))

            labels = CCP4MTZColLabels()
            labels.F = XSDataString('F_xdsproc')
            labels.SIGF = XSDataString('SIGF_xdsproc')
            labels.IMEAN = XSDataString('IMEAN')
            labels.SIGIMEAN = XSDataString('SIGIMEAN')
            dimple_in.ColLabels = labels

            # For now the import plugin does no give information about
            # the paths to the various files it generates so we look
            # into the results directory for the right mtz file
            mtz_file = None
            for f in os.listdir(self.results_dir):
                if f.endswith('anom_aimless.mtz'):
                    mtz_file = os.path.join(self.results_dir, f)
                    break


            if mtz_file is None:
                EDVerbose.ERROR('No suitable input mtz found for dimple, not running it')
            else:
                dimple_in.HKLIN = HKL(path=XSDataString(mtz_file))
                dimple_log = os.path.join(self.results_dir, '{0}_dimple.log'.format(self.image_prefix))
                dimple_in.outputLogFile = CCP4LogFile(path=XSDataString(dimple_log))
                dimple_in.HKLOUT = HKL(path=XSDataString(dimple_mtzout))
                self.dimple.dataInput = dimple_in
                self.dimple.executeSynchronous()
                if not self.dimple.isFailure():
                    dimple_did_run = True

        # Now create a coot startup file, only if dimple ran successfully
        if dimple_did_run:
            coot_script = """#!/bin/sh
if [ ! -e {mtz} ] || [ ! -e {pdb} ]; then
        echo Either {mtz} or {pdb} is missing
        echo Did dimple run?
        exit 1
else
        echo Let\\'s run coot
        coot --pdb {pdb} --auto {mtz} --python -c 'difference_map_peaks(2,0,5,5,1,1)'
fi
""".format(pdb=os.path.basename(dimple_out),
           mtz=os.path.basename(dimple_mtzout))

            script_path = os.path.join(self.results_dir, 'coot.sh')
            with open(script_path, 'w') as f:
                f.write(coot_script)
            os.chmod(script_path, S_IRUSR|S_IWUSR|S_IRGRP|S_IROTH|S_IXUSR|S_IXGRP|S_IXOTH)



    def postProcess(self, _edObject = None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlAutoproc.postProcess")

        # Create a file in the results directory to indicate all files have been
        # populated in it already so Max's code can be aware of that
        try:
            os.mknod(os.path.join(self.results_dir, '.finished'), 0755)
        except OSError: # file exists
            pass


        #Now that we have executed the whole thing we need to create
        #the suitable ISPyB plugin input and serialize it to the file
        #we've been given as input
        output = AutoProcContainer()

        # AutoProc attr
        autoproc = AutoProc()

        # There's also
        pointless_sg_str = self.file_conversion.dataOutput.pointless_sgstring
        if pointless_sg_str is not None:
            autoproc.spaceGroup = pointless_sg_str.value

        xdsout = self.xds_first.dataOutput

        # The unit cell will be taken from the no anom aimless run below

        output.AutoProc = autoproc

        # NOANOM PATH

        # scaling container and all the things that go in
        scaling_container_noanom = AutoProcScalingContainer()
        scaling = AutoProcScaling()
        scaling.recordTimeStamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        scaling_container_noanom.AutoProcScaling = scaling

        inner, outer, overall, unit_cell = _parse_aimless(self.file_conversion.dataOutput.aimless_log_noanom.value)

        autoproc.refinedCell_a = str(unit_cell[0])
        autoproc.refinedCell_b = str(unit_cell[1])
        autoproc.refinedCell_c = str(unit_cell[2])
        autoproc.refinedCell_alpha = str(unit_cell[3])
        autoproc.refinedCell_beta = str(unit_cell[4])
        autoproc.refinedCell_gamma = str(unit_cell[5])

        inner_stats = AutoProcScalingStatistics()
        for k, v in inner.iteritems():
            setattr(inner_stats, k, v)
        scaling_container_noanom.AutoProcScalingStatistics.append(inner_stats)

        outer_stats = AutoProcScalingStatistics()
        for k, v in outer.iteritems():
            setattr(outer_stats, k, v)
        scaling_container_noanom.AutoProcScalingStatistics.append(outer_stats)

        overall_stats = AutoProcScalingStatistics()
        for k, v in overall.iteritems():
            setattr(overall_stats, k, v)
        scaling_container_noanom.AutoProcScalingStatistics.append(overall_stats)

        integration_container_noanom = AutoProcIntegrationContainer()
        image = Image()
        image.dataCollectionId = self.dataInput.data_collection_id.value
        integration_container_noanom.Image = image

        integration_noanom = AutoProcIntegration()
        if self.integration_id_noanom is not None:
            integration_noanom.autoProcIntegrationId = self.integration_id_noanom
        integration_noanom.cell_a = unit_cell[0]
        integration_noanom.cell_b = unit_cell[1]
        integration_noanom.cell_c = unit_cell[2]
        integration_noanom.cell_alpha = unit_cell[3]
        integration_noanom.cell_beta = unit_cell[4]
        integration_noanom.cell_gamma = unit_cell[5]
        integration_noanom.anomalous = 0

        # done with the integration
        integration_container_noanom.AutoProcIntegration = integration_noanom
        scaling_container_noanom.AutoProcIntegrationContainer = integration_container_noanom

        # ANOM PATH
        scaling_container_anom = AutoProcScalingContainer()

        inner, outer, overall, unit_cell = _parse_aimless(self.file_conversion.dataOutput.aimless_log_anom.value)
        inner_stats = AutoProcScalingStatistics()
        for k, v in inner.iteritems():
            setattr(inner_stats, k, v)
        scaling_container_anom.AutoProcScalingStatistics.append(inner_stats)

        outer_stats = AutoProcScalingStatistics()
        for k, v in outer.iteritems():
            setattr(outer_stats, k, v)
        scaling_container_anom.AutoProcScalingStatistics.append(outer_stats)

        overall_stats = AutoProcScalingStatistics()
        for k, v in overall.iteritems():
            setattr(overall_stats, k, v)
        scaling_container_anom.AutoProcScalingStatistics.append(overall_stats)



        scaling = AutoProcScaling()
        scaling.recordTimeStamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        scaling_container_anom.AutoProcScaling = scaling

        xscale_stats_anom = self.xscale_generate.dataOutput.stats_anom_merged
        inner_stats_anom = xscale_stats_anom.completeness_entries[0]
        outer_stats_anom = xscale_stats_anom.completeness_entries[-1]

        # use the previous shell's res as low res if available
        prev_res = self.low_resolution_limit
        try:
            prev_res = xscale_stats_anom.completeness_entries[-2].res.value
        except IndexError:
            pass
        total_stats_anom = xscale_stats_anom.total_completeness

        stats = _create_scaling_stats(inner_stats_anom, 'innerShell',
                                      self.low_resolution_limit, True)
        overall_low = stats.resolutionLimitLow
        scaling_container_anom.AutoProcScalingStatistics.append(stats)

        stats = _create_scaling_stats(outer_stats_anom, 'outerShell',
                                      prev_res, True)
        overall_high = stats.resolutionLimitHigh
        scaling_container_anom.AutoProcScalingStatistics.append(stats)
        stats = _create_scaling_stats(total_stats_anom, 'overall',
                                      self.low_resolution_limit, True)
        stats.resolutionLimitLow = overall_low
        stats.resolutionLimitHigh = overall_high
        scaling_container_anom.AutoProcScalingStatistics.append(stats)


        integration_container_anom = AutoProcIntegrationContainer()
        image = Image()
        image.dataCollectionId = self.dataInput.data_collection_id.value
        integration_container_anom.Image = image

        integration_anom = AutoProcIntegration()
        crystal_stats =  self.parse_xds_anom.dataOutput
        if self.integration_id_anom is not None:
            integration_anom.autoProcIntegrationId = self.integration_id_anom
        integration_anom.cell_a = unit_cell[0]
        integration_anom.cell_b = unit_cell[1]
        integration_anom.cell_c = unit_cell[2]
        integration_anom.cell_alpha = unit_cell[3]
        integration_anom.cell_beta = unit_cell[4]
        integration_anom.cell_gamma = unit_cell[5]
        integration_anom.anomalous = 1

        # done with the integration
        integration_container_anom.AutoProcIntegration = integration_anom
        scaling_container_anom.AutoProcIntegrationContainer = integration_container_anom


        # ------ NO ANOM / ANOM end

        program_container = AutoProcProgramContainer()
        program_container.AutoProcProgram = AutoProcProgram()
        program_container.AutoProcProgram.processingCommandLine = ' '.join(sys.argv)
        program_container.AutoProcProgram.processingPrograms = 'EDNAproc'

        # now for the generated files. There's some magic to do with
        # their paths to determine where to put them on pyarch
        pyarch_path = None
        # Note: the path is in the form /data/whatever

        # remove the edna-autoproc-import suffix
        original_files_dir = self.file_conversion.dataInput.output_directory.value
        #files_dir, _ = os.path.split(original_files_dir)
        files_dir = original_files_dir

        # the whole transformation is fragile!
        if files_dir.startswith('/data/visitor'):
            # We might get empty elements at the head/tail of the list
            tokens = [elem for elem in files_dir.split(os.path.sep)
                      if len(elem) > 0]
            pyarch_path = os.path.join('/data/pyarch',
                                       tokens[3], tokens[2],
                                       *tokens[4:])
        else:
            # We might get empty elements at the head/tail of the list
            tokens = [elem for elem in files_dir.split(os.path.sep)
                      if len(elem) > 0]
            if tokens[2] == 'inhouse':
                pyarch_path = os.path.join('/data/pyarch', tokens[1],
                                           *tokens[3:])
        if pyarch_path is not None:
            pyarch_path = pyarch_path.replace('PROCESSED_DATA', 'RAW_DATA')
            try:
                os.makedirs(pyarch_path)
            except OSError:
                # dir already exists, may happen when testing
                EDVerbose.screen('Target directory on pyarch ({0}) already exists, ignoring'.format(pyarch_path))

            file_list = []
            # we can now copy the files to this dir
            for f in os.listdir(original_files_dir):
                current = os.path.join(original_files_dir, f)
                if not os.path.isfile(current):
                    continue
                if not os.path.splitext(current)[1].lower() in ISPYB_UPLOAD_EXTENSIONS:
                    continue
                new_path = os.path.join(pyarch_path, f)
                file_list.append(new_path)
                shutil.copyfile(current,
                                new_path)
            # now add those to the ispyb upload
            for path in file_list:
                dirname, filename = os.path.split(path)
                attach = AutoProcProgramAttachment()
                attach.fileType = "Result"
                attach.fileName = filename
                attach.filePath = dirname
                program_container.AutoProcProgramAttachment.append(attach)


        program_container.AutoProcProgram.processingStatus = True
        output.AutoProcProgramContainer = program_container

        # first with anom

        output.AutoProcScalingContainer = scaling_container_anom

        ispyb_input = XSDataInputStoreAutoProc()
        ispyb_input.AutoProcContainer = output


        with open(self.dataInput.output_file.path.value, 'w') as f:
            f.write(ispyb_input.marshal())

        # store results in ispyb
        self.store_autoproc_anom.dataInput = ispyb_input
        t0=time.time()
        self.store_autoproc_anom.executeSynchronous()
        self.stats['ispyb_upload'] = time.time() - t0

        with open(self.log_file_path, 'w') as f:
            json.dump(self.stats, f)

        if self.store_autoproc_anom.isFailure():
            self.ERROR('could not send results to ispyb')
        else:
            # store the autoproc ID as a filename in the
            # fastproc_integration_ids directory
            os.mknod(os.path.join(self.autoproc_ids_dir, str(self.integration_id_anom)), 0755)
        # then noanom stats

        output.AutoProcScalingContainer = scaling_container_noanom

        ispyb_input = XSDataInputStoreAutoProc()
        ispyb_input.AutoProcContainer = output


        with open(self.dataInput.output_file.path.value, 'w') as f:
            f.write(ispyb_input.marshal())

        # store results in ispyb
        self.store_autoproc_noanom.dataInput = ispyb_input
        t0=time.time()
        self.store_autoproc_noanom.executeSynchronous()
        self.stats['ispyb_upload'] = time.time() - t0

        with open(self.log_file_path, 'w') as f:
            json.dump(self.stats, f)

        if self.store_autoproc_noanom.isFailure():
            self.ERROR('could not send results to ispyb')
        else:
            # store the autoproc id
            os.mknod(os.path.join(self.autoproc_ids_dir, str(self.integration_id_noanom)), 0755)

# Proxy since the API changed and we can now log to several ids
def log_to_ispyb(integration_id, step, status, comments=""):
    if type(integration_id) is list:
        for item in integration_id:
            log_to_ispyb_impl(item, step, status, comments)
    else:
        log_to_ispyb_impl(integration_id, step, status, comments)

def log_to_ispyb_impl(integration_id, step, status, comments=""):
    # hack in the event we could not create an integration ID
    if integration_id is None:
        EDVerbose.ERROR('could not log to ispyb: no integration id')
        return
    autoproc_status = edFactoryPlugin.loadPlugin('EDPluginISPyBStoreAutoProcStatusv1_4')
    status_input = XSDataInputStoreAutoProcStatus()
    status_input.autoProcIntegrationId = integration_id
    status_data = AutoProcStatus()
    status_data.step = step
    status_data.status = status
    status_data.comments = comments
    status_input.AutoProcStatus = status_data

    autoproc_status.dataInput = status_input

    autoproc_status.executeSynchronous()

def create_integration_id(datacollect_id):
    autoproc_status = edFactoryPlugin.loadPlugin('EDPluginISPyBStoreAutoProcStatusv1_4')
    status_input = XSDataInputStoreAutoProcStatus()
    status_input.dataCollectionId = datacollect_id

    # needed even if we only want to get an integration ID?
    status_data = AutoProcStatus()
    status_data.step = "Indexing"
    status_data.status = "Launched"
    status_data.comments = "Getting integration ID"
    status_input.AutoProcStatus = status_data

    autoproc_status.dataInput = status_input
    # get our autoproc status id
    autoproc_status.executeSynchronous()
    return autoproc_status.dataOutput.autoProcIntegrationId

def _create_scaling_stats(xscale_stats, stats_type, lowres, anom):
    stats = AutoProcScalingStatistics()
    stats.scalingStatisticsType = stats_type
    stats.resolutionLimitLow = lowres
    if stats_type != 'overall':
        stats.resolutionLimitHigh = xscale_stats.res.value
    stats.meanIOverSigI = xscale_stats.isig.value
    stats.completeness = xscale_stats.complete.value
    stats.multiplicity = xscale_stats.multiplicity.value
    # The ispyb plugin DOES NOT convert to the right data types. This
    # happens to be an integer on the ispyb side
    stats.nTotalObservations = int(xscale_stats.observed.value)
    stats.rMerge = xscale_stats.rfactor.value
    stats.anomalous = anom

    return stats



# copy/pasted from another plugin
def _template_to_image(fmt, num):
    # for simplicity we will assume the template to contain only one
    # sequence of '?' characters. max's code uses a regexp so this
    # further restrict the possible templates.
    start = fmt.find('?')
    end = fmt.rfind('?')
    if start == -1 or end == -1:
        # the caller test for the file existence and an empty path
        # does not exist
        return ''
    prefix = fmt[:start]
    suffix = fmt[end+1:]
    length = end - start + 1

    # this is essentially the python format string equivalent to the
    # template string
    fmt_string = prefix + '{0:0' + str(length) + 'd}' + suffix

    return fmt_string.format(num)


# mapping between the start of the line and the name of the property
# in the ispyb data object thing
INTERESTING_LINES = {
    'Low resolution limit': 'resolutionLimitLow',
    'High resolution limit': 'resolutionLimitHigh',
    'Mean((I)/sd(I))': 'meanIOverSigI',
    'Completeness': 'completeness',
    'Multiplicity': 'multiplicity',
    'Total number of observations': 'nTotalObservations',
    'Rmerge  (within I+/I-)': 'rMerge'
}

UNIT_CELL_PREFIX = 'Average unit cell:' # special case, 6 values

def _parse_aimless(filepath):
    lines = []
    inner_stats = {'scalingStatisticsType':'innerShell'}
    outer_stats = {'scalingStatisticsType':'outerShell'}
    overall_stats = {'scalingStatisticsType':'overall'}
    unit_cell = None
    with open(filepath, 'r') as f:
        lines = f.readlines()
    started = False
    for line in lines:
        # avoid all the stuff before the final summary
        if line.startswith('<!--SUMMARY_BEGIN--> $TEXT:Result: $$ $$'):
            started = True
        if started:
            for prefix, prop_name in INTERESTING_LINES.iteritems():
                if line.startswith(prefix):
                    # We need to multiply the values for rMerge by 100
                    factor = 100 if prop_name == 'rMerge' else 1
                    # 3 last columns are the values we're after
                    overall, inner, outer = [float(x) * factor for x in line.split()[-3:]]
                    overall_stats[prop_name] = overall
                    inner_stats[prop_name] = inner
                    outer_stats[prop_name] = outer
            if line.startswith(UNIT_CELL_PREFIX):
                unit_cell = map(float, line.split()[-6:])
    return inner_stats, outer_stats, overall_stats, unit_cell


# taken straight from max's code
SPACE_GROUP_NAMES = {
    1: ' P 1 ',
    2: ' P -1 ',
    3: ' P 1 2 1 ',
    4: ' P 1 21 1 ',
    5: ' C 1 2 1 ',
    6: ' P 1 m 1 ',
    7: ' P 1 c 1 ',
    8: ' C 1 m 1 ',
    9: ' C 1 c 1 ',
    10: ' P 1 2/m 1 ',
    11: ' P 1 21/m 1 ',
    12: ' C 1 2/m 1 ',
    13: ' P 1 2/c 1 ',
    14: ' P 1 21/c 1 ',
    15: ' C 1 2/c 1 ',
    16: ' P 2 2 2 ',
    17: ' P 2 2 21 ',
    18: ' P 21 21 2 ',
    19: ' P 21 21 21 ',
    20: ' C 2 2 21 ',
    21: ' C 2 2 2 ',
    22: ' F 2 2 2 ',
    23: ' I 2 2 2 ',
    24: ' I 21 21 21 ',
    25: ' P m m 2 ',
    26: ' P m c 21 ',
    27: ' P c c 2 ',
    28: ' P m a 2 ',
    29: ' P c a 21 ',
    30: ' P n c 2 ',
    31: ' P m n 21 ',
    32: ' P b a 2 ',
    33: ' P n a 21 ',
    34: ' P n n 2 ',
    35: ' C m m 2 ',
    36: ' C m c 21 ',
    37: ' C c c 2 ',
    38: ' A m m 2 ',
    39: ' A b m 2 ',
    40: ' A m a 2 ',
    41: ' A b a 2 ',
    42: ' F m m 2 ',
    43: ' F d d 2 ',
    44: ' I m m 2 ',
    45: ' I b a 2 ',
    46: ' I m a 2 ',
    47: ' P m m m ',
    48: ' P n n n ',
    49: ' P c c m ',
    50: ' P b a n ',
    51: ' P m m a1 ',
    52: ' P n n a1 ',
    53: ' P m n a1 ',
    54: ' P c c a1 ',
    55: ' P b a m1 ',
    56: ' P c c n1 ',
    57: ' P b c m1 ',
    58: ' P n n m1 ',
    59: ' P m m n1 ',
    60: ' P b c n1 ',
    61: ' P b c a1 ',
    62: ' P n m a1 ',
    63: ' C m c m1 ',
    64: ' C m c a1 ',
    65: ' C m m m ',
    66: ' C c c m ',
    67: ' C m m a ',
    68: ' C c c a ',
    69: ' F m m m ',
    70: ' F d d d ',
    71: ' I m m m ',
    72: ' I b a m ',
    73: ' I b c a1 ',
    74: ' I m m a1 ',
    75: ' P 4 ',
    76: ' P 41 ',
    77: ' P 42 ',
    78: ' P 43 ',
    79: ' I 4 ',
    80: ' I 41 ',
    81: ' P -4 ',
    82: ' I -4 ',
    83: ' P 4/m ',
    84: ' P 42/m ',
    85: ' P 4/n ',
    86: ' P 42/n ',
    87: ' I 4/m ',
    88: ' I 41/a ',
    89: ' P 4 2 2 ',
    90: ' P 4 21 2 ',
    91: ' P 41 2 2 ',
    92: ' P 41 21 2 ',
    93: ' P 42 2 2 ',
    94: ' P 42 21 2 ',
    95: ' P 43 2 2 ',
    96: ' P 43 21 2 ',
    97: ' I 4 2 2 ',
    98: ' I 41 2 2 ',
    99: ' P 4 m m ',
    100: ' P 4 b m ',
    101: ' P 42 c m ',
    102: ' P 42 n m ',
    103: ' P 4 c c ',
    104: ' P 4 n c ',
    105: ' P 42 m c ',
    106: ' P 42 b c ',
    107: ' I 4 m m ',
    108: ' I 4 c m ',
    109: ' I 41 m d ',
    110: ' I 41 c d ',
    111: ' P -4 2 m ',
    112: ' P -4 2 c ',
    113: ' P -4 21 m ',
    114: ' P -4 21 c ',
    115: ' P -4 m 2 ',
    116: ' P -4 c 2 ',
    117: ' P -4 b 2 ',
    118: ' P -4 n 2 ',
    119: ' I -4 m 2 ',
    120: ' I -4 c 2 ',
    121: ' I -4 2 m ',
    122: ' I -4 2 d ',
    123: ' P 4/m m m ',
    124: ' P 4/m c c ',
    125: ' P 4/n b m ',
    126: ' P 4/n n c ',
    127: ' P 4/m b m1 ',
    128: ' P 4/m n c1 ',
    129: ' P 4/n m m1 ',
    130: ' P 4/n c c1 ',
    131: ' P 42/m m c ',
    132: ' P 42/m c m ',
    133: ' P 42/n b c ',
    134: ' P 42/n n m ',
    135: ' P 42/m b c ',
    136: ' P 42/m n m ',
    137: ' P 42/n m c ',
    138: ' P 42/n c m ',
    139: ' I 4/m m m ',
    140: ' I 4/m c m ',
    141: ' I 41/a m d ',
    142: ' I 41/a c d ',
    143: ' P 3 ',
    144: ' P 31 ',
    145: ' P 32 ',
    146: ' H 3 ',
    147: ' P -3 ',
    148: ' H -3 ',
    149: ' P 3 1 2 ',
    150: ' P 3 2 1 ',
    151: ' P 31 1 2 ',
    152: ' P 31 2 1 ',
    153: ' P 32 1 2 ',
    154: ' P 32 2 1 ',
    155: ' H 3 2 ',
    156: ' P 3 m 1 ',
    157: ' P 3 1 m ',
    158: ' P 3 c 1 ',
    159: ' P 3 1 c ',
    160: ' H 3 m ',
    161: ' H 3 c ',
    162: ' P -3 1 m ',
    163: ' P -3 1 c ',
    164: ' P -3 m 1 ',
    165: ' P -3 c 1 ',
    166: ' H -3 m ',
    167: ' H -3 c ',
    168: ' P 6 ',
    169: ' P 61 ',
    170: ' P 65 ',
    171: ' P 62 ',
    172: ' P 64 ',
    173: ' P 63 ',
    174: ' P -6 ',
    175: ' P 6/m ',
    176: ' P 63/m ',
    177: ' P 6 2 2 ',
    178: ' P 61 2 2 ',
    179: ' P 65 2 2 ',
    180: ' P 62 2 2 ',
    181: ' P 64 2 2 ',
    182: ' P 63 2 2 ',
    183: ' P 6 m m ',
    184: ' P 6 c c ',
    185: ' P 63 c m ',
    186: ' P 63 m c ',
    187: ' P -6 m 2 ',
    188: ' P -6 c 2 ',
    189: ' P -6 2 m ',
    190: ' P -6 2 c ',
    191: ' P 6/m m m ',
    192: ' P 6/m c c ',
    193: ' P 63/m c m ',
    194: ' P 63/m m c ',
    195: ' P 2 3 ',
    196: ' F 2 3 ',
    197: ' I 2 3 ',
    198: ' P 21 3 ',
    199: ' I 21 3 ',
    200: ' P m -3 ',
    201: ' P n -3 ',
    202: ' F m -3 ',
    203: ' F d -3 ',
    204: ' I m -3 ',
    205: ' P a -31 ',
    206: ' I a -31 ',
    207: ' P 4 3 2 ',
    208: ' P 42 3 2 ',
    209: ' F 4 3 2 ',
    210: ' F 41 3 2 ',
    211: ' I 4 3 2 ',
    212: ' P 43 3 2 ',
    213: ' P 41 3 2 ',
    214: ' I 41 3 2 ',
    215: ' P -4 3 m ',
    216: ' F -4 3 m ',
    217: ' I -4 3 m ',
    218: ' P -4 3 n ',
    219: ' F -4 3 c ',
    220: ' I -4 3 d ',
    221: ' P m -3 m ',
    222: ' P n -3 n ',
    223: ' P m -3 n1 ',
    224: ' P n -3 m1 ',
    225: ' F m -3 m ',
    226: ' F m -3 c ',
    227: ' F d -3 m1 ',
    228: ' F d -3 c1 ',
    229: ' I m -3 m ',
    230: ' I a -3 d1 ',
}


SPACE_GROUP_NUMBERS = {
    'P1':1,
    'P-1':2,
    'P121':3,
    'P1211':4,
    'C121':5,
    'P1M1':6,
    'P1C1':7,
    'C1M1':8,
    'C1C1':9,
    'P12/M1':10,
    'P121/M1':11,
    'C12/M1':12,
    'P12/C1':13,
    'P121/C1':14,
    'C12/C1':15,
    'P222':16,
    'P2221':17,
    'P21212':18,
    'P212121':19,
    'C2221':20,
    'C222':21,
    'F222':22,
    'I222':23,
    'I212121':24,
    'PMM2':25,
    'PMC21':26,
    'PCC2':27,
    'PMA2':28,
    'PCA21':29,
    'PNC2':30,
    'PMN21':31,
    'PBA2':32,
    'PNA21':33,
    'PNN2':34,
    'CMM2':35,
    'CMC21':36,
    'CCC2':37,
    'AMM2':38,
    'ABM2':39,
    'AMA2':40,
    'ABA2':41,
    'FMM2':42,
    'FDD2':43,
    'IMM2':44,
    'IBA2':45,
    'IMA2':46,
    'PMMM':47,
    'PNNN':48,
    'PCCM':49,
    'PBAN':50,
    'PMMA1':51,
    'PNNA1':52,
    'PMNA1':53,
    'PCCA1':54,
    'PBAM1':55,
    'PCCN1':56,
    'PBCM1':57,
    'PNNM1':58,
    'PMMN1':59,
    'PBCN1':60,
    'PBCA1':61,
    'PNMA1':62,
    'CMCM1':63,
    'CMCA1':64,
    'CMMM':65,
    'CCCM':66,
    'CMMA':67,
    'CCCA':68,
    'FMMM':69,
    'FDDD':70,
    'IMMM':71,
    'IBAM':72,
    'IBCA1':73,
    'IMMA1':74,
    'P4':75,
    'P41':76,
    'P42':77,
    'P43':78,
    'I4':79,
    'I41':80,
    'P-4':81,
    'I-4':82,
    'P4/M':83,
    'P42/M':84,
    'P4/N':85,
    'P42/N':86,
    'I4/M':87,
    'I41/A':88,
    'P422':89,
    'P4212':90,
    'P4122':91,
    'P41212':92,
    'P4222':93,
    'P42212':94,
    'P4322':95,
    'P43212':96,
    'I422':97,
    'I4122':98,
    'P4MM':99,
    'P4BM':100,
    'P42CM':101,
    'P42NM':102,
    'P4CC':103,
    'P4NC':104,
    'P42MC':105,
    'P42BC':106,
    'I4MM':107,
    'I4CM':108,
    'I41MD':109,
    'I41CD':110,
    'P-42M':111,
    'P-42C':112,
    'P-421M':113,
    'P-421C':114,
    'P-4M2':115,
    'P-4C2':116,
    'P-4B2':117,
    'P-4N2':118,
    'I-4M2':119,
    'I-4C2':120,
    'I-42M':121,
    'I-42D':122,
    'P4/MMM':123,
    'P4/MCC':124,
    'P4/NBM':125,
    'P4/NNC':126,
    'P4/MBM1':127,
    'P4/MNC1':128,
    'P4/NMM1':129,
    'P4/NCC1':130,
    'P42/MMC':131,
    'P42/MCM':132,
    'P42/NBC':133,
    'P42/NNM':134,
    'P42/MBC':135,
    'P42/MNM':136,
    'P42/NMC':137,
    'P42/NCM':138,
    'I4/MMM':139,
    'I4/MCM':140,
    'I41/AMD':141,
    'I41/ACD':142,
    'P3':143,
    'P31':144,
    'P32':145,
    'H3':146,
    'P-3':147,
    'H-3':148,
    'P312':149,
    'P321':150,
    'P3112':151,
    'P3121':152,
    'P3212':153,
    'P3221':154,
    'H32':155,
    'P3M1':156,
    'P31M':157,
    'P3C1':158,
    'P31C':159,
    'H3M':160,
    'H3C':161,
    'P-31M':162,
    'P-31C':163,
    'P-3M1':164,
    'P-3C1':165,
    'H-3M':166,
    'H-3C':167,
    'P6':168,
    'P61':169,
    'P65':170,
    'P62':171,
    'P64':172,
    'P63':173,
    'P-6':174,
    'P6/M':175,
    'P63/M':176,
    'P622':177,
    'P6122':178,
    'P6522':179,
    'P6222':180,
    'P6422':181,
    'P6322':182,
    'P6MM':183,
    'P6CC':184,
    'P63CM':185,
    'P63MC':186,
    'P-6M2':187,
    'P-6C2':188,
    'P-62M':189,
    'P-62C':190,
    'P6/MMM':191,
    'P6/MCC':192,
    'P63/MCM':193,
    'P63/MMC':194,
    'P23':195,
    'F23':196,
    'I23':197,
    'P213':198,
    'I213':199,
    'PM-3':200,
    'PN-3':201,
    'FM-3':202,
    'FD-3':203,
    'IM-3':204,
    'PA-31':205,
    'IA-31':206,
    'P432':207,
    'P4232':208,
    'F432':209,
    'F4132':210,
    'I432':211,
    'P4332':212,
    'P4132':213,
    'I4132':214,
    'P-43M':215,
    'F-43M':216,
    'I-43M':217,
    'P-43N':218,
    'F-43C':219,
    'I-43D':220,
    'PM-3M':221,
    'PN-3N':222,
    'PM-3N1':223,
    'PN-3M1':224,
    'FM-3M':225,
    'FM-3C':226,
    'FD-3M1':227,
    'FD-3C1':228,
    'IM-3M':229,
    'IA-3D1':230,
}
