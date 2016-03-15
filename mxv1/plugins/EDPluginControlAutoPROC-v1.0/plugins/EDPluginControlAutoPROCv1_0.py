# coding: utf8
#
#    Project: autoPROC
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

__author__ = "Olof Svensson"
__license__ = "GPLv2+"
__copyright__ = "ESRF"

import os
import time
import shutil
import socket

from EDPluginControl import EDPluginControl
from EDHandlerESRFPyarchv1_0 import EDHandlerESRFPyarchv1_0

from EDFactoryPlugin import edFactoryPlugin

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataString
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataDouble

from XSDataControlAutoPROCv1_0 import XSDataInputControlAutoPROC
from XSDataControlAutoPROCv1_0 import XSDataResultControlAutoPROC

edFactoryPlugin.loadModule('XSDataAutoPROCv1_0')

from XSDataAutoPROCv1_0 import XSDataAutoPROCIdentifier
from XSDataAutoPROCv1_0 import XSDataInputAutoPROC

edFactoryPlugin.loadModule('XSDataISPyBv1_4')
# plugin input/output
from XSDataISPyBv1_4 import AutoProcContainer
from XSDataISPyBv1_4 import AutoProcProgramAttachment
from XSDataISPyBv1_4 import XSDataInputRetrieveDataCollection
from XSDataISPyBv1_4 import XSDataInputStoreAutoProc
from XSDataISPyBv1_4 import XSDataResultStoreAutoProc


edFactoryPlugin.loadModule("XSDataMXWaitFilev1_1")
from XSDataMXWaitFilev1_1 import XSDataInputMXWaitFile

edFactoryPlugin.loadModule("XSDataHTML2PDFv1_0")
from XSDataHTML2PDFv1_0 import XSDataInputHTML2PDF

class EDPluginControlAutoPROCv1_0(EDPluginControl):
    """
    Control plugin for autoPROC
    """


    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputControlAutoPROC)
        self.dataOutput = XSDataResultStoreAutoProc()

    def configure(self):
        EDPluginControl.configure(self)

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlAutoPROCv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.dataCollectionId, "No data collection id")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlAutoPROCv1_0.preProcess")
        self.screen("autoPROC processing started")
        self.strHost = socket.gethostname()
        self.screen("Running on {0}".format(self.strHost))
        try:
            strLoad = os.getloadavg()
            self.screen("System load avg: {0}".format(strLoad))
        except OSError:
            pass

        self.edPluginWaitFileFirst = self.loadPlugin("EDPluginMXWaitFilev1_1", "MXWaitFileFirst")
        self.edPluginWaitFileLast = self.loadPlugin("EDPluginMXWaitFilev1_1", "MXWaitFileLast")

        self.edPluginRetrieveDataCollection = self.loadPlugin("EDPluginISPyBRetrieveDataCollectionv1_4")
        self.edPluginExecAutoPROC = self.loadPlugin("EDPluginExecAutoPROCv1_0")
        self.edPluginStoreAutoproc = self.loadPlugin("EDPluginISPyBStoreAutoProcv1_4")

        self.edPluginHTML2Pdf = self.loadPlugin("EDPluginHTML2PDFv1_0")


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG('EDPluginControlAutoPROCv1_0.process starting')

        directory = None
        template = None
        imageNoStart = None
        imageNoEnd = None
        pathToStartImage = None
        pathToEndImage = None

        # If we have a data collection id, use it
        if self.dataInput.dataCollectionId is not None:
            # Recover the data collection from ISPyB
            xsDataInputRetrieveDataCollection = XSDataInputRetrieveDataCollection()
            identifier = str(self.dataInput.dataCollectionId.value)
            xsDataInputRetrieveDataCollection.dataCollectionId = self.dataInput.dataCollectionId
            self.edPluginRetrieveDataCollection.dataInput = xsDataInputRetrieveDataCollection
            self.edPluginRetrieveDataCollection.executeSynchronous()
            ispybDataCollection = self.edPluginRetrieveDataCollection.dataOutput.dataCollection
            directory = ispybDataCollection.imageDirectory
            template = ispybDataCollection.fileTemplate.replace("%04d", "####")
            imageNoStart = ispybDataCollection.startImageNumber
            imageNoEnd = imageNoStart + ispybDataCollection.numberOfImages - 1

