#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
#                            Grenoble, France
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

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
import sys

sys.path.insert(0, "/opt/pxsoft/bes/vgit/linux-x86_64/id30a2/edna2")

try:
    from edna2.tasks.DiffractionThumbnail import DiffractionThumbnail
    EDNA2_THUMBNAILS = True
except:
    EDNA2_THUMBNAILS = False


try:
    from xmlrpclib import ServerProxy
    from xmlrpclib import Transport
except:
    from xmlrpc.client import ServerProxy
    from xmlrpc.client import Transport

from EDVerbose import EDVerbose
from EDPluginControl import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataTime

from XSDataMXv1 import XSDataCollection
from XSDataMXv1 import XSDataCrystal
from XSDataMXv1 import XSDataSpaceGroup
from XSDataMXv1 import XSDataIndexingInput
from XSDataMXv1 import XSDataInputCharacterisation
from XSDataMXv1 import XSDataResultCharacterisation
from XSDataMXv1 import XSDataGeneratePredictionInput
from XSDataMXv1 import XSDataIndexingSolutionSelected
from XSDataMXv1 import XSDataIntegrationInput
from XSDataMXv1 import XSDataInputStrategy
from XSDataMXv1 import XSDataInputControlXDSGenerateBackgroundImage
from XSDataMXv1 import XSDataIndexingInput
from XSDataMXv1 import XSDataInputControlKappa
from XSDataMXv1 import XSDataResultStrategy
from XSDataMXv1 import XSDataCollectionPlan
from XSDataMXv1 import XSDataCollection
from XSDataMXv1 import XSDataSubWedge
from XSDataMXv1 import XSDataExperimentalCondition
from XSDataMXv1 import XSDataGoniostat
from XSDataMXv1 import XSDataBeam
from XSDataMXv1 import XSDataStrategySummary

EDFactoryPluginStatic.loadModule("XSDataFbestv1_0")
from XSDataFbestv1_0 import XSDataInputFbest

EDFactoryPluginStatic.loadModule("XSDataMXThumbnailv1_1")
from XSDataMXThumbnailv1_1 import XSDataInputMXThumbnail

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


