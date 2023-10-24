# coding: utf8
#
#    Project: EDNAproc
#             http://www.edna-site.org
#
#    Copyright (C) ESRF
#
#    Principal authors: Thomas Boeglin and Olof Svensson
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

__authors__ = ["Thomas Boeglin", "Olof Svensson"]
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import smtplib

WS_URL = "https://ispyb.esrf.fr/ispyb-ws/ispybWS/ToolsForCollectionWebService?wsdl"

import os
import sys
import time
import shutil
import socket
import traceback
import subprocess

from EDPluginControl import EDPluginControl
from EDVerbose import EDVerbose

from EDFactoryPlugin import edFactoryPlugin
from EDUtilsPath import EDUtilsPath
from EDUtilsICAT import EDUtilsICAT

from EDHandlerXSDataISPyBv1_4 import EDHandlerXSDataISPyBv1_4

from EDHandlerESRFPyarchv1_0 import EDHandlerESRFPyarchv1_0

from XSDataCommon import XSDataFile, XSDataBoolean, XSDataString
from XSDataCommon import XSDataInteger, XSDataTime, XSDataDouble

from XSDataEDNAprocv1_0 import XSDataEDNAprocInput
from XSDataEDNAprocv1_0 import XSDataEDNAprocImport
from XSDataEDNAprocv1_0 import XSDataInputControlDimple

edFactoryPlugin.loadModule("XSDataXDSv1_0")

from XSDataXDSv1_0 import XSDataResCutoff
from XSDataXDSv1_0 import XSDataMinimalXdsIn
from XSDataXDSv1_0 import XSDataXdsGenerateInput
from XSDataXDSv1_0 import XSDataXdsOutputFile
from XSDataXDSv1_0 import XSDataXscaleInput
from XSDataXDSv1_0 import XSDataXscaleInputFile

edFactoryPlugin.loadModule("XSDataISPyBv1_4")
# plugin input/output
from XSDataISPyBv1_4 import XSDataInputStoreAutoProc
from XSDataISPyBv1_4 import XSDataResultStoreAutoProc

# dimple stuff

# this depends on the CCTBX modules so perhaps we could make running
# dimple dependent on whether those are installed or not
# edFactoryPlugin.loadModule('XSDataCCP4DIMPLE')
# from XSDataCCP4DIMPLE import CCP4DataInputControlPipelineCalcDiffMap
# from XSDataCCP4DIMPLE import HKL, XYZ, CCP4MTZColLabels, CCP4LogFile

# edFactoryPlugin.loadModule('EDPluginControlDIMPLEPipelineCalcDiffMapv10.py')

# what actually goes inside
from XSDataISPyBv1_4 import Image
from XSDataISPyBv1_4 import AutoProc
from XSDataISPyBv1_4 import AutoProcScaling
from XSDataISPyBv1_4 import AutoProcContainer
from XSDataISPyBv1_4 import AutoProcIntegration
from XSDataISPyBv1_4 import AutoProcProgramContainer
from XSDataISPyBv1_4 import AutoProcScalingContainer
from XSDataISPyBv1_4 import AutoProcScalingStatistics
from XSDataISPyBv1_4 import AutoProcProgramAttachment
from XSDataISPyBv1_4 import AutoProcIntegrationContainer

# add comments to data collection and data collection group
from XSDataISPyBv1_4 import XSDataInputISPyBUpdateDataCollectionGroupComment

# status updates
from XSDataISPyBv1_4 import AutoProcStatus
from XSDataISPyBv1_4 import XSDataInputStoreAutoProcStatus


edFactoryPlugin.loadModule("XSDataMXWaitFilev1_1")
from XSDataMXWaitFilev1_1 import XSDataInputMXWaitFile

edFactoryPlugin.loadModule("XSDataPhenixv1_1")
from XSDataPhenixv1_1 import XSDataInputPhenixXtriage

from xdscfgparser import parse_xds_file, dump_xds_file

# import autoproclog
# autoproclog.LOG_SERVER='rnice655:5000'

WAIT_FOR_FRAME_TIMEOUT = 240  # max uses 50*5

# We used to go through the results directory and add all files to the
# ispyb upload. Now some files should not be uploaded, so we'll
# discriminate by extension for now
ISPYB_UPLOAD_EXTENSIONS = [".lp", ".mtz", ".log", ".inp", ".gz"]


