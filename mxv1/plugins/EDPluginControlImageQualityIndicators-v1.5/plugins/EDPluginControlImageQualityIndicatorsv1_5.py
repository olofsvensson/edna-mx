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
import numpy
import base64

from EDVerbose import EDVerbose
from EDUtilsParallel import EDUtilsParallel
from EDUtilsPath import EDUtilsPath

from EDPluginControl import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic

from EDUtilsImage import EDUtilsImage

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataDouble

from XSDataMXv1 import XSDataImageQualityIndicators
from XSDataMXv1 import XSDataInputControlImageQualityIndicators
from XSDataMXv1 import XSDataResultControlImageQualityIndicators
from XSDataMXv1 import XSDataInputReadImageHeader
from XSDataMXv1 import XSDataInputSubWedgeAssemble
from XSDataMXv1 import XSDataCollection
from XSDataMXv1 import XSDataIndexingInput
from XSDataMXv1 import XSDataDozorInput

from EDHandlerXSDataPhenixv1_1 import EDHandlerXSDataPhenixv1_1

EDFactoryPluginStatic.loadModule("XSDataMXWaitFilev1_1")
from XSDataMXWaitFilev1_1 import XSDataInputMXWaitFile

EDFactoryPluginStatic.loadModule("XSDataPhenixv1_1")
from XSDataPhenixv1_1 import XSDataInputDistlSignalStrength
from XSDataPhenixv1_1 import XSDataInputLabelitIndexing

EDFactoryPluginStatic.loadModule("XSDataISPyBv1_4")
from XSDataISPyBv1_4 import XSDataISPyBImageQualityIndicators
from XSDataISPyBv1_4 import XSDataInputStoreListOfImageQualityIndicators

EDFactoryPluginStatic.loadModule("XSDataControlDozorv1_0")
from XSDataControlDozorv1_0 import XSDataInputControlDozor

EDFactoryPluginStatic.loadModule("XSDataControlH5ToCBFv1_1")
from XSDataControlH5ToCBFv1_1 import XSDataInputControlH5ToCBF

