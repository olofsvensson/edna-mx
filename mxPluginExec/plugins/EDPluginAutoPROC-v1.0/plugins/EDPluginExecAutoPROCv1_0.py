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

from EDUtilsPath import EDUtilsPath


class EDPluginExecAutoPROCv1_0(EDPluginExecProcessScript):
    """
    This plugin runs the autoPROC program 'process' written by Global Phasing
    """


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputAutoPROC)
        self.setDataOutput(XSDataResultAutoPROC())
        self.maxNoProcessors = 12
        self.pathToNeggiaPlugin = None
        self.doScaleWithXscale = False
        self.rotationAxis = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecAutoPROCv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")


    def configure(self):
        EDPluginExecProcessScript.configure(self)
        self.DEBUG("EDPluginExecAutoPROCv1_0.configure")
        self.maxNoProcessors = self.config.get("maxNoProcessors", self.maxNoProcessors)
        self.pathToNeggiaPlugin = self.config.get("pathToNeggiaPlugin")
        self.doScaleWithXscale = self.config.get("scaleWithXscale", self.doScaleWithXscale)
        self.rotationAxis = self.config.get("rotationAxis", self.rotationAxis)

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
        # ISPyB XML files
        ispybXML = os.path.join(strWorkingDir, "autoPROC.xml")
        if os.path.exists(ispybXML):
            self.dataOutput.ispybXML = XSDataFile(XSDataString(ispybXML))
        ispybXML_staraniso = os.path.join(strWorkingDir, "autoPROC_staraniso.xml")
        if os.path.exists(ispybXML_staraniso):
            self.dataOutput.ispybXML_staraniso = XSDataFile(XSDataString(ispybXML_staraniso))
        # Report PDFs
        reportPdf = os.path.join(strWorkingDir, "report.pdf")
        if os.path.exists(reportPdf):
            self.dataOutput.reportPdf = XSDataFile(XSDataString(reportPdf))
        else:
            self.dataOutput.reportPdf = None
        reportPdf_staraniso = os.path.join(strWorkingDir, "report_staraniso.pdf")
        if os.path.exists(reportPdf_staraniso):
            self.dataOutput.reportPdf_staraniso = XSDataFile(XSDataString(reportPdf_staraniso))
        # Working directory
        self.dataOutput.workingDirectory = XSDataFile(XSDataString(strWorkingDir))
        # processDirectory
        if self.dataInput.masterH5:
            processDirectory = os.path.join(strWorkingDir, "HDF5_1")
            if os.path.exists(processDirectory):
                self.dataOutput.addProcessDirectory(XSDataFile(XSDataString(processDirectory)))
        else:
            for identifier in self.dataInput.identifier:
                processDirectory = os.path.join(strWorkingDir, identifier.idN.value)
                if os.path.exists(processDirectory):
                    self.dataOutput.addProcessDirectory(XSDataFile(XSDataString(processDirectory)))


    def generateCommandLine(self, _xsDataInputAutoPROC):
        """
        This method creates the input command line for autoPROC
        """
        self.DEBUG("EDPluginExecAutoPROCv1_0.generateCommands")
        strCommandText = "-B -xml -nthreads {0} -M ReportingInlined autoPROC_HIGHLIGHT=\"no\"".format(self.maxNoProcessors)

        if self.doScaleWithXscale:
            strCommandText += " autoPROC_ScaleWithXscale='yes'"

        if self.rotationAxis is not None:
            strCommandText += " XdsFormatSpecificJiffyRun=no autoPROC_XdsKeyword_ROTATION_AXIS=\"{0}\"".format(self.rotationAxis)

        # Make sure we only store PDF files in summary html file
        strCommandText += " autoPROC_Summary2Base64_ConvertExtensions=\"pdf\""

        strCommandText += " autoPROC_Summary2Base64_ModalExtensions=\"LP html log mrfana pdb stats table1 xml sca\""

        # Master H5 file
        masterH5 = _xsDataInputAutoPROC.masterH5
        if masterH5 is None:
            # Identifier(s)
            for identifier in _xsDataInputAutoPROC.identifier:

                if EDUtilsPath.isEMBL() or EDUtilsPath.isALBA():
                    identifier.templateN.value = identifier.templateN.value.replace(\
                                    '%' + '05' + 'd', 5 * '#')
                strCommandText += " -Id {idN},{dirN},{templateN},{fromN},{toN}".format(
                                    idN=identifier.idN.value,
                                    dirN=identifier.dirN.path.value,
                                    templateN=identifier.templateN.value,
                                    fromN=identifier.fromN.value,
                                    toN=identifier.toN.value)
        else:
            strCommandText += " -h5 {0}".format(masterH5.path.value)
            if self.pathToNeggiaPlugin is not None:
                strCommandText += " autoPROC_XdsKeyword_LIB={0}".format(self.pathToNeggiaPlugin)

        # Resolution
        lowResolutionLimit = _xsDataInputAutoPROC.lowResolutionLimit
        highResolutionLimit = _xsDataInputAutoPROC.highResolutionLimit
        if lowResolutionLimit is not None or highResolutionLimit is not None:
            # See https://www.globalphasing.com/autoproc/manual/autoPROC4.html#processcli
            if lowResolutionLimit is None:
                low = 1000.0  # autoPROC default value
            else:
                low = lowResolutionLimit.value
            if highResolutionLimit is None:
                high = 0.1  # autoPROC default value
            else:
                high = highResolutionLimit.value
            strCommandText += " -R {0} {1}".format(low, high)
        # Anomalous
        anomalous = _xsDataInputAutoPROC.anomalous
        if anomalous is not None:
            if anomalous.value:
                strCommandText += " -ANO"
        # Reference MTZ file
        refMTZ = _xsDataInputAutoPROC.refMTZ
        if refMTZ is not None:
            strCommandText += " -ref {0}".format(refMTZ.path.value)
        # Forced space group
        if _xsDataInputAutoPROC.symm is not None:
            strCommandText += " symm=\"{0}\"".format(_xsDataInputAutoPROC.symm.value)
        # Forced cell
        if _xsDataInputAutoPROC.cell is not None:
            strCommandText += " cell=\"{0}\"".format(_xsDataInputAutoPROC.cell.value)

        return strCommandText
