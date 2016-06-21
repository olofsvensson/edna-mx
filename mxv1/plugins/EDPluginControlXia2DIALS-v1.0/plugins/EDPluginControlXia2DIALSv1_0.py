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
from EDUtilsPath import EDUtilsPath

from EDFactoryPlugin import edFactoryPlugin

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataString
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataDouble

from XSDataControlXia2DIALSv1_0 import XSDataInputControlXia2DIALS
from XSDataControlXia2DIALSv1_0 import XSDataResultControlXia2DIALS

edFactoryPlugin.loadModule('XSDataXia2DIALSv1_0')

from XSDataXia2DIALSv1_0 import XSDataInputXia2DIALS

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

class EDPluginControlXia2DIALSv1_0(EDPluginControl):
    """
    Control plugin for xia2 -dials
    """


    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputControlXia2DIALS)
        self.dataOutput = XSDataResultStoreAutoProc()

    def configure(self):
        EDPluginControl.configure(self)

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlXia2DIALSv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.dataCollectionId, "No data collection id")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlXia2DIALSv1_0.preProcess")
        self.screen("Xia2DIALS processing started")
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
        self.edPluginExecXia2DIALS = self.loadPlugin("EDPluginExecXia2DIALSv1_0")
        self.edPluginStoreAutoproc = self.loadPlugin("EDPluginISPyBStoreAutoProcv1_4")

        self.edPluginHTML2Pdf = self.loadPlugin("EDPluginHTML2PDFv1_0")


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG('EDPluginControlXia2DIALSv1_0.process starting')

        directory = None
        template = None
        imageNoStart = None
        imageNoEnd = None
        pathToStartImage = None
        pathToEndImage = None
        userName = os.environ["USER"]
        beamline = "unknown"
        proposal = "unknown"

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

        # Try to get proposal from path
        if EDUtilsPath.isESRF():
            listDirectory = directory.split(os.sep)
            try:
                if listDirectory[1] == "data":
                    if listDirectory[2] == "visitor":
                        beamline = listDirectory[4]
                        proposal = listDirectory[3]
                    else:
                        beamline = listDirectory[2]
                        proposal = listDirectory[4]
            except:
                beamline = "unknown"
                proposal = userName


        if imageNoEnd - imageNoStart < 8:
            error_message = "There are fewer than 8 images, aborting"
            self.addErrorMessage(error_message)
            self.ERROR(error_message)
            self.setFailure()
            return

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
        pyarchDirectory = pyarchDirectory.replace('PROCESSED_DATA', 'RAW_DATA')
        if pyarchDirectory is not None and not os.path.exists(pyarchDirectory):
            os.makedirs(pyarchDirectory, 0755)

        # Determine pyarch prefix
        listPrefix = template.split("_")
        strPyarchPrefix = "di_{0}_run{1}".format(listPrefix[-3], listPrefix[-2])

        isH5 = False
        if any(beamline in pathToStartImage for beamline in ["id23eh1", "id29"]):
            minSizeFirst = 6000000
            minSizeLast = 6000000
        elif any(beamline in pathToStartImage for beamline in ["id23eh2", "id30a1"]):
            minSizeFirst = 2000000
            minSizeLast = 2000000
        elif any(beamline in pathToStartImage for beamline in ["id30a3"]):
            minSizeFirst = 100000
            minSizeLast = 100000
            pathToStartImage = os.path.join(directory,
                                            self.eiger_template_to_image(template, imageNoStart))
            pathToEndImage = os.path.join(directory,
                                          self.eiger_template_to_image(template, imageNoEnd))
            isH5 = True
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



        # Prepare input to execution plugin
        xsDataInputXia2DIALS = XSDataInputXia2DIALS()
        if isH5:
            masterFilePath = os.path.join(directory,
                                          self.eiger_template_to_master(template))
            xsDataInputXia2DIALS.addImage(XSDataFile(XSDataString(masterFilePath)))
        else:
            xsDataInputXia2DIALS.addImage(XSDataFile(XSDataString(pathToStartImage)))
        # Force anomalous
        xsDataInputXia2DIALS.anomalous = XSDataBoolean(True)
        self.edPluginExecXia2DIALS.dataInput = xsDataInputXia2DIALS
        timeStart = time.localtime()
        self.edPluginExecXia2DIALS.executeSynchronous()
        timeEnd = time.localtime()

        # Copy dataFiles to results directory
        for dataFile in self.edPluginExecXia2DIALS.dataOutput.dataFiles:
            shutil.copy(dataFile.path.value, strResultsDirectory)

        # Read the generated ISPyB xml file - if any
        if self.edPluginExecXia2DIALS.dataOutput.ispybXML is not None:
            autoProcContainer = AutoProcContainer.parseFile(self.edPluginExecXia2DIALS.dataOutput.ispybXML.path.value)

            # "Fix" certain entries in the ISPyB xml file
            autoProcScalingContainer = autoProcContainer.AutoProcScalingContainer
            for autoProcScalingStatistics in autoProcScalingContainer.AutoProcScalingStatistics:
                autoProcScalingStatistics.anomalous = True
            autoProcIntegrationContainer = autoProcScalingContainer.AutoProcIntegrationContainer
            autoProcIntegration = autoProcIntegrationContainer.AutoProcIntegration
            autoProcIntegration.anomalous = True
            image = autoProcIntegrationContainer.Image
            image.dataCollectionId = self.dataInput.dataCollectionId.value
            autoProcProgramContainer = autoProcContainer.AutoProcProgramContainer
            autoProcProgram = autoProcProgramContainer.AutoProcProgram
            autoProcProgram.processingPrograms = "XIA2_DIALS"
            autoProcProgram.processingStatus = True
            autoProcProgram.processingStartTime = time.strftime("%a %b %d %H:%M:%S %Y", timeStart)
            autoProcProgram.processingEndTime = time.strftime("%a %b %d %H:%M:%S %Y", timeEnd)
            autoProcProgramContainer.AutoProcProgramAttachment = []
            # Upload the log file to ISPyB
            if self.edPluginExecXia2DIALS.dataOutput.logFile is not None:
                pathToLogFile = self.edPluginExecXia2DIALS.dataOutput.logFile.path.value
                pyarchFileName = strPyarchPrefix + "_xia2.log"
                shutil.copy(pathToLogFile, os.path.join(pyarchDirectory, pyarchFileName))
                autoProcProgramAttachment = AutoProcProgramAttachment()
                autoProcProgramAttachment.fileName = pyarchFileName
                autoProcProgramAttachment.filePath = pyarchDirectory
                autoProcProgramAttachment.fileType = "Log"
                autoProcProgramContainer.addAutoProcProgramAttachment(autoProcProgramAttachment)
            # Upload the summary file to ISPyB
            if self.edPluginExecXia2DIALS.dataOutput.summary is not None:
                pathToSummaryFile = self.edPluginExecXia2DIALS.dataOutput.summary.path.value
                pyarchFileName = strPyarchPrefix + "_xia2-summary.log"
                shutil.copy(pathToSummaryFile, os.path.join(pyarchDirectory, pyarchFileName))
                autoProcProgramAttachment = AutoProcProgramAttachment()
                autoProcProgramAttachment.fileName = pyarchFileName
                autoProcProgramAttachment.filePath = pyarchDirectory
                autoProcProgramAttachment.fileType = "Log"
                autoProcProgramContainer.addAutoProcProgramAttachment(autoProcProgramAttachment)
            # Create a pdf file of the html page
            if self.edPluginExecXia2DIALS.dataOutput.htmlFile is not None:
                pathToHtmlFile = self.edPluginExecXia2DIALS.dataOutput.htmlFile.path.value
                pyarchFileName = strPyarchPrefix + "_xia2.pdf"
                # Convert the xia2.html to xia2.pdf
                xsDataInputHTML2PDF = XSDataInputHTML2PDF()
                xsDataInputHTML2PDF.addHtmlFile(XSDataFile(XSDataString(pathToHtmlFile)))
                xsDataInputHTML2PDF.paperSize = XSDataString("A4")
                xsDataInputHTML2PDF.lowQuality = XSDataBoolean(True)
                self.edPluginHTML2Pdf.dataInput = xsDataInputHTML2PDF
                self.edPluginHTML2Pdf.executeSynchronous()
                pdfFile = self.edPluginHTML2Pdf.dataOutput.pdfFile.path.value
                shutil.copy(pdfFile, os.path.join(pyarchDirectory, pyarchFileName))
                autoProcProgramAttachment = AutoProcProgramAttachment()
                autoProcProgramAttachment.fileName = pyarchFileName
                autoProcProgramAttachment.filePath = pyarchDirectory
                autoProcProgramAttachment.fileType = "Log"
                autoProcProgramContainer.addAutoProcProgramAttachment(autoProcProgramAttachment)
            # Copy all log files
            for logFile in self.edPluginExecXia2DIALS.dataOutput.logFiles:
                pathToLogFile = logFile.path.value
                if pathToLogFile.endswith(".log"):
                    pyarchFileName = strPyarchPrefix + "_" + os.path.basename(pathToLogFile)
                    shutil.copy(pathToLogFile, os.path.join(pyarchDirectory, pyarchFileName))
                    autoProcProgramAttachment = AutoProcProgramAttachment()
                    autoProcProgramAttachment.fileName = pyarchFileName
                    autoProcProgramAttachment.filePath = pyarchDirectory
                    autoProcProgramAttachment.fileType = "Log"
                    autoProcProgramContainer.addAutoProcProgramAttachment(autoProcProgramAttachment)
            # Copy data files
            for dataFile in self.edPluginExecXia2DIALS.dataOutput.dataFiles:
                pathToDataFile = dataFile.path.value
                if pathToDataFile.endswith(".mtz"):
                    pyarchFileName = strPyarchPrefix + "_" + os.path.basename(pathToDataFile)
                    shutil.copy(pathToDataFile, os.path.join(pyarchDirectory, pyarchFileName))
                    autoProcProgramAttachment = AutoProcProgramAttachment()
                    autoProcProgramAttachment.fileName = pyarchFileName
                    autoProcProgramAttachment.filePath = pyarchDirectory
                    autoProcProgramAttachment.fileType = "Result"
                    autoProcProgramContainer.addAutoProcProgramAttachment(autoProcProgramAttachment)
            # Upload the xml to ISPyB
            xsDataInputStoreAutoProc = XSDataInputStoreAutoProc()
            xsDataInputStoreAutoProc.AutoProcContainer = autoProcContainer
            self.edPluginStoreAutoproc.dataInput = xsDataInputStoreAutoProc
            self.edPluginStoreAutoproc.executeSynchronous()

    def eiger_template_to_image(self, fmt, num):
        fileNumber = int(num / 100)
        if fileNumber == 0:
            fileNumber = 1
        fmt_string = fmt.replace("####", "1_data_%06d" % fileNumber)
        return fmt_string.format(num)

    def eiger_template_to_master(self, fmt):
        fmt_string = fmt.replace("####", "1_master")
        return fmt_string
