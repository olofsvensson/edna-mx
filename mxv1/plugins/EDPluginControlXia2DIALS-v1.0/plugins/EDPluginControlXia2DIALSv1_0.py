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
import sys
import time
import shutil
import socket

from EDPluginControl import EDPluginControl
from EDHandlerESRFPyarchv1_0 import EDHandlerESRFPyarchv1_0
from EDUtilsPath import EDUtilsPath
from EDHandlerXSDataISPyBv1_4 import EDHandlerXSDataISPyBv1_4

from EDFactoryPlugin import edFactoryPlugin

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataString
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataTime

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


edFactoryPlugin.loadModule("XSDataMXWaitFilev1_1")
from XSDataMXWaitFilev1_1 import XSDataInputMXWaitFile

class EDPluginControlXia2DIALSv1_0(EDPluginControl):
    """
    Control plugin for xia2 -dials
    """


    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputControlXia2DIALS)
        self.dataOutput = XSDataResultControlXia2DIALS()
        self.doAnom = True
        self.doNoanom = False
        self.doAnomAndNonanom = False
        self.pyarchPrefix = None
        self.resultsDirectory = None
        self.pyarchDirectory = None
        self.processingCommandLine = None
        self.processingPrograms = None
        self.hasUploadedAnomResultsToISPyB = False
        self.hasUploadedNoanomResultsToISPyB = False
        self.reprocess = False

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

        self.processingCommandLine = ' '.join(sys.argv)
        self.processingPrograms = "XIA2_DIALS"
        if self.reprocess:
            self.processingPrograms += " reprocess"

        if self.dataInput.doAnomAndNonanom is not None:
            self.doAnomAndNonanom = self.dataInput.doAnomAndNonanom.value

        if self.doAnomAndNonanom:
            self.doAnom = True
            self.doNoanom = True
        else:
            if self.dataInput.doAnom is not None:
                self.doAnom = self.dataInput.doAnom.value
            self.doNoanom = not self.doAnom

        if self.dataInput.reprocess is not None:
            self.reprocess = self.dataInput.reprocess.value

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
        if self.doAnom:
            self.edPluginExecXia2DIALSAnom = self.loadPlugin("EDPluginExecXia2DIALSv1_0", "EDPluginExecXia2DIALSv1_0_anom")
        if self.doNoanom:
            self.edPluginExecXia2DIALSNoanom = self.loadPlugin("EDPluginExecXia2DIALSv1_0", "EDPluginExecXia2DIALSv1_0_noanom")


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
            xsDataInputRetrieveDataCollection.dataCollectionId = self.dataInput.dataCollectionId
            self.edPluginRetrieveDataCollection.dataInput = xsDataInputRetrieveDataCollection
            self.edPluginRetrieveDataCollection.executeSynchronous()
            ispybDataCollection = self.edPluginRetrieveDataCollection.dataOutput.dataCollection
            directory = ispybDataCollection.imageDirectory
            if EDUtilsPath.isEMBL():
                template = ispybDataCollection.fileTemplate.replace("%05d", "####")
            else:
                template = ispybDataCollection.fileTemplate.replace("%04d", "####")
            if self.dataInput.startFrame is None:
                imageNoStart = ispybDataCollection.startImageNumber
            else:
                imageNoStart = self.dataInput.startFrame.value
            if self.dataInput.endFrame is None:
                imageNoEnd = imageNoStart + ispybDataCollection.numberOfImages - 1
            else:
                imageNoEnd = self.dataInput.endFrame.value

#            # DEBUG we set the end image to 20 in order to speed up things
#            self.warning("End image set to 20 (was {0})".format(imageNoEnd))
#            imageNoEnd = 20
            pathToStartImage = os.path.join(directory, ispybDataCollection.fileTemplate % imageNoStart)
            pathToEndImage = os.path.join(directory, ispybDataCollection.fileTemplate % imageNoEnd)
