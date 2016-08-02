# coding: utf8
#
#    Project: MXv1
#             http://www.edna-site.org
#
#    Copyright (C) ESRF
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
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os
import shutil

from EDPluginControl import EDPluginControl
from EDUtilsImage import EDUtilsImage
from EDUtilsPath import EDUtilsPath

from EDHandlerESRFPyarchv1_0 import EDHandlerESRFPyarchv1_0
from EDFactoryPlugin import edFactoryPlugin

from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataImage

from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataDozorv1_0")
from XSDataDozorv1_0 import XSDataInputDozor

from XSDataMXv1 import XSDataInputReadImageHeader

from XSDataControlDozorv1_0 import XSDataInputControlDozor
from XSDataControlDozorv1_0 import XSDataResultControlDozor
from XSDataControlDozorv1_0 import XSDataControlImageDozor
from XSDataControlDozorv1_0 import XSDataDozorInput

edFactoryPlugin.loadModule('XSDataISPyBv1_4')
from XSDataISPyBv1_4 import XSDataInputRetrieveDataCollection
from XSDataISPyBv1_4 import XSDataInputISPyBSetImageQualityIndicatorsPlot
from XSDataISPyBv1_4 import XSDataInputRetrieveDataCollection


class EDPluginControlDozorv1_0(EDPluginControl):
    """
    This plugin runs the Dozor program written by Sasha Popov
    """


    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputControlDozor)
        self.setDataOutput(XSDataResultControlDozor())
        self.strEDPluginControlReadImageHeaderName = "EDPluginControlReadImageHeaderv10"
        self.edPluginControlReadImageHeader = None
        self.strEDPluginDozorName = "EDPluginDozorv1_0"
        self.edPluginDozor = None
        self.xsDataControlDozorInput = None
        self.directory = None
        self.template = None
        self.maxBatchSize = 5000


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlDozorv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlDozorv1_0.preProcess")
        self.edPluginControlReadImageHeader = self.loadPlugin(self.strEDPluginControlReadImageHeaderName, "SubWedgeAssemble")
        self.edPluginDozor = self.loadPlugin(self.strEDPluginDozorName, "Dozor")




    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlDozorv1_0.process")
        xsDataResultControlDozor = XSDataResultControlDozor()
        # Check if connection to ISPyB needed
        if self.dataInput.dataCollectionId is not None:
            edPluginRetrieveDataCollection = self.loadPlugin("EDPluginISPyBRetrieveDataCollectionv1_4")
            xsDataInputRetrieveDataCollection = XSDataInputRetrieveDataCollection()
            xsDataInputRetrieveDataCollection.dataCollectionId = self.dataInput.dataCollectionId
            edPluginRetrieveDataCollection.dataInput = xsDataInputRetrieveDataCollection
            edPluginRetrieveDataCollection.executeSynchronous()
            ispybDataCollection = edPluginRetrieveDataCollection.dataOutput.dataCollection
            batchSize = ispybDataCollection.numberOfImages
            if batchSize > self.maxBatchSize:
                batchSize = self.maxBatchSize
            dictImage = self.createImageDictFromISPyB(ispybDataCollection)
        else:
            # No connection to ISPyB, take parameters from input
            if self.dataInput.batchSize is None:
                batchSize = 1
            else:
                batchSize = self.dataInput.batchSize.value
            dictImage = self.createImageDict(self.dataInput)
        listAllBatches = self.createListOfBatches(dictImage.keys(), batchSize)
        for listBatch in listAllBatches:
            # Read the header from the first image in the batch
            xsDataFile = dictImage[listBatch[0]]
            edPluginControlReadImageHeader = self.loadPlugin(self.strEDPluginControlReadImageHeaderName)
            xsDataInputReadImageHeader = XSDataInputReadImageHeader()
            xsDataInputReadImageHeader.image = xsDataFile
            edPluginControlReadImageHeader.dataInput = xsDataInputReadImageHeader
            edPluginControlReadImageHeader.executeSynchronous()
            subWedge = edPluginControlReadImageHeader.dataOutput.subWedge
            xsDataInputDozor = XSDataInputDozor()
            beam = subWedge.experimentalCondition.beam
            detector = subWedge.experimentalCondition.detector
            goniostat = subWedge.experimentalCondition.goniostat
            xsDataInputDozor.detectorType = detector.type
            xsDataInputDozor.exposureTime = XSDataDouble(beam.exposureTime.value)
            xsDataInputDozor.spotSize = XSDataInteger(3)
            xsDataInputDozor.detectorDistance = XSDataDouble(detector.distance.value)
            xsDataInputDozor.wavelength = XSDataDouble(beam.wavelength.value)
