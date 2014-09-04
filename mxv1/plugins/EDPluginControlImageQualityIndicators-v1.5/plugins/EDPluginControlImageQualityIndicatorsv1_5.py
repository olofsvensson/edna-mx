#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2011 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDVerbose import EDVerbose
from EDUtilsParallel import EDUtilsParallel

from EDPluginControl import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataImage

from XSDataMXv1 import XSDataImageQualityIndicators
from XSDataMXv1 import XSDataInputControlImageQualityIndicators
from XSDataMXv1 import XSDataResultControlImageQualityIndicators
from XSDataMXv1 import XSDataInputReadImageHeader
from XSDataMXv1 import XSDataInputSubWedgeAssemble
from XSDataMXv1 import XSDataCollection
from XSDataMXv1 import XSDataIndexingInput

from EDHandlerXSDataLabelitv1_1 import EDHandlerXSDataLabelitv1_1

EDFactoryPluginStatic.loadModule("XSDataMXWaitFilev1_1")
from XSDataMXWaitFilev1_1 import XSDataInputMXWaitFile

EDFactoryPluginStatic.loadModule("XSDataLabelitv1_1")
from XSDataLabelitv1_1 import XSDataInputDistlSignalStrength

EDFactoryPluginStatic.loadModule("XSDataISPyBv1_4")
from XSDataISPyBv1_4 import XSDataISPyBImageQualityIndicators
from XSDataISPyBv1_4 import XSDataInputStoreListOfImageQualityIndicators

EDFactoryPluginStatic.loadModule("XSDataControlDozorv1_0")
from XSDataControlDozorv1_0 import XSDataInputControlDozor