#        else:
#            directory = self.dataInput.dirN.value
#            template = self.dataInput.templateN.value
#            imageNoStart = self.dataInput.fromN.value
#            imageNoEnd = self.dataInput.toN.value
#            fileTemplate = template.replace("####", "%04d")
#            pathToStartImage = os.path.join(directory, fileTemplate % imageNoStart)
#            pathToEndImage = os.path.join(directory, fileTemplate % imageNoEnd)

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
            processDirectory = self.dataInput.processDirectory.path.value
        else:
            processDirectory = directory.replace("RAW_DATA", "PROCESSED_DATA")

        # Make results directory
        self.resultsDirectory = os.path.join(processDirectory, "results")
        if not os.path.exists(self.resultsDirectory):
            os.makedirs(self.resultsDirectory, 0o755)

        # Create path to pyarch
        if self.dataInput.reprocess is not None and self.dataInput.reprocess.value:
            self.pyarchDirectory = EDHandlerESRFPyarchv1_0.createPyarchReprocessDirectoryPath(beamline,
                "XIA2_DIALS", self.dataInput.dataCollectionId.value)
        else:
            self.pyarchDirectory = EDHandlerESRFPyarchv1_0.createPyarchFilePath(self.resultsDirectory)
        if self.pyarchDirectory is not None:
            self.pyarchDirectory = self.pyarchDirectory.replace('PROCESSED_DATA', 'RAW_DATA')
            if not os.path.exists(self.pyarchDirectory):
                try:
                    os.makedirs(self.pyarchDirectory, 0o755)
                except:
                    self.pyarchDirectory = None

        # Determine pyarch prefix
        listPrefix = template.split("_")
        self.pyarchPrefix = "di_{0}_run{1}".format(listPrefix[-3], listPrefix[-2])

        isH5 = False
        if any(beamline in pathToStartImage for beamline in ["id30a1"]):
            minSizeFirst = 2000000
            minSizeLast = 2000000
        elif any(beamline in pathToStartImage for beamline in ["id23eh1", "id23eh2", "id30a3", "id30b"]):
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

        if EDUtilsPath.isEMBL():
            fWaitFileTimeout = 60
        else:
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
        if self.doAnom:
            xsDataInputXia2DIALSAnom = XSDataInputXia2DIALS()
            xsDataInputXia2DIALSAnom.anomalous = XSDataBoolean(True)
            xsDataInputXia2DIALSAnom.spaceGroup = self.dataInput.spaceGroup
            xsDataInputXia2DIALSAnom.unitCell = self.dataInput.unitCell
            if imageNoStart is not None:
                xsDataInputXia2DIALSAnom.startFrame = XSDataInteger(imageNoStart)
            if imageNoEnd is not None:
                xsDataInputXia2DIALSAnom.endFrame = XSDataInteger(imageNoEnd)
        if self.doNoanom:
            xsDataInputXia2DIALSNoanom = XSDataInputXia2DIALS()
            xsDataInputXia2DIALSNoanom.anomalous = XSDataBoolean(False)
            xsDataInputXia2DIALSNoanom.spaceGroup = self.dataInput.spaceGroup
            xsDataInputXia2DIALSNoanom.unitCell = self.dataInput.unitCell
            if imageNoStart is not None:
                xsDataInputXia2DIALSNoanom.startFrame = XSDataInteger(imageNoStart)
            if imageNoEnd is not None:
                xsDataInputXia2DIALSNoanom.endFrame = XSDataInteger(imageNoEnd)
        if isH5:
            masterFilePath = os.path.join(directory,
                                          self.eiger_template_to_master(template))
            if self.doAnom:
                xsDataInputXia2DIALSAnom.addImage(XSDataFile(XSDataString(masterFilePath)))
            if self.doNoanom:
                xsDataInputXia2DIALSNoanom.addImage(XSDataFile(XSDataString(masterFilePath)))
        else:
            if self.doAnom:
                xsDataInputXia2DIALSAnom.addImage(XSDataFile(XSDataString(pathToStartImage)))
            if self.doNoanom:
                xsDataInputXia2DIALSNoanom.addImage(XSDataFile(XSDataString(pathToStartImage)))
        self.timeStart = time.localtime()

        if self.dataInput.dataCollectionId is not None:
            # Set ISPyB to running
            if self.doAnom:
                self.autoProcIntegrationIdAnom, self.autoProcProgramIdAnom = \
                  EDHandlerXSDataISPyBv1_4.setIspybToRunning(self, dataCollectionId=self.dataInput.dataCollectionId.value,
                                                             processingCommandLine=self.processingCommandLine,
                                                             processingPrograms=self.processingPrograms,
                                                             isAnom=True,
                                                             timeStart=self.timeStart)
            if self.doNoanom:
                self.autoProcIntegrationIdNoanom, self.autoProcProgramIdNoanom = \
                  EDHandlerXSDataISPyBv1_4.setIspybToRunning(self, dataCollectionId=self.dataInput.dataCollectionId.value,
                                                             processingCommandLine=self.processingCommandLine,
                                                             processingPrograms=self.processingPrograms,
                                                             isAnom=False,
                                                             timeStart=self.timeStart)

        if self.doAnom:
            self.edPluginExecXia2DIALSAnom.dataInput = xsDataInputXia2DIALSAnom
            self.edPluginExecXia2DIALSAnom.execute()
        if self.doNoanom:
            self.edPluginExecXia2DIALSNoanom.dataInput = xsDataInputXia2DIALSNoanom
            self.edPluginExecXia2DIALSNoanom.execute()
        if self.doAnom:
            self.edPluginExecXia2DIALSAnom.synchronize()
        if self.doNoanom:
            self.edPluginExecXia2DIALSNoanom.synchronize()
        self.timeEnd = time.localtime()

        # Upload to ISPyB
        if self.doAnom:
            self.hasUploadedAnomResultsToISPyB = self.uploadToISPyB(self.edPluginExecXia2DIALSAnom, True, proposal,
                               self.autoProcProgramIdAnom, self.autoProcIntegrationIdAnom)
            if self.hasUploadedAnomResultsToISPyB:
                self.screen("Anom results uploaded to ISPyB")
            else:
                self.ERROR("Could not upload anom results to ISPyB!")
        if self.doNoanom:
            self.hasUploadedNoanomResultsToISPyB = self.uploadToISPyB(self.edPluginExecXia2DIALSNoanom, False, proposal,
                               self.autoProcProgramIdNoanom, self.autoProcIntegrationIdNoanom)
            if self.hasUploadedNoanomResultsToISPyB:
                self.screen("Noanom results uploaded to ISPyB")
            else:
                self.ERROR("Could not upload noanom results to ISPyB!")

    def finallyProcess(self, _edObject=None):
        EDPluginControl.finallyProcess(self)
        if self.doAnom:
            self.edPluginExecXia2DIALSAnom.synchronize()
        if self.doNoanom:
            self.edPluginExecXia2DIALSNoanom.synchronize()
        strMessage = ""
        if self.getListOfWarningMessages() != []:
            strMessage += "Warning messages: \n\n"
            for strWarningMessage in self.getListOfWarningMessages():
                strMessage += strWarningMessage + "\n\n"
        if self.getListOfErrorMessages() != []:
            strMessage += "Error messages: \n\n"
            for strErrorMessage in self.getListOfErrorMessages():
                strMessage += strErrorMessage + "\n\n"
        if self.isFailure():
            self.screen("XIA2_DIALS processing ended with errors!")
            if strMessage != "":
                self.screen("Warning and/or error messages: \n{0}.".format(strMessage))
            self.timeEnd = time.localtime()
            if self.dataInput.dataCollectionId is not None:
                # Upload program failure status to ISPyB
                # anom
                self.screen("Setting anom program status to failed in ISPyB.")
                if self.doAnom and not self.hasUploadedAnomResultsToISPyB:
                    self.screen("Setting anom program status to failed in ISPyB.")
                    EDHandlerXSDataISPyBv1_4.setIspybToFailed(self, dataCollectionId=self.dataInput.dataCollectionId.value,
                         autoProcIntegrationId=self.autoProcIntegrationIdAnom,
                         autoProcProgramId=self.autoProcProgramIdAnom,
                         processingCommandLine=self.processingCommandLine,
                         processingPrograms=self.processingPrograms,
                         isAnom=True,
                         timeStart=self.timeStart,
                         timeEnd=self.timeEnd)

                if self.doNoanom and not self.hasUploadedNoanomResultsToISPyB:
                    self.screen("Setting noanom program status to failed in ISPyB.")
                    EDHandlerXSDataISPyBv1_4.setIspybToFailed(self, dataCollectionId=self.dataInput.dataCollectionId.value,
                         autoProcIntegrationId=self.autoProcIntegrationIdNoanom,
                         autoProcProgramId=self.autoProcProgramIdNoanom,
                         processingCommandLine=self.processingCommandLine,
                         processingPrograms=self.processingPrograms,
                         isAnom=False,
                         timeStart=self.timeStart,
                         timeEnd=self.timeEnd)

    def uploadToISPyB(self, edPluginExecXia2DIALS, isAnom, proposal, programId, integrationId):
        successUpload = False

        if isAnom:
            anomString = "anom"
        else:
            anomString = "noanom"

        # Read the generated ISPyB xml file - if any
        if self.pyarchDirectory is not None and edPluginExecXia2DIALS.dataOutput.ispybXML is not None:
            autoProcContainer = AutoProcContainer.parseFile(edPluginExecXia2DIALS.dataOutput.ispybXML.path.value)

            # "Fix" certain entries in the ISPyB xml file
            autoProcScalingContainer = autoProcContainer.AutoProcScalingContainer
            for autoProcScalingStatistics in autoProcScalingContainer.AutoProcScalingStatistics:
                if isAnom:
                    autoProcScalingStatistics.anomalous = True
                else:
                    autoProcScalingStatistics.anomalous = False
                # Convert from fraction to %
                autoProcScalingStatistics.rMerge *= 100.0
                autoProcScalingStatistics.rMeasWithinIPlusIMinus *= 100
                autoProcScalingStatistics.rMeasAllIPlusIMinus *= 100
                autoProcScalingStatistics.rPimWithinIPlusIMinus *= 100
                autoProcScalingStatistics.rPimAllIPlusIMinus *= 100
            autoProcIntegrationContainer = autoProcScalingContainer.AutoProcIntegrationContainer
            autoProcIntegration = autoProcIntegrationContainer.AutoProcIntegration
            autoProcIntegration.autoProcIntegrationId = integrationId
            if isAnom:
                autoProcIntegration.anomalous = True
            else:
                autoProcIntegration.anomalous = False
            image = autoProcIntegrationContainer.Image
            image.dataCollectionId = self.dataInput.dataCollectionId.value
            autoProcProgramContainer = autoProcContainer.AutoProcProgramContainer
            autoProcProgram = EDHandlerXSDataISPyBv1_4.createAutoProcProgram(
                    programId=programId, status="SUCCESS", timeStart=self.timeStart, timeEnd=self.timeEnd,
                    processingCommandLine=self.processingCommandLine, processingPrograms=self.processingPrograms)
            autoProcProgramContainer.AutoProcProgram = autoProcProgram
            autoProcProgramContainer.AutoProcProgramAttachment = []
            # Upload the log file to ISPyB
            if edPluginExecXia2DIALS.dataOutput.logFile is not None:
                pathToLogFile = edPluginExecXia2DIALS.dataOutput.logFile.path.value
                pyarchFileName = self.pyarchPrefix + "_" + anomString + "_xia2.log"
                shutil.copy(pathToLogFile, os.path.join(self.pyarchDirectory, pyarchFileName))
                shutil.copy(pathToLogFile, os.path.join(self.resultsDirectory, pyarchFileName))
                autoProcProgramAttachment = AutoProcProgramAttachment()
                autoProcProgramAttachment.fileName = pyarchFileName
                autoProcProgramAttachment.filePath = self.pyarchDirectory
                autoProcProgramAttachment.fileType = "Log"
                autoProcProgramContainer.addAutoProcProgramAttachment(autoProcProgramAttachment)
            # Upload the summary file to ISPyB
            if edPluginExecXia2DIALS.dataOutput.summary is not None:
                pathToSummaryFile = edPluginExecXia2DIALS.dataOutput.summary.path.value
                pyarchFileName = self.pyarchPrefix + "_" + anomString + "_xia2-summary.log"
                shutil.copy(pathToSummaryFile, os.path.join(self.pyarchDirectory, pyarchFileName))
                shutil.copy(pathToSummaryFile, os.path.join(self.resultsDirectory, pyarchFileName))
                autoProcProgramAttachment = AutoProcProgramAttachment()
                autoProcProgramAttachment.fileName = pyarchFileName
                autoProcProgramAttachment.filePath = self.pyarchDirectory
                autoProcProgramAttachment.fileType = "Log"
                autoProcProgramContainer.addAutoProcProgramAttachment(autoProcProgramAttachment)
            # Create a pdf file of the html page
            if edPluginExecXia2DIALS.dataOutput.htmlFile is not None:
                pathToHtmlFile = edPluginExecXia2DIALS.dataOutput.htmlFile.path.value
                pyarchFileName = self.pyarchPrefix + "_" + anomString + "_xia2.html"
                shutil.copy(pathToHtmlFile, os.path.join(self.pyarchDirectory, pyarchFileName))
                shutil.copy(pathToHtmlFile, os.path.join(self.resultsDirectory, pyarchFileName))
                autoProcProgramAttachment = AutoProcProgramAttachment()
                autoProcProgramAttachment.fileName = pyarchFileName
                autoProcProgramAttachment.filePath = self.pyarchDirectory
                autoProcProgramAttachment.fileType = "Log"
                autoProcProgramContainer.addAutoProcProgramAttachment(autoProcProgramAttachment)
            # Copy all log files
            for logFile in edPluginExecXia2DIALS.dataOutput.logFiles:
                pathToLogFile = logFile.path.value
                pyarchFileName = self.pyarchPrefix + "_" + anomString + "_" + os.path.basename(pathToLogFile)
                # Copy all log files to results:
                shutil.copy(pathToLogFile, os.path.join(self.resultsDirectory, pyarchFileName))
                # Only copy .log files to pyarch
                if pathToLogFile.endswith(".log"):
                    shutil.copy(pathToLogFile, os.path.join(self.pyarchDirectory, pyarchFileName))
                    autoProcProgramAttachment = AutoProcProgramAttachment()
                    autoProcProgramAttachment.fileName = pyarchFileName
                    autoProcProgramAttachment.filePath = self.pyarchDirectory
                    autoProcProgramAttachment.fileType = "Log"
                    autoProcProgramContainer.addAutoProcProgramAttachment(autoProcProgramAttachment)
            # Copy data files
            for dataFile in edPluginExecXia2DIALS.dataOutput.dataFiles:
                pathToDataFile = dataFile.path.value
                if pathToDataFile.endswith(".mtz"):
                    pyarchFileName = self.pyarchPrefix + "_" + anomString + "_" + os.path.basename(pathToDataFile)
                    shutil.copy(pathToDataFile, os.path.join(self.pyarchDirectory, pyarchFileName))
                    shutil.copy(pathToDataFile, os.path.join(self.resultsDirectory, pyarchFileName))
                    autoProcProgramAttachment = AutoProcProgramAttachment()
                    autoProcProgramAttachment.fileName = pyarchFileName
                    autoProcProgramAttachment.filePath = self.pyarchDirectory
                    autoProcProgramAttachment.fileType = "Result"
                    autoProcProgramContainer.addAutoProcProgramAttachment(autoProcProgramAttachment)
            # Upload the xml to ISPyB
            xsDataInputStoreAutoProc = XSDataInputStoreAutoProc()
            xsDataInputStoreAutoProc.AutoProcContainer = autoProcContainer
            edPluginStoreAutoproc = self.loadPlugin("EDPluginISPyBStoreAutoProcv1_4", "EDPluginISPyBStoreAutoProcv1_4_{0}".format(anomString))
            edPluginStoreAutoproc.dataInput = xsDataInputStoreAutoProc
            edPluginStoreAutoproc.executeSynchronous()
            successUpload = not edPluginStoreAutoproc.isFailure()
        else:
            # Copy dataFiles to results directory
            for dataFile in edPluginExecXia2DIALS.dataOutput.dataFiles:
                trunc, suffix = os.path.splitext(dataFile.path.value)
                newFileName = os.path.basename(trunc) + "_" + anomString + suffix
                shutil.copy(dataFile.path.value, os.path.join(self.resultsDirectory, newFileName))
        return successUpload

    def eiger_template_to_image(self, fmt, num):
        fileNumber = int(num / 100)
        if fileNumber == 0:
            fileNumber = 1
        fmt_string = fmt.replace("####", "1_data_%06d" % fileNumber)
        return fmt_string.format(num)

    def eiger_template_to_master(self, fmt):
        fmt_string = fmt.replace("####", "1_master")
        return fmt_string
