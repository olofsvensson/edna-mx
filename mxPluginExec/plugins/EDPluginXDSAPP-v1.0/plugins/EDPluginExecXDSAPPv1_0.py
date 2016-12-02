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

from XSDataXDSAPPv1_0 import XSDataInputXDSAPP
from XSDataXDSAPPv1_0 import XSDataResultXDSAPP


class EDPluginExecXDSAPPv1_0(EDPluginExecProcessScript):
    """
    This plugin runs the XDSAPP program 'process' written by Global Phasing
    """


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputXDSAPP)
        self.setDataOutput(XSDataResultXDSAPP())
        self.maxNoProcessors = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecXDSAPPv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")


    def configure(self):
        EDPluginExecProcessScript.configure(self)
        self.DEBUG("EDPluginExecXDSAPPv1_0.configure")
        self.maxNoProcessors = self.config.get("maxNoProcessors", self.maxNoProcessors)

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecXDSAPPv1_0.preProcess")
        strCommandLine = self.generateCommandLine(self.dataInput)
        self.setScriptCommandline(strCommandLine)


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecXDSAPPv1_0.postProcess")
        # Populate the results
#        xsDataResultXDSAPP = self.parseOutputDirectory(self.getWorkingDirectory())
#        self.dataOutput = xsDataResultXDSAPP


    def generateCommandLine(self, _xsDataInputXDSAPP):
        """
        This method creates the input command line for XDSAPP
        """
        self.DEBUG("EDPluginExecXDSAPPv1_0.generateCommands")
        strCommandText = ""

        # Image
        strCommandText += " --image {0}".format(_xsDataInputXDSAPP.image.path.value)

        anomalous = True
        if _xsDataInputXDSAPP.anomalous is not None:
            if not _xsDataInputXDSAPP.anomalous.value:
                anomalous = False

        if anomalous:
            strCommandText += " --fried=true"
        else:
            strCommandText += " --fried=true"

        strCommandText += " --dir={0}".format(self.getWorkingDirectory())

        print(strCommandText)
        return strCommandText

#    def parseOutputDirectory(self, _workingDirectory):
#        xsDataResultXDSAPP = XSDataResultXDSAPP()
#        # Log file
#        xia2txtPath = os.path.join(_workingDirectory, "xia2.txt")
#        if os.path.exists(xia2txtPath):
#            xsDataResultXDSAPP.logFile = XSDataFile(XSDataString(xia2txtPath))
#        # Html file
#        xia2htmlPath = os.path.join(_workingDirectory, "xia2.html")
#        if os.path.exists(xia2htmlPath):
#            xsDataResultXDSAPP.htmlFile = XSDataFile(XSDataString(xia2htmlPath))
#        # Summary file
#        summaryPath = os.path.join(_workingDirectory, "xia2-summary.dat")
#        if os.path.exists(summaryPath):
#            xsDataResultXDSAPP.summary = XSDataFile(XSDataString(summaryPath))
#        # ISPyB XML file
#        ispybXmlPath = os.path.join(_workingDirectory, "ispyb.xml")
#        if os.path.exists(ispybXmlPath):
#            xsDataResultXDSAPP.ispybXML = XSDataFile(XSDataString(ispybXmlPath))
#        # Datafiles
#        dataFiles = glob.glob(os.path.join(_workingDirectory, "DataFiles", "*"))
#        for dataFile in dataFiles:
#            xsDataResultXDSAPP.addDataFiles(XSDataFile(XSDataString(dataFile)))
#        # Log files
#        logFiles = glob.glob(os.path.join(_workingDirectory, "LogFiles", "*"))
#        for logFile in logFiles:
#            xsDataResultXDSAPP.addLogFiles(XSDataFile(XSDataString(logFile)))
#        return xsDataResultXDSAPP