class EDPluginControlImageQualityIndicatorsv1_5(EDPluginControl):
    """
    This plugin that control the plugin that generates the image quality indicators.
    """

    def __init__ (self):
        EDPluginControl.__init__(self)
        self.strPluginMXWaitFileName = "EDPluginMXWaitFilev1_1"
        self.strPluginName = "EDPluginDistlSignalStrengthv1_1"
        self.strPluginNameThinClient = "EDPluginDistlSignalStrengthThinClientv1_1"
        self.strPluginNameControlDozor = "EDPluginControlDozorv1_0"
        self.strISPyBPluginName = "EDPluginISPyBStoreListOfImageQualityIndicatorsv1_5"
        self.strIndexingLabelitPluginName = "EDPluginLabelitIndexingv1_1"
        self.edPluginLabelitIndexing = None
        self.strPluginReadImageHeaderName = "EDPluginControlReadImageHeaderv10"
        self.edPluginReadImageHeader = None
        self.edPluginControlDozor = None
        self.setXSDataInputClass(XSDataInputControlImageQualityIndicators)
        self.listPluginExecImageQualityIndicator = []
        self.listPluginControlDozor = []
        self.xsDataResultControlImageQualityIndicators = None
        self.edPluginMXWaitFile = None
        # Default time out for wait file
        self.fMXWaitFileTimeOut = 30  # s
        # Flag for using the thin client
        self.bUseThinClient = True
        self.edPluginISPyB = None
        self.listPluginLabelit = []
        

    def checkParameters(self):
        """
        Checks the mandatory parameters
        """
        self.DEBUG("EDPluginControlImageQualityIndicatorsv1_5.checkParameters")
        self.checkMandatoryParameters(self.getDataInput().getImage(), "Image")


    def configure(self, _edPlugin=None):
        EDPluginControl.configure(self)
        self.DEBUG("EDPluginControlReadImageHeaderv10.configure")
        self.fMXWaitFileTimeOut = float(self.config.get("MXWaitFileTimeOut", self.fMXWaitFileTimeOut))

    

    def process(self, _edPlugin=None):
        """
        Executes the execution plugins
        """
        EDPluginControl.process(self, _edPlugin)
        self.DEBUG("EDPluginControlImageQualityIndicatorsv1_5.process")
        EDUtilsParallel.initializeNbThread()
        # Check if we should do distlSignalStrength:
        bDoDistlSignalStrength = True
        if self.dataInput.doDistlSignalStrength is not None:
            if not self.dataInput.doDistlSignalStrength.value:
                bDoDistlSignalStrength = False
        # Check if we should do indexing:
        bDoIndexing = False
        if self.dataInput.doIndexing is not None:
            if self.dataInput.doIndexing.value:
                 bDoIndexing = True
        # Loop through all the incoming reference images
        listXSDataImage = self.dataInput.image
        xsDataInputMXWaitFile = XSDataInputMXWaitFile()
        self.xsDataResultControlImageQualityIndicators = XSDataResultControlImageQualityIndicators()
        listPlugin = []
        for xsDataImage in listXSDataImage:
            if not os.path.exists(xsDataImage.path.value):
                self.edPluginMXWaitFile = self.loadPlugin(self.strPluginMXWaitFileName)
                xsDataInputMXWaitFile.file = XSDataFile(xsDataImage.path)
                xsDataInputMXWaitFile.setSize(XSDataInteger(5000000))
                xsDataInputMXWaitFile.setTimeOut(XSDataTime(self.fMXWaitFileTimeOut))
                self.DEBUG("Wait file timeOut set to %f" % self.fMXWaitFileTimeOut)
                self.edPluginMXWaitFile.setDataInput(xsDataInputMXWaitFile)
                self.edPluginMXWaitFile.executeSynchronous()
            if not os.path.exists(xsDataImage.path.value):
                strError = "Time-out while waiting for image %s" % xsDataImage.path.value
                self.error(strError)
                self.addErrorMessage(strError)
                self.setFailure()
            else:
                if bDoDistlSignalStrength:
                    if self.bUseThinClient:
                        strPluginName = self.strPluginNameThinClient
                    else:
                        strPluginName = self.strPluginName
                    edPluginPluginExecImageQualityIndicator = self.loadPlugin(strPluginName)
                    self.listPluginExecImageQualityIndicator.append(edPluginPluginExecImageQualityIndicator)
                    xsDataInputDistlSignalStrength = XSDataInputDistlSignalStrength()
                    xsDataInputDistlSignalStrength.setReferenceImage(xsDataImage)
                    edPluginPluginExecImageQualityIndicator.setDataInput(xsDataInputDistlSignalStrength)
                    edPluginPluginExecImageQualityIndicator.execute()
                else:
                    edPluginPluginExecImageQualityIndicator = xsDataImage
                edPluginControlDozor = self.loadPlugin(self.strPluginNameControlDozor)
                xsDataInputControlDozor = XSDataInputControlDozor()
                xsDataInputControlDozor.addImage(XSDataFile(xsDataImage.path))
                edPluginControlDozor.dataInput = xsDataInputControlDozor
                edPluginControlDozor.execute()
                listPlugin.append([edPluginPluginExecImageQualityIndicator, edPluginControlDozor])
        listIndexing = []
        # Synchronize all image quality indicator plugins and upload to ISPyB
        xsDataInputStoreListOfImageQualityIndicators = XSDataInputStoreListOfImageQualityIndicators()
        for pluginPair in listPlugin:
            if bDoDistlSignalStrength:
                edPluginPluginExecImageQualityIndicator = pluginPair[0]
                edPluginPluginExecImageQualityIndicator.synchronize()
                if edPluginPluginExecImageQualityIndicator.dataOutput.imageQualityIndicators is None:
                    xsDataImageQualityIndicators = XSDataImageQualityIndicators()
                else:
                    xsDataImageQualityIndicators = XSDataImageQualityIndicators.parseString(\
                            edPluginPluginExecImageQualityIndicator.dataOutput.imageQualityIndicators.marshal())
            else:
                xsDataImageQualityIndicators = XSDataImageQualityIndicators()
                xsDataImage = pluginPair[0]
                xsDataImageQualityIndicators.image = xsDataImage
            edPluginControlDozor = pluginPair[1]
            edPluginControlDozor.synchronize()
            if edPluginControlDozor.dataOutput.imageDozor != []:
                xsDataImageQualityIndicators.dozor_score = edPluginControlDozor.dataOutput.imageDozor[0].score
            self.xsDataResultControlImageQualityIndicators.addImageQualityIndicators(xsDataImageQualityIndicators)
            if self.dataInput.doUploadToIspyb is not None and self.dataInput.doUploadToIspyb.value:
                xsDataISPyBImageQualityIndicators = \
                    XSDataISPyBImageQualityIndicators.parseString(xsDataImageQualityIndicators.marshal())
                xsDataInputStoreListOfImageQualityIndicators.addImageQualityIndicators(xsDataISPyBImageQualityIndicators)
