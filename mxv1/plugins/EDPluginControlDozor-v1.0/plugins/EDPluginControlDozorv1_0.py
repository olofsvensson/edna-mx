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
import sys
import numpy
import shutil
import base64
import tempfile
try:
    from xmlrpclib import ServerProxy
except:
    from xmlrpc.client import ServerProxy

from EDPluginControl import EDPluginControl
from EDUtilsImage import EDUtilsImage
from EDUtilsPath import EDUtilsPath

from EDHandlerESRFPyarchv1_0 import EDHandlerESRFPyarchv1_0
from EDFactoryPlugin import edFactoryPlugin
from EDUtilsParallel import EDUtilsParallel

from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataAngle

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

edFactoryPlugin.loadModule('XSDataH5ToCBFv1_1')
from XSDataH5ToCBFv1_1 import XSDataInputH5ToCBF



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
        self.hasHdf5Prefix = False
        self.cbfTempDir = None
        self.hasOverlap = False
        self.overlap = 0.0
        self.batchSize = None
        self.hdf5BatchSize = None
        self._strMxCuBE_URI = None
        self._oServerProxy = None
        self.doRadiationDamage = False
        self.gnuplot = "gnuplot"
        self.doISPyBUpload = False


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlDozorv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")

    def configure(self):
        EDPluginControl.configure(self)
        self.batchSize = self.config.get("batchSize")
        self.hdf5BatchSize = self.config.get("hdf5BatchSize")

        self._strMxCuBE_URI = self.config.get("mxCuBE_URI", None)
        if self._strMxCuBE_URI is not None:
            self.DEBUG("Enabling sending messages to mxCuBE via URI {0}".format(self._strMxCuBE_URI))
            self._oServerProxy = ServerProxy(self._strMxCuBE_URI)

        self.gnuplot = self.config.get("gnuplot", self.gnuplot)


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlDozorv1_0.preProcess")
        self.edPluginControlReadImageHeader = self.loadPlugin(self.strEDPluginControlReadImageHeaderName, "SubWedgeAssemble")
        if self.dataInput.batchSize is not None:
            self.batchSize = self.dataInput.batchSize.value
        if self.dataInput.radiationDamage is not None:
            self.doRadiationDamage = self.dataInput.radiationDamage.value
        if self.dataInput.doISPyBUpload is not None:
            if self.dataInput.doISPyBUpload.value:
                self.doISPyBUpload = True


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlDozorv1_0.process")
        self.sendMessageToMXCuBE("Processing started...", "info")
        EDUtilsParallel.initializeNbThread()
        xsDataResultControlDozor = XSDataResultControlDozor()
        # Check if connection to ISPyB needed
        if self.dataInput.dataCollectionId is not None:
            edPluginRetrieveDataCollection = self.loadPlugin("EDPluginISPyBRetrieveDataCollectionv1_4")
            xsDataInputRetrieveDataCollection = XSDataInputRetrieveDataCollection()
            xsDataInputRetrieveDataCollection.dataCollectionId = self.dataInput.dataCollectionId
            edPluginRetrieveDataCollection.dataInput = xsDataInputRetrieveDataCollection
            edPluginRetrieveDataCollection.executeSynchronous()
            ispybDataCollection = edPluginRetrieveDataCollection.dataOutput.dataCollection
            if self.batchSize is None:
                batchSize = ispybDataCollection.numberOfImages
            else:
                batchSize = self.batchSize
            if batchSize > self.maxBatchSize:
                batchSize = self.maxBatchSize
            if abs(ispybDataCollection.overlap) > 1:
                self.hasOverlap = True
                self.overlap = ispybDataCollection.overlap
            dictImage = self.createImageDictFromISPyB(ispybDataCollection)
        else:
            # No connection to ISPyB, take parameters from input
            if self.dataInput.batchSize is None:
                batchSize = self.maxBatchSize
            else:
                batchSize = self.dataInput.batchSize.value
            dictImage = self.createImageDict(self.dataInput)
        self.screen("Dozor batch size: {0}".format(batchSize))
        if self.dataInput.hdf5BatchSize is not None:
            self.hdf5BatchSize = self.dataInput.hdf5BatchSize.value
        listAllBatches = self.createListOfBatches(dictImage.keys(), batchSize)
        if dictImage[listAllBatches[0][0]].path.value.endswith("h5"):
            # Convert HDF5 images to CBF
            self.screen("HDF5 converter batch size: {0}".format(self.batchSize))
            if self.doRadiationDamage:
                self.cbfTempDir = None
            else:
                self.cbfTempDir = tempfile.mkdtemp(prefix="CbfTemp_")
            listHdf5Batches = self.createListOfBatches(dictImage.keys(), self.batchSize)
            dictImage, self.hasHdf5Prefix = self.convertToCBF(dictImage, listHdf5Batches, self.doRadiationDamage)
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
            if self.hasOverlap:
                xsDataInputDozor.overlap = XSDataAngle(self.overlap)
            strFileName = subWedge.image[0].path.value
            strPrefix = EDUtilsImage.getPrefix(strFileName)
            strSuffix = EDUtilsImage.getSuffix(strFileName)
            if EDUtilsPath.isEMBL():
                strXDSTemplate = "%s_?????.%s" % (strPrefix, strSuffix)
            elif self.hasHdf5Prefix and not self.hasOverlap:
                strXDSTemplate = "%s_??????.%s" % (strPrefix, strSuffix)
            else:
                strXDSTemplate = "%s_????.%s" % (strPrefix, strSuffix)
            xsDataInputDozor.nameTemplateImage = XSDataString(os.path.join(os.path.dirname(strFileName), strXDSTemplate))
            xsDataInputDozor.wedgeNumber = self.dataInput.wedgeNumber
            xsDataInputDozor.radiationDamage = self.dataInput.radiationDamage
            edPluginDozor = self.loadPlugin(self.strEDPluginDozorName, "Dozor_%05d" % subWedge.image[0].number.value)
            edPluginDozor.dataInput = xsDataInputDozor
            edPluginDozor.execute()
            edPluginDozor.synchronize()
            indexImage = 0
            imageDozorBatchList = []

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
                xsDataControlImageDozor.angle = xsDataResultDozor.angle
                xsDataResultControlDozor.addImageDozor(xsDataControlImageDozor)
                if xsDataResultControlDozor.inputDozor is None:
                    xsDataResultControlDozor.inputDozor = XSDataDozorInput().parseString(xsDataInputDozor.marshal())
                indexImage += 1

                dozorSpotListShape = []
                dozorSpotList = []
                spotFile = None
                if xsDataControlImageDozor.spotFile is not None:
                    spotFile = xsDataControlImageDozor.spotFile.path.value
                    if os.path.exists(spotFile):
                        numpyArray = numpy.loadtxt(spotFile, skiprows=3)
                        dozorSpotList = base64.b64encode(numpyArray.tostring())
                        dozorSpotListShape.append(numpyArray.shape[0])
                        if len(numpyArray.shape) > 1:
                            dozorSpotListShape.append(numpyArray.shape[1])

                imageDozorDict = {"index": xsDataControlImageDozor.number.value,
                                  "imageName": xsDataControlImageDozor.image.path.value,
                                  "dozor_score": xsDataControlImageDozor.mainScore.value,
                                  "dozorSpotsNumOf" : xsDataControlImageDozor.spotsNumOf.value,
                                  "dozorSpotFile": spotFile,
                                  "dozorSpotList" : dozorSpotList,
                                  "dozorSpotListShape": dozorSpotListShape,
                                  "dozorSpotsIntAver": xsDataControlImageDozor.spotsIntAver.value,
                                  "dozorSpotsResolution": xsDataControlImageDozor.spotsResolution.value
                                  }
                imageDozorBatchList.append(imageDozorDict)

            xsDataResultControlDozor.halfDoseTime = edPluginDozor.dataOutput.halfDoseTime
            xsDataResultControlDozor.pngPlots = edPluginDozor.dataOutput.pngPlots

            self.sendResultToMXCuBE(imageDozorBatchList)
            self.sendMessageToMXCuBE("Batch processed")
        self.dataOutput = xsDataResultControlDozor
        if self.cbfTempDir is not None:
            if self.dataInput.keepCbfTmpDirectory is not None and self.dataInput.keepCbfTmpDirectory.value:
                self.dataOutput.pathToCbfDirectory = XSDataFile(XSDataString(self.cbfTempDir))
            else:
                shutil.rmtree(self.cbfTempDir)

    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlDozorv1_0.postProcess")
        # Write a file to be used with ISPyB or GNUPLOT only if data collection id in input
        dataCollectionId = None
        if self.dataInput.dataCollectionId is None and len(self.dataInput.image) > 0:
            # Only try to obtain data collection id if at the ESRF and path starts with "/data"
            if EDUtilsPath.isESRF() and self.dataInput.image[0].path.value.startswith("/data"):
                xsDataInputRetrieveDataCollection = XSDataInputRetrieveDataCollection()
                # Hack to fix problem with looking for CBF images from ID30A-3 and ID23-1:
                imagePath = self.dataInput.image[0].path.value
                if "id23eh1" in imagePath or "id23eh2" in imagePath or "id30a3" in imagePath or "id30b" in imagePath:
                    imagePath = imagePath.replace(".cbf", ".h5")
                xsDataInputRetrieveDataCollection.image = XSDataImage(XSDataString(imagePath))
                edPluginISPyBRetrieveDataCollection = self.loadPlugin("EDPluginISPyBRetrieveDataCollectionv1_4")
                edPluginISPyBRetrieveDataCollection.dataInput = xsDataInputRetrieveDataCollection
                edPluginISPyBRetrieveDataCollection.executeSynchronous()
                xsDataResultRetrieveDataCollection = edPluginISPyBRetrieveDataCollection.dataOutput
                if xsDataResultRetrieveDataCollection is not None:
                    dataCollection = xsDataResultRetrieveDataCollection.dataCollection
                    if dataCollection is not None:
                        dataCollectionId = dataCollection.dataCollectionId
        elif self.dataInput.dataCollectionId is not None:
            dataCollectionId = self.dataInput.dataCollectionId.value

        if dataCollectionId is not None:
            minImageNumber = None
            maxImageNumber = None
            minAngle = None
            maxAngle = None
            minDozorValue = None
            maxDozorValue = None
            minResolution = None
            maxResolution = None
            dozorPlotFileName = "dozor_{0}.png".format(dataCollectionId)
            dozorCsvFileName = "dozor_{0}.csv".format(dataCollectionId)
            with open(os.path.join(self.getWorkingDirectory(), dozorCsvFileName), "w") as gnuplotFile:
                gnuplotFile.write("# Data directory: {0}\n".format(self.directory))
                gnuplotFile.write("# File template: {0}\n".format(self.template.replace("%04d", "####")))
                gnuplotFile.write("# {0:>9s}{1:>16s}{2:>16s}{3:>16s}{4:>16s}{5:>16s}\n".format("'Image no'",
                                                                               "'Angle'",
                                                                               "'No of spots'",
                                                                               "'Main score (*10)'",
                                                                               "'Spot score'",
                                                                               "'Visible res.'",
                                                               ))
                for imageDozor in self.dataOutput.imageDozor:
                    gnuplotFile.write("{0:10d},{1:15.3f},{2:15d},{3:15.3f},{4:15.3f},{5:15.3f}\n".format(imageDozor.number.value,
                                                                                                       imageDozor.angle.value,
                                                                                                       imageDozor.spotsNumOf.value,
                                                                                                       10 * imageDozor.mainScore.value,
                                                                                                       imageDozor.spotScore.value,
                                                                                                       imageDozor.visibleResolution.value,
                                                                                                       ))
                    if minImageNumber is None or minImageNumber > imageDozor.number.value:
                        minImageNumber = imageDozor.number.value
                        minAngle = imageDozor.angle.value
                    if maxImageNumber is None or maxImageNumber < imageDozor.number.value:
                        maxImageNumber = imageDozor.number.value
                        maxAngle = imageDozor.angle.value
                    if minDozorValue is None or minDozorValue > imageDozor.mainScore.value:
                        minDozorValue = imageDozor.spotScore.value
                    if maxDozorValue is None or maxDozorValue < imageDozor.mainScore.value:
                        maxDozorValue = imageDozor.spotScore.value

                    # Min resolution: the higher the value the lower the resolution
                    if minResolution is None or minResolution < imageDozor.visibleResolution.value:
                        # Disregard resolution worse than 10.0
                        if imageDozor.visibleResolution.value < 10.0:
                            minResolution = imageDozor.visibleResolution.value

                    # Max resolution: the lower the number the better the resolution
                    if maxResolution is None or maxResolution > imageDozor.visibleResolution.value:
                        maxResolution = imageDozor.visibleResolution.value

            xtics = ""
            if minImageNumber is not None and minImageNumber == maxImageNumber:
                minAngle -= 1.0
                maxAngle += 1.0
            noImages = maxImageNumber - minImageNumber + 1
            if noImages <= 4:
                minImageNumber -= 0.1
                maxImageNumber += 0.1
                deltaAngle = maxAngle - minAngle
                minAngle -= deltaAngle * 0.1 / noImages
                maxAngle += deltaAngle * 0.1 / noImages
                xtics = "1"

            if maxResolution is None or maxResolution > 0.8:
                maxResolution = 0.8
            else:
                maxResolution = int(maxResolution * 10.0) / 10.0

            if minResolution is None or minResolution < 4.5:
                minResolution = 4.5
            else:
                minResolution = int(minResolution * 10.0) / 10.0 + 1

            if maxDozorValue < 0.001 and minDozorValue < 0.001:
                yscale = "set yrange [-0.5:0.5]\n    set ytics 1"
            else:
                yscale = "set autoscale  y"

            gnuplotFile.close()
            gnuplotScript = \
    """#
    set terminal png
    set output '{dozorPlotFileName}'
    set title '{title}'
    set grid x2 y2
    set xlabel 'Image number'
    set x2label 'Angle (degrees)'
    set y2label 'Resolution (A)'
    set ylabel 'Number of spots / Dozor score (*10)'
    set xtics {xtics} nomirror
    set x2tics 
    set ytics nomirror
    set y2tics
    set xrange [{minImageNumber}:{maxImageNumber}]
    set x2range [{minAngle}:{maxAngle}]
    {yscale}
    set y2range [{minResolution}:{maxResolution}]
    set key below
    plot '{dozorCsvFileName}' using 1:3 title 'Number of spots' axes x1y1 with points linetype rgb 'goldenrod' pointtype 7 pointsize 1.5, \
         '{dozorCsvFileName}' using 1:4 title 'Dozor score' axes x1y1 with points linetype 3 pointtype 7 pointsize 1.5, \
         '{dozorCsvFileName}' using 1:6 title 'Visible resolution' axes x1y2 with points linetype 1 pointtype 7 pointsize 1.5
    """.format(title=self.template.replace("%04d", "####"),
               dozorPlotFileName=dozorPlotFileName,
               dozorCsvFileName=dozorCsvFileName,
               minImageNumber=minImageNumber,
               maxImageNumber=maxImageNumber,
               minAngle=minAngle,
               maxAngle=maxAngle,
               minResolution=minResolution,
               maxResolution=maxResolution,
               xtics=xtics,
               yscale=yscale,
               )
            pathGnuplotScript = os.path.join(self.getWorkingDirectory(), "gnuplot.sh")
            data_file = open(pathGnuplotScript, "w")
            data_file.write(gnuplotScript)
            data_file.close()
            oldCwd = os.getcwd()
            os.chdir(self.getWorkingDirectory())
            os.system("{0} {1}".format(self.gnuplot, pathGnuplotScript))
            os.chdir(oldCwd)

            self.dataOutput.dozorPlot = XSDataFile(XSDataString(os.path.join(self.getWorkingDirectory(), dozorPlotFileName)))

            if self.dataInput.processDirectory is not None:
                processDirectory = self.dataInput.processDirectory.path.value
            else:
                processDirectory = os.path.join(self.directory.replace("RAW_DATA", "PROCESSED_DATA"), "DozorPlot")
            resultsDirectory = os.path.join(processDirectory, "results")
            dozorPlotResultPath = os.path.join(resultsDirectory, dozorPlotFileName)
            dozorCsvResultPath = os.path.join(resultsDirectory, dozorCsvFileName)
            try:
                if not os.path.exists(resultsDirectory):
                    os.makedirs(resultsDirectory, 0o755)
                shutil.copy(os.path.join(self.getWorkingDirectory(), dozorPlotFileName), dozorPlotResultPath)
                shutil.copy(os.path.join(self.getWorkingDirectory(), dozorCsvFileName), dozorCsvResultPath)
            except:
                self.warning("Couldn't copy files to results directory: {0}".format(resultsDirectory))

            if self.doISPyBUpload:
                try:
                    # Create paths on pyarch
                    dozorPlotPyarchPath = EDHandlerESRFPyarchv1_0.createPyarchFilePath(dozorPlotResultPath)
                    dozorCsvPyarchPath = EDHandlerESRFPyarchv1_0.createPyarchFilePath(dozorCsvResultPath)
                    if not os.path.exists(os.path.dirname(dozorPlotPyarchPath)):
                        os.makedirs(os.path.dirname(dozorPlotPyarchPath), 0o755)
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
                    self.warning("Couldn't copy files to pyarch: {0}".format(dozorPlotPyarchPath))

        self.sendMessageToMXCuBE("Processing finished", "info")
        self.setStatusToMXCuBE("Success")


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

    def convertToCBF(self, dictImage, listAllBatches, doRadiationDamage=False):
        # Find start and end image number
        startImage = None
        endImage = None
        for image in dictImage:
            if startImage is None or startImage > image:
                startImage = image
            if endImage is None or endImage < image:
                endImage = image
        # Check if we are dealing with characterisation images
        newDict = {}
        hasHdf5Prefix = True
        if self.hasOverlap or startImage == endImage:
            hasHdf5Prefix = False
            for image in dictImage:
                xsDataInputH5ToCBF = XSDataInputH5ToCBF()
                xsDataInputH5ToCBF.hdf5File = dictImage[startImage]
                xsDataInputH5ToCBF.hdf5ImageNumber = XSDataInteger(image)
                xsDataInputH5ToCBF.imageNumber = XSDataInteger(startImage)
                xsDataInputH5ToCBF.forcedOutputDirectory = XSDataFile(XSDataString(self.cbfTempDir))
                xsDataInputH5ToCBF.forcedOutputImageNumber = XSDataInteger(image)
                edPluginH5ToCBF = self.loadPlugin("EDPluginH5ToCBFv1_1")
                edPluginH5ToCBF.dataInput = xsDataInputH5ToCBF
                edPluginH5ToCBF.executeSynchronous()
                newDict[image] = edPluginH5ToCBF.dataOutput.outputCBFFile
        else:
            listPluginH5ToCBF = []
            directory = os.path.dirname(dictImage[listAllBatches[0][0]].path.value)
            for batch in listAllBatches:
                xsDataInputH5ToCBF = XSDataInputH5ToCBF()
                if doRadiationDamage:
                    xsDataInputH5ToCBF.hdf5File = dictImage[batch[0]]
                    xsDataInputH5ToCBF.hdf5ImageNumber = XSDataInteger(batch[0])
                    xsDataInputH5ToCBF.startImageNumber = XSDataInteger(listAllBatches[0][0])
                    xsDataInputH5ToCBF.endImageNumber = XSDataInteger(listAllBatches[0][-1])
                else:
                    xsDataInputH5ToCBF.hdf5File = dictImage[startImage]
                    xsDataInputH5ToCBF.hdf5ImageNumber = XSDataInteger(1)
                    xsDataInputH5ToCBF.startImageNumber = XSDataInteger(batch[0])
                    xsDataInputH5ToCBF.endImageNumber = XSDataInteger(batch[-1])
                    xsDataInputH5ToCBF.forcedOutputDirectory = XSDataFile(XSDataString(self.cbfTempDir))
                edPluginH5ToCBF = self.loadPlugin("EDPluginH5ToCBFv1_1")
                edPluginH5ToCBF.dataInput = xsDataInputH5ToCBF
                if doRadiationDamage:
                    edPluginH5ToCBF.executeSynchronous()
                    if edPluginH5ToCBF.dataOutput is not None and edPluginH5ToCBF.dataOutput.outputCBFFileTemplate is not None:
                        outputCBFFileTemplate = edPluginH5ToCBF.dataOutput.outputCBFFileTemplate
                        for newImageNumber in batch:
                            oldImageNumber = newImageNumber - batch[0] + 1
                            oldPath = os.path.join(directory, outputCBFFileTemplate.path.value.replace("######", "{0:06d}".format(oldImageNumber)))
                            newPath = os.path.join(directory, outputCBFFileTemplate.path.value.replace("######", "{0:04d}".format(newImageNumber)))
                            os.rename(oldPath, newPath)
                            newDict[newImageNumber] = XSDataFile(XSDataString(newPath))
                    hasHdf5Prefix = False
                else:
                    edPluginH5ToCBF.execute()
                    listPluginH5ToCBF.append(edPluginH5ToCBF)
            for edPluginH5ToCBF in listPluginH5ToCBF:
                edPluginH5ToCBF.synchronize()
                if edPluginH5ToCBF.dataOutput is not None and edPluginH5ToCBF.dataOutput.outputCBFFileTemplate is not None:
                    outputCBFFileTemplate = edPluginH5ToCBF.dataOutput.outputCBFFileTemplate.path.value
                    outputCBFFileTemplate = outputCBFFileTemplate.replace("######", "{0:06d}")
                    for image in dictImage:
                        newDict[image] = XSDataFile(XSDataString(outputCBFFileTemplate.format(image)))
        return newDict, hasHdf5Prefix

    def sendMessageToMXCuBE(self, _strMessage, level="info"):
        if self._oServerProxy is not None:
            self.DEBUG("Sending message to mxCuBE: {0}".format(_strMessage))
            try:
                for strMessage in _strMessage.split("\n"):
                    if strMessage != "":
                        self._oServerProxy.log_message("EDNA | Dozor: " + _strMessage, level)
            except:
                self.DEBUG("Sending message to mxCuBE failed!")

    def sendResultToMXCuBE(self, _batchData):
        if self._oServerProxy is not None:
            self.DEBUG("Sending Dozor results to mxCuBE")
            try:
                self._oServerProxy.dozor_batch_processed(_batchData)
            except:
                pass

    def setStatusToMXCuBE(self, status):
        if self._oServerProxy is not None:
            self.DEBUG("Sending dozor status %s to mxCuBE" % status)
            try:
                self._oServerProxy.dozor_status_changed(status)
            except:
                pass
