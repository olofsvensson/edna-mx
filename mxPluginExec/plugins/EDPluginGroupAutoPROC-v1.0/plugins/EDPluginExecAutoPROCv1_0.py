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

from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString

from XSDataAutoPROCv1_0 import XSDataInputAutoPROC
from XSDataAutoPROCv1_0 import XSDataResultAutoPROC


class EDPluginExecAutoPROCv1_0(EDPluginExecProcessScript):
    """
    This plugin runs the autoPROC program 'process' written by Global Phasing
    """


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputAutoPROC)
        self.setDataOutput(XSDataResultAutoPROC())

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecAutoPROCv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecAutoPROCv1_0.preProcess")
        strCommandLine = self.generateCommandLine(self.dataInput)
        self.setScriptCommandline(strCommandLine)


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecAutoPROCv1_0.postProcess")
        strWorkingDir = self.getWorkingDirectory()
        # Log file
        self.dataOutput.logFile = XSDataFile(XSDataString(os.path.join(strWorkingDir, self.getScriptLogFileName())))
        # ISPyB XML file
        ispybXML = os.path.join(strWorkingDir, "autoPROC.xml")
        if os.path.exists(ispybXML):
            self.dataOutput.ispybXML = XSDataFile(XSDataString(ispybXML))
        # processDirectory
        processDirectory = os.path.join(strWorkingDir, self.dataInput.idN.value)
        if os.path.exists(processDirectory):
            self.dataOutput.processDirectory = XSDataFile(XSDataString(processDirectory))


    def generateCommandLine(self, _xsDataInputAutoPROC):
        """
        This method creates the input command line for autoPROC
        """
        self.DEBUG("EDPluginExecAutoPROCv1_0.generateCommands")
        strCommandText = "-B -xml"
        # imageDirectory
        imageDirectory = _xsDataInputAutoPROC.imageDirectory
        if imageDirectory is not None:
            strCommandText += " -I {0}".format(imageDirectory.path.value)
        # Id
        idN = _xsDataInputAutoPROC.idN
        dirN = _xsDataInputAutoPROC.dirN
        templateN = _xsDataInputAutoPROC.templateN
        fromN = _xsDataInputAutoPROC.fromN
        toN = _xsDataInputAutoPROC.toN
        if all(v is not None for v in [idN, dirN, templateN, fromN, toN]):
            strCommandText += " -Id {idN},{dirN},{templateN},{fromN},{toN}".format(
                              idN=idN.value, dirN=dirN.path.value, templateN=templateN.value,
                              fromN=fromN.value, toN=toN.value)
        # Resolution
        lowResolutionLimit = _xsDataInputAutoPROC.lowResolutionLimit
        highResolutionLimit = _xsDataInputAutoPROC.highResolutionLimit
        if lowResolutionLimit is not None and highResolutionLimit is not None:
            strCommandText += " -R {0} {1}".format(lowResolutionLimit.value, highResolutionLimit.value)
        # Anomalous
        anomalous = _xsDataInputAutoPROC.anomalous
        if anomalous is not None:
            if anomalous.value:
                strCommandText += " -ANO"
            else:
                strCommandText += " -noANO"
        # Reference MTZ file
        refMTZ = _xsDataInputAutoPROC.refMTZ
        if refMTZ is not None:
            strCommandText += " -ref {0}".format(refMTZ.path.value)
        # Master H5 file
        masterH5 = _xsDataInputAutoPROC.masterH5
        if masterH5 is not None:
            strCommandText += " -h5 {0}".format(masterH5.path.value)
        return strCommandText
