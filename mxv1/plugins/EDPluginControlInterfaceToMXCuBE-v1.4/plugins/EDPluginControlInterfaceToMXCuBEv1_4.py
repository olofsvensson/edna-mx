#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2016 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Olof Svensson (svensson@esrf.fr)
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
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
import smtplib
import time
import socket
import tempfile
import xml

try:
    from xmlrpclib import ServerProxy
    from xmlrpclib import Transport
except:
    from xmlrpc.client import ServerProxy
    from xmlrpc.client import Transport

from EDMessage import EDMessage
from EDPluginControl import EDPluginControl
from EDUtilsFile import EDUtilsFile
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsImage import EDUtilsImage
from EDConfiguration import EDConfiguration
from EDUtilsPath import EDUtilsPath
from EDUtilsICAT import EDUtilsICAT
from EDHandlerESRFPyarchv1_0 import EDHandlerESRFPyarchv1_0

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataFlux
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataDictionary
from XSDataCommon import XSDataKeyValuePair
from XSDataCommon import XSDataSize
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataTime

from XSDataMXv1 import XSDataInputControlISPyB
from XSDataMXv1 import XSDataResultCharacterisation

from XSDataMXCuBEv1_4 import XSDataInputMXCuBE
from XSDataMXCuBEv1_4 import XSDataResultMXCuBE

EDFactoryPluginStatic.loadModule("XSDataMXWaitFilev1_1")
from XSDataMXWaitFilev1_1 import XSDataInputMXWaitFile

EDFactoryPluginStatic.loadModule("XSDataSimpleHTMLPagev1_1")
from XSDataSimpleHTMLPagev1_1 import XSDataInputSimpleHTMLPage

EDFactoryPluginStatic.loadModule("XSDataInterfacev1_2")
from XSDataInterfacev1_2 import XSDataInputInterface

EDFactoryPluginStatic.loadModule("XSDataISPyBv1_4")
from XSDataISPyBv1_4 import XSDataInputRetrieveDataCollection
from XSDataISPyBv1_4 import XSDataInputISPyBSetBestWilsonPlotPath
from XSDataISPyBv1_4 import XSDataISPyBWorkflow
from XSDataISPyBv1_4 import XSDataInputISPyBStoreWorkflow
from XSDataISPyBv1_4 import XSDataInputISPyBStoreWorkflowStep
from XSDataISPyBv1_4 import XSDataInputISPyBUpdateDataCollectionGroupWorkflowId

EDFactoryPluginStatic.loadModule("XSDataControlH5ToCBFv1_1")
from XSDataControlH5ToCBFv1_1 import XSDataInputControlH5ToCBF

from EDHandlerXSDataISPyBv1_4 import EDHandlerXSDataISPyBv1_4

class TokenTransport(Transport):

    def __init__(self, token, use_datetime=0):
        Transport.__init__(self, use_datetime=use_datetime)
        self.token = token

    def send_content(self, connection, request_body):
        connection.putheader("Content-Type", "text/xml")
        connection.putheader("Content-Length", str(len(request_body)))
        connection.putheader("Token", self.token)
        connection.endheaders()
        if request_body:
            connection.send(request_body)


