#!/usr/bin/env python

#
# Generated Wed Oct 25 10:15::44 2017 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = { \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
}

try:
    from XSDataCommon import XSDataDouble
    from XSDataCommon import XSDataInput
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
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInput
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



class XSDataInputFbest(XSDataInput):
    def __init__(self, configuration=None, crystalSize=None, sensitivity=None, doseRate=None, doseLimit=None, minExposureTime=None, rotationWidth=None, rotationRange=None, slitY=None, slitX=None, aperture=None, wavelength=None, beamV=None, beamH=None, resolution=None, flux=None):
        XSDataInput.__init__(self, configuration)
        if flux is None:
            self._flux = None
        elif flux.__class__.__name__ == "XSDataDouble":
            self._flux = flux
        else:
            strMessage = "ERROR! XSDataInputFbest constructor argument 'flux' is not XSDataDouble but %s" % self._flux.__class__.__name__
            raise BaseException(strMessage)
        if resolution is None:
            self._resolution = None
        elif resolution.__class__.__name__ == "XSDataDouble":
            self._resolution = resolution
        else:
            strMessage = "ERROR! XSDataInputFbest constructor argument 'resolution' is not XSDataDouble but %s" % self._resolution.__class__.__name__
            raise BaseException(strMessage)
        if beamH is None:
            self._beamH = None
        elif beamH.__class__.__name__ == "XSDataDouble":
            self._beamH = beamH
        else:
            strMessage = "ERROR! XSDataInputFbest constructor argument 'beamH' is not XSDataDouble but %s" % self._beamH.__class__.__name__
            raise BaseException(strMessage)
        if beamV is None:
            self._beamV = None
        elif beamV.__class__.__name__ == "XSDataDouble":
            self._beamV = beamV
        else:
            strMessage = "ERROR! XSDataInputFbest constructor argument 'beamV' is not XSDataDouble but %s" % self._beamV.__class__.__name__
            raise BaseException(strMessage)
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataDouble":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSDataInputFbest constructor argument 'wavelength' is not XSDataDouble but %s" % self._wavelength.__class__.__name__
            raise BaseException(strMessage)
        if aperture is None:
            self._aperture = None
        elif aperture.__class__.__name__ == "XSDataDouble":
            self._aperture = aperture
        else:
            strMessage = "ERROR! XSDataInputFbest constructor argument 'aperture' is not XSDataDouble but %s" % self._aperture.__class__.__name__
            raise BaseException(strMessage)
        if slitX is None:
            self._slitX = None
        elif slitX.__class__.__name__ == "XSDataDouble":
            self._slitX = slitX
        else:
            strMessage = "ERROR! XSDataInputFbest constructor argument 'slitX' is not XSDataDouble but %s" % self._slitX.__class__.__name__
            raise BaseException(strMessage)
        if slitY is None:
            self._slitY = None
        elif slitY.__class__.__name__ == "XSDataDouble":
            self._slitY = slitY
        else:
            strMessage = "ERROR! XSDataInputFbest constructor argument 'slitY' is not XSDataDouble but %s" % self._slitY.__class__.__name__
            raise BaseException(strMessage)
        if rotationRange is None:
            self._rotationRange = None
        elif rotationRange.__class__.__name__ == "XSDataDouble":
            self._rotationRange = rotationRange
        else:
            strMessage = "ERROR! XSDataInputFbest constructor argument 'rotationRange' is not XSDataDouble but %s" % self._rotationRange.__class__.__name__
            raise BaseException(strMessage)
        if rotationWidth is None:
            self._rotationWidth = None
        elif rotationWidth.__class__.__name__ == "XSDataDouble":
            self._rotationWidth = rotationWidth
        else:
            strMessage = "ERROR! XSDataInputFbest constructor argument 'rotationWidth' is not XSDataDouble but %s" % self._rotationWidth.__class__.__name__
            raise BaseException(strMessage)
        if minExposureTime is None:
            self._minExposureTime = None
        elif minExposureTime.__class__.__name__ == "XSDataDouble":
            self._minExposureTime = minExposureTime
        else:
            strMessage = "ERROR! XSDataInputFbest constructor argument 'minExposureTime' is not XSDataDouble but %s" % self._minExposureTime.__class__.__name__
            raise BaseException(strMessage)
        if doseLimit is None:
            self._doseLimit = None
        elif doseLimit.__class__.__name__ == "XSDataDouble":
            self._doseLimit = doseLimit
        else:
            strMessage = "ERROR! XSDataInputFbest constructor argument 'doseLimit' is not XSDataDouble but %s" % self._doseLimit.__class__.__name__
            raise BaseException(strMessage)
        if doseRate is None:
            self._doseRate = None
        elif doseRate.__class__.__name__ == "XSDataDouble":
            self._doseRate = doseRate
        else:
            strMessage = "ERROR! XSDataInputFbest constructor argument 'doseRate' is not XSDataDouble but %s" % self._doseRate.__class__.__name__
            raise BaseException(strMessage)
        if sensitivity is None:
            self._sensitivity = None
        elif sensitivity.__class__.__name__ == "XSDataDouble":
            self._sensitivity = sensitivity
        else:
            strMessage = "ERROR! XSDataInputFbest constructor argument 'sensitivity' is not XSDataDouble but %s" % self._sensitivity.__class__.__name__
            raise BaseException(strMessage)
        if crystalSize is None:
            self._crystalSize = None
        elif crystalSize.__class__.__name__ == "XSDataDouble":
            self._crystalSize = crystalSize
        else:
            strMessage = "ERROR! XSDataInputFbest constructor argument 'crystalSize' is not XSDataDouble but %s" % self._crystalSize.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'flux' attribute
    def getFlux(self): return self._flux
    def setFlux(self, flux):
        if flux is None:
            self._flux = None
        elif flux.__class__.__name__ == "XSDataDouble":
            self._flux = flux
        else:
            strMessage = "ERROR! XSDataInputFbest.setFlux argument is not XSDataDouble but %s" % flux.__class__.__name__
            raise BaseException(strMessage)
    def delFlux(self): self._flux = None
    flux = property(getFlux, setFlux, delFlux, "Property for flux")
    # Methods and properties for the 'resolution' attribute
    def getResolution(self): return self._resolution
    def setResolution(self, resolution):
        if resolution is None:
            self._resolution = None
        elif resolution.__class__.__name__ == "XSDataDouble":
            self._resolution = resolution
        else:
            strMessage = "ERROR! XSDataInputFbest.setResolution argument is not XSDataDouble but %s" % resolution.__class__.__name__
            raise BaseException(strMessage)
    def delResolution(self): self._resolution = None
    resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
    # Methods and properties for the 'beamH' attribute
    def getBeamH(self): return self._beamH
    def setBeamH(self, beamH):
        if beamH is None:
            self._beamH = None
        elif beamH.__class__.__name__ == "XSDataDouble":
            self._beamH = beamH
        else:
            strMessage = "ERROR! XSDataInputFbest.setBeamH argument is not XSDataDouble but %s" % beamH.__class__.__name__
            raise BaseException(strMessage)
    def delBeamH(self): self._beamH = None
    beamH = property(getBeamH, setBeamH, delBeamH, "Property for beamH")
    # Methods and properties for the 'beamV' attribute
    def getBeamV(self): return self._beamV
    def setBeamV(self, beamV):
        if beamV is None:
            self._beamV = None
        elif beamV.__class__.__name__ == "XSDataDouble":
            self._beamV = beamV
        else:
            strMessage = "ERROR! XSDataInputFbest.setBeamV argument is not XSDataDouble but %s" % beamV.__class__.__name__
            raise BaseException(strMessage)
    def delBeamV(self): self._beamV = None
    beamV = property(getBeamV, setBeamV, delBeamV, "Property for beamV")
    # Methods and properties for the 'wavelength' attribute
    def getWavelength(self): return self._wavelength
    def setWavelength(self, wavelength):
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataDouble":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSDataInputFbest.setWavelength argument is not XSDataDouble but %s" % wavelength.__class__.__name__
            raise BaseException(strMessage)
    def delWavelength(self): self._wavelength = None
    wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
    # Methods and properties for the 'aperture' attribute
    def getAperture(self): return self._aperture
    def setAperture(self, aperture):
        if aperture is None:
            self._aperture = None
        elif aperture.__class__.__name__ == "XSDataDouble":
            self._aperture = aperture
        else:
            strMessage = "ERROR! XSDataInputFbest.setAperture argument is not XSDataDouble but %s" % aperture.__class__.__name__
            raise BaseException(strMessage)
    def delAperture(self): self._aperture = None
    aperture = property(getAperture, setAperture, delAperture, "Property for aperture")
    # Methods and properties for the 'slitX' attribute
    def getSlitX(self): return self._slitX
    def setSlitX(self, slitX):
        if slitX is None:
            self._slitX = None
        elif slitX.__class__.__name__ == "XSDataDouble":
            self._slitX = slitX
        else:
            strMessage = "ERROR! XSDataInputFbest.setSlitX argument is not XSDataDouble but %s" % slitX.__class__.__name__
            raise BaseException(strMessage)
    def delSlitX(self): self._slitX = None
    slitX = property(getSlitX, setSlitX, delSlitX, "Property for slitX")
    # Methods and properties for the 'slitY' attribute
    def getSlitY(self): return self._slitY
    def setSlitY(self, slitY):
        if slitY is None:
            self._slitY = None
        elif slitY.__class__.__name__ == "XSDataDouble":
            self._slitY = slitY
        else:
            strMessage = "ERROR! XSDataInputFbest.setSlitY argument is not XSDataDouble but %s" % slitY.__class__.__name__
            raise BaseException(strMessage)
    def delSlitY(self): self._slitY = None
    slitY = property(getSlitY, setSlitY, delSlitY, "Property for slitY")
    # Methods and properties for the 'rotationRange' attribute
    def getRotationRange(self): return self._rotationRange
    def setRotationRange(self, rotationRange):
        if rotationRange is None:
            self._rotationRange = None
        elif rotationRange.__class__.__name__ == "XSDataDouble":
            self._rotationRange = rotationRange
        else:
            strMessage = "ERROR! XSDataInputFbest.setRotationRange argument is not XSDataDouble but %s" % rotationRange.__class__.__name__
            raise BaseException(strMessage)
    def delRotationRange(self): self._rotationRange = None
    rotationRange = property(getRotationRange, setRotationRange, delRotationRange, "Property for rotationRange")
    # Methods and properties for the 'rotationWidth' attribute
    def getRotationWidth(self): return self._rotationWidth
    def setRotationWidth(self, rotationWidth):
        if rotationWidth is None:
            self._rotationWidth = None
        elif rotationWidth.__class__.__name__ == "XSDataDouble":
            self._rotationWidth = rotationWidth
        else:
            strMessage = "ERROR! XSDataInputFbest.setRotationWidth argument is not XSDataDouble but %s" % rotationWidth.__class__.__name__
            raise BaseException(strMessage)
    def delRotationWidth(self): self._rotationWidth = None
    rotationWidth = property(getRotationWidth, setRotationWidth, delRotationWidth, "Property for rotationWidth")
    # Methods and properties for the 'minExposureTime' attribute
    def getMinExposureTime(self): return self._minExposureTime
    def setMinExposureTime(self, minExposureTime):
        if minExposureTime is None:
            self._minExposureTime = None
        elif minExposureTime.__class__.__name__ == "XSDataDouble":
            self._minExposureTime = minExposureTime
        else:
            strMessage = "ERROR! XSDataInputFbest.setMinExposureTime argument is not XSDataDouble but %s" % minExposureTime.__class__.__name__
            raise BaseException(strMessage)
    def delMinExposureTime(self): self._minExposureTime = None
    minExposureTime = property(getMinExposureTime, setMinExposureTime, delMinExposureTime, "Property for minExposureTime")
    # Methods and properties for the 'doseLimit' attribute
    def getDoseLimit(self): return self._doseLimit
    def setDoseLimit(self, doseLimit):
        if doseLimit is None:
            self._doseLimit = None
        elif doseLimit.__class__.__name__ == "XSDataDouble":
            self._doseLimit = doseLimit
        else:
            strMessage = "ERROR! XSDataInputFbest.setDoseLimit argument is not XSDataDouble but %s" % doseLimit.__class__.__name__
            raise BaseException(strMessage)
    def delDoseLimit(self): self._doseLimit = None
    doseLimit = property(getDoseLimit, setDoseLimit, delDoseLimit, "Property for doseLimit")
    # Methods and properties for the 'doseRate' attribute
    def getDoseRate(self): return self._doseRate
    def setDoseRate(self, doseRate):
        if doseRate is None:
            self._doseRate = None
        elif doseRate.__class__.__name__ == "XSDataDouble":
            self._doseRate = doseRate
        else:
            strMessage = "ERROR! XSDataInputFbest.setDoseRate argument is not XSDataDouble but %s" % doseRate.__class__.__name__
            raise BaseException(strMessage)
    def delDoseRate(self): self._doseRate = None
    doseRate = property(getDoseRate, setDoseRate, delDoseRate, "Property for doseRate")
    # Methods and properties for the 'sensitivity' attribute
    def getSensitivity(self): return self._sensitivity
    def setSensitivity(self, sensitivity):
        if sensitivity is None:
            self._sensitivity = None
        elif sensitivity.__class__.__name__ == "XSDataDouble":
            self._sensitivity = sensitivity
        else:
            strMessage = "ERROR! XSDataInputFbest.setSensitivity argument is not XSDataDouble but %s" % sensitivity.__class__.__name__
            raise BaseException(strMessage)
    def delSensitivity(self): self._sensitivity = None
    sensitivity = property(getSensitivity, setSensitivity, delSensitivity, "Property for sensitivity")
    # Methods and properties for the 'crystalSize' attribute
    def getCrystalSize(self): return self._crystalSize
    def setCrystalSize(self, crystalSize):
        if crystalSize is None:
            self._crystalSize = None
        elif crystalSize.__class__.__name__ == "XSDataDouble":
            self._crystalSize = crystalSize
        else:
            strMessage = "ERROR! XSDataInputFbest.setCrystalSize argument is not XSDataDouble but %s" % crystalSize.__class__.__name__
            raise BaseException(strMessage)
    def delCrystalSize(self): self._crystalSize = None
    crystalSize = property(getCrystalSize, setCrystalSize, delCrystalSize, "Property for crystalSize")
    def export(self, outfile, level, name_='XSDataInputFbest'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputFbest'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._flux is not None:
            self.flux.export(outfile, level, name_='flux')
        else:
            warnEmptyAttribute("flux", "XSDataDouble")
        if self._resolution is not None:
            self.resolution.export(outfile, level, name_='resolution')
        else:
            warnEmptyAttribute("resolution", "XSDataDouble")
        if self._beamH is not None:
            self.beamH.export(outfile, level, name_='beamH')
        if self._beamV is not None:
            self.beamV.export(outfile, level, name_='beamV')
        if self._wavelength is not None:
            self.wavelength.export(outfile, level, name_='wavelength')
        if self._aperture is not None:
            self.aperture.export(outfile, level, name_='aperture')
        if self._slitX is not None:
            self.slitX.export(outfile, level, name_='slitX')
        if self._slitY is not None:
            self.slitY.export(outfile, level, name_='slitY')
        if self._rotationRange is not None:
            self.rotationRange.export(outfile, level, name_='rotationRange')
        if self._rotationWidth is not None:
            self.rotationWidth.export(outfile, level, name_='rotationWidth')
        if self._minExposureTime is not None:
            self.minExposureTime.export(outfile, level, name_='minExposureTime')
        if self._doseLimit is not None:
            self.doseLimit.export(outfile, level, name_='doseLimit')
        if self._doseRate is not None:
            self.doseRate.export(outfile, level, name_='doseRate')
        if self._sensitivity is not None:
            self.sensitivity.export(outfile, level, name_='sensitivity')
        if self._crystalSize is not None:
            self.crystalSize.export(outfile, level, name_='crystalSize')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'flux':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setFlux(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamH':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamH(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamV':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamV(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'wavelength':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setWavelength(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aperture':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAperture(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'slitX':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setSlitX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'slitY':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setSlitY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotationRange':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRotationRange(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotationWidth':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRotationWidth(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minExposureTime':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMinExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'doseLimit':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDoseLimit(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'doseRate':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDoseRate(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sensitivity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setSensitivity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystalSize':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCrystalSize(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputFbest" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputFbest' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputFbest is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputFbest.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputFbest()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputFbest" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputFbest()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputFbest


class XSDataResultFbest(XSDataResult):
    def __init__(self, status=None, minExposure=None, sensitivity=None, doseRate=None, totalExposureTime=None, totalDose=None, resolution=None, rotationWidth=None, numberOfImages=None, transmission=None, exposureTimePerImage=None):
        XSDataResult.__init__(self, status)
        if exposureTimePerImage is None:
            self._exposureTimePerImage = None
        elif exposureTimePerImage.__class__.__name__ == "XSDataDouble":
            self._exposureTimePerImage = exposureTimePerImage
        else:
            strMessage = "ERROR! XSDataResultFbest constructor argument 'exposureTimePerImage' is not XSDataDouble but %s" % self._exposureTimePerImage.__class__.__name__
            raise BaseException(strMessage)
        if transmission is None:
            self._transmission = None
        elif transmission.__class__.__name__ == "XSDataDouble":
            self._transmission = transmission
        else:
            strMessage = "ERROR! XSDataResultFbest constructor argument 'transmission' is not XSDataDouble but %s" % self._transmission.__class__.__name__
            raise BaseException(strMessage)
        if numberOfImages is None:
            self._numberOfImages = None
        elif numberOfImages.__class__.__name__ == "XSDataDouble":
            self._numberOfImages = numberOfImages
        else:
            strMessage = "ERROR! XSDataResultFbest constructor argument 'numberOfImages' is not XSDataDouble but %s" % self._numberOfImages.__class__.__name__
            raise BaseException(strMessage)
        if rotationWidth is None:
            self._rotationWidth = None
        elif rotationWidth.__class__.__name__ == "XSDataDouble":
            self._rotationWidth = rotationWidth
        else:
            strMessage = "ERROR! XSDataResultFbest constructor argument 'rotationWidth' is not XSDataDouble but %s" % self._rotationWidth.__class__.__name__
            raise BaseException(strMessage)
        if resolution is None:
            self._resolution = None
        elif resolution.__class__.__name__ == "XSDataDouble":
            self._resolution = resolution
        else:
            strMessage = "ERROR! XSDataResultFbest constructor argument 'resolution' is not XSDataDouble but %s" % self._resolution.__class__.__name__
            raise BaseException(strMessage)
        if totalDose is None:
            self._totalDose = None
        elif totalDose.__class__.__name__ == "XSDataDouble":
            self._totalDose = totalDose
        else:
            strMessage = "ERROR! XSDataResultFbest constructor argument 'totalDose' is not XSDataDouble but %s" % self._totalDose.__class__.__name__
            raise BaseException(strMessage)
        if totalExposureTime is None:
            self._totalExposureTime = None
        elif totalExposureTime.__class__.__name__ == "XSDataDouble":
            self._totalExposureTime = totalExposureTime
        else:
            strMessage = "ERROR! XSDataResultFbest constructor argument 'totalExposureTime' is not XSDataDouble but %s" % self._totalExposureTime.__class__.__name__
            raise BaseException(strMessage)
        if doseRate is None:
            self._doseRate = None
        elif doseRate.__class__.__name__ == "XSDataDouble":
            self._doseRate = doseRate
        else:
            strMessage = "ERROR! XSDataResultFbest constructor argument 'doseRate' is not XSDataDouble but %s" % self._doseRate.__class__.__name__
            raise BaseException(strMessage)
        if sensitivity is None:
            self._sensitivity = None
        elif sensitivity.__class__.__name__ == "XSDataDouble":
            self._sensitivity = sensitivity
        else:
            strMessage = "ERROR! XSDataResultFbest constructor argument 'sensitivity' is not XSDataDouble but %s" % self._sensitivity.__class__.__name__
            raise BaseException(strMessage)
        if minExposure is None:
            self._minExposure = None
        elif minExposure.__class__.__name__ == "XSDataDouble":
            self._minExposure = minExposure
        else:
            strMessage = "ERROR! XSDataResultFbest constructor argument 'minExposure' is not XSDataDouble but %s" % self._minExposure.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'exposureTimePerImage' attribute
    def getExposureTimePerImage(self): return self._exposureTimePerImage
    def setExposureTimePerImage(self, exposureTimePerImage):
        if exposureTimePerImage is None:
            self._exposureTimePerImage = None
        elif exposureTimePerImage.__class__.__name__ == "XSDataDouble":
            self._exposureTimePerImage = exposureTimePerImage
        else:
            strMessage = "ERROR! XSDataResultFbest.setExposureTimePerImage argument is not XSDataDouble but %s" % exposureTimePerImage.__class__.__name__
            raise BaseException(strMessage)
    def delExposureTimePerImage(self): self._exposureTimePerImage = None
    exposureTimePerImage = property(getExposureTimePerImage, setExposureTimePerImage, delExposureTimePerImage, "Property for exposureTimePerImage")
    # Methods and properties for the 'transmission' attribute
    def getTransmission(self): return self._transmission
    def setTransmission(self, transmission):
        if transmission is None:
            self._transmission = None
        elif transmission.__class__.__name__ == "XSDataDouble":
            self._transmission = transmission
        else:
            strMessage = "ERROR! XSDataResultFbest.setTransmission argument is not XSDataDouble but %s" % transmission.__class__.__name__
            raise BaseException(strMessage)
    def delTransmission(self): self._transmission = None
    transmission = property(getTransmission, setTransmission, delTransmission, "Property for transmission")
    # Methods and properties for the 'numberOfImages' attribute
    def getNumberOfImages(self): return self._numberOfImages
    def setNumberOfImages(self, numberOfImages):
        if numberOfImages is None:
            self._numberOfImages = None
        elif numberOfImages.__class__.__name__ == "XSDataDouble":
            self._numberOfImages = numberOfImages
        else:
            strMessage = "ERROR! XSDataResultFbest.setNumberOfImages argument is not XSDataDouble but %s" % numberOfImages.__class__.__name__
            raise BaseException(strMessage)
    def delNumberOfImages(self): self._numberOfImages = None
    numberOfImages = property(getNumberOfImages, setNumberOfImages, delNumberOfImages, "Property for numberOfImages")
    # Methods and properties for the 'rotationWidth' attribute
    def getRotationWidth(self): return self._rotationWidth
    def setRotationWidth(self, rotationWidth):
        if rotationWidth is None:
            self._rotationWidth = None
        elif rotationWidth.__class__.__name__ == "XSDataDouble":
            self._rotationWidth = rotationWidth
        else:
            strMessage = "ERROR! XSDataResultFbest.setRotationWidth argument is not XSDataDouble but %s" % rotationWidth.__class__.__name__
            raise BaseException(strMessage)
    def delRotationWidth(self): self._rotationWidth = None
    rotationWidth = property(getRotationWidth, setRotationWidth, delRotationWidth, "Property for rotationWidth")
    # Methods and properties for the 'resolution' attribute
    def getResolution(self): return self._resolution
    def setResolution(self, resolution):
        if resolution is None:
            self._resolution = None
        elif resolution.__class__.__name__ == "XSDataDouble":
            self._resolution = resolution
        else:
            strMessage = "ERROR! XSDataResultFbest.setResolution argument is not XSDataDouble but %s" % resolution.__class__.__name__
            raise BaseException(strMessage)
    def delResolution(self): self._resolution = None
    resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
    # Methods and properties for the 'totalDose' attribute
    def getTotalDose(self): return self._totalDose
    def setTotalDose(self, totalDose):
        if totalDose is None:
            self._totalDose = None
        elif totalDose.__class__.__name__ == "XSDataDouble":
            self._totalDose = totalDose
        else:
            strMessage = "ERROR! XSDataResultFbest.setTotalDose argument is not XSDataDouble but %s" % totalDose.__class__.__name__
            raise BaseException(strMessage)
    def delTotalDose(self): self._totalDose = None
    totalDose = property(getTotalDose, setTotalDose, delTotalDose, "Property for totalDose")
    # Methods and properties for the 'totalExposureTime' attribute
    def getTotalExposureTime(self): return self._totalExposureTime
    def setTotalExposureTime(self, totalExposureTime):
        if totalExposureTime is None:
            self._totalExposureTime = None
        elif totalExposureTime.__class__.__name__ == "XSDataDouble":
            self._totalExposureTime = totalExposureTime
        else:
            strMessage = "ERROR! XSDataResultFbest.setTotalExposureTime argument is not XSDataDouble but %s" % totalExposureTime.__class__.__name__
            raise BaseException(strMessage)
    def delTotalExposureTime(self): self._totalExposureTime = None
    totalExposureTime = property(getTotalExposureTime, setTotalExposureTime, delTotalExposureTime, "Property for totalExposureTime")
    # Methods and properties for the 'doseRate' attribute
    def getDoseRate(self): return self._doseRate
    def setDoseRate(self, doseRate):
        if doseRate is None:
            self._doseRate = None
        elif doseRate.__class__.__name__ == "XSDataDouble":
            self._doseRate = doseRate
        else:
            strMessage = "ERROR! XSDataResultFbest.setDoseRate argument is not XSDataDouble but %s" % doseRate.__class__.__name__
            raise BaseException(strMessage)
    def delDoseRate(self): self._doseRate = None
    doseRate = property(getDoseRate, setDoseRate, delDoseRate, "Property for doseRate")
    # Methods and properties for the 'sensitivity' attribute
    def getSensitivity(self): return self._sensitivity
    def setSensitivity(self, sensitivity):
        if sensitivity is None:
            self._sensitivity = None
        elif sensitivity.__class__.__name__ == "XSDataDouble":
            self._sensitivity = sensitivity
        else:
            strMessage = "ERROR! XSDataResultFbest.setSensitivity argument is not XSDataDouble but %s" % sensitivity.__class__.__name__
            raise BaseException(strMessage)
    def delSensitivity(self): self._sensitivity = None
    sensitivity = property(getSensitivity, setSensitivity, delSensitivity, "Property for sensitivity")
    # Methods and properties for the 'minExposure' attribute
    def getMinExposure(self): return self._minExposure
    def setMinExposure(self, minExposure):
        if minExposure is None:
            self._minExposure = None
        elif minExposure.__class__.__name__ == "XSDataDouble":
            self._minExposure = minExposure
        else:
            strMessage = "ERROR! XSDataResultFbest.setMinExposure argument is not XSDataDouble but %s" % minExposure.__class__.__name__
            raise BaseException(strMessage)
    def delMinExposure(self): self._minExposure = None
    minExposure = property(getMinExposure, setMinExposure, delMinExposure, "Property for minExposure")
    def export(self, outfile, level, name_='XSDataResultFbest'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultFbest'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._exposureTimePerImage is not None:
            self.exposureTimePerImage.export(outfile, level, name_='exposureTimePerImage')
        if self._transmission is not None:
            self.transmission.export(outfile, level, name_='transmission')
        if self._numberOfImages is not None:
            self.numberOfImages.export(outfile, level, name_='numberOfImages')
        if self._rotationWidth is not None:
            self.rotationWidth.export(outfile, level, name_='rotationWidth')
        if self._resolution is not None:
            self.resolution.export(outfile, level, name_='resolution')
        if self._totalDose is not None:
            self.totalDose.export(outfile, level, name_='totalDose')
        if self._totalExposureTime is not None:
            self.totalExposureTime.export(outfile, level, name_='totalExposureTime')
        if self._doseRate is not None:
            self.doseRate.export(outfile, level, name_='doseRate')
        if self._sensitivity is not None:
            self.sensitivity.export(outfile, level, name_='sensitivity')
        if self._minExposure is not None:
            self.minExposure.export(outfile, level, name_='minExposure')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exposureTimePerImage':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setExposureTimePerImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'transmission':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTransmission(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'numberOfImages':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setNumberOfImages(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotationWidth':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRotationWidth(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'totalDose':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTotalDose(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'totalExposureTime':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTotalExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'doseRate':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDoseRate(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sensitivity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setSensitivity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minExposure':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMinExposure(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultFbest" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultFbest' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultFbest is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultFbest.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultFbest()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultFbest" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultFbest()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultFbest



# End of data representation classes.


