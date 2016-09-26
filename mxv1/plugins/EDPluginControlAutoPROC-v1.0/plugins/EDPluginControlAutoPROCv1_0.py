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
import gzip
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
        self.doAnomAndNonanom = True
        self.pyarchPrefix = None
        self.resultsDirectory = None
        self.pyarchDirectory = None

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

        if self.dataInput.doAnomAndNonanom is not None:
            if self.dataInput.doAnomAndNonanom.value:
                self.doAnomAndNonanom = True
            else:
                self.doAnomAndNonanom = False

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
        self.edPluginExecAutoPROCAnom = self.loadPlugin("EDPluginExecAutoPROCv1_0", "EDPluginExecAutoPROCv1_0_anom")
        if self.doAnomAndNonanom:
            self.edPluginExecAutoPROCNoanom = self.loadPlugin("EDPluginExecAutoPROCv1_0", "EDPluginExecAutoPROCv1_0_noanom")
        self.edPluginStoreAutoprocAnom = self.loadPlugin("EDPluginISPyBStoreAutoProcv1_4", "EDPluginISPyBStoreAutoProcv1_4_anom")
        self.edPluginStoreAutoprocNoanom = self.loadPlugin("EDPluginISPyBStoreAutoProcv1_4", "EDPluginISPyBStoreAutoProcv1_4_noanom")



    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG('EDPluginControlAutoPROCv1_0.process starting')

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
            processDirectory = self.dataInput.processDirectory.path.value
        else:
            processDirectory = directory.replace("RAW_DATA", "PROCESSED_DATA")

        # Make results directory
        self.resultsDirectory = os.path.join(processDirectory, "results")
        if not os.path.exists(self.resultsDirectory):
            os.makedirs(self.resultsDirectory, 0755)

        # Create path to pyarch
        self.pyarchDirectory = EDHandlerESRFPyarchv1_0.createPyarchFilePath(self.resultsDirectory)
        self.pyarchDirectory = self.pyarchDirectory.replace('PROCESSED_DATA', 'RAW_DATA')
        if self.pyarchDirectory is not None and not os.path.exists(self.pyarchDirectory):
            os.makedirs(self.pyarchDirectory, 0755)

        # Determine pyarch prefix
        listPrefix = template.split("_")
        self.pyarchPrefix = "ap_{0}_run{1}".format(listPrefix[-3], listPrefix[-2])

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
        xsDataInputAutoPROCAnom = XSDataInputAutoPROC()
        xsDataInputAutoPROCAnom.anomalous = XSDataBoolean(True)
        if self.doAnomAndNonanom:
            xsDataInputAutoPROCNoanom = XSDataInputAutoPROC()
            xsDataInputAutoPROCNoanom.anomalous = XSDataBoolean(False)
        xsDataAutoPROCIdentifier = XSDataAutoPROCIdentifier()
        xsDataAutoPROCIdentifier.idN = XSDataString(identifier)
        xsDataAutoPROCIdentifier.dirN = XSDataFile(XSDataString(directory))
        xsDataAutoPROCIdentifier.templateN = XSDataString(template)
        xsDataAutoPROCIdentifier.fromN = XSDataInteger(imageNoStart)
        xsDataAutoPROCIdentifier.toN = XSDataInteger(imageNoEnd)
        xsDataInputAutoPROCAnom.addIdentifier(xsDataAutoPROCIdentifier)
        if self.doAnomAndNonanom:
            xsDataInputAutoPROCNoanom.addIdentifier(xsDataAutoPROCIdentifier.copy())
        if isH5:
            masterFilePath = os.path.join(directory,
                                          self.eiger_template_to_master(template))
            xsDataInputAutoPROCAnom.masterH5 = XSDataFile(XSDataString(masterFilePath))
            if self.doAnomAndNonanom:
                xsDataInputAutoPROCNoanom.masterH5 = XSDataFile(XSDataString(masterFilePath))
        timeStart = time.localtime()
        self.edPluginExecAutoPROCAnom.dataInput = xsDataInputAutoPROCAnom
        self.edPluginExecAutoPROCAnom.execute()
        if self.doAnomAndNonanom:
            self.edPluginExecAutoPROCNoanom.dataInput = xsDataInputAutoPROCNoanom
            self.edPluginExecAutoPROCNoanom.execute()
        self.edPluginExecAutoPROCAnom.synchronize()
        if self.doAnomAndNonanom:
            self.edPluginExecAutoPROCNoanom.synchronize()
        timeEnd = time.localtime()

        # Upload to ISPyB
        self.uploadToISPyB(self.edPluginExecAutoPROCAnom, True, proposal, timeStart, timeEnd)
        if self.doAnomAndNonanom:
            self.uploadToISPyB(self.edPluginExecAutoPROCNoanom, False, proposal, timeStart, timeEnd)


    def uploadToISPyB(self, edPluginExecAutoPROC, isAnom, proposal, timeStart, timeEnd):
        if isAnom:
            anomString = "anom"
        else:
            anomString = "noanom"
        # Read the generated ISPyB xml file - if any
        if edPluginExecAutoPROC.dataOutput.ispybXML is not None:
            autoProcContainer = AutoProcContainer.parseFile(edPluginExecAutoPROC.dataOutput.ispybXML.path.value)

            # "Fix" certain entries in the ISPyB xml file
            autoProcScalingContainer = autoProcContainer.AutoProcScalingContainer
            for autoProcScalingStatistics in autoProcScalingContainer.AutoProcScalingStatistics:
                if isAnom:
                    autoProcScalingStatistics.anomalous = True
                else:
                    autoProcScalingStatistics.anomalous = False
                # Convert from fraction to %
                autoProcScalingStatistics.rMerge *= 100.0
            autoProcIntegrationContainer = autoProcScalingContainer.AutoProcIntegrationContainer
            image = autoProcIntegrationContainer.Image
            image.dataCollectionId = self.dataInput.dataCollectionId.value
            autoProcIntegration = autoProcIntegrationContainer.AutoProcIntegration
            if isAnom:
                autoProcIntegration.anomalous = True
            else:
                autoProcIntegration.anomalous = False
            autoProcProgramContainer = autoProcContainer.AutoProcProgramContainer
            autoProcProgram = autoProcProgramContainer.AutoProcProgram
            autoProcProgram.processingPrograms = "autoPROC"
            autoProcProgram.processingStartTime = time.strftime("%a %b %d %H:%M:%S %Y", timeStart)
            autoProcProgram.processingEndTime = time.strftime("%a %b %d %H:%M:%S %Y", timeEnd)
            for autoProcProgramAttachment in autoProcProgramContainer.AutoProcProgramAttachment:
                if autoProcProgramAttachment.fileName == "summary.html":
                    summaryHtmlPath = os.path.join(autoProcProgramAttachment.filePath, autoProcProgramAttachment.fileName)
                    # Replace opidXX with user name
                    htmlSummary = open(summaryHtmlPath).read()
                    userString1 = "User      : {0} (".format(os.environ["USER"])
                    userString2 = "User      : {0} (".format(proposal)
                    htmlSummary = htmlSummary.replace(userString1, userString2)
                    open(summaryHtmlPath, "w").write(htmlSummary)
                    # Convert the summary.html to summary.pdf
                    xsDataInputHTML2PDF = XSDataInputHTML2PDF()
                    xsDataInputHTML2PDF.addHtmlFile(XSDataFile(XSDataString(summaryHtmlPath)))
                    xsDataInputHTML2PDF.paperSize = XSDataString("A3")
                    xsDataInputHTML2PDF.lowQuality = XSDataBoolean(True)
                    edPluginHTML2Pdf = self.loadPlugin("EDPluginHTML2PDFv1_0", "EDPluginHTML2PDFv1_0_{0}".format(anomString))
                    edPluginHTML2Pdf.dataInput = xsDataInputHTML2PDF
                    edPluginHTML2Pdf.executeSynchronous()
                    pdfFile = edPluginHTML2Pdf.dataOutput.pdfFile.path.value
                    pyarchPdfFile = self.pyarchPrefix + "_" + anomString + "_" + os.path.basename(pdfFile)
                    # Copy file to results directory and pyarch
                    shutil.copy(pdfFile, os.path.join(self.resultsDirectory, pyarchPdfFile))
                    shutil.copy(pdfFile, os.path.join(self.pyarchDirectory, pyarchPdfFile))
                    autoProcProgramAttachment.fileName = pyarchPdfFile
                    autoProcProgramAttachment.filePath = self.pyarchDirectory
                elif autoProcProgramAttachment.fileName == "truncate-unique.mtz":
                    pathtoFile = os.path.join(autoProcProgramAttachment.filePath, autoProcProgramAttachment.fileName)
                    pyarchFile = self.pyarchPrefix + "_{0}_truncate.mtz".format(anomString)
                    shutil.copy(pathtoFile, os.path.join(self.resultsDirectory, pyarchFile))
                    shutil.copy(pathtoFile, os.path.join(self.pyarchDirectory, pyarchFile))
                    autoProcProgramAttachment.fileName = pyarchFile
                    autoProcProgramAttachment.filePath = self.pyarchDirectory
                else:
                    pathtoFile = os.path.join(autoProcProgramAttachment.filePath, autoProcProgramAttachment.fileName)
                    pyarchFile = self.pyarchPrefix + "_" + anomString + "_" + autoProcProgramAttachment.fileName
                    shutil.copy(pathtoFile, os.path.join(self.resultsDirectory, pyarchFile))
                    shutil.copy(pathtoFile, os.path.join(self.pyarchDirectory, pyarchFile))
                    autoProcProgramAttachment.fileName = pyarchFile
                    autoProcProgramAttachment.filePath = self.pyarchDirectory
            # Add XSCALE.LP file if present
            processDirectory = edPluginExecAutoPROC.dataOutput.processDirectory[0].path.value
            pathToXSCALELog = os.path.join(processDirectory, "xscale_XSCALE.LP")
            if os.path.exists(pathToXSCALELog):
                pyarchXSCALELog = self.pyarchPrefix + "_merged_{0}_XSCALE.LP".format(anomString)
                shutil.copy(pathToXSCALELog, os.path.join(self.resultsDirectory, pyarchXSCALELog))
                shutil.copy(pathToXSCALELog, os.path.join(self.pyarchDirectory, pyarchXSCALELog))
                autoProcProgramAttachment = AutoProcProgramAttachment()
                autoProcProgramAttachment.fileName = pyarchXSCALELog
                autoProcProgramAttachment.filePath = self.pyarchDirectory
                autoProcProgramAttachment.fileType = "Result"
                autoProcProgramContainer.addAutoProcProgramAttachment(autoProcProgramAttachment)
            # Add XDS_ASCII.HKL if present and gzip it
            pathToXdsAsciiHkl = os.path.join(processDirectory, "XDS_ASCII.HKL")
            if os.path.exists(pathToXdsAsciiHkl):
                pyarchXdsAsciiHkl = self.pyarchPrefix + "_merged_{0}_XDS_ASCII.HKL.gz".format(anonString)
                f_in = open(pathToXdsAsciiHkl)
                f_out = gzip.open(os.path.join(self.pyarchDirectory, pyarchXdsAsciiHkl), "wb")
                f_out.writelines(f_in)
                f_out.close()
                f_in.close()
                shutil.copy(os.path.join(self.pyarchDirectory, pyarchXdsAsciiHkl), os.path.join(self.resultsDirectory, pyarchXdsAsciiHkl))
                autoProcProgramAttachment = AutoProcProgramAttachment()
                autoProcProgramAttachment.fileName = pyarchXdsAsciiHkl
                autoProcProgramAttachment.filePath = self.pyarchDirectory
                autoProcProgramAttachment.fileType = "Result"
                autoProcProgramContainer.addAutoProcProgramAttachment(autoProcProgramAttachment)
            # Add log file
            pathToLogFile = edPluginExecAutoPROC.dataOutput.logFile.path.value
            autoPROClog = open(pathToLogFile).read()
            userString1 = "User      : {0} (".format(os.environ["USER"])
            userString2 = "User      : {0} (".format(proposal)
            autoPROClog = autoPROClog.replace(userString1, userString2)
            open(pathToLogFile, "w").write(autoPROClog)
            pyarchLogFile = self.pyarchPrefix + "_{0}_autoPROC.log".format(anomString)
            shutil.copy(pathToLogFile, os.path.join(self.resultsDirectory, pyarchLogFile))
            shutil.copy(pathToLogFile, os.path.join(self.pyarchDirectory, pyarchLogFile))
            autoProcProgramAttachment = AutoProcProgramAttachment()
            autoProcProgramAttachment.fileName = pyarchLogFile
            autoProcProgramAttachment.filePath = self.pyarchDirectory
            autoProcProgramAttachment.fileType = "Log"
            autoProcProgramContainer.addAutoProcProgramAttachment(autoProcProgramAttachment)

            # Upload the xml to ISPyB
            xsDataInputStoreAutoProc = XSDataInputStoreAutoProc()
            xsDataInputStoreAutoProc.AutoProcContainer = autoProcContainer
            if isAnom:
                self.edPluginStoreAutoprocAnom.dataInput = xsDataInputStoreAutoProc
                self.edPluginStoreAutoprocAnom.executeSynchronous()
            else:
                self.edPluginStoreAutoprocNoanom.dataInput = xsDataInputStoreAutoProc
                self.edPluginStoreAutoprocNoanom.executeSynchronous()


    def eiger_template_to_image(self, fmt, num):
        fileNumber = int(num / 100)
        if fileNumber == 0:
            fileNumber = 1
        fmt_string = fmt.replace("####", "1_data_%06d" % fileNumber)
        return fmt_string.format(num)

    def eiger_template_to_master(self, fmt):
        fmt_string = fmt.replace("####", "1_master")
        return fmt_string
