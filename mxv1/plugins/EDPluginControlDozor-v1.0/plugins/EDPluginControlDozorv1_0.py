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

from EDPluginControl import EDPluginControl
from EDUtilsImage import EDUtilsImage
from EDUtilsPath import EDUtilsPath

from EDFactoryPlugin import edFactoryPlugin

from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

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
                xsDataControlImageDozor.mainScore = xsDataResultDozor.mainScore
                xsDataControlImageDozor.spotScore = xsDataResultDozor.spotScore
                xsDataControlImageDozor.visibleResolution = xsDataResultDozor.visibleResolution
                xsDataResultControlDozor.addImageDozor(xsDataControlImageDozor)
                if xsDataResultControlDozor.inputDozor is None:
                    xsDataResultControlDozor.inputDozor = XSDataDozorInput().parseString(xsDataInputDozor.marshal())
                indexImage += 1
            xsDataResultControlDozor.halfDoseTime = edPluginDozor.dataOutput.halfDoseTime
        self.dataOutput = xsDataResultControlDozor

    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlDozorv1_0.postProcess")
        # Write a file to be used with ISPyB or GNUPLOT
        if len(self.dataOutput.imageDozor) > 1:
            with open(os.path.join(self.getWorkingDirectory(), "gnuplot.dat"), "w") as gnuplotFile:
                gnuplotFile.write("# Data directory: {0}\n".format(self.directory))
                gnuplotFile.write("# File template: {0}\n".format(self.template))
                gnuplotFile.write("# {0:>8s}{1:>15s}{2:>15s}{3:>15s}\n".format("'Image no'",
                                                                               "'Main score'",
                                                                               "'Spot score'",
                                                                               "'Visible res.'",
                                                               ))
                for imageDozor in self.dataOutput.imageDozor:
                    gnuplotFile.write("{0:10d}{1:15.3f}{2:15.3f}{3:15.3f}\n".format(imageDozor.number.value,
                                                                                    imageDozor.mainScore.value,
                                                                                    imageDozor.spotScore.value,
                                                                                    imageDozor.visibleResolution.value,
                                                                                    ))
            gnuplotFile.close()
            gnuplotScript = \
"""#
set terminal png
set output "dozor.png"
set grid x y2
set xlabel "Image number"
set y2label "Resolution (A)"
set ylabel "Dozor score"
set autoscale  x
set autoscale  y
set autoscale y2
plot 'gnuplot.dat' using 0:2 title "Dozor score" axes x1y1 with points, 'gnuplot.dat' using 0:4 title "Visible resolution" axes x1y2 with lines
"""
            pathGnuplotScript = os.path.join(self.getWorkingDirectory(), "gnuplot.sh")
            data_file = open(pathGnuplotScript, "w")
            data_file.write(gnuplotScript)
            data_file.close()
            oldCwd = os.getcwd()
            os.chdir(self.getWorkingDirectory())
            os.system("gnuplot %s" % pathGnuplotScript)
            os.chdir(oldCwd)




    def createImageDict(self, _xsDataControlDozorInput):
        # Create dictionary of all images with the image number as key
        dictImage = {}
        if len(_xsDataControlDozorInput.image) > 0:
            listImage = _xsDataControlDozorInput.image
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
