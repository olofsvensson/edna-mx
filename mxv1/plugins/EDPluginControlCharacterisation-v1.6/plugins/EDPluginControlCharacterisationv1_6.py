#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2017 European Synchrotron Radiation Facility
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

__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
import xmlrpclib

from EDPluginControl import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataCommon import XSDataString
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataFile

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

EDFactoryPluginStatic.loadModule("XSDataMXThumbnailv1_1")
from XSDataMXThumbnailv1_1 import XSDataInputMXThumbnail

from EDHandlerXSDataXDSv1_0 import EDHandlerXSDataXDSv1_0

class EDPluginControlCharacterisationv1_6(EDPluginControl):
    """
    Characterisation based on XDS
    """


    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputCharacterisation)
        self._strPluginControlIndexingIndicators = "EDPluginControlIndexingIndicatorsv1_1"
        self._fMinTransmission = 10  # %
        self._listPluginGenerateThumbnail = []
        self._strCharacterisationShortSummary = ""
        self._strStatusMessage = ""
        self._strIndexingPluginName = "EDPluginXDSIndexingv1_0"
        self._strIntegrationPluginName = "EDPluginXDSIntegrationv1_0"
        self._edPluginIndexing = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlCharacterisationv1_6.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDataCollection(), "dataCollection")
        self.checkMandatoryParameters(self.getDataInput().getDataCollection().getDiffractionPlan(), "diffractionPlan")

    def configure(self):
        """
        Gets the configuration parameters (if any).
        """
        EDPluginControl.configure(self)
        self.DEBUG("EDPluginControlCharacterisationv1_6.configure")
        self._strMxCuBE_URI = self.config.get("mxCuBE_URI", None)
        if self._strMxCuBE_URI is not None and "mxCuBE_XMLRPC_log" in os.environ.keys():
            self.DEBUG("Enabling sending messages to mxCuBE via URI {0}".format(self._strMxCuBE_URI))
            self._oServerProxy = xmlrpclib.ServerProxy(self._strMxCuBE_URI)
        self._runKappa = self.config.get("runKappa", False)
        self._fMinTransmission = self.config.get("minTransmissionWarning", self._fMinTransmission)



    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlCharacterisationv1_6.preProcess")
        self._xsDataResultCharacterisation = XSDataResultCharacterisation()


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlCharacterisationv1_6.process")
        self.doXdsIndexingIntegration(self.dataInput.dataCollection)


    def finallyProcess(self, _edObject=None):
        EDPluginControl.finallyProcess(self)
        self.DEBUG("EDPluginControlCharacterisationv1_6.finallyProcess")
        # Synchronize thumbnail plugins
        for tuplePlugin in self._listPluginGenerateThumbnail:
            image = tuplePlugin[0]
            tuplePlugin[1].synchronize()
            jpegImage = image.copy()
            jpegImage.path = tuplePlugin[1].dataOutput.thumbnail.path
            self._xsDataResultCharacterisation.addJpegImage(jpegImage)
            tuplePlugin[2].synchronize()
            thumbnailImage = image.copy()
            thumbnailImage.path = tuplePlugin[2].dataOutput.thumbnail.path
            self._xsDataResultCharacterisation.addThumbnailImage(thumbnailImage)
#        if self._edPluginControlGeneratePrediction.isRunning():
#            self._edPluginControlGeneratePrediction.synchronize()
#        if self._strStatusMessage != None:
#            self.setDataOutput(XSDataString(self._strStatusMessage), "statusMessage")
#            self._xsDataResultCharacterisation.setStatusMessage(XSDataString(self._strStatusMessage))
#        if self._strCharacterisationShortSummary != None:
#            self.setDataOutput(XSDataString(self._strCharacterisationShortSummary), "shortSummary")
#            self._xsDataResultCharacterisation.setShortSummary(XSDataString(self._strCharacterisationShortSummary))
#        if self._xsDataResultCharacterisation is not None:
#            self.setDataOutput(self._xsDataResultCharacterisation)
        if self.isFailure():
            self.sendMessageToMXCuBE("Ended with error messages", "error")



    def doXdsIndexingIntegration(self, _xsDataCollection):
        # Load the plugin
        self._edPluginIndexing = self.loadPlugin(self._strIndexingPluginName, "Indexing")
        # XDS Indexing
        xsDataIndexingInput = XSDataIndexingInput()
        xsDataIndexingInput.setDataCollection(_xsDataCollection)
        self._edPluginIndexing.dataInput = EDHandlerXSDataXDSv1_0.generateXSDataInputXDSIndexing(xsDataIndexingInput)
        self._edPluginIndexing.executeSynchronous()
        xsDataResultXDSIndexing = self._edPluginIndexing.dataOutput
        if xsDataResultXDSIndexing.spaceGroupNumber is not None:
            spaceGroupNumber = xsDataResultXDSIndexing.spaceGroupNumber.value
            unitCell = xsDataResultXDSIndexing.unitCell
            filePaths = xsDataResultXDSIndexing.filePaths
            index = 1
            for subWedge in _xsDataCollection.subWedge:
                xsDataCollection = XSDataCollection()
                xsDataCollection.addSubWedge(subWedge)
                xsDataIndexingInput = XSDataIndexingInput()
                xsDataIndexingInput.setDataCollection(xsDataCollection)

                xsDataInputXDSIntegration = EDHandlerXSDataXDSv1_0.generateXSDataInputXDSIntegration(xsDataIndexingInput,
                                                                                                     spaceGroupNumber,
                                                                                                     unitCell,
                                                                                                     filePaths)
                edPluginIntegration = self.loadPlugin(self._strIntegrationPluginName, "Integration_{0}".format(index))
                edPluginIntegration.dataInput = xsDataInputXDSIntegration
                edPluginIntegration.executeSynchronous()
                # self._edPluginIntegration.dataInput = xsDataInputXDSIntegration
                index += 1



    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        self.DEBUG("EDPluginControlCharacterisationv1_6.generateExecutiveSummary")
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
#        if self._edPluginControlIndexingIndicators is not None:
#            self.appendExecutiveSummary(self._edPluginControlIndexingIndicators, "")
#        if self._edPluginControlIntegration is not None:
#            self.appendExecutiveSummary(self._edPluginControlIntegration, "")
#        if self._edPluginControlStrategy is not None:
#            self.appendExecutiveSummary(self._edPluginControlStrategy, "")
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


    def addStatusMessage(self, _strStatusMessage):
        if self._strStatusMessage != "":
            self._strStatusMessage += " "
        self._strStatusMessage += _strStatusMessage
        self.sendMessageToMXCuBE(_strStatusMessage)


    def doStrategyCalculation(self, _bValue):
        self._bDoStrategyCalculation = _bValue


    def sendMessageToMXCuBE(self, _strMessage, level="info"):
        # Only for mxCuBE
        if self._strMxCuBE_URI is not None:
            self.DEBUG("Sending message to mxCuBE: {0}".format(_strMessage))
            try:
                for strMessage in _strMessage.split("\n"):
                    if strMessage != "":
                        self._oServerProxy.log_message("Characterisation: " + strMessage, level)
            except:
                self.DEBUG("Sending message to mxCuBE failed!")
