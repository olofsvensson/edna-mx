#!/usr/bin/env python

#
# Generated Wed Apr 1 10:18::04 2015 by EDGenerateDS.
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
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
}

try:
    from XSDataCommon import XSData
    from XSDataCommon import XSDataDouble
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataMatrixDouble
    from XSDataCommon import XSDataResult
    from XSDataCommon import XSDataString
    from XSDataCommon import XSDataLength
    from XSDataCommon import XSDataAngle
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
from XSDataCommon import XSData
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataMatrixDouble
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataAngle




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



class XSDataXOalignCell(XSData):
    def __init__(self, length_c=None, length_b=None, length_a=None, angle_gamma=None, angle_beta=None, angle_alpha=None):
        XSData.__init__(self, )
        if angle_alpha is None:
            self._angle_alpha = None
        elif angle_alpha.__class__.__name__ == "XSDataAngle":
            self._angle_alpha = angle_alpha
        else:
            strMessage = "ERROR! XSDataXOalignCell constructor argument 'angle_alpha' is not XSDataAngle but %s" % self._angle_alpha.__class__.__name__
            raise BaseException(strMessage)
        if angle_beta is None:
            self._angle_beta = None
        elif angle_beta.__class__.__name__ == "XSDataAngle":
            self._angle_beta = angle_beta
        else:
            strMessage = "ERROR! XSDataXOalignCell constructor argument 'angle_beta' is not XSDataAngle but %s" % self._angle_beta.__class__.__name__
            raise BaseException(strMessage)
        if angle_gamma is None:
            self._angle_gamma = None
        elif angle_gamma.__class__.__name__ == "XSDataAngle":
            self._angle_gamma = angle_gamma
        else:
            strMessage = "ERROR! XSDataXOalignCell constructor argument 'angle_gamma' is not XSDataAngle but %s" % self._angle_gamma.__class__.__name__
            raise BaseException(strMessage)
        if length_a is None:
            self._length_a = None
        elif length_a.__class__.__name__ == "XSDataLength":
            self._length_a = length_a
        else:
            strMessage = "ERROR! XSDataXOalignCell constructor argument 'length_a' is not XSDataLength but %s" % self._length_a.__class__.__name__
            raise BaseException(strMessage)
        if length_b is None:
            self._length_b = None
        elif length_b.__class__.__name__ == "XSDataLength":
            self._length_b = length_b
        else:
            strMessage = "ERROR! XSDataXOalignCell constructor argument 'length_b' is not XSDataLength but %s" % self._length_b.__class__.__name__
            raise BaseException(strMessage)
        if length_c is None:
            self._length_c = None
        elif length_c.__class__.__name__ == "XSDataLength":
            self._length_c = length_c
        else:
            strMessage = "ERROR! XSDataXOalignCell constructor argument 'length_c' is not XSDataLength but %s" % self._length_c.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'angle_alpha' attribute
    def getAngle_alpha(self): return self._angle_alpha
    def setAngle_alpha(self, angle_alpha):
        if angle_alpha is None:
            self._angle_alpha = None
        elif angle_alpha.__class__.__name__ == "XSDataAngle":
            self._angle_alpha = angle_alpha
        else:
            strMessage = "ERROR! XSDataXOalignCell.setAngle_alpha argument is not XSDataAngle but %s" % angle_alpha.__class__.__name__
            raise BaseException(strMessage)
    def delAngle_alpha(self): self._angle_alpha = None
    angle_alpha = property(getAngle_alpha, setAngle_alpha, delAngle_alpha, "Property for angle_alpha")
    # Methods and properties for the 'angle_beta' attribute
    def getAngle_beta(self): return self._angle_beta
    def setAngle_beta(self, angle_beta):
        if angle_beta is None:
            self._angle_beta = None
        elif angle_beta.__class__.__name__ == "XSDataAngle":
            self._angle_beta = angle_beta
        else:
            strMessage = "ERROR! XSDataXOalignCell.setAngle_beta argument is not XSDataAngle but %s" % angle_beta.__class__.__name__
            raise BaseException(strMessage)
    def delAngle_beta(self): self._angle_beta = None
    angle_beta = property(getAngle_beta, setAngle_beta, delAngle_beta, "Property for angle_beta")
    # Methods and properties for the 'angle_gamma' attribute
    def getAngle_gamma(self): return self._angle_gamma
    def setAngle_gamma(self, angle_gamma):
        if angle_gamma is None:
            self._angle_gamma = None
        elif angle_gamma.__class__.__name__ == "XSDataAngle":
            self._angle_gamma = angle_gamma
        else:
            strMessage = "ERROR! XSDataXOalignCell.setAngle_gamma argument is not XSDataAngle but %s" % angle_gamma.__class__.__name__
            raise BaseException(strMessage)
    def delAngle_gamma(self): self._angle_gamma = None
    angle_gamma = property(getAngle_gamma, setAngle_gamma, delAngle_gamma, "Property for angle_gamma")
    # Methods and properties for the 'length_a' attribute
    def getLength_a(self): return self._length_a
    def setLength_a(self, length_a):
        if length_a is None:
            self._length_a = None
        elif length_a.__class__.__name__ == "XSDataLength":
            self._length_a = length_a
        else:
            strMessage = "ERROR! XSDataXOalignCell.setLength_a argument is not XSDataLength but %s" % length_a.__class__.__name__
            raise BaseException(strMessage)
    def delLength_a(self): self._length_a = None
    length_a = property(getLength_a, setLength_a, delLength_a, "Property for length_a")
    # Methods and properties for the 'length_b' attribute
    def getLength_b(self): return self._length_b
    def setLength_b(self, length_b):
        if length_b is None:
            self._length_b = None
        elif length_b.__class__.__name__ == "XSDataLength":
            self._length_b = length_b
        else:
            strMessage = "ERROR! XSDataXOalignCell.setLength_b argument is not XSDataLength but %s" % length_b.__class__.__name__
            raise BaseException(strMessage)
    def delLength_b(self): self._length_b = None
    length_b = property(getLength_b, setLength_b, delLength_b, "Property for length_b")
    # Methods and properties for the 'length_c' attribute
    def getLength_c(self): return self._length_c
    def setLength_c(self, length_c):
        if length_c is None:
            self._length_c = None
        elif length_c.__class__.__name__ == "XSDataLength":
            self._length_c = length_c
        else:
            strMessage = "ERROR! XSDataXOalignCell.setLength_c argument is not XSDataLength but %s" % length_c.__class__.__name__
            raise BaseException(strMessage)
    def delLength_c(self): self._length_c = None
    length_c = property(getLength_c, setLength_c, delLength_c, "Property for length_c")
    def export(self, outfile, level, name_='XSDataXOalignCell'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXOalignCell'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._angle_alpha is not None:
            self.angle_alpha.export(outfile, level, name_='angle_alpha')
        else:
            warnEmptyAttribute("angle_alpha", "XSDataAngle")
        if self._angle_beta is not None:
            self.angle_beta.export(outfile, level, name_='angle_beta')
        else:
            warnEmptyAttribute("angle_beta", "XSDataAngle")
        if self._angle_gamma is not None:
            self.angle_gamma.export(outfile, level, name_='angle_gamma')
        else:
            warnEmptyAttribute("angle_gamma", "XSDataAngle")
        if self._length_a is not None:
            self.length_a.export(outfile, level, name_='length_a')
        else:
            warnEmptyAttribute("length_a", "XSDataLength")
        if self._length_b is not None:
            self.length_b.export(outfile, level, name_='length_b')
        else:
            warnEmptyAttribute("length_b", "XSDataLength")
        if self._length_c is not None:
            self.length_c.export(outfile, level, name_='length_c')
        else:
            warnEmptyAttribute("length_c", "XSDataLength")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'angle_alpha':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setAngle_alpha(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'angle_beta':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setAngle_beta(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'angle_gamma':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setAngle_gamma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'length_a':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setLength_a(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'length_b':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setLength_b(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'length_c':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setLength_c(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXOalignCell" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXOalignCell' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXOalignCell is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXOalignCell.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXOalignCell()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXOalignCell" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXOalignCell()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXOalignCell


class XSDataXOalignOrientation(XSData):
    def __init__(self, matrixU=None, matrixA=None):
        XSData.__init__(self, )
        if matrixA is None:
            self._matrixA = None
        elif matrixA.__class__.__name__ == "XSDataMatrixDouble":
            self._matrixA = matrixA
        else:
            strMessage = "ERROR! XSDataXOalignOrientation constructor argument 'matrixA' is not XSDataMatrixDouble but %s" % self._matrixA.__class__.__name__
            raise BaseException(strMessage)
        if matrixU is None:
            self._matrixU = None
        elif matrixU.__class__.__name__ == "XSDataMatrixDouble":
            self._matrixU = matrixU
        else:
            strMessage = "ERROR! XSDataXOalignOrientation constructor argument 'matrixU' is not XSDataMatrixDouble but %s" % self._matrixU.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'matrixA' attribute
    def getMatrixA(self): return self._matrixA
    def setMatrixA(self, matrixA):
        if matrixA is None:
            self._matrixA = None
        elif matrixA.__class__.__name__ == "XSDataMatrixDouble":
            self._matrixA = matrixA
        else:
            strMessage = "ERROR! XSDataXOalignOrientation.setMatrixA argument is not XSDataMatrixDouble but %s" % matrixA.__class__.__name__
            raise BaseException(strMessage)
    def delMatrixA(self): self._matrixA = None
    matrixA = property(getMatrixA, setMatrixA, delMatrixA, "Property for matrixA")
    # Methods and properties for the 'matrixU' attribute
    def getMatrixU(self): return self._matrixU
    def setMatrixU(self, matrixU):
        if matrixU is None:
            self._matrixU = None
        elif matrixU.__class__.__name__ == "XSDataMatrixDouble":
            self._matrixU = matrixU
        else:
            strMessage = "ERROR! XSDataXOalignOrientation.setMatrixU argument is not XSDataMatrixDouble but %s" % matrixU.__class__.__name__
            raise BaseException(strMessage)
    def delMatrixU(self): self._matrixU = None
    matrixU = property(getMatrixU, setMatrixU, delMatrixU, "Property for matrixU")
    def export(self, outfile, level, name_='XSDataXOalignOrientation'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXOalignOrientation'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._matrixA is not None:
            self.matrixA.export(outfile, level, name_='matrixA')
        else:
            warnEmptyAttribute("matrixA", "XSDataMatrixDouble")
        if self._matrixU is not None:
            self.matrixU.export(outfile, level, name_='matrixU')
        else:
            warnEmptyAttribute("matrixU", "XSDataMatrixDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'matrixA':
            obj_ = XSDataMatrixDouble()
            obj_.build(child_)
            self.setMatrixA(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'matrixU':
            obj_ = XSDataMatrixDouble()
            obj_.build(child_)
            self.setMatrixU(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXOalignOrientation" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXOalignOrientation' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXOalignOrientation is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXOalignOrientation.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXOalignOrientation()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXOalignOrientation" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXOalignOrientation()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXOalignOrientation


class XSDataXOalignSolution(XSData):
    def __init__(self, settings=None, phi=None, kappa=None):
        XSData.__init__(self, )
        if kappa is None:
            self._kappa = None
        elif kappa.__class__.__name__ == "XSDataDouble":
            self._kappa = kappa
        else:
            strMessage = "ERROR! XSDataXOalignSolution constructor argument 'kappa' is not XSDataDouble but %s" % self._kappa.__class__.__name__
            raise BaseException(strMessage)
        if phi is None:
            self._phi = None
        elif phi.__class__.__name__ == "XSDataDouble":
            self._phi = phi
        else:
            strMessage = "ERROR! XSDataXOalignSolution constructor argument 'phi' is not XSDataDouble but %s" % self._phi.__class__.__name__
            raise BaseException(strMessage)
        if settings is None:
            self._settings = None
        elif settings.__class__.__name__ == "XSDataString":
            self._settings = settings
        else:
            strMessage = "ERROR! XSDataXOalignSolution constructor argument 'settings' is not XSDataString but %s" % self._settings.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'kappa' attribute
    def getKappa(self): return self._kappa
    def setKappa(self, kappa):
        if kappa is None:
            self._kappa = None
        elif kappa.__class__.__name__ == "XSDataDouble":
            self._kappa = kappa
        else:
            strMessage = "ERROR! XSDataXOalignSolution.setKappa argument is not XSDataDouble but %s" % kappa.__class__.__name__
            raise BaseException(strMessage)
    def delKappa(self): self._kappa = None
    kappa = property(getKappa, setKappa, delKappa, "Property for kappa")
    # Methods and properties for the 'phi' attribute
    def getPhi(self): return self._phi
    def setPhi(self, phi):
        if phi is None:
            self._phi = None
        elif phi.__class__.__name__ == "XSDataDouble":
            self._phi = phi
        else:
            strMessage = "ERROR! XSDataXOalignSolution.setPhi argument is not XSDataDouble but %s" % phi.__class__.__name__
            raise BaseException(strMessage)
    def delPhi(self): self._phi = None
    phi = property(getPhi, setPhi, delPhi, "Property for phi")
    # Methods and properties for the 'settings' attribute
    def getSettings(self): return self._settings
    def setSettings(self, settings):
        if settings is None:
            self._settings = None
        elif settings.__class__.__name__ == "XSDataString":
            self._settings = settings
        else:
            strMessage = "ERROR! XSDataXOalignSolution.setSettings argument is not XSDataString but %s" % settings.__class__.__name__
            raise BaseException(strMessage)
    def delSettings(self): self._settings = None
    settings = property(getSettings, setSettings, delSettings, "Property for settings")
    def export(self, outfile, level, name_='XSDataXOalignSolution'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXOalignSolution'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._kappa is not None:
            self.kappa.export(outfile, level, name_='kappa')
        else:
            warnEmptyAttribute("kappa", "XSDataDouble")
        if self._phi is not None:
            self.phi.export(outfile, level, name_='phi')
        else:
            warnEmptyAttribute("phi", "XSDataDouble")
        if self._settings is not None:
            self.settings.export(outfile, level, name_='settings')
        else:
            warnEmptyAttribute("settings", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kappa':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setKappa(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phi':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setPhi(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'settings':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSettings(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXOalignSolution" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXOalignSolution' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXOalignSolution is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXOalignSolution.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXOalignSolution()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXOalignSolution" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXOalignSolution()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXOalignSolution


class XSDataInputXOalign(XSDataInput):
    def __init__(self, configuration=None, phi=None, kappa=None, omega=None, cell=None, orientation=None, symmetry=None):
        XSDataInput.__init__(self, configuration)
        if symmetry is None:
            self._symmetry = None
        elif symmetry.__class__.__name__ == "XSDataString":
            self._symmetry = symmetry
        else:
            strMessage = "ERROR! XSDataInputXOalign constructor argument 'symmetry' is not XSDataString but %s" % self._symmetry.__class__.__name__
            raise BaseException(strMessage)
        if orientation is None:
            self._orientation = None
        elif orientation.__class__.__name__ == "XSDataXOalignOrientation":
            self._orientation = orientation
        else:
            strMessage = "ERROR! XSDataInputXOalign constructor argument 'orientation' is not XSDataXOalignOrientation but %s" % self._orientation.__class__.__name__
            raise BaseException(strMessage)
        if cell is None:
            self._cell = None
        elif cell.__class__.__name__ == "XSDataXOalignCell":
            self._cell = cell
        else:
            strMessage = "ERROR! XSDataInputXOalign constructor argument 'cell' is not XSDataXOalignCell but %s" % self._cell.__class__.__name__
            raise BaseException(strMessage)
        if omega is None:
            self._omega = None
        elif omega.__class__.__name__ == "XSDataAngle":
            self._omega = omega
        else:
            strMessage = "ERROR! XSDataInputXOalign constructor argument 'omega' is not XSDataAngle but %s" % self._omega.__class__.__name__
            raise BaseException(strMessage)
        if kappa is None:
            self._kappa = None
        elif kappa.__class__.__name__ == "XSDataAngle":
            self._kappa = kappa
        else:
            strMessage = "ERROR! XSDataInputXOalign constructor argument 'kappa' is not XSDataAngle but %s" % self._kappa.__class__.__name__
            raise BaseException(strMessage)
        if phi is None:
            self._phi = None
        elif phi.__class__.__name__ == "XSDataAngle":
            self._phi = phi
        else:
            strMessage = "ERROR! XSDataInputXOalign constructor argument 'phi' is not XSDataAngle but %s" % self._phi.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'symmetry' attribute
    def getSymmetry(self): return self._symmetry
    def setSymmetry(self, symmetry):
        if symmetry is None:
            self._symmetry = None
        elif symmetry.__class__.__name__ == "XSDataString":
            self._symmetry = symmetry
        else:
            strMessage = "ERROR! XSDataInputXOalign.setSymmetry argument is not XSDataString but %s" % symmetry.__class__.__name__
            raise BaseException(strMessage)
    def delSymmetry(self): self._symmetry = None
    symmetry = property(getSymmetry, setSymmetry, delSymmetry, "Property for symmetry")
    # Methods and properties for the 'orientation' attribute
    def getOrientation(self): return self._orientation
    def setOrientation(self, orientation):
        if orientation is None:
            self._orientation = None
        elif orientation.__class__.__name__ == "XSDataXOalignOrientation":
            self._orientation = orientation
        else:
            strMessage = "ERROR! XSDataInputXOalign.setOrientation argument is not XSDataXOalignOrientation but %s" % orientation.__class__.__name__
            raise BaseException(strMessage)
    def delOrientation(self): self._orientation = None
    orientation = property(getOrientation, setOrientation, delOrientation, "Property for orientation")
    # Methods and properties for the 'cell' attribute
    def getCell(self): return self._cell
    def setCell(self, cell):
        if cell is None:
            self._cell = None
        elif cell.__class__.__name__ == "XSDataXOalignCell":
            self._cell = cell
        else:
            strMessage = "ERROR! XSDataInputXOalign.setCell argument is not XSDataXOalignCell but %s" % cell.__class__.__name__
            raise BaseException(strMessage)
    def delCell(self): self._cell = None
    cell = property(getCell, setCell, delCell, "Property for cell")
    # Methods and properties for the 'omega' attribute
    def getOmega(self): return self._omega
    def setOmega(self, omega):
        if omega is None:
            self._omega = None
        elif omega.__class__.__name__ == "XSDataAngle":
            self._omega = omega
        else:
            strMessage = "ERROR! XSDataInputXOalign.setOmega argument is not XSDataAngle but %s" % omega.__class__.__name__
            raise BaseException(strMessage)
    def delOmega(self): self._omega = None
    omega = property(getOmega, setOmega, delOmega, "Property for omega")
    # Methods and properties for the 'kappa' attribute
    def getKappa(self): return self._kappa
    def setKappa(self, kappa):
        if kappa is None:
            self._kappa = None
        elif kappa.__class__.__name__ == "XSDataAngle":
            self._kappa = kappa
        else:
            strMessage = "ERROR! XSDataInputXOalign.setKappa argument is not XSDataAngle but %s" % kappa.__class__.__name__
            raise BaseException(strMessage)
    def delKappa(self): self._kappa = None
    kappa = property(getKappa, setKappa, delKappa, "Property for kappa")
    # Methods and properties for the 'phi' attribute
    def getPhi(self): return self._phi
    def setPhi(self, phi):
        if phi is None:
            self._phi = None
        elif phi.__class__.__name__ == "XSDataAngle":
            self._phi = phi
        else:
            strMessage = "ERROR! XSDataInputXOalign.setPhi argument is not XSDataAngle but %s" % phi.__class__.__name__
            raise BaseException(strMessage)
    def delPhi(self): self._phi = None
    phi = property(getPhi, setPhi, delPhi, "Property for phi")
    def export(self, outfile, level, name_='XSDataInputXOalign'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputXOalign'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._symmetry is not None:
            self.symmetry.export(outfile, level, name_='symmetry')
        else:
            warnEmptyAttribute("symmetry", "XSDataString")
        if self._orientation is not None:
            self.orientation.export(outfile, level, name_='orientation')
        else:
            warnEmptyAttribute("orientation", "XSDataXOalignOrientation")
        if self._cell is not None:
            self.cell.export(outfile, level, name_='cell')
        else:
            warnEmptyAttribute("cell", "XSDataXOalignCell")
        if self._omega is not None:
            self.omega.export(outfile, level, name_='omega')
        if self._kappa is not None:
            self.kappa.export(outfile, level, name_='kappa')
        if self._phi is not None:
            self.phi.export(outfile, level, name_='phi')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'symmetry':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSymmetry(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'orientation':
            obj_ = XSDataXOalignOrientation()
            obj_.build(child_)
            self.setOrientation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell':
            obj_ = XSDataXOalignCell()
            obj_.build(child_)
            self.setCell(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'omega':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setOmega(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kappa':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setKappa(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phi':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setPhi(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputXOalign" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputXOalign' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputXOalign is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputXOalign.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputXOalign()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputXOalign" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputXOalign()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputXOalign


class XSDataResultXOalign(XSDataResult):
    def __init__(self, status=None, solution=None, logFile=None):
        XSDataResult.__init__(self, status)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultXOalign constructor argument 'logFile' is not XSDataFile but %s" % self._logFile.__class__.__name__
            raise BaseException(strMessage)
        if solution is None:
            self._solution = []
        elif solution.__class__.__name__ == "list":
            self._solution = solution
        else:
            strMessage = "ERROR! XSDataResultXOalign constructor argument 'solution' is not list but %s" % self._solution.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultXOalign.setLogFile argument is not XSDataFile but %s" % logFile.__class__.__name__
            raise BaseException(strMessage)
    def delLogFile(self): self._logFile = None
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    # Methods and properties for the 'solution' attribute
    def getSolution(self): return self._solution
    def setSolution(self, solution):
        if solution is None:
            self._solution = []
        elif solution.__class__.__name__ == "list":
            self._solution = solution
        else:
            strMessage = "ERROR! XSDataResultXOalign.setSolution argument is not list but %s" % solution.__class__.__name__
            raise BaseException(strMessage)
    def delSolution(self): self._solution = None
    solution = property(getSolution, setSolution, delSolution, "Property for solution")
    def addSolution(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultXOalign.addSolution argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXOalignSolution":
            self._solution.append(value)
        else:
            strMessage = "ERROR! XSDataResultXOalign.addSolution argument is not XSDataXOalignSolution but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertSolution(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultXOalign.insertSolution argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultXOalign.insertSolution argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXOalignSolution":
            self._solution[index] = value
        else:
            strMessage = "ERROR! XSDataResultXOalign.addSolution argument is not XSDataXOalignSolution but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataResultXOalign'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultXOalign'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_='logFile')
        for solution_ in self.getSolution():
            solution_.export(outfile, level, name_='solution')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'logFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'solution':
            obj_ = XSDataXOalignSolution()
            obj_.build(child_)
            self.solution.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultXOalign" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultXOalign' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultXOalign is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultXOalign.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultXOalign()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultXOalign" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultXOalign()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultXOalign



# End of data representation classes.


