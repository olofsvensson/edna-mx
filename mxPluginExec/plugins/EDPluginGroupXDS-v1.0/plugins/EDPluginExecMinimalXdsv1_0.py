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


import os
import os.path
import shutil
import fnmatch

from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDVerbose import EDVerbose
from EDUtilsPath import EDUtilsPath
from EDUtilsFile import EDUtilsFile

from XSDataCommon import XSDataBoolean
from XSDataXDSv1_0 import XSDataMinimalXdsIn
from XSDataXDSv1_0 import XSDataMinimalXdsOut
from xdscfgparser import parse_xds_file, dump_xds_file



class EDPluginExecMinimalXdsv1_0(EDPluginExecProcessScript):


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataMinimalXdsIn)
        self.setDataOutput(XSDataMinimalXdsOut())
        self.dataOutput.succeeded = XSDataBoolean(False)
        self.maxNoProcessors = 10
        self.maxNoJobs = 1
        self.pathToNeggiaPlugin = None

    def configure(self):
        EDPluginExecProcessScript.configure(self)
        self.DEBUG("EDPluginExecMinimalXdsv1_0.configure")
        self.maxNoProcessors = self.config.get("maxNoProcessors", self.maxNoProcessors)
        self.maxNoJobs = self.config.get("maxNoJobs", self.maxNoJobs)
        self.pathToNeggiaPlugin = self.config.get("pathToNeggiaPlugin")


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecMinimalXdsv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.input_file, "No XDS input file given")

        # really look into the mandatory arg
        xds_input = os.path.abspath(self.dataInput.input_file.value)
        if not (os.path.exists(xds_input) and os.path.isfile(xds_input)):
            strErrorMessage = "Cannot find or read XDS input file {0}".format(xds_input)
            self.ERROR(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.dataOutput.succeeded = XSDataBoolean(False)
            self.setFailure()
            return

        # if we have a resolution it has to be a list of 2 XSDataDouble
        resrange = self.dataInput.resolution_range
        if resrange is not None and len(resrange) != 0:
            # a non specified list input parameter has a default value
            # of [], seriously???
            if len(resrange) != 2:
                strErrorMessage = "Resolution range must be 2 in length ({0} given)".format(resrange)
                self.ERROR(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.dataOutput.succeeded = XSDataBoolean(False)
                self.setFailure()
                return


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginMinimalXDS.preProcess")
        xds_input = os.path.abspath(self.dataInput.input_file.value)
        workingDirectory = self.getWorkingDirectory()
        if not os.path.exists(workingDirectory):
            os.makedirs(workingDirectory, 0o755)
        shutil.copy(xds_input, workingDirectory)

        # our new xds file
        xds_file = os.path.join(self.getWorkingDirectory(), 'XDS.INP')

        parsed_config = parse_xds_file(xds_file)

        file_template = parsed_config['NAME_TEMPLATE_OF_DATA_FRAMES='][0]

        # Find out the real path for the template
        file_template_real_path = os.path.join(os.path.dirname(xds_input), file_template)

        # get the real directory the files are in by getting the real
        # path of the first image
        first_image_no = parsed_config['DATA_RANGE='][0]
        first_image = _template_to_image(file_template_real_path, first_image_no)

        parsed_config['NAME_TEMPLATE_OF_DATA_FRAMES='] = file_template_real_path

        # perhaps modify some params
        job = self.dataInput.job
        maxproc = self.dataInput.maxproc
        maxjobs = self.dataInput.maxjobs
        resolution_range = self.dataInput.resolution_range
        friedels_law = self.dataInput.friedels_law
        spot_range = self.dataInput.spot_range
        spacegroup = self.dataInput.spacegroup
        unit_cell = self.dataInput.unit_cell

        self.DEBUG('requested spot range is {0}'.format(spot_range))

        if job is not None:
            parsed_config["JOB="] = job.value
        if maxproc is not None:
            parsed_config["MAXIMUM_NUMBER_OF_PROCESSORS="] = maxproc.value
        if maxjobs is not None:
            parsed_config["MAXIMUM_NUMBER_OF_JOBS="] = maxjobs.value
        if resolution_range is not None and len(resolution_range) != 0:
            parsed_config["INCLUDE_RESOLUTION_RANGE="] = [x.value for x in resolution_range]
        if friedels_law is not None:
            if friedels_law.value:
                parsed_config["FRIEDEL'S_LAW="] = "TRUE"
            else:
                parsed_config["FRIEDEL'S_LAW="] = "FALSE"
        if self.dataInput.start_image is not None:
            start_image = self.dataInput.start_image.value
            parsed_config['DATA_RANGE='][0] = start_image
        else:
            start_image = parsed_config['DATA_RANGE='][0]
        if self.dataInput.end_image is not None:
            end_image = self.dataInput.end_image.value
            parsed_config['DATA_RANGE='][1] = end_image
        else:
            end_image = parsed_config['DATA_RANGE='][1]
        spot_range_list = list()
        if spot_range is not None and len(spot_range) > 0:
            spot_range_list = []
            for srange in spot_range:
                spot_range_list.append([srange.begin, srange.end])
            spot_range_list = self.checkSpotRanges(spot_range_list, start_image, end_image)
        elif 'SPOT_RANGE=' in parsed_config:
            spot_range_list = self.checkSpotRanges(parsed_config['SPOT_RANGE='], start_image, end_image)
        else:
            spot_range_list = [[start_image, end_image]]
        self.DEBUG('setting the spot range to {0}'.format(spot_range_list))
        parsed_config['SPOT_RANGE='] = spot_range_list
        # Check background range
        if 'BACKGROUND_RANGE=' in parsed_config:
            background_range = parsed_config['BACKGROUND_RANGE=']
            if background_range[0] < start_image:
                background_range[0] = start_image
                background_range[1] += start_image - 1
            if background_range[1] > end_image:
                background_range[1] = end_image
            parsed_config['BACKGROUND_RANGE='] = background_range
        # unit cell might be an empty string or some other crazy stuff
        # we need 6 floats/ints
        if unit_cell is not None:
            ucells = unit_cell.value.split(' ')
            if len(ucells) != 6:
                unit_cell = None
            else:
                try:
                    if any(float(x) == 0 for x in ucells):
                        unit_cell = None
                except ValueError:
                    unit_cell = None
        # both need to be specified
        if spacegroup is not None and unit_cell is not None:
            self.DEBUG('specific spacegroup requested: {0}'.format(spacegroup.value))
            self.DEBUG('specific unit cell requested: {0}'.format(unit_cell.value))
            parsed_config['SPACE_GROUP_NUMBER='] = str(spacegroup.value)
            # Check if this is ok
            parsed_config['UNIT_CELL_CONSTANTS='] = unit_cell.value

        # For [XY]-GEO_CORR files, link them in the cwd and fix their paths
        if 'X-GEO_CORR=' in parsed_config:
            xgeo = parsed_config['X-GEO_CORR='][0]
            xgeo_path = os.path.join(self.getWorkingDirectory(), os.path.basename(xgeo))
            if not os.path.exists(xgeo_path):
                os.symlink(xgeo, xgeo_path)
            parsed_config['X-GEO_CORR='] = os.path.basename(xgeo)
        if 'Y-GEO_CORR=' in parsed_config:
            ygeo = parsed_config['Y-GEO_CORR='][0]
            ygeo_path = os.path.join(self.getWorkingDirectory(), os.path.basename(ygeo))
            if not os.path.exists(ygeo_path):
                os.symlink(ygeo, ygeo_path)
            parsed_config['Y-GEO_CORR='] = os.path.basename(ygeo)

        # Neggia plugin
        if not "LIB=" in parsed_config and \
                self.pathToNeggiaPlugin is not None and \
                file_template.lower().endswith("h5"):
            parsed_config["LIB="] = self.pathToNeggiaPlugin

        # Max no processors and Jobs
        if not EDUtilsPath.isEMBL():
            parsed_config['MAXIMUM_NUMBER_OF_PROCESSORS='] = str(self.maxNoProcessors)
        parsed_config['MAXIMUM_NUMBER_OF_JOBS='] = self.maxNoJobs

        # Save back the changes
        dump_xds_file(xds_file, parsed_config)

    def process(self, _edObject=None):
        EDPluginExecProcessScript.process(self)
        self.DEBUG("EDPluginMinimalXds.process")


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginMinimalXds.postProcess")
        # Check log for warning and errors
        strPathToLogFile = os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName())
        self.checkLogForWarningAndErrors(strPathToLogFile)


        # XDS is considered to have succeeded iff CORRECT.LP has been created
        outfile = os.path.join(self.getWorkingDirectory(), 'CORRECT.LP')
        self.DEBUG('looking for {0}'.format(outfile))
        if not os.path.isfile(outfile):
            self.DEBUG('NOT FOUND')
            self.dataOutput.succeeded = XSDataBoolean(False)
            strErrorMessage = "Cannot find CORRECT.LP output file"
            self.ERROR(strErrorMessage)
            if len(self.getListOfErrorMessages()) == 0:
                self.addErrorMessage(strErrorMessage)
            else:
                self.addWarningMessage(strErrorMessage)
            self.setFailure()
            return
        else:
            self.DEBUG('FOUND')
            self.dataOutput.succeeded = XSDataBoolean(True)
        self.DEBUG('succeeded is {0} and succeeded.value is {1}'.format(self.dataOutput.succeeded,
                                                                        self.dataOutput.succeeded.value))

    def checkLogForWarningAndErrors(self, _strPathToLogFile):
        """Checks the plugin/XDS log file for warning and error messages"""
        if os.path.exists(_strPathToLogFile):
            strLog = EDUtilsFile.readFile(_strPathToLogFile)
            listLog = strLog.split("\n")
            for strLogLine in listLog:
                # Check for missing images
                if "!!! ERROR " in strLogLine:
                    self.ERROR(strLogLine)
                    self.addErrorMessage(strLogLine)

    def checkSpotRanges(self, _listSpotRange, start_image, end_image):
        # Check existing spot range
        newListSpotRange = []
        for spotRange in _listSpotRange:
            if spotRange[0] >= start_image and spotRange[1] <= end_image:
                newListSpotRange.append('{0} {1}'.format(spotRange[0], spotRange[1]))
            elif spotRange[0] < start_image and spotRange[1] >= start_image and spotRange[1] <= end_image:
                newListSpotRange.append('{0} {1}'.format(start_image, spotRange[1]))
            elif spotRange[0] >= start_image and spotRange[0] <= end_image and spotRange[1] > end_image:
                newListSpotRange.append('{0} {1}'.format(spotRange[0], end_image))
        if len(newListSpotRange) == 0:
            newListSpotRange = ['{0} {1}'.format(start_image, end_image)]
        return newListSpotRange



# XXX: This is the third file I copy this function to: extract it
# somewhere
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
    suffix = fmt[end + 1:]
    length = end - start + 1

    # this is essentially the python format string equivalent to the
    # template string
    fmt_string = prefix + '{0:0' + str(length) + 'd}' + suffix

    return fmt_string.format(num)