class EDPluginControlInterfaceToMXCuBEv1_4(EDPluginControl):
    """
    This is the plugin interface to launch the MXv1 characterisation from an MXCuBE gui.
    It is for the moment a wrapper for the EDPluginControlCCP4iv1_1 plugin, which also
    runs the ISPyB control plugin if a data collection id is available.
    """

    EDNA_CONTACT_EMAIL = "contactEmail"
    EDNA_EMAIL_SENDER = "emailSender"


    def __init__ (self):
        """
        Initialisation of EDPluginControlInterfaceToMXCuBEv1_4:
        - Input data type class : XSDataInputMXCuBE
        - Name of default characterisation plugin : EDPluginControlCharacterisationv1_1
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputMXCuBE)
        self.strPluginMXWaitFileName = "EDPluginMXWaitFilev1_1"
        self.strPluginControlInterface = "EDPluginControlInterfacev1_2"
        self.edPluginControlInterface = None
        self.strPluginControlISPyB = "EDPluginControlISPyBv1_4"
        self.edPluginControlISPyB = None
        self.xsDataResultMXCuBE = None
        self.xsDataIntegerDataCollectionId = None
        self.strPluginExecOutputHTMLName = "EDPluginExecOutputHTMLv1_0"
        self.edPluginExecOutputHTML = None
        self.strPluginExecSimpleHTMLName = "EDPluginExecSimpleHTMLPagev1_1"
        self.edPluginExecSimpleHTML = None
        self.strPluginISPyBRetrieveDataCollection = "EDPluginISPyBRetrieveDataCollectionv1_4"
        self.edPluginISPyBRetrieveDataCollection = None
        self.strPluginControlH5ToCBF = "EDPluginControlH5ToCBFv1_1"
        self.edPluginControlH5ToCBF = None
        self.strPluginStoreWorkflow = "EDPluginISPyBStoreWorkflowv1_4"
        self.edPluginStoreWorkflow = None
        self.strPluginStoreWorkflowStep = "EDPluginISPyBStoreWorkflowStepv1_4"
        self.edPluginStoreWorkflowStep = None
        self.strUpdateDataCollectionGroupWorkflowId = "EDPluginISPyBUpdateDataCollectionGroupWorkflowIdv1_4"
        self.edPluginUpdateDataCollectionGroupWorkflowId = None
        self.strEDNAContactEmail = None
        self.strEDNAEmailSender = "edna-support@esrf.fr"
        self.tStart = None
        self.tStop = None
        self.fFluxThreshold = 1e3
        self.bIsEigerDetector = False
        self.xsDataFirstImage = None
        self.strMxCuBE_URI = None
        self.serverProxy = None
        self.minImageSize = 100000
        self.fMXWaitFileTimeOut = 60
        self.strSubject = None
        self.strMessage = None

    def checkParameters(self):
        """
        Checks the mandatory input parameters :
        - dataSet
        - outputFileDirectory
        """
        self.verboseDebug("EDPluginControlInterfaceToMXCuBEv1_4.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDataSet(), "dataSet")


    def configure(self):
        EDPluginControl.configure(self)
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_4.configure")
        self.strEDNAEmailSender = self.config.get(self.EDNA_EMAIL_SENDER, self.strEDNAEmailSender)
        self.strEDNAContactEmail = self.config.get(self.EDNA_CONTACT_EMAIL, self.strEDNAContactEmail)
        self.strMxCuBE_URI = self.config.get("mxCuBE_URI", None)
        self.minImageSize = int(self.config.get("minImageSize", self.minImageSize))
        self.fMXWaitFileTimeOut = int(self.config.get("fileTimeOut", self.fMXWaitFileTimeOut))



    def preProcess(self, _edPlugin=None):
        """
        This method prepares the input for the CCP4i plugin and loads it.
        """
        EDPluginControl.preProcess(self, _edPlugin)
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_4.preProcess...")

        self.tStart = time.time()

        # self.edPluginExecOutputHTML = self.loadPlugin(self.strPluginExecOutputHTMLName, "OutputHTML")
        self.edPluginExecSimpleHTML = self.loadPlugin(self.strPluginExecSimpleHTMLName, "SimpleHTML")
        self.edPluginISPyBRetrieveDataCollection = self.loadPlugin(self.strPluginISPyBRetrieveDataCollection, \
                                                                   "ISPyBRetrieveDataCollection")
        self.xsDataResultMXCuBE = XSDataResultMXCuBE()



    def process(self, _edPlugin=None):
        EDPluginControl.process(self, _edPlugin)
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_4.process...")

        xsDataInputMXCuBE = self.getDataInput()

        if xsDataInputMXCuBE.token is not None:
            strToken = xsDataInputMXCuBE.token.value
        else:
            strToken = None
        if self.strMxCuBE_URI is not None:
            self.DEBUG("Enabling sending messages to mxCuBE via URI {0}".format(self.strMxCuBE_URI))
            if strToken is None:
                self.serverProxy = ServerProxy(self.strMxCuBE_URI)
            else:
                self.serverProxy = ServerProxy(self.strMxCuBE_URI, transport=TokenTransport(strToken))

        xsDataInputInterface = XSDataInputInterface()
        self.edPluginControlInterface = self.loadPlugin(self.strPluginControlInterface)
        self.xsDataFirstImage = None
        dictH5ToCBFPlugin = {}
        pluginIndex = 1
        for xsDataSetMXCuBE in xsDataInputMXCuBE.dataSet:
            for xsDataImage in xsDataSetMXCuBE.imageFile:
                imagePath = xsDataImage.path.value
                if os.path.exists(imagePath):
                    message = "Input file ok: {0}".format(imagePath)
                    self.screen(message)
                    # self.sendMessageToMXCuBE(message)
                else:
                    self.sendMessageToMXCuBE(
                        "Waiting for file: {0}, timeout {1} s".format(imagePath, self.fMXWaitFileTimeOut))
                    edPluginMXWaitFile = self.loadPlugin(self.strPluginMXWaitFileName)
                    xsDataInputMXWaitFile = XSDataInputMXWaitFile()
                    xsDataInputMXWaitFile.file = XSDataFile(XSDataString(imagePath))
                    xsDataInputMXWaitFile.setSize(XSDataInteger(self.minImageSize))
                    xsDataInputMXWaitFile.setTimeOut(XSDataTime(self.fMXWaitFileTimeOut))
                    self.DEBUG("Wait file timeOut set to %f" % self.fMXWaitFileTimeOut)
                    edPluginMXWaitFile.setDataInput(xsDataInputMXWaitFile)
                    edPluginMXWaitFile.executeSynchronous()
                    if edPluginMXWaitFile.dataOutput.timedOut.value:
                        errorMessage = "ERROR! File {0} does not exist on disk.".format(imagePath)
                        self.ERROR(errorMessage)
                        self.sendMessageToMXCuBE(errorMessage, "error")
                        self.setFailure()
                        break
                if xsDataImage.path.value.endswith(".h5"):
                    self.bIsEigerDetector = True
                    xsDataInputControlH5ToCBF = XSDataInputControlH5ToCBF()
                    xsDataInputControlH5ToCBF.hdf5File = XSDataFile(xsDataImage.path)
                    xsDataInputControlH5ToCBF.imageNumber = xsDataImage.number
                    edPluginControlH5ToCBF = self.loadPlugin(self.strPluginControlH5ToCBF, "ControlH5ToCBF_{0:01d}".format(pluginIndex))
                    edPluginControlH5ToCBF.dataInput = xsDataInputControlH5ToCBF
                    self.sendMessageToMXCuBE(f"Starting to convert {os.path.basename(xsDataImage.path.value)}, index = {pluginIndex}")
                    edPluginControlH5ToCBF.execute()
                    dictH5ToCBFPlugin[xsDataImage.path.value] = edPluginControlH5ToCBF
                    pluginIndex += 1
        for xsDataSetMXCuBE in xsDataInputMXCuBE.dataSet:
            for xsDataImage in xsDataSetMXCuBE.imageFile:
                if xsDataImage.path.value.endswith(".h5"):
                    edPluginControlH5ToCBF = dictH5ToCBFPlugin[xsDataImage.path.value]
                    edPluginControlH5ToCBF.synchronize()
                    cbfFile = edPluginControlH5ToCBF.dataOutput.outputCBFFile
                    self.sendMessageToMXCuBE(f"Image converted {os.path.basename(cbfFile.path.value)}")
                    xsDataInputInterface.addImagePath(XSDataImage(cbfFile.path))
                    if self.xsDataFirstImage is None:
                        strCbfFilePath = cbfFile.path.value
                        strH5FilePath = strCbfFilePath.replace(".cbf", ".h5")
                        self.xsDataFirstImage = XSDataImage(XSDataString(strH5FilePath))
                else:
                    xsDataInputInterface.addImagePath(xsDataImage)
                    if self.xsDataFirstImage is None:
                        self.xsDataFirstImage = xsDataImage

        xsDataExperimentalCondition = self.getFluxAndBeamSizeFromISPyB(self.xsDataFirstImage, \
                                                            xsDataInputMXCuBE.experimentalCondition)

        xsDataInputInterface.experimentalCondition = xsDataExperimentalCondition
        xsDataInputInterface.diffractionPlan = xsDataInputMXCuBE.diffractionPlan
        xsDataInputInterface.sample = xsDataInputMXCuBE.sample
        xsDataInputInterface.dataCollectionId = xsDataInputMXCuBE.dataCollectionId
        xsDataInputInterface.token = xsDataInputMXCuBE.token
        self.edPluginControlInterface.dataInput = xsDataInputInterface

        if not self.isFailure() and self.edPluginControlInterface is not None:
            self.connectProcess(self.edPluginControlInterface.executeSynchronous)
            self.edPluginControlInterface.connectSUCCESS(self.doSuccessActionInterface)
            self.edPluginControlInterface.connectFAILURE(self.doFailureActionInterface)


    def finallyProcess(self, _edPlugin=None):
        EDPluginControl.finallyProcess(self, _edPlugin)
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_4.finallyProcess...")
        self.createResultMXCubE()
        self.sendCharacterisationResultToMXCuBE(xml.sax.saxutils.escape(self.xsDataResultMXCuBE.marshal()))
        self.storeResultsInISPyB(self.strSubject, self.strMessage)
        self.setDataOutput(self.xsDataResultMXCuBE)


    def doSuccessActionInterface(self, _edPlugin=None):
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_4.doSuccessActionInterface...")
        self.retrieveSuccessMessages(self.edPluginControlInterface, "EDPluginControlInterfaceToMXCuBEv1_4.doSuccessActionInterface")
        # Send success email message (MXSUP-183):
        self.tStop = time.time()
        self.strSubject = "SUCCESS"
        self.strMessage = "Characterisation success!"

    def doFailureActionInterface(self, _edPlugin=None):
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_4.doFailureActionInterface...")
        # Send failure email message (MXSUP-183):
        self.tStop = time.time()
        self.strSubject = "FAILURE"
        self.strMessage = "Characterisation FAILURE!"


    def createResultMXCubE(self):
        xsDataResultCharacterisation = self.edPluginControlInterface.dataOutput.resultCharacterisation
        if self.bIsEigerDetector:
            xsDataResultCharacterisation = self.makeNumberOfImagesMultipleOf100(xsDataResultCharacterisation)
        self.xsDataResultMXCuBE.setCharacterisationResult(xsDataResultCharacterisation)
        xsDataResultControlISPyB = self.edPluginControlInterface.dataOutput.resultControlISPyB
        if xsDataResultControlISPyB != None:
            self.xsDataResultMXCuBE.screeningId = xsDataResultControlISPyB.screeningId
        if xsDataResultCharacterisation != None:
            self.xsDataResultMXCuBE.characterisationResult = xsDataResultCharacterisation
            strPathCharacterisationResult = os.path.join(self.getWorkingDirectory(), "CharacterisationResult.xml")
            xsDataResultCharacterisation.exportToFile(strPathCharacterisationResult)
            self.xsDataResultMXCuBE.setListOfOutputFiles(XSDataString(strPathCharacterisationResult))
            # For the moment, create "DNA" style output directory
            self.strPathToDNAFileDirectory = self.createDNAFileDirectoryPath(xsDataResultCharacterisation)
            xsDataDictionaryLogFile = None
            if (self.createDNAFileDirectory(self.strPathToDNAFileDirectory)):
                xsDataDictionaryLogFile = self.createOutputFileDictionary(xsDataResultCharacterisation, self.strPathToDNAFileDirectory)
            self.strPyArchPathToDNAFileDirectory = EDHandlerESRFPyarchv1_0.createPyarchFilePath(self.strPathToDNAFileDirectory)
            if (self.createDNAFileDirectory(self.strPyArchPathToDNAFileDirectory)):
                xsDataDictionaryLogFile = self.createOutputFileDictionary(xsDataResultCharacterisation, self.strPyArchPathToDNAFileDirectory)
            self.xsDataResultMXCuBE.setOutputFileDictionary(xsDataDictionaryLogFile)

    def storeResultsInISPyB(self, _strSubject, _strMessage):
        if self.xsDataResultMXCuBE.characterisationResult is not None:
            xsDataResultCharacterisation = self.xsDataResultMXCuBE.characterisationResult
            xsDataDictionaryLogFile = self.xsDataResultMXCuBE.outputFileDictionary
            strCharacterisationSuccess = None
            strSubject = _strSubject
            strMessage = _strMessage
            if xsDataResultCharacterisation.statusMessage:
                strMessage += "\n\n"
                strMessage += xsDataResultCharacterisation.statusMessage.value
            if xsDataResultCharacterisation.shortSummary:
                strMessage += "\n\n"
                strMessage += xsDataResultCharacterisation.shortSummary.value
            self.sendEmail(strSubject, strMessage)
            # Fix for bug EDNA-55 : If burning strategy EDNA2html shouldn't be run
            bRunExecOutputHTML = False
            xsDataInputMXCuBE = self.getDataInput()
            xsDataDiffractionPlan = xsDataInputMXCuBE.diffractionPlan
            if xsDataDiffractionPlan is not None and xsDataDiffractionPlan.strategyOption is not None:
                strStrategyOption = xsDataDiffractionPlan.strategyOption.value
                if strStrategyOption.find("-DamPar") != -1:
                    bRunExecOutputHTML = False
            if (self.edPluginExecOutputHTML is not None) and bRunExecOutputHTML:
                self.edPluginExecOutputHTML.setDataInput(XSDataFile(XSDataString(self.strPathToDNAFileDirectory)), "dnaFileDirectory")
                self.edPluginExecOutputHTML.execute()
            # Fix for bug MXSUP-251: Put the BEST .par file in the EDNA characterisation root directory
            xsDataIntegrationResult = xsDataResultCharacterisation.integrationResult
            if xsDataIntegrationResult:
                listXSDataIntegrationSubWedgeResult = xsDataIntegrationResult.integrationSubWedgeResult
                for xsDataIntegrationSubWedgeResult in listXSDataIntegrationSubWedgeResult:
                    if xsDataIntegrationSubWedgeResult.bestfilePar is not None:
                        strBestfilePar = xsDataIntegrationSubWedgeResult.bestfilePar.value
                        # Put the file one directory above the mxCuBE v1.3 plugin working directory:
                        strDir = os.path.dirname(self.getWorkingDirectory())
                        strPath = os.path.join(strDir, "bestfile.par")
                        EDUtilsFile.writeFile(strPath, strBestfilePar)
                        break
            # Execute plugin which creates a simple HTML page
            self.executeSimpleHTML(xsDataResultCharacterisation)
            # Upload the best wilson plot path to ISPyB
            strWorkflowStepImage = None
            strPyarchWorkflowStepImage = None
            strBestWilsonPlotPath = EDHandlerXSDataISPyBv1_4.getBestWilsonPlotPath(xsDataResultCharacterisation)
            if self.strPyArchPathToDNAFileDirectory is not None:
                if strBestWilsonPlotPath is not None:
                    strCharacterisationSuccess = "Success"
                    # Copy wilson path to Pyarch
                    strWorkflowStepImage = strBestWilsonPlotPath
                    strPyarchWorkflowStepImage = os.path.join(self.strPyArchPathToDNAFileDirectory, os.path.basename(strBestWilsonPlotPath))
                else:
                    strCharacterisationSuccess = "Failure"
                    # Copy first thumbnail image
                    if len(xsDataResultCharacterisation.thumbnailImage) > 1:
                        strThumbnailImage = xsDataResultCharacterisation.thumbnailImage[0].path.value
                        if os.path.exists(strThumbnailImage):
                            strWorkflowStepImage = strThumbnailImage
                            strPyarchWorkflowStepImage = os.path.join(self.strPyArchPathToDNAFileDirectory, os.path.basename(strWorkflowStepImage))
            if strPyarchWorkflowStepImage is not None:
                if not os.path.exists(strPyarchWorkflowStepImage):
                    if not os.path.exists(os.path.dirname(strPyarchWorkflowStepImage)):
                        os.makedirs(os.path.dirname(strPyarchWorkflowStepImage), 755)
                    EDUtilsPath.systemCopyFile(strWorkflowStepImage, strPyarchWorkflowStepImage)
                    os.chmod(strPyarchWorkflowStepImage, 0o644)
                self.DEBUG("Workflow step image pyarch path: %s " % strPyarchWorkflowStepImage)
                if self.edPluginControlInterface.dataOutput.resultControlISPyB is not None:
                    xsDataInputISPyBSetBestWilsonPlotPath = XSDataInputISPyBSetBestWilsonPlotPath()
                    if self.edPluginISPyBRetrieveDataCollection is not None:
                        if self.edPluginISPyBRetrieveDataCollection.dataOutput is not None:
                            dataCollectionId = self.edPluginISPyBRetrieveDataCollection.dataOutput.dataCollection.dataCollectionId
                            xsDataInputISPyBSetBestWilsonPlotPath.dataCollectionId = XSDataInteger(dataCollectionId)
                            xsDataInputISPyBSetBestWilsonPlotPath.bestWilsonPlotPath = XSDataString(strPyarchWorkflowStepImage)
                            edPluginSetBestWilsonPlotPath = self.loadPlugin("EDPluginISPyBSetBestWilsonPlotPathv1_4", "ISPyBSetBestWilsonPlotPath")
                            edPluginSetBestWilsonPlotPath.dataInput = xsDataInputISPyBSetBestWilsonPlotPath
                            edPluginSetBestWilsonPlotPath.executeSynchronous()
            # Only for the ESRF:
            if EDUtilsPath.isESRF() or EDUtilsPath.isEMBL():
                # For EXI: create workflow entry with one workflow step
                self.edPluginStoreWorkflow = self.loadPlugin(self.strPluginStoreWorkflow)
                self.edPluginStoreWorkflowStep = self.loadPlugin(self.strPluginStoreWorkflowStep)
                self.edPluginUpdateDataCollectionGroupWorkflowId = self.loadPlugin(self.strUpdateDataCollectionGroupWorkflowId)
                xsDataISPyBWorkflow = XSDataISPyBWorkflow()
                xsDataISPyBWorkflow.workflowType = XSDataString("Characterisation")
                xsDataISPyBWorkflow.workflowTitle = XSDataString("Characterisation")
                # Try to get the path tp the executeive log file from xsDataDictionaryLogFile
                for xsDataKeyValuePair in xsDataDictionaryLogFile.keyValuePair:
                    if xsDataKeyValuePair.key.value == "executiveSummary":
                        xsDataISPyBWorkflow.logFilePath = xsDataKeyValuePair.value
                xsDataISPyBWorkflow.status = XSDataString("Success")
                xsDataInputISPyBStoreWorkflow = XSDataInputISPyBStoreWorkflow()
                xsDataInputISPyBStoreWorkflow.workflow = xsDataISPyBWorkflow
                self.edPluginStoreWorkflow.dataInput = xsDataInputISPyBStoreWorkflow
                self.edPluginStoreWorkflow.executeSynchronous()
                if self.edPluginStoreWorkflow.dataOutput is not None and self.edPluginStoreWorkflow.dataOutput.workflowId is not None:
                    workflowId = self.edPluginStoreWorkflow.dataOutput.workflowId.value
                    # Update data collection group
                    xsDataInputISPyBUpdateDataCollectionGroupWorkflowId = XSDataInputISPyBUpdateDataCollectionGroupWorkflowId()
                    xsDataInputISPyBUpdateDataCollectionGroupWorkflowId.workflowId = XSDataInteger(workflowId)
                    xsDataInputISPyBUpdateDataCollectionGroupWorkflowId.fileLocation = XSDataString(os.path.dirname(self.xsDataFirstImage.path.value))
                    xsDataInputISPyBUpdateDataCollectionGroupWorkflowId.fileName = XSDataString(os.path.basename(self.xsDataFirstImage.path.value))
                    self.edPluginUpdateDataCollectionGroupWorkflowId.dataInput = xsDataInputISPyBUpdateDataCollectionGroupWorkflowId
                    self.edPluginUpdateDataCollectionGroupWorkflowId.executeSynchronous()
                    xsDataInputISPyBStoreWorkflowStep = XSDataInputISPyBStoreWorkflowStep()
                    xsDataInputISPyBStoreWorkflowStep.workflowId = XSDataInteger(workflowId)
                    xsDataInputISPyBStoreWorkflowStep.workflowStepType = XSDataString("Characterisation")
                    xsDataInputISPyBStoreWorkflowStep.status = XSDataString(strCharacterisationSuccess)
                    if strPyarchWorkflowStepImage is not None:
                        xsDataInputISPyBStoreWorkflowStep.imageResultFilePath = XSDataString(strPyarchWorkflowStepImage)
                    if self.strPyArchPathToDNAFileDirectory is not None:
                        xsDataInputISPyBStoreWorkflowStep.htmlResultFilePath = XSDataString(os.path.join(self.strPyArchPathToDNAFileDirectory, "Characterisation", "index.html"))
                    if self.edPluginExecSimpleHTML.dataOutput is not None:
                         strResultFilePath = self.edPluginExecSimpleHTML.dataOutput.pathToJsonFile.path.value
                         # strPyarchResultFilePath = EDHandlerESRFPyarchv1_0.createPyarchFilePath(strResultFilePath)
                         xsDataInputISPyBStoreWorkflowStep.resultFilePath = XSDataString(strResultFilePath)
                    self.edPluginStoreWorkflowStep.dataInput = xsDataInputISPyBStoreWorkflowStep
                    self.edPluginStoreWorkflowStep.executeSynchronous()
                    # Upload also to ICAT
                    first_image_path = self.xsDataFirstImage.path.value
                    beamline, proposal = EDUtilsPath.getBeamlineProposal(first_image_path)
                    EDUtilsICAT.storeWorkflowStep(
                        beamline=beamline,
                        proposal=proposal,
                        directory=os.path.dirname(first_image_path),
                        workflowStepType="characterisation",
                        workflow_name=None,
                        workflow_type=None,
                        request_id=None,
                        snap_shot_path=strPyarchWorkflowStepImage,
                        json_path=strResultFilePath,
                        icat_sub_dir="icat",
                    )



    def doSuccessActionISPyB(self, _edPlugin):
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_4.doSuccessActionISPyB...")
        self.retrieveSuccessMessages(self.edPluginControlISPyB, "EDPluginControlInterfaceToMXCuBEv1_4.doSuccessActionISPyB")


    def doFailureActionISPyB(self, _edPlugin=None):
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_4.doFailureActionISpyB...")
        self.retrieveFailureMessages(self.edPluginControlISPyB, "EDPluginControlInterfaceToMXCuBEv1_4.doFailureActionISpyB")
        # Send failure email message (MXSUP-183):
        self.strSubject = "%s : FAILURE!" % EDUtilsPath.getEdnaSite()
        self.strMessage = "ISPyB FAILURE!"
        self.sendEmail(self.strSubject, self.strMessage)


    def createDNAFileDirectoryPath(self, _xsDataResultCharacterisation):
        """
        This method creates a "DNA" style directory path, i.e. in the same directory were the 
        images are located a new directory is created with the following convention:
        
          dnafiles_prefix_runNumber
        
        The path to this directory is returned if the directory was successfully created.
        """
        # First extract all reference image directory paths and names
        xsDataCollection = _xsDataResultCharacterisation.dataCollection
        listImageDirectoryPath = []
        listImagePrefix = []
        for xsDataSubWedge in xsDataCollection.subWedge:
            for xsDataImage in xsDataSubWedge.image:
                strImagePath = xsDataImage.path.value
                listImageDirectoryPath.append(os.path.dirname(strImagePath))
                listImagePrefix.append(EDUtilsImage.getPrefix(strImagePath))
        # TODO: Check that all paths and prefixes are the same
        strImageDirectory = listImageDirectoryPath[0]
        strPrefix = listImagePrefix[0]
        # Remove any "ref-" or "postref-" from the prefix in order to make it fully
        # compatitble with DNA standards:
        if (strPrefix is not None):
            if (strPrefix.startswith("ref-")):
                strPrefix = strPrefix[4:]
            elif (strPrefix.startswith("postref-")):
                strPrefix = strPrefix[8:]
        strDNAFileDirectoryPath = os.path.join(strImageDirectory, "%s_dnafiles" % strPrefix)
        return strDNAFileDirectoryPath





    def createDNAFileDirectory(self, _strDNAFileDirectoryPath):
        """
        Create a "DNA-files" directory - if possible.
        """
        bSuccess = False
        if (_strDNAFileDirectoryPath is not None):
            if (os.path.exists(_strDNAFileDirectoryPath)):
                self.warning("Removing existing DNA files directory: %s" % _strDNAFileDirectoryPath)
                if (os.access(_strDNAFileDirectoryPath, os.W_OK)):
                    EDUtilsPath.systemRmTree(_strDNAFileDirectoryPath)
                else:
                    self.warning("Cannot remove existing DNA files directory!")
            if (_strDNAFileDirectoryPath is not None):
                # Check if directory one level up is writeable
                strDNAFileBaseDirectory = os.path.split(_strDNAFileDirectoryPath)[0]
                if (os.access(strDNAFileBaseDirectory, os.W_OK)):
                    self.DEBUG("Creating DNA files directory: %s" % _strDNAFileDirectoryPath)
                    os.makedirs(_strDNAFileDirectoryPath, mode=0o755)
                    bSuccess = True
                else:
                    self.warning("Cannot create DNA files directory: %s" % _strDNAFileDirectoryPath)
        return bSuccess



    def splitHeadDirectory(self, _strPath):
        """
        This method works like os.path.split except that it splits the head directory
        from the rest of the path. Example:
        "/" -> [ None, None]
        "/data" -> ["data", None]
        "/data/visitor" -> ["data", "visitor"]
        "/data/visitor/mx415/id14eh2/20100212" -> ["data", "visitor/mx415/id14eh2/20100212"]
        """
        listOfDirectories = _strPath.split(os.sep)
        strTail = None
        strHead = None
        if (len(listOfDirectories) > 1):
            strHead = listOfDirectories[1]
            if (strHead == ""):
                strHead = None
            if (len(listOfDirectories) > 1):
                for strEntry in listOfDirectories[2:]:
                    if (strTail is None):
                        strTail = strEntry
                    else:
                        strTail = os.path.join(strTail, strEntry)
        return [ strHead, strTail ]


    def createOutputFileDictionary(self, _xsDataResultCharacterisation, _strPathToLogFileDirectory=None):
        """
        This method creates an XSDataDictionary containing the name and locations of the 
        characterisation output files.
        """
        xsDataDictionaryLogFile = XSDataDictionary()
        # Start with the prediction images
        xsDataIndexingResult = _xsDataResultCharacterisation.indexingResult
        if xsDataIndexingResult is not None:
            xsDataGeneratePredictionResult = xsDataIndexingResult.predictionResult
            if xsDataGeneratePredictionResult is not None:
                listXSDataImagePrediction = xsDataGeneratePredictionResult.predictionImage
                for xsDataImagePrediction in listXSDataImagePrediction:
                    xsDataKeyValuePair = XSDataKeyValuePair()
                    iPredictionImageNumber = xsDataImagePrediction.number.value
                    xsDataStringKey = XSDataString("predictionImage_%d" % iPredictionImageNumber)
                    xsDataStringValue = None
                    strPredictionImagePath = xsDataImagePrediction.path.value
                    if (_strPathToLogFileDirectory is not None):
                        strPredictionImageFileName = EDUtilsFile.getBaseName(strPredictionImagePath)
                        strNewPredictionImagePath = os.path.join(_strPathToLogFileDirectory, strPredictionImageFileName)
                        EDUtilsFile.copyFile(strPredictionImagePath, strNewPredictionImagePath)
                        xsDataStringValue = XSDataString(strNewPredictionImagePath)
                    else:
                        xsDataStringValue = XSDataString(strPredictionImageFileName)
                    xsDataKeyValuePair.setKey(xsDataStringKey)
                    xsDataKeyValuePair.setValue(xsDataStringValue)
                    xsDataDictionaryLogFile.addKeyValuePair(xsDataKeyValuePair)
        # Best log file
        strPathToBESTLogFile = None
        strPathToFBESTLogFile = None
        strPathToExecutiveSummary = self.getLogFileName()
        if _xsDataResultCharacterisation.strategyResult is not None:
            if _xsDataResultCharacterisation.strategyResult.bestLogFile is not None:
                strPathToBESTLogFile = _xsDataResultCharacterisation.strategyResult.bestLogFile.path.value
            if strPathToBESTLogFile is not None:
                xsDataStringKey = XSDataString("logFileBest")
                xsDataStringValue = None
                if (_strPathToLogFileDirectory is not None):
                    strNewBestLogPath = os.path.join(_strPathToLogFileDirectory, "best.log")
                    EDUtilsFile.copyFile(strPathToBESTLogFile, strNewBestLogPath)
                    xsDataStringValue = XSDataString(strNewBestLogPath)
                else:
                    xsDataStringValue = XSDataString(strPathToBESTLogFile)
                xsDataKeyValuePair = XSDataKeyValuePair()
                xsDataKeyValuePair.setKey(xsDataStringKey)
                xsDataKeyValuePair.setValue(xsDataStringValue)
                xsDataDictionaryLogFile.addKeyValuePair(xsDataKeyValuePair)
            if _xsDataResultCharacterisation.strategyResult.fbestLogFile is not None:
                strPathToFBESTLogFile = _xsDataResultCharacterisation.strategyResult.fbestLogFile.path.value
            if strPathToFBESTLogFile is not None:
                xsDataStringKey = XSDataString("logFileFBest")
                xsDataStringValue = None
                if (_strPathToLogFileDirectory is not None):
                    strNewFBestLogPath = os.path.join(_strPathToLogFileDirectory, "fbest.log")
                    EDUtilsFile.copyFile(strPathToFBESTLogFile, strNewFBestLogPath)
                    xsDataStringValue = XSDataString(strNewFBestLogPath)
                else:
                    xsDataStringValue = XSDataString(strPathToFBESTLogFile)
                xsDataKeyValuePair = XSDataKeyValuePair()
                xsDataKeyValuePair.setKey(xsDataStringKey)
                xsDataKeyValuePair.setValue(xsDataStringValue)
                xsDataDictionaryLogFile.addKeyValuePair(xsDataKeyValuePair)
            if (strPathToExecutiveSummary is not None):
                xsDataStringKey = XSDataString("executiveSummary")
                xsDataStringValue = None
                if (_strPathToLogFileDirectory is not None):
                    strExecutiveSummaryFileName = EDUtilsFile.getBaseName(strPathToExecutiveSummary)
                    strNewExecutiveSummaryPath = os.path.join(_strPathToLogFileDirectory, strExecutiveSummaryFileName)
                    EDUtilsFile.copyFile(strPathToExecutiveSummary, strNewExecutiveSummaryPath)
                    xsDataStringValue = XSDataString(strNewExecutiveSummaryPath)
                    # Copy also the executive summary file to "dna_log.txt"...
                    strNewExecutiveSummaryPath = os.path.join(_strPathToLogFileDirectory, "dna_log.txt")
                    EDUtilsFile.copyFile(strPathToExecutiveSummary, strNewExecutiveSummaryPath)
                else:
                    xsDataStringValue = XSDataString(strPathToExecutiveSummary)
                xsDataKeyValuePair = XSDataKeyValuePair()
                xsDataKeyValuePair.setKey(xsDataStringKey)
                xsDataKeyValuePair.setValue(xsDataStringValue)
                xsDataDictionaryLogFile.addKeyValuePair(xsDataKeyValuePair)

        return xsDataDictionaryLogFile





    def doFailureActionCharacterisation(self, _edPlugin=None):
        """
        retrieve the potential warning messages
        retrieve the potential error messages
        """
        self.DEBUG("EDPluginControlInterfacev1_4.doFailureActionCharacterisation")
        self.setFailure()
        # Send failure email message (MXSUP-183):
        self.strSubject = "%s : FAILURE!" % EDUtilsPath.getEdnaSite()
        self.strMessage = "Characterisation FAILURE!"
        self.sendEmail(self.strSubject, self.strMessage)


    def getFluxAndBeamSizeFromISPyB(self, _xsDataFirstImage, _xsDataExperimentalCondition):
        """
        This method retrieves the flux and beamsize from ISPyB
        """
        fFlux = None
        xsDataExperimentalCondition = None
        if (_xsDataExperimentalCondition is not None):
            if _xsDataExperimentalCondition.beam is not None:
                if _xsDataExperimentalCondition.beam.flux is not None:
                    fFlux = _xsDataExperimentalCondition.beam.flux.value
                    self.screen("MXCuBE reports flux to be: %g photons/sec" % fFlux)
            xsDataExperimentalCondition = _xsDataExperimentalCondition.copy()
            xsDataInputRetrieveDataCollection = XSDataInputRetrieveDataCollection()
            xsDataInputRetrieveDataCollection.setImage(XSDataImage(_xsDataFirstImage.path))
            self.edPluginISPyBRetrieveDataCollection.setDataInput(xsDataInputRetrieveDataCollection)
            self.edPluginISPyBRetrieveDataCollection.executeSynchronous()
            xsDataResultRetrieveDataCollection = self.edPluginISPyBRetrieveDataCollection.dataOutput
            if xsDataResultRetrieveDataCollection is not None:
                xsDataISPyBDataCollection = xsDataResultRetrieveDataCollection.dataCollection
                if xsDataISPyBDataCollection is not None:
                    if fFlux is None:
                        fFlux = xsDataISPyBDataCollection.flux_end
                        self.screen("ISPyB reports flux to be: %g photons/sec" % fFlux)
                    fBeamSizeAtSampleX = xsDataISPyBDataCollection.beamSizeAtSampleX
                    fBeamSizeAtSampleY = xsDataISPyBDataCollection.beamSizeAtSampleY
                    if fBeamSizeAtSampleX is not None and fBeamSizeAtSampleY is not None:
                        self.screen("ISPyB reports beamsize X to be: %.3f mm" % fBeamSizeAtSampleX)
                        self.screen("ISPyB reports beamsize Y to be: %.3f mm" % fBeamSizeAtSampleY)
                        xsDataSize = XSDataSize()
                        xsDataSize.x = XSDataLength(fBeamSizeAtSampleX)
                        xsDataSize.y = XSDataLength(fBeamSizeAtSampleY)
                        xsDataExperimentalCondition.beam.size = xsDataSize
                    # Get transmission if it's not already there
                    if xsDataExperimentalCondition.beam.transmission is None:
                        fTransmission = xsDataISPyBDataCollection.transmission
                        xsDataExperimentalCondition.beam.transmission = XSDataDouble(fTransmission)
            if fFlux is not None and fFlux > self.fFluxThreshold:
                xsDataExperimentalCondition.beam.flux = XSDataFlux(fFlux)
            else:
                # Force flux to 0.0
                self.screen("No flux could be obtained from neither mxCuBE nor from ISPyB, forcing flux to 0.0 photon/s")
                xsDataExperimentalCondition.beam.flux = XSDataFlux(0.0)

        return xsDataExperimentalCondition






    def updateDataInputCharacterisation(self, _xsDataInputCharacterisation):
        """
        This method updates the xsDataInputCharacterisation object given as argument with the following
        parameters (if available) goven as input:
        - Diffraction plan
        - Beam size
        - Beam flux
        - Min exposure time per image
        - Max oscillation speed
        - Min oscillation width
        - Sample information
        """
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_4.createDataInputCharacterisationFromDataSets")
        xsDataCollection = _xsDataInputCharacterisation.dataCollection
        if (_xsDataInputCharacterisation is not None):
            xsDataInputCCP4i = self.getDataInput()
            # Update with diffraction plan
            xsDiffactionPlan = xsDataInputCCP4i.diffractionPlan
            if(xsDiffactionPlan is not None):
                xsDataCollection.setDiffractionPlan(xsDiffactionPlan)
            # Update the data collection subwedges with additional experimental conditions
            for xsDataSubWedge in xsDataCollection.subWedge:
                xsDataExperimentalCondition = xsDataInputCCP4i.experimentalCondition
                if(xsDataExperimentalCondition is not None):
                    xsDataBeam = xsDataExperimentalCondition.beam
                    if(xsDataBeam is not None):
                        xsDataBeamSize = xsDataBeam.size
                        if(xsDataBeamSize is not None):
                            xsDataSubWedge.experimentalCondition.beam.size = xsDataBeamSize
                        xsDataBeamFlux = xsDataBeam.flux
                        if(xsDataBeamFlux is not None):
                            xsDataSubWedge.experimentalCondition.beam.flux = xsDataBeamFlux
                        xsDataMinExposureTime = xsDataBeam.minExposureTimePerImage
                        if(xsDataMinExposureTime is not None):
                            xsDataSubWedge.experimentalCondition.beam.minExposureTimePerImage = xsDataMinExposureTime
                    xsDataGoniostat = xsDataExperimentalCondition.goniostat
                    if(xsDataGoniostat is not None):
                        xsDataMaxOscSpeed = xsDataGoniostat.maxOscillationSpeed
                        if(xsDataMaxOscSpeed is not None):
                            xsDataSubWedge.experimentalCondition.goniostat.maxOscillationSpeed = xsDataMaxOscSpeed
                        xsDataMinOscWidth = xsDataGoniostat.minOscillationWidth
                        if(xsDataMinOscWidth is not None):
                            xsDataSubWedge.experimentalCondition.goniostat.minOscillationWidth = xsDataMinOscWidth
            # Update with the sample
            xsDataSample = xsDataInputCCP4i.sample
            if(xsDataSample is not None):
                xsDataCollection.setSample(xsDataSample)

    def getBeamlineProposalFromPath(self, _strPathToImage):
        """ESRF specific code for extracting the beamline name and prefix from the path"""
        listPath = _strPathToImage.split("/")
        strPrefix = EDUtilsImage.getPrefix(_strPathToImage).replace("ref-", "")
        if listPath[2] == "visitor":
            strBeamline = listPath[4]
            strProposal = listPath[3]
        elif listPath[3] == "inhouse":
            strBeamline = listPath[2]
            strProposal = listPath[4]
        else:
            strBeamline = "nobeamline"
            strProposal = "noproposal"
        return (strBeamline, strProposal, strPrefix)

    def sendEmail(self, _strSubject, _strMessage):
        """Sends an email to the EDNA contact person (if configured)."""
        strTime = "%.1f s" % (self.tStop - self.tStart)
        if EDUtilsPath.isESRF():
            strPathImage = None
            for dataSet in self.dataInput.dataSet:
                for imageFile in dataSet.imageFile:
                    strPathImage = imageFile.path.value
                    break
            if strPathImage is not None:
                (strBeamline, strProposal, strPrefix) = self.getBeamlineProposalFromPath(strPathImage)
            else:
                strBeamline = "Unknown"
                strProposal = "Unknown"
                strPrefix = "Unknown"
            strHost = socket.gethostname()
            strSubject = "EDNA ch %s %s %s %s %s (%s)" % (_strSubject, strBeamline, strProposal, strPrefix, strHost, strTime)
        else:
            strSubject = "EDNA %s : %s (%s)" % (_strSubject, EDUtilsPath.getEdnaSite(), strTime)
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_4.sendEmail: Subject = %s" % strSubject)
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_4.sendEmail: Message:")
        self.DEBUG(_strMessage)
        if self.strEDNAContactEmail == None:
            self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_4.sendEmail: No email address configured!")
        elif not EDUtilsPath.getEdnaSite().startswith("ESRF"):
            self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_4.sendEmail: Not executed at the ESRF! EDNA_SITE=%s" % EDUtilsPath.getEdnaSite())
        else:
            try:
                self.DEBUG("Sending message to %s." % self.strEDNAContactEmail)
                self.DEBUG("Message: %s" % _strMessage)
                strMessage = "EDNA_HOME = %s\n" % EDUtilsPath.getEdnaHome()
                strMessage += "EDNA_SITE = %s\n" % EDUtilsPath.getEdnaSite()
                strMessage += "PLUGIN_NAME = %s\n" % self.getPluginName()
                strMessage += "working_dir = %s\n\n" % self.getWorkingDirectory()
                strMessage += "Reference images:\n"
                xsDataInputMXCuBE = self.getDataInput()
                for xsDataSetMXCuBE in xsDataInputMXCuBE.getDataSet():
                    for xsDataFile in xsDataSetMXCuBE.getImageFile():
                        strMessage += "%s\n" % xsDataFile.path.value
                strMessage += "\n"
                strMessage += _strMessage
                strEmailMsg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" % (self.strEDNAEmailSender, \
                                                                                self.strEDNAContactEmail, \
                                                                                strSubject, strMessage))
                server = smtplib.SMTP("localhost")
                server.sendmail(self.strEDNAEmailSender, self.strEDNAContactEmail, strEmailMsg)
                server.quit()
            except:
                self.ERROR("Error when sending email message!")
                self.writeErrorTrace()


    def executeSimpleHTML(self, _xsDataResultCharacterisation):
        xsDataInputSimpleHTMLPage = XSDataInputSimpleHTMLPage()
        xsDataInputSimpleHTMLPage.setCharacterisationResult(_xsDataResultCharacterisation)
        self.edPluginExecSimpleHTML.setDataInput(xsDataInputSimpleHTMLPage)
        self.edPluginExecSimpleHTML.connectSUCCESS(self.doSuccessSimpleHTML)
        self.edPluginExecSimpleHTML.connectFAILURE(self.doFailureSimpleHTML)
        self.executePluginSynchronous(self.edPluginExecSimpleHTML)


    def doSuccessSimpleHTML(self, _edPlugin=None):
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_4.doSuccessSimpleHTML...")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlInterfaceToMXCuBEv1_4.doSuccessSimpleHTML")
        # Copy files from working directory
        if self.dataInput.htmlDir is None:
            self.xsDataResultMXCuBE.setHtmlPage(_edPlugin.dataOutput.pathToHTMLFile)
        else:
            htmlDir = self.dataInput.htmlDir.path.value
            if os.path.exists(htmlDir):
                # Potentially unsafe but very unlikely that this will cause problems
                htmlDir = tempfile.mktemp(prefix=os.path.basename(htmlDir),
                                          dir=os.path.dirname(htmlDir))
            EDUtilsPath.systemCopyTree(os.path.dirname(_edPlugin.dataOutput.pathToHTMLFile.path.value), htmlDir)
            htmlPage = os.path.join(htmlDir, os.path.basename(_edPlugin.dataOutput.pathToHTMLFile.path.value))
            self.xsDataResultMXCuBE.setHtmlPage(XSDataFile(XSDataString(htmlPage)))


    def doFailureSimpleHTML(self, _edPlugin=None):
        self.DEBUG("EDPluginControlInterfaceToMXCuBEv1_4.doFailureSimpleHTML...")


    def makeNumberOfImagesMultipleOf100(self, _xsDataResultCharacterisation):
        xsDataResultCharacterisation = _xsDataResultCharacterisation.copy()
        strategyResult = xsDataResultCharacterisation.strategyResult
        if strategyResult is not None:
            for collectionPlan in strategyResult.collectionPlan:
                for subWedge in collectionPlan.collectionStrategy.subWedge:
                    rotationAxisStart = subWedge.experimentalCondition.goniostat.rotationAxisStart.value
                    rotationAxisEnd = subWedge.experimentalCondition.goniostat.rotationAxisEnd.value
                    oscillationWidth = subWedge.experimentalCondition.goniostat.oscillationWidth.value
                    noImages = int((rotationAxisEnd - rotationAxisStart) / oscillationWidth)
                    self.screen("Strategy: number of images for subWedge #{0}: {1}".format(subWedge.subWedgeNumber.value, noImages))

        return xsDataResultCharacterisation


    def sendMessageToMXCuBE(self, _strMessage, level="info"):
        if self.serverProxy is not None:
            self.DEBUG("Sending message to mxCuBE: {0}, level {1}".format(_strMessage, level))
            try:
                for strMessage in _strMessage.split("\n"):
                    if strMessage != "":
                        self.screen(strMessage)
                        self.serverProxy.log_message("Characterisation: " + strMessage, level)
            except Exception as e:
                self.screen(e)
                self.DEBUG("Sending message to mxCuBE failed!")

    def sendCharacterisationResultToMXCuBE(self, _strXML):
        if self.serverProxy is not None:
            try:
                self.serverProxy.setCharacterisationResult(_strXML)
            except Exception as e:
                self.screen(e)
                self.ERROR("Sending characterisation results to mxCuBE failed!")