EDFactoryPluginStatic.loadModule('XSDataH5ToCBFv1_1')
from XSDataH5ToCBFv1_1 import XSDataInputH5ToCBF


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
        self.strPluginControlH5ToCBF = "EDPluginControlH5ToCBFv1_1"
        self.setXSDataInputClass(XSDataInputControlImageQualityIndicators)
        self.listPluginExecImageQualityIndicator = []
        self.listPluginControlDozor = []
        self.xsDataResultControlImageQualityIndicators = None
        self.edPluginMXWaitFile = None
        # Default time out for wait file
        self.fMXWaitFileTimeOut = 120  # s
        # Flag for using the thin client - disabled as of 2016/07/20
        self.bUseThinClient = False
        self.edPluginISPyB = None
        self.listPluginLabelit = []
        self.defaultMinImageSize = 1000000
        self.minImageSize = None
        self.strEDPluginControlReadImageHeaderName = "EDPluginControlReadImageHeaderv10"
        self.hasOverlap = False

    def checkParameters(self):
        """
        Checks the mandatory parameters
        """
        self.DEBUG("EDPluginControlImageQualityIndicatorsv1_5.checkParameters")
        # self.checkMandatoryParameters(self.getDataInput().getImage(), "Image")


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
        self.DEBUG("EDPluginControlImageQualityIndicatorsv1_5.process")
        EDUtilsParallel.initializeNbThread()
        # Check batch size
        if self.dataInput.batchSize is None:
            batchSize = 1
        else:
            batchSize = self.dataInput.batchSize.value
        self.screen("Image quality indicators batch size: {0}".format(batchSize))
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
        # Check if fast mesh (for HDF5)
        isFastMesh = False
        if self.dataInput.fastMesh:
            isFastMesh = self.dataInput.fastMesh.value
        # Loop through all the incoming reference images
        if len(self.dataInput.image) == 0:
            directory = self.dataInput.directory.path.value
            template = self.dataInput.template.value
            startNo = self.dataInput.startNo.value
            endNo = self.dataInput.endNo.value
            listXSDataImage = []
            for index in range(startNo, endNo + 1):
                imageName = template.replace("####", "{0:04d}".format(index))
                imagePath = os.path.join(directory, imageName)
                xsDataImage = XSDataImage(path=XSDataString(imagePath), number=XSDataInteger(index))
                listXSDataImage.append(xsDataImage)
        else:
            listXSDataImage = self.dataInput.image
        xsDataInputMXWaitFile = XSDataInputMXWaitFile()
        self.xsDataResultControlImageQualityIndicators = XSDataResultControlImageQualityIndicators()
        listPluginDistl = []
        listPluginDozor = []
        listOfImagesInBatch = []
        listOfAllBatches = []
        indexBatch = 0
        listH5FilePath = []
        # Process data in batches
        for xsDataImage in listXSDataImage:
            listOfImagesInBatch.append(xsDataImage.copy())
            if len(listOfImagesInBatch) == batchSize:
                listOfAllBatches.append(listOfImagesInBatch)
                listOfImagesInBatch = []
        if len(listOfImagesInBatch) > 0:
            listOfAllBatches.append(listOfImagesInBatch)
            listOfImagesInBatch = []
        # Loop over batches
        for listOfImagesInBatch in listOfAllBatches:
            # First wait for images
            for image in listOfImagesInBatch:
                strPathToImage = image.path.value
                # If Eiger, just wait for the h5 file
                if strPathToImage.endswith(".h5"):
                    h5MasterFilePath, h5DataFilePath, hdf5ImageNumber = self.getH5FilePath(strPathToImage,
                                                                                           batchSize=batchSize,
                                                                                           isFastMesh=isFastMesh)
    #                print(h5FilePath)
    #                print(hdf5ImageNumber)
                    if not h5DataFilePath in listH5FilePath:
                        self.screen("ID30a3 Eiger data, waiting for master and data files...")
                        listH5FilePath.append(h5DataFilePath)
                        self.edPluginMXWaitFile = self.loadPlugin(self.strPluginMXWaitFileName)
                        xsDataInputMXWaitFile.file = XSDataFile(XSDataString(h5DataFilePath))
                        xsDataInputMXWaitFile.setSize(XSDataInteger(self.minImageSize))
                        xsDataInputMXWaitFile.setTimeOut(XSDataTime(self.fMXWaitFileTimeOut))
                        self.screen("Waiting for file {0}".format(h5DataFilePath))
                        self.DEBUG("Wait file timeOut set to %f" % self.fMXWaitFileTimeOut)
                        self.edPluginMXWaitFile.setDataInput(xsDataInputMXWaitFile)
                        self.edPluginMXWaitFile.executeSynchronous()
    #                    hdf5FilePath = strPathToImage.replace(".cbf", ".h5")
                        time.sleep(1)
                    if not os.path.exists(h5DataFilePath):
                        strError = "Time-out while waiting for image %s" % h5DataFilePath
                        self.error(strError)
                        self.addErrorMessage(strError)
                        self.setFailure()
                else:
                    if not os.path.exists(strPathToImage):
                        # self.screen("Waiting for file {0}".format(strPathToImage))
                        self.edPluginMXWaitFile = self.loadPlugin(self.strPluginMXWaitFileName)
                        xsDataInputMXWaitFile.file = XSDataFile(XSDataString(strPathToImage))
                        xsDataInputMXWaitFile.setSize(XSDataInteger(self.minImageSize))
                        xsDataInputMXWaitFile.setTimeOut(XSDataTime(self.fMXWaitFileTimeOut))
                        self.screen("Wait file timeOut set to %.0f s" % self.fMXWaitFileTimeOut)
                        self.edPluginMXWaitFile.setDataInput(xsDataInputMXWaitFile)
                        self.edPluginMXWaitFile.executeSynchronous()
                    if not os.path.exists(strPathToImage):
                        strError = "Time-out while waiting for image %s" % strPathToImage
                        self.error(strError)
                        self.addErrorMessage(strError)
                        self.setFailure()
            if not self.isFailure():
                strPathToFirstImage = listOfImagesInBatch[0].path.value
                if strPathToImage.endswith(".h5"):
                    indexLoop = 1
                    continueLoop = True
                    while continueLoop:
                        directory = os.path.dirname(strPathToFirstImage)
                        firstImage = EDUtilsImage.getImageNumber(listOfImagesInBatch[0].path.value)
                        lastImage = EDUtilsImage.getImageNumber(listOfImagesInBatch[-1].path.value)
                        xsDataInputH5ToCBF = XSDataInputH5ToCBF()
                        xsDataInputH5ToCBF.hdf5File = XSDataFile(listOfImagesInBatch[0].path)
                        xsDataInputH5ToCBF.hdf5ImageNumber = XSDataInteger(1)
                        xsDataInputH5ToCBF.startImageNumber = XSDataInteger(firstImage)
                        xsDataInputH5ToCBF.endImageNumber = XSDataInteger(lastImage)
                        xsDataInputH5ToCBF.forcedOutputDirectory = XSDataFile(XSDataString(directory))
                        edPluginH5ToCBF = self.loadPlugin("EDPluginH5ToCBFv1_1")
                        edPluginH5ToCBF.dataInput = xsDataInputH5ToCBF
                        edPluginH5ToCBF.execute()
                        edPluginH5ToCBF.synchronize()
                        outputCBFFileTemplate = edPluginH5ToCBF.dataOutput.outputCBFFileTemplate
                        if outputCBFFileTemplate is not None:
                            lastCbfFile = outputCBFFileTemplate.path.value.replace("######", "{0:06d}".format(EDUtilsImage.getImageNumber(listOfImagesInBatch[-1].path.value)))
                            strPathToImage = os.path.join(directory, lastCbfFile)
    #                        print(cbfFile.path.value)
                            if os.path.exists(strPathToImage):
                                # Rename all images
                                for image in listOfImagesInBatch:
                                    image.path.value = image.path.value.replace(".h5", ".cbf")
                                    imageNumber = EDUtilsImage.getImageNumber(image.path.value)
                                    oldPath = os.path.join(directory, outputCBFFileTemplate.path.value.replace("######", "{0:06d}".format(imageNumber)))
                                    newPath = os.path.join(directory, outputCBFFileTemplate.path.value.replace("######", "{0:04d}".format(imageNumber)))
                                    os.rename(oldPath, newPath)
                                lastCbfFile = outputCBFFileTemplate.path.value.replace("######", "{0:04d}".format(EDUtilsImage.getImageNumber(listOfImagesInBatch[-1].path.value)))
                                strPathToImage = os.path.join(directory, lastCbfFile)
                                self.screen("Image has been converted to CBF file: {0}".format(strPathToImage))
                                continueLoop = False
    #                    print(continueLoop)
                        if continueLoop:
                            self.screen("Still waiting for converting to CBF file: {0}".format(strPathToImage))
                            indexLoop += 1
                            time.sleep(5)
                            if indexLoop > 10:
                                continueLoop = False

                for image in listOfImagesInBatch:
                    strPathToImage = image.path.value
                    # Check if we should run distl.signalStrength
                    xsDataImageNew = XSDataImage(XSDataString(strPathToImage))
                    xsDataImageNew.number = XSDataInteger(EDUtilsImage.getImageNumber(image.path.value))
                    edPluginPluginExecImageQualityIndicator = None
                    if bDoDistlSignalStrength:
                        if self.bUseThinClient:
                            strPluginName = self.strPluginNameThinClient
                        else:
                            strPluginName = self.strPluginName
                        edPluginPluginExecImageQualityIndicator = self.loadPlugin(strPluginName)
                        self.listPluginExecImageQualityIndicator.append(edPluginPluginExecImageQualityIndicator)
                        xsDataInputDistlSignalStrength = XSDataInputDistlSignalStrength()
                        xsDataInputDistlSignalStrength.setReferenceImage(xsDataImageNew)
                        edPluginPluginExecImageQualityIndicator.setDataInput(xsDataInputDistlSignalStrength)
                        edPluginPluginExecImageQualityIndicator.execute()
                    listPluginDistl.append((xsDataImageNew.copy(), edPluginPluginExecImageQualityIndicator))

                edPluginControlDozor = self.loadPlugin(self.strPluginNameControlDozor,
                                                       "ControlDozor_{0}".format(os.path.splitext(os.path.basename(strPathToFirstImage))[0]))
                xsDataInputControlDozor = XSDataInputControlDozor()
                for image in listOfImagesInBatch:
                    xsDataInputControlDozor.addImage(XSDataFile(image.path))
                xsDataInputControlDozor.batchSize = XSDataInteger(len(listOfImagesInBatch))
                edPluginControlDozor.dataInput = xsDataInputControlDozor
                edPluginControlDozor.execute()
                listPluginDozor.append((edPluginControlDozor, list(listOfImagesInBatch)))

        if not self.isFailure():
            listIndexing = []
            # Synchronize all image quality indicator plugins and upload to ISPyB
            xsDataInputStoreListOfImageQualityIndicators = XSDataInputStoreListOfImageQualityIndicators()

            for (xsDataImage, edPluginPluginExecImageQualityIndicator) in listPluginDistl:
                xsDataImageQualityIndicators = XSDataImageQualityIndicators()
                xsDataImageQualityIndicators.image = xsDataImage.copy()
                if edPluginPluginExecImageQualityIndicator is not None:
                    edPluginPluginExecImageQualityIndicator.synchronize()
                    if edPluginPluginExecImageQualityIndicator.dataOutput is not None:
                        if edPluginPluginExecImageQualityIndicator.dataOutput.imageQualityIndicators is not None:
                            xsDataImageQualityIndicators = XSDataImageQualityIndicators.parseString(\
                                    edPluginPluginExecImageQualityIndicator.dataOutput.imageQualityIndicators.marshal())
                self.xsDataResultControlImageQualityIndicators.addImageQualityIndicators(xsDataImageQualityIndicators)

            for (edPluginControlDozor, listBatch) in listPluginDozor:
                edPluginControlDozor.synchronize()
                # Check that we got at least one result
                if len(edPluginControlDozor.dataOutput.imageDozor) == 0:
                    # Run the dozor plugin again, this time synchronously
                    firstImage = os.path.basename(listBatch[0].path.value)
                    lastImage = os.path.basename(listBatch[-1].path.value)
                    self.screen("No dozor results! Re-executing Dozor for images {0} to {1}".format(firstImage, lastImage))
                    time.sleep(5)
                    edPluginControlDozor = self.loadPlugin(self.strPluginNameControlDozor, "ControlDozor_reexecution_{0}".format(os.path.splitext(firstImage)[0]))
                    xsDataInputControlDozor = XSDataInputControlDozor()
                    for image in listBatch:
                        xsDataInputControlDozor.addImage(XSDataFile(image.path))
                    xsDataInputControlDozor.batchSize = XSDataInteger(batchSize)
                    edPluginControlDozor.dataInput = xsDataInputControlDozor
                    edPluginControlDozor.executeSynchronous()
                for imageDozor in edPluginControlDozor.dataOutput.imageDozor:
                    for xsDataImageQualityIndicators in self.xsDataResultControlImageQualityIndicators.imageQualityIndicators:
                        if xsDataImageQualityIndicators.image.path.value == imageDozor.image.path.value:
                            xsDataImageQualityIndicators.dozor_score = imageDozor.mainScore
                            xsDataImageQualityIndicators.dozorSpotFile = imageDozor.spotFile
                            if imageDozor.spotFile is not None:
                                if os.path.exists(imageDozor.spotFile.path.value):
                                    numpyArray = numpy.loadtxt(imageDozor.spotFile.path.value, skiprows=3)
                                    xsDataImageQualityIndicators.dozorSpotList = XSDataString(base64.b64encode(numpyArray.tostring()))
                                    xsDataImageQualityIndicators.addDozorSpotListShape(XSDataInteger(numpyArray.shape[0]))
                                    if len(numpyArray.shape) > 1:
                                        xsDataImageQualityIndicators.addDozorSpotListShape(XSDataInteger(numpyArray.shape[1]))
                            xsDataImageQualityIndicators.dozorSpotsIntAver = imageDozor.spotsIntAver
                            xsDataImageQualityIndicators.dozorSpotsResolution = imageDozor.spotsResolution
                            xsDataImageQualityIndicators.dozorVisibleResolution = imageDozor.visibleResolution
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
                    if xsDataResultControlImageQualityIndicator.dozor_score.value > 1:
                        xsDataInputReadImageHeader = XSDataInputReadImageHeader()
                        xsDataInputReadImageHeader.image = XSDataFile(xsDataResultControlImageQualityIndicator.image.path)
                        self.edPluginReadImageHeader = self.loadPlugin(self.strPluginReadImageHeaderName)
                        self.edPluginReadImageHeader.dataInput = xsDataInputReadImageHeader
                        self.edPluginReadImageHeader.executeSynchronous()
                        xsDataResultReadImageHeader = self.edPluginReadImageHeader.dataOutput
                        if xsDataResultReadImageHeader is not None:
                            edPluginLabelitIndexing = self.loadPlugin(self.strIndexingLabelitPluginName)
                            xsDataInputLabelitIndexing = XSDataInputLabelitIndexing()
                            xsDataInputLabelitIndexing.image.append(XSDataImage(xsDataResultControlImageQualityIndicator.image.path))
                            edPluginLabelitIndexing.setDataInput(xsDataInputLabelitIndexing)
                            self.listPluginLabelit.append([edPluginLabelitIndexing, xsDataResultControlImageQualityIndicator])
                            edPluginLabelitIndexing.execute()
                for tupleLabelit in self.listPluginLabelit:
                    edPluginLabelitIndexing = tupleLabelit[0]
                    xsDataResultControlImageQualityIndicator = tupleLabelit[1]
                    edPluginLabelitIndexing.synchronize()
                    if not edPluginLabelitIndexing.isFailure() and edPluginLabelitIndexing.dataOutput is not None:
                        xsDataResultLabelitIndexing = edPluginLabelitIndexing.getDataOutput()
                        xsDataIndexingResult = EDHandlerXSDataPhenixv1_1.generateXSDataIndexingResult(xsDataResultLabelitIndexing)
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

    def getH5FilePath(self, filePath, batchSize=1, isFastMesh=False):
        imageNumber = EDUtilsImage.getImageNumber(filePath)
        prefix = EDUtilsImage.getPrefix(filePath)
        if isFastMesh:
            h5ImageNumber = int((imageNumber - 1) / 100) + 1
            h5FileNumber = 1
        else:
            h5ImageNumber = 1
            h5FileNumber = int((imageNumber - 1) / batchSize) * batchSize + 1
        h5MasterFileName = "{prefix}_{h5FileNumber}_master.h5".format(prefix=prefix,
                                                                      h5FileNumber=h5FileNumber)
        h5MasterFilePath = os.path.join(os.path.dirname(filePath), h5MasterFileName)
        h5DataFileName = "{prefix}_{h5FileNumber}_data_{h5ImageNumber:06d}.h5".format(prefix=prefix,
                                                                                      h5FileNumber=h5FileNumber,
                                                                                      h5ImageNumber=h5ImageNumber)
        h5DataFilePath = os.path.join(os.path.dirname(filePath), h5DataFileName)
        return h5MasterFilePath, h5DataFilePath, h5FileNumber
