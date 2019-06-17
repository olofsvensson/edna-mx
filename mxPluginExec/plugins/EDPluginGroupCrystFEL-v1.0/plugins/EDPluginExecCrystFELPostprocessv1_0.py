# coding: utf8
#
#    Project: MX Plugin Exec
#             http://www.edna-site.org
#
#    Copyright (C) ESRF
#
#    Principal author:       Olof Svensson
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

__author__ = "Ivars Karpics"
__license__ = "GPLv3+"
__copyright__ = "EMBL Hamburg"

import os

from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataCommon import XSDataDouble, XSDataString, XSDataFile

from XSDataCrystFELv1_0 import XSDataInputCrystFEL
from XSDataCrystFELv1_0 import XSDataResultCrystFEL


class EDPluginExecCrystFELPostprocessv1_0(EDPluginExecProcessScript):
    """
    This plugin runs the CrystFEL program
    """


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputCrystFEL)
        self.setDataOutput(XSDataResultCrystFEL())

        #TODO move to input file
        self.partialator_options = "--max-adu=65000 --iterations=1 --model=unity -j 60"
        self.mtz_filename = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecCrystFELPostprocessv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")


    def configure(self):
        EDPluginExecProcessScript.configure(self)
        self.DEBUG("EDPluginExecCrystFELPostprocessv1_0.configure")

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecCrystFELPostprocessv1_0.preProcess")

        self.mtz_filename = "%s_partialator_%s.mtz" % (
            self.dataInput.baseFileName.value,
            self.dataInput.pointGroup.value
        )

        strCommandLine = self.generateCommandLine(self.dataInput)
        self.setScriptCommandline(strCommandLine)


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecCrystFELPostprocessv1_0.postProcess")
        # Populate the results
        xsDataResultCrystFEL = self.parseOutputDirectory(self.getWorkingDirectory())
        self.dataOutput = xsDataResultCrystFEL

        strErrorMessage = "EDPluginExecCrystFELPostprocessv1_0.postProcess: "
        if not os.path.exists(self.mtz_filename):
            strErrorMessage += "No mtz file %s generated" % self.mtz_filename
            self.ERROR(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
        else:
            #Parse results
            #We find the *stasummary*.dat file
            #TODO open file directly
            stats_summary_filename = None
            for filename in os.listdir(os.path.dirname(self.mtz_filename)):
                full_path = os.path.join(os.path.dirname(self.mtz_filename), filename)
                if "statsummary" in filename and filename.endswith("dat"):
                    stats_summary_filename = full_path
                file_ext = os.path.splitext(filename)[1][1:]
                if file_ext in ("log"):
                    self.dataOutput.addLogFiles(XSDataFile(XSDataString(full_path)))
                if file_ext in ("hkl", "mtz", "dat"):
                    self.dataOutput.addDataFiles(XSDataFile(XSDataString(full_path)))

            if not stats_summary_filename:
                strErrorMessage += "Unable to find summary stats file"
                self.ERROR(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
            else:
                self.dataOutput.summaryFile = XSDataFile(XSDataString(stats_summary_filename))
                stats_summary_file = open(stats_summary_filename)
                comment = "CrystFEL: "

                for row, line in enumerate(stats_summary_file.readlines()):
                    if row < 2:
                        comment += line
                    if line.startswith("overall Compl"):
                        self.dataOutput.overallCompl = XSDataDouble(float(line[17:22]))
                    elif line.startswith("overall Red"):
                        self.dataOutput.overallRed = XSDataDouble(float(line[17:22]))
                    elif line.startswith("overall <snr>"):
                        self.dataOutput.overallSnr = XSDataDouble(float(line[17:22]))
                    elif line.startswith("overall Rsplit"):
                        self.dataOutput.overallRsplit = XSDataDouble(float(line[17:22]))
                    elif line.startswith("overall CC"):
                        self.dataOutput.overallCC = XSDataDouble(float(line[17:22]))
                    if row == 13:
                        self.dataOutput.resolutionLimitLow = XSDataDouble(float(line[:7]))
                    elif row == 22:
                        self.dataOutput.resolutionLimitHigh = XSDataDouble(float(line[:7]))
                stats_summary_file.close
                self.dataOutput.comment = XSDataString(comment.replace("  ", " ").replace("\n", " "))

    def generateCommandLine(self, _xsDataInputCrystFEL):
        """
        This method creates the input command line for CrystFEL
        """
        self.DEBUG("EDPluginExecCrystFELPostprocessv1_0.generateCommands")
     
        strCommandText = "%s.stream %s %s %s %s -partialator -onlystats" % (
            _xsDataInputCrystFEL.baseFileName.value,
            _xsDataInputCrystFEL.cellFile.value,
            _xsDataInputCrystFEL.pointGroup.value,
            _xsDataInputCrystFEL.spaceGroup.value,
            _xsDataInputCrystFEL.resCutOff.value
        )
        return  strCommandText

    def parseOutputDirectory(self, _workingDirectory):
        xsDataResultCrystFEL = XSDataResultCrystFEL()
        return xsDataResultCrystFEL
