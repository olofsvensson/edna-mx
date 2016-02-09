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
import time

from EDVerbose import EDVerbose
from EDUtilsParallel import EDUtilsParallel

from EDPluginControl import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic

from EDUtilsImage import EDUtilsImage

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataTime

from XSDataMXv1 import XSDataImageQualityIndicators
from XSDataMXv1 import XSDataInputControlImageQualityIndicators
from XSDataMXv1 import XSDataResultControlImageQualityIndicators
from XSDataMXv1 import XSDataInputReadImageHeader
from XSDataMXv1 import XSDataInputSubWedgeAssemble
from XSDataMXv1 import XSDataCollection
from XSDataMXv1 import XSDataIndexingInput
from XSDataMXv1 import XSDataDozorInput

from EDHandlerXSDataMOSFLMv10 import EDHandlerXSDataMOSFLMv10

EDFactoryPluginStatic.loadModule("XSDataMXWaitFilev1_1")
from XSDataMXWaitFilev1_1 import XSDataInputMXWaitFile

EDFactoryPluginStatic.loadModule("XSDataPhenixv1_1")
from XSDataPhenixv1_1 import XSDataInputDistlSignalStrength

EDFactoryPluginStatic.loadModule("XSDataISPyBv1_4")
from XSDataISPyBv1_4 import XSDataISPyBImageQualityIndicators
from XSDataISPyBv1_4 import XSDataInputStoreListOfImageQualityIndicators

EDFactoryPluginStatic.loadModule("XSDataControlDozorv1_0")
from XSDataControlDozorv1_0 import XSDataInputControlDozor

EDFactoryPluginStatic.loadModule("XSDataControlH5ToCBFv1_0")
from XSDataControlH5ToCBFv1_0 import XSDataInputControlH5ToCBF