class EDPluginControlEDNAprocv1_0(EDPluginControl):
    """
    Runs the part of the EDNAproc pipeline that has to be run on the
    cluster.
    """

    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataEDNAprocInput)
        self.dataOutput = XSDataResultStoreAutoProc()
        self.strEDNAContactEmail = None
        self.strEDNAEmailSender = "edna-support@esrf.fr"
        self.strHost = None
        self.plugin_start = time.time()
        self.process_start = None
        self.process_end = None
        self.strBeamline = None
        self.strProposal = None
        self.strSessionDate = None
        self.strPrefix = None
        self.dataInputOrig = None
        self.bExecutedDimple = False
        self.timeStart = None
        self.timeEnd = None
        self.processingCommandLine = " ".join(sys.argv)
        self.hasUploadedAnomResultsToISPyB = False
        self.hasUploadedNoanomResultsToISPyB = False
        self.doAnom = True
        self.doNonom = False
        self.doAnomAndNonanom = False
        self.root_dir = None
        self.ispyb_user = None
        self.ispyb_password = None
        self.raw_data_dir = None
        self.icat_processed_data_dir = None
        self.processingPrograms = None

    def configure(self):
        EDPluginControl.configure(self)
        self.ispyb_user = self.config.get("ispyb_user")
        self.ispyb_password = self.config.get("ispyb_password")
        self.strEDNAContactEmail = self.config.get(
            "contactEmail", self.strEDNAContactEmail
        )
        self.strEDNAEmailSender = self.config.get(
            "emailSender", self.strEDNAEmailSender
        )

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlEDNAprocv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")

    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlEDNAprocv1_0.preProcess")
        self.processingPrograms = "EDNA_proc"
        self.screen("EDNA Auto Processing started")
        self.strHost = socket.gethostname()
        self.screen("Running on {0}".format(self.strHost))
        try:
            strLoad = os.getloadavg()
            self.screen("System load avg: {0}".format(strLoad))
        except OSError:
            pass

        data_in = self.dataInput

        # ICAT upload
        if self.dataInput.icat_processed_data_dir is not None:
            self.icat_processed_data_dir = self.dataInput.icat_processed_data_dir.value

        if data_in.input_file is None:
            # Input data file not provided, try to create one
            if EDUtilsPath.isESRF() and data_in.data_collection_id is not None:
                data_collection_id = data_in.data_collection_id.value
                newpath = self.createInputFile(
                    data_collection_id, self.getWorkingDirectory()
                )
                data_in.input_file = XSDataFile(XSDataString(newpath))
                self.dataInputOrig = self.dataInput.copy()
                # Copy original input file
                shutil.copy(
                    newpath,
                    os.path.join(self.getWorkingDirectory(), "XSD.INP_GENERATED"),
                )
                self.root_dir = self.getWorkingDirectory()
            else:
                strErrorMessage = "No input file provided!"
                self.ERROR(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
                # setFailure does not prevent preProcess/process/etc from running
                raise Exception("EDNA FAILURE")
        else:
            # save the root path (where the initial xds.inp is) for later use
            self.root_dir = os.path.abspath(
                os.path.dirname(self.dataInput.input_file.path.value)
            )
            self.dataInputOrig = self.dataInput.copy()
            # at least check for the xds input file existence before
            # trying to start anything even if the first xds run does it
            # anyway
            if not os.path.exists(data_in.input_file.path.value):
                strErrorMessage = "The specified input file does not exist: {0}".format(
                    data_in.input_file.path.value
                )
                self.ERROR(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
                # setFailure does not prevent preProcess/process/etc from running
                raise Exception("EDNA FAILURE")
            else:
                # copy it to our dir and modify our input
                newpath = os.path.join(
                    self.getWorkingDirectory(),
                    os.path.basename(data_in.input_file.path.value),
                )
                shutil.copyfile(data_in.input_file.path.value, newpath)
                data_in.input_file.path = XSDataString(newpath)

        if self.dataInput.doAnomAndNonanom is not None:
            self.doAnomAndNonanom = self.dataInput.doAnomAndNonanom.value

        if self.doAnomAndNonanom:
            self.doAnom = True
            self.doNoanom = True
        else:
            if self.dataInput.doAnom is not None:
                self.doAnom = self.dataInput.doAnom.value
            self.doNoanom = not self.doAnom

        if EDUtilsPath.isESRF():
            (
                self.strBeamline,
                self.strProposal,
                self.strSessionDate,
                self.strPrefix,
            ) = self.getBeamlinePrefixFromPath(self.dataInputOrig.input_file.path.value)
            strSubject = "EDNA dp %s %s %s %s started" % (
                self.strBeamline,
                self.strProposal,
                self.strPrefix,
                self.strHost,
            )
        else:
            strSubject = "EDNA dp started on host %s" % self.strHost

        self.sendEmail(strSubject, "")

        # Check if the spacegroup needs to be converted to a number
        # (ie it's a symbolic thing)
        sgnumber = None
        if data_in.spacegroup is not None:
            try:
                sgnumber = int(data_in.spacegroup.value)
            except ValueError:
                # strip all whitespace and upcase the whole thing
                cleanedup = data_in.spacegroup.value.replace(" ", "").upper()
                if cleanedup in SPACE_GROUP_NUMBERS:
                    sgnumber = SPACE_GROUP_NUMBERS[cleanedup]

        xds_in = XSDataMinimalXdsIn()
        xds_in.input_file = data_in.input_file.path
        xds_in.start_image = data_in.start_image
        xds_in.end_image = data_in.end_image
        if sgnumber is not None:
            xds_in.spacegroup = XSDataInteger(sgnumber)

        if data_in.unit_cell is not None:
            # Workaround for mxCuBE unit cell comma separation and trailing "2"
            unit_cell = data_in.unit_cell
            unit_cell.value = unit_cell.value.replace(",", " ")
            if unit_cell.value.endswith("2"):
                unit_cell.value = unit_cell.value[:-1]

            # Check that unit cell is not zero
            if not any(abs(float(num)) < 0.1 for num in unit_cell.value.split()):
                xds_in.unit_cell = unit_cell

        self.stats = dict()

        # Get the image prefix from the directory name
        # XXX: This is horrible
        try:
            self.image_prefix = "_".join(
                os.path.basename(self.root_dir).split("_")[1:-1]
            )
        except Exception:
            self.image_prefix = ""

        if EDUtilsPath.isEMBL():
            # Add prefix if edna used
            self.image_prefix = self.image_prefix + "_edna"

        # The resultsdir used to be root_dir/results/fast_processing
        # self.results_dir = os.path.join(self.root_dir, 'results', 'fast_processing')
        # Now it is the <directory of the output_file>/results
        if (
            self.dataInput.output_file is not None
            and os.path.dirname(self.dataInput.output_file.path.value) != ""
        ):
            self.results_dir = os.path.join(
                os.path.dirname(self.dataInput.output_file.path.value), "results"
            )
        else:
            self.results_dir = os.path.join(
                os.path.dirname(self.dataInput.input_file.path.value), "results"
            )
        if os.path.exists(self.results_dir):
            # Remove existing results
            shutil.rmtree(self.results_dir)
        try:
            os.makedirs(self.results_dir)
        except OSError:  # it most likely exists
            strWarningMessage = "Error creating the results directory: {0}".format(
                traceback.format_exc()
            )
            self.addWarningMessage(strWarningMessage)
            self.WARNING(strWarningMessage)

        # Copy the vanilla XDS input file to the results dir
        infile_dest = os.path.join(
            self.results_dir, "ep_" + self.image_prefix + "_input_XDS.INP"
        )
        shutil.copy(self.dataInput.input_file.path.value, infile_dest)

        # Ensure the EDNAproc ids directory is there
        self.autoproc_ids_dir = os.path.join(
            self.results_dir, "fastproc_integration_ids"
        )
        try:
            os.makedirs(self.autoproc_ids_dir)
        except OSError:  # it's there
            strWarningMessage = "Error creating the EDNAproc ids directory: {0}".format(
                traceback.format_exc()
            )
            self.addWarningMessage(strWarningMessage)
            self.WARNING(strWarningMessage)

        # we'll need the low res limit later on
        lowres = data_in.low_resolution_limit
        if lowres is not None:
            self.low_resolution_limit = lowres.value
        else:
            if EDUtilsPath.isEMBL():
                self.low_resolution_limit = 999
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
        if "X-GEO_CORR=" in conf:
            xgeo = os.path.abspath(os.path.join(self.root_dir, conf["X-GEO_CORR="][0]))
            if not os.path.exists(xgeo):
                self.DEBUG("geometry file {0} does not exist, removing".format(xgeo))
                del conf["X-GEO_CORR="]
            else:
                conf["X-GEO_CORR="] = xgeo

        if "Y-GEO_CORR=" in conf:
            ygeo = os.path.abspath(os.path.join(self.root_dir, conf["Y-GEO_CORR="][0]))
            if not os.path.exists(ygeo):
                self.DEBUG("geometry file {0} does not exist, removing".format(ygeo))
                del conf["Y-GEO_CORR="]
            else:
                conf["Y-GEO_CORR="] = ygeo

        dump_xds_file(data_in.input_file.path.value, conf)

        resrange = conf.get("INCLUDE_RESOLUTION_RANGE=")

        if resrange is not None:
            if self.low_resolution_limit is not None:
                resrange[0] = self.low_resolution_limit
            if self.res_override is not None:
                resrange[1] = self.res_override
            conf["INCLUDE_RESOLUTION_RANGE="] = resrange
            dump_xds_file(data_in.input_file.path.value, conf)

        data_range = conf.get("DATA_RANGE=")
        # we'll need that for the very last part ( file import )
        self.data_range = data_range
        if data_range is not None:
            start_image = data_range[0]
            end_image = data_range[1]

        if self.dataInput.start_image is not None:
            start_image = self.dataInput.start_image.value
            self.data_range[0] = start_image

        if self.dataInput.end_image is not None:
            end_image = self.dataInput.end_image.value
            self.data_range[1] = end_image

        if end_image - start_image < 8:
            error_message = "There are fewer than 8 images, aborting"
            self.addErrorMessage(error_message)
            self.ERROR(error_message)
            self.setFailure()
            return

        template = conf["NAME_TEMPLATE_OF_DATA_FRAMES="][0]
        self.DEBUG("template for images is {0}".format(template))
        # fix the path if it's not absolute
        if not os.path.isabs(template):
            self.DEBUG("file template {0} is not absolute".format(template))
            template = os.path.normpath(os.path.join(self.root_dir, template))
            conf["NAME_TEMPLATE_OF_DATA_FRAMES="] = template
            self.DEBUG("file template fixed to {0}".format(template))
            self.DEBUG(
                "dumping back the file to {0}".format(data_in.input_file.path.value)
            )
            dump_xds_file(data_in.input_file.path.value, conf)

        self.first_image = _template_to_image(template, start_image)
        self.last_image = _template_to_image(template, end_image)
        self.raw_data_dir = os.path.realpath(os.path.dirname(template))
        # Follow symbolic links and remore "/mnt/..." from path:
        if EDUtilsPath.isESRF() and "/data" in self.raw_data_dir:
            if not self.raw_data_dir.startswith("/data"):
                position = self.raw_data_dir.find("/data")
                self.raw_data_dir = self.raw_data_dir[position:]

        self.xds_first = self.loadPlugin(
            "EDPluginControlRunXdsFastProcv1_0", "XDS_first"
        )
        self.xds_first.dataInput = xds_in

        if EDUtilsPath.isESRF():
            self.waitFileFirst = self.loadPlugin(
                "EDPluginMXWaitFilev1_1", "MXWaitFileFirst"
            )
            self.waitFileLast = self.loadPlugin(
                "EDPluginMXWaitFilev1_1", "MXWaitFileLast"
            )

        self.generate = self.loadPlugin("EDPluginXDSGeneratev1_0", "XDSGenerate")
        self.generate_xscale = self.loadPlugin(
            "EDPluginXDSGeneratev1_0", "XDSGenerate_for_Xscale"
        )

        self.first_res_cutoff = self.loadPlugin("EDPluginResCutoffv1_0")

        if self.doAnom:
            self.res_cutoff_anom = self.loadPlugin("EDPluginResCutoffv1_0")
            self.parse_xds_anom = self.loadPlugin("EDPluginParseXdsOutputv1_0")
            self.store_autoproc_anom = self.loadPlugin("EDPluginISPyBStoreAutoProcv1_4")
        if self.doNoanom:
            self.res_cutoff_noanom = self.loadPlugin("EDPluginResCutoffv1_0")
            self.parse_xds_noanom = self.loadPlugin("EDPluginParseXdsOutputv1_0")
            self.store_autoproc_noanom = self.loadPlugin(
                "EDPluginISPyBStoreAutoProcv1_4"
            )

        self.xscale_generate = self.loadPlugin("EDPluginControlXscaleGeneratev1_0")

        self.file_conversion = self.loadPlugin("EDPluginControlEDNAprocImportv1_0")

        self.phenixXtriage = self.loadPlugin("EDPluginPhenixXtriagev1_1")

        self.edPluginISPyBUpdateDataCollectionGroupComment = self.loadPlugin(
            "EDPluginISPyBUpdateDataCollectionGroupCommentv1_4"
        )

        # ESRF specific: wait till we got the last image
        if EDUtilsPath.isESRF():
            listDirectory = self.first_image.split(os.path.sep)
            first_image = self.first_image
            last_image = self.last_image
            if any(beamline in self.first_image for beamline in ["id30a1", "id30a2"]):
                minSizeFirst = 2000000
                minSizeLast = 2000000
            elif any(
                beamline in self.first_image
                for beamline in ["id23eh1", "id23eh2", "id30a3", "id30b"]
            ):
                minSizeFirst = 1000000
                minSizeLast = 1000000
                first_image = self.eiger_template_to_image(template, start_image)
                last_image = self.eiger_template_to_image(template, end_image)
            else:
                minSizeFirst = 1000000
                minSizeLast = 1000000

            fWaitFileTimeout = 3600  # s

            xsDataInputMXWaitFileFirst = XSDataInputMXWaitFile()
            xsDataInputMXWaitFileFirst.file = XSDataFile(XSDataString(first_image))
            xsDataInputMXWaitFileFirst.timeOut = XSDataTime(fWaitFileTimeout)
            self.waitFileFirst.size = XSDataInteger(minSizeFirst)
            self.waitFileFirst.dataInput = xsDataInputMXWaitFileFirst
            self.waitFileFirst.executeSynchronous()
            if self.waitFileFirst.dataOutput.timedOut.value:
                strWarningMessage = (
                    "Timeout after %d seconds waiting for the first image %s!"
                    % (fWaitFileTimeout, self.first_image)
                )
                self.addWarningMessage(strWarningMessage)
                self.WARNING(strWarningMessage)

            xsDataInputMXWaitFileLast = XSDataInputMXWaitFile()
            xsDataInputMXWaitFileLast.file = XSDataFile(XSDataString(last_image))
            xsDataInputMXWaitFileLast.timeOut = XSDataTime(fWaitFileTimeout)
            self.waitFileLast.size = XSDataInteger(minSizeLast)
            self.waitFileLast.dataInput = xsDataInputMXWaitFileLast
            self.waitFileLast.executeSynchronous()
            if self.waitFileLast.dataOutput.timedOut.value:
                strErrorMessage = (
                    "Timeout after %d seconds waiting for the last image %s!"
                    % (fWaitFileTimeout, self.last_image)
                )
                self.addErrorMessage(strErrorMessage)
                self.ERROR(strErrorMessage)
                self.setFailure()

        self.DEBUG("EDPluginControlEDNAprocv1_0.preProcess finished")

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlEDNAprocv1_0.process starting")

        self.timeStart = time.localtime()
        self.process_start = time.time()
        self.integration_id = None
        self.integration_id_anom = None
        self.program_id_anom = None
        self.integration_id_noanom = None
        self.program_id_noanom = None
        if self.dataInput.data_collection_id is not None:

            if self.doAnom:
                try:
                    (
                        self.integration_id_anom,
                        self.program_id_anom,
                    ) = self.create_integration_id(
                        self.dataInput.data_collection_id.value,
                        "Creating anomalous integration ID",
                        isAnom=True,
                    )
                except Exception as e:
                    strErrorMessage = "Could not get anom integration ID: \n{0}".format(
                        traceback.format_exc(e)
                    )
                    self.addErrorMessage(strErrorMessage)
                    self.ERROR(strErrorMessage)
                    self.integration_id_anom = None

            if self.doNoanom:
                try:
                    (
                        self.integration_id_noanom,
                        self.program_id_noanom,
                    ) = self.create_integration_id(
                        self.dataInput.data_collection_id.value,
                        "Creating non-anomalous integration ID",
                        isAnom=False,
                    )
                except Exception as e:
                    strErrorMessage = (
                        "Could not get non-anom integration ID: \n{0}".format(
                            traceback.format_exc(e)
                        )
                    )
                    self.addErrorMessage(strErrorMessage)
                    self.ERROR(strErrorMessage)
                    self.integration_id_noanom = None
        # Choose integration_id_anom is present, otherwise integration_id_anom
        if self.integration_id_anom is not None:
            self.integration_id = self.integration_id_anom
        elif self.integration_id_noanom is not None:
            self.integration_id = self.integration_id_noanom

        # first XDS plugin run with supplied XDS file
        self.screen("Starting first XDS run...")
        if self.doAnom:
            self.log_to_ispyb(
                self.integration_id, "Indexing", "Launched", "XDS started"
            )
        else:
            self.log_to_ispyb(
                self.integration_id_noanom, "Indexing", "Launched", "XDS started"
            )

        t0 = time.time()
        self.xds_first.executeSynchronous()
        self.retrieveFailureMessages(self.xds_first, "Fast proc")

        self.stats["first_xds"] = time.time() - t0

        if self.xds_first.isFailure():
            self.ERROR("first XDS run failed")
            self.setFailure()
            self.log_to_ispyb(
                self.integration_id,
                "Indexing",
                "Failed",
                "XDS failed after {0:.1f}s".format(self.stats["first_xds"]),
            )
            return
        else:
            self.screen("FINISHED first XDS run")
            self.log_to_ispyb(
                self.integration_id,
                "Indexing",
                "Successful",
                "XDS finished after {0:.1f}s".format(self.stats["first_xds"]),
            )
        self.screen("FINISHED first XDS run")

        # Copy the XDS.INP file that was used for the successful run
        # to the results directory
        tmppath = os.path.join(
            self.results_dir, "ep_" + self.image_prefix + "_successful_XDS.INP"
        )
        shutil.copy(
            os.path.join(self.xds_first.dataOutput.xds_run_directory.value, "XDS.INP"),
            tmppath,
        )

        # Copy the CORRECT.LP and INTEGRATE.LP files as well
        for fileName in ["CORRECT.LP", "INTEGRATE.LP"]:
            filePath = os.path.join(
                self.results_dir, "ep_" + self.image_prefix + "_" + fileName
            )
            try:
                shutil.copy(
                    os.path.join(
                        self.xds_first.dataOutput.xds_run_directory.value, fileName
                    ),
                    filePath,
                )
            except (IOError, OSError):
                strErrorMessage = (
                    "Failed to copy {0} file ({1}) to the results dir".format(
                        fileName, filePath
                    )
                )
                self.addErrorMessage(strErrorMessage)
                self.ERROR(strErrorMessage)

        self.log_to_ispyb(
            self.integration_id, "Indexing", "Launched", "Start of resolution cutoff"
        )

        # apply the first res cutoff with the res extracted from the first XDS run
        self.screen("STARTING first resolution cutoff")
        t0 = time.time()
        xdsresult = self.xds_first.dataOutput

        # for the custom stats
        #        self.custom_stats['overall_i_over_sigma']=xdsresult.total_completeness.isig.value
        #        self.custom_stats['overall_r_value']=xdsresult.total_completeness.rfactor.value
        #        self.custom_stats['inner_i_over_sigma']=xdsresult.completeness_entries[0].isig.value
        #        self.custom_stats['inner_r_value']=xdsresult.completeness_entries[0].rfactor.value
        #        self.custom_stats['i_over_sigma']=xdsresult.completeness_entries[-1].isig.value
        #        self.custom_stats['r_value']=xdsresult.completeness_entries[-1].rfactor.value

        res_cutoff_in = XSDataResCutoff()
        res_cutoff_in.xds_res = xdsresult
        res_cutoff_in.completeness_entries = xdsresult.completeness_entries
        res_cutoff_in.detector_max_res = self.dataInput.detector_max_res

        # XXX: remove from the data model as it is just pass-through?
        res_cutoff_in.total_completeness = xdsresult.total_completeness
        res_cutoff_in.completeness_cutoff = self.dataInput.completeness_cutoff
        res_cutoff_in.isig_cutoff = XSDataDouble(1.0)
        # res_cutoff_in.isig_cutoff = self.dataInput.isig_cutoff
        res_cutoff_in.r_value_cutoff = self.dataInput.r_value_cutoff
        res_cutoff_in.cc_half_cutoff = self.dataInput.cc_half_cutoff
        self.first_res_cutoff.dataInput = res_cutoff_in
        self.first_res_cutoff.executeSynchronous()
        self.retrieveFailureMessages(self.first_res_cutoff, "First res cutoff")

        self.stats["first_res_cutoff"] = time.time() - t0

        if self.first_res_cutoff.isFailure():
            self.ERROR("res cutoff failed")
            self.log_to_ispyb(
                self.integration_id,
                "Indexing",
                "Failed",
                "Resolution cutoff failed after {0:.1f}s".format(
                    self.stats["first_res_cutoff"]
                ),
            )
            self.setFailure()
            return
        else:
            self.screen("FINISHED first resolution cutoff")
            self.log_to_ispyb(
                self.integration_id,
                "Indexing",
                "Successful",
                "Resolution cutoff finished",
            )

        resolution = self.first_res_cutoff.dataOutput.res

        # for the generate w/ and w/out anom we have to specify where
        # the first XDS plugin run took place
        xds_run_directory = os.path.abspath(
            self.xds_first.dataOutput.xds_run_directory.value
        )
        self.screen("the xds run took place in {0}".format(xds_run_directory))
        generate_input = XSDataXdsGenerateInput()
        generate_input.resolution = resolution
        generate_input.previous_run_dir = XSDataString(xds_run_directory)
        generate_input.doAnom = XSDataBoolean(self.doAnom)
        generate_input.doNoanom = XSDataBoolean(self.doNoanom)
        self.generate.dataInput = generate_input

        self.log_to_ispyb(
            self.integration_id, "Scaling", "Launched", "Start of scaling"
        )

        self.DEBUG("STARTING anom/noanom generation")
        t0 = time.time()
        self.generate.executeSynchronous()
        self.retrieveFailureMessages(self.generate, "anom/noanom_generation")

        self.stats["anom/noanom_generation"] = time.time() - t0

        self.DEBUG("FINISHED anom/noanom generation")

        if self.generate.isFailure():
            self.ERROR("generating w/ and w/out anom failed")
            self.setFailure()
            self.log_to_ispyb(
                self.integration_id,
                "Scaling",
                "Failed",
                "Scaling failed after {0:.1}s".format(
                    self.stats["anom/noanom_generation"]
                ),
            )
            return
        else:
            self.screen("generating w/ and w/out anom finished")
            self.log_to_ispyb(
                self.integration_id,
                "Scaling",
                "Successful",
                "Scaling finished in {0:.1f}s".format(
                    self.stats["anom/noanom_generation"]
                ),
            )

        # Copy the integrate and xds_ascii files to the results directory (for
        # max)
        if self.doAnom:
            shutil.copy(
                self.generate.dataOutput.hkl_anom.value,
                os.path.join(self.results_dir, "ep_XDS_ASCII.HKL"),
            )
            shutil.copy(
                self.generate.dataOutput.integrate_anom.value,
                os.path.join(self.results_dir, "ep_INTEGRATE.HKL"),
            )
        elif self.doNoanom:
            shutil.copy(
                self.generate.dataOutput.hkl_no_anom.value,
                os.path.join(self.results_dir, "ep_XDS_ASCII.HKL"),
            )
            shutil.copy(
                self.generate.dataOutput.integrate_noanom.value,
                os.path.join(self.results_dir, "ep_INTEGRATE.HKL"),
            )

        if self.doAnom:
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
            self.retrieveFailureMessages(self.parse_xds_anom, "Parse xds anom")

            if self.parse_xds_anom.isFailure():
                strErrorMessage = "Parsing the xds generated w/ anom failed"
                self.addErrorMessage(strErrorMessage)
                self.ERROR(strErrorMessage)
                self.setFailure()
                return

        if self.doNoanom:
            # now the other one w/out anom
            parse_noanom_input = XSDataXdsOutputFile()
            parse_noanom_input.correct_lp = XSDataFile()
            parse_noanom_input.correct_lp.path = (
                self.generate.dataOutput.correct_lp_no_anom
            )

            gxparm_file_noanom = XSDataFile()
            gxparm_file_noanom.path = self.generate.dataOutput.gxparm
            parse_noanom_input.gxparm = gxparm_file_noanom

            self.parse_xds_noanom.dataInput = parse_noanom_input
            self.parse_xds_noanom.executeSynchronous()
            self.retrieveFailureMessages(self.parse_xds_noanom, "Parse xds noanom")

            if self.parse_xds_noanom.isFailure():
                strErrorMessage = "Parsing the xds generated w/ no anom failed"
                self.addErrorMessage(strErrorMessage)
                self.ERROR(strErrorMessage)
                self.setFailure()
                return

        # we now can apply the res cutoff on the anom and no anom
        # outputs. Note that this is not done in parallel, like the
        # xds parsing

        if self.doAnom:
            self.log_to_ispyb(
                self.integration_id,
                "Scaling",
                "Launched",
                "Start of anomalous resolution cutoffs",
            )
        if self.doNoanom:
            self.log_to_ispyb(
                self.integration_id_noanom,
                "Scaling",
                "Launched",
                "Start of non-anomalous resolution cutoffs",
            )

        # XXX completeness_cutoff/res_override and isig_cutoff still
        # missing
        if self.doAnom:
            res_cutoff_anom_in = XSDataResCutoff()
            res_cutoff_anom_in.detector_max_res = self.dataInput.detector_max_res
            res_cutoff_anom_in.xds_res = self.parse_xds_anom.dataOutput
            res_cutoff_anom_in.completeness_entries = (
                self.parse_xds_anom.dataOutput.completeness_entries
            )
            res_cutoff_anom_in.total_completeness = (
                self.parse_xds_anom.dataOutput.total_completeness
            )
            # pass in global cutoffs
            res_cutoff_anom_in.completeness_cutoff = self.dataInput.completeness_cutoff
            res_cutoff_anom_in.isig_cutoff = XSDataDouble(1.0)
            # res_cutoff_anom_in.isig_cutoff = self.dataInput.isig_cutoff
            res_cutoff_anom_in.r_value_cutoff = self.dataInput.r_value_cutoff
            res_cutoff_anom_in.cc_half_cutoff = self.dataInput.cc_half_cutoff
            self.res_cutoff_anom.dataInput = res_cutoff_anom_in

            self.DEBUG("STARTING anom res cutoff")
            t0 = time.time()
            self.res_cutoff_anom.executeSynchronous()
            self.retrieveFailureMessages(self.res_cutoff_anom, "Res cut anom")
            self.stats["res_cutoff_anom"] = time.time() - t0

            if self.res_cutoff_anom.isFailure():
                self.ERROR("res cutoff for anom data failed")
                self.setFailure()
                self.log_to_ispyb(
                    self.integration_id,
                    "Scaling",
                    "Failed",
                    "Anomalous resolution cutoffs failed in {0:.1f}s".format(
                        self.stats["res_cutoff_anom"] + self.stats["res_cutoff_anom"]
                    ),
                )
                return
            else:
                self.screen("FINISHED anom res cutoff")
                self.log_to_ispyb(
                    self.integration_id,
                    "Scaling",
                    "Successful",
                    "Anomalous resolution cutoffs finished in {0:.1f}s".format(
                        self.stats["res_cutoff_anom"] + self.stats["res_cutoff_anom"]
                    ),
                )

            self.DEBUG("FINISHED anom res cutoff")

        if self.doNoanom:
            # same for non anom
            res_cutoff_noanom_in = XSDataResCutoff()
            res_cutoff_noanom_in.detector_max_res = self.dataInput.detector_max_res
            res_cutoff_noanom_in.xds_res = self.parse_xds_noanom.dataOutput
            res_cutoff_noanom_in.completeness_entries = (
                self.parse_xds_noanom.dataOutput.completeness_entries
            )
            res_cutoff_noanom_in.total_completeness = (
                self.parse_xds_noanom.dataOutput.total_completeness
            )
            # pass in global cutoffs
            res_cutoff_noanom_in.completeness_cutoff = (
                self.dataInput.completeness_cutoff
            )
            res_cutoff_noanom_in.isig_cutoff = XSDataDouble(1.0)
            # res_cutoff_noanom_in.isig_cutoff = self.dataInput.isig_cutoff
            res_cutoff_noanom_in.r_value_cutoff = self.dataInput.r_value_cutoff
            res_cutoff_noanom_in.cc_half_cutoff = self.dataInput.cc_half_cutoff
            self.res_cutoff_noanom.dataInput = res_cutoff_noanom_in

            self.DEBUG("STARTING noanom res cutoff")
            t0 = time.time()
            self.res_cutoff_noanom.executeSynchronous()
            self.retrieveFailureMessages(self.res_cutoff_noanom, "Res cut noanom")
            self.stats["res_cutoff_noanom"] = time.time() - t0

            if self.res_cutoff_noanom.isFailure():
                self.ERROR("res cutoff for non anom data failed")
                self.setFailure()
                self.log_to_ispyb(
                    self.integration_id_noanom,
                    "Scaling",
                    "Failed",
                    "Non-anomalous resolution cutoffs failed in {0:.1f}s".format(
                        self.stats["res_cutoff_noanom"]
                    ),
                )
                return
            else:
                self.screen("FINISHED noanom res cutoff")
                self.log_to_ispyb(
                    self.integration_id_noanom,
                    "Scaling",
                    "Successful",
                    "Non-anomalous resolution cutoffs finished in {0:.1f}s".format(
                        self.stats["res_cutoff_noanom"]
                    ),
                )

        import_in = XSDataEDNAprocImport()
        if self.doAnom:
            import_in.input_anom = self.generate.dataOutput.hkl_anom
        if self.doNoanom:
            import_in.input_noanom = self.generate.dataOutput.hkl_no_anom
        import_in.dataCollectionID = self.dataInput.data_collection_id
        import_in.start_image = XSDataInteger(self.data_range[0])
        import_in.end_image = XSDataInteger(self.data_range[1])

        # XXX: is this the right place to get the res from?
        if self.doAnom:
            import_in.res = self.res_cutoff_anom.dataOutput.res
        elif self.doNoanom:
            import_in.res = self.res_cutoff_noanom.dataOutput.res

        # XXX: This is optional but seems required by aimless
        import_in.nres = self.dataInput.nres

        import_in.output_directory = XSDataString(self.results_dir)

        try:
            import_in.image_prefix = XSDataString(self.image_prefix)
        except Exception:
            self.DEBUG(
                'could not determine image prefix from directory "{0}"'.format(
                    self.root_dir
                )
            )

        if self.dataInput.spacegroup is not None:
            import_in.choose_spacegroup = self.dataInput.spacegroup

        self.file_conversion.dataInput = import_in

        t0 = time.time()
        self.file_conversion.executeSynchronous()
        self.retrieveFailureMessages(self.file_conversion, "File conversion")
        self.stats["autoproc_import"] = time.time() - t0

        if self.file_conversion.isFailure():
            strErrorMessage = "File import failed"
            self.addErrorMessage(strErrorMessage)
            self.ERROR(strErrorMessage)

        # use the cell dimensions and spacegroup from pointless to create a
        # file in the results directory
        filename = "_".join(
            [
                str(self.file_conversion.dataOutput.pointless_sgnumber.value),
                str(self.file_conversion.dataOutput.pointless_cell[0].value),
                str(self.file_conversion.dataOutput.pointless_cell[1].value),
                str(self.file_conversion.dataOutput.pointless_cell[2].value),
                str(self.file_conversion.dataOutput.pointless_cell[3].value),
                str(self.file_conversion.dataOutput.pointless_cell[4].value),
                str(self.file_conversion.dataOutput.pointless_cell[5].value),
            ]
        )
        try:
            os.mknod(os.path.join(self.results_dir, filename), 0o755)
        except OSError:  # file exists
            pass

        # now we just have to run XScale to generate w/ and w/out
        # anom, merged and unmerged

        generate_xscale_input = XSDataXdsGenerateInput()
        generate_xscale_input.resolution = resolution
        generate_xscale_input.previous_run_dir = XSDataString(xds_run_directory)
        generate_xscale_input.spacegroup = (
            self.file_conversion.dataOutput.pointless_sgnumber
        )
        generate_xscale_input.doAnom = XSDataBoolean(self.doAnom)
        generate_xscale_input.doNoanom = XSDataBoolean(self.doNoanom)
        pointless_cell = ""
        list_pointless_cell = self.file_conversion.dataOutput.pointless_cell
        pointless_cell += "{0}".format(list_pointless_cell[0].value)
        for cell_param in list_pointless_cell[1:]:
            pointless_cell += " {0}".format(cell_param.value)
        generate_xscale_input.unit_cell = XSDataString(pointless_cell)
        self.generate_xscale.dataInput = generate_xscale_input
        self.generate_xscale.executeSynchronous()

        # We use another control plugin for that to isolate the whole thing
        xscale_generate_in = XSDataXscaleInput()

        input_file = XSDataXscaleInputFile()
        if self.doAnom:
            input_file.path_anom = self.generate_xscale.dataOutput.hkl_anom
        if self.doNoanom:
            input_file.path_noanom = self.generate_xscale.dataOutput.hkl_no_anom

        xscale_generate_in.xds_files = [input_file]
        xscale_generate_in.unit_cell_constants = (
            self.file_conversion.dataOutput.pointless_cell
        )
        xscale_generate_in.sg_number = (
            self.file_conversion.dataOutput.pointless_sgnumber
        )

        if self.doAnom:
            input_file.res = self.res_cutoff_anom.dataOutput.res
            xscale_generate_in.bins = self.res_cutoff_anom.dataOutput.bins
            xscale_generate_in.friedels_law = XSDataBoolean(False)
        elif self.doNoanom:
            input_file.res = self.res_cutoff_noanom.dataOutput.res
            xscale_generate_in.bins = self.res_cutoff_noanom.dataOutput.bins
            xscale_generate_in.friedels_law = XSDataBoolean(True)

        self.xscale_generate.dataInput = xscale_generate_in
        self.DEBUG("STARTING xscale generation")
        self.log_to_ispyb(self.integration_id, "Scaling", "Launched", "Start of XSCALE")

        t0 = time.time()
        self.xscale_generate.executeSynchronous()
        self.retrieveFailureMessages(self.xscale_generate, "XSCALE")
        self.stats["xscale_generate"] = time.time() - t0

        if self.xscale_generate.isFailure():
            strErrorMessage = "Xscale generation failed"
            self.addErrorMessage(strErrorMessage)
            self.ERROR(strErrorMessage)
            self.log_to_ispyb(
                self.integration_id,
                "Scaling",
                "Failed",
                "XSCALE failed after {0:.1f}s".format(self.stats["xscale_generate"]),
            )
            return
        else:
            self.screen("xscale anom/merge generation finished")
            self.log_to_ispyb(
                self.integration_id,
                "Scaling",
                "Successful",
                "XSCALE finished in {0:.1f}s".format(self.stats["xscale_generate"]),
            )

        # Copy the generated files to the results dir
        attrs = []
        if self.doAnom:
            attrs += ["lp_anom_merged", "lp_anom_unmerged"]
        if self.doNoanom:
            attrs += ["lp_noanom_merged", "lp_noanom_unmerged"]

        xscale_logs = [getattr(self.xscale_generate.dataOutput, attr) for attr in attrs]
        xscale_logs = [log.value for log in xscale_logs if log is not None]
        for log in xscale_logs:
            target = os.path.join(
                self.results_dir,
                "_".join(["ep_" + self.image_prefix, os.path.basename(log)]),
            )
            try:
                shutil.copyfile(log, target)
            except IOError:
                strErrorMessage = "Could not copy {0} to {1}".format(log, target)
                self.addErrorMessage(strErrorMessage)
                self.ERROR(strErrorMessage)

        # Run phenix.xtriage
        xsDataInputPhenixXtriage = XSDataInputPhenixXtriage()
        if self.doAnom:
            xsDataInputPhenixXtriage.mtzFile = XSDataFile(
                XSDataString(
                    os.path.join(
                        self.file_conversion.dataInput.output_directory.value,
                        "ep_{0}_unmerged_anom_pointless_multirecord.mtz.gz".format(
                            self.image_prefix
                        ),
                    )
                )
            )
        else:
            xsDataInputPhenixXtriage.mtzFile = XSDataFile(
                XSDataString(
                    os.path.join(
                        self.file_conversion.dataInput.output_directory.value,
                        "ep_{0}_unmerged_noanom_pointless_multirecord.mtz.gz".format(
                            self.image_prefix
                        ),
                    )
                )
            )
        self.phenixXtriage.dataInput = xsDataInputPhenixXtriage
        self.phenixXtriage.executeSynchronous()
        if self.phenixXtriage.isFailure():
            self.log_to_ispyb(
                self.integration_id, "Scaling", "Failed", "phenix.xtriage failed"
            )
        else:
            xsDataResultPhenixXtriage = self.phenixXtriage.dataOutput

            shutil.copy(
                xsDataResultPhenixXtriage.logFile.path.value,
                os.path.join(
                    self.file_conversion.dataInput.output_directory.value,
                    "ep_{0}_phenix_xtriage_anom.log".format(self.image_prefix),
                ),
            )

            if xsDataResultPhenixXtriage.pseudotranslation.value:
                strMessage = "Pseudotranslation detected by phenix.xtriage!"
                bPseudotranslation = True
            else:
                strMessage = "No pseudotranslation detected by phenix.xtriage."
                bPseudotranslation = False
            self.screen(strMessage)
            self.log_to_ispyb(self.integration_id, "Scaling", "Successful", strMessage)

            if xsDataResultPhenixXtriage.twinning.value:
                strMessage = "Twinning detected by phenix.xtriage!"
                bTwinning = True
            else:
                strMessage = "No twinning detected by phenix.xtriage."
                bTwinning = False
            self.screen(strMessage)
            self.log_to_ispyb(self.integration_id, "Scaling", "Successful", strMessage)

            if self.dataInput.data_collection_id is not None and (
                bPseudotranslation or bTwinning
            ):
                if bPseudotranslation and bTwinning:
                    strISPyBComment = (
                        "EDNA dp: pseudo-translation and twinning detected."
                    )
                elif bPseudotranslation:
                    strISPyBComment = "EDNA dp: pseudo-translation detected."
                else:
                    strISPyBComment = "EDNA dp: twinning detected."
                xsDataInput = XSDataInputISPyBUpdateDataCollectionGroupComment()
                xsDataInput.newComment = XSDataString(strISPyBComment)
                xsDataInput.dataCollectionId = self.dataInput.data_collection_id
                self.edPluginISPyBUpdateDataCollectionGroupComment.dataInput = (
                    xsDataInput
                )
                self.executePluginSynchronous(
                    self.edPluginISPyBUpdateDataCollectionGroupComment
                )

        self.process_end = time.time()
        self.timeEnd = time.localtime()

    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlEDNAprocv1_0.postProcess")

        # Create a file in the results directory to indicate all files have been
        # populated in it already so Max's code can be aware of that
        try:
            os.mknod(os.path.join(self.results_dir, ".finished"), 0o755)
        except OSError:  # file exists
            pass

        if self.dataInput.data_collection_id is not None:
            # Now that we have executed the whole thing we need to create
            # the suitable ISPyB plugin input and serialize it to the file
            # we've been given as input
            output = AutoProcContainer()

            # AutoProc attr
            autoproc = AutoProc()

            # There's also
            pointless_sg_str = self.file_conversion.dataOutput.pointless_sgstring
            if pointless_sg_str is not None:
                autoproc.spaceGroup = pointless_sg_str.value

            # The unit cell will be taken from the no anom aimless run below

            output.AutoProc = autoproc

            if self.doAnom:
                # ANOM PATH
                scaling_container_anom = AutoProcScalingContainer()

                inner, outer, overall, unit_cell = self.parse_aimless(
                    self.file_conversion.dataOutput.aimless_log_anom.value
                )
                inner_stats = AutoProcScalingStatistics()
                for k, v in inner.items():
                    setattr(inner_stats, k, v)
                inner_stats.anomalous = True
                scaling_container_anom.AutoProcScalingStatistics.append(inner_stats)

                outer_stats = AutoProcScalingStatistics()
                for k, v in outer.items():
                    setattr(outer_stats, k, v)
                outer_stats.anomalous = True
                scaling_container_anom.AutoProcScalingStatistics.append(outer_stats)

                overall_stats = AutoProcScalingStatistics()
                for k, v in overall.items():
                    setattr(overall_stats, k, v)
                overall_stats.anomalous = True
                scaling_container_anom.AutoProcScalingStatistics.append(overall_stats)

                scaling = AutoProcScaling()
                scaling.recordTimeStamp = time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.localtime()
                )

                scaling_container_anom.AutoProcScaling = scaling

                integration_container_anom = AutoProcIntegrationContainer()
                image = Image()
                if self.dataInput.data_collection_id is not None:
                    image.dataCollectionId = self.dataInput.data_collection_id.value
                integration_container_anom.Image = image

                integration_anom = AutoProcIntegration()
                if self.integration_id is not None:
                    integration_anom.autoProcIntegrationId = self.integration_id
                integration_anom.cell_a = unit_cell[0]
                integration_anom.cell_b = unit_cell[1]
                integration_anom.cell_c = unit_cell[2]
                integration_anom.cell_alpha = unit_cell[3]
                integration_anom.cell_beta = unit_cell[4]
                integration_anom.cell_gamma = unit_cell[5]
                integration_anom.anomalous = 1

                # done with the integration
                integration_container_anom.AutoProcIntegration = integration_anom
                scaling_container_anom.AutoProcIntegrationContainer = (
                    integration_container_anom
                )

            if self.doNoanom:
                # NOANOM PATH

                # scaling container and all the things that go in
                scaling_container_noanom = AutoProcScalingContainer()
                scaling = AutoProcScaling()
                scaling.recordTimeStamp = time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.localtime()
                )

                scaling_container_noanom.AutoProcScaling = scaling

                inner, outer, overall, unit_cell = self.parse_aimless(
                    self.file_conversion.dataOutput.aimless_log_noanom.value
                )

                autoproc.refinedCell_a = str(unit_cell[0])
                autoproc.refinedCell_b = str(unit_cell[1])
                autoproc.refinedCell_c = str(unit_cell[2])
                autoproc.refinedCell_alpha = str(unit_cell[3])
                autoproc.refinedCell_beta = str(unit_cell[4])
                autoproc.refinedCell_gamma = str(unit_cell[5])

                inner_stats = AutoProcScalingStatistics()
                for k, v in inner.items():
                    setattr(inner_stats, k, v)
                inner_stats.anomalous = False
                scaling_container_noanom.AutoProcScalingStatistics.append(inner_stats)

                outer_stats = AutoProcScalingStatistics()
                for k, v in outer.items():
                    setattr(outer_stats, k, v)
                outer_stats.anomalous = False
                scaling_container_noanom.AutoProcScalingStatistics.append(outer_stats)

                overall_stats = AutoProcScalingStatistics()
                for k, v in overall.items():
                    setattr(overall_stats, k, v)
                overall_stats.anomalous = False
                scaling_container_noanom.AutoProcScalingStatistics.append(overall_stats)

                integration_container_noanom = AutoProcIntegrationContainer()
                image = Image()
                if self.dataInput.data_collection_id is not None:
                    image.dataCollectionId = self.dataInput.data_collection_id.value
                integration_container_noanom.Image = image

                integration_noanom = AutoProcIntegration()
                if self.integration_id_noanom is not None:
                    integration_noanom.autoProcIntegrationId = (
                        self.integration_id_noanom
                    )
                integration_noanom.cell_a = unit_cell[0]
                integration_noanom.cell_b = unit_cell[1]
                integration_noanom.cell_c = unit_cell[2]
                integration_noanom.cell_alpha = unit_cell[3]
                integration_noanom.cell_beta = unit_cell[4]
                integration_noanom.cell_gamma = unit_cell[5]
                integration_noanom.anomalous = 0

                # done with the integration
                integration_container_noanom.AutoProcIntegration = integration_noanom
                scaling_container_noanom.AutoProcIntegrationContainer = (
                    integration_container_noanom
                )

            # ------ NO ANOM / ANOM end
            if self.doAnom:
                program_container_anom = AutoProcProgramContainer()
                program_container_anom.AutoProcProgram = (
                    EDHandlerXSDataISPyBv1_4.createAutoProcProgram(
                        programId=self.program_id_anom,
                        status="SUCCESS",
                        timeStart=self.timeStart,
                        timeEnd=self.timeEnd,
                        processingCommandLine=self.processingCommandLine,
                        processingPrograms=self.processingPrograms,
                    )
                )

            if self.doNoanom:
                program_container_noanom = AutoProcProgramContainer()
                program_container_noanom.AutoProcProgram = (
                    EDHandlerXSDataISPyBv1_4.createAutoProcProgram(
                        programId=self.program_id_noanom,
                        status="SUCCESS",
                        timeStart=self.timeStart,
                        timeEnd=self.timeEnd,
                        processingCommandLine=self.processingCommandLine,
                        processingPrograms=self.processingPrograms,
                    )
                )

            # now for the generated files. There's some magic to do with
            # their paths to determine where to put them on pyarch
            pyarch_path = None
            # Note: the path is in the form /data/whatever

            # remove the edna-autoproc-import suffix
            original_files_dir = self.file_conversion.dataInput.output_directory.value
            # files_dir, _ = os.path.split(original_files_dir)
            files_dir = original_files_dir

            if EDUtilsPath.isALBA():
                _pyarch_path = EDHandlerESRFPyarchv1_0.translateToIspybALBAPath(
                    self.first_image
                )
                pyarch_path = "_".join(_pyarch_path.split("_")[:-1])
                from datetime import datetime

                _id = datetime.now().strftime("%Y%m%d_%H%M%S")
                pyarch_path = os.path.join(pyarch_path, "ednaPROC_%s" % _id)

            # the whole transformation is fragile!
            if EDUtilsPath.isEMBL():
                tokens = [
                    elem
                    for elem in self.first_image.split(os.path.sep)
                    if len(elem) > 0
                ]
                print(tokens)
                if "p14" in tokens[0:3] or "P14" in tokens[0:3]:
                    strBeamline = "p14"
                elif "p13" in tokens[0:3] or "P13" in tokens[0:3]:
                    strBeamline = "p13"
                else:
                    strBeamline = ""
                pyarch_path = os.path.join("/data/ispyb", strBeamline, *tokens[3:-1])
                pyarch_path = os.path.join(pyarch_path, "%s" % self.integration_id)
            elif EDUtilsPath.isESRF():
                if files_dir.startswith("/data/visitor"):
                    # We might get empty elements at the head/tail of the list
                    tokens = [
                        elem for elem in files_dir.split(os.path.sep) if len(elem) > 0
                    ]
                    year = tokens[4][0:4]
                    pyarch_path = os.path.join(
                        "/data/pyarch", year, tokens[3], tokens[2], *tokens[4:]
                    )
                else:
                    # We might get empty elements at the head/tail of the list
                    tokens = [
                        elem for elem in files_dir.split(os.path.sep) if len(elem) > 0
                    ]
                    if tokens[2] == "inhouse":
                        year = tokens[4][0:4]
                        pyarch_path = os.path.join(
                            "/data/pyarch", year, tokens[1], *tokens[3:]
                        )
            elif EDUtilsPath.isMAXIV():
                pyarch_path = files_dir.replace("/data", "/mxn/groups/ispybstorage", 1)

            if pyarch_path is not None:
                pyarch_path = pyarch_path.replace("PROCESSED_DATA", "RAW_DATA")
                try:
                    os.makedirs(pyarch_path)
                except OSError:
                    # dir already exists, may happen when testing
                    self.screen(
                        "Target directory on pyarch ({0}) already exists, ignoring".format(
                            pyarch_path
                        )
                    )

                file_list = []
                # we can now copy the files to this dir
                for f in os.listdir(original_files_dir):
                    current = os.path.join(original_files_dir, f)
                    if not os.path.isfile(current):
                        continue
                    if (
                        not os.path.splitext(current)[1].lower()
                        in ISPYB_UPLOAD_EXTENSIONS
                    ):
                        continue
                    new_path = os.path.join(pyarch_path, f)
                    self.screen("Uploading {0} to ISPyB".format(f))
                    file_list.append(new_path)
                    shutil.copyfile(current, new_path)
                # now add those to the ispyb upload
                for path in file_list:
                    dirname, filename = os.path.split(path)
                    if self.doAnom:
                        attach_anom = AutoProcProgramAttachment()
                        attach_anom.fileType = "Result"
                        attach_anom.fileName = filename
                        attach_anom.filePath = dirname
                        program_container_anom.AutoProcProgramAttachment.append(
                            attach_anom
                        )
                    if self.doNoanom:
                        attach_noanom = AutoProcProgramAttachment()
                        attach_noanom.fileType = "Result"
                        attach_noanom.fileName = filename
                        attach_noanom.filePath = dirname
                        program_container_noanom.AutoProcProgramAttachment.append(
                            attach_noanom
                        )

            if self.doAnom:
                # first with anom

                output.AutoProcProgramContainer = program_container_anom
                output.AutoProcScalingContainer = scaling_container_anom

                ispyb_input = XSDataInputStoreAutoProc()
                ispyb_input.AutoProcContainer = output

                if self.dataInput.output_file is not None:
                    with open(self.dataInput.output_file.path.value, "w") as f:
                        f.write(ispyb_input.marshal())

                autoProcProgramId = None
                if self.dataInput.data_collection_id is not None:
                    # store results in ispyb
                    self.store_autoproc_anom.dataInput = ispyb_input
                    t0 = time.time()
                    self.store_autoproc_anom.executeSynchronous()
                    autoProcProgramId = (
                        self.store_autoproc_anom.dataOutput.autoProcProgramId.value
                    )

                    if self.store_autoproc_anom.isFailure():
                        self.ERROR("Could not upload anom results to ispyb!")
                    else:
                        self.hasUploadedAnomResultsToISPyB = True
                        self.screen("Anom results uploaded to ISPyB")
                        # store the EDNAproc ID as a filename in the
                        # fastproc_integration_ids directory
                        os.mknod(
                            os.path.join(
                                self.autoproc_ids_dir, str(self.integration_id)
                            ),
                            0o755,
                        )

                    self.retrieveFailureMessages(
                        self.store_autoproc_anom, "Store EDNAproc anom"
                    )
                    self.stats["ispyb_upload"] = time.time() - t0

                    # Upload to ICAT
                    if self.icat_processed_data_dir is not None:
                        EDUtilsICAT.uploadToICAT(
                            processName=self.processingPrograms,
                            xsDataInputStoreAutoProc=ispyb_input,
                            directory=self.raw_data_dir,
                            icatProcessDataDir=self.icat_processed_data_dir,
                            isAnom=True,
                            beamline=self.strBeamline,
                            proposal=self.strProposal,
                            timeStart=None,
                            timeEnd=None,
                        )

            if self.doNoanom:
                # then noanom stats

                output.AutoProcProgramContainer = program_container_noanom
                output.AutoProcScalingContainer = scaling_container_noanom

                ispyb_input = XSDataInputStoreAutoProc()
                ispyb_input.AutoProcContainer = output

                if self.dataInput.output_file is not None:
                    with open(self.dataInput.output_file.path.value, "w") as f:
                        f.write(ispyb_input.marshal())

                if self.dataInput.data_collection_id is not None:
                    # store results in ispyb
                    self.store_autoproc_noanom.dataInput = ispyb_input
                    t0 = time.time()
                    self.store_autoproc_noanom.executeSynchronous()
                    autoProcProgramId = (
                        self.store_autoproc_noanom.dataOutput.autoProcProgramId.value
                    )

                    if self.store_autoproc_noanom.isFailure():
                        self.ERROR("Could not upload noanom results to ISPyB!")
                    else:
                        self.hasUploadedNoanomResultsToISPyB = True
                        self.screen("Noanom results uploaded to ISPyB")
                        # store the EDNAproc id
                        os.mknod(
                            os.path.join(
                                self.autoproc_ids_dir, str(self.integration_id_noanom)
                            ),
                            0o755,
                        )

                    self.retrieveFailureMessages(
                        self.store_autoproc_noanom, "Store EDNAproc noanom"
                    )
                    self.stats["ispyb_upload"] = time.time() - t0
                    # Upload to ICAT
                    if self.icat_processed_data_dir is not None:
                        EDUtilsICAT.uploadToICAT(
                            processName=self.processingPrograms,
                            xsDataInputStoreAutoProc=ispyb_input,
                            directory=self.raw_data_dir,
                            icatProcessDataDir=self.icat_processed_data_dir,
                            isAnom=False,
                            beamline=self.strBeamline,
                            proposal=self.strProposal,
                            timeStart=None,
                            timeEnd=None,
                        )

            # Finally run dimple if executed at the ESRF
            if (
                EDUtilsPath.isESRF()
                or EDUtilsPath.isEMBL()
                or EDUtilsPath.isALBA()
                or EDUtilsPath.isMAXIV()
            ):
                xsDataInputControlDimple = XSDataInputControlDimple()
                xsDataInputControlDimple.dataCollectionId = (
                    self.dataInput.data_collection_id
                )
                xsDataInputControlDimple.mtzFile = XSDataFile(
                    XSDataString(
                        os.path.join(
                            self.file_conversion.dataInput.output_directory.value,
                            "ep_{0}_anom_aimless.mtz".format(self.image_prefix),
                        )
                    )
                )
                xsDataInputControlDimple.imagePrefix = XSDataString(self.image_prefix)
                xsDataInputControlDimple.proposal = XSDataString(self.strProposal)
                xsDataInputControlDimple.sessionDate = XSDataString(self.strSessionDate)
                xsDataInputControlDimple.beamline = XSDataString(self.strBeamline)
                xsDataInputControlDimple.pdbDirectory = XSDataFile(
                    XSDataString(self.root_dir)
                )
                xsDataInputControlDimple.resultsDirectory = XSDataFile(
                    XSDataString(self.results_dir)
                )
                if pyarch_path is not None:
                    xsDataInputControlDimple.pyarchPath = XSDataFile(
                        XSDataString(pyarch_path)
                    )
                if autoProcProgramId is not None:
                    xsDataInputControlDimple.autoProcProgramId = XSDataInteger(
                        autoProcProgramId
                    )
                edPluginControlRunDimple = self.loadPlugin(
                    "EDPluginControlRunDimplev1_0"
                )
                edPluginControlRunDimple.dataInput = xsDataInputControlDimple
                edPluginControlRunDimple.executeSynchronous()
                if (
                    edPluginControlRunDimple.dataOutput.dimpleExecutedSuccessfully
                    is not None
                ):
                    if (
                        edPluginControlRunDimple.dataOutput.dimpleExecutedSuccessfully.value
                    ):
                        self.bExecutedDimple = True
                        strISPyBComment = "DIMPLE results available for EDNA_proc"
                        xsDataInput = XSDataInputISPyBUpdateDataCollectionGroupComment()
                        xsDataInput.newComment = XSDataString(strISPyBComment)
                        xsDataInput.dataCollectionId = self.dataInput.data_collection_id
                        self.edPluginISPyBUpdateDataCollectionGroupComment.dataInput = (
                            xsDataInput
                        )
                        self.executePluginSynchronous(
                            self.edPluginISPyBUpdateDataCollectionGroupComment
                        )

    def finallyProcess(self, _edObject=None):
        EDPluginControl.finallyProcess(self)
        strMessage = ""
        if self.getListOfWarningMessages() != []:
            strMessage += "Warning messages: \n\n"
            for strWarningMessage in self.getListOfWarningMessages():
                strMessage += strWarningMessage + "\n\n"
        if self.getListOfErrorMessages() != []:
            strMessage += "Error messages: \n\n"
            for strErrorMessage in self.getListOfErrorMessages():
                strMessage += strErrorMessage + "\n\n"
        if self.isFailure():
            strStatus = "FAILURE"
            if self.dataInput.data_collection_id is not None:
                if self.doAnom and not self.hasUploadedAnomResultsToISPyB:
                    # Upload program status to ISPyB
                    # anom
                    inputStoreAutoProcAnom = (
                        EDHandlerXSDataISPyBv1_4.createInputStoreAutoProc(
                            self.dataInput.data_collection_id.value,
                            self.integration_id,
                            isAnomalous=True,
                            programId=self.program_id_anom,
                            status="FAILED",
                            timeStart=self.timeStart,
                            timeEnd=self.timeEnd,
                            processingCommandLine=self.processingCommandLine,
                            processingPrograms=self.processingPrograms,
                        )
                    )
                    self.store_autoproc_anom.dataInput = inputStoreAutoProcAnom
                    self.store_autoproc_anom.executeSynchronous()

                if self.doNoanom and not self.hasUploadedNoanomResultsToISPyB:
                    # noanom
                    inputStoreAutoProcNoanom = (
                        EDHandlerXSDataISPyBv1_4.createInputStoreAutoProc(
                            self.dataInput.data_collection_id.value,
                            self.integration_id_noanom,
                            isAnomalous=False,
                            programId=self.program_id_noanom,
                            status="FAILED",
                            timeStart=self.timeStart,
                            timeEnd=self.timeEnd,
                            processingCommandLine=self.processingCommandLine,
                            processingPrograms=self.processingPrograms,
                        )
                    )
                    self.store_autoproc_noanom.dataInput = inputStoreAutoProcNoanom
                    self.store_autoproc_noanom.executeSynchronous()

        else:
            strStatus = "SUCCESS"
        if EDUtilsPath.isESRF():
            if self.bExecutedDimple:
                strSubject = "EDNA dp DIMPLE %s %s %s %s %s" % (
                    self.strBeamline,
                    self.strProposal,
                    self.strPrefix,
                    self.strHost,
                    strStatus,
                )
            else:
                strSubject = "EDNA dp %s %s %s %s %s" % (
                    self.strBeamline,
                    self.strProposal,
                    self.strPrefix,
                    self.strHost,
                    strStatus,
                )
        else:
            strSubject = "EDNA dp host %s %s" % (self.strHost, strStatus)

        strMessage += "\n\nPlugin execution time: %.2f s\n" % (
            time.time() - self.plugin_start
        )
        if self.process_end is not None:
            fProcessExecutionTime = self.process_end - self.process_start
            iStartImage = self.data_range[0]
            iEndImage = self.data_range[1]
            iNoImages = iEndImage - iStartImage + 1
            strMessage += "No images: %d\n" % iNoImages
            strMessage += "Process execution time: %.2f s\n" % fProcessExecutionTime
            strMessage += "Process execution time per image: %.2f s\n" % (
                fProcessExecutionTime / iNoImages
            )
        self.sendEmail(strSubject, strMessage)

    def getBeamlinePrefixFromPath(self, strPathToXDSInp):
        """
        ESRF specific code for extracting the
        beamline name and prefix from the path
        """
        strBeamline = ""
        strProposal = ""
        strPrefix = ""
        strSessionDate = ""
        listPath = strPathToXDSInp.split("/")
        if listPath[2] == "gz":
            if listPath[3] == "visitor":
                strBeamline = listPath[5]
                strProposal = listPath[4]
                strSessionDate = listPath[6]
            elif listPath[4] == "inhouse":
                strBeamline = listPath[3]
                strProposal = listPath[5]
                strSessionDate = listPath[6]
        elif listPath[2] == "visitor":
            strBeamline = listPath[4]
            strProposal = listPath[3]
            strSessionDate = listPath[5]
        elif listPath[3] == "inhouse":
            strBeamline = listPath[2]
            strProposal = listPath[4]
            strSessionDate = listPath[5]
        strPrefix = listPath[-2][4:]
        return (strBeamline, strProposal, strSessionDate, strPrefix)

    def sendEmail(self, _strSubject, _strMessage):
        """Sends an email to the EDNA contact person (if configured)."""

        self.DEBUG("EDPluginControlEDNAprocv1_0.sendEmail: Subject = %s" % _strSubject)
        self.DEBUG("EDPluginControlEDNAprocv1_0.sendEmail: Message:")
        self.DEBUG(_strMessage)
        if self.strEDNAContactEmail is None:
            self.DEBUG(
                "EDPluginControlEDNAprocv1_0.sendEmail: No email address configured!"
            )
        elif self.getWorkingDirectory().find("ref-") != -1:
            self.DEBUG(
                "EDPluginControlEDNAprocv1_0.sendEmail: "
                + "Working directory contains 'ref-', "
                + "hence probably reference data collection"
            )
        else:
            try:
                self.DEBUG("Sending message to %s." % self.strEDNAContactEmail)
                self.DEBUG("Message: %s" % _strMessage)
                strMessage = "EDNA_HOME = %s\n" % EDUtilsPath.getEdnaHome()
                strMessage += "EDNA_SITE = %s\n" % EDUtilsPath.getEdnaSite()
                strMessage += "PLUGIN_NAME = %s\n" % self.getPluginName()
                strMessage += "working_dir = %s\n\n" % self.getWorkingDirectory()
                try:
                    strLoad = os.getloadavg()
                    strMessage += "System load avg: {0}\n".format(strLoad)
                except OSError:
                    pass
                strMessage += "\n"
                strMessage += _strMessage
                strEmailMsg = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" % (
                    self.strEDNAEmailSender,
                    self.strEDNAContactEmail,
                    _strSubject,
                    strMessage,
                )
                server = smtplib.SMTP("localhost")
                server.sendmail(
                    self.strEDNAEmailSender, self.strEDNAContactEmail, strEmailMsg
                )
                server.quit()
            except Exception:
                self.ERROR("Error when sending email message!")
                self.writeErrorTrace()

    # Proxy since the API changed and we can now log to several ids
    def log_to_ispyb(self, integration_id, step, status, comments=""):
        if integration_id is not None:
            if type(integration_id) is list:
                for item in integration_id:
                    self.log_to_ispyb_impl(item, step, status, comments)
            else:
                self.log_to_ispyb_impl(integration_id, step, status, comments)
                if status == "Failed":
                    for strErrorMessage in self.getListOfErrorMessages():
                        self.log_to_ispyb_impl(
                            integration_id, step, status, strErrorMessage
                        )

    def log_to_ispyb_impl(self, integration_id, step, status, comments=""):
        # hack in the event we could not create an integration ID
        if integration_id is None:
            EDVerbose.ERROR("could not log to ispyb: no integration id")
            return
        autoproc_status = edFactoryPlugin.loadPlugin(
            "EDPluginISPyBStoreAutoProcStatusv1_4"
        )
        status_input = XSDataInputStoreAutoProcStatus()
        status_input.autoProcIntegrationId = integration_id
        status_data = AutoProcStatus()
        status_data.step = step
        status_data.status = status
        status_data.comments = comments
        status_input.AutoProcStatus = status_data

        autoproc_status.dataInput = status_input

        autoproc_status.executeSynchronous()

    def create_integration_id(self, datacollect_id, comments, isAnom=True):
        autoproc_status = edFactoryPlugin.loadPlugin(
            "EDPluginISPyBStoreAutoProcStatusv1_4"
        )
        status_input = XSDataInputStoreAutoProcStatus()
        status_input.dataCollectionId = datacollect_id
        status_input.anomalous = isAnom

        # needed even if we only want to get an integration ID?
        status_data = AutoProcStatus()
        status_data.step = "Indexing"
        status_data.status = "Launched"
        status_data.comments = comments

        # Program
        autoProcProgram = EDHandlerXSDataISPyBv1_4.createAutoProcProgram(
            programId=None,
            status="RUNNING",
            timeStart=self.timeStart,
            timeEnd=self.timeEnd,
            processingCommandLine=self.processingCommandLine,
            processingPrograms=self.processingPrograms,
        )

        status_input.AutoProcProgram = autoProcProgram
        status_input.AutoProcStatus = status_data

        autoproc_status.dataInput = status_input
        # get our EDNAproc status id
        autoproc_status.executeSynchronous()
        return (
            autoproc_status.dataOutput.autoProcIntegrationId,
            autoproc_status.dataOutput.autoProcProgramId,
        )

    def parse_aimless(self, filepath):
        # mapping between the start of the line and the name of the property
        # in the ispyb data object thing
        INTERESTING_LINES = {
            "Low resolution limit": "resolutionLimitLow",
            "High resolution limit": "resolutionLimitHigh",
            "Mean((I)/sd(I))": "meanIOverSigI",
            "Completeness": "completeness",
            "Multiplicity": "multiplicity",
            "Total number of observations": "nTotalObservations",
            "Total number unique": "ntotalUniqueObservations",
            "Rmerge  (within I+/I-)": "rMerge",
            "Rmeas (within I+/I-)": "rMeasWithinIPlusIMinus",
            "Rmeas (all I+ & I-)": "rMeasAllIPlusIMinus",
            "Rpim (within I+/I-)": "rPimWithinIPlusIMinus",
            "Rpim (all I+ & I-)": "rPimAllIPlusIMinus",
            "Anomalous completeness": "anomalousCompleteness",
            "Anomalous multiplicity": "anomalousMultiplicity",
            "Mn(I) half-set correlation CC(1/2)": "ccHalf",
        }

        UNIT_CELL_PREFIX = "Average unit cell:"  # special case, 6 values
        lines = []
        inner_stats = {"scalingStatisticsType": "innerShell"}
        outer_stats = {"scalingStatisticsType": "outerShell"}
        overall_stats = {"scalingStatisticsType": "overall"}
        unit_cell = None
        with open(filepath, "r") as f:
            lines = f.readlines()
        started = False
        for line in lines:
            # avoid all the stuff before the final summary
            if line.startswith("<!--SUMMARY_BEGIN--> $TEXT:Result: $$ $$"):
                started = True
            if started:
                for prefix, prop_name in INTERESTING_LINES.items():
                    if line.startswith(prefix):
                        # We need to multiply the values for rMerge by 100
                        factor = (
                            100
                            if prop_name.lower().startswith("rm")
                            or prop_name.lower().startswith("rp")
                            else 1
                        )
                        # 3 last columns are the values we're after
                        overall, inner, outer = [
                            float(x) * factor for x in line.split()[-3:]
                        ]
                        overall_stats[prop_name] = overall
                        inner_stats[prop_name] = inner
                        outer_stats[prop_name] = outer
                if line.startswith(UNIT_CELL_PREFIX):
                    unit_cell = list(map(float, line.split()[-6:]))
        return inner_stats, outer_stats, overall_stats, unit_cell

    def eiger_template_to_image(self, fmt, num):
        fileNumber = int(num / 100)
        if fileNumber == 0:
            fileNumber = 1
        fmt_string = fmt.replace("??????", "data_%06d" % fileNumber)
        return fmt_string.format(num)

    def createInputFile(self, data_collection_id, directory):
        inputFilePath = os.path.join(directory, "XDS.INP")
        if "Test" in EDUtilsPath.getEdnaSite():
            pipe1 = subprocess.Popen(
                "/opt/pxsoft/bin/xdsinp2 -t {0}".format(data_collection_id),
                shell=True,
                stdout=subprocess.PIPE,
                close_fds=True,
            )
        else:
            pipe1 = subprocess.Popen(
                "/opt/pxsoft/bin/xdsinp2 {0}".format(data_collection_id),
                shell=True,
                stdout=subprocess.PIPE,
                close_fds=True,
            )
        xdsInp = pipe1.communicate()[0]
        with open(inputFilePath, "w") as f:
            f.write(str(xdsInp))
        return inputFilePath


