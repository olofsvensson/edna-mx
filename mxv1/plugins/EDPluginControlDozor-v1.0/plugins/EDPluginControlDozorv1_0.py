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

from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString

from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataDozorv1_0")
from XSDataDozorv1_0 import XSDataInputDozor

from XSDataMXv1 import XSDataInputReadImageHeader

from XSDataControlDozorv1_0 import XSDataInputControlDozor
from XSDataControlDozorv1_0 import XSDataResultControlDozor
from XSDataControlDozorv1_0 import XSDataControlImageDozor
from XSDataControlDozorv1_0 import XSDataDozorInput


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
        if self.dataInput.batchSize is None:
            batchSize = 1
        else:
            batchSize = self.dataInput.batchSize.value
        dictImage = self.createImageDict(self.dataInput.image)
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
            xsDataInputDozor.oscillationRange = XSDataDouble(goniostat.oscillationWidth.value * len(listBatch))
#            xsDataInputDozor.imageStep : XSDataDouble optional
            xsDataInputDozor.startingAngle = XSDataDouble(goniostat.rotationAxisStart.value)
            xsDataInputDozor.firstImageNumber = subWedge.image[0].number
            xsDataInputDozor.numberImages = XSDataInteger(len(listBatch))
            strFileName = subWedge.image[0].path.value
            strPrefix = EDUtilsImage.getPrefix(strFileName)
            strSuffix = EDUtilsImage.getSuffix(strFileName)
            strXDSTemplate = "%s_????.%s" % (strPrefix, strSuffix)
            xsDataInputDozor.nameTemplateImage = XSDataString(os.path.join(os.path.dirname(strFileName), strXDSTemplate))
            edPluginDozor = self.loadPlugin(self.strEDPluginDozorName, "Dozor_%05d" % subWedge.image[0].number.value)
            edPluginDozor.dataInput = xsDataInputDozor
            edPluginDozor.executeSynchronous()
            indexImage = 0
            for xsDataResultDozor in edPluginDozor.dataOutput.imageDozor:
                xsDataControlImageDozor = XSDataControlImageDozor()
                xsDataControlImageDozor.image = dictImage[listBatch[indexImage]]
                xsDataControlImageDozor.spots_num_of = xsDataResultDozor.spots_num_of
                xsDataControlImageDozor.spots_int_aver = xsDataResultDozor.spots_int_aver
                xsDataControlImageDozor.spots_resolution = xsDataResultDozor.spots_resolution
                xsDataControlImageDozor.powder_wilson_scale = xsDataResultDozor.powder_wilson_scale
                xsDataControlImageDozor.powder_wilson_bfactor = xsDataResultDozor.powder_wilson_bfactor
                xsDataControlImageDozor.powder_wilson_resolution = xsDataResultDozor.powder_wilson_resolution
                xsDataControlImageDozor.powder_wilson_correlation = xsDataResultDozor.powder_wilson_correlation
                xsDataControlImageDozor.powder_wilson_rfactor = xsDataResultDozor.powder_wilson_rfactor
                xsDataControlImageDozor.score = xsDataResultDozor.score
                xsDataControlImageDozor.spotFile = xsDataResultDozor.spotFile
                xsDataResultControlDozor.addImageDozor(xsDataControlImageDozor)
                if xsDataResultControlDozor.inputDozor is None:
                    xsDataResultControlDozor.inputDozor = XSDataDozorInput().parseString(xsDataInputDozor.marshal())
                indexImage += 1
        self.dataOutput = xsDataResultControlDozor


    def createImageDict(self, listImage):
        # Create dictionary of all images with the image number as key
        dictImage = {}
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