class EDPluginControlImageQualityIndicatorsv1_4(EDPluginControl):
    """
    This plugin that control the plugin that generates the image quality indicators.
    """

    def __init__ (self):
        EDPluginControl.__init__(self)
        self.strPluginMXWaitFileName = "EDPluginMXWaitFilev1_1"
        self.strPluginName = "EDPluginDistlSignalStrengthv1_1"
        self.strPluginNameThinClient = "EDPluginDistlSignalStrengthThinClientv1_1"
        self.strPluginNameControlDozor = "EDPluginControlDozorv1_0"
        self.strISPyBPluginName = "EDPluginISPyBStoreListOfImageQualityIndicatorsv1_4"
        self.strIndexingMOSFLMPluginName = "EDPluginMOSFLMIndexingv10"
        self.edPluginMOSFLMIndexing = None
        self.strPluginReadImageHeaderName = "EDPluginControlReadImageHeaderv10"
        self.edPluginReadImageHeader = None
        self.edPluginControlDozor = None
        self.strPluginControlH5ToCBF = "EDPluginControlH5ToCBFv1_0"
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
        self.listPluginMOSFLM = []
        self.defaultMinImageSize = 1000000
        self.minImageSize = None


    def checkParameters(self):
        """
        Checks the mandatory parameters
        """
        self.DEBUG("EDPluginControlImageQualityIndicatorsv1_4.checkParameters")
        self.checkMandatoryParameters(self.getDataInput().getImage(), "Image")


    def configure(self, _edPlugin=None):
        EDPluginControl.configure(self)
        self.DEBUG("EDPluginControlReadImageHeaderv10.configure")
        self.fMXWaitFileTimeOut = float(self.config.get("MXWaitFileTimeOut", self.fMXWaitFileTimeOut))
        self.minImageSize = self.config.get("minImageSize")
        if self.minImageSize is None:
            self.minImageSize = self.defaultMinImageSize



    def process(self, _edPlugin=None):
        """
        Executes the execution plugins
        """
        EDPluginControl.process(self, _edPlugin)
        self.DEBUG("EDPluginControlImageQualityIndicatorsv1_4.process")
        EDUtilsParallel.initializeNbThread()
        # Check batch size
        if self.dataInput.batchSize is None:
            batchSize = 1
        else:
            batchSize = self.dataInput.batchSize.value
        self.screen("Batch size: {0}".format(batchSize))
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
        listPluginDistl = []
        listPluginDozor = []
        listBatch = []
        indexBatch = 0
        listH5FilePath = []
        ispybDataCollection = None
        for xsDataImage in listXSDataImage:
            # If Eiger, just wait for the h5 file
            if "id30a3" in listXSDataImage[0].path.value:
                h5FilePath, hdf5ImageNumber = self.getH5FilePath(xsDataImage.path.value, batchSize)
                print(h5FilePath)
                print(hdf5ImageNumber)
                if not h5FilePath in listH5FilePath:
                    listH5FilePath.append(h5FilePath)
                    self.edPluginMXWaitFile = self.loadPlugin(self.strPluginMXWaitFileName)
                    xsDataInputMXWaitFile.file = XSDataFile(XSDataString(h5FilePath))
                    xsDataInputMXWaitFile.setSize(XSDataInteger(self.minImageSize))
                    xsDataInputMXWaitFile.setTimeOut(XSDataTime(self.fMXWaitFileTimeOut))
                    self.DEBUG("Wait file timeOut set to %f" % self.fMXWaitFileTimeOut)
                    self.edPluginMXWaitFile.setDataInput(xsDataInputMXWaitFile)
                    self.edPluginMXWaitFile.executeSynchronous()
                    hdf5FilePath = xsDataImage.path.value.replace(".cbf", ".h5")
                    ispybDataCollection = None
                    time.sleep(5)
                xsDataInputControlH5ToCBF = XSDataInputControlH5ToCBF()
                xsDataInputControlH5ToCBF.hdf5File = XSDataFile(XSDataString(hdf5FilePath))
                imageNumber = EDUtilsImage.getImageNumber(xsDataImage.path.value)
                xsDataInputControlH5ToCBF.imageNumber = XSDataInteger(imageNumber)
                xsDataInputControlH5ToCBF.hdf5ImageNumber = XSDataInteger(hdf5ImageNumber)
                xsDataInputControlH5ToCBF.ispybDataCollection = ispybDataCollection
                edPluginControlH5ToCBF = self.loadPlugin(self.strPluginControlH5ToCBF, "ControlH5ToCBF_%04d" % imageNumber)
                edPluginControlH5ToCBF.dataInput = xsDataInputControlH5ToCBF
                edPluginControlH5ToCBF.executeSynchronous()
                cbfFile = edPluginControlH5ToCBF.dataOutput.outputCBFFile
                ispybDataCollection = edPluginControlH5ToCBF.dataOutput.ispybDataCollection


            else:
                self.edPluginMXWaitFile = self.loadPlugin(self.strPluginMXWaitFileName)
                xsDataInputMXWaitFile.file = XSDataFile(xsDataImage.path)
                xsDataInputMXWaitFile.setSize(XSDataInteger(self.minImageSize))
                xsDataInputMXWaitFile.setTimeOut(XSDataTime(self.fMXWaitFileTimeOut))
                self.DEBUG("Wait file timeOut set to %f" % self.fMXWaitFileTimeOut)
                self.edPluginMXWaitFile.setDataInput(xsDataInputMXWaitFile)
                self.edPluginMXWaitFile.executeSynchronous()
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
                # Check if we should run distl.signalStrength
                edPluginPluginExecImageQualityIndicator = None
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
                listPluginDistl.append((xsDataImage.copy(), edPluginPluginExecImageQualityIndicator))
                listBatch.append(xsDataImage.copy())
                if len(listBatch) == batchSize:
                    edPluginControlDozor = self.loadPlugin(self.strPluginNameControlDozor)
                    xsDataInputControlDozor = XSDataInputControlDozor()
                    for image in listBatch:
                        xsDataInputControlDozor.addImage(XSDataFile(image.path))
                    xsDataInputControlDozor.batchSize = XSDataInteger(batchSize)
                    edPluginControlDozor.dataInput = xsDataInputControlDozor
                    edPluginControlDozor.execute()
                    listPluginDozor.append((edPluginControlDozor, listBatch))
                    listBatch = []
        if len(listBatch) > 0:
            # Process the remaining images...
            edPluginControlDozor = self.loadPlugin(self.strPluginNameControlDozor)
            xsDataInputControlDozor = XSDataInputControlDozor()
            for image in listBatch:
                xsDataInputControlDozor.addImage(XSDataFile(image.path))
            xsDataInputControlDozor.batchSize = XSDataInteger(batchSize)
            edPluginControlDozor.dataInput = xsDataInputControlDozor
            edPluginControlDozor.execute()
            listPluginDozor.append([edPluginControlDozor, listBatch])
        listIndexing = []
        # Synchronize all image quality indicator plugins and upload to ISPyB
        xsDataInputStoreListOfImageQualityIndicators = XSDataInputStoreListOfImageQualityIndicators()

        for (xsDataImage, edPluginPluginExecImageQualityIndicator) in listPluginDistl:
            xsDataImageQualityIndicators = XSDataImageQualityIndicators()
            xsDataImageQualityIndicators.image = xsDataImage.copy()
            if edPluginPluginExecImageQualityIndicator is not None:
                edPluginPluginExecImageQualityIndicator.synchronize()
                if edPluginPluginExecImageQualityIndicator.dataOutput.imageQualityIndicators is not None:
                    xsDataImageQualityIndicators = XSDataImageQualityIndicators.parseString(\
                            edPluginPluginExecImageQualityIndicator.dataOutput.imageQualityIndicators.marshal())
            self.xsDataResultControlImageQualityIndicators.addImageQualityIndicators(xsDataImageQualityIndicators)

        for (edPluginControlDozor, listBatch) in listPluginDozor:
            edPluginControlDozor.synchronize()
            for imageDozor in edPluginControlDozor.dataOutput.imageDozor:
                for xsDataImageQualityIndicators in self.xsDataResultControlImageQualityIndicators.imageQualityIndicators:
                    if xsDataImageQualityIndicators.image.path.value == imageDozor.image.path.value:
                        xsDataImageQualityIndicators.dozor_score = imageDozor.score
                        xsDataImageQualityIndicators.dozorSpotFile = imageDozor.spotFile
                        xsDataImageQualityIndicators.dozorSpotsIntAver = imageDozor.spots_int_aver
                        xsDataImageQualityIndicators.dozorSpotsResolution = imageDozor.spots_resolution
                        if self.xsDataResultControlImageQualityIndicators.inputDozor is None:
                            if edPluginControlDozor.dataOutput.inputDozor is not None:
                                self.xsDataResultControlImageQualityIndicators.inputDozor = XSDataDozorInput().parseString(
                                               edPluginControlDozor.dataOutput.inputDozor.marshal())
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
                        xsDataSubWedge = xsDataResultReadImageHeader.subWedge
                        self.xsDataCollection = XSDataCollection()
                        self.xsDataCollection.addSubWedge(xsDataSubWedge)
                        xsDataIndexingInput = XSDataIndexingInput()
                        xsDataIndexingInput.setDataCollection(self.xsDataCollection)
                        xsDataMOSFLMIndexingInput = EDHandlerXSDataMOSFLMv10.generateXSDataMOSFLMInputIndexing(xsDataIndexingInput)
                        edPluginMOSFLMIndexing = self.loadPlugin(self.strIndexingMOSFLMPluginName)
                        self.listPluginMOSFLM.append([edPluginMOSFLMIndexing, xsDataResultControlImageQualityIndicator])
                        edPluginMOSFLMIndexing.setDataInput(xsDataMOSFLMIndexingInput)
                        edPluginMOSFLMIndexing.execute()
            for tupleMOSFLM in self.listPluginMOSFLM:
                edPluginMOSFLMIndexing = tupleMOSFLM[0]
                xsDataResultControlImageQualityIndicator = tupleMOSFLM[1]
                edPluginMOSFLMIndexing.synchronize()
                if not edPluginMOSFLMIndexing.isFailure():
                    xsDataMOSFLMOutput = edPluginMOSFLMIndexing.dataOutput
                    xsDataIndexingResult = EDHandlerXSDataMOSFLMv10.generateXSDataIndexingResult(xsDataMOSFLMOutput)
                    selectedSolution = xsDataIndexingResult.selectedSolution
                    if selectedSolution is not None:
                        xsDataResultControlImageQualityIndicator.selectedIndexingSolution = selectedSolution