def _create_scaling_stats(xscale_stats, stats_type, lowres, anom):
    stats = AutoProcScalingStatistics()
    stats.scalingStatisticsType = stats_type
    stats.resolutionLimitLow = lowres
    if stats_type != "overall":
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
    start = fmt.find("?")
    end = fmt.rfind("?")
    if start == -1 or end == -1:
        # the caller test for the file existence and an empty path
        # does not exist
        return ""
    prefix = fmt[:start]
    suffix = fmt[end + 1:]
    length = end - start + 1

    # this is essentially the python format string equivalent to the
    # template string
    fmt_string = prefix + "{0:0" + str(length) + "d}" + suffix

    return fmt_string.format(num)


# taken straight from max's code
SPACE_GROUP_NAMES = {
    1: " P 1 ",
    2: " P -1 ",
    3: " P 1 2 1 ",
    4: " P 1 21 1 ",
    5: " C 1 2 1 ",
    6: " P 1 m 1 ",
    7: " P 1 c 1 ",
    8: " C 1 m 1 ",
    9: " C 1 c 1 ",
    10: " P 1 2/m 1 ",
    11: " P 1 21/m 1 ",
    12: " C 1 2/m 1 ",
    13: " P 1 2/c 1 ",
    14: " P 1 21/c 1 ",
    15: " C 1 2/c 1 ",
    16: " P 2 2 2 ",
    17: " P 2 2 21 ",
    18: " P 21 21 2 ",
    19: " P 21 21 21 ",
    20: " C 2 2 21 ",
    21: " C 2 2 2 ",
    22: " F 2 2 2 ",
    23: " I 2 2 2 ",
    24: " I 21 21 21 ",
    25: " P m m 2 ",
    26: " P m c 21 ",
    27: " P c c 2 ",
    28: " P m a 2 ",
    29: " P c a 21 ",
    30: " P n c 2 ",
    31: " P m n 21 ",
    32: " P b a 2 ",
    33: " P n a 21 ",
    34: " P n n 2 ",
    35: " C m m 2 ",
    36: " C m c 21 ",
    37: " C c c 2 ",
    38: " A m m 2 ",
    39: " A b m 2 ",
    40: " A m a 2 ",
    41: " A b a 2 ",
    42: " F m m 2 ",
    43: " F d d 2 ",
    44: " I m m 2 ",
    45: " I b a 2 ",
    46: " I m a 2 ",
    47: " P m m m ",
    48: " P n n n ",
    49: " P c c m ",
    50: " P b a n ",
    51: " P m m a1 ",
    52: " P n n a1 ",
    53: " P m n a1 ",
    54: " P c c a1 ",
    55: " P b a m1 ",
    56: " P c c n1 ",
    57: " P b c m1 ",
    58: " P n n m1 ",
    59: " P m m n1 ",
    60: " P b c n1 ",
    61: " P b c a1 ",
    62: " P n m a1 ",
    63: " C m c m1 ",
    64: " C m c a1 ",
    65: " C m m m ",
    66: " C c c m ",
    67: " C m m a ",
    68: " C c c a ",
    69: " F m m m ",
    70: " F d d d ",
    71: " I m m m ",
    72: " I b a m ",
    73: " I b c a1 ",
    74: " I m m a1 ",
    75: " P 4 ",
    76: " P 41 ",
    77: " P 42 ",
    78: " P 43 ",
    79: " I 4 ",
    80: " I 41 ",
    81: " P -4 ",
    82: " I -4 ",
    83: " P 4/m ",
    84: " P 42/m ",
    85: " P 4/n ",
    86: " P 42/n ",
    87: " I 4/m ",
    88: " I 41/a ",
    89: " P 4 2 2 ",
    90: " P 4 21 2 ",
    91: " P 41 2 2 ",
    92: " P 41 21 2 ",
    93: " P 42 2 2 ",
    94: " P 42 21 2 ",
    95: " P 43 2 2 ",
    96: " P 43 21 2 ",
    97: " I 4 2 2 ",
    98: " I 41 2 2 ",
    99: " P 4 m m ",
    100: " P 4 b m ",
    101: " P 42 c m ",
    102: " P 42 n m ",
    103: " P 4 c c ",
    104: " P 4 n c ",
    105: " P 42 m c ",
    106: " P 42 b c ",
    107: " I 4 m m ",
    108: " I 4 c m ",
    109: " I 41 m d ",
    110: " I 41 c d ",
    111: " P -4 2 m ",
    112: " P -4 2 c ",
    113: " P -4 21 m ",
    114: " P -4 21 c ",
    115: " P -4 m 2 ",
    116: " P -4 c 2 ",
    117: " P -4 b 2 ",
    118: " P -4 n 2 ",
    119: " I -4 m 2 ",
    120: " I -4 c 2 ",
    121: " I -4 2 m ",
    122: " I -4 2 d ",
    123: " P 4/m m m ",
    124: " P 4/m c c ",
    125: " P 4/n b m ",
    126: " P 4/n n c ",
    127: " P 4/m b m1 ",
    128: " P 4/m n c1 ",
    129: " P 4/n m m1 ",
    130: " P 4/n c c1 ",
    131: " P 42/m m c ",
    132: " P 42/m c m ",
    133: " P 42/n b c ",
    134: " P 42/n n m ",
    135: " P 42/m b c ",
    136: " P 42/m n m ",
    137: " P 42/n m c ",
    138: " P 42/n c m ",
    139: " I 4/m m m ",
    140: " I 4/m c m ",
    141: " I 41/a m d ",
    142: " I 41/a c d ",
    143: " P 3 ",
    144: " P 31 ",
    145: " P 32 ",
    146: " H 3 ",
    147: " P -3 ",
    148: " H -3 ",
    149: " P 3 1 2 ",
    150: " P 3 2 1 ",
    151: " P 31 1 2 ",
    152: " P 31 2 1 ",
    153: " P 32 1 2 ",
    154: " P 32 2 1 ",
    155: " H 3 2 ",
    156: " P 3 m 1 ",
    157: " P 3 1 m ",
    158: " P 3 c 1 ",
    159: " P 3 1 c ",
    160: " H 3 m ",
    161: " H 3 c ",
    162: " P -3 1 m ",
    163: " P -3 1 c ",
    164: " P -3 m 1 ",
    165: " P -3 c 1 ",
    166: " H -3 m ",
    167: " H -3 c ",
    168: " P 6 ",
    169: " P 61 ",
    170: " P 65 ",
    171: " P 62 ",
    172: " P 64 ",
    173: " P 63 ",
    174: " P -6 ",
    175: " P 6/m ",
    176: " P 63/m ",
    177: " P 6 2 2 ",
    178: " P 61 2 2 ",
    179: " P 65 2 2 ",
    180: " P 62 2 2 ",
    181: " P 64 2 2 ",
    182: " P 63 2 2 ",
    183: " P 6 m m ",
    184: " P 6 c c ",
    185: " P 63 c m ",
    186: " P 63 m c ",
    187: " P -6 m 2 ",
    188: " P -6 c 2 ",
    189: " P -6 2 m ",
    190: " P -6 2 c ",
    191: " P 6/m m m ",
    192: " P 6/m c c ",
    193: " P 63/m c m ",
    194: " P 63/m m c ",
    195: " P 2 3 ",
    196: " F 2 3 ",
    197: " I 2 3 ",
    198: " P 21 3 ",
    199: " I 21 3 ",
    200: " P m -3 ",
    201: " P n -3 ",
    202: " F m -3 ",
    203: " F d -3 ",
    204: " I m -3 ",
    205: " P a -31 ",
    206: " I a -31 ",
    207: " P 4 3 2 ",
    208: " P 42 3 2 ",
    209: " F 4 3 2 ",
    210: " F 41 3 2 ",
    211: " I 4 3 2 ",
    212: " P 43 3 2 ",
    213: " P 41 3 2 ",
    214: " I 41 3 2 ",
    215: " P -4 3 m ",
    216: " F -4 3 m ",
    217: " I -4 3 m ",
    218: " P -4 3 n ",
    219: " F -4 3 c ",
    220: " I -4 3 d ",
    221: " P m -3 m ",
    222: " P n -3 n ",
    223: " P m -3 n1 ",
    224: " P n -3 m1 ",
    225: " F m -3 m ",
    226: " F m -3 c ",
    227: " F d -3 m1 ",
    228: " F d -3 c1 ",
    229: " I m -3 m ",
    230: " I a -3 d1 ",
}