class EDPluginControlCharacterisationv1_5(EDPluginControl):
    """
    [To be replaced with a description of EDPluginControlTemplatev10]
    """
    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputCharacterisation)
        self._strPluginControlIndexingIndicators = "EDPluginControlIndexingIndicatorsv1_1"
        self._strPluginExecEvaluationIndexing = "EDPluginExecEvaluationIndexingv10"
        self._strPluginControlIndexingMOSFLM = "EDPluginControlIndexingMOSFLMv10"
        self._strPluginControlGeneratePrediction = "EDPluginControlGeneratePredictionv10"
        self._strPluginControlIntegration = "EDPluginControlIntegrationv10"
        self._strPluginControlXDSGenerateBackgroundImage = "EDPluginControlXDSGenerateBackgroundImagev1_0"
        self._strPluginControlStrategy = "EDPluginControlStrategyv1_2"
        self._strPluginGenerateThumbnailName = "EDPluginMXThumbnailv1_1"
        self._strPluginControlKappaName = "EDPluginControlKappav1_0"
        self._strPluginExecFbestName = "EDPluginFbestv1_0"
        self._listPluginGenerateThumbnail = []
        self._edPluginControlIndexingIndicators = None
        self._edPluginExecEvaluationIndexingMOSFLM = None
        self._edPluginExecEvaluationIndexingLABELIT = None
        self._edPluginControlGeneratePrediction = None
        self._edPluginControlIntegration = None
        self._edPluginControlXDSGenerateBackgroundImage = None
        self._edPluginControlStrategy = None
        self._edPluginControlKappa = None
        self._xsDataCollection = None
        self._xsDataResultCharacterisation = None
        self._xsDataIndexingResultMOSFLM = None
        self._xsDataCrystal = None
        self._strCharacterisationShortSummary = ""
        self._strStatusMessage = ""
        self._xsDataFileXdsBackgroundImage = None
        self._bDoStrategyCalculation = True
        self._fMinTransmission = 10  # %
        self._iNoReferenceImages = None
        self._iNoImagesWithDozorScore = None
        self._fMinDozorScore = None
        self._fAverageDozorScore = None
        self._strMxCuBE_URI = None
        self._oServerProxy = None
        self._runKappa = False
        self._bDoOnlyMoslmfIndexing = False
        self._fThresholdMosflmIndexing = None
        self._fVMaxVisibleResolution = None
        self._fCurrentResolution = None
        self._strStrategyType = None
        self._bDoOnlyFbest = False
        self._bMoslmWithoutThreshold = True

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlCharacterisationv1_5.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDataCollection(), "dataCollection")
        self.checkMandatoryParameters(self.getDataInput().getDataCollection().getDiffractionPlan(), "diffractionPlan")

    def configure(self):
        """
        Gets the configuration parameters (if any).
        """
        EDPluginControl.configure(self)
        self.DEBUG("EDPluginControlCharacterisationv1_5.configure")
        self._strMxCuBE_URI = self.config.get("mxCuBE_URI", None)
        # if self._strMxCuBE_URI is not None and "mxCuBE_XMLRPC_log" in os.environ.keys():
        #    self.DEBUG("Enabling sending messages to mxCuBE via URI {0}".format(self._strMxCuBE_URI))
        #    self._oServerProxy = xmlrpclib.ServerProxy(self._strMxCuBE_URI)
        self._runKappa = self.config.get("runKappa", False)
        self._fMinTransmission = self.config.get("minTransmissionWarning", self._fMinTransmission)
        self._bDoOnlyMoslmfIndexing = self.config.get("doOnlyMosflmIndexing", False)
        self._fThresholdMosflmIndexing = float(self.config.get("thresholdMosflmIndexing", 10.0))
        self._strStrategyType = self.config.get("strategyType", None)


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlCharacterisationv1_5.preProcess")
        xsDataInputCharacterisation = self.getDataInput()
        if xsDataInputCharacterisation.token is not None:
            strToken = xsDataInputCharacterisation.token.value
        else:
            strToken = None

        if xsDataInputCharacterisation.currentResolution is not None:
            self._fCurrentResolution = xsDataInputCharacterisation.currentResolution.value
        else:
            self._fCurrentResolution = None

        if self._strMxCuBE_URI is not None:
            self.DEBUG("Enabling sending messages to mxCuBE via URI {0}".format(self._strMxCuBE_URI))
            if strToken is None:
                self._oServerProxy = ServerProxy(self._strMxCuBE_URI)
            else:
                self._oServerProxy = ServerProxy(self._strMxCuBE_URI, transport=TokenTransport(strToken))
        self._xsDataResultCharacterisation = XSDataResultCharacterisation()
        # Load the plugins
        self._edPluginControlIndexingIndicators = self.loadPlugin(self._strPluginControlIndexingIndicators, \
                                                                   "Indexing")
        self._edPluginExecEvaluationIndexingLABELIT = self.loadPlugin(self._strPluginExecEvaluationIndexing, \
                                                                   "IndexingEvalualtionLABELIT")
        self._edPluginControlIndexingMOSFLM = self.loadPlugin(self._strPluginControlIndexingMOSFLM, \
                                                                   "IndexingMOSFLM")
        self._edPluginExecEvaluationIndexingMOSFLM = self.loadPlugin(self._strPluginExecEvaluationIndexing, \
                                                                   "IndexingEvalualtionMOSFLM")
        self._edPluginControlGeneratePrediction = self.loadPlugin(self._strPluginControlGeneratePrediction, \
                                                                   "GeneratePrediction")
        self._edPluginControlIntegration = self.loadPlugin(self._strPluginControlIntegration, \
                                                            "Integration")
        self._edPluginControlXDSGenerateBackgroundImage = self.loadPlugin(self._strPluginControlXDSGenerateBackgroundImage, \
                                                            "ControlXDSGenerateBackgroundImage")
        self._edPluginControlStrategy = self.loadPlugin(self._strPluginControlStrategy, \
                                                         "Strategy")
        self._edPluginExecFbest = self.loadPlugin(self._strPluginExecFbestName, \
                                                         "Fbest")
        if self._runKappa:
            self._edPluginControlKappa = self.loadPlugin(self._strPluginControlKappaName, "Kappa")
        if (self._edPluginControlIndexingIndicators is not None):
            self.DEBUG("EDPluginControlCharacterisationv1_5.preProcess: " + self._strPluginControlIndexingIndicators + " Found... setting Data Input")
            # create Data Input for indexing
            self._xsDataCollection = xsDataInputCharacterisation.getDataCollection()
            self._xsDataDiffractionPlan = self._xsDataCollection.getDiffractionPlan()
            self._bDoOnlyFbest = False
            self._bMoslmWithoutThreshold = True
            if self._xsDataDiffractionPlan.strategyType is not None:
                self._strStrategyType = self._xsDataDiffractionPlan.strategyType.value
            if self._strStrategyType is None:
                self._strStrategyType = "fast"
            if self._strStrategyType.lower() == "fbest":
                self.addStatusMessage("FBEST strategy (instead of BEST)")
                self._bDoOnlyFbest = True
                self._bDoStrategyCalculation = False
                self._edPluginControlIndexingIndicators.setLabelitIndexing(False)
            elif self._strStrategyType.lower() == "fast":
                self.addStatusMessage("FAST strategy: Labelit, MOSLFM only if diffraction signal above threshold, and BEST")
                self._bMoslmWithoutThreshold = False
            elif self._strStrategyType.lower() == "full":
                self.addStatusMessage("FULL strategy: Labelit, MOSLFM and BEST")
            else:
                self.addStatusMessage(f"Unknow strategy type: {self._strStrategyType}", "warning")
                self.addStatusMessage("Using FULL strategy: Labelit, MOSLFM and BEST", "warning")
            # MXSUP-1445: Check if transmission is less than 10% and warn if it's the case
            xsDataFirstSubWedge = self._xsDataCollection.getSubWedge()[0]
            xsDataBeam = xsDataFirstSubWedge.getExperimentalCondition().getBeam()
            if xsDataBeam.getTransmission() is not None:
                fTransmission = xsDataBeam.getTransmission().getValue()
                if fTransmission < self._fMinTransmission:
                    strWarningMessageBanner = "^"*80
                    strWarningMessage1 = "WARNING! Transmission for characterisation set to %.1f %%" % fTransmission
                    strWarningMessage2 = "Please consider re-characterising with transmission set to 100 %"
                    self.warning(strWarningMessageBanner)
                    self.warning(strWarningMessage1)
                    self.warning(strWarningMessage2)
                    self.warning(strWarningMessageBanner)
                    self.addWarningMessage(strWarningMessageBanner)
                    self.addWarningMessage(strWarningMessage1)
                    self.addWarningMessage(strWarningMessage2)
                    self.addWarningMessage(strWarningMessageBanner)
                    self.addStatusMessage(strWarningMessage1, "warning")
                    self.addStatusMessage(strWarningMessage2, "warning")
            xsDataCrystal = None
            xsDataSubWedgeList = self._xsDataCollection.getSubWedge()
            if ((xsDataSubWedgeList is None) or (xsDataSubWedgeList == [])):
                strError = "EDPluginControlCharacterisationv1_5.preProcess: No subwedges in input data."
                self.ERROR(strError)
                self.setFailure()
            else:
                # Load the thumbnail plugins
                self._iNoReferenceImages = 0
                for subWedge in xsDataInputCharacterisation.dataCollection.subWedge:
                    for image in subWedge.image:
                        self._iNoReferenceImages += 1
                        if EDNA2_THUMBNAILS:
                            inDataDiffThumbnail = {
                                "image": [image.path.value],
                                "forcedOutputDirectory": self.getWorkingDirectory(),
                                "workingDirectory": self.getWorkingDirectory()
                            }
                            diffractionThumbnail = DiffractionThumbnail(inData=inDataDiffThumbnail)
                            diffractionThumbnail.start()
                            self._listPluginGenerateThumbnail.append((image, diffractionThumbnail))
                        else:
                            edPluginJpeg = self.loadPlugin(self._strPluginGenerateThumbnailName)
                            xsDataInputMXThumbnail = XSDataInputMXThumbnail()
                            xsDataInputMXThumbnail.image = XSDataFile(image.path)
                            xsDataInputMXThumbnail.height = XSDataInteger(1024)
                            xsDataInputMXThumbnail.width = XSDataInteger(1024)
                            jpegFilename = os.path.splitext(os.path.basename(image.path.value))[0] + ".jpg"
                            xsDataInputMXThumbnail.outputPath = XSDataFile(XSDataString(os.path.join(self.getWorkingDirectory(), jpegFilename)))
                            edPluginJpeg.dataInput = xsDataInputMXThumbnail
                            edPluginThumnail = self.loadPlugin(self._strPluginGenerateThumbnailName)
                            xsDataInputMXThumbnail = XSDataInputMXThumbnail()
                            xsDataInputMXThumbnail.image = XSDataFile(image.path)
                            xsDataInputMXThumbnail.height = XSDataInteger(256)
                            xsDataInputMXThumbnail.width = XSDataInteger(256)
                            thumbnailFilename = os.path.splitext(os.path.basename(image.path.value))[0] + ".thumbnail.jpg"
                            xsDataInputMXThumbnail.outputPath = XSDataFile(XSDataString(os.path.join(self.getWorkingDirectory(), thumbnailFilename)))
                            edPluginThumnail.dataInput = xsDataInputMXThumbnail
                            self._listPluginGenerateThumbnail.append((image, edPluginJpeg, edPluginThumnail))
                            edPluginJpeg.execute()
                            edPluginThumnail.execute()
                xsDataExperimentalCondition = xsDataSubWedgeList[0].getExperimentalCondition()

                # Fix for bug 431: if the flux is zero raise an error
                xsDataDoubleFlux = xsDataExperimentalCondition.getBeam().getFlux()
                if (xsDataDoubleFlux is not None):
                    if (xsDataDoubleFlux.getValue() < 0.1):
                        strErrorMessage = "Input flux is negative or close to zero. Execution of characterisation aborted."
                        self.ERROR(strErrorMessage)
                        self.sendMessageToMXCuBE(strErrorMessage, "error")
                        self.addErrorMessage("EDPluginControlCharacterisationv1_5.preProcess ERROR: " + strErrorMessage)
                        # self.addComment(strErrorMessage)
                        self.setFailure()

                xsDataDiffractionPlan = self._xsDataCollection.getDiffractionPlan()
                xsDataStringForcedSpaceGroup = xsDataDiffractionPlan.getForcedSpaceGroup()
                if (xsDataStringForcedSpaceGroup is not None):
                    self._xsDataCrystal = XSDataCrystal()
                    xsDataSpaceGroup = XSDataSpaceGroup()
                    xsDataSpaceGroup.setName(xsDataStringForcedSpaceGroup)
                    self._xsDataCrystal.setSpaceGroup(xsDataSpaceGroup)

                self._edPluginControlIndexingIndicators.setDataInput(self._xsDataCollection, "dataCollection")
                if self._xsDataCrystal is not None:
                    self._edPluginControlIndexingIndicators.setDataInput(self._xsDataCrystal, "crystal")

                self._edPluginControlIndexingIndicators.strToken = strToken

                # Populate characterisation object
                self._xsDataResultCharacterisation.setDataCollection(XSDataCollection.parseString(self._xsDataCollection.marshal()))
        if self._edPluginControlIndexingMOSFLM is not None:
            xsDataIndexingInput = XSDataIndexingInput()
            xsDataIndexingInput.dataCollection = self._xsDataCollection
            xsDataIndexingInput.experimentalCondition = self._xsDataCollection.subWedge[0].experimentalCondition
            xsDataIndexingInput.crystal = self._xsDataCrystal
            self._edPluginControlIndexingMOSFLM.setDataInput(xsDataIndexingInput)


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlCharacterisationv1_5.process")
        self._edPluginControlIndexingIndicators.connectSUCCESS(self.doSuccessIndexingIndicators)
        self._edPluginControlIndexingIndicators.connectFAILURE(self.doFailureIndexingIndicators)
        self._edPluginExecEvaluationIndexingLABELIT.connectSUCCESS(self.doSuccessEvaluationIndexingLABELIT)
        self._edPluginExecEvaluationIndexingLABELIT.connectFAILURE(self.doFailureEvaluationIndexingLABELIT)
        # self._edPluginControlIndexingMOSFLM.connectSUCCESS(self.doSuccessIndexingMOSFLM)
        # self._edPluginControlIndexingMOSFLM.connectFAILURE(self.doFailureIndexingMOSFLM)
        self._edPluginExecEvaluationIndexingMOSFLM.connectSUCCESS(self.doSuccessEvaluationIndexingMOSFLM)
        self._edPluginExecEvaluationIndexingMOSFLM.connectFAILURE(self.doFailureEvaluationIndexingMOSFLM)
        self._edPluginControlGeneratePrediction.connectSUCCESS(self.doSuccessGeneratePrediction)
        self._edPluginControlGeneratePrediction.connectFAILURE(self.doFailureGeneratePrediction)
        self._edPluginControlIntegration.connectSUCCESS(self.doSuccessIntegration)
        self._edPluginControlIntegration.connectFAILURE(self.doFailureIntegration)
        self._edPluginControlXDSGenerateBackgroundImage.connectSUCCESS(self.doSuccessXDSGenerateBackgroundImage)
        self._edPluginControlXDSGenerateBackgroundImage.connectFAILURE(self.doFailureXDSGenerateBackgroundImage)
        self._edPluginControlStrategy.connectSUCCESS(self.doSuccessStrategy)
        self._edPluginControlStrategy.connectFAILURE(self.doFailureStrategy)
        if self._bDoOnlyFbest:
            self.addStatusMessage("Dozor")
        elif not self._bDoOnlyMoslmfIndexing:
            self.addStatusMessage("Labelit indexing")
        self.addStatusMessage("MOSFLM indexing")
        self.executePlugin(self._edPluginControlIndexingMOSFLM)
        self.executePluginSynchronous(self._edPluginControlIndexingIndicators)


    def finallyProcess(self, _edObject=None):
        EDPluginControl.finallyProcess(self)
        self.DEBUG("EDPluginControlCharacterisationv1_5.finallyProcess")
        # Synchronize thumbnail plugins
        for tuplePlugin in self._listPluginGenerateThumbnail:
            if EDNA2_THUMBNAILS:
                image = tuplePlugin[0]
                tuplePlugin[1].join()
                jpegImage = image.copy()
                jpegImage.path = XSDataString(tuplePlugin[1].outData["pathToJPEGImage"][0])
                self._xsDataResultCharacterisation.addJpegImage(jpegImage)
                thumbnailImage = image.copy()
                thumbnailImage.path = XSDataString(tuplePlugin[1].outData["pathToThumbImage"][0])
            else:
                image = tuplePlugin[0]
                tuplePlugin[1].synchronize()
                jpegImage = image.copy()
                jpegImage.path = tuplePlugin[1].dataOutput.thumbnail.path
                self._xsDataResultCharacterisation.addJpegImage(jpegImage)
                tuplePlugin[2].synchronize()
                thumbnailImage = image.copy()
                thumbnailImage.path = tuplePlugin[2].dataOutput.thumbnail.path
            self._xsDataResultCharacterisation.addThumbnailImage(thumbnailImage)           
            self._xsDataResultCharacterisation.addThumbnailImage(thumbnailImage)
        if self._edPluginControlGeneratePrediction.isRunning():
            self._edPluginControlGeneratePrediction.synchronize()
        if self._strStatusMessage != None:
            self.setDataOutput(XSDataString(self._strStatusMessage), "statusMessage")
            self._xsDataResultCharacterisation.setStatusMessage(XSDataString(self._strStatusMessage))
        if self._strCharacterisationShortSummary != None:
            self.setDataOutput(XSDataString(self._strCharacterisationShortSummary), "shortSummary")
            self._xsDataResultCharacterisation.setShortSummary(XSDataString(self._strCharacterisationShortSummary))
        if self._xsDataResultCharacterisation is not None:
            self.setDataOutput(self._xsDataResultCharacterisation)
        if self.isFailure():
            self.sendMessageToMXCuBE("Characterisation ended with error messages", "error")


    def doSuccessIndexingIndicators(self, _edPlugin=None):
        self.DEBUG("EDPluginControlCharacterisationv1_5.doSuccessIndexingIndicators")
        # self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_5.doSuccessIndexingIndicators")
        if self._edPluginControlIndexingIndicators.hasDataOutput("indexingResult"):
            xsDataIndexingResult = self._edPluginControlIndexingIndicators.getDataOutput("indexingResult")[0]
            # self._xsDataResultCharacterisation.setIndexingResult(xsDataIndexingResult)
            self._edPluginExecEvaluationIndexingLABELIT.setDataInput(xsDataIndexingResult, "indexingResult")
        if self._edPluginControlIndexingIndicators.hasDataOutput("imageQualityIndicators"):
            nDozorScores = 1
            listXSDataImageQualityIndicators = self._edPluginControlIndexingIndicators.getDataOutput("imageQualityIndicators")
            for xsDataImageQualityIndicators in listXSDataImageQualityIndicators:
                if xsDataImageQualityIndicators.dozor_score:
                    if self._iNoImagesWithDozorScore is None:
                        self._iNoImagesWithDozorScore = 0
                        self._fAverageDozorScore = 0.0
                    fNewDozorScore = xsDataImageQualityIndicators.dozor_score.value
                    self._iNoImagesWithDozorScore += 1
                    self._fAverageDozorScore = self._fAverageDozorScore + ( fNewDozorScore - self._fAverageDozorScore ) / nDozorScores
                    if self._fMinDozorScore is None or fNewDozorScore < self._fMinDozorScore:
                        self._fMinDozorScore = fNewDozorScore
                    nDozorScores += 1
                if xsDataImageQualityIndicators.dozorVisibleResolution is not None:
                    fNewVisibleResolution = xsDataImageQualityIndicators.dozorVisibleResolution.value
                    if self._fVMaxVisibleResolution is None or fNewVisibleResolution < self._fVMaxVisibleResolution:
                        self._fVMaxVisibleResolution = fNewVisibleResolution
                self._xsDataResultCharacterisation.addImageQualityIndicators(xsDataImageQualityIndicators)
                self._edPluginExecEvaluationIndexingLABELIT.setDataInput(xsDataImageQualityIndicators, "imageQualityIndicators")
        if self._iNoImagesWithDozorScore is None or self._iNoImagesWithDozorScore == 0:
            strErrorMessage = "Execution of Indexing and Indicators plugin failed."
            self.sendMessageToMXCuBE(strErrorMessage, "error")
            self.generateExecutiveSummary(self)
            if self._xsDataResultCharacterisation is not None:
                self.setDataOutput(self._xsDataResultCharacterisation)
            self.setFailure()
            if self._strStatusMessage != None:
                self.setDataOutput(XSDataString(self._strStatusMessage), "statusMessage")
                self.writeDataOutput()
        elif self._fAverageDozorScore is None or self._fAverageDozorScore < 0.001:
            self.sendMessageToMXCuBE("No diffraction detected therefore no strategy calculated.", "warning")
            self.generateExecutiveSummary(self)
            if self._xsDataResultCharacterisation is not None:
                self.setDataOutput(self._xsDataResultCharacterisation)
            self.setFailure()
        else:
            self.sendMessageToMXCuBE("Min dozor score: {0:.1f}".format(self._fMinDozorScore))
            self.sendMessageToMXCuBE("Average dozor score: {0:.1f}".format(self._fAverageDozorScore))
            self.sendMessageToMXCuBE("Max visible resolution: {0:.1f}".format(self._fVMaxVisibleResolution))
            if self._edPluginControlIndexingIndicators.hasDataOutput("indicatorsShortSummary"):
                indicatorsShortSummary = self._edPluginControlIndexingIndicators.getDataOutput("indicatorsShortSummary")[0].getValue()
                self._strCharacterisationShortSummary += indicatorsShortSummary
                self.sendMessageToMXCuBE(indicatorsShortSummary)
            if self._bDoOnlyFbest:
                self.executeFbest()
            else:
                self.executePluginSynchronous(self._edPluginExecEvaluationIndexingLABELIT)


    def doFailureIndexingIndicators(self, _edPlugin=None):
        self.DEBUG("EDPluginControlCharacterisationv1_5.doFailureIndexingIndicators")
        # If more than two reference images try to index with MOSFLM:
        if self._edPluginControlIndexingIndicators.hasDataOutput("indicatorsShortSummary"):
            indicatorsShortSummary = self._edPluginControlIndexingIndicators.getDataOutput("indicatorsShortSummary")[0].getValue()
            self._strCharacterisationShortSummary += indicatorsShortSummary
            self.sendMessageToMXCuBE(indicatorsShortSummary)
        self.checkIfIndexWithMosflm()


    def checkIfIndexWithMosflm(self):
        strWarningMessage = None
        if self._bMoslmWithoutThreshold or self._bDoOnlyMoslmfIndexing:
            bRunMOSFLM = True
            self.sendMessageToMXCuBE("Running MOSFLM by default")
        elif self._fVMaxVisibleResolution > 6.0:
            bRunMOSFLM = False
            strWarningMessage = f"Labelit indexing cancelled and not running MOSFLM indexing because visible resolution lower than 6.0 A"
            self.sendMessageToMXCuBE(strWarningMessage, "warning")
        elif self._fVMaxVisibleResolution > 4.0:
            bRunMOSFLM = False
            strWarningMessage = f"Not running MOSFLM indexing because visible resolution lower than 4.0 A"
            self.sendMessageToMXCuBE(strWarningMessage, "warning")
        elif self._fVMaxVisibleResolution < 2.0:
            bRunMOSFLM = True
            self.sendMessageToMXCuBE("Running MOSFLM because visible resolution higher than 2.0 A")
        elif self._fMinDozorScore < self._fThresholdMosflmIndexing:
            bRunMOSFLM = False
            strWarningMessage = "Not running MOSFLM indexing because of low diffraction signal from at least one image" + \
                                f" (dozor score {self._fMinDozorScore:.1f}" + \
                                f" less than threshold {self._fThresholdMosflmIndexing:.1f})."
            self.sendMessageToMXCuBE(strWarningMessage, "warning")
        else:
            bRunMOSFLM = True
            self.sendMessageToMXCuBE(f"Running MOSFLM (average dozor score average above threshold {self._fThresholdMosflmIndexing:.1f})")
        if strWarningMessage is not None and bRunMOSFLM:
            strWarningMessage = "No indexing solution from Labelit, trying MOSFLM indexing"
            self.sendMessageToMXCuBE(strWarningMessage, "warning")
        if bRunMOSFLM:
            self._edPluginControlIndexingMOSFLM.synchronize()
            if self._edPluginControlIndexingMOSFLM.isFailure():
                self.doFailureIndexingMOSFLM(self._edPluginControlIndexingMOSFLM)
            else:
                self.doSuccessIndexingMOSFLM(self._edPluginControlIndexingMOSFLM)
        else:
            self.executeFbest()


    def doSuccessIndexingMOSFLM(self, _edPlugin=None):
        self.DEBUG("EDPluginControlCharacterisationv1_5.doSuccessIndexingMOSFLM")
        xsDataIndexingResult = self._edPluginControlIndexingMOSFLM.dataOutput
        self._edPluginExecEvaluationIndexingMOSFLM.setDataInput(xsDataIndexingResult, "indexingResult")
        self.executePluginSynchronous(self._edPluginExecEvaluationIndexingMOSFLM)


    def doFailureIndexingMOSFLM(self, _edPlugin=None):
        self.DEBUG("EDPluginControlCharacterisationv1_5.doFailureIndexingMOSFLM")
        strWarningMessage = "Indexing with MOSFLM failed."
        self.sendMessageToMXCuBE(strWarningMessage, "warning")
        self.executePluginSynchronous(self._edPluginExecEvaluationIndexingMOSFLM)




    def doSuccessEvaluationIndexingLABELIT(self, _edPlugin=None):
        self.DEBUG("EDPluginControlCharacterisationv1_5.doSuccessEvaluationIndexingLABELIT")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_5.doSuccessEvaluationIndexingLABELIT")
        # Retrieve status messages (if any)
        # if self._edPluginExecEvaluationIndexingLABELIT.hasDataOutput("statusMessageIndexing"):
        #     self.addStatusMessage("Labelit: " + self._edPluginExecEvaluationIndexingLABELIT.getDataOutput("statusMessageIndexing")[0].getValue())
        # Check if indexing was successful
        bIndexingSuccess = self._edPluginExecEvaluationIndexingLABELIT.getDataOutput("indexingSuccess")[0].getValue()
        if bIndexingSuccess:
            if self._edPluginExecEvaluationIndexingLABELIT.hasDataOutput("statusMessageIndexing"):
                self.addStatusMessage(
                    "Labelit: " + self._edPluginExecEvaluationIndexingLABELIT.getDataOutput("statusMessageIndexing")[
                        0].getValue())
            else:
                self.addStatusMessage("Labelit indexing successful")
            xsDataIndexingResult = self._edPluginExecEvaluationIndexingLABELIT.getDataOutput("indexingResult")[0]
            self._xsDataResultCharacterisation.setIndexingResult(xsDataIndexingResult)
            xsDataCollection = self._xsDataResultCharacterisation.getDataCollection()
            xsDataGeneratePredictionInput = XSDataGeneratePredictionInput()
            xsDataGeneratePredictionInput.setDataCollection(XSDataCollection.parseString(xsDataCollection.marshal()))
            xsDataGeneratePredictionInput.setSelectedIndexingSolution(XSDataIndexingSolutionSelected.parseString(xsDataIndexingResult.getSelectedSolution().marshal()))
            self._edPluginControlGeneratePrediction.setDataInput(xsDataGeneratePredictionInput)
            if self._edPluginControlIndexingIndicators.hasDataOutput("indexingShortSummary"):
                indexingShortSummary = self._edPluginControlIndexingIndicators.getDataOutput("indexingShortSummary")[0].getValue()
                self._strCharacterisationShortSummary += indexingShortSummary
                self.addStatusMessage(indexingShortSummary)
            # Start the generation of prediction images - we synchronize in the post-process
            self._edPluginControlGeneratePrediction.execute()
            # Then start the integration of the reference images
            self.indexingToIntegration()
        else:
            self.checkIfIndexWithMosflm()


    def doSuccessEvaluationIndexingMOSFLM(self, _edPlugin=None):
        self.DEBUG("EDPluginControlCharacterisationv1_5.doSuccessEvaluationIndexingMOSFLM")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_5.doSuccessEvaluationIndexingMOSFLM")
        # Retrieve status messages (if any)
        # if self._edPluginExecEvaluationIndexingMOSFLM.hasDataOutput("statusMessageIndexing"):
        #     self.addStatusMessage("MOSFLM: " + self._edPluginExecEvaluationIndexingMOSFLM.getDataOutput("statusMessageIndexing")[0].getValue())
        # Check if indexing was successful
        bIndexingSuccess = self._edPluginExecEvaluationIndexingMOSFLM.getDataOutput("indexingSuccess")[0].getValue()
        if bIndexingSuccess:
            if self._edPluginExecEvaluationIndexingMOSFLM.hasDataOutput("statusMessageIndexing"):
                self.addStatusMessage(
                    "MOSFLM: " + self._edPluginExecEvaluationIndexingMOSFLM.getDataOutput("statusMessageIndexing")[
                        0].getValue())
            else:
                self.addStatusMessage("MOSFLM indexing successful.")
            xsDataIndexingResult = self._edPluginExecEvaluationIndexingMOSFLM.getDataOutput("indexingResult")[0]
            self._xsDataResultCharacterisation.setIndexingResult(xsDataIndexingResult)
            self._strCharacterisationShortSummary += self.generateIndexingShortSummary(xsDataIndexingResult)
            xsDataCollection = self._xsDataResultCharacterisation.getDataCollection()
            xsDataGeneratePredictionInput = XSDataGeneratePredictionInput()
            xsDataGeneratePredictionInput.setDataCollection(XSDataCollection.parseString(xsDataCollection.marshal()))
            xsDataGeneratePredictionInput.setSelectedIndexingSolution(XSDataIndexingSolutionSelected.parseString(xsDataIndexingResult.getSelectedSolution().marshal()))
            self._edPluginControlGeneratePrediction.setDataInput(xsDataGeneratePredictionInput)
            if self._edPluginControlIndexingIndicators.hasDataOutput("indexingShortSummary"):
                self._strCharacterisationShortSummary += self._edPluginControlIndexingIndicators.getDataOutput("indexingShortSummary")[0].getValue()
            # Start the generation of prediction images - we synchronize in the post-process
            self._edPluginControlGeneratePrediction.execute()
            # Then start the integration of the reference images
            self.indexingToIntegration()
        else:
            self.addStatusMessage("MOSFLM: no indexing solution found.")
            self.executeFbest()

    def generateIndexingShortSummary(self, _xsDataIndexingResult):
        """
        Generates a very short summary of the indexing
        """
        strIndexingShortSummary = ""
        if self.hasDataInput("crystal"):
            xsDataCrystal = self.getDataInput("crystal")[0]
            if xsDataCrystal.getSpaceGroup() is not None:
                strForcedSpaceGroup = xsDataCrystal.getSpaceGroup().getName().getValue().upper()
                if xsDataCrystal.getSpaceGroup().getName().getValue() != "":
                    strIndexingShortSummary += "Forced space group: %s\n" % strForcedSpaceGroup
        if _xsDataIndexingResult is not None:
            # Indexing solution
            xsDataSelectedSolution = _xsDataIndexingResult.getSelectedSolution()
            xsDataCrystal = xsDataSelectedSolution.getCrystal()
            # Refined cell parameters
            xsDataCell = xsDataCrystal.getCell()
            fA = xsDataCell.getLength_a().getValue()
            fB = xsDataCell.getLength_b().getValue()
            fC = xsDataCell.getLength_c().getValue()
            fAlpha = xsDataCell.getAngle_alpha().getValue()
            fBeta = xsDataCell.getAngle_beta().getValue()
            fGamma = xsDataCell.getAngle_gamma().getValue()
            # Estimated mosaicity
            fEstimatedMosaicity = xsDataCrystal.getMosaicity().getValue()
            # Space group
            strSpaceGroup = xsDataCrystal.getSpaceGroup().getName().getValue()
            # Spot deviation
            xsDataStatisticsIndexing = xsDataSelectedSolution.getStatistics()
            fSpotDeviationPositional = xsDataStatisticsIndexing.getSpotDeviationPositional().getValue()
            strIndexingShortSummary += "Indexing: laue/space group %s, mosaicity %.2f [degree], " % (strSpaceGroup, fEstimatedMosaicity)
            strIndexingShortSummary += "RMS dev pos %.2f [mm]" % fSpotDeviationPositional
            if xsDataStatisticsIndexing.getSpotDeviationAngular() is not None:
                fSpotDeviationAngular = xsDataStatisticsIndexing.getSpotDeviationAngular().getValue()
                strIndexingShortSummary += " ang %.2f [degree]" % fSpotDeviationAngular
            strIndexingShortSummary += "\n"
            strIndexingShortSummary += "Indexing: refined Cell: %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f\n" % (fA, fB, fC, fAlpha, fBeta, fGamma)
        else:
            strIndexingShortSummary += "Indexing failed."
        return strIndexingShortSummary


    def indexingToIntegration(self, _edPlugin=None):
        # Run Kappa if configured
        if self._runKappa:
            xsDataInputControlKappa = XSDataInputControlKappa()
            xsDataInputControlKappa.dataCollection = self._xsDataCollection
            xsDataInputControlKappa.selectedSolution = self._xsDataResultCharacterisation.indexingResult.selectedSolution
            self._edPluginControlKappa.dataInput = xsDataInputControlKappa
            self.executePluginSynchronous(self._edPluginControlKappa)
            if not self._edPluginControlKappa.isFailure():
                self._xsDataResultCharacterisation.kappaReorientation = self._edPluginControlKappa.dataOutput
        # Create the XDS background image
        xsDataInputControlXDSGenerateBackgroundImage = XSDataInputControlXDSGenerateBackgroundImage()
        xsDataInputControlXDSGenerateBackgroundImage.setDataCollection(self._xsDataCollection)
        self._edPluginControlXDSGenerateBackgroundImage.setDataInput(xsDataInputControlXDSGenerateBackgroundImage)
        self._edPluginControlXDSGenerateBackgroundImage.execute()
        # Integrate the reference images
        xsDataIntegrationInput = XSDataIntegrationInput()
        xsDataIntegrationInput.setDataCollection(self._xsDataResultCharacterisation.getDataCollection())
        xsDataIndexingResult = self._xsDataResultCharacterisation.getIndexingResult()
        xsDataExperimentalConditionRefinded = xsDataIndexingResult.getSelectedSolution().getExperimentalConditionRefined()
        xsDataIntegrationInput.setExperimentalConditionRefined(xsDataExperimentalConditionRefinded)
        xsDataIntegrationInput.setSelectedIndexingSolution(xsDataIndexingResult.getSelectedSolution())
        self._edPluginControlIntegration.setDataInput(xsDataIntegrationInput)
        self.executePluginSynchronous(self._edPluginControlIntegration)



    def doFailureEvaluationIndexingLABELIT(self, _edPlugin=None):
        self.DEBUG("EDPluginControlCharacterisationv1_5.doFailureEvaluationIndexingLABELIT")
        # self.addStatusMessage("Execution of Labelit indexing evaluation plugin failed.", "warning")
        self.executeFbest()

    def doFailureEvaluationIndexingMOSFLM(self, _edPlugin=None):
        self.DEBUG("EDPluginControlCharacterisationv1_5.doFailureEvaluationIndexingMOSFLM")
        # self.addStatusMessage("Execution of MOSFLM indexing evaluation plugin failed.", "warning")
        self.executeFbest()

    def doSuccessGeneratePrediction(self, _edPlugin=None):
        self.DEBUG("EDPluginControlCharacterisationv1_5.doSuccessGeneratePrediction")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_5.doSuccessGeneratePrediction")
        xsDataGeneratePredictionResult = _edPlugin.getDataOutput()
        xsDataIndexingResult = self._xsDataResultCharacterisation.getIndexingResult()
        xsDataIndexingResult.setPredictionResult(xsDataGeneratePredictionResult)


    def doFailureGeneratePrediction(self, _edPlugin=None):
        self.DEBUG("EDPluginControlCharacterisationv1_5.doFailureGeneratePrediction")
        strWarningMessage = "Execution of generate prediction plugin failed."
        self.WARNING(strWarningMessage)
        self.addWarningMessage(strWarningMessage)
        if self._xsDataResultCharacterisation is not None:
            self.setDataOutput(self._xsDataResultCharacterisation)
        # self.addComment("warning: no prediction images")


    def doSuccessIntegration(self, _edPlugin=None):
        self.DEBUG("EDPluginControlCharacterisationv1_5.doSuccessIntegration")
        self.retrieveSuccessMessages(self._edPluginControlIntegration, "EDPluginControlCharacterisationv1_5.doSuccessIntegration")
        # Wait for XDS plugin if necessary
        self._edPluginControlXDSGenerateBackgroundImage.synchronize()
        self.addStatusMessage("MOSFLM integration successful.")
        xsDataIntegrationOutput = self._edPluginControlIntegration.getDataOutput()
        self._xsDataResultCharacterisation.setIntegrationResult(xsDataIntegrationOutput)
        # Integration short summary
        if self._edPluginControlIntegration.hasDataOutput("integrationShortSummary"):
            integrationShortSummary = self._edPluginControlIntegration.getDataOutput("integrationShortSummary")[0].getValue()
            self._strCharacterisationShortSummary += integrationShortSummary
            # self.sendMessageToMXCuBE(integrationShortSummary)
        # self.DEBUG( self._xsDataExperimentCharacterisation.marshal() )
        if self._bDoStrategyCalculation:
            xsDataInputStrategy = XSDataInputStrategy()
            xsDataSolutionSelected = self._xsDataResultCharacterisation.getIndexingResult().getSelectedSolution()
            xsDataInputStrategy.setCrystalRefined(xsDataSolutionSelected.getCrystal())
            xsDataInputStrategy.setSample(self._xsDataResultCharacterisation.getDataCollection().getSample())
            xsDataIntegrationSubWedgeResultList = xsDataIntegrationOutput.getIntegrationSubWedgeResult()
            bFirst = True
            for xsDataIntegrationSubWedgeResult in xsDataIntegrationSubWedgeResultList:
                if xsDataIntegrationSubWedgeResult.getBestfileHKL() is not None:
                    xsDataInputStrategy.addBestFileContentHKL(xsDataIntegrationSubWedgeResult.getBestfileHKL())
                    if bFirst:
                        xsDataInputStrategy.setBestFileContentDat(xsDataIntegrationSubWedgeResult.getBestfileDat())
                        xsDataInputStrategy.setBestFileContentPar(xsDataIntegrationSubWedgeResult.getBestfilePar())
                        xsDataInputStrategy.setExperimentalCondition(xsDataIntegrationSubWedgeResult.getExperimentalConditionRefined())
                        bFirst = False
            xsDataInputStrategy.setXdsBackgroundImage(self._xsDataFileXdsBackgroundImage)
            xsDataInputStrategy.setDataCollection(self._xsDataCollection)
            xsDataInputStrategy.setDiffractionPlan(self._xsDataResultCharacterisation.getDataCollection().getDiffractionPlan())
            self._edPluginControlStrategy.setDataInput(xsDataInputStrategy)
            self.executePluginSynchronous(self._edPluginControlStrategy)
        else:
            self.executeFbest()



    def doFailureIntegration(self, _edPlugin=None):
        self.DEBUG("EDPluginControlCharacterisationv1_5.doFailureIntegration")
        self.addStatusMessage("MOSFLM integration of one or more images failed.", "warning")
        self.executeFbest()


    def doSuccessXDSGenerateBackgroundImage(self, _edPlugin=None):
        self.DEBUG("EDPluginControlCharacterisationv1_5.doSuccessXDSGenerateBackgroundImage")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlCharacterisationv1_5.doSuccessXDSGenerateBackgroundImage")
        self._xsDataFileXdsBackgroundImage = self._edPluginControlXDSGenerateBackgroundImage.getDataOutput().getXdsBackgroundImage()
        self._xsDataResultCharacterisation.setXdsBackgroundImage(self._xsDataFileXdsBackgroundImage)


    def doFailureXDSGenerateBackgroundImage(self, _edPlugin=None):
        self.DEBUG("EDPluginControlCharacterisationv1_5.doFailureXDSGenerateBackgroundImage")


    def doSuccessStrategy(self, _edPlugin=None):
        self.DEBUG("EDPluginControlCharacterisationv1_5.doSuccessStrategy")
        self.retrieveSuccessMessages(self._edPluginControlStrategy, "EDPluginControlCharacterisationv1_5.doSuccessStrategy")
        xsDataStrategyResult = self._edPluginControlStrategy.getDataOutput()
        self._xsDataResultCharacterisation.setStrategyResult(xsDataStrategyResult)
        if self._edPluginControlStrategy.hasDataOutput("strategyShortSummary"):
            strategyShortSummary = self._edPluginControlStrategy.getDataOutput("strategyShortSummary")[0].getValue()
            self._strCharacterisationShortSummary += strategyShortSummary
            self.sendMessageToMXCuBE(strategyShortSummary)
        self.addStatusMessage("Strategy calculation successful.")


    def doFailureStrategy(self, _edPlugin=None):
        self.DEBUG("EDPluginControlCharacterisationv1_5.doFailureStrategy")
        xsDataStrategyResult = self._edPluginControlStrategy.getDataOutput()
        self._xsDataResultCharacterisation.setStrategyResult(xsDataStrategyResult)
        self.addStatusMessage("BEST strategy calculation failed.", "warning")
        self.executeFbest()


    def executeFbest(self):
        self.addStatusMessage("Executing Fbest for minimal strategy")
        inputCharacterisation = self.getDataInput()
        dataCollection = inputCharacterisation.dataCollection
        subWedge = dataCollection.subWedge[0]
        experimentalCondition = subWedge.experimentalCondition
        detector = experimentalCondition.detector
        beam = experimentalCondition.beam
        flux = beam.flux.value
        beamH = beam.size.x.value
        beamV = beam.size.y.value
        wavelength = beam.wavelength.value
        minExposureTime = beam.minExposureTimePerImage.value
        xsDataInputFbest = XSDataInputFbest()
        xsDataInputFbest.flux = XSDataDouble(flux)
        fFbestResolution = None
        if self._fVMaxVisibleResolution is not None:
            fFbestResolution = self._fVMaxVisibleResolution
            resolutionSource = "dozor visible resolution"
        elif self._fCurrentResolution is not None:
            fFbestResolution = self._fCurrentResolution
            resolutionSource = "input file"
        else:
            fFbestResolution = self.getResolutionFromMXCuBE()
            if fFbestResolution is None:
                fFbestResolution = 2.0
                resolutionSource = "default value"
                self.addStatusMessage(f"No input resolution, using default resolution {fFbestResolution:.2f} A", "warning")
            else:
                resolutionSource = "MXCuBE"
        self.addStatusMessage(f"Fbest: input resolution {fFbestResolution:.2f} A from {resolutionSource}")
        xsDataInputFbest.resolution = XSDataDouble(fFbestResolution)
        xsDataInputFbest.beamH = XSDataDouble(beamH * 1000)
        xsDataInputFbest.beamV = XSDataDouble(beamV * 1000)
        xsDataInputFbest.wavelength = XSDataDouble(wavelength)
        # xsDataInputFbest.aperture = XSDataDouble(0.0)
        # xsDataInputFbest.slitX = XSDataDouble(0.0)
        # xsDataInputFbest.slitY = XSDataDouble(0.0)
        # xsDataInputFbest.rotationRange = XSDataDouble(0.0)
        xsDataInputFbest.rotationWidth = XSDataDouble(0.2)
        xsDataInputFbest.minExposureTime = XSDataDouble(minExposureTime)
        # xsDataInputFbest.doseLimit = XSDataDouble(0.0)
        # xsDataInputFbest.doseRate = XSDataDouble(0.0)
        # xsDataInputFbest.sensitivity = XSDataDouble(0.0)
        # xsDataInputFbest.crystalSize = XSDataDouble(0.0)
        self._edPluginExecFbest.setDataInput(xsDataInputFbest)
        self.executePluginSynchronous(self._edPluginExecFbest)
        xsDataResultFbest = self._edPluginExecFbest.dataOutput
        if xsDataResultFbest is None or self._edPluginExecFbest.isFailure():
            self.addStatusMessage("Fbest execution failed", "error")
            self.setFailure()
        else:
            # Generate xsDataStrategyResult
            if self._xsDataResultCharacterisation.strategyResult is None:
                xsDataResultStrategy = XSDataResultStrategy()
            else:
                xsDataResultStrategy = self._xsDataResultCharacterisation.strategyResult
            xsDataCollectionPlan = XSDataCollectionPlan()
            xsDataCollectionPlan.collectionPlanNumber = XSDataInteger(1)
            xsDataCollectionStrategy = XSDataCollection()
            xsDataStrategySummary = XSDataStrategySummary()
            xsDataSubWedge = XSDataSubWedge()
            xsDataExperimentalCondition = XSDataExperimentalCondition()
            xsDataGoniostat = XSDataGoniostat()
            xsDataBeam = XSDataBeam()
            fBestShortSummary1 = "FBest: "
            fBestShortSummary2 = "FBest: "
            if xsDataResultFbest.totalDose is not None:
                totalDose = xsDataResultFbest.totalDose.value
                fBestShortSummary1 += f"Total dose {totalDose:.2f},"
            if xsDataResultFbest.rotationWidth is not None:
                rotationWidth = xsDataResultFbest.rotationWidth.value
                xsDataGoniostat.oscillationWidth = XSDataAngle(rotationWidth)
                fBestShortSummary1 += f" oscillation width {rotationWidth} degrees,"
            if xsDataResultFbest.numberOfImages is not None:
                numberOfImages = xsDataResultFbest.numberOfImages.value
                fBestShortSummary1 += f" number of images {numberOfImages}"
                xsDataGoniostat.rotationAxisStart = XSDataAngle(0.0)
                xsDataGoniostat.rotationAxisEnd = XSDataAngle(numberOfImages * rotationWidth)
            if xsDataResultFbest.exposureTimePerImage is not None:
                exposureTime = xsDataResultFbest.exposureTimePerImage.value
                xsDataBeam.exposureTime = XSDataTime(exposureTime)
                fBestShortSummary2 += f"Exposure time {exposureTime:.3f} s,"
            if xsDataResultFbest.transmission is not None:
                transmission = xsDataResultFbest.transmission.value
                xsDataBeam.transmission = xsDataResultFbest.transmission
                fBestShortSummary2 += f" transmission {transmission} %,"
            if xsDataResultFbest.resolution is not None:
                resolution = xsDataResultFbest.resolution.value
                fBestShortSummary2 += f" resolution {resolution} A"
                xsDataStrategySummary.resolution = XSDataDouble(resolution)
            self.sendMessageToMXCuBE(fBestShortSummary1)
            self.sendMessageToMXCuBE(fBestShortSummary2)
            self._strCharacterisationShortSummary += fBestShortSummary2 + "\n"
            self._strCharacterisationShortSummary += fBestShortSummary1
            # if xsDataResultFbest.totalExposureTime is not None:
            #     totalExposureTime = xsDataResultFbest.totalExposureTime.value
            #     xsDataStrategySummary.totalDataCollectionTime = XSDataTime(totalExposureTime)
            # if xsDataResultFbest.doseRate is not None:
            #     doseRate = xsDataResultFbest.doseRate.value
            #     self.addStatusMessage(f"FBest: dose rate {doseRate}")
            # if xsDataResultFbest.sensitivity is not None:
            #     sensitivity = xsDataResultFbest.sensitivity.value
            #     self.addStatusMessage(f"FBest: sensitivity {sensitivity}")
            # if xsDataResultFbest.minExposure is not None:
            #     minExposure = xsDataResultFbest.minExposure.value
            #     self.addStatusMessage(f"FBest: min Exposure {minExposure}")
            xsDataResultStrategy.fbestLogFile = xsDataResultFbest.fbestLogFile

            xsDataExperimentalCondition.beam = xsDataBeam
            xsDataExperimentalCondition.goniostat = xsDataGoniostat
            xsDataExperimentalCondition.detector = detector
            xsDataSubWedge.subWedgeNumber = XSDataInteger(1)
            xsDataSubWedge.experimentalCondition = xsDataExperimentalCondition
            xsDataCollectionStrategy.addSubWedge(xsDataSubWedge)
            xsDataCollectionPlan.collectionStrategy = xsDataCollectionStrategy
            xsDataCollectionPlan.strategySummary = xsDataStrategySummary
            xsDataResultStrategy.addCollectionPlan(xsDataCollectionPlan)
            self._xsDataResultCharacterisation.setStrategyResult(xsDataResultStrategy)
            # self.screen(self._xsDataResultCharacterisation.marshal())
            self.addStatusMessage("Fbest strategy calculation successful.")


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        self.DEBUG("EDPluginControlCharacterisationv1_5.generateExecutiveSummary")
        self.addExecutiveSummaryLine("Summary of characterisation:")
        xsDataInputStrategy = self.getDataInput()
        xsDataCollection = xsDataInputStrategy.getDataCollection()
        # MXSUP-1445: Check if transmission is less than 10% and warn if it's the case
        xsDataFirstSubWedge = xsDataCollection.getSubWedge()[0]
        xsDataBeam = xsDataFirstSubWedge.getExperimentalCondition().getBeam()
        if xsDataBeam.getTransmission() is not None:
            fTransmission = xsDataBeam.getTransmission().getValue()
            if fTransmission < self._fMinTransmission:
                self.addExecutiveSummaryLine("^"*80)
                self.addExecutiveSummaryLine("^"*80)
                self.addExecutiveSummaryLine("")
                self.addExecutiveSummaryLine("WARNING! Transmission for characterisation set to %.1f %%" % fTransmission)
                self.addExecutiveSummaryLine("Please consider re-characterising with transmission set to 100 %")
                self.addExecutiveSummaryLine("")
                self.addExecutiveSummaryLine("^"*80)
                self.addExecutiveSummaryLine("^"*80)
        xsDataDiffractionPlan = xsDataCollection.getDiffractionPlan()
        self.addExecutiveSummaryLine("Diffraction plan:")
        if (xsDataDiffractionPlan.getComplexity() is not None):
            self.addExecutiveSummaryLine("BEST complexity                       : %s" % xsDataDiffractionPlan.getComplexity().getValue())
        if (xsDataDiffractionPlan.getAimedCompleteness() is not None):
            self.addExecutiveSummaryLine("Aimed completeness                    : %6.1f [%%]" % (100.0 * xsDataDiffractionPlan.getAimedCompleteness().getValue()))
        if (xsDataDiffractionPlan.getRequiredCompleteness() is not None):
            self.addExecutiveSummaryLine("Required completeness                 : %6.1f [%%]" % (100.0 * xsDataDiffractionPlan.getRequiredCompleteness().getValue()))
        if (xsDataDiffractionPlan.getAimedIOverSigmaAtHighestResolution() is not None):
            self.addExecutiveSummaryLine("Aimed I/sigma at highest resolution   : %6.1f" % xsDataDiffractionPlan.getAimedIOverSigmaAtHighestResolution().getValue())
        if (xsDataDiffractionPlan.getAimedResolution() is not None):
            self.addExecutiveSummaryLine("Aimed resolution                      : %6.1f [A]" % xsDataDiffractionPlan.getAimedResolution().getValue())
        if (xsDataDiffractionPlan.getRequiredResolution() is not None):
            self.addExecutiveSummaryLine("Required resolution                   : %6.1f [A]" % xsDataDiffractionPlan.getRequiredResolution().getValue())
        if (xsDataDiffractionPlan.getAimedMultiplicity() is not None):
            self.addExecutiveSummaryLine("Aimed multiplicity                    : %6.1f" % xsDataDiffractionPlan.getAimedMultiplicity().getValue())
        if (xsDataDiffractionPlan.getRequiredMultiplicity() is not None):
            self.addExecutiveSummaryLine("Required multiplicity                 : %6.1f" % xsDataDiffractionPlan.getRequiredMultiplicity().getValue())
        if (xsDataDiffractionPlan.getForcedSpaceGroup() is not None):
            self.addExecutiveSummaryLine("Forced space group                    : %6s" % xsDataDiffractionPlan.getForcedSpaceGroup().getValue())
        if (xsDataDiffractionPlan.getMaxExposureTimePerDataCollection() is not None):
            self.addExecutiveSummaryLine("Max exposure time per data collection : %6.1f [s]" % xsDataDiffractionPlan.getMaxExposureTimePerDataCollection().getValue())
        self.addExecutiveSummarySeparator()
        # if self._edPluginControlIndexingIndicators is not None:
        #     self.appendExecutiveSummary(self._edPluginControlIndexingIndicators, "")
        # if self._edPluginControlIntegration is not None:
        #     self.appendExecutiveSummary(self._edPluginControlIntegration, "")
        # if self._edPluginControlStrategy is not None:
        #     self.appendExecutiveSummary(self._edPluginControlStrategy, "")
        self.addExecutiveSummarySeparator()
        if self._strCharacterisationShortSummary is not None:
            self.addExecutiveSummaryLine("Characterisation short summary:")
            self.addExecutiveSummaryLine("")
            if self._strStatusMessage != None:
                for strLine in self._strStatusMessage.split(". "):
                    if strLine.endswith("."):
                        self.addExecutiveSummaryLine(strLine)
                    else:
                        self.addExecutiveSummaryLine(strLine + ".")
            self.addExecutiveSummaryLine("")
            for strLine in self._strCharacterisationShortSummary.split("\n"):
                if strLine != "\n":
                    self.addExecutiveSummaryLine(strLine)
        self.addErrorWarningMessagesToExecutiveSummary("Characterisation error and warning messages: ")
        self.addExecutiveSummarySeparator()


    def getPluginStrategyName(self):
        return self._strPluginControlStrategy


    def addStatusMessage(self, _strStatusMessage, level="info"):
        if self._strStatusMessage != "":
            if not _strStatusMessage.endswith("."):
                self._strStatusMessage += "."
            self._strStatusMessage += " "
        self._strStatusMessage += _strStatusMessage
        self.sendMessageToMXCuBE(_strStatusMessage, level=level)


    def doStrategyCalculation(self, _bValue):
        self._bDoStrategyCalculation = _bValue


    def sendMessageToMXCuBE(self, _strMessage, level="info"):
        # Only for mxCuBE
        if level.lower() == "warning":
            self.WARNING(_strMessage)
            self.addWarningMessage(_strMessage)
        elif level.lower() == "error":
            self.ERROR(_strMessage)
            self.addErrorMessage(_strMessage)
        else:
            self.screen(_strMessage)
        if self._strMxCuBE_URI is not None:
            self.DEBUG("Sending message to mxCuBE: {0}".format(_strMessage))
            try:
                for strMessage in _strMessage.split("\n"):
                    if strMessage != "":
                        self._oServerProxy.log_message("Characterisation: " + strMessage, level)
            except:
                self.DEBUG("Sending message to mxCuBE failed!")

    def getResolutionFromMXCuBE(self):
        fCurrentResolution = None
        if self._strMxCuBE_URI is not None:
            self.DEBUG("Trying to read resolution from MXCuBE")
            try:
                fCurrentResolution = float(self._oServerProxy.beamline_setup_read("/beamline/resolution"))
            except Exception as e:
                self.DEBUG("Cannot read resolution from MXCuBE!")
        return fCurrentResolution
