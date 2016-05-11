#!/usr/bin/env python

#
# Generated Thu Feb 11 11:24::06 2016 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = { \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
}

try:
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataInteger
    from XSDataCommon import XSDataResult
except ImportError as error:
    if strEdnaHome is not None:
        for strXsdName in dictLocation:
            strXsdModule = strXsdName + ".py"
            strRootdir = os.path.dirname(os.path.abspath(os.path.join(strEdnaHome, dictLocation[strXsdName])))
            for strRoot, listDirs, listFiles in os.walk(strRootdir):
                if strXsdModule in listFiles:
                    sys.path.append(strRoot)
    else:
        raise error
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult




#
# Support/utility functions.
#

# Compabiltity between Python 2 and 3:
if sys.version.startswith('3'):
    unicode = str
    from io import StringIO
else:
    from StringIO import StringIO


def showIndent(outfile, level):
    for idx in range(level):
        outfile.write(unicode('    '))


def warnEmptyAttribute(_strName, _strTypeName):
    pass
    #if not _strTypeName in ["float", "double", "string", "boolean", "integer"]:
    #    print("Warning! Non-optional attribute %s of type %s is None!" % (_strName, _strTypeName))

class MixedContainer(object):
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:     # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, name)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write(unicode('<%s>%s</%s>' % (self.name, self.value, self.name)))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write(unicode('<%s>%d</%s>' % (self.name, self.value, self.name)))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write(unicode('<%s>%f</%s>' % (self.name, self.value, self.name)))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write(unicode('<%s>%g</%s>' % (self.name, self.value, self.name)))

#
# Data representation classes.
#