#            xsDataInputDozor.fractionPolatization : XSDataDouble optional
            orgx = detector.beamPositionY.value / detector.pixelSizeY.value
            orgy = detector.beamPositionX.value / detector.pixelSizeX.value
            xsDataInputDozor.orgx = XSDataDouble(orgx)
            xsDataInputDozor.orgy = XSDataDouble(orgy)
            xsDataInputDozor.oscillationRange = XSDataDouble(goniostat.oscillationWidth.value)
#            xsDataInputDozor.imageStep : XSDataDouble optional
            xsDataInputDozor.startingAngle = XSDataDouble(goniostat.rotationAxisStart.value)
            xsDataInputDozor.firstImageNumber = subWedge.image[0].number
            xsDataInputDozor.numberImages = XSDataInteger(len(listBatch))
            strFileName = subWedge.image[0].path.value
            strPrefix = EDUtilsImage.getPrefix(strFileName)
            strSuffix = EDUtilsImage.getSuffix(strFileName)
            if EDUtilsPath.isEMBL():
                strXDSTemplate = "%s_?????.%s" % (strPrefix, strSuffix)
            else:
                strXDSTemplate = "%s_????.%s" % (strPrefix, strSuffix)
            xsDataInputDozor.nameTemplateImage = XSDataString(os.path.join(os.path.dirname(strFileName), strXDSTemplate))
            xsDataInputDozor.wedgeNumber = self.dataInput.wedgeNumber
            xsDataInputDozor.radiationDamage = self.dataInput.radiationDamage
            edPluginDozor = self.loadPlugin(self.strEDPluginDozorName, "Dozor_%05d" % subWedge.image[0].number.value)
            edPluginDozor.dataInput = xsDataInputDozor
            edPluginDozor.executeSynchronous()
            indexImage = 0
            for xsDataResultDozor in edPluginDozor.dataOutput.imageDozor:
                xsDataControlImageDozor = XSDataControlImageDozor()
                xsDataControlImageDozor.number = xsDataResultDozor.number
                xsDataControlImageDozor.image = dictImage[listBatch[indexImage]]
                xsDataControlImageDozor.spotsNumOf = xsDataResultDozor.spotsNumOf
                xsDataControlImageDozor.spotsIntAver = xsDataResultDozor.spotsIntAver
                xsDataControlImageDozor.spotsResolution = xsDataResultDozor.spotsResolution
                xsDataControlImageDozor.powderWilsonScale = xsDataResultDozor.powderWilsonScale
                xsDataControlImageDozor.powderWilsonBfactor = xsDataResultDozor.powderWilsonBfactor
                xsDataControlImageDozor.powderWilsonResolution = xsDataResultDozor.powderWilsonResolution
                xsDataControlImageDozor.powderWilsonCorrelation = xsDataResultDozor.powderWilsonCorrelation
                xsDataControlImageDozor.powderWilsonRfactor = xsDataResultDozor.powderWilsonRfactor
                xsDataControlImageDozor.mainScore = xsDataResultDozor.mainScore
                xsDataControlImageDozor.spotScore = xsDataResultDozor.spotScore
                xsDataControlImageDozor.visibleResolution = xsDataResultDozor.visibleResolution
                xsDataControlImageDozor.spotFile = xsDataResultDozor.spotFile
                xsDataResultControlDozor.addImageDozor(xsDataControlImageDozor)
                if xsDataResultControlDozor.inputDozor is None:
                    xsDataResultControlDozor.inputDozor = XSDataDozorInput().parseString(xsDataInputDozor.marshal())
                indexImage += 1
            xsDataResultControlDozor.halfDoseTime = edPluginDozor.dataOutput.halfDoseTime
        self.dataOutput = xsDataResultControlDozor

    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlDozorv1_0.postProcess")
        # Write a file to be used with ISPyB or GNUPLOT only if data collection id in input
        dataCollectionId = None
        if self.dataInput.dataCollectionId is None and len(self.dataInput.image) > 0:
            xsDataInputRetrieveDataCollection = XSDataInputRetrieveDataCollection()
            xsDataInputRetrieveDataCollection.image = XSDataImage(self.dataInput.image[0].path)
            edPluginISPyBRetrieveDataCollection = self.loadPlugin("EDPluginISPyBRetrieveDataCollectionv1_4")
            edPluginISPyBRetrieveDataCollection.dataInput = xsDataInputRetrieveDataCollection
            edPluginISPyBRetrieveDataCollection.executeSynchronous()
            xsDataResultRetrieveDataCollection = edPluginISPyBRetrieveDataCollection.dataOutput
            if xsDataResultRetrieveDataCollection is not None:
                dataCollection = xsDataResultRetrieveDataCollection.dataCollection
                if dataCollection is not None:
                    dataCollectionId = dataCollection.dataCollectionId
        else:
            dataCollectionId = self.dataInput.dataCollectionId.value

        if dataCollectionId is not None:
            dozorPlotFileName = "dozor_{0}.png".format(dataCollectionId)
            dozorCsvFileName = "dozor_{0}.csv".format(dataCollectionId)
            with open(os.path.join(self.getWorkingDirectory(), dozorCsvFileName), "w") as gnuplotFile:
                gnuplotFile.write("# Data directory: {0}\n".format(self.directory))
                gnuplotFile.write("# File template: {0}\n".format(self.template.replace("%04d", "####")))
                gnuplotFile.write("# {0:>9s}{1:>16s}{2:>16s}{3:>16s}{4:>16s}\n".format("'Image no'",
                                                                               "'No of spots'",
                                                                               "'Main score'",
                                                                               "'Spot score'",
                                                                               "'Visible res.'",
                                                               ))
                for imageDozor in self.dataOutput.imageDozor:
                    gnuplotFile.write("{0:10d},{1:15d},{2:15.3f},{3:15.3f},{4:15.3f}\n".format(imageDozor.number.value,
                                                                                               imageDozor.spotsNumOf.value,
                                                                                               imageDozor.mainScore.value,
                                                                                               imageDozor.spotScore.value,
                                                                                               imageDozor.visibleResolution.value,
                                                                                               ))
            gnuplotFile.close()
            gnuplotScript = \
    """#
    set terminal png
    set output '{dozorPlotFileName}'
    set title '{title}'
    set grid x y2
    set xlabel 'Image number'
    set y2label 'Resolution (A)'
    set ylabel 'Number of spots / Dozor score'
    set ytics nomirror
    set y2tics
    set autoscale  x
    set autoscale  y
    set y2range [4.5: 0.8]
    set key below
    plot '{dozorCsvFileName}' using 1:2 title 'Number of spots' axes x1y1 with points linetype rgb 'goldenrod' pointtype 7 pointsize 1.5, \
     '{dozorCsvFileName}' using 1:3 title 'Dozor score' axes x1y1 with points linetype 3 pointtype 7 pointsize 1.5, \
     '{dozorCsvFileName}' using 1:5 title 'Visible resolution' axes x1y2 with points linetype 1 pointtype 7 pointsize 1.5
    """.format(title=self.template.replace("%04d", "####"),
               dozorPlotFileName=dozorPlotFileName,
               dozorCsvFileName=dozorCsvFileName)
            pathGnuplotScript = os.path.join(self.getWorkingDirectory(), "gnuplot.sh")
            data_file = open(pathGnuplotScript, "w")
            data_file.write(gnuplotScript)
            data_file.close()
            oldCwd = os.getcwd()
            os.chdir(self.getWorkingDirectory())
            os.system("gnuplot %s" % pathGnuplotScript)
            os.chdir(oldCwd)
            if self.dataInput.processDirectory is not None:
                processDirectory = self.dataInput.processDirectory.path.value
            else:
                processDirectory = os.path.join(self.directory.replace("RAW_DATA", "PROCESSED_DATA"), "DozorPlot")
            resultsDirectory = os.path.join(processDirectory, "results")
            if not os.path.exists(resultsDirectory):
                os.makedirs(resultsDirectory, 0755)
            dozorPlotResultPath = os.path.join(resultsDirectory, dozorPlotFileName)
            dozorCsvResultPath = os.path.join(resultsDirectory, dozorCsvFileName)
            shutil.copy(os.path.join(self.getWorkingDirectory(), dozorPlotFileName), dozorPlotResultPath)
            shutil.copy(os.path.join(self.getWorkingDirectory(), dozorCsvFileName), dozorCsvResultPath)
            # Create paths on pyarch
            dozorPlotPyarchPath = EDHandlerESRFPyarchv1_0.createPyarchFilePath(dozorPlotResultPath)
            dozorCsvPyarchPath = EDHandlerESRFPyarchv1_0.createPyarchFilePath(dozorCsvResultPath)
            try:
                if not os.path.exists(os.path.dirname(dozorPlotPyarchPath)):
                    os.makedirs(os.path.dirname(dozorPlotPyarchPath), 0755)
                shutil.copy(dozorPlotResultPath, dozorPlotPyarchPath)
                shutil.copy(dozorCsvResultPath, dozorCsvPyarchPath)
                # Upload to data collection
                xsDataInputISPyBSetImageQualityIndicatorsPlot = XSDataInputISPyBSetImageQualityIndicatorsPlot()
                xsDataInputISPyBSetImageQualityIndicatorsPlot.dataCollectionId = XSDataInteger(dataCollectionId)
                xsDataInputISPyBSetImageQualityIndicatorsPlot.imageQualityIndicatorsPlotPath = XSDataString(dozorPlotPyarchPath)
                xsDataInputISPyBSetImageQualityIndicatorsPlot.imageQualityIndicatorsCSVPath = XSDataString(dozorCsvPyarchPath)
                EDPluginISPyBSetImageQualityIndicatorsPlot = self.loadPlugin("EDPluginISPyBSetImageQualityIndicatorsPlotv1_4")
                EDPluginISPyBSetImageQualityIndicatorsPlot.dataInput = xsDataInputISPyBSetImageQualityIndicatorsPlot
                EDPluginISPyBSetImageQualityIndicatorsPlot.executeSynchronous()
            except:
                self.warning("Couldn't copy files to pyarch")



    def createImageDict(self, _xsDataControlDozorInput):
        # Create dictionary of all images with the image number as key
        dictImage = {}
        if len(_xsDataControlDozorInput.image) > 0:
            listImage = _xsDataControlDozorInput.image
            pathToFirstImage = listImage[0].path.value
            self.directory = os.path.dirname(pathToFirstImage)
            self.template = os.path.basename(pathToFirstImage).replace("0001", "####")
        else:
            # Create list of images
            listImage = []
            self.directory = _xsDataControlDozorInput.directory.path.value
            self.template = _xsDataControlDozorInput.template.value
            startNo = _xsDataControlDozorInput.startNo.value
            endNo = _xsDataControlDozorInput.endNo.value
            for imageIndex in range(startNo, endNo + 1):
                imageName = self.template % imageIndex
                imagePath = os.path.join(self.directory, imageName)
                listImage.append(XSDataFile(XSDataString(imagePath)))
        for image in listImage:
            imagePath = image.path.value
            imageNo = EDUtilsImage.getImageNumber(imagePath)
            dictImage[imageNo] = image
        return dictImage

    def createImageDictFromISPyB(self, _ispybDataCollection):
        # Create dictionary of all images with the image number as key
        dictImage = {}
        # Create list of images
        listImage = []
        self.directory = _ispybDataCollection.imageDirectory
        self.template = _ispybDataCollection.fileTemplate
        startNo = _ispybDataCollection.startImageNumber
        endNo = _ispybDataCollection.startImageNumber + _ispybDataCollection.numberOfImages - 1
        for imageIndex in range(startNo, endNo + 1):
            imageName = self.template % imageIndex
            imagePath = os.path.join(self.directory, imageName)
            listImage.append(XSDataFile(XSDataString(imagePath)))
        for image in listImage:
            imagePath = image.path.value
            imageNo = EDUtilsImage.getImageNumber(imagePath)
            dictImage[imageNo] = image
        return dictImage


    def createListOfBatches(self, listImage, batchSize):
        # Create the list of batches containing the image no
        listAllBatches = []
        listImagesInBatch = []
        indexBatch = 0
        indexNextImageInBatch = None
        listImageSorted = sorted(listImage)
        for imageNo in listImageSorted:
            if indexNextImageInBatch is None:
                # This image can be appended to this batch
                indexBatch = 1
                indexNextImageInBatch = imageNo + 1
                listImagesInBatch.append(imageNo)
                if batchSize == 1:
                    listAllBatches.append(listImagesInBatch)
                    listImagesInBatch = []
                    indexNextImageInBatch = None
            elif imageNo != indexNextImageInBatch or indexBatch == batchSize:
                # A new batch must be started
                indexBatch = 1
                listAllBatches.append(listImagesInBatch)
                listImagesInBatch = [imageNo]
                indexNextImageInBatch = imageNo + 1
            else:
                # This image can be appended to this batch
                listImagesInBatch.append(imageNo)
                indexNextImageInBatch += 1
                indexBatch += 1
        if listImagesInBatch != []:
            listAllBatches.append(listImagesInBatch)
        return listAllBatches
