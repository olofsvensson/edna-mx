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

__author__ = "Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os
import glob

from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString

from XSDataXIA2v1_0 import XSDataInputXIA2
from XSDataXIA2v1_0 import XSDataResultXIA2


class EDPluginExecXIA2v1_0(EDPluginExecProcessScript):
    """
    This plugin runs the XIA2 program 'process' written by Global Phasing
    """


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputXIA2)
        self.setDataOutput(XSDataResultXIA2())

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecXIA2v1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecXIA2v1_0.preProcess")
        strCommandLine = self.generateCommandLine(self.dataInput)
        self.setScriptCommandline(strCommandLine)


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecXIA2v1_0.postProcess")
        # Populate the results
        xsDataResultXIA2 = self.parseOutputDirectory(self.getWorkingDirectory())
        self.dataOutput = xsDataResultXIA2


    def generateCommandLine(self, _xsDataInputXIA2):
        """
        This method creates the input command line for XIA2
        """
        self.DEBUG("EDPluginExecXIA2v1_0.generateCommands")
        strCommandText = "-dials -ispyb_xml_out ispyb.xml"

        for image in _xsDataInputXIA2.image:
            strCommandText += " image={0}".format(image.path.value)

        return strCommandText

    def parseOutputDirectory(self, _workingDirectory):
        xsDataResultXIA2 = XSDataResultXIA2()
        # Log file
        xia2txtPath = os.path.join(_workingDirectory, "xia2.txt")
        if os.path.exists(xia2txtPath):
            xsDataResultXIA2.logFile = XSDataFile(XSDataString(xia2txtPath))
        # Summary file
        summaryPath = os.path.join(_workingDirectory, "xia2-summary.dat")
        if os.path.exists(summaryPath):
            xsDataResultXIA2.summary = XSDataFile(XSDataString(summaryPath))
        # ISPyB XML file
        ispybXmlPath = os.path.join(_workingDirectory, "ispyb.xml")
        if os.path.exists(ispybXmlPath):
            xsDataResultXIA2.ispybXML = XSDataFile(XSDataString(ispybXmlPath))
        # Datafiles
        dataFiles = glob.glob(os.path.join(_workingDirectory, "DataFiles", "*"))
        for dataFile in dataFiles:
            xsDataResultXIA2.addDataFiles(XSDataFile(XSDataString(dataFile)))
        # Log files
        logFiles = glob.glob(os.path.join(_workingDirectory, "LogFiles", "*"))
        for logFile in logFiles:
            xsDataResultXIA2.addLogFiles(XSDataFile(XSDataString(logFile)))
        return xsDataResultXIA2