class XSDataISPyBDataCollection(object):
    def __init__(self, ybeam=None, xtalSnapshotFullPath4=None, xtalSnapshotFullPath3=None, xtalSnapshotFullPath2=None, xtalSnapshotFullPath1=None, xbeam=None, wavelength=None, undulatorGap3=None, undulatorGap2=None, undulatorGap1=None, transmission=None, synchrotronMode=None, startTime=None, strategySubWedgeOrigId=None, startImageNumber=None, slitGapHorizontal=None, slitGapVertical=None, sessionId=None, runStatus=None, rotationAxis=None, resolutionAtCorner=None, resolution=None, printableForReport=None, phiStart=None, overlap=None, omegaStart=None, numberOfPasses=None, numberOfImages=None, kappaStart=None, imageSuffix=None, imagePrefix=None, imageDirectory=None, flux=None, fileTemplate=None, experimentType=None, exposureTime=None, endTime=None, detectorMode=None, detectorDistance=None, detector2theta=None, dataCollectionNumber=None, dataCollectionId=None, crystalClass=None, comments=None, centeringMethod=None, blSampleId=None, beamSizeAtSampleY=None, beamSizeAtSampleX=None, beamShape=None, axisStart=None, axisRange=None, axisEnd=None, averageTemperature=None, actualCenteringPosition=None):
        self._actualCenteringPosition = str(actualCenteringPosition)
        if averageTemperature is None:
            self._averageTemperature = None
        else:
            self._averageTemperature = float(averageTemperature)
        if axisEnd is None:
            self._axisEnd = None
        else:
            self._axisEnd = float(axisEnd)
        if axisRange is None:
            self._axisRange = None
        else:
            self._axisRange = float(axisRange)
        if axisStart is None:
            self._axisStart = None
        else:
            self._axisStart = float(axisStart)
        self._beamShape = str(beamShape)
        if beamSizeAtSampleX is None:
            self._beamSizeAtSampleX = None
        else:
            self._beamSizeAtSampleX = float(beamSizeAtSampleX)
        if beamSizeAtSampleY is None:
            self._beamSizeAtSampleY = None
        else:
            self._beamSizeAtSampleY = float(beamSizeAtSampleY)
        if blSampleId is None:
            self._blSampleId = None
        else:
            self._blSampleId = int(blSampleId)
        self._centeringMethod = str(centeringMethod)
        self._comments = str(comments)
        self._crystalClass = str(crystalClass)
        if dataCollectionId is None:
            self._dataCollectionId = None
        else:
            self._dataCollectionId = int(dataCollectionId)
        if dataCollectionNumber is None:
            self._dataCollectionNumber = None
        else:
            self._dataCollectionNumber = int(dataCollectionNumber)
        if detector2theta is None:
            self._detector2theta = None
        else:
            self._detector2theta = float(detector2theta)
        if detectorDistance is None:
            self._detectorDistance = None
        else:
            self._detectorDistance = float(detectorDistance)
        self._detectorMode = str(detectorMode)
        self._endTime = str(endTime)
        if exposureTime is None:
            self._exposureTime = None
        else:
            self._exposureTime = float(exposureTime)
        self._experimentType = str(experimentType)
        self._fileTemplate = str(fileTemplate)
        if flux is None:
            self._flux = None
        else:
            self._flux = float(flux)
        self._imageDirectory = str(imageDirectory)
        self._imagePrefix = str(imagePrefix)
        self._imageSuffix = str(imageSuffix)
        if kappaStart is None:
            self._kappaStart = None
        else:
            self._kappaStart = float(kappaStart)
        if numberOfImages is None:
            self._numberOfImages = None
        else:
            self._numberOfImages = int(numberOfImages)
        if numberOfPasses is None:
            self._numberOfPasses = None
        else:
            self._numberOfPasses = int(numberOfPasses)
        if omegaStart is None:
            self._omegaStart = None
        else:
            self._omegaStart = float(omegaStart)
        if overlap is None:
            self._overlap = None
        else:
            self._overlap = float(overlap)
        if phiStart is None:
            self._phiStart = None
        else:
            self._phiStart = float(phiStart)
        self._printableForReport = bool(printableForReport)
        if resolution is None:
            self._resolution = None
        else:
            self._resolution = float(resolution)
        if resolutionAtCorner is None:
            self._resolutionAtCorner = None
        else:
            self._resolutionAtCorner = float(resolutionAtCorner)
        self._rotationAxis = str(rotationAxis)
        self._runStatus = str(runStatus)
        if sessionId is None:
            self._sessionId = None
        else:
            self._sessionId = int(sessionId)
        if slitGapVertical is None:
            self._slitGapVertical = None
        else:
            self._slitGapVertical = float(slitGapVertical)
        if slitGapHorizontal is None:
            self._slitGapHorizontal = None
        else:
            self._slitGapHorizontal = float(slitGapHorizontal)
        if startImageNumber is None:
            self._startImageNumber = None
        else:
            self._startImageNumber = int(startImageNumber)
        if strategySubWedgeOrigId is None:
            self._strategySubWedgeOrigId = None
        else:
            self._strategySubWedgeOrigId = int(strategySubWedgeOrigId)
        self._startTime = str(startTime)
        self._synchrotronMode = str(synchrotronMode)
        if transmission is None:
            self._transmission = None
        else:
            self._transmission = float(transmission)
        if undulatorGap1 is None:
            self._undulatorGap1 = None
        else:
            self._undulatorGap1 = float(undulatorGap1)
        if undulatorGap2 is None:
            self._undulatorGap2 = None
        else:
            self._undulatorGap2 = float(undulatorGap2)
        if undulatorGap3 is None:
            self._undulatorGap3 = None
        else:
            self._undulatorGap3 = float(undulatorGap3)
        if wavelength is None:
            self._wavelength = None
        else:
            self._wavelength = float(wavelength)
        if xbeam is None:
            self._xbeam = None
        else:
            self._xbeam = float(xbeam)
        self._xtalSnapshotFullPath1 = str(xtalSnapshotFullPath1)
        self._xtalSnapshotFullPath2 = str(xtalSnapshotFullPath2)
        self._xtalSnapshotFullPath3 = str(xtalSnapshotFullPath3)
        self._xtalSnapshotFullPath4 = str(xtalSnapshotFullPath4)
        if ybeam is None:
            self._ybeam = None
        else:
            self._ybeam = float(ybeam)
    # Methods and properties for the 'actualCenteringPosition' attribute
    def getActualCenteringPosition(self): return self._actualCenteringPosition
    def setActualCenteringPosition(self, actualCenteringPosition):
        self._actualCenteringPosition = str(actualCenteringPosition)
    def delActualCenteringPosition(self): self._actualCenteringPosition = None
    actualCenteringPosition = property(getActualCenteringPosition, setActualCenteringPosition, delActualCenteringPosition, "Property for actualCenteringPosition")
    # Methods and properties for the 'averageTemperature' attribute
    def getAverageTemperature(self): return self._averageTemperature
    def setAverageTemperature(self, averageTemperature):
        if averageTemperature is None:
            self._averageTemperature = None
        else:
            self._averageTemperature = float(averageTemperature)
    def delAverageTemperature(self): self._averageTemperature = None
    averageTemperature = property(getAverageTemperature, setAverageTemperature, delAverageTemperature, "Property for averageTemperature")
    # Methods and properties for the 'axisEnd' attribute
    def getAxisEnd(self): return self._axisEnd
    def setAxisEnd(self, axisEnd):
        if axisEnd is None:
            self._axisEnd = None
        else:
            self._axisEnd = float(axisEnd)
    def delAxisEnd(self): self._axisEnd = None
    axisEnd = property(getAxisEnd, setAxisEnd, delAxisEnd, "Property for axisEnd")
    # Methods and properties for the 'axisRange' attribute
    def getAxisRange(self): return self._axisRange
    def setAxisRange(self, axisRange):
        if axisRange is None:
            self._axisRange = None
        else:
            self._axisRange = float(axisRange)
    def delAxisRange(self): self._axisRange = None
    axisRange = property(getAxisRange, setAxisRange, delAxisRange, "Property for axisRange")
    # Methods and properties for the 'axisStart' attribute
    def getAxisStart(self): return self._axisStart
    def setAxisStart(self, axisStart):
        if axisStart is None:
            self._axisStart = None
        else:
            self._axisStart = float(axisStart)
    def delAxisStart(self): self._axisStart = None
    axisStart = property(getAxisStart, setAxisStart, delAxisStart, "Property for axisStart")
    # Methods and properties for the 'beamShape' attribute
    def getBeamShape(self): return self._beamShape
    def setBeamShape(self, beamShape):
        self._beamShape = str(beamShape)
    def delBeamShape(self): self._beamShape = None
    beamShape = property(getBeamShape, setBeamShape, delBeamShape, "Property for beamShape")
    # Methods and properties for the 'beamSizeAtSampleX' attribute
    def getBeamSizeAtSampleX(self): return self._beamSizeAtSampleX
    def setBeamSizeAtSampleX(self, beamSizeAtSampleX):
        if beamSizeAtSampleX is None:
            self._beamSizeAtSampleX = None
        else:
            self._beamSizeAtSampleX = float(beamSizeAtSampleX)
    def delBeamSizeAtSampleX(self): self._beamSizeAtSampleX = None
    beamSizeAtSampleX = property(getBeamSizeAtSampleX, setBeamSizeAtSampleX, delBeamSizeAtSampleX, "Property for beamSizeAtSampleX")
    # Methods and properties for the 'beamSizeAtSampleY' attribute
    def getBeamSizeAtSampleY(self): return self._beamSizeAtSampleY
    def setBeamSizeAtSampleY(self, beamSizeAtSampleY):
        if beamSizeAtSampleY is None:
            self._beamSizeAtSampleY = None
        else:
            self._beamSizeAtSampleY = float(beamSizeAtSampleY)
    def delBeamSizeAtSampleY(self): self._beamSizeAtSampleY = None
    beamSizeAtSampleY = property(getBeamSizeAtSampleY, setBeamSizeAtSampleY, delBeamSizeAtSampleY, "Property for beamSizeAtSampleY")
    # Methods and properties for the 'blSampleId' attribute
    def getBlSampleId(self): return self._blSampleId
    def setBlSampleId(self, blSampleId):
        if blSampleId is None:
            self._blSampleId = None
        else:
            self._blSampleId = int(blSampleId)
    def delBlSampleId(self): self._blSampleId = None
    blSampleId = property(getBlSampleId, setBlSampleId, delBlSampleId, "Property for blSampleId")
    # Methods and properties for the 'centeringMethod' attribute
    def getCenteringMethod(self): return self._centeringMethod
    def setCenteringMethod(self, centeringMethod):
        self._centeringMethod = str(centeringMethod)
    def delCenteringMethod(self): self._centeringMethod = None
    centeringMethod = property(getCenteringMethod, setCenteringMethod, delCenteringMethod, "Property for centeringMethod")
    # Methods and properties for the 'comments' attribute
    def getComments(self): return self._comments
    def setComments(self, comments):
        self._comments = str(comments)
    def delComments(self): self._comments = None
    comments = property(getComments, setComments, delComments, "Property for comments")
    # Methods and properties for the 'crystalClass' attribute
    def getCrystalClass(self): return self._crystalClass
    def setCrystalClass(self, crystalClass):
        self._crystalClass = str(crystalClass)
    def delCrystalClass(self): self._crystalClass = None
    crystalClass = property(getCrystalClass, setCrystalClass, delCrystalClass, "Property for crystalClass")
    # Methods and properties for the 'dataCollectionId' attribute
    def getDataCollectionId(self): return self._dataCollectionId
    def setDataCollectionId(self, dataCollectionId):
        if dataCollectionId is None:
            self._dataCollectionId = None
        else:
            self._dataCollectionId = int(dataCollectionId)
    def delDataCollectionId(self): self._dataCollectionId = None
    dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
    # Methods and properties for the 'dataCollectionNumber' attribute
    def getDataCollectionNumber(self): return self._dataCollectionNumber
    def setDataCollectionNumber(self, dataCollectionNumber):
        if dataCollectionNumber is None:
            self._dataCollectionNumber = None
        else:
            self._dataCollectionNumber = int(dataCollectionNumber)
    def delDataCollectionNumber(self): self._dataCollectionNumber = None
    dataCollectionNumber = property(getDataCollectionNumber, setDataCollectionNumber, delDataCollectionNumber, "Property for dataCollectionNumber")
    # Methods and properties for the 'detector2theta' attribute
    def getDetector2theta(self): return self._detector2theta
    def setDetector2theta(self, detector2theta):
        if detector2theta is None:
            self._detector2theta = None
        else:
            self._detector2theta = float(detector2theta)
    def delDetector2theta(self): self._detector2theta = None
    detector2theta = property(getDetector2theta, setDetector2theta, delDetector2theta, "Property for detector2theta")
    # Methods and properties for the 'detectorDistance' attribute
    def getDetectorDistance(self): return self._detectorDistance
    def setDetectorDistance(self, detectorDistance):
        if detectorDistance is None:
            self._detectorDistance = None
        else:
            self._detectorDistance = float(detectorDistance)
    def delDetectorDistance(self): self._detectorDistance = None
    detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
    # Methods and properties for the 'detectorMode' attribute
    def getDetectorMode(self): return self._detectorMode
    def setDetectorMode(self, detectorMode):
        self._detectorMode = str(detectorMode)
    def delDetectorMode(self): self._detectorMode = None
    detectorMode = property(getDetectorMode, setDetectorMode, delDetectorMode, "Property for detectorMode")
    # Methods and properties for the 'endTime' attribute
    def getEndTime(self): return self._endTime
    def setEndTime(self, endTime):
        self._endTime = str(endTime)
    def delEndTime(self): self._endTime = None
    endTime = property(getEndTime, setEndTime, delEndTime, "Property for endTime")
    # Methods and properties for the 'exposureTime' attribute
    def getExposureTime(self): return self._exposureTime
    def setExposureTime(self, exposureTime):
        if exposureTime is None:
            self._exposureTime = None
        else:
            self._exposureTime = float(exposureTime)
    def delExposureTime(self): self._exposureTime = None
    exposureTime = property(getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime")
    # Methods and properties for the 'experimentType' attribute
    def getExperimentType(self): return self._experimentType
    def setExperimentType(self, experimentType):
        self._experimentType = str(experimentType)
    def delExperimentType(self): self._experimentType = None
    experimentType = property(getExperimentType, setExperimentType, delExperimentType, "Property for experimentType")
    # Methods and properties for the 'fileTemplate' attribute
    def getFileTemplate(self): return self._fileTemplate
    def setFileTemplate(self, fileTemplate):
        self._fileTemplate = str(fileTemplate)
    def delFileTemplate(self): self._fileTemplate = None
    fileTemplate = property(getFileTemplate, setFileTemplate, delFileTemplate, "Property for fileTemplate")
    # Methods and properties for the 'flux' attribute
    def getFlux(self): return self._flux
    def setFlux(self, flux):
        if flux is None:
            self._flux = None
        else:
            self._flux = float(flux)
    def delFlux(self): self._flux = None
    flux = property(getFlux, setFlux, delFlux, "Property for flux")
    # Methods and properties for the 'imageDirectory' attribute
    def getImageDirectory(self): return self._imageDirectory
    def setImageDirectory(self, imageDirectory):
        self._imageDirectory = str(imageDirectory)
    def delImageDirectory(self): self._imageDirectory = None
    imageDirectory = property(getImageDirectory, setImageDirectory, delImageDirectory, "Property for imageDirectory")
    # Methods and properties for the 'imagePrefix' attribute
    def getImagePrefix(self): return self._imagePrefix
    def setImagePrefix(self, imagePrefix):
        self._imagePrefix = str(imagePrefix)
    def delImagePrefix(self): self._imagePrefix = None
    imagePrefix = property(getImagePrefix, setImagePrefix, delImagePrefix, "Property for imagePrefix")
    # Methods and properties for the 'imageSuffix' attribute
    def getImageSuffix(self): return self._imageSuffix
    def setImageSuffix(self, imageSuffix):
        self._imageSuffix = str(imageSuffix)
    def delImageSuffix(self): self._imageSuffix = None
    imageSuffix = property(getImageSuffix, setImageSuffix, delImageSuffix, "Property for imageSuffix")
    # Methods and properties for the 'kappaStart' attribute
    def getKappaStart(self): return self._kappaStart
    def setKappaStart(self, kappaStart):
        if kappaStart is None:
            self._kappaStart = None
        else:
            self._kappaStart = float(kappaStart)
    def delKappaStart(self): self._kappaStart = None
    kappaStart = property(getKappaStart, setKappaStart, delKappaStart, "Property for kappaStart")
    # Methods and properties for the 'numberOfImages' attribute
    def getNumberOfImages(self): return self._numberOfImages
    def setNumberOfImages(self, numberOfImages):
        if numberOfImages is None:
            self._numberOfImages = None
        else:
            self._numberOfImages = int(numberOfImages)
    def delNumberOfImages(self): self._numberOfImages = None
    numberOfImages = property(getNumberOfImages, setNumberOfImages, delNumberOfImages, "Property for numberOfImages")
    # Methods and properties for the 'numberOfPasses' attribute
    def getNumberOfPasses(self): return self._numberOfPasses
    def setNumberOfPasses(self, numberOfPasses):
        if numberOfPasses is None:
            self._numberOfPasses = None
        else:
            self._numberOfPasses = int(numberOfPasses)
    def delNumberOfPasses(self): self._numberOfPasses = None
    numberOfPasses = property(getNumberOfPasses, setNumberOfPasses, delNumberOfPasses, "Property for numberOfPasses")
    # Methods and properties for the 'omegaStart' attribute
    def getOmegaStart(self): return self._omegaStart
    def setOmegaStart(self, omegaStart):
        if omegaStart is None:
            self._omegaStart = None
        else:
            self._omegaStart = float(omegaStart)
    def delOmegaStart(self): self._omegaStart = None
    omegaStart = property(getOmegaStart, setOmegaStart, delOmegaStart, "Property for omegaStart")
    # Methods and properties for the 'overlap' attribute
    def getOverlap(self): return self._overlap
    def setOverlap(self, overlap):
        if overlap is None:
            self._overlap = None
        else:
            self._overlap = float(overlap)
    def delOverlap(self): self._overlap = None
    overlap = property(getOverlap, setOverlap, delOverlap, "Property for overlap")
    # Methods and properties for the 'phiStart' attribute
    def getPhiStart(self): return self._phiStart
    def setPhiStart(self, phiStart):
        if phiStart is None:
            self._phiStart = None
        else:
            self._phiStart = float(phiStart)
    def delPhiStart(self): self._phiStart = None
    phiStart = property(getPhiStart, setPhiStart, delPhiStart, "Property for phiStart")
    # Methods and properties for the 'printableForReport' attribute
    def getPrintableForReport(self): return self._printableForReport
    def setPrintableForReport(self, printableForReport):
        self._printableForReport = bool(printableForReport)
    def delPrintableForReport(self): self._printableForReport = None
    printableForReport = property(getPrintableForReport, setPrintableForReport, delPrintableForReport, "Property for printableForReport")
    # Methods and properties for the 'resolution' attribute
    def getResolution(self): return self._resolution
    def setResolution(self, resolution):
        if resolution is None:
            self._resolution = None
        else:
            self._resolution = float(resolution)
    def delResolution(self): self._resolution = None
    resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
    # Methods and properties for the 'resolutionAtCorner' attribute
    def getResolutionAtCorner(self): return self._resolutionAtCorner
    def setResolutionAtCorner(self, resolutionAtCorner):
        if resolutionAtCorner is None:
            self._resolutionAtCorner = None
        else:
            self._resolutionAtCorner = float(resolutionAtCorner)
    def delResolutionAtCorner(self): self._resolutionAtCorner = None
    resolutionAtCorner = property(getResolutionAtCorner, setResolutionAtCorner, delResolutionAtCorner, "Property for resolutionAtCorner")
    # Methods and properties for the 'rotationAxis' attribute
    def getRotationAxis(self): return self._rotationAxis
    def setRotationAxis(self, rotationAxis):
        self._rotationAxis = str(rotationAxis)
    def delRotationAxis(self): self._rotationAxis = None
    rotationAxis = property(getRotationAxis, setRotationAxis, delRotationAxis, "Property for rotationAxis")
    # Methods and properties for the 'runStatus' attribute
    def getRunStatus(self): return self._runStatus
    def setRunStatus(self, runStatus):
        self._runStatus = str(runStatus)
    def delRunStatus(self): self._runStatus = None
    runStatus = property(getRunStatus, setRunStatus, delRunStatus, "Property for runStatus")
    # Methods and properties for the 'sessionId' attribute
    def getSessionId(self): return self._sessionId
    def setSessionId(self, sessionId):
        if sessionId is None:
            self._sessionId = None
        else:
            self._sessionId = int(sessionId)
    def delSessionId(self): self._sessionId = None
    sessionId = property(getSessionId, setSessionId, delSessionId, "Property for sessionId")
    # Methods and properties for the 'slitGapVertical' attribute
    def getSlitGapVertical(self): return self._slitGapVertical
    def setSlitGapVertical(self, slitGapVertical):
        if slitGapVertical is None:
            self._slitGapVertical = None
        else:
            self._slitGapVertical = float(slitGapVertical)
    def delSlitGapVertical(self): self._slitGapVertical = None
    slitGapVertical = property(getSlitGapVertical, setSlitGapVertical, delSlitGapVertical, "Property for slitGapVertical")
    # Methods and properties for the 'slitGapHorizontal' attribute
    def getSlitGapHorizontal(self): return self._slitGapHorizontal
    def setSlitGapHorizontal(self, slitGapHorizontal):
        if slitGapHorizontal is None:
            self._slitGapHorizontal = None
        else:
            self._slitGapHorizontal = float(slitGapHorizontal)
    def delSlitGapHorizontal(self): self._slitGapHorizontal = None
    slitGapHorizontal = property(getSlitGapHorizontal, setSlitGapHorizontal, delSlitGapHorizontal, "Property for slitGapHorizontal")
    # Methods and properties for the 'startImageNumber' attribute
    def getStartImageNumber(self): return self._startImageNumber
    def setStartImageNumber(self, startImageNumber):
        if startImageNumber is None:
            self._startImageNumber = None
        else:
            self._startImageNumber = int(startImageNumber)
    def delStartImageNumber(self): self._startImageNumber = None
    startImageNumber = property(getStartImageNumber, setStartImageNumber, delStartImageNumber, "Property for startImageNumber")
    # Methods and properties for the 'strategySubWedgeOrigId' attribute
    def getStrategySubWedgeOrigId(self): return self._strategySubWedgeOrigId
    def setStrategySubWedgeOrigId(self, strategySubWedgeOrigId):
        if strategySubWedgeOrigId is None:
            self._strategySubWedgeOrigId = None
        else:
            self._strategySubWedgeOrigId = int(strategySubWedgeOrigId)
    def delStrategySubWedgeOrigId(self): self._strategySubWedgeOrigId = None
    strategySubWedgeOrigId = property(getStrategySubWedgeOrigId, setStrategySubWedgeOrigId, delStrategySubWedgeOrigId, "Property for strategySubWedgeOrigId")
    # Methods and properties for the 'startTime' attribute
    def getStartTime(self): return self._startTime
    def setStartTime(self, startTime):
        self._startTime = str(startTime)
    def delStartTime(self): self._startTime = None
    startTime = property(getStartTime, setStartTime, delStartTime, "Property for startTime")
    # Methods and properties for the 'synchrotronMode' attribute
    def getSynchrotronMode(self): return self._synchrotronMode
    def setSynchrotronMode(self, synchrotronMode):
        self._synchrotronMode = str(synchrotronMode)
    def delSynchrotronMode(self): self._synchrotronMode = None
    synchrotronMode = property(getSynchrotronMode, setSynchrotronMode, delSynchrotronMode, "Property for synchrotronMode")
    # Methods and properties for the 'transmission' attribute
    def getTransmission(self): return self._transmission
    def setTransmission(self, transmission):
        if transmission is None:
            self._transmission = None
        else:
            self._transmission = float(transmission)
    def delTransmission(self): self._transmission = None
    transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
    # Methods and properties for the 'undulatorGap1' attribute
    def getUndulatorGap1(self): return self._undulatorGap1
    def setUndulatorGap1(self, undulatorGap1):
        if undulatorGap1 is None:
            self._undulatorGap1 = None
        else:
            self._undulatorGap1 = float(undulatorGap1)
    def delUndulatorGap1(self): self._undulatorGap1 = None
    undulatorGap1 = property(getUndulatorGap1, setUndulatorGap1, delUndulatorGap1, "Property for undulatorGap1")
    # Methods and properties for the 'undulatorGap2' attribute
    def getUndulatorGap2(self): return self._undulatorGap2
    def setUndulatorGap2(self, undulatorGap2):
        if undulatorGap2 is None:
            self._undulatorGap2 = None
        else:
            self._undulatorGap2 = float(undulatorGap2)
    def delUndulatorGap2(self): self._undulatorGap2 = None
    undulatorGap2 = property(getUndulatorGap2, setUndulatorGap2, delUndulatorGap2, "Property for undulatorGap2")
    # Methods and properties for the 'undulatorGap3' attribute
    def getUndulatorGap3(self): return self._undulatorGap3
    def setUndulatorGap3(self, undulatorGap3):
        if undulatorGap3 is None:
            self._undulatorGap3 = None
        else:
            self._undulatorGap3 = float(undulatorGap3)
    def delUndulatorGap3(self): self._undulatorGap3 = None
    undulatorGap3 = property(getUndulatorGap3, setUndulatorGap3, delUndulatorGap3, "Property for undulatorGap3")
    # Methods and properties for the 'wavelength' attribute
    def getWavelength(self): return self._wavelength
    def setWavelength(self, wavelength):
        if wavelength is None:
            self._wavelength = None
        else:
            self._wavelength = float(wavelength)
    def delWavelength(self): self._wavelength = None
    wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
    # Methods and properties for the 'xbeam' attribute
    def getXbeam(self): return self._xbeam
    def setXbeam(self, xbeam):
        if xbeam is None:
            self._xbeam = None
        else:
            self._xbeam = float(xbeam)
    def delXbeam(self): self._xbeam = None
    xbeam = property(getXbeam, setXbeam, delXbeam, "Property for xbeam")
    # Methods and properties for the 'xtalSnapshotFullPath1' attribute
    def getXtalSnapshotFullPath1(self): return self._xtalSnapshotFullPath1
    def setXtalSnapshotFullPath1(self, xtalSnapshotFullPath1):
        self._xtalSnapshotFullPath1 = str(xtalSnapshotFullPath1)
    def delXtalSnapshotFullPath1(self): self._xtalSnapshotFullPath1 = None
    xtalSnapshotFullPath1 = property(getXtalSnapshotFullPath1, setXtalSnapshotFullPath1, delXtalSnapshotFullPath1, "Property for xtalSnapshotFullPath1")
    # Methods and properties for the 'xtalSnapshotFullPath2' attribute
    def getXtalSnapshotFullPath2(self): return self._xtalSnapshotFullPath2
    def setXtalSnapshotFullPath2(self, xtalSnapshotFullPath2):
        self._xtalSnapshotFullPath2 = str(xtalSnapshotFullPath2)
    def delXtalSnapshotFullPath2(self): self._xtalSnapshotFullPath2 = None
    xtalSnapshotFullPath2 = property(getXtalSnapshotFullPath2, setXtalSnapshotFullPath2, delXtalSnapshotFullPath2, "Property for xtalSnapshotFullPath2")
    # Methods and properties for the 'xtalSnapshotFullPath3' attribute
    def getXtalSnapshotFullPath3(self): return self._xtalSnapshotFullPath3
    def setXtalSnapshotFullPath3(self, xtalSnapshotFullPath3):
        self._xtalSnapshotFullPath3 = str(xtalSnapshotFullPath3)
    def delXtalSnapshotFullPath3(self): self._xtalSnapshotFullPath3 = None
    xtalSnapshotFullPath3 = property(getXtalSnapshotFullPath3, setXtalSnapshotFullPath3, delXtalSnapshotFullPath3, "Property for xtalSnapshotFullPath3")
    # Methods and properties for the 'xtalSnapshotFullPath4' attribute
    def getXtalSnapshotFullPath4(self): return self._xtalSnapshotFullPath4
    def setXtalSnapshotFullPath4(self, xtalSnapshotFullPath4):
        self._xtalSnapshotFullPath4 = str(xtalSnapshotFullPath4)
    def delXtalSnapshotFullPath4(self): self._xtalSnapshotFullPath4 = None
    xtalSnapshotFullPath4 = property(getXtalSnapshotFullPath4, setXtalSnapshotFullPath4, delXtalSnapshotFullPath4, "Property for xtalSnapshotFullPath4")
    # Methods and properties for the 'ybeam' attribute
    def getYbeam(self): return self._ybeam
    def setYbeam(self, ybeam):
        if ybeam is None:
            self._ybeam = None
        else:
            self._ybeam = float(ybeam)
    def delYbeam(self): self._ybeam = None
    ybeam = property(getYbeam, setYbeam, delYbeam, "Property for ybeam")
    def export(self, outfile, level, name_='XSDataISPyBDataCollection'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataISPyBDataCollection'):
        pass
        if self._actualCenteringPosition is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<actualCenteringPosition>%s</actualCenteringPosition>\n' % self._actualCenteringPosition))
        else:
            warnEmptyAttribute("actualCenteringPosition", "string")
        if self._averageTemperature is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<averageTemperature>%e</averageTemperature>\n' % self._averageTemperature))
        else:
            warnEmptyAttribute("averageTemperature", "float")
        if self._axisEnd is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<axisEnd>%e</axisEnd>\n' % self._axisEnd))
        else:
            warnEmptyAttribute("axisEnd", "float")
        if self._axisRange is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<axisRange>%e</axisRange>\n' % self._axisRange))
        else:
            warnEmptyAttribute("axisRange", "float")
        if self._axisStart is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<axisStart>%e</axisStart>\n' % self._axisStart))
        else:
            warnEmptyAttribute("axisStart", "float")
        if self._beamShape is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<beamShape>%s</beamShape>\n' % self._beamShape))
        else:
            warnEmptyAttribute("beamShape", "string")
        if self._beamSizeAtSampleX is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<beamSizeAtSampleX>%e</beamSizeAtSampleX>\n' % self._beamSizeAtSampleX))
        else:
            warnEmptyAttribute("beamSizeAtSampleX", "float")
        if self._beamSizeAtSampleY is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<beamSizeAtSampleY>%e</beamSizeAtSampleY>\n' % self._beamSizeAtSampleY))
        else:
            warnEmptyAttribute("beamSizeAtSampleY", "float")
        if self._blSampleId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<blSampleId>%d</blSampleId>\n' % self._blSampleId))
        else:
            warnEmptyAttribute("blSampleId", "integer")
        if self._centeringMethod is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<centeringMethod>%s</centeringMethod>\n' % self._centeringMethod))
        else:
            warnEmptyAttribute("centeringMethod", "string")
        if self._comments is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<comments>%s</comments>\n' % self._comments))
        else:
            warnEmptyAttribute("comments", "string")
        if self._crystalClass is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<crystalClass>%s</crystalClass>\n' % self._crystalClass))
        else:
            warnEmptyAttribute("crystalClass", "string")
        if self._dataCollectionId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<dataCollectionId>%d</dataCollectionId>\n' % self._dataCollectionId))
        else:
            warnEmptyAttribute("dataCollectionId", "integer")
        if self._dataCollectionNumber is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<dataCollectionNumber>%d</dataCollectionNumber>\n' % self._dataCollectionNumber))
        else:
            warnEmptyAttribute("dataCollectionNumber", "integer")
        if self._detector2theta is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<detector2theta>%e</detector2theta>\n' % self._detector2theta))
        else:
            warnEmptyAttribute("detector2theta", "float")
        if self._detectorDistance is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<detectorDistance>%e</detectorDistance>\n' % self._detectorDistance))
        else:
            warnEmptyAttribute("detectorDistance", "float")
        if self._detectorMode is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<detectorMode>%s</detectorMode>\n' % self._detectorMode))
        else:
            warnEmptyAttribute("detectorMode", "string")
        if self._endTime is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<endTime>%s</endTime>\n' % self._endTime))
        else:
            warnEmptyAttribute("endTime", "string")
        if self._exposureTime is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<exposureTime>%e</exposureTime>\n' % self._exposureTime))
        else:
            warnEmptyAttribute("exposureTime", "float")
        if self._experimentType is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<experimentType>%s</experimentType>\n' % self._experimentType))
        else:
            warnEmptyAttribute("experimentType", "string")
        if self._fileTemplate is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<fileTemplate>%s</fileTemplate>\n' % self._fileTemplate))
        else:
            warnEmptyAttribute("fileTemplate", "string")
        if self._flux is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<flux>%e</flux>\n' % self._flux))
        else:
            warnEmptyAttribute("flux", "float")
        if self._imageDirectory is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<imageDirectory>%s</imageDirectory>\n' % self._imageDirectory))
        else:
            warnEmptyAttribute("imageDirectory", "string")
        if self._imagePrefix is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<imagePrefix>%s</imagePrefix>\n' % self._imagePrefix))
        else:
            warnEmptyAttribute("imagePrefix", "string")
        if self._imageSuffix is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<imageSuffix>%s</imageSuffix>\n' % self._imageSuffix))
        else:
            warnEmptyAttribute("imageSuffix", "string")
        if self._kappaStart is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<kappaStart>%e</kappaStart>\n' % self._kappaStart))
        else:
            warnEmptyAttribute("kappaStart", "float")
        if self._numberOfImages is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<numberOfImages>%d</numberOfImages>\n' % self._numberOfImages))
        else:
            warnEmptyAttribute("numberOfImages", "integer")
        if self._numberOfPasses is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<numberOfPasses>%d</numberOfPasses>\n' % self._numberOfPasses))
        else:
            warnEmptyAttribute("numberOfPasses", "integer")
        if self._omegaStart is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<omegaStart>%e</omegaStart>\n' % self._omegaStart))
        else:
            warnEmptyAttribute("omegaStart", "float")
        if self._overlap is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<overlap>%e</overlap>\n' % self._overlap))
        else:
            warnEmptyAttribute("overlap", "float")
        if self._phiStart is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<phiStart>%e</phiStart>\n' % self._phiStart))
        else:
            warnEmptyAttribute("phiStart", "float")
        if self._printableForReport is not None:
            showIndent(outfile, level)
            if self._printableForReport:
                outfile.write(unicode('<printableForReport>true</printableForReport>\n'))
            else:
                outfile.write(unicode('<printableForReport>false</printableForReport>\n'))
        else:
            warnEmptyAttribute("printableForReport", "boolean")
        if self._resolution is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<resolution>%e</resolution>\n' % self._resolution))
        else:
            warnEmptyAttribute("resolution", "float")
        if self._resolutionAtCorner is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<resolutionAtCorner>%e</resolutionAtCorner>\n' % self._resolutionAtCorner))
        else:
            warnEmptyAttribute("resolutionAtCorner", "float")
        if self._rotationAxis is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<rotationAxis>%s</rotationAxis>\n' % self._rotationAxis))
        else:
            warnEmptyAttribute("rotationAxis", "string")
        if self._runStatus is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<runStatus>%s</runStatus>\n' % self._runStatus))
        else:
            warnEmptyAttribute("runStatus", "string")
        if self._sessionId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<sessionId>%d</sessionId>\n' % self._sessionId))
        else:
            warnEmptyAttribute("sessionId", "integer")
        if self._slitGapVertical is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<slitGapVertical>%e</slitGapVertical>\n' % self._slitGapVertical))
        else:
            warnEmptyAttribute("slitGapVertical", "float")
        if self._slitGapHorizontal is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<slitGapHorizontal>%e</slitGapHorizontal>\n' % self._slitGapHorizontal))
        else:
            warnEmptyAttribute("slitGapHorizontal", "float")
        if self._startImageNumber is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<startImageNumber>%d</startImageNumber>\n' % self._startImageNumber))
        else:
            warnEmptyAttribute("startImageNumber", "integer")
        if self._strategySubWedgeOrigId is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<strategySubWedgeOrigId>%d</strategySubWedgeOrigId>\n' % self._strategySubWedgeOrigId))
        if self._startTime is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<startTime>%s</startTime>\n' % self._startTime))
        else:
            warnEmptyAttribute("startTime", "string")
        if self._synchrotronMode is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<synchrotronMode>%s</synchrotronMode>\n' % self._synchrotronMode))
        else:
            warnEmptyAttribute("synchrotronMode", "string")
        if self._transmission is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<transmission>%e</transmission>\n' % self._transmission))
        else:
            warnEmptyAttribute("transmission", "float")
        if self._undulatorGap1 is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<undulatorGap1>%e</undulatorGap1>\n' % self._undulatorGap1))
        else:
            warnEmptyAttribute("undulatorGap1", "float")
        if self._undulatorGap2 is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<undulatorGap2>%e</undulatorGap2>\n' % self._undulatorGap2))
        else:
            warnEmptyAttribute("undulatorGap2", "float")
        if self._undulatorGap3 is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<undulatorGap3>%e</undulatorGap3>\n' % self._undulatorGap3))
        else:
            warnEmptyAttribute("undulatorGap3", "float")
        if self._wavelength is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<wavelength>%e</wavelength>\n' % self._wavelength))
        else:
            warnEmptyAttribute("wavelength", "float")
        if self._xbeam is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<xbeam>%e</xbeam>\n' % self._xbeam))
        else:
            warnEmptyAttribute("xbeam", "float")
        if self._xtalSnapshotFullPath1 is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<xtalSnapshotFullPath1>%s</xtalSnapshotFullPath1>\n' % self._xtalSnapshotFullPath1))
        else:
            warnEmptyAttribute("xtalSnapshotFullPath1", "string")
        if self._xtalSnapshotFullPath2 is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<xtalSnapshotFullPath2>%s</xtalSnapshotFullPath2>\n' % self._xtalSnapshotFullPath2))
        else:
            warnEmptyAttribute("xtalSnapshotFullPath2", "string")
        if self._xtalSnapshotFullPath3 is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<xtalSnapshotFullPath3>%s</xtalSnapshotFullPath3>\n' % self._xtalSnapshotFullPath3))
        else:
            warnEmptyAttribute("xtalSnapshotFullPath3", "string")
        if self._xtalSnapshotFullPath4 is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<xtalSnapshotFullPath4>%s</xtalSnapshotFullPath4>\n' % self._xtalSnapshotFullPath4))
        else:
            warnEmptyAttribute("xtalSnapshotFullPath4", "string")
        if self._ybeam is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<ybeam>%e</ybeam>\n' % self._ybeam))
        else:
            warnEmptyAttribute("ybeam", "float")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'actualCenteringPosition':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._actualCenteringPosition = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'averageTemperature':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._averageTemperature = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'axisEnd':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._axisEnd = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'axisRange':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._axisRange = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'axisStart':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._axisStart = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamShape':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._beamShape = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamSizeAtSampleX':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._beamSizeAtSampleX = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamSizeAtSampleY':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._beamSizeAtSampleY = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'blSampleId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._blSampleId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'centeringMethod':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._centeringMethod = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comments':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._comments = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystalClass':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._crystalClass = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._dataCollectionId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionNumber':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._dataCollectionNumber = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detector2theta':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._detector2theta = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detectorDistance':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._detectorDistance = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detectorMode':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._detectorMode = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'endTime':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._endTime = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposureTime':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._exposureTime = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentType':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._experimentType = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fileTemplate':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._fileTemplate = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'flux':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._flux = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageDirectory':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._imageDirectory = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imagePrefix':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._imagePrefix = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageSuffix':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._imageSuffix = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kappaStart':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._kappaStart = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfImages':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._numberOfImages = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfPasses':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._numberOfPasses = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'omegaStart':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._omegaStart = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'overlap':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._overlap = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phiStart':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._phiStart = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'printableForReport':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                if sval_ in ('True', 'true', '1'):
                    ival_ = True
                elif sval_ in ('False', 'false', '0'):
                    ival_ = False
                else:
                    raise ValueError('requires boolean -- %s' % child_.toxml())
                self._printableForReport = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._resolution = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolutionAtCorner':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._resolutionAtCorner = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotationAxis':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._rotationAxis = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'runStatus':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._runStatus = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sessionId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._sessionId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'slitGapVertical':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._slitGapVertical = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'slitGapHorizontal':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._slitGapHorizontal = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'startImageNumber':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._startImageNumber = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'strategySubWedgeOrigId':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._strategySubWedgeOrigId = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'startTime':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._startTime = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'synchrotronMode':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._synchrotronMode = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'transmission':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._transmission = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'undulatorGap1':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._undulatorGap1 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'undulatorGap2':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._undulatorGap2 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'undulatorGap3':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._undulatorGap3 = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'wavelength':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._wavelength = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xbeam':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._xbeam = fval_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xtalSnapshotFullPath1':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._xtalSnapshotFullPath1 = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xtalSnapshotFullPath2':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._xtalSnapshotFullPath2 = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xtalSnapshotFullPath3':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._xtalSnapshotFullPath3 = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xtalSnapshotFullPath4':
            value_ = ''
            for text__content_ in child_.childNodes:
                if text__content_.nodeValue is not None:
                    value_ += text__content_.nodeValue
            self._xtalSnapshotFullPath4 = value_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ybeam':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    fval_ = float(sval_)
                except ValueError:
                    raise ValueError('requires float (or double) -- %s' % child_.toxml())
                self._ybeam = fval_
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataISPyBDataCollection" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataISPyBDataCollection' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataISPyBDataCollection is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataISPyBDataCollection.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBDataCollection()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataISPyBDataCollection" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataISPyBDataCollection()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataISPyBDataCollection


class XSDataInputControlH5ToCBF(XSDataInput):
    def __init__(self, configuration=None, forcedOutputDirectory=None, ispybDataCollection=None, hdf5File=None, hdf5ImageNumber=None, imageNumber=None):
        XSDataInput.__init__(self, configuration)
        if imageNumber is None:
            self._imageNumber = None
        elif imageNumber.__class__.__name__ == "XSDataInteger":
            self._imageNumber = imageNumber
        else:
            strMessage = "ERROR! XSDataInputControlH5ToCBF constructor argument 'imageNumber' is not XSDataInteger but %s" % self._imageNumber.__class__.__name__
            raise BaseException(strMessage)
        if hdf5ImageNumber is None:
            self._hdf5ImageNumber = None
        elif hdf5ImageNumber.__class__.__name__ == "XSDataInteger":
            self._hdf5ImageNumber = hdf5ImageNumber
        else:
            strMessage = "ERROR! XSDataInputControlH5ToCBF constructor argument 'hdf5ImageNumber' is not XSDataInteger but %s" % self._hdf5ImageNumber.__class__.__name__
            raise BaseException(strMessage)
        if hdf5File is None:
            self._hdf5File = None
        elif hdf5File.__class__.__name__ == "XSDataFile":
            self._hdf5File = hdf5File
        else:
            strMessage = "ERROR! XSDataInputControlH5ToCBF constructor argument 'hdf5File' is not XSDataFile but %s" % self._hdf5File.__class__.__name__
            raise BaseException(strMessage)
        if ispybDataCollection is None:
            self._ispybDataCollection = None
        elif ispybDataCollection.__class__.__name__ == "XSDataISPyBDataCollection":
            self._ispybDataCollection = ispybDataCollection
        else:
            strMessage = "ERROR! XSDataInputControlH5ToCBF constructor argument 'ispybDataCollection' is not XSDataISPyBDataCollection but %s" % self._ispybDataCollection.__class__.__name__
            raise BaseException(strMessage)
        if forcedOutputDirectory is None:
            self._forcedOutputDirectory = None
        elif forcedOutputDirectory.__class__.__name__ == "XSDataFile":
            self._forcedOutputDirectory = forcedOutputDirectory
        else:
            strMessage = "ERROR! XSDataInputControlH5ToCBF constructor argument 'forcedOutputDirectory' is not XSDataFile but %s" % self._forcedOutputDirectory.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'imageNumber' attribute
    def getImageNumber(self): return self._imageNumber
    def setImageNumber(self, imageNumber):
        if imageNumber is None:
            self._imageNumber = None
        elif imageNumber.__class__.__name__ == "XSDataInteger":
            self._imageNumber = imageNumber
        else:
            strMessage = "ERROR! XSDataInputControlH5ToCBF.setImageNumber argument is not XSDataInteger but %s" % imageNumber.__class__.__name__
            raise BaseException(strMessage)
    def delImageNumber(self): self._imageNumber = None
    imageNumber = property(getImageNumber, setImageNumber, delImageNumber, "Property for imageNumber")
    # Methods and properties for the 'hdf5ImageNumber' attribute
    def getHdf5ImageNumber(self): return self._hdf5ImageNumber
    def setHdf5ImageNumber(self, hdf5ImageNumber):
        if hdf5ImageNumber is None:
            self._hdf5ImageNumber = None
        elif hdf5ImageNumber.__class__.__name__ == "XSDataInteger":
            self._hdf5ImageNumber = hdf5ImageNumber
        else:
            strMessage = "ERROR! XSDataInputControlH5ToCBF.setHdf5ImageNumber argument is not XSDataInteger but %s" % hdf5ImageNumber.__class__.__name__
            raise BaseException(strMessage)
    def delHdf5ImageNumber(self): self._hdf5ImageNumber = None
    hdf5ImageNumber = property(getHdf5ImageNumber, setHdf5ImageNumber, delHdf5ImageNumber, "Property for hdf5ImageNumber")
    # Methods and properties for the 'hdf5File' attribute
    def getHdf5File(self): return self._hdf5File
    def setHdf5File(self, hdf5File):
        if hdf5File is None:
            self._hdf5File = None
        elif hdf5File.__class__.__name__ == "XSDataFile":
            self._hdf5File = hdf5File
        else:
            strMessage = "ERROR! XSDataInputControlH5ToCBF.setHdf5File argument is not XSDataFile but %s" % hdf5File.__class__.__name__
            raise BaseException(strMessage)
    def delHdf5File(self): self._hdf5File = None
    hdf5File = property(getHdf5File, setHdf5File, delHdf5File, "Property for hdf5File")
    # Methods and properties for the 'ispybDataCollection' attribute
    def getIspybDataCollection(self): return self._ispybDataCollection
    def setIspybDataCollection(self, ispybDataCollection):
        if ispybDataCollection is None:
            self._ispybDataCollection = None
        elif ispybDataCollection.__class__.__name__ == "XSDataISPyBDataCollection":
            self._ispybDataCollection = ispybDataCollection
        else:
            strMessage = "ERROR! XSDataInputControlH5ToCBF.setIspybDataCollection argument is not XSDataISPyBDataCollection but %s" % ispybDataCollection.__class__.__name__
            raise BaseException(strMessage)
    def delIspybDataCollection(self): self._ispybDataCollection = None
    ispybDataCollection = property(getIspybDataCollection, setIspybDataCollection, delIspybDataCollection, "Property for ispybDataCollection")
    # Methods and properties for the 'forcedOutputDirectory' attribute
    def getForcedOutputDirectory(self): return self._forcedOutputDirectory
    def setForcedOutputDirectory(self, forcedOutputDirectory):
        if forcedOutputDirectory is None:
            self._forcedOutputDirectory = None
        elif forcedOutputDirectory.__class__.__name__ == "XSDataFile":
            self._forcedOutputDirectory = forcedOutputDirectory
        else:
            strMessage = "ERROR! XSDataInputControlH5ToCBF.setForcedOutputDirectory argument is not XSDataFile but %s" % forcedOutputDirectory.__class__.__name__
            raise BaseException(strMessage)
    def delForcedOutputDirectory(self): self._forcedOutputDirectory = None
    forcedOutputDirectory = property(getForcedOutputDirectory, setForcedOutputDirectory, delForcedOutputDirectory, "Property for forcedOutputDirectory")
    def export(self, outfile, level, name_='XSDataInputControlH5ToCBF'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputControlH5ToCBF'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._imageNumber is not None:
            self.imageNumber.export(outfile, level, name_='imageNumber')
        else:
            warnEmptyAttribute("imageNumber", "XSDataInteger")
        if self._hdf5ImageNumber is not None:
            self.hdf5ImageNumber.export(outfile, level, name_='hdf5ImageNumber')
        if self._hdf5File is not None:
            self.hdf5File.export(outfile, level, name_='hdf5File')
        else:
            warnEmptyAttribute("hdf5File", "XSDataFile")
        if self._ispybDataCollection is not None:
            self.ispybDataCollection.export(outfile, level, name_='ispybDataCollection')
        if self._forcedOutputDirectory is not None:
            self.forcedOutputDirectory.export(outfile, level, name_='forcedOutputDirectory')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imageNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setImageNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hdf5ImageNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setHdf5ImageNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hdf5File':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setHdf5File(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ispybDataCollection':
            obj_ = XSDataISPyBDataCollection()
            obj_.build(child_)
            self.setIspybDataCollection(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'forcedOutputDirectory':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setForcedOutputDirectory(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputControlH5ToCBF" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputControlH5ToCBF' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputControlH5ToCBF is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputControlH5ToCBF.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputControlH5ToCBF()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputControlH5ToCBF" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputControlH5ToCBF()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputControlH5ToCBF


class XSDataResultControlH5ToCBF(XSDataResult):
    def __init__(self, status=None, ispybDataCollection=None, outputCBFFile=None):
        XSDataResult.__init__(self, status)
        if outputCBFFile is None:
            self._outputCBFFile = None
        elif outputCBFFile.__class__.__name__ == "XSDataFile":
            self._outputCBFFile = outputCBFFile
        else:
            strMessage = "ERROR! XSDataResultControlH5ToCBF constructor argument 'outputCBFFile' is not XSDataFile but %s" % self._outputCBFFile.__class__.__name__
            raise BaseException(strMessage)
        if ispybDataCollection is None:
            self._ispybDataCollection = None
        elif ispybDataCollection.__class__.__name__ == "XSDataISPyBDataCollection":
            self._ispybDataCollection = ispybDataCollection
        else:
            strMessage = "ERROR! XSDataResultControlH5ToCBF constructor argument 'ispybDataCollection' is not XSDataISPyBDataCollection but %s" % self._ispybDataCollection.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'outputCBFFile' attribute
    def getOutputCBFFile(self): return self._outputCBFFile
    def setOutputCBFFile(self, outputCBFFile):
        if outputCBFFile is None:
            self._outputCBFFile = None
        elif outputCBFFile.__class__.__name__ == "XSDataFile":
            self._outputCBFFile = outputCBFFile
        else:
            strMessage = "ERROR! XSDataResultControlH5ToCBF.setOutputCBFFile argument is not XSDataFile but %s" % outputCBFFile.__class__.__name__
            raise BaseException(strMessage)
    def delOutputCBFFile(self): self._outputCBFFile = None
    outputCBFFile = property(getOutputCBFFile, setOutputCBFFile, delOutputCBFFile, "Property for outputCBFFile")
    # Methods and properties for the 'ispybDataCollection' attribute
    def getIspybDataCollection(self): return self._ispybDataCollection
    def setIspybDataCollection(self, ispybDataCollection):
        if ispybDataCollection is None:
            self._ispybDataCollection = None
        elif ispybDataCollection.__class__.__name__ == "XSDataISPyBDataCollection":
            self._ispybDataCollection = ispybDataCollection
        else:
            strMessage = "ERROR! XSDataResultControlH5ToCBF.setIspybDataCollection argument is not XSDataISPyBDataCollection but %s" % ispybDataCollection.__class__.__name__
            raise BaseException(strMessage)
    def delIspybDataCollection(self): self._ispybDataCollection = None
    ispybDataCollection = property(getIspybDataCollection, setIspybDataCollection, delIspybDataCollection, "Property for ispybDataCollection")
    def export(self, outfile, level, name_='XSDataResultControlH5ToCBF'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultControlH5ToCBF'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._outputCBFFile is not None:
            self.outputCBFFile.export(outfile, level, name_='outputCBFFile')
        else:
            warnEmptyAttribute("outputCBFFile", "XSDataFile")
        if self._ispybDataCollection is not None:
            self.ispybDataCollection.export(outfile, level, name_='ispybDataCollection')
        else:
            warnEmptyAttribute("ispybDataCollection", "XSDataISPyBDataCollection")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputCBFFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutputCBFFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ispybDataCollection':
            obj_ = XSDataISPyBDataCollection()
            obj_.build(child_)
            self.setIspybDataCollection(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultControlH5ToCBF" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultControlH5ToCBF' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultControlH5ToCBF is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultControlH5ToCBF.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultControlH5ToCBF()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultControlH5ToCBF" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultControlH5ToCBF()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultControlH5ToCBF



# End of data representation classes.