SPACE_GROUP_NUMBERS = {
    "P1": 1,
    "P-1": 2,
    "P121": 3,
    "P1211": 4,
    "C121": 5,
    "P1M1": 6,
    "P1C1": 7,
    "C1M1": 8,
    "C1C1": 9,
    "P12/M1": 10,
    "P121/M1": 11,
    "C12/M1": 12,
    "P12/C1": 13,
    "P121/C1": 14,
    "C12/C1": 15,
    "P222": 16,
    "P2221": 17,
    "P21212": 18,
    "P212121": 19,
    "C2221": 20,
    "C222": 21,
    "F222": 22,
    "I222": 23,
    "I212121": 24,
    "PMM2": 25,
    "PMC21": 26,
    "PCC2": 27,
    "PMA2": 28,
    "PCA21": 29,
    "PNC2": 30,
    "PMN21": 31,
    "PBA2": 32,
    "PNA21": 33,
    "PNN2": 34,
    "CMM2": 35,
    "CMC21": 36,
    "CCC2": 37,
    "AMM2": 38,
    "ABM2": 39,
    "AMA2": 40,
    "ABA2": 41,
    "FMM2": 42,
    "FDD2": 43,
    "IMM2": 44,
    "IBA2": 45,
    "IMA2": 46,
    "PMMM": 47,
    "PNNN": 48,
    "PCCM": 49,
    "PBAN": 50,
    "PMMA1": 51,
    "PNNA1": 52,
    "PMNA1": 53,
    "PCCA1": 54,
    "PBAM1": 55,
    "PCCN1": 56,
    "PBCM1": 57,
    "PNNM1": 58,
    "PMMN1": 59,
    "PBCN1": 60,
    "PBCA1": 61,
    "PNMA1": 62,
    "CMCM1": 63,
    "CMCA1": 64,
    "CMMM": 65,
    "CCCM": 66,
    "CMMA": 67,
    "CCCA": 68,
    "FMMM": 69,
    "FDDD": 70,
    "IMMM": 71,
    "IBAM": 72,
    "IBCA1": 73,
    "IMMA1": 74,
    "P4": 75,
    "P41": 76,
    "P42": 77,
    "P43": 78,
    "I4": 79,
    "I41": 80,
    "P-4": 81,
    "I-4": 82,
    "P4/M": 83,
    "P42/M": 84,
    "P4/N": 85,
    "P42/N": 86,
    "I4/M": 87,
    "I41/A": 88,
    "P422": 89,
    "P4212": 90,
    "P4122": 91,
    "P41212": 92,
    "P4222": 93,
    "P42212": 94,
    "P4322": 95,
    "P43212": 96,
    "I422": 97,
    "I4122": 98,
    "P4MM": 99,
    "P4BM": 100,
    "P42CM": 101,
    "P42NM": 102,
    "P4CC": 103,
    "P4NC": 104,
    "P42MC": 105,
    "P42BC": 106,
    "I4MM": 107,
    "I4CM": 108,
    "I41MD": 109,
    "I41CD": 110,
    "P-42M": 111,
    "P-42C": 112,
    "P-421M": 113,
    "P-421C": 114,
    "P-4M2": 115,
    "P-4C2": 116,
    "P-4B2": 117,
    "P-4N2": 118,
    "I-4M2": 119,
    "I-4C2": 120,
    "I-42M": 121,
    "I-42D": 122,
    "P4/MMM": 123,
    "P4/MCC": 124,
    "P4/NBM": 125,
    "P4/NNC": 126,
    "P4/MBM1": 127,
    "P4/MNC1": 128,
    "P4/NMM1": 129,
    "P4/NCC1": 130,
    "P42/MMC": 131,
    "P42/MCM": 132,
    "P42/NBC": 133,
    "P42/NNM": 134,
    "P42/MBC": 135,
    "P42/MNM": 136,
    "P42/NMC": 137,
    "P42/NCM": 138,
    "I4/MMM": 139,
    "I4/MCM": 140,
    "I41/AMD": 141,
    "I41/ACD": 142,
    "P3": 143,
    "P31": 144,
    "P32": 145,
    "H3": 146,
    "P-3": 147,
    "H-3": 148,
    "P312": 149,
    "P321": 150,
    "P3112": 151,
    "P3121": 152,
    "P3212": 153,
    "P3221": 154,
    "H32": 155,
    "P3M1": 156,
    "P31M": 157,
    "P3C1": 158,
    "P31C": 159,
    "H3M": 160,
    "H3C": 161,
    "P-31M": 162,
    "P-31C": 163,
    "P-3M1": 164,
    "P-3C1": 165,
    "H-3M": 166,
    "H-3C": 167,
    "P6": 168,
    "P61": 169,
    "P65": 170,
    "P62": 171,
    "P64": 172,
    "P63": 173,
    "P-6": 174,
    "P6/M": 175,
    "P63/M": 176,
    "P622": 177,
    "P6122": 178,
    "P6522": 179,
    "P6222": 180,
    "P6422": 181,
    "P6322": 182,
    "P6MM": 183,
    "P6CC": 184,
    "P63CM": 185,
    "P63MC": 186,
    "P-6M2": 187,
    "P-6C2": 188,
    "P-62M": 189,
    "P-62C": 190,
    "P6/MMM": 191,
    "P6/MCC": 192,
    "P63/MCM": 193,
    "P63/MMC": 194,
    "P23": 195,
    "F23": 196,
    "I23": 197,
    "P213": 198,
    "I213": 199,
    "PM-3": 200,
    "PN-3": 201,
    "FM-3": 202,
    "FD-3": 203,
    "IM-3": 204,
    "PA-31": 205,
    "IA-31": 206,
    "P432": 207,
    "P4232": 208,
    "F432": 209,
    "F4132": 210,
    "I432": 211,
    "P4332": 212,
    "P4132": 213,
    "I4132": 214,
    "P-43M": 215,
    "F-43M": 216,
    "I-43M": 217,
    "P-43N": 218,
    "F-43C": 219,
    "I-43D": 220,
    "PM-3M": 221,
    "PN-3N": 222,
    "PM-3N1": 223,
    "PN-3M1": 224,
    "FM-3M": 225,
    "FM-3C": 226,
    "FD-3M1": 227,
    "FD-3C1": 228,
    "IM-3M": 229,
    "IA-3D1": 230,
}
