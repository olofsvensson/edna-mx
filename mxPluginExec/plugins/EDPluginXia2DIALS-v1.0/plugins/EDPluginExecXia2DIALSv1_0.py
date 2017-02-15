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

from XSDataXia2DIALSv1_0 import XSDataInputXia2DIALS
from XSDataXia2DIALSv1_0 import XSDataResultXia2DIALS


class EDPluginExecXia2DIALSv1_0(EDPluginExecProcessScript):
    """
    This plugin runs the Xia2DIALS program 'process' written by Global Phasing
    """


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputXia2DIALS)
        self.setDataOutput(XSDataResultXia2DIALS())
        self.maxNoProcessors = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecXia2DIALSv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")


    def configure(self):
        EDPluginExecProcessScript.configure(self)
        self.DEBUG("EDPluginExecXia2DIALSv1_0.configure")
        self.maxNoProcessors = self.config.get("maxNoProcessors", self.maxNoProcessors)

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecXia2DIALSv1_0.preProcess")
        strCommandLine = self.generateCommandLine(self.dataInput)
        self.setScriptCommandline(strCommandLine)


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecXia2DIALSv1_0.postProcess")
        # Run xia2.ispyb_xml
        currentDir = os.getcwd()
        os.chdir(self.getWorkingDirectory())
        subprocess.call("/opt/pxsoft/bin/xia2.ispyb_xml")
        os.chdir(currentDir)
        # Populate the results
        xsDataResultXia2DIALS = self.parseOutputDirectory(self.getWorkingDirectory())
        self.dataOutput = xsDataResultXia2DIALS


    def generateCommandLine(self, _xsDataInputXia2DIALS):
        """
        This method creates the input command line for Xia2DIALS
        """
        self.DEBUG("EDPluginExecXia2DIALSv1_0.generateCommands")
        strCommandText = "pipeline=dials"

        anomalous = True
        if _xsDataInputXia2DIALS.anomalous is not None:
            if not _xsDataInputXia2DIALS.anomalous.value:
                anomalous = False

        if anomalous:
            strCommandText += " atom=X"

        for image in _xsDataInputXia2DIALS.image:
            strCommandText += " image={0}".format(image.path.value)

        if self.maxNoProcessors is not None:
            strCommandText += " multiprocessing.nproc={0}".format(self.maxNoProcessors)


        return strCommandText

    def parseOutputDirectory(self, _workingDirectory):
        xsDataResultXia2DIALS = XSDataResultXia2DIALS()
        # Log file
        xia2txtPath = os.path.join(_workingDirectory, "xia2.txt")
        if os.path.exists(xia2txtPath):
            xsDataResultXia2DIALS.logFile = XSDataFile(XSDataString(xia2txtPath))
        # Html file
        xia2htmlPath = os.path.join(_workingDirectory, "xia2.html")
        if os.path.exists(xia2htmlPath):
            xsDataResultXia2DIALS.htmlFile = XSDataFile(XSDataString(xia2htmlPath))
        # Summary file
        summaryPath = os.path.join(_workingDirectory, "xia2-summary.dat")
        if os.path.exists(summaryPath):
            xsDataResultXia2DIALS.summary = XSDataFile(XSDataString(summaryPath))
        # ISPyB XML file
        ispybXmlPath = os.path.join(_workingDirectory, "ispyb.xml")
        if os.path.exists(ispybXmlPath):
            xsDataResultXia2DIALS.ispybXML = XSDataFile(XSDataString(ispybXmlPath))
        # Datafiles
        dataFiles = glob.glob(os.path.join(_workingDirectory, "DataFiles", "*"))
        for dataFile in dataFiles:
            xsDataResultXia2DIALS.addDataFiles(XSDataFile(XSDataString(dataFile)))
        # Log files
        logFiles = glob.glob(os.path.join(_workingDirectory, "LogFiles", "*"))
        for logFile in logFiles:
            xsDataResultXia2DIALS.addLogFiles(XSDataFile(XSDataString(logFile)))
        return xsDataResultXia2DIALS
