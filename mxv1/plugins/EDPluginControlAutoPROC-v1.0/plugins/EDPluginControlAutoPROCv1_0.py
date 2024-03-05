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
import pathlib
import sys
import gzip
import time
import shutil
import socket

from EDPluginControl import EDPluginControl
from EDHandlerESRFPyarchv1_0 import EDHandlerESRFPyarchv1_0
from EDUtilsPath import EDUtilsPath
from EDUtilsICAT import EDUtilsICAT
from EDHandlerXSDataISPyBv1_4 import EDHandlerXSDataISPyBv1_4

from EDFactoryPlugin import edFactoryPlugin

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataString
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataTime

from XSDataControlAutoPROCv1_0 import XSDataInputControlAutoPROC

edFactoryPlugin.loadModule("XSDataAutoPROCv1_0")

from XSDataAutoPROCv1_0 import XSDataAutoPROCIdentifier
from XSDataAutoPROCv1_0 import XSDataInputAutoPROC

edFactoryPlugin.loadModule("XSDataISPyBv1_4")
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
        self.doAnom = True
        self.doNoanom = False
        self.doAnomAndNonanom = False
        self.pyarchPrefix = None
        self.resultsDirectory = None
        self.pyarchDirectory = None
        self.hasUploadedAnomResultsToISPyB = False
        self.hasUploadedNoanomResultsToISPyB = False
        self.hasUploadedAnomStaranisoResultsToISPyB = False
        self.hasUploadedNoanomStaranisoResultsToISPyB = False
        self.listPyarchFile = []
        self.reprocess = False
        self.exclude_range = None

    def configure(self):
        EDPluginControl.configure(self)

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlAutoPROCv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")

    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlAutoPROCv1_0.preProcess")
        self.screen("autoPROC processing started")

        self.processingCommandLine = " ".join(sys.argv)
        self.processingProgram = "autoPROC"
        self.processingProgramStaraniso = "autoPROC_staraniso"

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

        self.edPluginWaitFileFirst = self.loadPlugin(
            "EDPluginMXWaitFilev1_1", "MXWaitFileFirst"
        )
        self.edPluginWaitFileLast = self.loadPlugin(
            "EDPluginMXWaitFilev1_1", "MXWaitFileLast"
        )

        self.edPluginRetrieveDataCollection = self.loadPlugin(
            "EDPluginISPyBRetrieveDataCollectionv1_4"
        )
        if self.doAnom:
            self.edPluginExecAutoPROCAnom = self.loadPlugin(
                "EDPluginExecAutoPROCv1_0", "EDPluginExecAutoPROCv1_0_anom"
            )
        if self.doNoanom:
            self.edPluginExecAutoPROCNoanom = self.loadPlugin(
                "EDPluginExecAutoPROCv1_0", "EDPluginExecAutoPROCv1_0_noanom"
            )

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlAutoPROCv1_0.process starting")

        directory = None
        template = None
        imageNoStart = None
        imageNoEnd = None
        pathToStartImage = None
        pathToEndImage = None
        beamline = "unknown"
        proposal = "unknown"

        # If we have a data collection id, use it
        if self.dataInput.dataCollectionId is not None:
            # Recover the data collection from ISPyB
            xsDataInputRetrieveDataCollection = XSDataInputRetrieveDataCollection()
            identifier = str(self.dataInput.dataCollectionId.value)
            xsDataInputRetrieveDataCollection.dataCollectionId = (
                self.dataInput.dataCollectionId
            )
            self.edPluginRetrieveDataCollection.dataInput = (
                xsDataInputRetrieveDataCollection
            )
            self.edPluginRetrieveDataCollection.executeSynchronous()
            ispybDataCollection = (
                self.edPluginRetrieveDataCollection.dataOutput.dataCollection
            )
            directory = ispybDataCollection.imageDirectory
            if EDUtilsPath.isEMBL():
                template = ispybDataCollection.fileTemplate.replace("%05d", "#" * 5)
            elif EDUtilsPath.isMAXIV():
                template = ispybDataCollection.fileTemplate
            else:
                template = ispybDataCollection.fileTemplate.replace("%04d", "####")
            if self.dataInput.fromN is None:
                imageNoStart = ispybDataCollection.startImageNumber
            else:
                imageNoStart = self.dataInput.fromN.value
            if self.dataInput.toN is None:
                imageNoEnd = imageNoStart + ispybDataCollection.numberOfImages - 1
            else:
                imageNoEnd = self.dataInput.toN.value
            pathToStartImage = os.path.join(
                directory, ispybDataCollection.fileTemplate % imageNoStart
            )
            pathToEndImage = os.path.join(
                directory, ispybDataCollection.fileTemplate % imageNoEnd
            )
        else:
            identifier = str(int(time.time()))
            directory = self.dataInput.dirN.path.value
            template = self.dataInput.templateN.value
            imageNoStart = self.dataInput.fromN.value
            imageNoEnd = self.dataInput.toN.value
            if EDUtilsPath.isEMBL():
                fileTemplate = template.replace("#####", "%05d")
            else:
                fileTemplate = template.replace("####", "%04d")
            pathToStartImage = os.path.join(directory, fileTemplate % imageNoStart)
            pathToEndImage = os.path.join(directory, fileTemplate % imageNoEnd)

        if self.dataInput.exclude_range is not None:
            self.exclude_range = []
            for xsdata_range in self.dataInput.exclude_range:
                self.exclude_range.append([xsdata_range.begin, xsdata_range.end])

        # Try to get proposal from path
        beamline, proposal = EDUtilsPath.getBeamlineProposal(directory)

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
        if EDUtilsPath.isALBA():
            _processDirectory = "_".join(pathToStartImage.split("_")[:-1])
            from datetime import datetime

            _id = datetime.now().strftime("%Y%m%d_%H%M%S")
            self.resultsDirectory = os.path.join(_processDirectory, "autoPROC_%s" % _id)
        else:
            self.resultsDirectory = os.path.join(processDirectory, "results")
            if not os.path.exists(self.resultsDirectory):
                os.makedirs(self.resultsDirectory, 0o755)

        # Create path to pyarch
        self.pyarchDirectory = EDHandlerESRFPyarchv1_0.createPyarchFilePath(
            self.resultsDirectory
        )
        if self.pyarchDirectory is not None:
            self.pyarchDirectory = self.pyarchDirectory.replace(
                "PROCESSED_DATA", "RAW_DATA"
            )
            if not os.path.exists(self.pyarchDirectory):
                try:
                    os.makedirs(self.pyarchDirectory, 0o755)
                except Exception:
                    self.pyarchDirectory = None

        # The resultsDirectory is not used at ALBA (only pyarchDirectory)
        if EDUtilsPath.isALBA():
            self.resultsDirectory = None

        # Determine pyarch prefix
        if EDUtilsPath.isALBA():
            listPrefix = template.split("_")
            self.pyarchPrefix = "ap_{0}_{1}".format(
                "_".join(listPrefix[:-2]), listPrefix[-2]
            )
        else:
            listPrefix = template.split("_")
            self.pyarchPrefix = "ap_{0}_run{1}".format(listPrefix[-3], listPrefix[-2])

        isH5 = False
        if any(beamline in pathToStartImage for beamline in ["id30a1"]):
            minSizeFirst = 2000000
            minSizeLast = 2000000
        elif any(
            beamline in pathToStartImage
            for beamline in ["id23eh1", "id23eh2", "id30a3", "id30b"]
        ):
            minSizeFirst = 100000
            minSizeLast = 100000
            pathToStartImage = os.path.join(
                directory, self.eiger_template_to_image(template, imageNoStart)
            )
            pathToEndImage = os.path.join(
                directory, self.eiger_template_to_image(template, imageNoEnd)
            )
            isH5 = True
        else:
            minSizeFirst = 1000000
            minSizeLast = 1000000

        if EDUtilsPath.isMAXIV():
            minSizeFirst = 100000
            minSizeLast = 100000
            pathToStartImage = os.path.join(
                directory, self.eiger_template_to_image(template, imageNoStart)
            )
            pathToEndImage = os.path.join(
                directory, self.eiger_template_to_image(template, imageNoEnd)
            )
            isH5 = True

        if EDUtilsPath.isEMBL() or EDUtilsPath.isMAXIV():
            fWaitFileTimeout = 60  # s
        else:
            fWaitFileTimeout = 3600  # s

        xsDataInputMXWaitFileFirst = XSDataInputMXWaitFile()
        xsDataInputMXWaitFileFirst.file = XSDataFile(XSDataString(pathToStartImage))
        xsDataInputMXWaitFileFirst.timeOut = XSDataTime(fWaitFileTimeout)
        self.edPluginWaitFileFirst.size = XSDataInteger(minSizeFirst)
        self.edPluginWaitFileFirst.dataInput = xsDataInputMXWaitFileFirst
        self.edPluginWaitFileFirst.executeSynchronous()
        if self.edPluginWaitFileFirst.dataOutput.timedOut.value:
            strWarningMessage = (
                "Timeout after %d seconds waiting for the first image %s!"
                % (fWaitFileTimeout, pathToStartImage)
            )
            self.addWarningMessage(strWarningMessage)
            self.WARNING(strWarningMessage)

        xsDataInputMXWaitFileLast = XSDataInputMXWaitFile()
        xsDataInputMXWaitFileLast.file = XSDataFile(XSDataString(pathToEndImage))
        xsDataInputMXWaitFileLast.timeOut = XSDataTime(fWaitFileTimeout)
        self.edPluginWaitFileLast.size = XSDataInteger(minSizeLast)
        self.edPluginWaitFileLast.dataInput = xsDataInputMXWaitFileLast
        self.edPluginWaitFileLast.executeSynchronous()
        if self.edPluginWaitFileLast.dataOutput.timedOut.value:
            strErrorMessage = (
                "Timeout after %d seconds waiting for the last image %s!"
                % (fWaitFileTimeout, pathToEndImage)
            )
            self.addErrorMessage(strErrorMessage)
            self.ERROR(strErrorMessage)
            self.setFailure()

        self.timeStart = time.localtime()
        if self.dataInput.dataCollectionId is not None:
            # Set ISPyB to running
            if self.doAnom:
                (
                    self.autoProcIntegrationIdAnom,
                    self.autoProcProgramIdAnom,
                ) = EDHandlerXSDataISPyBv1_4.setIspybToRunning(
                    self,
                    dataCollectionId=self.dataInput.dataCollectionId.value,
                    processingCommandLine=self.processingCommandLine,
                    processingPrograms=self.processingProgram,
                    isAnom=True,
                    timeStart=self.timeStart,
                )
                (
                    self.autoProcIntegrationIdAnomStaraniso,
                    self.autoProcProgramIdAnomStaraniso,
                ) = EDHandlerXSDataISPyBv1_4.setIspybToRunning(
                    self,
                    dataCollectionId=self.dataInput.dataCollectionId.value,
                    processingCommandLine=self.processingCommandLine,
                    processingPrograms=self.processingProgramStaraniso,
                    isAnom=True,
                    timeStart=self.timeStart,
                )
            if self.doNoanom:
                (
                    self.autoProcIntegrationIdNoanom,
                    self.autoProcProgramIdNoanom,
                ) = EDHandlerXSDataISPyBv1_4.setIspybToRunning(
                    self,
                    dataCollectionId=self.dataInput.dataCollectionId.value,
                    processingCommandLine=self.processingCommandLine,
                    processingPrograms=self.processingProgram,
                    isAnom=False,
                    timeStart=self.timeStart,
                )
                (
                    self.autoProcIntegrationIdNoanomStaraniso,
                    self.autoProcProgramIdNoanomStaraniso,
                ) = EDHandlerXSDataISPyBv1_4.setIspybToRunning(
                    self,
                    dataCollectionId=self.dataInput.dataCollectionId.value,
                    processingCommandLine=self.processingCommandLine,
                    processingPrograms=self.processingProgramStaraniso,
                    isAnom=False,
                    timeStart=self.timeStart,
                )

        # Prepare input to execution plugin
        if self.doAnom:
            xsDataInputAutoPROCAnom = XSDataInputAutoPROC()
            xsDataInputAutoPROCAnom.anomalous = XSDataBoolean(True)
            xsDataInputAutoPROCAnom.symm = self.dataInput.symm
            xsDataInputAutoPROCAnom.cell = self.dataInput.cell
            xsDataInputAutoPROCAnom.lowResolutionLimit = (
                self.dataInput.lowResolutionLimit
            )
            xsDataInputAutoPROCAnom.highResolutionLimit = (
                self.dataInput.highResolutionLimit
            )
        if self.doNoanom:
            xsDataInputAutoPROCNoanom = XSDataInputAutoPROC()
            xsDataInputAutoPROCNoanom.anomalous = XSDataBoolean(False)
            xsDataInputAutoPROCNoanom.symm = self.dataInput.symm
            xsDataInputAutoPROCNoanom.cell = self.dataInput.cell
            xsDataInputAutoPROCNoanom.lowResolutionLimit = (
                self.dataInput.lowResolutionLimit
            )
            xsDataInputAutoPROCNoanom.highResolutionLimit = (
                self.dataInput.highResolutionLimit
            )
        if self.exclude_range is None or len(self.exclude_range) == 0:
            list_data_range = [[imageNoStart, imageNoEnd]]
        else:
            list_data_range = []
            first_iteration = True
            for exclude_begin, exclude_end in self.exclude_range:
                if first_iteration:
                    list_data_range.append([imageNoStart, exclude_begin-1])
                    first_iteration = False
                else:
                    list_data_range.append([next_include_begin, exclude_begin-1])
                next_include_begin = exclude_end + 1
            list_data_range.append([next_include_begin, imageNoEnd])
        for index, range in enumerate(list_data_range):
            begin, end = range
            xsDataAutoPROCIdentifier = XSDataAutoPROCIdentifier()
            xsDataAutoPROCIdentifier.idN = XSDataString(identifier + "_" + str(index+1))
            xsDataAutoPROCIdentifier.dirN = XSDataFile(XSDataString(directory))
            xsDataAutoPROCIdentifier.templateN = XSDataString(template)
            xsDataAutoPROCIdentifier.fromN = XSDataInteger(begin)
            xsDataAutoPROCIdentifier.toN = XSDataInteger(end)
            if self.doAnom:
                xsDataInputAutoPROCAnom.addIdentifier(xsDataAutoPROCIdentifier)
            if self.doNoanom:
                xsDataInputAutoPROCNoanom.addIdentifier(xsDataAutoPROCIdentifier.copy())
        if isH5:
            masterFilePath = os.path.join(
                directory, self.eiger_template_to_master(template)
            )
            if self.doAnom:
                xsDataInputAutoPROCAnom.masterH5 = XSDataFile(
                    XSDataString(masterFilePath)
                )
            if self.doNoanom:
                xsDataInputAutoPROCNoanom.masterH5 = XSDataFile(
                    XSDataString(masterFilePath)
                )
        timeStart = time.localtime()
        if self.doAnom:
            self.edPluginExecAutoPROCAnom.dataInput = xsDataInputAutoPROCAnom
            self.edPluginExecAutoPROCAnom.execute()
        if self.doNoanom:
            self.edPluginExecAutoPROCNoanom.dataInput = xsDataInputAutoPROCNoanom
            self.edPluginExecAutoPROCNoanom.execute()
        if self.doAnom:
            self.edPluginExecAutoPROCAnom.synchronize()
        if self.doNoanom:
            self.edPluginExecAutoPROCNoanom.synchronize()
        timeEnd = time.localtime()

        if self.dataInput.icatProcessDataDir is not None:
            icatProcessDataDir = self.dataInput.icatProcessDataDir.path.value
        else:
            icatProcessDataDir = None

        # Upload to ISPyB and ICAT
        self.screen("Uploading to ISPyB and ICAT")
        if self.doAnom:
            self.screen("Anom upload")
            xsDataInputStoreAutoProc_anom = self.uploadToISPyB(
                edPluginExecAutoPROC=self.edPluginExecAutoPROCAnom,
                isAnom=True,
                isStaraniso=False,
                proposal=proposal,
                timeStart=timeStart,
                timeEnd=timeEnd,
            )
            self.screen(f"{xsDataInputStoreAutoProc_anom} and {icatProcessDataDir}")
            if (
                xsDataInputStoreAutoProc_anom is not None
                and icatProcessDataDir is not None
            ):
                EDUtilsICAT.uploadToICAT(
                    processName="autoPROC",
                    xsDataInputStoreAutoProc=xsDataInputStoreAutoProc_anom,
                    directory=directory,
                    icatProcessDataDir=icatProcessDataDir,
                    isAnom=True,
                    beamline=beamline,
                    proposal=proposal,
                    timeStart=timeStart,
                    timeEnd=timeEnd,
                    reprocess=self.reprocess
                )
            xsDataInputStoreAutoProc_anom_staraniso = self.uploadToISPyB(
                edPluginExecAutoPROC=self.edPluginExecAutoPROCAnom,
                isAnom=True,
                isStaraniso=True,
                proposal=proposal,
                timeStart=timeStart,
                timeEnd=timeEnd,
            )
            self.screen(
                f"{xsDataInputStoreAutoProc_anom_staraniso} and {icatProcessDataDir}"
            )
            if (
                xsDataInputStoreAutoProc_anom_staraniso is not None
                and icatProcessDataDir is not None
            ):
                EDUtilsICAT.uploadToICAT(
                    processName="autoPROC_staraniso",
                    xsDataInputStoreAutoProc=xsDataInputStoreAutoProc_anom_staraniso,
                    directory=directory,
                    icatProcessDataDir=icatProcessDataDir,
                    isAnom=True,
                    beamline=beamline,
                    proposal=proposal,
                    timeStart=timeStart,
                    timeEnd=timeEnd,
                    reprocess=self.reprocess
                )

        if self.doNoanom:
            self.screen("Noanom upload")
            xsDataInputStoreAutoProc_noanom = self.uploadToISPyB(
                edPluginExecAutoPROC=self.edPluginExecAutoPROCNoanom,
                isAnom=False,
                isStaraniso=False,
                proposal=proposal,
                timeStart=timeStart,
                timeEnd=timeEnd,
            )
            if (
                xsDataInputStoreAutoProc_noanom is not None
                and icatProcessDataDir is not None
            ):
                EDUtilsICAT.uploadToICAT(
                    processName="autoPROC",
                    xsDataInputStoreAutoProc=xsDataInputStoreAutoProc_noanom,
                    directory=directory,
                    icatProcessDataDir=icatProcessDataDir,
                    isAnom=False,
                    beamline=beamline,
                    proposal=proposal,
                    timeStart=timeStart,
                    timeEnd=timeEnd,
                    reprocess=self.reprocess
                )
            xsDataInputStoreAutoProc_noanom_staraniso = self.uploadToISPyB(
                edPluginExecAutoPROC=self.edPluginExecAutoPROCNoanom,
                isAnom=False,
                isStaraniso=True,
                proposal=proposal,
                timeStart=timeStart,
                timeEnd=timeEnd,
            )
            if (
                xsDataInputStoreAutoProc_noanom_staraniso is not None
                and icatProcessDataDir is not None
            ):
                EDUtilsICAT.uploadToICAT(
                    processName="autoPROC_staraniso",
                    xsDataInputStoreAutoProc=xsDataInputStoreAutoProc_noanom_staraniso,
                    directory=directory,
                    icatProcessDataDir=icatProcessDataDir,
                    isAnom=False,
                    beamline=beamline,
                    proposal=proposal,
                    timeStart=timeStart,
                    timeEnd=timeEnd,
                    reprocess=self.reprocess
                )

    def finallyProcess(self, _edObject=None):
        EDPluginControl.finallyProcess(self)
        if self.doAnom:
            self.edPluginExecAutoPROCAnom.synchronize()
        if self.doNoanom:
            self.edPluginExecAutoPROCNoanom.synchronize()
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
            self.timeEnd = time.localtime()
            if self.dataInput.dataCollectionId is not None:
                # Upload program status to ISPyB
                # anom
                if self.doAnom:
                    if not self.hasUploadedAnomResultsToISPyB:
                        EDHandlerXSDataISPyBv1_4.setIspybToFailed(
                            self,
                            dataCollectionId=self.dataInput.dataCollectionId.value,
                            autoProcIntegrationId=self.autoProcIntegrationIdAnom,
                            autoProcProgramId=self.autoProcProgramIdAnom,
                            processingCommandLine=self.processingCommandLine,
                            processingPrograms=self.processingProgram,
                            isAnom=True,
                            timeStart=self.timeStart,
                            timeEnd=self.timeEnd,
                        )
                    if not self.hasUploadedAnomStaranisoResultsToISPyB:
                        EDHandlerXSDataISPyBv1_4.setIspybToFailed(
                            self,
                            dataCollectionId=self.dataInput.dataCollectionId.value,
                            autoProcIntegrationId=self.autoProcIntegrationIdAnom,
                            autoProcProgramId=self.autoProcProgramIdAnom,
                            processingCommandLine=self.processingCommandLine,
                            processingPrograms=self.processingProgramStaraniso,
                            isAnom=True,
                            timeStart=self.timeStart,
                            timeEnd=self.timeEnd,
                        )

                if self.doNoanom:
                    # noanom
                    if not self.hasUploadedNoanomResultsToISPyB:
                        EDHandlerXSDataISPyBv1_4.setIspybToFailed(
                            self,
                            dataCollectionId=self.dataInput.dataCollectionId.value,
                            autoProcIntegrationId=self.autoProcIntegrationIdNoanom,
                            autoProcProgramId=self.autoProcProgramIdNoanom,
                            processingCommandLine=self.processingCommandLine,
                            processingPrograms=self.processingProgram,
                            isAnom=False,
                            timeStart=self.timeStart,
                            timeEnd=self.timeEnd,
                        )
                    if not self.hasUploadedNoanomStaranisoResultsToISPyB:
                        EDHandlerXSDataISPyBv1_4.setIspybToFailed(
                            self,
                            dataCollectionId=self.dataInput.dataCollectionId.value,
                            autoProcIntegrationId=self.autoProcIntegrationIdNoanom,
                            autoProcProgramId=self.autoProcProgramIdNoanom,
                            processingCommandLine=self.processingCommandLine,
                            processingPrograms=self.processingProgramStaraniso,
                            isAnom=False,
                            timeStart=self.timeStart,
                            timeEnd=self.timeEnd,
                        )

    def uploadToISPyB(
        self, edPluginExecAutoPROC, isAnom, isStaraniso, proposal, timeStart, timeEnd
    ):
        if isAnom:
            anomString = "anom"
        else:
            anomString = "noanom"
        if isStaraniso:
            staranisoString = "_staraniso"
        else:
            staranisoString = ""
        # Read the generated ISPyB xml file
        pathToISPyBXML = None
        xsDataInputStoreAutoProc = None
        if isStaraniso:
            if edPluginExecAutoPROC.dataOutput.ispybXML_staraniso is not None:
                pathToISPyBXML = (
                    edPluginExecAutoPROC.dataOutput.ispybXML_staraniso.path.value
                )
        elif edPluginExecAutoPROC.dataOutput.ispybXML is not None:
            pathToISPyBXML = edPluginExecAutoPROC.dataOutput.ispybXML.path.value
        if pathToISPyBXML is not None:
            autoProcContainer = AutoProcContainer.parseFile(pathToISPyBXML)
            # "Fix" certain entries in the ISPyB xml file
            autoProcScalingContainer = autoProcContainer.AutoProcScalingContainer
            for (
                autoProcScalingStatistics
            ) in autoProcScalingContainer.AutoProcScalingStatistics:
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
            autoProcIntegrationContainer = (
                autoProcScalingContainer.AutoProcIntegrationContainer
            )
            image = autoProcIntegrationContainer.Image
            if self.dataInput.dataCollectionId is not None:
                image.dataCollectionId = self.dataInput.dataCollectionId.value
            autoProcIntegration = autoProcIntegrationContainer.AutoProcIntegration
            autoProcProgramContainer = autoProcContainer.AutoProcProgramContainer
            autoProcProgram = autoProcProgramContainer.AutoProcProgram
            if isAnom:
                autoProcIntegration.anomalous = True
                if isStaraniso:
                    autoProcIntegration.autoProcIntegrationId = (
                        self.autoProcIntegrationIdAnomStaraniso
                    )
                    autoProcProgram.autoProcProgramId = (
                        self.autoProcProgramIdAnomStaraniso
                    )
                else:
                    autoProcIntegration.autoProcIntegrationId = (
                        self.autoProcIntegrationIdAnom
                    )
                    autoProcProgram.autoProcProgramId = self.autoProcProgramIdAnom
            else:
                autoProcIntegration.anomalous = False
                if isStaraniso:
                    autoProcIntegration.autoProcIntegrationId = (
                        self.autoProcIntegrationIdNoanomStaraniso
                    )
                    autoProcProgram.autoProcProgramId = (
                        self.autoProcProgramIdNoanomStaraniso
                    )
                else:
                    autoProcIntegration.autoProcIntegrationId = (
                        self.autoProcIntegrationIdNoanom
                    )
                    autoProcProgram.autoProcProgramId = self.autoProcProgramIdNoanom
            autoProcProgram.processingPrograms = "autoPROC" + staranisoString
            autoProcProgram.processingStartTime = time.strftime(
                "%a %b %d %H:%M:%S %Y", timeStart
            )
            autoProcProgram.processingEndTime = time.strftime(
                "%a %b %d %H:%M:%S %Y", timeEnd
            )
            autoProcProgram.processingStatus = "SUCCESS"
            # EDNA-245 - remove "truncate_{early,late}-unique.mtz" from
            # autoProcProgramContainer.AutoProcProgramAttachment
            autoProcProgramContainer.AutoProcProgramAttachment[:] = [
                x
                for x in autoProcProgramContainer.AutoProcProgramAttachment
                if not self.matchesTruncateEarlyLate(x.fileName)
            ]
            for (
                autoProcProgramAttachment
            ) in autoProcProgramContainer.AutoProcProgramAttachment:
                if autoProcProgramAttachment.fileName == "summary.html":
                    # Check if summary_inlined.html exists
                    summaryInlinedHtmlPath = os.path.join(
                        autoProcProgramAttachment.filePath, "summary_inlined.html"
                    )
                    if os.path.exists(summaryInlinedHtmlPath):
                        summaryName = "summary_inlined"
                        summaryHtmlPath = summaryInlinedHtmlPath
                    else:
                        summaryName = "summary"
                        summaryHtmlPath = os.path.join(
                            autoProcProgramAttachment.filePath,
                            autoProcProgramAttachment.fileName,
                        )
                    # Replace opidXX with user name
                    htmlSummary = open(summaryHtmlPath).read()
                    userString1 = "User      : {0} (".format(os.environ["USER"])
                    userString2 = "User      : {0} (".format(proposal)
                    htmlSummary = htmlSummary.replace(userString1, userString2)
                    open(summaryHtmlPath, "w").write(htmlSummary)
                    # Upload summary.html
                    pathtoFile = summaryHtmlPath
                    pyarchFile = self.pyarchPrefix + "_{0}_{1}.html".format(
                        anomString, summaryName
                    )
                    if pyarchFile not in self.listPyarchFile:
                        if self.resultsDirectory:
                            shutil.copy(
                                pathtoFile,
                                os.path.join(self.resultsDirectory, pyarchFile),
                            )
                            self.listPyarchFile.append(pyarchFile)
                    if self.pyarchDirectory is not None:
                        shutil.copy(
                            pathtoFile, os.path.join(self.pyarchDirectory, pyarchFile)
                        )
                        autoProcProgramAttachment.fileName = os.path.basename(
                            pyarchFile
                        )
                        autoProcProgramAttachment.filePath = self.pyarchDirectory
                        autoProcProgramAttachment.fileType = "Log"

                    if summaryName == "summary":
                        # Convert the summary.html to summary.pdf
                        xsDataInputHTML2PDF = XSDataInputHTML2PDF()
                        xsDataInputHTML2PDF.addHtmlFile(
                            XSDataFile(XSDataString(summaryHtmlPath))
                        )
                        xsDataInputHTML2PDF.paperSize = XSDataString("A3")
                        xsDataInputHTML2PDF.lowQuality = XSDataBoolean(True)
                        edPluginHTML2Pdf = self.loadPlugin(
                            "EDPluginHTML2PDFv1_0",
                            "EDPluginHTML2PDFv1_0_{0}".format(anomString),
                        )
                        edPluginHTML2Pdf.dataInput = xsDataInputHTML2PDF
                        edPluginHTML2Pdf.executeSynchronous()
                        pdfFile = edPluginHTML2Pdf.dataOutput.pdfFile.path.value
                        pyarchPdfFile = (
                            self.pyarchPrefix
                            + "_"
                            + anomString
                            + "_"
                            + os.path.basename(pdfFile)
                        )
                        # Copy file to results directory and pyarch
                        if self.resultsDirectory:
                            shutil.copy(
                                pdfFile,
                                os.path.join(self.resultsDirectory, pyarchPdfFile),
                            )
                        if self.pyarchDirectory is not None:
                            shutil.copy(
                                pdfFile,
                                os.path.join(self.pyarchDirectory, pyarchPdfFile),
                            )
                            autoProcProgramAttachmentPdf = AutoProcProgramAttachment()
                            autoProcProgramAttachmentPdf.fileName = pyarchPdfFile
                            autoProcProgramAttachmentPdf.filePath = self.pyarchDirectory
                            autoProcProgramAttachmentPdf.fileType = "Log"
                            autoProcProgramContainer.addAutoProcProgramAttachment(
                                autoProcProgramAttachmentPdf
                            )
                elif autoProcProgramAttachment.fileName == "truncate-unique.mtz":
                    pathtoFile = os.path.join(
                        autoProcProgramAttachment.filePath,
                        autoProcProgramAttachment.fileName,
                    )
                    pyarchFile = self.pyarchPrefix + "_{0}_truncate.mtz".format(
                        anomString
                    )
                    if self.resultsDirectory:
                        shutil.copy(
                            pathtoFile, os.path.join(self.resultsDirectory, pyarchFile)
                        )
                    if self.pyarchDirectory is not None:
                        shutil.copy(
                            pathtoFile, os.path.join(self.pyarchDirectory, pyarchFile)
                        )
                        autoProcProgramAttachment.fileName = pyarchFile
                        autoProcProgramAttachment.filePath = self.pyarchDirectory
                else:
                    pathtoFile = os.path.join(
                        autoProcProgramAttachment.filePath,
                        autoProcProgramAttachment.fileName,
                    )
                    pyarchFile = (
                        self.pyarchPrefix
                        + "_"
                        + anomString
                        + "_"
                        + autoProcProgramAttachment.fileName
                    )
                    if self.resultsDirectory:
                        shutil.copy(
                            pathtoFile, os.path.join(self.resultsDirectory, pyarchFile)
                        )
                    if self.pyarchDirectory is not None:
                        shutil.copy(
                            pathtoFile, os.path.join(self.pyarchDirectory, pyarchFile)
                        )
                        autoProcProgramAttachment.fileName = pyarchFile
                        autoProcProgramAttachment.filePath = self.pyarchDirectory
            # Add XSCALE.LP file if present
            processDirectory = edPluginExecAutoPROC.dataOutput.processDirectory[
                0
            ].path.value
            pathToXSCALELog = os.path.join(processDirectory, "XSCALE.LP")
            if os.path.exists(pathToXSCALELog):
                pyarchXSCALELog = self.pyarchPrefix + "_merged_{0}_XSCALE.LP".format(
                    anomString
                )
                if self.resultsDirectory:
                    shutil.copy(
                        pathToXSCALELog,
                        os.path.join(self.resultsDirectory, pyarchXSCALELog),
                    )
                if self.pyarchDirectory is not None:
                    shutil.copy(
                        pathToXSCALELog,
                        os.path.join(self.pyarchDirectory, pyarchXSCALELog),
                    )
                    autoProcProgramAttachment = AutoProcProgramAttachment()
                    autoProcProgramAttachment.fileName = pyarchXSCALELog
                    autoProcProgramAttachment.filePath = self.pyarchDirectory
                    autoProcProgramAttachment.fileType = "Result"
                    autoProcProgramContainer.addAutoProcProgramAttachment(
                        autoProcProgramAttachment
                    )
            # Add XDS_ASCII.HKL if present and gzip it
            pathToXdsAsciiHkl = os.path.join(processDirectory, "XDS_ASCII.HKL")
            if os.path.exists(pathToXdsAsciiHkl) and self.pyarchDirectory is not None:
                pyarchXdsAsciiHkl = self.pyarchPrefix + "_{0}_XDS_ASCII.HKL.gz".format(
                    anomString
                )
                with open(pathToXdsAsciiHkl, "rb") as f_in:
                    with gzip.open(
                        os.path.join(self.pyarchDirectory, pyarchXdsAsciiHkl), "wb"
                    ) as f_out:
                        shutil.copyfileobj(f_in, f_out)
                if self.resultsDirectory:
                    shutil.copy(
                        os.path.join(self.pyarchDirectory, pyarchXdsAsciiHkl),
                        os.path.join(self.resultsDirectory, pyarchXdsAsciiHkl),
                    )
                autoProcProgramAttachment = AutoProcProgramAttachment()
                autoProcProgramAttachment.fileName = pyarchXdsAsciiHkl
                autoProcProgramAttachment.filePath = self.pyarchDirectory
                autoProcProgramAttachment.fileType = "Result"
                autoProcProgramContainer.addAutoProcProgramAttachment(
                    autoProcProgramAttachment
                )
            # Add XPARM.XDS and GXPARM.XDS if present
            xparm_xds_path = os.path.join(processDirectory, "XPARM.XDS")
            if os.path.exists(xparm_xds_path):
                pyarch_xparm_xds_name = self.pyarchPrefix + "_{0}_XPARM.XDS".format(anomString)
                if self.resultsDirectory:
                    shutil.copy(
                        xparm_xds_path,
                        os.path.join(self.resultsDirectory, pyarch_xparm_xds_name),
                    )
                shutil.copyfile(
                    xparm_xds_path,
                    os.path.join(self.pyarchDirectory, pyarch_xparm_xds_name)
                )
                autoProcProgramAttachment = AutoProcProgramAttachment()
                autoProcProgramAttachment.fileName = pyarch_xparm_xds_name
                autoProcProgramAttachment.filePath = self.pyarchDirectory
                autoProcProgramAttachment.fileType = "Result"
                autoProcProgramContainer.addAutoProcProgramAttachment(
                    autoProcProgramAttachment
                )
            gxparm_xds_path = os.path.join(processDirectory, "GXPARM.XDS")
            if os.path.exists(gxparm_xds_path):
                pyarch_gxparm_xds_name = self.pyarchPrefix + "_{0}_GXPARM.XDS".format(anomString)
                if self.resultsDirectory:
                    shutil.copy(
                        gxparm_xds_path,
                        os.path.join(self.resultsDirectory, pyarch_gxparm_xds_name),
                    )
                shutil.copyfile(
                    gxparm_xds_path,
                    os.path.join(self.pyarchDirectory, pyarch_gxparm_xds_name)
                )
                autoProcProgramAttachment = AutoProcProgramAttachment()
                autoProcProgramAttachment.fileName = pyarch_gxparm_xds_name
                autoProcProgramAttachment.filePath = self.pyarchDirectory
                autoProcProgramAttachment.fileType = "Result"
                autoProcProgramContainer.addAutoProcProgramAttachment(
                    autoProcProgramAttachment
                )
            # Add log file
            pathToLogFile = edPluginExecAutoPROC.dataOutput.logFile.path.value
            autoPROClog = open(pathToLogFile).read()
            userString1 = "User      : {0} (".format(os.environ["USER"])
            userString2 = "User      : {0} (".format(proposal)
            autoPROClog = autoPROClog.replace(userString1, userString2)
            open(pathToLogFile, "w").write(autoPROClog)
            pyarchLogFile = self.pyarchPrefix + "_{0}_autoPROC.log".format(anomString)
            if self.resultsDirectory:
                shutil.copy(
                    pathToLogFile, os.path.join(self.resultsDirectory, pyarchLogFile)
                )
            if self.pyarchDirectory is not None:
                shutil.copy(
                    pathToLogFile, os.path.join(self.pyarchDirectory, pyarchLogFile)
                )
                autoProcProgramAttachment = AutoProcProgramAttachment()
                autoProcProgramAttachment.fileName = pyarchLogFile
                autoProcProgramAttachment.filePath = self.pyarchDirectory
                autoProcProgramAttachment.fileType = "Log"
                autoProcProgramContainer.addAutoProcProgramAttachment(
                    autoProcProgramAttachment
                )
            # Add report.pdf
            pathToRepordPdf = None
            if (
                isStaraniso
                and edPluginExecAutoPROC.dataOutput.reportPdf_staraniso is not None
            ):
                pathToRepordPdf = (
                    edPluginExecAutoPROC.dataOutput.reportPdf_staraniso.path.value
                )
            elif edPluginExecAutoPROC.dataOutput.reportPdf is not None:
                pathToRepordPdf = edPluginExecAutoPROC.dataOutput.reportPdf.path.value
            if pathToRepordPdf is not None:
                pyarchReportFile = self.pyarchPrefix + "_{0}_{1}".format(
                    anomString, os.path.basename(pathToRepordPdf)
                )
                if self.resultsDirectory:
                    shutil.copy(
                        pathToRepordPdf,
                        os.path.join(self.resultsDirectory, pyarchReportFile),
                    )
                if self.pyarchDirectory is not None:
                    shutil.copy(
                        pathToRepordPdf,
                        os.path.join(self.pyarchDirectory, pyarchReportFile),
                    )
                    autoProcProgramAttachment = AutoProcProgramAttachment()
                    autoProcProgramAttachment.fileName = pyarchReportFile
                    autoProcProgramAttachment.filePath = self.pyarchDirectory
                    autoProcProgramAttachment.fileType = "Log"
                    autoProcProgramContainer.addAutoProcProgramAttachment(
                        autoProcProgramAttachment
                    )

            # Upload the xml to ISPyB
            xsDataInputStoreAutoProc = XSDataInputStoreAutoProc()
            xsDataInputStoreAutoProc.AutoProcContainer = autoProcContainer
            edPluginStoreAutoprocAnom = self.loadPlugin(
                "EDPluginISPyBStoreAutoProcv1_4",
                "ISPyBStoreAutoProcv1_4_{0}{1}".format(anomString, staranisoString),
            )
            edPluginStoreAutoprocAnom.dataInput = xsDataInputStoreAutoProc
            edPluginStoreAutoprocAnom.executeSynchronous()
            isSuccess = not edPluginStoreAutoprocAnom.isFailure()
            if isSuccess:
                self.screen(
                    "{0}{1} results uploaded to ISPyB".format(
                        anomString, staranisoString
                    )
                )
                if isAnom:
                    if isStaraniso:
                        self.hasUploadedAnomStaranisoResultsToISPyB = True
                    else:
                        self.hasUploadedAnomResultsToISPyB = True
                else:
                    if isStaraniso:
                        self.hasUploadedNoanomStaranisoResultsToISPyB = True
                    else:
                        self.hasUploadedNoanomResultsToISPyB = True
            else:
                self.screen(
                    "Could not upload {0}{1} results to ISPyB".format(
                        anomString, staranisoString
                    )
                )
        return xsDataInputStoreAutoProc


    def eiger_template_to_image(self, fmt, num):
        fileNumber = int(num / 100)
        if fileNumber == 0:
            fileNumber = 1
        if EDUtilsPath.isMAXIV():
            fmt_string = fmt.replace("%06d", "data_%06d" % fileNumber)
        else:
            fmt_string = fmt.replace("####", "1_data_%06d" % fileNumber)
        return fmt_string.format(num)

    def eiger_template_to_master(self, fmt):
        if EDUtilsPath.isMAXIV():
            fmt_string = fmt.replace("%06d", "master")
        else:
            fmt_string = fmt.replace("####", "1_master")
        return fmt_string

    def matchesTruncateEarlyLate(self, fileName):
        value = False
        if (
            fileName == "truncate_early-unique.mtz"
            or fileName == "truncate_late-unique.mtz"
        ):
            value = True
        return value