#        print xsDataInputStoreListOfImageQualityIndicators.marshal()
        if self.dataInput.doUploadToIspyb is not None and self.dataInput.doUploadToIspyb.value:
            self.edPluginISPyB = self.loadPlugin(self.strISPyBPluginName)
            self.edPluginISPyB.dataInput = xsDataInputStoreListOfImageQualityIndicators
            self.edPluginISPyB.execute()
        #
        if bDoIndexing:
            # Find the 5 most intensive images (TIS):
            listImage = []
            # Check that we have dozor_score from all images:
            has_dozor_score = True
            for imageQualityIndicators in self.xsDataResultControlImageQualityIndicators.imageQualityIndicators:
                if imageQualityIndicators.dozor_score is None:
                    has_dozor_score = False
            if has_dozor_score:
                listSorted = sorted(self.xsDataResultControlImageQualityIndicators.imageQualityIndicators,
                                    key=lambda imageQualityIndicators: imageQualityIndicators.dozor_score.value)
            else:
                listSorted = sorted(self.xsDataResultControlImageQualityIndicators.imageQualityIndicators,
                                    key=lambda imageQualityIndicators: imageQualityIndicators.totalIntegratedSignal.value)
            for xsDataResultControlImageQualityIndicator in listSorted[-5:]:
                if xsDataResultControlImageQualityIndicator.goodBraggCandidates.value > 30:
                    xsDataInputReadImageHeader = XSDataInputReadImageHeader()
                    xsDataInputReadImageHeader.image = XSDataFile(xsDataResultControlImageQualityIndicator.image.path)
                    self.edPluginReadImageHeader = self.loadPlugin(self.strPluginReadImageHeaderName)
                    self.edPluginReadImageHeader.dataInput = xsDataInputReadImageHeader
                    self.edPluginReadImageHeader.executeSynchronous()
                    xsDataResultReadImageHeader = self.edPluginReadImageHeader.dataOutput
                    if xsDataResultReadImageHeader is not None:
                        edPluginLabelitIndexing = self.loadPlugin(self.strIndexingLabelitPluginName)
                        edPluginLabelitIndexing.setDataInput(XSDataImage(xsDataResultControlImageQualityIndicator.image.path), "referenceImage", )
                        self.listPluginLabelit.append([edPluginLabelitIndexing, xsDataResultControlImageQualityIndicator])
                        edPluginLabelitIndexing.execute()
            for tupleLabelit in self.listPluginLabelit:
                edPluginLabelitIndexing = tupleLabelit[0]
                xsDataResultControlImageQualityIndicator = tupleLabelit[1]
                edPluginLabelitIndexing.synchronize()
                if not edPluginLabelitIndexing.isFailure():
                    if edPluginLabelitIndexing.hasDataOutput("labelitScreenOutput") and edPluginLabelitIndexing.hasDataOutput("mosflmScriptsOutput"):
                        xsDataLabelitOutput = edPluginLabelitIndexing.getDataOutput("labelitScreenOutput")[0]
                        xsDataLabelitMosflmScriptsOutput = edPluginLabelitIndexing.getDataOutput("mosflmScriptsOutput")[0]
                        xsDataIndexingResult = EDHandlerXSDataLabelitv1_1.generateXSDataIndexingResult(xsDataLabelitOutput, xsDataLabelitMosflmScriptsOutput)
                        selectedSolution = xsDataIndexingResult.selectedSolution
                        if selectedSolution is not None:
                            xsDataResultControlImageQualityIndicator.selectedIndexingSolution = selectedSolution
            
        

    def finallyProcess(self, _edPlugin=None):
        EDPluginControl.finallyProcess(self, _edPlugin)
        if self.edPluginISPyB is not None:
            # Synchronize ISPyB plugin
            self.DEBUG("EDPluginControlImageQualityIndicatorsv1_5.finallyProcess")
            self.edPluginISPyB.synchronize()
            listId = []
            for xsDataInteger in self.edPluginISPyB.dataOutput.imageQualityIndicatorsId:
                listId.append(xsDataInteger.value)
            self.DEBUG("ISPyB imageQualityIndicatorIds = %r" % listId) 
        self.setDataOutput(self.xsDataResultControlImageQualityIndicators)



    def generateExecutiveSummary(self, _edPlugin=None):
        self.DEBUG("EDPluginControlImageQualityIndicatorsv1_5.generateExecutiveSummary")
        self.addErrorWarningMessagesToExecutiveSummary("Image quality indicator plugin execution failure! Error messages: ")
        self.addExecutiveSummaryLine("Summary of image quality indicators with %s :" % self.strPluginName)
        for edPluginPluginExecImageQualityIndicator in self.listPluginExecImageQualityIndicator:
            self.addExecutiveSummaryLine("")
            if edPluginPluginExecImageQualityIndicator is not None:
                self.appendExecutiveSummary(edPluginPluginExecImageQualityIndicator, "Distl.signal_strength : ", _bAddSeparator=False)