#            # DEBUG we set the end image to 20 in order to speed up things
#            self.warning("End image set to 20 (was {0})".format(imageNoEnd))
#            imageNoEnd = 20
            pathToStartImage = os.path.join(directory, ispybDataCollection.fileTemplate % imageNoStart)
            pathToEndImage = os.path.join(directory, ispybDataCollection.fileTemplate % imageNoEnd)
        else:
            identifier = str(int(time.time()))
            directory = self.dataInput.dirN.value
            template = self.dataInput.templateN.value
            imageNoStart = self.dataInput.fromN.value
            imageNoEnd = self.dataInput.toN.value
            fileTemplate = template.replace("####", "%04d")
            pathToStartImage = os.path.join(directory, fileTemplate % imageNoStart)
            pathToEndImage = os.path.join(directory, fileTemplate % imageNoEnd)

        # Process directory
        if self.dataInput.processDirectory is not None:
            strProcessDirectory = self.dataInput.processDirectory.path.value
        else:
            strProcessDirectory = directory.replace("RAW_DATA", "PROCESSED_DATA")

        # Make results directory
        strResultsDirectory = os.path.join(strProcessDirectory, "results")
        if not os.path.exists(strResultsDirectory):
            os.makedirs(strResultsDirectory, 0755)

        # Create path to pyarch
        pyarchDirectory = EDHandlerESRFPyarchv1_0.createPyarchFilePath(strResultsDirectory)
        if pyarchDirectory is not None and not os.path.exists(pyarchDirectory):
            os.makedirs(pyarchDirectory, 0755)

        # Determine pyarch prefix
        listPrefix = template.split("_")
        strPyarchPrefix = "{0}_run{1}".format(listPrefix[-3], listPrefix[-2])


        if any(beamline in pathToStartImage for beamline in ["id23eh1", "id29"]):
            minSizeFirst = 6000000
            minSizeLast = 6000000
        elif any(beamline in pathToStartImage for beamline in ["id23eh2", "id30a1"]):
            minSizeFirst = 2000000
            minSizeLast = 2000000
        elif any(beamline in pathToStartImage for beamline in ["id30a3"]):
            minSizeFirst = 100000
            minSizeLast = 100000
            pathToStartImage = self.eiger_template_to_image(template, start_image)
            pathToEndImage = self.eiger_template_to_image(template, end_image)
        else:
            minSizeFirst = 1000000
            minSizeLast = 1000000

        fWaitFileTimeout = 3600  # s

        xsDataInputMXWaitFileFirst = XSDataInputMXWaitFile()
        xsDataInputMXWaitFileFirst.file = XSDataFile(XSDataString(pathToStartImage))
        xsDataInputMXWaitFileFirst.timeOut = XSDataTime(fWaitFileTimeout)
        self.edPluginWaitFileFirst.size = XSDataInteger(minSizeFirst)
        self.edPluginWaitFileFirst.dataInput = xsDataInputMXWaitFileFirst
        self.edPluginWaitFileFirst.executeSynchronous()
        if self.edPluginWaitFileFirst.dataOutput.timedOut.value:
            strWarningMessage = "Timeout after %d seconds waiting for the first image %s!" % (fWaitFileTimeout, pathToStartImage)
            self.addWarningMessage(strWarningMessage)
            self.WARNING(strWarningMessage)

        xsDataInputMXWaitFileLast = XSDataInputMXWaitFile()
        xsDataInputMXWaitFileLast.file = XSDataFile(XSDataString(pathToEndImage))
        xsDataInputMXWaitFileLast.timeOut = XSDataTime(fWaitFileTimeout)
        self.edPluginWaitFileLast.size = XSDataInteger(minSizeLast)
        self.edPluginWaitFileLast.dataInput = xsDataInputMXWaitFileLast
        self.edPluginWaitFileLast.executeSynchronous()
        if self.edPluginWaitFileLast.dataOutput.timedOut.value:
            strErrorMessage = "Timeout after %d seconds waiting for the last image %s!" % (fWaitFileTimeout, pathToEndImage)
            self.addErrorMessage(strErrorMessage)
            self.ERROR(strErrorMessage)
            self.setFailure()



        # Prepare input to autoPROC execution plugin
        xsDataInputAutoPROC = XSDataInputAutoPROC()
        xsDataAutoPROCIdentifier = XSDataAutoPROCIdentifier()
        xsDataAutoPROCIdentifier.idN = XSDataString(identifier)
        xsDataAutoPROCIdentifier.dirN = XSDataFile(XSDataString(directory))
        xsDataAutoPROCIdentifier.templateN = XSDataString(template)
        xsDataAutoPROCIdentifier.fromN = XSDataInteger(imageNoStart)
        xsDataAutoPROCIdentifier.toN = XSDataInteger(imageNoEnd)
        xsDataInputAutoPROC.addIdentifier(xsDataAutoPROCIdentifier)
        self.edPluginExecAutoPROC.dataInput = xsDataInputAutoPROC
        self.edPluginExecAutoPROC.executeSynchronous()

        # Read the generated ISPyB xml file
        autoProcContainer = AutoProcContainer.parseFile(self.edPluginExecAutoPROC.dataOutput.ispybXML.path.value)

        # "Fix" certain entries in the ISPyB xml file
        autoProcScalingContainer = autoProcContainer.AutoProcScalingContainer
        for autoProcScalingStatistics in autoProcScalingContainer.AutoProcScalingStatistics:
            autoProcScalingStatistics.anomalous = True
            if autoProcScalingStatistics.rMerge < 1.0:
                autoProcScalingStatistics.rMerge *= 100.0
        autoProcIntegrationContainer = autoProcScalingContainer.AutoProcIntegrationContainer
        image = autoProcIntegrationContainer.Image
        image.dataCollectionId = self.dataInput.dataCollectionId.value
        autoProcIntegration = autoProcIntegrationContainer.AutoProcIntegration
        autoProcIntegration.anomalous = True
        autoProcProgramContainer = autoProcContainer.AutoProcProgramContainer
        autoProcProgram = autoProcProgramContainer.AutoProcProgram
        autoProcProgram.processingPrograms = "autoPROC"
        autoProcProgram.processingStartTime = time.strftime("%a %b %d %H:%M:%S %Y", time.strptime(autoProcProgram.processingStartTime, "%a %b %d %H:%M:%S %Z %Y"))
        autoProcProgram.processingEndTime = time.strftime("%a %b %d %H:%M:%S %Y", time.strptime(autoProcProgram.processingEndTime, "%a %b %d %H:%M:%S %Z %Y"))
        for autoProcProgramAttachment in autoProcProgramContainer.AutoProcProgramAttachment:
            if autoProcProgramAttachment.fileName == "summary.html":
                # Convert the summary.html to summary.pdf
                summaryHtmlPath = os.path.join(autoProcProgramAttachment.filePath, autoProcProgramAttachment.fileName)
                xsDataInputHTML2PDF = XSDataInputHTML2PDF()
                xsDataInputHTML2PDF.addHtmlFile(XSDataFile(XSDataString(summaryHtmlPath)))
                xsDataInputHTML2PDF.paperSize = XSDataString("A3")
                xsDataInputHTML2PDF.lowQuality = XSDataBoolean(True)
                self.edPluginHTML2Pdf.dataInput = xsDataInputHTML2PDF
                self.edPluginHTML2Pdf.executeSynchronous()
                pdfFile = self.edPluginHTML2Pdf.dataOutput.pdfFile.path.value
                strPyarchPdfFile = strPyarchPrefix + "_" + os.path.basename(pdfFile)
                # Copy file to results directory and pyarch
                shutil.copy(pdfFile, os.path.join(strResultsDirectory, strPyarchPdfFile))
                shutil.copy(pdfFile, os.path.join(pyarchDirectory, strPyarchPdfFile))
                autoProcProgramAttachment.fileName = strPyarchPdfFile
                autoProcProgramAttachment.filePath = pyarchDirectory
            elif autoProcProgramAttachment.fileName == "truncate-unique.mtz":
                strPathtoFile = os.path.join(autoProcProgramAttachment.filePath, autoProcProgramAttachment.fileName)
                strPyarchFile = strPyarchPrefix + "_anom_truncate.mtz"
                shutil.copy(strPathtoFile, os.path.join(strResultsDirectory, strPyarchFile))
                shutil.copy(strPathtoFile, os.path.join(pyarchDirectory, strPyarchFile))
                autoProcProgramAttachment.fileName = strPyarchFile
                autoProcProgramAttachment.filePath = pyarchDirectory
            else:
                strPathtoFile = os.path.join(autoProcProgramAttachment.filePath, autoProcProgramAttachment.fileName)
                strPyarchFile = strPyarchPrefix + "_" + autoProcProgramAttachment.fileName
                shutil.copy(strPathtoFile, os.path.join(strResultsDirectory, strPyarchFile))
                shutil.copy(strPathtoFile, os.path.join(pyarchDirectory, strPyarchFile))
                autoProcProgramAttachment.fileName = strPyarchFile
                autoProcProgramAttachment.filePath = pyarchDirectory
        # Add log file
        strPathToLogFile = self.edPluginExecAutoPROC.dataOutput.logFile.path.value
        strPyarchLogFile = strPyarchPrefix + "_autoPROC.log"
        shutil.copy(strPathToLogFile, os.path.join(strResultsDirectory, strPyarchLogFile))
        shutil.copy(strPathToLogFile, os.path.join(pyarchDirectory, strPyarchLogFile))
        autoProcProgramAttachment = AutoProcProgramAttachment()
        autoProcProgramAttachment.fileName = strPyarchLogFile
        autoProcProgramAttachment.filePath = pyarchDirectory
        autoProcProgramAttachment.fileType = "Log"
        autoProcProgramContainer.addAutoProcProgramAttachment(autoProcProgramAttachment)
        print(autoProcContainer.marshal())

        # Upload the xml to ISPyB
        xsDataInputStoreAutoProc = XSDataInputStoreAutoProc()
        xsDataInputStoreAutoProc.AutoProcContainer = autoProcContainer
        self.edPluginStoreAutoproc.dataInput = xsDataInputStoreAutoProc
        self.edPluginStoreAutoproc.executeSynchronous()

    def eiger_template_to_image(self, fmt, num):
        fileNumber = int(num / 100)
        if fileNumber == 0:
            fileNumber = 1
        fmt_string = fmt.replace("??????", "data_%06d" % fileNumber)
        return fmt_string.format(num)