#                print xsDataIndexingResult.marshal()
#                xsDataResultISPyB = edPluginISPyB.dataOutput
#                if xsDataResultISPyB is not None:
                # print xsDataResultISPyB.marshal()



    def finallyProcess(self, _edPlugin=None):
        EDPluginControl.finallyProcess(self, _edPlugin)
        if self.edPluginISPyB is not None:
            # Synchronize ISPyB plugin
            self.DEBUG("EDPluginControlImageQualityIndicatorsv1_4.finallyProcess")
            self.edPluginISPyB.synchronize()
            listId = []
            for xsDataInteger in self.edPluginISPyB.dataOutput.imageQualityIndicatorsId:
                listId.append(xsDataInteger.value)
            self.DEBUG("ISPyB imageQualityIndicatorIds = %r" % listId)
        self.setDataOutput(self.xsDataResultControlImageQualityIndicators)



    def generateExecutiveSummary(self, _edPlugin=None):
        self.DEBUG("EDPluginControlImageQualityIndicatorsv1_4.generateExecutiveSummary")
        self.addErrorWarningMessagesToExecutiveSummary("Image quality indicator plugin execution failure! Error messages: ")
        self.addExecutiveSummaryLine("Summary of image quality indicators with %s :" % self.strPluginName)
        for edPluginPluginExecImageQualityIndicator in self.listPluginExecImageQualityIndicator:
            self.addExecutiveSummaryLine("")
            if edPluginPluginExecImageQualityIndicator is not None:
                self.appendExecutiveSummary(edPluginPluginExecImageQualityIndicator, "Distl.signal_strength : ", _bAddSeparator=False)

    def getH5FilePath(self, filePath, batchSize=1):
        imageNumber = EDUtilsImage.getImageNumber(filePath)
        prefix = EDUtilsImage.getPrefix(filePath)
        h5FileNumber = int((imageNumber - 1) / batchSize) * batchSize + 1
        h5FileName = "{prefix}_{h5FileNumber}_master.h5".format(prefix=prefix,
                                                                h5FileNumber=h5FileNumber)
        h5FilePath = os.path.join(os.path.dirname(filePath), h5FileName)
        return h5FilePath, h5FileNumber
