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

import os, time

from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDUtilsImage import EDUtilsImage

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

from XSDataHTML2PDFv1_0 import XSDataInputHTML2PDF
from XSDataHTML2PDFv1_0 import XSDataResultHTML2PDF

class EDPluginHTML2PDFv1_0(EDPluginExecProcessScript):
    """
    This plugin runs wkhtmltopdf to create a PDF file from an html file.
    """


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputHTML2PDF)
        self.setDataOutput(XSDataResultHTML2PDF())
        self.pdfFile = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginHTML2PDFv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.htmlFile, "html file is None")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginHTML2PDFv1_0.preProcess")
        xsDataInputHTML2PDF = self.getDataInput()
        if xsDataInputHTML2PDF.resultDirectory is None:
            resultDirectory = self.getWorkingDirectory()
        else:
            resultDirectory = xsDataInputHTML2PDF.resultDirectory.path.value
        self.setScriptCommandline(self.generateCommands(xsDataInputHTML2PDF, resultDirectory))


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginHTML2PDFv1_0.postProcess")


    def finallyProcess(self, _edObject=None):
        EDPluginExecProcessScript.finallyProcess(self)
        self.DEBUG("EDPluginHTML2PDFv1_0.finallyProcess")
        if self.pdfFile is not None:
            if os.path.exists(self.pdfFile):
                self.dataOutput.pdfFile = XSDataFile(XSDataString(self.pdfFile))


    def generateCommands(self, _xsDataInputHTML2PDF, _resultDirectory):
        """
        This method create the command line for wkhtmltopdf
        """
        self.DEBUG("EDPluginHTML2PDFv1_0.generateCommands")

        listHtmlFile = _xsDataInputHTML2PDF.htmlFile
        pdfFileName = os.path.basename(listHtmlFile[0].path.value).split(".")[0] + ".pdf"
        pdfFile = os.path.join(_resultDirectory, pdfFileName)
        scriptCommandLine = ""
        if _xsDataInputHTML2PDF.lowQuality is not None:
            if _xsDataInputHTML2PDF.lowQuality.value:
                scriptCommandLine += "-l "
        if _xsDataInputHTML2PDF.paperSize is not None:
            scriptCommandLine += "-s {0} ".format(_xsDataInputHTML2PDF.paperSize.value)
        for htmlFile in listHtmlFile:
            scriptCommandLine += "{0} ".format(htmlFile.path.value, pdfFile)
        scriptCommandLine += "{0}".format(pdfFile)
        self.pdfFile = pdfFile

        return scriptCommandLine

