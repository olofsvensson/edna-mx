#!/usr/bin/env python

#
# Generated Wed Jul 3 05:33::08 2019 by EDGenerateDS.
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
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
 "XSDataCommon": "kernel/datamodel", \
}

try:
    from XSDataCommon import XSData
    from XSDataCommon import XSDataBoolean
    from XSDataCommon import XSDataDouble
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataFloat
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataInteger
    from XSDataCommon import XSDataResult
    from XSDataCommon import XSDataString
    from XSDataCommon import XSDataVectorDouble
    from XSDataCommon import XSDataLength
    from XSDataCommon import XSDataWavelength
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
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
from XSDataCommon import XSDataVectorDouble
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataWavelength
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



class XSData2DCoordinates(object):
    def __init__(self, y=None, x=None):
        if x is None:
            self._x = None
        elif x.__class__.__name__ == "XSDataDouble":
            self._x = x
        else:
            strMessage = "ERROR! XSData2DCoordinates constructor argument 'x' is not XSDataDouble but %s" % self._x.__class__.__name__
            raise BaseException(strMessage)
        if y is None:
            self._y = None
        elif y.__class__.__name__ == "XSDataDouble":
            self._y = y
        else:
            strMessage = "ERROR! XSData2DCoordinates constructor argument 'y' is not XSDataDouble but %s" % self._y.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'x' attribute
    def getX(self): return self._x
    def setX(self, x):
        if x is None:
            self._x = None
        elif x.__class__.__name__ == "XSDataDouble":
            self._x = x
        else:
            strMessage = "ERROR! XSData2DCoordinates.setX argument is not XSDataDouble but %s" % x.__class__.__name__
            raise BaseException(strMessage)
    def delX(self): self._x = None
    x = property(getX, setX, delX, "Property for x")
    # Methods and properties for the 'y' attribute
    def getY(self): return self._y
    def setY(self, y):
        if y is None:
            self._y = None
        elif y.__class__.__name__ == "XSDataDouble":
            self._y = y
        else:
            strMessage = "ERROR! XSData2DCoordinates.setY argument is not XSDataDouble but %s" % y.__class__.__name__
            raise BaseException(strMessage)
    def delY(self): self._y = None
    y = property(getY, setY, delY, "Property for y")
    def export(self, outfile, level, name_='XSData2DCoordinates'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSData2DCoordinates'):
        pass
        if self._x is not None:
            self.x.export(outfile, level, name_='x')
        else:
            warnEmptyAttribute("x", "XSDataDouble")
        if self._y is not None:
            self.y.export(outfile, level, name_='y')
        else:
            warnEmptyAttribute("y", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'x':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'y':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setY(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSData2DCoordinates" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSData2DCoordinates' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSData2DCoordinates is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSData2DCoordinates.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSData2DCoordinates()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSData2DCoordinates" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSData2DCoordinates()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSData2DCoordinates


class XSDataCell(object):
    def __init__(self, length_c=None, length_b=None, length_a=None, angle_gamma=None, angle_beta=None, angle_alpha=None):
        if angle_alpha is None:
            self._angle_alpha = None
        elif angle_alpha.__class__.__name__ == "XSDataAngle":
            self._angle_alpha = angle_alpha
        else:
            strMessage = "ERROR! XSDataCell constructor argument 'angle_alpha' is not XSDataAngle but %s" % self._angle_alpha.__class__.__name__
            raise BaseException(strMessage)
        if angle_beta is None:
            self._angle_beta = None
        elif angle_beta.__class__.__name__ == "XSDataAngle":
            self._angle_beta = angle_beta
        else:
            strMessage = "ERROR! XSDataCell constructor argument 'angle_beta' is not XSDataAngle but %s" % self._angle_beta.__class__.__name__
            raise BaseException(strMessage)
        if angle_gamma is None:
            self._angle_gamma = None
        elif angle_gamma.__class__.__name__ == "XSDataAngle":
            self._angle_gamma = angle_gamma
        else:
            strMessage = "ERROR! XSDataCell constructor argument 'angle_gamma' is not XSDataAngle but %s" % self._angle_gamma.__class__.__name__
            raise BaseException(strMessage)
        if length_a is None:
            self._length_a = None
        elif length_a.__class__.__name__ == "XSDataLength":
            self._length_a = length_a
        else:
            strMessage = "ERROR! XSDataCell constructor argument 'length_a' is not XSDataLength but %s" % self._length_a.__class__.__name__
            raise BaseException(strMessage)
        if length_b is None:
            self._length_b = None
        elif length_b.__class__.__name__ == "XSDataLength":
            self._length_b = length_b
        else:
            strMessage = "ERROR! XSDataCell constructor argument 'length_b' is not XSDataLength but %s" % self._length_b.__class__.__name__
            raise BaseException(strMessage)
        if length_c is None:
            self._length_c = None
        elif length_c.__class__.__name__ == "XSDataLength":
            self._length_c = length_c
        else:
            strMessage = "ERROR! XSDataCell constructor argument 'length_c' is not XSDataLength but %s" % self._length_c.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'angle_alpha' attribute
    def getAngle_alpha(self): return self._angle_alpha
    def setAngle_alpha(self, angle_alpha):
        if angle_alpha is None:
            self._angle_alpha = None
        elif angle_alpha.__class__.__name__ == "XSDataAngle":
            self._angle_alpha = angle_alpha
        else:
            strMessage = "ERROR! XSDataCell.setAngle_alpha argument is not XSDataAngle but %s" % angle_alpha.__class__.__name__
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
            strMessage = "ERROR! XSDataCell.setAngle_beta argument is not XSDataAngle but %s" % angle_beta.__class__.__name__
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
            strMessage = "ERROR! XSDataCell.setAngle_gamma argument is not XSDataAngle but %s" % angle_gamma.__class__.__name__
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
            strMessage = "ERROR! XSDataCell.setLength_a argument is not XSDataLength but %s" % length_a.__class__.__name__
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
            strMessage = "ERROR! XSDataCell.setLength_b argument is not XSDataLength but %s" % length_b.__class__.__name__
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
            strMessage = "ERROR! XSDataCell.setLength_c argument is not XSDataLength but %s" % length_c.__class__.__name__
            raise BaseException(strMessage)
    def delLength_c(self): self._length_c = None
    length_c = property(getLength_c, setLength_c, delLength_c, "Property for length_c")
    def export(self, outfile, level, name_='XSDataCell'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataCell'):
        pass
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
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataCell" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataCell' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataCell is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataCell.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataCell()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataCell" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataCell()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataCell


class XSDataRange(object):
    def __init__(self, end=None, begin=None):
        if begin is None:
            self._begin = None
        else:
            self._begin = int(begin)
        if end is None:
            self._end = None
        else:
            self._end = int(end)
    # Methods and properties for the 'begin' attribute
    def getBegin(self): return self._begin
    def setBegin(self, begin):
        if begin is None:
            self._begin = None
        else:
            self._begin = int(begin)
    def delBegin(self): self._begin = None
    begin = property(getBegin, setBegin, delBegin, "Property for begin")
    # Methods and properties for the 'end' attribute
    def getEnd(self): return self._end
    def setEnd(self, end):
        if end is None:
            self._end = None
        else:
            self._end = int(end)
    def delEnd(self): self._end = None
    end = property(getEnd, setEnd, delEnd, "Property for end")
    def export(self, outfile, level, name_='XSDataRange'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataRange'):
        pass
        if self._begin is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<begin>%d</begin>\n' % self._begin))
        else:
            warnEmptyAttribute("begin", "integer")
        if self._end is not None:
            showIndent(outfile, level)
            outfile.write(unicode('<end>%d</end>\n' % self._end))
        else:
            warnEmptyAttribute("end", "integer")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'begin':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._begin = ival_
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'end':
            if child_.firstChild:
                sval_ = child_.firstChild.nodeValue
                try:
                    ival_ = int(sval_)
                except ValueError:
                    raise ValueError('requires integer -- %s' % child_.toxml())
                self._end = ival_
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataRange" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataRange' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataRange is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataRange.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataRange()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataRange" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataRange()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataRange


class XSDataXdsCompletenessEntry(object):
    def __init__(self, half_dataset_correlation=None, isig=None, rfactor=None, complete=None, possible=None, unique=None, observed=None, res=None):
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataDouble":
            self._res = res
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry constructor argument 'res' is not XSDataDouble but %s" % self._res.__class__.__name__
            raise BaseException(strMessage)
        if observed is None:
            self._observed = None
        elif observed.__class__.__name__ == "XSDataDouble":
            self._observed = observed
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry constructor argument 'observed' is not XSDataDouble but %s" % self._observed.__class__.__name__
            raise BaseException(strMessage)
        if unique is None:
            self._unique = None
        elif unique.__class__.__name__ == "XSDataDouble":
            self._unique = unique
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry constructor argument 'unique' is not XSDataDouble but %s" % self._unique.__class__.__name__
            raise BaseException(strMessage)
        if possible is None:
            self._possible = None
        elif possible.__class__.__name__ == "XSDataDouble":
            self._possible = possible
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry constructor argument 'possible' is not XSDataDouble but %s" % self._possible.__class__.__name__
            raise BaseException(strMessage)
        if complete is None:
            self._complete = None
        elif complete.__class__.__name__ == "XSDataDouble":
            self._complete = complete
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry constructor argument 'complete' is not XSDataDouble but %s" % self._complete.__class__.__name__
            raise BaseException(strMessage)
        if rfactor is None:
            self._rfactor = None
        elif rfactor.__class__.__name__ == "XSDataDouble":
            self._rfactor = rfactor
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry constructor argument 'rfactor' is not XSDataDouble but %s" % self._rfactor.__class__.__name__
            raise BaseException(strMessage)
        if isig is None:
            self._isig = None
        elif isig.__class__.__name__ == "XSDataDouble":
            self._isig = isig
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry constructor argument 'isig' is not XSDataDouble but %s" % self._isig.__class__.__name__
            raise BaseException(strMessage)
        if half_dataset_correlation is None:
            self._half_dataset_correlation = None
        elif half_dataset_correlation.__class__.__name__ == "XSDataDouble":
            self._half_dataset_correlation = half_dataset_correlation
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry constructor argument 'half_dataset_correlation' is not XSDataDouble but %s" % self._half_dataset_correlation.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'res' attribute
    def getRes(self): return self._res
    def setRes(self, res):
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataDouble":
            self._res = res
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry.setRes argument is not XSDataDouble but %s" % res.__class__.__name__
            raise BaseException(strMessage)
    def delRes(self): self._res = None
    res = property(getRes, setRes, delRes, "Property for res")
    # Methods and properties for the 'observed' attribute
    def getObserved(self): return self._observed
    def setObserved(self, observed):
        if observed is None:
            self._observed = None
        elif observed.__class__.__name__ == "XSDataDouble":
            self._observed = observed
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry.setObserved argument is not XSDataDouble but %s" % observed.__class__.__name__
            raise BaseException(strMessage)
    def delObserved(self): self._observed = None
    observed = property(getObserved, setObserved, delObserved, "Property for observed")
    # Methods and properties for the 'unique' attribute
    def getUnique(self): return self._unique
    def setUnique(self, unique):
        if unique is None:
            self._unique = None
        elif unique.__class__.__name__ == "XSDataDouble":
            self._unique = unique
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry.setUnique argument is not XSDataDouble but %s" % unique.__class__.__name__
            raise BaseException(strMessage)
    def delUnique(self): self._unique = None
    unique = property(getUnique, setUnique, delUnique, "Property for unique")
    # Methods and properties for the 'possible' attribute
    def getPossible(self): return self._possible
    def setPossible(self, possible):
        if possible is None:
            self._possible = None
        elif possible.__class__.__name__ == "XSDataDouble":
            self._possible = possible
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry.setPossible argument is not XSDataDouble but %s" % possible.__class__.__name__
            raise BaseException(strMessage)
    def delPossible(self): self._possible = None
    possible = property(getPossible, setPossible, delPossible, "Property for possible")
    # Methods and properties for the 'complete' attribute
    def getComplete(self): return self._complete
    def setComplete(self, complete):
        if complete is None:
            self._complete = None
        elif complete.__class__.__name__ == "XSDataDouble":
            self._complete = complete
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry.setComplete argument is not XSDataDouble but %s" % complete.__class__.__name__
            raise BaseException(strMessage)
    def delComplete(self): self._complete = None
    complete = property(getComplete, setComplete, delComplete, "Property for complete")
    # Methods and properties for the 'rfactor' attribute
    def getRfactor(self): return self._rfactor
    def setRfactor(self, rfactor):
        if rfactor is None:
            self._rfactor = None
        elif rfactor.__class__.__name__ == "XSDataDouble":
            self._rfactor = rfactor
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry.setRfactor argument is not XSDataDouble but %s" % rfactor.__class__.__name__
            raise BaseException(strMessage)
    def delRfactor(self): self._rfactor = None
    rfactor = property(getRfactor, setRfactor, delRfactor, "Property for rfactor")
    # Methods and properties for the 'isig' attribute
    def getIsig(self): return self._isig
    def setIsig(self, isig):
        if isig is None:
            self._isig = None
        elif isig.__class__.__name__ == "XSDataDouble":
            self._isig = isig
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry.setIsig argument is not XSDataDouble but %s" % isig.__class__.__name__
            raise BaseException(strMessage)
    def delIsig(self): self._isig = None
    isig = property(getIsig, setIsig, delIsig, "Property for isig")
    # Methods and properties for the 'half_dataset_correlation' attribute
    def getHalf_dataset_correlation(self): return self._half_dataset_correlation
    def setHalf_dataset_correlation(self, half_dataset_correlation):
        if half_dataset_correlation is None:
            self._half_dataset_correlation = None
        elif half_dataset_correlation.__class__.__name__ == "XSDataDouble":
            self._half_dataset_correlation = half_dataset_correlation
        else:
            strMessage = "ERROR! XSDataXdsCompletenessEntry.setHalf_dataset_correlation argument is not XSDataDouble but %s" % half_dataset_correlation.__class__.__name__
            raise BaseException(strMessage)
    def delHalf_dataset_correlation(self): self._half_dataset_correlation = None
    half_dataset_correlation = property(getHalf_dataset_correlation, setHalf_dataset_correlation, delHalf_dataset_correlation, "Property for half_dataset_correlation")
    def export(self, outfile, level, name_='XSDataXdsCompletenessEntry'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXdsCompletenessEntry'):
        pass
        if self._res is not None:
            self.res.export(outfile, level, name_='res')
        else:
            warnEmptyAttribute("res", "XSDataDouble")
        if self._observed is not None:
            self.observed.export(outfile, level, name_='observed')
        else:
            warnEmptyAttribute("observed", "XSDataDouble")
        if self._unique is not None:
            self.unique.export(outfile, level, name_='unique')
        else:
            warnEmptyAttribute("unique", "XSDataDouble")
        if self._possible is not None:
            self.possible.export(outfile, level, name_='possible')
        else:
            warnEmptyAttribute("possible", "XSDataDouble")
        if self._complete is not None:
            self.complete.export(outfile, level, name_='complete')
        else:
            warnEmptyAttribute("complete", "XSDataDouble")
        if self._rfactor is not None:
            self.rfactor.export(outfile, level, name_='rfactor')
        else:
            warnEmptyAttribute("rfactor", "XSDataDouble")
        if self._isig is not None:
            self.isig.export(outfile, level, name_='isig')
        else:
            warnEmptyAttribute("isig", "XSDataDouble")
        if self._half_dataset_correlation is not None:
            self.half_dataset_correlation.export(outfile, level, name_='half_dataset_correlation')
        else:
            warnEmptyAttribute("half_dataset_correlation", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'res':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRes(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'observed':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setObserved(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unique':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setUnique(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'possible':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setPossible(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'complete':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setComplete(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rfactor':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRfactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'isig':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setIsig(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'half_dataset_correlation':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setHalf_dataset_correlation(obj_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXdsCompletenessEntry" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXdsCompletenessEntry' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXdsCompletenessEntry is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXdsCompletenessEntry.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXdsCompletenessEntry()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXdsCompletenessEntry" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXdsCompletenessEntry()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXdsCompletenessEntry


class XSDataXDSBeam(XSData):
    def __init__(self, x_ray_wavelength=None, polarization_plane_normal=None, incident_beam_direction=None, fraction_of_polarization=None):
        XSData.__init__(self, )
        if fraction_of_polarization is None:
            self._fraction_of_polarization = None
        elif fraction_of_polarization.__class__.__name__ == "XSDataDouble":
            self._fraction_of_polarization = fraction_of_polarization
        else:
            strMessage = "ERROR! XSDataXDSBeam constructor argument 'fraction_of_polarization' is not XSDataDouble but %s" % self._fraction_of_polarization.__class__.__name__
            raise BaseException(strMessage)
        if incident_beam_direction is None:
            self._incident_beam_direction = None
        elif incident_beam_direction.__class__.__name__ == "XSDataVectorDouble":
            self._incident_beam_direction = incident_beam_direction
        else:
            strMessage = "ERROR! XSDataXDSBeam constructor argument 'incident_beam_direction' is not XSDataVectorDouble but %s" % self._incident_beam_direction.__class__.__name__
            raise BaseException(strMessage)
        if polarization_plane_normal is None:
            self._polarization_plane_normal = None
        elif polarization_plane_normal.__class__.__name__ == "XSDataVectorDouble":
            self._polarization_plane_normal = polarization_plane_normal
        else:
            strMessage = "ERROR! XSDataXDSBeam constructor argument 'polarization_plane_normal' is not XSDataVectorDouble but %s" % self._polarization_plane_normal.__class__.__name__
            raise BaseException(strMessage)
        if x_ray_wavelength is None:
            self._x_ray_wavelength = None
        elif x_ray_wavelength.__class__.__name__ == "XSDataWavelength":
            self._x_ray_wavelength = x_ray_wavelength
        else:
            strMessage = "ERROR! XSDataXDSBeam constructor argument 'x_ray_wavelength' is not XSDataWavelength but %s" % self._x_ray_wavelength.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'fraction_of_polarization' attribute
    def getFraction_of_polarization(self): return self._fraction_of_polarization
    def setFraction_of_polarization(self, fraction_of_polarization):
        if fraction_of_polarization is None:
            self._fraction_of_polarization = None
        elif fraction_of_polarization.__class__.__name__ == "XSDataDouble":
            self._fraction_of_polarization = fraction_of_polarization
        else:
            strMessage = "ERROR! XSDataXDSBeam.setFraction_of_polarization argument is not XSDataDouble but %s" % fraction_of_polarization.__class__.__name__
            raise BaseException(strMessage)
    def delFraction_of_polarization(self): self._fraction_of_polarization = None
    fraction_of_polarization = property(getFraction_of_polarization, setFraction_of_polarization, delFraction_of_polarization, "Property for fraction_of_polarization")
    # Methods and properties for the 'incident_beam_direction' attribute
    def getIncident_beam_direction(self): return self._incident_beam_direction
    def setIncident_beam_direction(self, incident_beam_direction):
        if incident_beam_direction is None:
            self._incident_beam_direction = None
        elif incident_beam_direction.__class__.__name__ == "XSDataVectorDouble":
            self._incident_beam_direction = incident_beam_direction
        else:
            strMessage = "ERROR! XSDataXDSBeam.setIncident_beam_direction argument is not XSDataVectorDouble but %s" % incident_beam_direction.__class__.__name__
            raise BaseException(strMessage)
    def delIncident_beam_direction(self): self._incident_beam_direction = None
    incident_beam_direction = property(getIncident_beam_direction, setIncident_beam_direction, delIncident_beam_direction, "Property for incident_beam_direction")
    # Methods and properties for the 'polarization_plane_normal' attribute
    def getPolarization_plane_normal(self): return self._polarization_plane_normal
    def setPolarization_plane_normal(self, polarization_plane_normal):
        if polarization_plane_normal is None:
            self._polarization_plane_normal = None
        elif polarization_plane_normal.__class__.__name__ == "XSDataVectorDouble":
            self._polarization_plane_normal = polarization_plane_normal
        else:
            strMessage = "ERROR! XSDataXDSBeam.setPolarization_plane_normal argument is not XSDataVectorDouble but %s" % polarization_plane_normal.__class__.__name__
            raise BaseException(strMessage)
    def delPolarization_plane_normal(self): self._polarization_plane_normal = None
    polarization_plane_normal = property(getPolarization_plane_normal, setPolarization_plane_normal, delPolarization_plane_normal, "Property for polarization_plane_normal")
    # Methods and properties for the 'x_ray_wavelength' attribute
    def getX_ray_wavelength(self): return self._x_ray_wavelength
    def setX_ray_wavelength(self, x_ray_wavelength):
        if x_ray_wavelength is None:
            self._x_ray_wavelength = None
        elif x_ray_wavelength.__class__.__name__ == "XSDataWavelength":
            self._x_ray_wavelength = x_ray_wavelength
        else:
            strMessage = "ERROR! XSDataXDSBeam.setX_ray_wavelength argument is not XSDataWavelength but %s" % x_ray_wavelength.__class__.__name__
            raise BaseException(strMessage)
    def delX_ray_wavelength(self): self._x_ray_wavelength = None
    x_ray_wavelength = property(getX_ray_wavelength, setX_ray_wavelength, delX_ray_wavelength, "Property for x_ray_wavelength")
    def export(self, outfile, level, name_='XSDataXDSBeam'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXDSBeam'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._fraction_of_polarization is not None:
            self.fraction_of_polarization.export(outfile, level, name_='fraction_of_polarization')
        if self._incident_beam_direction is not None:
            self.incident_beam_direction.export(outfile, level, name_='incident_beam_direction')
        else:
            warnEmptyAttribute("incident_beam_direction", "XSDataVectorDouble")
        if self._polarization_plane_normal is not None:
            self.polarization_plane_normal.export(outfile, level, name_='polarization_plane_normal')
        else:
            warnEmptyAttribute("polarization_plane_normal", "XSDataVectorDouble")
        if self._x_ray_wavelength is not None:
            self.x_ray_wavelength.export(outfile, level, name_='x_ray_wavelength')
        else:
            warnEmptyAttribute("x_ray_wavelength", "XSDataWavelength")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fraction_of_polarization':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setFraction_of_polarization(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'incident_beam_direction':
            obj_ = XSDataVectorDouble()
            obj_.build(child_)
            self.setIncident_beam_direction(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'polarization_plane_normal':
            obj_ = XSDataVectorDouble()
            obj_.build(child_)
            self.setPolarization_plane_normal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'x_ray_wavelength':
            obj_ = XSDataWavelength()
            obj_.build(child_)
            self.setX_ray_wavelength(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXDSBeam" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXDSBeam' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXDSBeam is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXDSBeam.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXDSBeam()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXDSBeam" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXDSBeam()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXDSBeam


class XSDataXDSCell(XSData):
    def __init__(self, angle_gamma=None, length_c=None, length_b=None, length_a=None, angle_beta=None, angle_alpha=None):
        XSData.__init__(self, )
        if angle_alpha is None:
            self._angle_alpha = None
        elif angle_alpha.__class__.__name__ == "XSDataAngle":
            self._angle_alpha = angle_alpha
        else:
            strMessage = "ERROR! XSDataXDSCell constructor argument 'angle_alpha' is not XSDataAngle but %s" % self._angle_alpha.__class__.__name__
            raise BaseException(strMessage)
        if angle_beta is None:
            self._angle_beta = None
        elif angle_beta.__class__.__name__ == "XSDataAngle":
            self._angle_beta = angle_beta
        else:
            strMessage = "ERROR! XSDataXDSCell constructor argument 'angle_beta' is not XSDataAngle but %s" % self._angle_beta.__class__.__name__
            raise BaseException(strMessage)
        if length_a is None:
            self._length_a = None
        elif length_a.__class__.__name__ == "XSDataLength":
            self._length_a = length_a
        else:
            strMessage = "ERROR! XSDataXDSCell constructor argument 'length_a' is not XSDataLength but %s" % self._length_a.__class__.__name__
            raise BaseException(strMessage)
        if length_b is None:
            self._length_b = None
        elif length_b.__class__.__name__ == "XSDataLength":
            self._length_b = length_b
        else:
            strMessage = "ERROR! XSDataXDSCell constructor argument 'length_b' is not XSDataLength but %s" % self._length_b.__class__.__name__
            raise BaseException(strMessage)
        if length_c is None:
            self._length_c = None
        elif length_c.__class__.__name__ == "XSDataLength":
            self._length_c = length_c
        else:
            strMessage = "ERROR! XSDataXDSCell constructor argument 'length_c' is not XSDataLength but %s" % self._length_c.__class__.__name__
            raise BaseException(strMessage)
        if angle_gamma is None:
            self._angle_gamma = None
        elif angle_gamma.__class__.__name__ == "XSDataAngle":
            self._angle_gamma = angle_gamma
        else:
            strMessage = "ERROR! XSDataXDSCell constructor argument 'angle_gamma' is not XSDataAngle but %s" % self._angle_gamma.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'angle_alpha' attribute
    def getAngle_alpha(self): return self._angle_alpha
    def setAngle_alpha(self, angle_alpha):
        if angle_alpha is None:
            self._angle_alpha = None
        elif angle_alpha.__class__.__name__ == "XSDataAngle":
            self._angle_alpha = angle_alpha
        else:
            strMessage = "ERROR! XSDataXDSCell.setAngle_alpha argument is not XSDataAngle but %s" % angle_alpha.__class__.__name__
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
            strMessage = "ERROR! XSDataXDSCell.setAngle_beta argument is not XSDataAngle but %s" % angle_beta.__class__.__name__
            raise BaseException(strMessage)
    def delAngle_beta(self): self._angle_beta = None
    angle_beta = property(getAngle_beta, setAngle_beta, delAngle_beta, "Property for angle_beta")
    # Methods and properties for the 'length_a' attribute
    def getLength_a(self): return self._length_a
    def setLength_a(self, length_a):
        if length_a is None:
            self._length_a = None
        elif length_a.__class__.__name__ == "XSDataLength":
            self._length_a = length_a
        else:
            strMessage = "ERROR! XSDataXDSCell.setLength_a argument is not XSDataLength but %s" % length_a.__class__.__name__
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
            strMessage = "ERROR! XSDataXDSCell.setLength_b argument is not XSDataLength but %s" % length_b.__class__.__name__
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
            strMessage = "ERROR! XSDataXDSCell.setLength_c argument is not XSDataLength but %s" % length_c.__class__.__name__
            raise BaseException(strMessage)
    def delLength_c(self): self._length_c = None
    length_c = property(getLength_c, setLength_c, delLength_c, "Property for length_c")
    # Methods and properties for the 'angle_gamma' attribute
    def getAngle_gamma(self): return self._angle_gamma
    def setAngle_gamma(self, angle_gamma):
        if angle_gamma is None:
            self._angle_gamma = None
        elif angle_gamma.__class__.__name__ == "XSDataAngle":
            self._angle_gamma = angle_gamma
        else:
            strMessage = "ERROR! XSDataXDSCell.setAngle_gamma argument is not XSDataAngle but %s" % angle_gamma.__class__.__name__
            raise BaseException(strMessage)
    def delAngle_gamma(self): self._angle_gamma = None
    angle_gamma = property(getAngle_gamma, setAngle_gamma, delAngle_gamma, "Property for angle_gamma")
    def export(self, outfile, level, name_='XSDataXDSCell'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXDSCell'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._angle_alpha is not None:
            self.angle_alpha.export(outfile, level, name_='angle_alpha')
        else:
            warnEmptyAttribute("angle_alpha", "XSDataAngle")
        if self._angle_beta is not None:
            self.angle_beta.export(outfile, level, name_='angle_beta')
        else:
            warnEmptyAttribute("angle_beta", "XSDataAngle")
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
        if self._angle_gamma is not None:
            self.angle_gamma.export(outfile, level, name_='angle_gamma')
        else:
            warnEmptyAttribute("angle_gamma", "XSDataAngle")
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
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'angle_gamma':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setAngle_gamma(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXDSCell" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXDSCell' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXDSCell is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXDSCell.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXDSCell()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXDSCell" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXDSCell()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXDSCell


class XSDataXDSCrystal(XSData):
    def __init__(self, minimum_number_of_pixels_in_a_spot=None, unit_cell_constants=None, strong_pixel=None, space_group_number=None, friedels_law=None):
        XSData.__init__(self, )
        if friedels_law is None:
            self._friedels_law = None
        elif friedels_law.__class__.__name__ == "XSDataString":
            self._friedels_law = friedels_law
        else:
            strMessage = "ERROR! XSDataXDSCrystal constructor argument 'friedels_law' is not XSDataString but %s" % self._friedels_law.__class__.__name__
            raise BaseException(strMessage)
        if space_group_number is None:
            self._space_group_number = None
        elif space_group_number.__class__.__name__ == "XSDataInteger":
            self._space_group_number = space_group_number
        else:
            strMessage = "ERROR! XSDataXDSCrystal constructor argument 'space_group_number' is not XSDataInteger but %s" % self._space_group_number.__class__.__name__
            raise BaseException(strMessage)
        if strong_pixel is None:
            self._strong_pixel = None
        elif strong_pixel.__class__.__name__ == "XSDataInteger":
            self._strong_pixel = strong_pixel
        else:
            strMessage = "ERROR! XSDataXDSCrystal constructor argument 'strong_pixel' is not XSDataInteger but %s" % self._strong_pixel.__class__.__name__
            raise BaseException(strMessage)
        if unit_cell_constants is None:
            self._unit_cell_constants = None
        elif unit_cell_constants.__class__.__name__ == "XSDataXDSCell":
            self._unit_cell_constants = unit_cell_constants
        else:
            strMessage = "ERROR! XSDataXDSCrystal constructor argument 'unit_cell_constants' is not XSDataXDSCell but %s" % self._unit_cell_constants.__class__.__name__
            raise BaseException(strMessage)
        if minimum_number_of_pixels_in_a_spot is None:
            self._minimum_number_of_pixels_in_a_spot = None
        elif minimum_number_of_pixels_in_a_spot.__class__.__name__ == "XSDataInteger":
            self._minimum_number_of_pixels_in_a_spot = minimum_number_of_pixels_in_a_spot
        else:
            strMessage = "ERROR! XSDataXDSCrystal constructor argument 'minimum_number_of_pixels_in_a_spot' is not XSDataInteger but %s" % self._minimum_number_of_pixels_in_a_spot.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'friedels_law' attribute
    def getFriedels_law(self): return self._friedels_law
    def setFriedels_law(self, friedels_law):
        if friedels_law is None:
            self._friedels_law = None
        elif friedels_law.__class__.__name__ == "XSDataString":
            self._friedels_law = friedels_law
        else:
            strMessage = "ERROR! XSDataXDSCrystal.setFriedels_law argument is not XSDataString but %s" % friedels_law.__class__.__name__
            raise BaseException(strMessage)
    def delFriedels_law(self): self._friedels_law = None
    friedels_law = property(getFriedels_law, setFriedels_law, delFriedels_law, "Property for friedels_law")
    # Methods and properties for the 'space_group_number' attribute
    def getSpace_group_number(self): return self._space_group_number
    def setSpace_group_number(self, space_group_number):
        if space_group_number is None:
            self._space_group_number = None
        elif space_group_number.__class__.__name__ == "XSDataInteger":
            self._space_group_number = space_group_number
        else:
            strMessage = "ERROR! XSDataXDSCrystal.setSpace_group_number argument is not XSDataInteger but %s" % space_group_number.__class__.__name__
            raise BaseException(strMessage)
    def delSpace_group_number(self): self._space_group_number = None
    space_group_number = property(getSpace_group_number, setSpace_group_number, delSpace_group_number, "Property for space_group_number")
    # Methods and properties for the 'strong_pixel' attribute
    def getStrong_pixel(self): return self._strong_pixel
    def setStrong_pixel(self, strong_pixel):
        if strong_pixel is None:
            self._strong_pixel = None
        elif strong_pixel.__class__.__name__ == "XSDataInteger":
            self._strong_pixel = strong_pixel
        else:
            strMessage = "ERROR! XSDataXDSCrystal.setStrong_pixel argument is not XSDataInteger but %s" % strong_pixel.__class__.__name__
            raise BaseException(strMessage)
    def delStrong_pixel(self): self._strong_pixel = None
    strong_pixel = property(getStrong_pixel, setStrong_pixel, delStrong_pixel, "Property for strong_pixel")
    # Methods and properties for the 'unit_cell_constants' attribute
    def getUnit_cell_constants(self): return self._unit_cell_constants
    def setUnit_cell_constants(self, unit_cell_constants):
        if unit_cell_constants is None:
            self._unit_cell_constants = None
        elif unit_cell_constants.__class__.__name__ == "XSDataXDSCell":
            self._unit_cell_constants = unit_cell_constants
        else:
            strMessage = "ERROR! XSDataXDSCrystal.setUnit_cell_constants argument is not XSDataXDSCell but %s" % unit_cell_constants.__class__.__name__
            raise BaseException(strMessage)
    def delUnit_cell_constants(self): self._unit_cell_constants = None
    unit_cell_constants = property(getUnit_cell_constants, setUnit_cell_constants, delUnit_cell_constants, "Property for unit_cell_constants")
    # Methods and properties for the 'minimum_number_of_pixels_in_a_spot' attribute
    def getMinimum_number_of_pixels_in_a_spot(self): return self._minimum_number_of_pixels_in_a_spot
    def setMinimum_number_of_pixels_in_a_spot(self, minimum_number_of_pixels_in_a_spot):
        if minimum_number_of_pixels_in_a_spot is None:
            self._minimum_number_of_pixels_in_a_spot = None
        elif minimum_number_of_pixels_in_a_spot.__class__.__name__ == "XSDataInteger":
            self._minimum_number_of_pixels_in_a_spot = minimum_number_of_pixels_in_a_spot
        else:
            strMessage = "ERROR! XSDataXDSCrystal.setMinimum_number_of_pixels_in_a_spot argument is not XSDataInteger but %s" % minimum_number_of_pixels_in_a_spot.__class__.__name__
            raise BaseException(strMessage)
    def delMinimum_number_of_pixels_in_a_spot(self): self._minimum_number_of_pixels_in_a_spot = None
    minimum_number_of_pixels_in_a_spot = property(getMinimum_number_of_pixels_in_a_spot, setMinimum_number_of_pixels_in_a_spot, delMinimum_number_of_pixels_in_a_spot, "Property for minimum_number_of_pixels_in_a_spot")
    def export(self, outfile, level, name_='XSDataXDSCrystal'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXDSCrystal'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._friedels_law is not None:
            self.friedels_law.export(outfile, level, name_='friedels_law')
        else:
            warnEmptyAttribute("friedels_law", "XSDataString")
        if self._space_group_number is not None:
            self.space_group_number.export(outfile, level, name_='space_group_number')
        else:
            warnEmptyAttribute("space_group_number", "XSDataInteger")
        if self._strong_pixel is not None:
            self.strong_pixel.export(outfile, level, name_='strong_pixel')
        else:
            warnEmptyAttribute("strong_pixel", "XSDataInteger")
        if self._unit_cell_constants is not None:
            self.unit_cell_constants.export(outfile, level, name_='unit_cell_constants')
        else:
            warnEmptyAttribute("unit_cell_constants", "XSDataXDSCell")
        if self._minimum_number_of_pixels_in_a_spot is not None:
            self.minimum_number_of_pixels_in_a_spot.export(outfile, level, name_='minimum_number_of_pixels_in_a_spot')
        else:
            warnEmptyAttribute("minimum_number_of_pixels_in_a_spot", "XSDataInteger")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'friedels_law':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setFriedels_law(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'space_group_number':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSpace_group_number(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'strong_pixel':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setStrong_pixel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit_cell_constants':
            obj_ = XSDataXDSCell()
            obj_.build(child_)
            self.setUnit_cell_constants(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minimum_number_of_pixels_in_a_spot':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setMinimum_number_of_pixels_in_a_spot(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXDSCrystal" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXDSCrystal' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXDSCrystal is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXDSCrystal.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXDSCrystal()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXDSCrystal" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXDSCrystal()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXDSCrystal


class XSDataXDSDoubleRange(XSData):
    def __init__(self, upper=None, lower=None):
        XSData.__init__(self, )
        if lower is None:
            self._lower = None
        elif lower.__class__.__name__ == "XSDataDouble":
            self._lower = lower
        else:
            strMessage = "ERROR! XSDataXDSDoubleRange constructor argument 'lower' is not XSDataDouble but %s" % self._lower.__class__.__name__
            raise BaseException(strMessage)
        if upper is None:
            self._upper = None
        elif upper.__class__.__name__ == "XSDataDouble":
            self._upper = upper
        else:
            strMessage = "ERROR! XSDataXDSDoubleRange constructor argument 'upper' is not XSDataDouble but %s" % self._upper.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'lower' attribute
    def getLower(self): return self._lower
    def setLower(self, lower):
        if lower is None:
            self._lower = None
        elif lower.__class__.__name__ == "XSDataDouble":
            self._lower = lower
        else:
            strMessage = "ERROR! XSDataXDSDoubleRange.setLower argument is not XSDataDouble but %s" % lower.__class__.__name__
            raise BaseException(strMessage)
    def delLower(self): self._lower = None
    lower = property(getLower, setLower, delLower, "Property for lower")
    # Methods and properties for the 'upper' attribute
    def getUpper(self): return self._upper
    def setUpper(self, upper):
        if upper is None:
            self._upper = None
        elif upper.__class__.__name__ == "XSDataDouble":
            self._upper = upper
        else:
            strMessage = "ERROR! XSDataXDSDoubleRange.setUpper argument is not XSDataDouble but %s" % upper.__class__.__name__
            raise BaseException(strMessage)
    def delUpper(self): self._upper = None
    upper = property(getUpper, setUpper, delUpper, "Property for upper")
    def export(self, outfile, level, name_='XSDataXDSDoubleRange'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXDSDoubleRange'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._lower is not None:
            self.lower.export(outfile, level, name_='lower')
        else:
            warnEmptyAttribute("lower", "XSDataDouble")
        if self._upper is not None:
            self.upper.export(outfile, level, name_='upper')
        else:
            warnEmptyAttribute("upper", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lower':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setLower(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'upper':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setUpper(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXDSDoubleRange" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXDSDoubleRange' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXDSDoubleRange is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXDSDoubleRange.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXDSDoubleRange()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXDSDoubleRange" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXDSDoubleRange()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXDSDoubleRange


class XSDataXDSGoniostat(XSData):
    def __init__(self, starting_angle=None, rotation_axis=None, oscillation_range=None):
        XSData.__init__(self, )
        if oscillation_range is None:
            self._oscillation_range = None
        elif oscillation_range.__class__.__name__ == "XSDataAngle":
            self._oscillation_range = oscillation_range
        else:
            strMessage = "ERROR! XSDataXDSGoniostat constructor argument 'oscillation_range' is not XSDataAngle but %s" % self._oscillation_range.__class__.__name__
            raise BaseException(strMessage)
        if rotation_axis is None:
            self._rotation_axis = None
        elif rotation_axis.__class__.__name__ == "XSDataVectorDouble":
            self._rotation_axis = rotation_axis
        else:
            strMessage = "ERROR! XSDataXDSGoniostat constructor argument 'rotation_axis' is not XSDataVectorDouble but %s" % self._rotation_axis.__class__.__name__
            raise BaseException(strMessage)
        if starting_angle is None:
            self._starting_angle = None
        elif starting_angle.__class__.__name__ == "XSDataAngle":
            self._starting_angle = starting_angle
        else:
            strMessage = "ERROR! XSDataXDSGoniostat constructor argument 'starting_angle' is not XSDataAngle but %s" % self._starting_angle.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'oscillation_range' attribute
    def getOscillation_range(self): return self._oscillation_range
    def setOscillation_range(self, oscillation_range):
        if oscillation_range is None:
            self._oscillation_range = None
        elif oscillation_range.__class__.__name__ == "XSDataAngle":
            self._oscillation_range = oscillation_range
        else:
            strMessage = "ERROR! XSDataXDSGoniostat.setOscillation_range argument is not XSDataAngle but %s" % oscillation_range.__class__.__name__
            raise BaseException(strMessage)
    def delOscillation_range(self): self._oscillation_range = None
    oscillation_range = property(getOscillation_range, setOscillation_range, delOscillation_range, "Property for oscillation_range")
    # Methods and properties for the 'rotation_axis' attribute
    def getRotation_axis(self): return self._rotation_axis
    def setRotation_axis(self, rotation_axis):
        if rotation_axis is None:
            self._rotation_axis = None
        elif rotation_axis.__class__.__name__ == "XSDataVectorDouble":
            self._rotation_axis = rotation_axis
        else:
            strMessage = "ERROR! XSDataXDSGoniostat.setRotation_axis argument is not XSDataVectorDouble but %s" % rotation_axis.__class__.__name__
            raise BaseException(strMessage)
    def delRotation_axis(self): self._rotation_axis = None
    rotation_axis = property(getRotation_axis, setRotation_axis, delRotation_axis, "Property for rotation_axis")
    # Methods and properties for the 'starting_angle' attribute
    def getStarting_angle(self): return self._starting_angle
    def setStarting_angle(self, starting_angle):
        if starting_angle is None:
            self._starting_angle = None
        elif starting_angle.__class__.__name__ == "XSDataAngle":
            self._starting_angle = starting_angle
        else:
            strMessage = "ERROR! XSDataXDSGoniostat.setStarting_angle argument is not XSDataAngle but %s" % starting_angle.__class__.__name__
            raise BaseException(strMessage)
    def delStarting_angle(self): self._starting_angle = None
    starting_angle = property(getStarting_angle, setStarting_angle, delStarting_angle, "Property for starting_angle")
    def export(self, outfile, level, name_='XSDataXDSGoniostat'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXDSGoniostat'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._oscillation_range is not None:
            self.oscillation_range.export(outfile, level, name_='oscillation_range')
        else:
            warnEmptyAttribute("oscillation_range", "XSDataAngle")
        if self._rotation_axis is not None:
            self.rotation_axis.export(outfile, level, name_='rotation_axis')
        else:
            warnEmptyAttribute("rotation_axis", "XSDataVectorDouble")
        if self._starting_angle is not None:
            self.starting_angle.export(outfile, level, name_='starting_angle')
        else:
            warnEmptyAttribute("starting_angle", "XSDataAngle")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'oscillation_range':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setOscillation_range(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rotation_axis':
            obj_ = XSDataVectorDouble()
            obj_.build(child_)
            self.setRotation_axis(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'starting_angle':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setStarting_angle(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXDSGoniostat" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXDSGoniostat' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXDSGoniostat is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXDSGoniostat.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXDSGoniostat()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXDSGoniostat" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXDSGoniostat()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXDSGoniostat


class XSDataXDSIntegerRange(XSData):
    def __init__(self, upper=None, lower=None):
        XSData.__init__(self, )
        if lower is None:
            self._lower = None
        elif lower.__class__.__name__ == "XSDataInteger":
            self._lower = lower
        else:
            strMessage = "ERROR! XSDataXDSIntegerRange constructor argument 'lower' is not XSDataInteger but %s" % self._lower.__class__.__name__
            raise BaseException(strMessage)
        if upper is None:
            self._upper = None
        elif upper.__class__.__name__ == "XSDataInteger":
            self._upper = upper
        else:
            strMessage = "ERROR! XSDataXDSIntegerRange constructor argument 'upper' is not XSDataInteger but %s" % self._upper.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'lower' attribute
    def getLower(self): return self._lower
    def setLower(self, lower):
        if lower is None:
            self._lower = None
        elif lower.__class__.__name__ == "XSDataInteger":
            self._lower = lower
        else:
            strMessage = "ERROR! XSDataXDSIntegerRange.setLower argument is not XSDataInteger but %s" % lower.__class__.__name__
            raise BaseException(strMessage)
    def delLower(self): self._lower = None
    lower = property(getLower, setLower, delLower, "Property for lower")
    # Methods and properties for the 'upper' attribute
    def getUpper(self): return self._upper
    def setUpper(self, upper):
        if upper is None:
            self._upper = None
        elif upper.__class__.__name__ == "XSDataInteger":
            self._upper = upper
        else:
            strMessage = "ERROR! XSDataXDSIntegerRange.setUpper argument is not XSDataInteger but %s" % upper.__class__.__name__
            raise BaseException(strMessage)
    def delUpper(self): self._upper = None
    upper = property(getUpper, setUpper, delUpper, "Property for upper")
    def export(self, outfile, level, name_='XSDataXDSIntegerRange'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXDSIntegerRange'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._lower is not None:
            self.lower.export(outfile, level, name_='lower')
        else:
            warnEmptyAttribute("lower", "XSDataInteger")
        if self._upper is not None:
            self.upper.export(outfile, level, name_='upper')
        else:
            warnEmptyAttribute("upper", "XSDataInteger")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lower':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setLower(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'upper':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setUpper(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXDSIntegerRange" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXDSIntegerRange' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXDSIntegerRange is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXDSIntegerRange.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXDSIntegerRange()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXDSIntegerRange" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXDSIntegerRange()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXDSIntegerRange


class XSDataXDSDetector(XSData):
    def __init__(self, trusted_region=None, sensor_thickness=None, untrusted_rectangle=None, value_range_for_trusted_detector_pixels=None, qy=None, qx=None, overload=None, orgy=None, orgx=None, ny=None, nx=None, minimum_valid_pixel_value=None, direction_of_detector_y_axis=None, direction_of_detector_x_axis=None, detector_name=None, detector_distance=None):
        XSData.__init__(self, )
        if detector_distance is None:
            self._detector_distance = None
        elif detector_distance.__class__.__name__ == "XSDataLength":
            self._detector_distance = detector_distance
        else:
            strMessage = "ERROR! XSDataXDSDetector constructor argument 'detector_distance' is not XSDataLength but %s" % self._detector_distance.__class__.__name__
            raise BaseException(strMessage)
        if detector_name is None:
            self._detector_name = None
        elif detector_name.__class__.__name__ == "XSDataString":
            self._detector_name = detector_name
        else:
            strMessage = "ERROR! XSDataXDSDetector constructor argument 'detector_name' is not XSDataString but %s" % self._detector_name.__class__.__name__
            raise BaseException(strMessage)
        if direction_of_detector_x_axis is None:
            self._direction_of_detector_x_axis = None
        elif direction_of_detector_x_axis.__class__.__name__ == "XSDataVectorDouble":
            self._direction_of_detector_x_axis = direction_of_detector_x_axis
        else:
            strMessage = "ERROR! XSDataXDSDetector constructor argument 'direction_of_detector_x_axis' is not XSDataVectorDouble but %s" % self._direction_of_detector_x_axis.__class__.__name__
            raise BaseException(strMessage)
        if direction_of_detector_y_axis is None:
            self._direction_of_detector_y_axis = None
        elif direction_of_detector_y_axis.__class__.__name__ == "XSDataVectorDouble":
            self._direction_of_detector_y_axis = direction_of_detector_y_axis
        else:
            strMessage = "ERROR! XSDataXDSDetector constructor argument 'direction_of_detector_y_axis' is not XSDataVectorDouble but %s" % self._direction_of_detector_y_axis.__class__.__name__
            raise BaseException(strMessage)
        if minimum_valid_pixel_value is None:
            self._minimum_valid_pixel_value = None
        elif minimum_valid_pixel_value.__class__.__name__ == "XSDataInteger":
            self._minimum_valid_pixel_value = minimum_valid_pixel_value
        else:
            strMessage = "ERROR! XSDataXDSDetector constructor argument 'minimum_valid_pixel_value' is not XSDataInteger but %s" % self._minimum_valid_pixel_value.__class__.__name__
            raise BaseException(strMessage)
        if nx is None:
            self._nx = None
        elif nx.__class__.__name__ == "XSDataInteger":
            self._nx = nx
        else:
            strMessage = "ERROR! XSDataXDSDetector constructor argument 'nx' is not XSDataInteger but %s" % self._nx.__class__.__name__
            raise BaseException(strMessage)
        if ny is None:
            self._ny = None
        elif ny.__class__.__name__ == "XSDataInteger":
            self._ny = ny
        else:
            strMessage = "ERROR! XSDataXDSDetector constructor argument 'ny' is not XSDataInteger but %s" % self._ny.__class__.__name__
            raise BaseException(strMessage)
        if orgx is None:
            self._orgx = None
        elif orgx.__class__.__name__ == "XSDataDouble":
            self._orgx = orgx
        else:
            strMessage = "ERROR! XSDataXDSDetector constructor argument 'orgx' is not XSDataDouble but %s" % self._orgx.__class__.__name__
            raise BaseException(strMessage)
        if orgy is None:
            self._orgy = None
        elif orgy.__class__.__name__ == "XSDataDouble":
            self._orgy = orgy
        else:
            strMessage = "ERROR! XSDataXDSDetector constructor argument 'orgy' is not XSDataDouble but %s" % self._orgy.__class__.__name__
            raise BaseException(strMessage)
        if overload is None:
            self._overload = None
        elif overload.__class__.__name__ == "XSDataInteger":
            self._overload = overload
        else:
            strMessage = "ERROR! XSDataXDSDetector constructor argument 'overload' is not XSDataInteger but %s" % self._overload.__class__.__name__
            raise BaseException(strMessage)
        if qx is None:
            self._qx = None
        elif qx.__class__.__name__ == "XSDataLength":
            self._qx = qx
        else:
            strMessage = "ERROR! XSDataXDSDetector constructor argument 'qx' is not XSDataLength but %s" % self._qx.__class__.__name__
            raise BaseException(strMessage)
        if qy is None:
            self._qy = None
        elif qy.__class__.__name__ == "XSDataLength":
            self._qy = qy
        else:
            strMessage = "ERROR! XSDataXDSDetector constructor argument 'qy' is not XSDataLength but %s" % self._qy.__class__.__name__
            raise BaseException(strMessage)
        if value_range_for_trusted_detector_pixels is None:
            self._value_range_for_trusted_detector_pixels = None
        elif value_range_for_trusted_detector_pixels.__class__.__name__ == "XSDataXDSIntegerRange":
            self._value_range_for_trusted_detector_pixels = value_range_for_trusted_detector_pixels
        else:
            strMessage = "ERROR! XSDataXDSDetector constructor argument 'value_range_for_trusted_detector_pixels' is not XSDataXDSIntegerRange but %s" % self._value_range_for_trusted_detector_pixels.__class__.__name__
            raise BaseException(strMessage)
        if untrusted_rectangle is None:
            self._untrusted_rectangle = []
        elif untrusted_rectangle.__class__.__name__ == "list":
            self._untrusted_rectangle = untrusted_rectangle
        else:
            strMessage = "ERROR! XSDataXDSDetector constructor argument 'untrusted_rectangle' is not list but %s" % self._untrusted_rectangle.__class__.__name__
            raise BaseException(strMessage)
        if sensor_thickness is None:
            self._sensor_thickness = None
        elif sensor_thickness.__class__.__name__ == "XSDataDouble":
            self._sensor_thickness = sensor_thickness
        else:
            strMessage = "ERROR! XSDataXDSDetector constructor argument 'sensor_thickness' is not XSDataDouble but %s" % self._sensor_thickness.__class__.__name__
            raise BaseException(strMessage)
        if trusted_region is None:
            self._trusted_region = None
        elif trusted_region.__class__.__name__ == "XSDataXDSDoubleRange":
            self._trusted_region = trusted_region
        else:
            strMessage = "ERROR! XSDataXDSDetector constructor argument 'trusted_region' is not XSDataXDSDoubleRange but %s" % self._trusted_region.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'detector_distance' attribute
    def getDetector_distance(self): return self._detector_distance
    def setDetector_distance(self, detector_distance):
        if detector_distance is None:
            self._detector_distance = None
        elif detector_distance.__class__.__name__ == "XSDataLength":
            self._detector_distance = detector_distance
        else:
            strMessage = "ERROR! XSDataXDSDetector.setDetector_distance argument is not XSDataLength but %s" % detector_distance.__class__.__name__
            raise BaseException(strMessage)
    def delDetector_distance(self): self._detector_distance = None
    detector_distance = property(getDetector_distance, setDetector_distance, delDetector_distance, "Property for detector_distance")
    # Methods and properties for the 'detector_name' attribute
    def getDetector_name(self): return self._detector_name
    def setDetector_name(self, detector_name):
        if detector_name is None:
            self._detector_name = None
        elif detector_name.__class__.__name__ == "XSDataString":
            self._detector_name = detector_name
        else:
            strMessage = "ERROR! XSDataXDSDetector.setDetector_name argument is not XSDataString but %s" % detector_name.__class__.__name__
            raise BaseException(strMessage)
    def delDetector_name(self): self._detector_name = None
    detector_name = property(getDetector_name, setDetector_name, delDetector_name, "Property for detector_name")
    # Methods and properties for the 'direction_of_detector_x_axis' attribute
    def getDirection_of_detector_x_axis(self): return self._direction_of_detector_x_axis
    def setDirection_of_detector_x_axis(self, direction_of_detector_x_axis):
        if direction_of_detector_x_axis is None:
            self._direction_of_detector_x_axis = None
        elif direction_of_detector_x_axis.__class__.__name__ == "XSDataVectorDouble":
            self._direction_of_detector_x_axis = direction_of_detector_x_axis
        else:
            strMessage = "ERROR! XSDataXDSDetector.setDirection_of_detector_x_axis argument is not XSDataVectorDouble but %s" % direction_of_detector_x_axis.__class__.__name__
            raise BaseException(strMessage)
    def delDirection_of_detector_x_axis(self): self._direction_of_detector_x_axis = None
    direction_of_detector_x_axis = property(getDirection_of_detector_x_axis, setDirection_of_detector_x_axis, delDirection_of_detector_x_axis, "Property for direction_of_detector_x_axis")
    # Methods and properties for the 'direction_of_detector_y_axis' attribute
    def getDirection_of_detector_y_axis(self): return self._direction_of_detector_y_axis
    def setDirection_of_detector_y_axis(self, direction_of_detector_y_axis):
        if direction_of_detector_y_axis is None:
            self._direction_of_detector_y_axis = None
        elif direction_of_detector_y_axis.__class__.__name__ == "XSDataVectorDouble":
            self._direction_of_detector_y_axis = direction_of_detector_y_axis
        else:
            strMessage = "ERROR! XSDataXDSDetector.setDirection_of_detector_y_axis argument is not XSDataVectorDouble but %s" % direction_of_detector_y_axis.__class__.__name__
            raise BaseException(strMessage)
    def delDirection_of_detector_y_axis(self): self._direction_of_detector_y_axis = None
    direction_of_detector_y_axis = property(getDirection_of_detector_y_axis, setDirection_of_detector_y_axis, delDirection_of_detector_y_axis, "Property for direction_of_detector_y_axis")
    # Methods and properties for the 'minimum_valid_pixel_value' attribute
    def getMinimum_valid_pixel_value(self): return self._minimum_valid_pixel_value
    def setMinimum_valid_pixel_value(self, minimum_valid_pixel_value):
        if minimum_valid_pixel_value is None:
            self._minimum_valid_pixel_value = None
        elif minimum_valid_pixel_value.__class__.__name__ == "XSDataInteger":
            self._minimum_valid_pixel_value = minimum_valid_pixel_value
        else:
            strMessage = "ERROR! XSDataXDSDetector.setMinimum_valid_pixel_value argument is not XSDataInteger but %s" % minimum_valid_pixel_value.__class__.__name__
            raise BaseException(strMessage)
    def delMinimum_valid_pixel_value(self): self._minimum_valid_pixel_value = None
    minimum_valid_pixel_value = property(getMinimum_valid_pixel_value, setMinimum_valid_pixel_value, delMinimum_valid_pixel_value, "Property for minimum_valid_pixel_value")
    # Methods and properties for the 'nx' attribute
    def getNx(self): return self._nx
    def setNx(self, nx):
        if nx is None:
            self._nx = None
        elif nx.__class__.__name__ == "XSDataInteger":
            self._nx = nx
        else:
            strMessage = "ERROR! XSDataXDSDetector.setNx argument is not XSDataInteger but %s" % nx.__class__.__name__
            raise BaseException(strMessage)
    def delNx(self): self._nx = None
    nx = property(getNx, setNx, delNx, "Property for nx")
    # Methods and properties for the 'ny' attribute
    def getNy(self): return self._ny
    def setNy(self, ny):
        if ny is None:
            self._ny = None
        elif ny.__class__.__name__ == "XSDataInteger":
            self._ny = ny
        else:
            strMessage = "ERROR! XSDataXDSDetector.setNy argument is not XSDataInteger but %s" % ny.__class__.__name__
            raise BaseException(strMessage)
    def delNy(self): self._ny = None
    ny = property(getNy, setNy, delNy, "Property for ny")
    # Methods and properties for the 'orgx' attribute
    def getOrgx(self): return self._orgx
    def setOrgx(self, orgx):
        if orgx is None:
            self._orgx = None
        elif orgx.__class__.__name__ == "XSDataDouble":
            self._orgx = orgx
        else:
            strMessage = "ERROR! XSDataXDSDetector.setOrgx argument is not XSDataDouble but %s" % orgx.__class__.__name__
            raise BaseException(strMessage)
    def delOrgx(self): self._orgx = None
    orgx = property(getOrgx, setOrgx, delOrgx, "Property for orgx")
    # Methods and properties for the 'orgy' attribute
    def getOrgy(self): return self._orgy
    def setOrgy(self, orgy):
        if orgy is None:
            self._orgy = None
        elif orgy.__class__.__name__ == "XSDataDouble":
            self._orgy = orgy
        else:
            strMessage = "ERROR! XSDataXDSDetector.setOrgy argument is not XSDataDouble but %s" % orgy.__class__.__name__
            raise BaseException(strMessage)
    def delOrgy(self): self._orgy = None
    orgy = property(getOrgy, setOrgy, delOrgy, "Property for orgy")
    # Methods and properties for the 'overload' attribute
    def getOverload(self): return self._overload
    def setOverload(self, overload):
        if overload is None:
            self._overload = None
        elif overload.__class__.__name__ == "XSDataInteger":
            self._overload = overload
        else:
            strMessage = "ERROR! XSDataXDSDetector.setOverload argument is not XSDataInteger but %s" % overload.__class__.__name__
            raise BaseException(strMessage)
    def delOverload(self): self._overload = None
    overload = property(getOverload, setOverload, delOverload, "Property for overload")
    # Methods and properties for the 'qx' attribute
    def getQx(self): return self._qx
    def setQx(self, qx):
        if qx is None:
            self._qx = None
        elif qx.__class__.__name__ == "XSDataLength":
            self._qx = qx
        else:
            strMessage = "ERROR! XSDataXDSDetector.setQx argument is not XSDataLength but %s" % qx.__class__.__name__
            raise BaseException(strMessage)
    def delQx(self): self._qx = None
    qx = property(getQx, setQx, delQx, "Property for qx")
    # Methods and properties for the 'qy' attribute
    def getQy(self): return self._qy
    def setQy(self, qy):
        if qy is None:
            self._qy = None
        elif qy.__class__.__name__ == "XSDataLength":
            self._qy = qy
        else:
            strMessage = "ERROR! XSDataXDSDetector.setQy argument is not XSDataLength but %s" % qy.__class__.__name__
            raise BaseException(strMessage)
    def delQy(self): self._qy = None
    qy = property(getQy, setQy, delQy, "Property for qy")
    # Methods and properties for the 'value_range_for_trusted_detector_pixels' attribute
    def getValue_range_for_trusted_detector_pixels(self): return self._value_range_for_trusted_detector_pixels
    def setValue_range_for_trusted_detector_pixels(self, value_range_for_trusted_detector_pixels):
        if value_range_for_trusted_detector_pixels is None:
            self._value_range_for_trusted_detector_pixels = None
        elif value_range_for_trusted_detector_pixels.__class__.__name__ == "XSDataXDSIntegerRange":
            self._value_range_for_trusted_detector_pixels = value_range_for_trusted_detector_pixels
        else:
            strMessage = "ERROR! XSDataXDSDetector.setValue_range_for_trusted_detector_pixels argument is not XSDataXDSIntegerRange but %s" % value_range_for_trusted_detector_pixels.__class__.__name__
            raise BaseException(strMessage)
    def delValue_range_for_trusted_detector_pixels(self): self._value_range_for_trusted_detector_pixels = None
    value_range_for_trusted_detector_pixels = property(getValue_range_for_trusted_detector_pixels, setValue_range_for_trusted_detector_pixels, delValue_range_for_trusted_detector_pixels, "Property for value_range_for_trusted_detector_pixels")
    # Methods and properties for the 'untrusted_rectangle' attribute
    def getUntrusted_rectangle(self): return self._untrusted_rectangle
    def setUntrusted_rectangle(self, untrusted_rectangle):
        if untrusted_rectangle is None:
            self._untrusted_rectangle = []
        elif untrusted_rectangle.__class__.__name__ == "list":
            self._untrusted_rectangle = untrusted_rectangle
        else:
            strMessage = "ERROR! XSDataXDSDetector.setUntrusted_rectangle argument is not list but %s" % untrusted_rectangle.__class__.__name__
            raise BaseException(strMessage)
    def delUntrusted_rectangle(self): self._untrusted_rectangle = None
    untrusted_rectangle = property(getUntrusted_rectangle, setUntrusted_rectangle, delUntrusted_rectangle, "Property for untrusted_rectangle")
    def addUntrusted_rectangle(self, value):
        if value is None:
            strMessage = "ERROR! XSDataXDSDetector.addUntrusted_rectangle argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXDSRectangle":
            self._untrusted_rectangle.append(value)
        else:
            strMessage = "ERROR! XSDataXDSDetector.addUntrusted_rectangle argument is not XSDataXDSRectangle but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertUntrusted_rectangle(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataXDSDetector.insertUntrusted_rectangle argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataXDSDetector.insertUntrusted_rectangle argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXDSRectangle":
            self._untrusted_rectangle[index] = value
        else:
            strMessage = "ERROR! XSDataXDSDetector.addUntrusted_rectangle argument is not XSDataXDSRectangle but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'sensor_thickness' attribute
    def getSensor_thickness(self): return self._sensor_thickness
    def setSensor_thickness(self, sensor_thickness):
        if sensor_thickness is None:
            self._sensor_thickness = None
        elif sensor_thickness.__class__.__name__ == "XSDataDouble":
            self._sensor_thickness = sensor_thickness
        else:
            strMessage = "ERROR! XSDataXDSDetector.setSensor_thickness argument is not XSDataDouble but %s" % sensor_thickness.__class__.__name__
            raise BaseException(strMessage)
    def delSensor_thickness(self): self._sensor_thickness = None
    sensor_thickness = property(getSensor_thickness, setSensor_thickness, delSensor_thickness, "Property for sensor_thickness")
    # Methods and properties for the 'trusted_region' attribute
    def getTrusted_region(self): return self._trusted_region
    def setTrusted_region(self, trusted_region):
        if trusted_region is None:
            self._trusted_region = None
        elif trusted_region.__class__.__name__ == "XSDataXDSDoubleRange":
            self._trusted_region = trusted_region
        else:
            strMessage = "ERROR! XSDataXDSDetector.setTrusted_region argument is not XSDataXDSDoubleRange but %s" % trusted_region.__class__.__name__
            raise BaseException(strMessage)
    def delTrusted_region(self): self._trusted_region = None
    trusted_region = property(getTrusted_region, setTrusted_region, delTrusted_region, "Property for trusted_region")
    def export(self, outfile, level, name_='XSDataXDSDetector'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXDSDetector'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._detector_distance is not None:
            self.detector_distance.export(outfile, level, name_='detector_distance')
        else:
            warnEmptyAttribute("detector_distance", "XSDataLength")
        if self._detector_name is not None:
            self.detector_name.export(outfile, level, name_='detector_name')
        else:
            warnEmptyAttribute("detector_name", "XSDataString")
        if self._direction_of_detector_x_axis is not None:
            self.direction_of_detector_x_axis.export(outfile, level, name_='direction_of_detector_x_axis')
        else:
            warnEmptyAttribute("direction_of_detector_x_axis", "XSDataVectorDouble")
        if self._direction_of_detector_y_axis is not None:
            self.direction_of_detector_y_axis.export(outfile, level, name_='direction_of_detector_y_axis')
        else:
            warnEmptyAttribute("direction_of_detector_y_axis", "XSDataVectorDouble")
        if self._minimum_valid_pixel_value is not None:
            self.minimum_valid_pixel_value.export(outfile, level, name_='minimum_valid_pixel_value')
        else:
            warnEmptyAttribute("minimum_valid_pixel_value", "XSDataInteger")
        if self._nx is not None:
            self.nx.export(outfile, level, name_='nx')
        else:
            warnEmptyAttribute("nx", "XSDataInteger")
        if self._ny is not None:
            self.ny.export(outfile, level, name_='ny')
        else:
            warnEmptyAttribute("ny", "XSDataInteger")
        if self._orgx is not None:
            self.orgx.export(outfile, level, name_='orgx')
        else:
            warnEmptyAttribute("orgx", "XSDataDouble")
        if self._orgy is not None:
            self.orgy.export(outfile, level, name_='orgy')
        else:
            warnEmptyAttribute("orgy", "XSDataDouble")
        if self._overload is not None:
            self.overload.export(outfile, level, name_='overload')
        else:
            warnEmptyAttribute("overload", "XSDataInteger")
        if self._qx is not None:
            self.qx.export(outfile, level, name_='qx')
        else:
            warnEmptyAttribute("qx", "XSDataLength")
        if self._qy is not None:
            self.qy.export(outfile, level, name_='qy')
        else:
            warnEmptyAttribute("qy", "XSDataLength")
        if self._value_range_for_trusted_detector_pixels is not None:
            self.value_range_for_trusted_detector_pixels.export(outfile, level, name_='value_range_for_trusted_detector_pixels')
        for untrusted_rectangle_ in self.getUntrusted_rectangle():
            untrusted_rectangle_.export(outfile, level, name_='untrusted_rectangle')
        if self._sensor_thickness is not None:
            self.sensor_thickness.export(outfile, level, name_='sensor_thickness')
        if self._trusted_region is not None:
            self.trusted_region.export(outfile, level, name_='trusted_region')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detector_distance':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setDetector_distance(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detector_name':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setDetector_name(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'direction_of_detector_x_axis':
            obj_ = XSDataVectorDouble()
            obj_.build(child_)
            self.setDirection_of_detector_x_axis(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'direction_of_detector_y_axis':
            obj_ = XSDataVectorDouble()
            obj_.build(child_)
            self.setDirection_of_detector_y_axis(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minimum_valid_pixel_value':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setMinimum_valid_pixel_value(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nx':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNx(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ny':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'orgx':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setOrgx(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'orgy':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setOrgy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'overload':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setOverload(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'qx':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setQx(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'qy':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setQy(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'value_range_for_trusted_detector_pixels':
            obj_ = XSDataXDSIntegerRange()
            obj_.build(child_)
            self.setValue_range_for_trusted_detector_pixels(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'untrusted_rectangle':
            obj_ = XSDataXDSRectangle()
            obj_.build(child_)
            self.untrusted_rectangle.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sensor_thickness':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setSensor_thickness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'trusted_region':
            obj_ = XSDataXDSDoubleRange()
            obj_.build(child_)
            self.setTrusted_region(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXDSDetector" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXDSDetector' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXDSDetector is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXDSDetector.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXDSDetector()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXDSDetector" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXDSDetector()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXDSDetector


class XSDataXDSImage(XSData):
    def __init__(self, name_template_of_data_frames=None, starting_frame=None, spot_range=None, data_range=None, background_range=None):
        XSData.__init__(self, )
        if background_range is None:
            self._background_range = []
        elif background_range.__class__.__name__ == "list":
            self._background_range = background_range
        else:
            strMessage = "ERROR! XSDataXDSImage constructor argument 'background_range' is not list but %s" % self._background_range.__class__.__name__
            raise BaseException(strMessage)
        if data_range is None:
            self._data_range = []
        elif data_range.__class__.__name__ == "list":
            self._data_range = data_range
        else:
            strMessage = "ERROR! XSDataXDSImage constructor argument 'data_range' is not list but %s" % self._data_range.__class__.__name__
            raise BaseException(strMessage)
        if spot_range is None:
            self._spot_range = []
        elif spot_range.__class__.__name__ == "list":
            self._spot_range = spot_range
        else:
            strMessage = "ERROR! XSDataXDSImage constructor argument 'spot_range' is not list but %s" % self._spot_range.__class__.__name__
            raise BaseException(strMessage)
        if starting_frame is None:
            self._starting_frame = None
        elif starting_frame.__class__.__name__ == "XSDataInteger":
            self._starting_frame = starting_frame
        else:
            strMessage = "ERROR! XSDataXDSImage constructor argument 'starting_frame' is not XSDataInteger but %s" % self._starting_frame.__class__.__name__
            raise BaseException(strMessage)
        if name_template_of_data_frames is None:
            self._name_template_of_data_frames = None
        elif name_template_of_data_frames.__class__.__name__ == "XSDataString":
            self._name_template_of_data_frames = name_template_of_data_frames
        else:
            strMessage = "ERROR! XSDataXDSImage constructor argument 'name_template_of_data_frames' is not XSDataString but %s" % self._name_template_of_data_frames.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'background_range' attribute
    def getBackground_range(self): return self._background_range
    def setBackground_range(self, background_range):
        if background_range is None:
            self._background_range = []
        elif background_range.__class__.__name__ == "list":
            self._background_range = background_range
        else:
            strMessage = "ERROR! XSDataXDSImage.setBackground_range argument is not list but %s" % background_range.__class__.__name__
            raise BaseException(strMessage)
    def delBackground_range(self): self._background_range = None
    background_range = property(getBackground_range, setBackground_range, delBackground_range, "Property for background_range")
    def addBackground_range(self, value):
        if value is None:
            strMessage = "ERROR! XSDataXDSImage.addBackground_range argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXDSIntegerRange":
            self._background_range.append(value)
        else:
            strMessage = "ERROR! XSDataXDSImage.addBackground_range argument is not XSDataXDSIntegerRange but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertBackground_range(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataXDSImage.insertBackground_range argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataXDSImage.insertBackground_range argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXDSIntegerRange":
            self._background_range[index] = value
        else:
            strMessage = "ERROR! XSDataXDSImage.addBackground_range argument is not XSDataXDSIntegerRange but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'data_range' attribute
    def getData_range(self): return self._data_range
    def setData_range(self, data_range):
        if data_range is None:
            self._data_range = []
        elif data_range.__class__.__name__ == "list":
            self._data_range = data_range
        else:
            strMessage = "ERROR! XSDataXDSImage.setData_range argument is not list but %s" % data_range.__class__.__name__
            raise BaseException(strMessage)
    def delData_range(self): self._data_range = None
    data_range = property(getData_range, setData_range, delData_range, "Property for data_range")
    def addData_range(self, value):
        if value is None:
            strMessage = "ERROR! XSDataXDSImage.addData_range argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXDSIntegerRange":
            self._data_range.append(value)
        else:
            strMessage = "ERROR! XSDataXDSImage.addData_range argument is not XSDataXDSIntegerRange but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertData_range(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataXDSImage.insertData_range argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataXDSImage.insertData_range argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXDSIntegerRange":
            self._data_range[index] = value
        else:
            strMessage = "ERROR! XSDataXDSImage.addData_range argument is not XSDataXDSIntegerRange but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'spot_range' attribute
    def getSpot_range(self): return self._spot_range
    def setSpot_range(self, spot_range):
        if spot_range is None:
            self._spot_range = []
        elif spot_range.__class__.__name__ == "list":
            self._spot_range = spot_range
        else:
            strMessage = "ERROR! XSDataXDSImage.setSpot_range argument is not list but %s" % spot_range.__class__.__name__
            raise BaseException(strMessage)
    def delSpot_range(self): self._spot_range = None
    spot_range = property(getSpot_range, setSpot_range, delSpot_range, "Property for spot_range")
    def addSpot_range(self, value):
        if value is None:
            strMessage = "ERROR! XSDataXDSImage.addSpot_range argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXDSIntegerRange":
            self._spot_range.append(value)
        else:
            strMessage = "ERROR! XSDataXDSImage.addSpot_range argument is not XSDataXDSIntegerRange but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertSpot_range(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataXDSImage.insertSpot_range argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataXDSImage.insertSpot_range argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXDSIntegerRange":
            self._spot_range[index] = value
        else:
            strMessage = "ERROR! XSDataXDSImage.addSpot_range argument is not XSDataXDSIntegerRange but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'starting_frame' attribute
    def getStarting_frame(self): return self._starting_frame
    def setStarting_frame(self, starting_frame):
        if starting_frame is None:
            self._starting_frame = None
        elif starting_frame.__class__.__name__ == "XSDataInteger":
            self._starting_frame = starting_frame
        else:
            strMessage = "ERROR! XSDataXDSImage.setStarting_frame argument is not XSDataInteger but %s" % starting_frame.__class__.__name__
            raise BaseException(strMessage)
    def delStarting_frame(self): self._starting_frame = None
    starting_frame = property(getStarting_frame, setStarting_frame, delStarting_frame, "Property for starting_frame")
    # Methods and properties for the 'name_template_of_data_frames' attribute
    def getName_template_of_data_frames(self): return self._name_template_of_data_frames
    def setName_template_of_data_frames(self, name_template_of_data_frames):
        if name_template_of_data_frames is None:
            self._name_template_of_data_frames = None
        elif name_template_of_data_frames.__class__.__name__ == "XSDataString":
            self._name_template_of_data_frames = name_template_of_data_frames
        else:
            strMessage = "ERROR! XSDataXDSImage.setName_template_of_data_frames argument is not XSDataString but %s" % name_template_of_data_frames.__class__.__name__
            raise BaseException(strMessage)
    def delName_template_of_data_frames(self): self._name_template_of_data_frames = None
    name_template_of_data_frames = property(getName_template_of_data_frames, setName_template_of_data_frames, delName_template_of_data_frames, "Property for name_template_of_data_frames")
    def export(self, outfile, level, name_='XSDataXDSImage'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXDSImage'):
        XSData.exportChildren(self, outfile, level, name_)
        for background_range_ in self.getBackground_range():
            background_range_.export(outfile, level, name_='background_range')
        if self.getBackground_range() == []:
            warnEmptyAttribute("background_range", "XSDataXDSIntegerRange")
        for data_range_ in self.getData_range():
            data_range_.export(outfile, level, name_='data_range')
        if self.getData_range() == []:
            warnEmptyAttribute("data_range", "XSDataXDSIntegerRange")
        for spot_range_ in self.getSpot_range():
            spot_range_.export(outfile, level, name_='spot_range')
        if self.getSpot_range() == []:
            warnEmptyAttribute("spot_range", "XSDataXDSIntegerRange")
        if self._starting_frame is not None:
            self.starting_frame.export(outfile, level, name_='starting_frame')
        else:
            warnEmptyAttribute("starting_frame", "XSDataInteger")
        if self._name_template_of_data_frames is not None:
            self.name_template_of_data_frames.export(outfile, level, name_='name_template_of_data_frames')
        else:
            warnEmptyAttribute("name_template_of_data_frames", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'background_range':
            obj_ = XSDataXDSIntegerRange()
            obj_.build(child_)
            self.background_range.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'data_range':
            obj_ = XSDataXDSIntegerRange()
            obj_.build(child_)
            self.data_range.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spot_range':
            obj_ = XSDataXDSIntegerRange()
            obj_.build(child_)
            self.spot_range.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'starting_frame':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setStarting_frame(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'name_template_of_data_frames':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setName_template_of_data_frames(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXDSImage" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXDSImage' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXDSImage is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXDSImage.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXDSImage()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXDSImage" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXDSImage()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXDSImage


class XSDataXDSImageLink(XSData):
    def __init__(self, target=None, source=None):
        XSData.__init__(self, )
        if source is None:
            self._source = None
        elif source.__class__.__name__ == "XSDataFile":
            self._source = source
        else:
            strMessage = "ERROR! XSDataXDSImageLink constructor argument 'source' is not XSDataFile but %s" % self._source.__class__.__name__
            raise BaseException(strMessage)
        if target is None:
            self._target = None
        elif target.__class__.__name__ == "XSDataString":
            self._target = target
        else:
            strMessage = "ERROR! XSDataXDSImageLink constructor argument 'target' is not XSDataString but %s" % self._target.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'source' attribute
    def getSource(self): return self._source
    def setSource(self, source):
        if source is None:
            self._source = None
        elif source.__class__.__name__ == "XSDataFile":
            self._source = source
        else:
            strMessage = "ERROR! XSDataXDSImageLink.setSource argument is not XSDataFile but %s" % source.__class__.__name__
            raise BaseException(strMessage)
    def delSource(self): self._source = None
    source = property(getSource, setSource, delSource, "Property for source")
    # Methods and properties for the 'target' attribute
    def getTarget(self): return self._target
    def setTarget(self, target):
        if target is None:
            self._target = None
        elif target.__class__.__name__ == "XSDataString":
            self._target = target
        else:
            strMessage = "ERROR! XSDataXDSImageLink.setTarget argument is not XSDataString but %s" % target.__class__.__name__
            raise BaseException(strMessage)
    def delTarget(self): self._target = None
    target = property(getTarget, setTarget, delTarget, "Property for target")
    def export(self, outfile, level, name_='XSDataXDSImageLink'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXDSImageLink'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._source is not None:
            self.source.export(outfile, level, name_='source')
        else:
            warnEmptyAttribute("source", "XSDataFile")
        if self._target is not None:
            self.target.export(outfile, level, name_='target')
        else:
            warnEmptyAttribute("target", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'source':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSource(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'target':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setTarget(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXDSImageLink" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXDSImageLink' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXDSImageLink is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXDSImageLink.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXDSImageLink()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXDSImageLink" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXDSImageLink()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXDSImageLink


class XSDataXDSRectangle(XSData):
    def __init__(self, y2=None, y1=None, x2=None, x1=None):
        XSData.__init__(self, )
        if x1 is None:
            self._x1 = None
        elif x1.__class__.__name__ == "XSDataInteger":
            self._x1 = x1
        else:
            strMessage = "ERROR! XSDataXDSRectangle constructor argument 'x1' is not XSDataInteger but %s" % self._x1.__class__.__name__
            raise BaseException(strMessage)
        if x2 is None:
            self._x2 = None
        elif x2.__class__.__name__ == "XSDataInteger":
            self._x2 = x2
        else:
            strMessage = "ERROR! XSDataXDSRectangle constructor argument 'x2' is not XSDataInteger but %s" % self._x2.__class__.__name__
            raise BaseException(strMessage)
        if y1 is None:
            self._y1 = None
        elif y1.__class__.__name__ == "XSDataInteger":
            self._y1 = y1
        else:
            strMessage = "ERROR! XSDataXDSRectangle constructor argument 'y1' is not XSDataInteger but %s" % self._y1.__class__.__name__
            raise BaseException(strMessage)
        if y2 is None:
            self._y2 = None
        elif y2.__class__.__name__ == "XSDataInteger":
            self._y2 = y2
        else:
            strMessage = "ERROR! XSDataXDSRectangle constructor argument 'y2' is not XSDataInteger but %s" % self._y2.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'x1' attribute
    def getX1(self): return self._x1
    def setX1(self, x1):
        if x1 is None:
            self._x1 = None
        elif x1.__class__.__name__ == "XSDataInteger":
            self._x1 = x1
        else:
            strMessage = "ERROR! XSDataXDSRectangle.setX1 argument is not XSDataInteger but %s" % x1.__class__.__name__
            raise BaseException(strMessage)
    def delX1(self): self._x1 = None
    x1 = property(getX1, setX1, delX1, "Property for x1")
    # Methods and properties for the 'x2' attribute
    def getX2(self): return self._x2
    def setX2(self, x2):
        if x2 is None:
            self._x2 = None
        elif x2.__class__.__name__ == "XSDataInteger":
            self._x2 = x2
        else:
            strMessage = "ERROR! XSDataXDSRectangle.setX2 argument is not XSDataInteger but %s" % x2.__class__.__name__
            raise BaseException(strMessage)
    def delX2(self): self._x2 = None
    x2 = property(getX2, setX2, delX2, "Property for x2")
    # Methods and properties for the 'y1' attribute
    def getY1(self): return self._y1
    def setY1(self, y1):
        if y1 is None:
            self._y1 = None
        elif y1.__class__.__name__ == "XSDataInteger":
            self._y1 = y1
        else:
            strMessage = "ERROR! XSDataXDSRectangle.setY1 argument is not XSDataInteger but %s" % y1.__class__.__name__
            raise BaseException(strMessage)
    def delY1(self): self._y1 = None
    y1 = property(getY1, setY1, delY1, "Property for y1")
    # Methods and properties for the 'y2' attribute
    def getY2(self): return self._y2
    def setY2(self, y2):
        if y2 is None:
            self._y2 = None
        elif y2.__class__.__name__ == "XSDataInteger":
            self._y2 = y2
        else:
            strMessage = "ERROR! XSDataXDSRectangle.setY2 argument is not XSDataInteger but %s" % y2.__class__.__name__
            raise BaseException(strMessage)
    def delY2(self): self._y2 = None
    y2 = property(getY2, setY2, delY2, "Property for y2")
    def export(self, outfile, level, name_='XSDataXDSRectangle'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXDSRectangle'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._x1 is not None:
            self.x1.export(outfile, level, name_='x1')
        else:
            warnEmptyAttribute("x1", "XSDataInteger")
        if self._x2 is not None:
            self.x2.export(outfile, level, name_='x2')
        else:
            warnEmptyAttribute("x2", "XSDataInteger")
        if self._y1 is not None:
            self.y1.export(outfile, level, name_='y1')
        else:
            warnEmptyAttribute("y1", "XSDataInteger")
        if self._y2 is not None:
            self.y2.export(outfile, level, name_='y2')
        else:
            warnEmptyAttribute("y2", "XSDataInteger")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'x1':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setX1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'x2':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setX2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'y1':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setY1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'y2':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setY2(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXDSRectangle" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXDSRectangle' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXDSRectangle is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXDSRectangle.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXDSRectangle()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXDSRectangle" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXDSRectangle()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXDSRectangle


class XSDataXDSVector(XSData):
    def __init__(self, v3=None, v2=None, v1=None):
        XSData.__init__(self, )
        if v1 is None:
            self._v1 = None
        elif v1.__class__.__name__ == "XSDataFloat":
            self._v1 = v1
        else:
            strMessage = "ERROR! XSDataXDSVector constructor argument 'v1' is not XSDataFloat but %s" % self._v1.__class__.__name__
            raise BaseException(strMessage)
        if v2 is None:
            self._v2 = None
        elif v2.__class__.__name__ == "XSDataFloat":
            self._v2 = v2
        else:
            strMessage = "ERROR! XSDataXDSVector constructor argument 'v2' is not XSDataFloat but %s" % self._v2.__class__.__name__
            raise BaseException(strMessage)
        if v3 is None:
            self._v3 = None
        elif v3.__class__.__name__ == "XSDataFloat":
            self._v3 = v3
        else:
            strMessage = "ERROR! XSDataXDSVector constructor argument 'v3' is not XSDataFloat but %s" % self._v3.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'v1' attribute
    def getV1(self): return self._v1
    def setV1(self, v1):
        if v1 is None:
            self._v1 = None
        elif v1.__class__.__name__ == "XSDataFloat":
            self._v1 = v1
        else:
            strMessage = "ERROR! XSDataXDSVector.setV1 argument is not XSDataFloat but %s" % v1.__class__.__name__
            raise BaseException(strMessage)
    def delV1(self): self._v1 = None
    v1 = property(getV1, setV1, delV1, "Property for v1")
    # Methods and properties for the 'v2' attribute
    def getV2(self): return self._v2
    def setV2(self, v2):
        if v2 is None:
            self._v2 = None
        elif v2.__class__.__name__ == "XSDataFloat":
            self._v2 = v2
        else:
            strMessage = "ERROR! XSDataXDSVector.setV2 argument is not XSDataFloat but %s" % v2.__class__.__name__
            raise BaseException(strMessage)
    def delV2(self): self._v2 = None
    v2 = property(getV2, setV2, delV2, "Property for v2")
    # Methods and properties for the 'v3' attribute
    def getV3(self): return self._v3
    def setV3(self, v3):
        if v3 is None:
            self._v3 = None
        elif v3.__class__.__name__ == "XSDataFloat":
            self._v3 = v3
        else:
            strMessage = "ERROR! XSDataXDSVector.setV3 argument is not XSDataFloat but %s" % v3.__class__.__name__
            raise BaseException(strMessage)
    def delV3(self): self._v3 = None
    v3 = property(getV3, setV3, delV3, "Property for v3")
    def export(self, outfile, level, name_='XSDataXDSVector'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXDSVector'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._v1 is not None:
            self.v1.export(outfile, level, name_='v1')
        else:
            warnEmptyAttribute("v1", "XSDataFloat")
        if self._v2 is not None:
            self.v2.export(outfile, level, name_='v2')
        else:
            warnEmptyAttribute("v2", "XSDataFloat")
        if self._v3 is not None:
            self.v3.export(outfile, level, name_='v3')
        else:
            warnEmptyAttribute("v3", "XSDataFloat")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'v1':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setV1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'v2':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setV2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'v3':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setV3(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXDSVector" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXDSVector' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXDSVector is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXDSVector.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXDSVector()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXDSVector" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXDSVector()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXDSVector


class XSDataXscaleCompletenessEntry(XSDataXdsCompletenessEntry):
    def __init__(self, half_dataset_correlation=None, isig=None, rfactor=None, complete=None, possible=None, unique=None, observed=None, res=None, multiplicity=None):
        XSDataXdsCompletenessEntry.__init__(self, half_dataset_correlation, isig, rfactor, complete, possible, unique, observed, res)
        if multiplicity is None:
            self._multiplicity = None
        elif multiplicity.__class__.__name__ == "XSDataDouble":
            self._multiplicity = multiplicity
        else:
            strMessage = "ERROR! XSDataXscaleCompletenessEntry constructor argument 'multiplicity' is not XSDataDouble but %s" % self._multiplicity.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'multiplicity' attribute
    def getMultiplicity(self): return self._multiplicity
    def setMultiplicity(self, multiplicity):
        if multiplicity is None:
            self._multiplicity = None
        elif multiplicity.__class__.__name__ == "XSDataDouble":
            self._multiplicity = multiplicity
        else:
            strMessage = "ERROR! XSDataXscaleCompletenessEntry.setMultiplicity argument is not XSDataDouble but %s" % multiplicity.__class__.__name__
            raise BaseException(strMessage)
    def delMultiplicity(self): self._multiplicity = None
    multiplicity = property(getMultiplicity, setMultiplicity, delMultiplicity, "Property for multiplicity")
    def export(self, outfile, level, name_='XSDataXscaleCompletenessEntry'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXscaleCompletenessEntry'):
        XSDataXdsCompletenessEntry.exportChildren(self, outfile, level, name_)
        if self._multiplicity is not None:
            self.multiplicity.export(outfile, level, name_='multiplicity')
        else:
            warnEmptyAttribute("multiplicity", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'multiplicity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMultiplicity(obj_)
        XSDataXdsCompletenessEntry.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXscaleCompletenessEntry" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXscaleCompletenessEntry' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXscaleCompletenessEntry is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXscaleCompletenessEntry.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleCompletenessEntry()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXscaleCompletenessEntry" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleCompletenessEntry()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXscaleCompletenessEntry


class XSDataXDSFilePaths(XSDataInput):
    def __init__(self, configuration=None, blankCbf=None, gainCbf=None, bkginitCbf=None, yCorrectionsCbf=None, xCorrectionsCbf=None, xparmXds=None):
        XSDataInput.__init__(self, configuration)
        if xparmXds is None:
            self._xparmXds = None
        elif xparmXds.__class__.__name__ == "XSDataFile":
            self._xparmXds = xparmXds
        else:
            strMessage = "ERROR! XSDataXDSFilePaths constructor argument 'xparmXds' is not XSDataFile but %s" % self._xparmXds.__class__.__name__
            raise BaseException(strMessage)
        if xCorrectionsCbf is None:
            self._xCorrectionsCbf = None
        elif xCorrectionsCbf.__class__.__name__ == "XSDataFile":
            self._xCorrectionsCbf = xCorrectionsCbf
        else:
            strMessage = "ERROR! XSDataXDSFilePaths constructor argument 'xCorrectionsCbf' is not XSDataFile but %s" % self._xCorrectionsCbf.__class__.__name__
            raise BaseException(strMessage)
        if yCorrectionsCbf is None:
            self._yCorrectionsCbf = None
        elif yCorrectionsCbf.__class__.__name__ == "XSDataFile":
            self._yCorrectionsCbf = yCorrectionsCbf
        else:
            strMessage = "ERROR! XSDataXDSFilePaths constructor argument 'yCorrectionsCbf' is not XSDataFile but %s" % self._yCorrectionsCbf.__class__.__name__
            raise BaseException(strMessage)
        if bkginitCbf is None:
            self._bkginitCbf = None
        elif bkginitCbf.__class__.__name__ == "XSDataFile":
            self._bkginitCbf = bkginitCbf
        else:
            strMessage = "ERROR! XSDataXDSFilePaths constructor argument 'bkginitCbf' is not XSDataFile but %s" % self._bkginitCbf.__class__.__name__
            raise BaseException(strMessage)
        if gainCbf is None:
            self._gainCbf = None
        elif gainCbf.__class__.__name__ == "XSDataFile":
            self._gainCbf = gainCbf
        else:
            strMessage = "ERROR! XSDataXDSFilePaths constructor argument 'gainCbf' is not XSDataFile but %s" % self._gainCbf.__class__.__name__
            raise BaseException(strMessage)
        if blankCbf is None:
            self._blankCbf = None
        elif blankCbf.__class__.__name__ == "XSDataFile":
            self._blankCbf = blankCbf
        else:
            strMessage = "ERROR! XSDataXDSFilePaths constructor argument 'blankCbf' is not XSDataFile but %s" % self._blankCbf.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'xparmXds' attribute
    def getXparmXds(self): return self._xparmXds
    def setXparmXds(self, xparmXds):
        if xparmXds is None:
            self._xparmXds = None
        elif xparmXds.__class__.__name__ == "XSDataFile":
            self._xparmXds = xparmXds
        else:
            strMessage = "ERROR! XSDataXDSFilePaths.setXparmXds argument is not XSDataFile but %s" % xparmXds.__class__.__name__
            raise BaseException(strMessage)
    def delXparmXds(self): self._xparmXds = None
    xparmXds = property(getXparmXds, setXparmXds, delXparmXds, "Property for xparmXds")
    # Methods and properties for the 'xCorrectionsCbf' attribute
    def getXCorrectionsCbf(self): return self._xCorrectionsCbf
    def setXCorrectionsCbf(self, xCorrectionsCbf):
        if xCorrectionsCbf is None:
            self._xCorrectionsCbf = None
        elif xCorrectionsCbf.__class__.__name__ == "XSDataFile":
            self._xCorrectionsCbf = xCorrectionsCbf
        else:
            strMessage = "ERROR! XSDataXDSFilePaths.setXCorrectionsCbf argument is not XSDataFile but %s" % xCorrectionsCbf.__class__.__name__
            raise BaseException(strMessage)
    def delXCorrectionsCbf(self): self._xCorrectionsCbf = None
    xCorrectionsCbf = property(getXCorrectionsCbf, setXCorrectionsCbf, delXCorrectionsCbf, "Property for xCorrectionsCbf")
    # Methods and properties for the 'yCorrectionsCbf' attribute
    def getYCorrectionsCbf(self): return self._yCorrectionsCbf
    def setYCorrectionsCbf(self, yCorrectionsCbf):
        if yCorrectionsCbf is None:
            self._yCorrectionsCbf = None
        elif yCorrectionsCbf.__class__.__name__ == "XSDataFile":
            self._yCorrectionsCbf = yCorrectionsCbf
        else:
            strMessage = "ERROR! XSDataXDSFilePaths.setYCorrectionsCbf argument is not XSDataFile but %s" % yCorrectionsCbf.__class__.__name__
            raise BaseException(strMessage)
    def delYCorrectionsCbf(self): self._yCorrectionsCbf = None
    yCorrectionsCbf = property(getYCorrectionsCbf, setYCorrectionsCbf, delYCorrectionsCbf, "Property for yCorrectionsCbf")
    # Methods and properties for the 'bkginitCbf' attribute
    def getBkginitCbf(self): return self._bkginitCbf
    def setBkginitCbf(self, bkginitCbf):
        if bkginitCbf is None:
            self._bkginitCbf = None
        elif bkginitCbf.__class__.__name__ == "XSDataFile":
            self._bkginitCbf = bkginitCbf
        else:
            strMessage = "ERROR! XSDataXDSFilePaths.setBkginitCbf argument is not XSDataFile but %s" % bkginitCbf.__class__.__name__
            raise BaseException(strMessage)
    def delBkginitCbf(self): self._bkginitCbf = None
    bkginitCbf = property(getBkginitCbf, setBkginitCbf, delBkginitCbf, "Property for bkginitCbf")
    # Methods and properties for the 'gainCbf' attribute
    def getGainCbf(self): return self._gainCbf
    def setGainCbf(self, gainCbf):
        if gainCbf is None:
            self._gainCbf = None
        elif gainCbf.__class__.__name__ == "XSDataFile":
            self._gainCbf = gainCbf
        else:
            strMessage = "ERROR! XSDataXDSFilePaths.setGainCbf argument is not XSDataFile but %s" % gainCbf.__class__.__name__
            raise BaseException(strMessage)
    def delGainCbf(self): self._gainCbf = None
    gainCbf = property(getGainCbf, setGainCbf, delGainCbf, "Property for gainCbf")
    # Methods and properties for the 'blankCbf' attribute
    def getBlankCbf(self): return self._blankCbf
    def setBlankCbf(self, blankCbf):
        if blankCbf is None:
            self._blankCbf = None
        elif blankCbf.__class__.__name__ == "XSDataFile":
            self._blankCbf = blankCbf
        else:
            strMessage = "ERROR! XSDataXDSFilePaths.setBlankCbf argument is not XSDataFile but %s" % blankCbf.__class__.__name__
            raise BaseException(strMessage)
    def delBlankCbf(self): self._blankCbf = None
    blankCbf = property(getBlankCbf, setBlankCbf, delBlankCbf, "Property for blankCbf")
    def export(self, outfile, level, name_='XSDataXDSFilePaths'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXDSFilePaths'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._xparmXds is not None:
            self.xparmXds.export(outfile, level, name_='xparmXds')
        if self._xCorrectionsCbf is not None:
            self.xCorrectionsCbf.export(outfile, level, name_='xCorrectionsCbf')
        if self._yCorrectionsCbf is not None:
            self.yCorrectionsCbf.export(outfile, level, name_='yCorrectionsCbf')
        if self._bkginitCbf is not None:
            self.bkginitCbf.export(outfile, level, name_='bkginitCbf')
        if self._gainCbf is not None:
            self.gainCbf.export(outfile, level, name_='gainCbf')
        if self._blankCbf is not None:
            self.blankCbf.export(outfile, level, name_='blankCbf')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xparmXds':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setXparmXds(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xCorrectionsCbf':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setXCorrectionsCbf(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'yCorrectionsCbf':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setYCorrectionsCbf(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bkginitCbf':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setBkginitCbf(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gainCbf':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGainCbf(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'blankCbf':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setBlankCbf(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXDSFilePaths" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXDSFilePaths' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXDSFilePaths is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXDSFilePaths.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXDSFilePaths()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXDSFilePaths" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXDSFilePaths()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXDSFilePaths


class XSDataInputXDS(XSDataInput):
    def __init__(self, configuration=None, filePaths=None, image_link=None, image=None, goniostat=None, detector=None, crystal=None, beam=None):
        XSDataInput.__init__(self, configuration)
        if beam is None:
            self._beam = None
        elif beam.__class__.__name__ == "XSDataXDSBeam":
            self._beam = beam
        else:
            strMessage = "ERROR! XSDataInputXDS constructor argument 'beam' is not XSDataXDSBeam but %s" % self._beam.__class__.__name__
            raise BaseException(strMessage)
        if crystal is None:
            self._crystal = None
        elif crystal.__class__.__name__ == "XSDataXDSCrystal":
            self._crystal = crystal
        else:
            strMessage = "ERROR! XSDataInputXDS constructor argument 'crystal' is not XSDataXDSCrystal but %s" % self._crystal.__class__.__name__
            raise BaseException(strMessage)
        if detector is None:
            self._detector = None
        elif detector.__class__.__name__ == "XSDataXDSDetector":
            self._detector = detector
        else:
            strMessage = "ERROR! XSDataInputXDS constructor argument 'detector' is not XSDataXDSDetector but %s" % self._detector.__class__.__name__
            raise BaseException(strMessage)
        if goniostat is None:
            self._goniostat = None
        elif goniostat.__class__.__name__ == "XSDataXDSGoniostat":
            self._goniostat = goniostat
        else:
            strMessage = "ERROR! XSDataInputXDS constructor argument 'goniostat' is not XSDataXDSGoniostat but %s" % self._goniostat.__class__.__name__
            raise BaseException(strMessage)
        if image is None:
            self._image = None
        elif image.__class__.__name__ == "XSDataXDSImage":
            self._image = image
        else:
            strMessage = "ERROR! XSDataInputXDS constructor argument 'image' is not XSDataXDSImage but %s" % self._image.__class__.__name__
            raise BaseException(strMessage)
        if image_link is None:
            self._image_link = []
        elif image_link.__class__.__name__ == "list":
            self._image_link = image_link
        else:
            strMessage = "ERROR! XSDataInputXDS constructor argument 'image_link' is not list but %s" % self._image_link.__class__.__name__
            raise BaseException(strMessage)
        if filePaths is None:
            self._filePaths = None
        elif filePaths.__class__.__name__ == "XSDataXDSFilePaths":
            self._filePaths = filePaths
        else:
            strMessage = "ERROR! XSDataInputXDS constructor argument 'filePaths' is not XSDataXDSFilePaths but %s" % self._filePaths.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'beam' attribute
    def getBeam(self): return self._beam
    def setBeam(self, beam):
        if beam is None:
            self._beam = None
        elif beam.__class__.__name__ == "XSDataXDSBeam":
            self._beam = beam
        else:
            strMessage = "ERROR! XSDataInputXDS.setBeam argument is not XSDataXDSBeam but %s" % beam.__class__.__name__
            raise BaseException(strMessage)
    def delBeam(self): self._beam = None
    beam = property(getBeam, setBeam, delBeam, "Property for beam")
    # Methods and properties for the 'crystal' attribute
    def getCrystal(self): return self._crystal
    def setCrystal(self, crystal):
        if crystal is None:
            self._crystal = None
        elif crystal.__class__.__name__ == "XSDataXDSCrystal":
            self._crystal = crystal
        else:
            strMessage = "ERROR! XSDataInputXDS.setCrystal argument is not XSDataXDSCrystal but %s" % crystal.__class__.__name__
            raise BaseException(strMessage)
    def delCrystal(self): self._crystal = None
    crystal = property(getCrystal, setCrystal, delCrystal, "Property for crystal")
    # Methods and properties for the 'detector' attribute
    def getDetector(self): return self._detector
    def setDetector(self, detector):
        if detector is None:
            self._detector = None
        elif detector.__class__.__name__ == "XSDataXDSDetector":
            self._detector = detector
        else:
            strMessage = "ERROR! XSDataInputXDS.setDetector argument is not XSDataXDSDetector but %s" % detector.__class__.__name__
            raise BaseException(strMessage)
    def delDetector(self): self._detector = None
    detector = property(getDetector, setDetector, delDetector, "Property for detector")
    # Methods and properties for the 'goniostat' attribute
    def getGoniostat(self): return self._goniostat
    def setGoniostat(self, goniostat):
        if goniostat is None:
            self._goniostat = None
        elif goniostat.__class__.__name__ == "XSDataXDSGoniostat":
            self._goniostat = goniostat
        else:
            strMessage = "ERROR! XSDataInputXDS.setGoniostat argument is not XSDataXDSGoniostat but %s" % goniostat.__class__.__name__
            raise BaseException(strMessage)
    def delGoniostat(self): self._goniostat = None
    goniostat = property(getGoniostat, setGoniostat, delGoniostat, "Property for goniostat")
    # Methods and properties for the 'image' attribute
    def getImage(self): return self._image
    def setImage(self, image):
        if image is None:
            self._image = None
        elif image.__class__.__name__ == "XSDataXDSImage":
            self._image = image
        else:
            strMessage = "ERROR! XSDataInputXDS.setImage argument is not XSDataXDSImage but %s" % image.__class__.__name__
            raise BaseException(strMessage)
    def delImage(self): self._image = None
    image = property(getImage, setImage, delImage, "Property for image")
    # Methods and properties for the 'image_link' attribute
    def getImage_link(self): return self._image_link
    def setImage_link(self, image_link):
        if image_link is None:
            self._image_link = []
        elif image_link.__class__.__name__ == "list":
            self._image_link = image_link
        else:
            strMessage = "ERROR! XSDataInputXDS.setImage_link argument is not list but %s" % image_link.__class__.__name__
            raise BaseException(strMessage)
    def delImage_link(self): self._image_link = None
    image_link = property(getImage_link, setImage_link, delImage_link, "Property for image_link")
    def addImage_link(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputXDS.addImage_link argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXDSImageLink":
            self._image_link.append(value)
        else:
            strMessage = "ERROR! XSDataInputXDS.addImage_link argument is not XSDataXDSImageLink but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertImage_link(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputXDS.insertImage_link argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputXDS.insertImage_link argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXDSImageLink":
            self._image_link[index] = value
        else:
            strMessage = "ERROR! XSDataInputXDS.addImage_link argument is not XSDataXDSImageLink but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'filePaths' attribute
    def getFilePaths(self): return self._filePaths
    def setFilePaths(self, filePaths):
        if filePaths is None:
            self._filePaths = None
        elif filePaths.__class__.__name__ == "XSDataXDSFilePaths":
            self._filePaths = filePaths
        else:
            strMessage = "ERROR! XSDataInputXDS.setFilePaths argument is not XSDataXDSFilePaths but %s" % filePaths.__class__.__name__
            raise BaseException(strMessage)
    def delFilePaths(self): self._filePaths = None
    filePaths = property(getFilePaths, setFilePaths, delFilePaths, "Property for filePaths")
    def export(self, outfile, level, name_='XSDataInputXDS'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputXDS'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._beam is not None:
            self.beam.export(outfile, level, name_='beam')
        else:
            warnEmptyAttribute("beam", "XSDataXDSBeam")
        if self._crystal is not None:
            self.crystal.export(outfile, level, name_='crystal')
        if self._detector is not None:
            self.detector.export(outfile, level, name_='detector')
        else:
            warnEmptyAttribute("detector", "XSDataXDSDetector")
        if self._goniostat is not None:
            self.goniostat.export(outfile, level, name_='goniostat')
        else:
            warnEmptyAttribute("goniostat", "XSDataXDSGoniostat")
        if self._image is not None:
            self.image.export(outfile, level, name_='image')
        else:
            warnEmptyAttribute("image", "XSDataXDSImage")
        for image_link_ in self.getImage_link():
            image_link_.export(outfile, level, name_='image_link')
        if self.getImage_link() == []:
            warnEmptyAttribute("image_link", "XSDataXDSImageLink")
        if self._filePaths is not None:
            self.filePaths.export(outfile, level, name_='filePaths')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beam':
            obj_ = XSDataXDSBeam()
            obj_.build(child_)
            self.setBeam(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystal':
            obj_ = XSDataXDSCrystal()
            obj_.build(child_)
            self.setCrystal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detector':
            obj_ = XSDataXDSDetector()
            obj_.build(child_)
            self.setDetector(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'goniostat':
            obj_ = XSDataXDSGoniostat()
            obj_.build(child_)
            self.setGoniostat(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataXDSImage()
            obj_.build(child_)
            self.setImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image_link':
            obj_ = XSDataXDSImageLink()
            obj_.build(child_)
            self.image_link.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'filePaths':
            obj_ = XSDataXDSFilePaths()
            obj_.build(child_)
            self.setFilePaths(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputXDS" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputXDS' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputXDS is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputXDS.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputXDS()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputXDS" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputXDS()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputXDS


class XSDataMinimalXdsIn(XSDataInput):
    def __init__(self, configuration=None, end_image=None, start_image=None, unit_cell=None, spacegroup=None, spot_range=None, resolution_range=None, friedels_law=None, maxjobs=None, maxproc=None, job=None, input_file=None):
        XSDataInput.__init__(self, configuration)
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'input_file' is not XSDataString but %s" % self._input_file.__class__.__name__
            raise BaseException(strMessage)
        if job is None:
            self._job = None
        elif job.__class__.__name__ == "XSDataString":
            self._job = job
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'job' is not XSDataString but %s" % self._job.__class__.__name__
            raise BaseException(strMessage)
        if maxproc is None:
            self._maxproc = None
        elif maxproc.__class__.__name__ == "XSDataInteger":
            self._maxproc = maxproc
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'maxproc' is not XSDataInteger but %s" % self._maxproc.__class__.__name__
            raise BaseException(strMessage)
        if maxjobs is None:
            self._maxjobs = None
        elif maxjobs.__class__.__name__ == "XSDataInteger":
            self._maxjobs = maxjobs
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'maxjobs' is not XSDataInteger but %s" % self._maxjobs.__class__.__name__
            raise BaseException(strMessage)
        if friedels_law is None:
            self._friedels_law = None
        elif friedels_law.__class__.__name__ == "XSDataBoolean":
            self._friedels_law = friedels_law
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'friedels_law' is not XSDataBoolean but %s" % self._friedels_law.__class__.__name__
            raise BaseException(strMessage)
        if resolution_range is None:
            self._resolution_range = []
        elif resolution_range.__class__.__name__ == "list":
            self._resolution_range = resolution_range
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'resolution_range' is not list but %s" % self._resolution_range.__class__.__name__
            raise BaseException(strMessage)
        if spot_range is None:
            self._spot_range = []
        elif spot_range.__class__.__name__ == "list":
            self._spot_range = spot_range
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'spot_range' is not list but %s" % self._spot_range.__class__.__name__
            raise BaseException(strMessage)
        if spacegroup is None:
            self._spacegroup = None
        elif spacegroup.__class__.__name__ == "XSDataInteger":
            self._spacegroup = spacegroup
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'spacegroup' is not XSDataInteger but %s" % self._spacegroup.__class__.__name__
            raise BaseException(strMessage)
        if unit_cell is None:
            self._unit_cell = None
        elif unit_cell.__class__.__name__ == "XSDataString":
            self._unit_cell = unit_cell
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'unit_cell' is not XSDataString but %s" % self._unit_cell.__class__.__name__
            raise BaseException(strMessage)
        if start_image is None:
            self._start_image = None
        elif start_image.__class__.__name__ == "XSDataInteger":
            self._start_image = start_image
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'start_image' is not XSDataInteger but %s" % self._start_image.__class__.__name__
            raise BaseException(strMessage)
        if end_image is None:
            self._end_image = None
        elif end_image.__class__.__name__ == "XSDataInteger":
            self._end_image = end_image
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn constructor argument 'end_image' is not XSDataInteger but %s" % self._end_image.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'input_file' attribute
    def getInput_file(self): return self._input_file
    def setInput_file(self, input_file):
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setInput_file argument is not XSDataString but %s" % input_file.__class__.__name__
            raise BaseException(strMessage)
    def delInput_file(self): self._input_file = None
    input_file = property(getInput_file, setInput_file, delInput_file, "Property for input_file")
    # Methods and properties for the 'job' attribute
    def getJob(self): return self._job
    def setJob(self, job):
        if job is None:
            self._job = None
        elif job.__class__.__name__ == "XSDataString":
            self._job = job
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setJob argument is not XSDataString but %s" % job.__class__.__name__
            raise BaseException(strMessage)
    def delJob(self): self._job = None
    job = property(getJob, setJob, delJob, "Property for job")
    # Methods and properties for the 'maxproc' attribute
    def getMaxproc(self): return self._maxproc
    def setMaxproc(self, maxproc):
        if maxproc is None:
            self._maxproc = None
        elif maxproc.__class__.__name__ == "XSDataInteger":
            self._maxproc = maxproc
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setMaxproc argument is not XSDataInteger but %s" % maxproc.__class__.__name__
            raise BaseException(strMessage)
    def delMaxproc(self): self._maxproc = None
    maxproc = property(getMaxproc, setMaxproc, delMaxproc, "Property for maxproc")
    # Methods and properties for the 'maxjobs' attribute
    def getMaxjobs(self): return self._maxjobs
    def setMaxjobs(self, maxjobs):
        if maxjobs is None:
            self._maxjobs = None
        elif maxjobs.__class__.__name__ == "XSDataInteger":
            self._maxjobs = maxjobs
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setMaxjobs argument is not XSDataInteger but %s" % maxjobs.__class__.__name__
            raise BaseException(strMessage)
    def delMaxjobs(self): self._maxjobs = None
    maxjobs = property(getMaxjobs, setMaxjobs, delMaxjobs, "Property for maxjobs")
    # Methods and properties for the 'friedels_law' attribute
    def getFriedels_law(self): return self._friedels_law
    def setFriedels_law(self, friedels_law):
        if friedels_law is None:
            self._friedels_law = None
        elif friedels_law.__class__.__name__ == "XSDataBoolean":
            self._friedels_law = friedels_law
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setFriedels_law argument is not XSDataBoolean but %s" % friedels_law.__class__.__name__
            raise BaseException(strMessage)
    def delFriedels_law(self): self._friedels_law = None
    friedels_law = property(getFriedels_law, setFriedels_law, delFriedels_law, "Property for friedels_law")
    # Methods and properties for the 'resolution_range' attribute
    def getResolution_range(self): return self._resolution_range
    def setResolution_range(self, resolution_range):
        if resolution_range is None:
            self._resolution_range = []
        elif resolution_range.__class__.__name__ == "list":
            self._resolution_range = resolution_range
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setResolution_range argument is not list but %s" % resolution_range.__class__.__name__
            raise BaseException(strMessage)
    def delResolution_range(self): self._resolution_range = None
    resolution_range = property(getResolution_range, setResolution_range, delResolution_range, "Property for resolution_range")
    def addResolution_range(self, value):
        if value is None:
            strMessage = "ERROR! XSDataMinimalXdsIn.addResolution_range argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._resolution_range.append(value)
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.addResolution_range argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertResolution_range(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataMinimalXdsIn.insertResolution_range argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataMinimalXdsIn.insertResolution_range argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._resolution_range[index] = value
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.addResolution_range argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'spot_range' attribute
    def getSpot_range(self): return self._spot_range
    def setSpot_range(self, spot_range):
        if spot_range is None:
            self._spot_range = []
        elif spot_range.__class__.__name__ == "list":
            self._spot_range = spot_range
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setSpot_range argument is not list but %s" % spot_range.__class__.__name__
            raise BaseException(strMessage)
    def delSpot_range(self): self._spot_range = None
    spot_range = property(getSpot_range, setSpot_range, delSpot_range, "Property for spot_range")
    def addSpot_range(self, value):
        if value is None:
            strMessage = "ERROR! XSDataMinimalXdsIn.addSpot_range argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataRange":
            self._spot_range.append(value)
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.addSpot_range argument is not XSDataRange but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertSpot_range(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataMinimalXdsIn.insertSpot_range argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataMinimalXdsIn.insertSpot_range argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataRange":
            self._spot_range[index] = value
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.addSpot_range argument is not XSDataRange but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'spacegroup' attribute
    def getSpacegroup(self): return self._spacegroup
    def setSpacegroup(self, spacegroup):
        if spacegroup is None:
            self._spacegroup = None
        elif spacegroup.__class__.__name__ == "XSDataInteger":
            self._spacegroup = spacegroup
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setSpacegroup argument is not XSDataInteger but %s" % spacegroup.__class__.__name__
            raise BaseException(strMessage)
    def delSpacegroup(self): self._spacegroup = None
    spacegroup = property(getSpacegroup, setSpacegroup, delSpacegroup, "Property for spacegroup")
    # Methods and properties for the 'unit_cell' attribute
    def getUnit_cell(self): return self._unit_cell
    def setUnit_cell(self, unit_cell):
        if unit_cell is None:
            self._unit_cell = None
        elif unit_cell.__class__.__name__ == "XSDataString":
            self._unit_cell = unit_cell
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setUnit_cell argument is not XSDataString but %s" % unit_cell.__class__.__name__
            raise BaseException(strMessage)
    def delUnit_cell(self): self._unit_cell = None
    unit_cell = property(getUnit_cell, setUnit_cell, delUnit_cell, "Property for unit_cell")
    # Methods and properties for the 'start_image' attribute
    def getStart_image(self): return self._start_image
    def setStart_image(self, start_image):
        if start_image is None:
            self._start_image = None
        elif start_image.__class__.__name__ == "XSDataInteger":
            self._start_image = start_image
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setStart_image argument is not XSDataInteger but %s" % start_image.__class__.__name__
            raise BaseException(strMessage)
    def delStart_image(self): self._start_image = None
    start_image = property(getStart_image, setStart_image, delStart_image, "Property for start_image")
    # Methods and properties for the 'end_image' attribute
    def getEnd_image(self): return self._end_image
    def setEnd_image(self, end_image):
        if end_image is None:
            self._end_image = None
        elif end_image.__class__.__name__ == "XSDataInteger":
            self._end_image = end_image
        else:
            strMessage = "ERROR! XSDataMinimalXdsIn.setEnd_image argument is not XSDataInteger but %s" % end_image.__class__.__name__
            raise BaseException(strMessage)
    def delEnd_image(self): self._end_image = None
    end_image = property(getEnd_image, setEnd_image, delEnd_image, "Property for end_image")
    def export(self, outfile, level, name_='XSDataMinimalXdsIn'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMinimalXdsIn'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._input_file is not None:
            self.input_file.export(outfile, level, name_='input_file')
        else:
            warnEmptyAttribute("input_file", "XSDataString")
        if self._job is not None:
            self.job.export(outfile, level, name_='job')
        if self._maxproc is not None:
            self.maxproc.export(outfile, level, name_='maxproc')
        if self._maxjobs is not None:
            self.maxjobs.export(outfile, level, name_='maxjobs')
        if self._friedels_law is not None:
            self.friedels_law.export(outfile, level, name_='friedels_law')
        for resolution_range_ in self.getResolution_range():
            resolution_range_.export(outfile, level, name_='resolution_range')
        for spot_range_ in self.getSpot_range():
            spot_range_.export(outfile, level, name_='spot_range')
        if self._spacegroup is not None:
            self.spacegroup.export(outfile, level, name_='spacegroup')
        if self._unit_cell is not None:
            self.unit_cell.export(outfile, level, name_='unit_cell')
        if self._start_image is not None:
            self.start_image.export(outfile, level, name_='start_image')
        if self._end_image is not None:
            self.end_image.export(outfile, level, name_='end_image')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'input_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setInput_file(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'job':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setJob(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maxproc':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setMaxproc(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maxjobs':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setMaxjobs(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'friedels_law':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setFriedels_law(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution_range':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.resolution_range.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spot_range':
            obj_ = XSDataRange()
            obj_.build(child_)
            self.spot_range.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spacegroup':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSpacegroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit_cell':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setUnit_cell(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'start_image':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setStart_image(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'end_image':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setEnd_image(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMinimalXdsIn" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMinimalXdsIn' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMinimalXdsIn is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMinimalXdsIn.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMinimalXdsIn()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMinimalXdsIn" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMinimalXdsIn()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMinimalXdsIn


class XSDataMinimalXdsOut(XSDataResult):
    def __init__(self, status=None, succeeded=None):
        XSDataResult.__init__(self, status)
        if succeeded is None:
            self._succeeded = None
        elif succeeded.__class__.__name__ == "XSDataBoolean":
            self._succeeded = succeeded
        else:
            strMessage = "ERROR! XSDataMinimalXdsOut constructor argument 'succeeded' is not XSDataBoolean but %s" % self._succeeded.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'succeeded' attribute
    def getSucceeded(self): return self._succeeded
    def setSucceeded(self, succeeded):
        if succeeded is None:
            self._succeeded = None
        elif succeeded.__class__.__name__ == "XSDataBoolean":
            self._succeeded = succeeded
        else:
            strMessage = "ERROR! XSDataMinimalXdsOut.setSucceeded argument is not XSDataBoolean but %s" % succeeded.__class__.__name__
            raise BaseException(strMessage)
    def delSucceeded(self): self._succeeded = None
    succeeded = property(getSucceeded, setSucceeded, delSucceeded, "Property for succeeded")
    def export(self, outfile, level, name_='XSDataMinimalXdsOut'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataMinimalXdsOut'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._succeeded is not None:
            self.succeeded.export(outfile, level, name_='succeeded')
        else:
            warnEmptyAttribute("succeeded", "XSDataBoolean")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'succeeded':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setSucceeded(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataMinimalXdsOut" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataMinimalXdsOut' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataMinimalXdsOut is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataMinimalXdsOut.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataMinimalXdsOut()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataMinimalXdsOut" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataMinimalXdsOut()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataMinimalXdsOut


class XSDataResCutoff(XSDataInput):
    def __init__(self, configuration=None, cc_half_cutoff=None, r_value_cutoff=None, isig_cutoff=None, completeness_cutoff=None, res_override=None, total_completeness=None, detector_max_res=None, completeness_entries=None, xds_res=None):
        XSDataInput.__init__(self, configuration)
        if xds_res is None:
            self._xds_res = None
        elif xds_res.__class__.__name__ == "XSDataXdsOutput":
            self._xds_res = xds_res
        else:
            strMessage = "ERROR! XSDataResCutoff constructor argument 'xds_res' is not XSDataXdsOutput but %s" % self._xds_res.__class__.__name__
            raise BaseException(strMessage)
        if completeness_entries is None:
            self._completeness_entries = []
        elif completeness_entries.__class__.__name__ == "list":
            self._completeness_entries = completeness_entries
        else:
            strMessage = "ERROR! XSDataResCutoff constructor argument 'completeness_entries' is not list but %s" % self._completeness_entries.__class__.__name__
            raise BaseException(strMessage)
        if detector_max_res is None:
            self._detector_max_res = None
        elif detector_max_res.__class__.__name__ == "XSDataDouble":
            self._detector_max_res = detector_max_res
        else:
            strMessage = "ERROR! XSDataResCutoff constructor argument 'detector_max_res' is not XSDataDouble but %s" % self._detector_max_res.__class__.__name__
            raise BaseException(strMessage)
        if total_completeness is None:
            self._total_completeness = None
        elif total_completeness.__class__.__name__ == "XSDataXdsCompletenessEntry":
            self._total_completeness = total_completeness
        else:
            strMessage = "ERROR! XSDataResCutoff constructor argument 'total_completeness' is not XSDataXdsCompletenessEntry but %s" % self._total_completeness.__class__.__name__
            raise BaseException(strMessage)
        if res_override is None:
            self._res_override = None
        elif res_override.__class__.__name__ == "XSDataDouble":
            self._res_override = res_override
        else:
            strMessage = "ERROR! XSDataResCutoff constructor argument 'res_override' is not XSDataDouble but %s" % self._res_override.__class__.__name__
            raise BaseException(strMessage)
        if completeness_cutoff is None:
            self._completeness_cutoff = None
        elif completeness_cutoff.__class__.__name__ == "XSDataDouble":
            self._completeness_cutoff = completeness_cutoff
        else:
            strMessage = "ERROR! XSDataResCutoff constructor argument 'completeness_cutoff' is not XSDataDouble but %s" % self._completeness_cutoff.__class__.__name__
            raise BaseException(strMessage)
        if isig_cutoff is None:
            self._isig_cutoff = None
        elif isig_cutoff.__class__.__name__ == "XSDataDouble":
            self._isig_cutoff = isig_cutoff
        else:
            strMessage = "ERROR! XSDataResCutoff constructor argument 'isig_cutoff' is not XSDataDouble but %s" % self._isig_cutoff.__class__.__name__
            raise BaseException(strMessage)
        if r_value_cutoff is None:
            self._r_value_cutoff = None
        elif r_value_cutoff.__class__.__name__ == "XSDataDouble":
            self._r_value_cutoff = r_value_cutoff
        else:
            strMessage = "ERROR! XSDataResCutoff constructor argument 'r_value_cutoff' is not XSDataDouble but %s" % self._r_value_cutoff.__class__.__name__
            raise BaseException(strMessage)
        if cc_half_cutoff is None:
            self._cc_half_cutoff = None
        elif cc_half_cutoff.__class__.__name__ == "XSDataDouble":
            self._cc_half_cutoff = cc_half_cutoff
        else:
            strMessage = "ERROR! XSDataResCutoff constructor argument 'cc_half_cutoff' is not XSDataDouble but %s" % self._cc_half_cutoff.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'xds_res' attribute
    def getXds_res(self): return self._xds_res
    def setXds_res(self, xds_res):
        if xds_res is None:
            self._xds_res = None
        elif xds_res.__class__.__name__ == "XSDataXdsOutput":
            self._xds_res = xds_res
        else:
            strMessage = "ERROR! XSDataResCutoff.setXds_res argument is not XSDataXdsOutput but %s" % xds_res.__class__.__name__
            raise BaseException(strMessage)
    def delXds_res(self): self._xds_res = None
    xds_res = property(getXds_res, setXds_res, delXds_res, "Property for xds_res")
    # Methods and properties for the 'completeness_entries' attribute
    def getCompleteness_entries(self): return self._completeness_entries
    def setCompleteness_entries(self, completeness_entries):
        if completeness_entries is None:
            self._completeness_entries = []
        elif completeness_entries.__class__.__name__ == "list":
            self._completeness_entries = completeness_entries
        else:
            strMessage = "ERROR! XSDataResCutoff.setCompleteness_entries argument is not list but %s" % completeness_entries.__class__.__name__
            raise BaseException(strMessage)
    def delCompleteness_entries(self): self._completeness_entries = None
    completeness_entries = property(getCompleteness_entries, setCompleteness_entries, delCompleteness_entries, "Property for completeness_entries")
    def addCompleteness_entries(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResCutoff.addCompleteness_entries argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXdsCompletenessEntry":
            self._completeness_entries.append(value)
        else:
            strMessage = "ERROR! XSDataResCutoff.addCompleteness_entries argument is not XSDataXdsCompletenessEntry but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertCompleteness_entries(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResCutoff.insertCompleteness_entries argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResCutoff.insertCompleteness_entries argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXdsCompletenessEntry":
            self._completeness_entries[index] = value
        else:
            strMessage = "ERROR! XSDataResCutoff.addCompleteness_entries argument is not XSDataXdsCompletenessEntry but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'detector_max_res' attribute
    def getDetector_max_res(self): return self._detector_max_res
    def setDetector_max_res(self, detector_max_res):
        if detector_max_res is None:
            self._detector_max_res = None
        elif detector_max_res.__class__.__name__ == "XSDataDouble":
            self._detector_max_res = detector_max_res
        else:
            strMessage = "ERROR! XSDataResCutoff.setDetector_max_res argument is not XSDataDouble but %s" % detector_max_res.__class__.__name__
            raise BaseException(strMessage)
    def delDetector_max_res(self): self._detector_max_res = None
    detector_max_res = property(getDetector_max_res, setDetector_max_res, delDetector_max_res, "Property for detector_max_res")
    # Methods and properties for the 'total_completeness' attribute
    def getTotal_completeness(self): return self._total_completeness
    def setTotal_completeness(self, total_completeness):
        if total_completeness is None:
            self._total_completeness = None
        elif total_completeness.__class__.__name__ == "XSDataXdsCompletenessEntry":
            self._total_completeness = total_completeness
        else:
            strMessage = "ERROR! XSDataResCutoff.setTotal_completeness argument is not XSDataXdsCompletenessEntry but %s" % total_completeness.__class__.__name__
            raise BaseException(strMessage)
    def delTotal_completeness(self): self._total_completeness = None
    total_completeness = property(getTotal_completeness, setTotal_completeness, delTotal_completeness, "Property for total_completeness")
    # Methods and properties for the 'res_override' attribute
    def getRes_override(self): return self._res_override
    def setRes_override(self, res_override):
        if res_override is None:
            self._res_override = None
        elif res_override.__class__.__name__ == "XSDataDouble":
            self._res_override = res_override
        else:
            strMessage = "ERROR! XSDataResCutoff.setRes_override argument is not XSDataDouble but %s" % res_override.__class__.__name__
            raise BaseException(strMessage)
    def delRes_override(self): self._res_override = None
    res_override = property(getRes_override, setRes_override, delRes_override, "Property for res_override")
    # Methods and properties for the 'completeness_cutoff' attribute
    def getCompleteness_cutoff(self): return self._completeness_cutoff
    def setCompleteness_cutoff(self, completeness_cutoff):
        if completeness_cutoff is None:
            self._completeness_cutoff = None
        elif completeness_cutoff.__class__.__name__ == "XSDataDouble":
            self._completeness_cutoff = completeness_cutoff
        else:
            strMessage = "ERROR! XSDataResCutoff.setCompleteness_cutoff argument is not XSDataDouble but %s" % completeness_cutoff.__class__.__name__
            raise BaseException(strMessage)
    def delCompleteness_cutoff(self): self._completeness_cutoff = None
    completeness_cutoff = property(getCompleteness_cutoff, setCompleteness_cutoff, delCompleteness_cutoff, "Property for completeness_cutoff")
    # Methods and properties for the 'isig_cutoff' attribute
    def getIsig_cutoff(self): return self._isig_cutoff
    def setIsig_cutoff(self, isig_cutoff):
        if isig_cutoff is None:
            self._isig_cutoff = None
        elif isig_cutoff.__class__.__name__ == "XSDataDouble":
            self._isig_cutoff = isig_cutoff
        else:
            strMessage = "ERROR! XSDataResCutoff.setIsig_cutoff argument is not XSDataDouble but %s" % isig_cutoff.__class__.__name__
            raise BaseException(strMessage)
    def delIsig_cutoff(self): self._isig_cutoff = None
    isig_cutoff = property(getIsig_cutoff, setIsig_cutoff, delIsig_cutoff, "Property for isig_cutoff")
    # Methods and properties for the 'r_value_cutoff' attribute
    def getR_value_cutoff(self): return self._r_value_cutoff
    def setR_value_cutoff(self, r_value_cutoff):
        if r_value_cutoff is None:
            self._r_value_cutoff = None
        elif r_value_cutoff.__class__.__name__ == "XSDataDouble":
            self._r_value_cutoff = r_value_cutoff
        else:
            strMessage = "ERROR! XSDataResCutoff.setR_value_cutoff argument is not XSDataDouble but %s" % r_value_cutoff.__class__.__name__
            raise BaseException(strMessage)
    def delR_value_cutoff(self): self._r_value_cutoff = None
    r_value_cutoff = property(getR_value_cutoff, setR_value_cutoff, delR_value_cutoff, "Property for r_value_cutoff")
    # Methods and properties for the 'cc_half_cutoff' attribute
    def getCc_half_cutoff(self): return self._cc_half_cutoff
    def setCc_half_cutoff(self, cc_half_cutoff):
        if cc_half_cutoff is None:
            self._cc_half_cutoff = None
        elif cc_half_cutoff.__class__.__name__ == "XSDataDouble":
            self._cc_half_cutoff = cc_half_cutoff
        else:
            strMessage = "ERROR! XSDataResCutoff.setCc_half_cutoff argument is not XSDataDouble but %s" % cc_half_cutoff.__class__.__name__
            raise BaseException(strMessage)
    def delCc_half_cutoff(self): self._cc_half_cutoff = None
    cc_half_cutoff = property(getCc_half_cutoff, setCc_half_cutoff, delCc_half_cutoff, "Property for cc_half_cutoff")
    def export(self, outfile, level, name_='XSDataResCutoff'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResCutoff'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._xds_res is not None:
            self.xds_res.export(outfile, level, name_='xds_res')
        else:
            warnEmptyAttribute("xds_res", "XSDataXdsOutput")
        for completeness_entries_ in self.getCompleteness_entries():
            completeness_entries_.export(outfile, level, name_='completeness_entries')
        if self.getCompleteness_entries() == []:
            warnEmptyAttribute("completeness_entries", "XSDataXdsCompletenessEntry")
        if self._detector_max_res is not None:
            self.detector_max_res.export(outfile, level, name_='detector_max_res')
        if self._total_completeness is not None:
            self.total_completeness.export(outfile, level, name_='total_completeness')
        else:
            warnEmptyAttribute("total_completeness", "XSDataXdsCompletenessEntry")
        if self._res_override is not None:
            self.res_override.export(outfile, level, name_='res_override')
        if self._completeness_cutoff is not None:
            self.completeness_cutoff.export(outfile, level, name_='completeness_cutoff')
        if self._isig_cutoff is not None:
            self.isig_cutoff.export(outfile, level, name_='isig_cutoff')
        if self._r_value_cutoff is not None:
            self.r_value_cutoff.export(outfile, level, name_='r_value_cutoff')
        if self._cc_half_cutoff is not None:
            self.cc_half_cutoff.export(outfile, level, name_='cc_half_cutoff')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xds_res':
            obj_ = XSDataXdsOutput()
            obj_.build(child_)
            self.setXds_res(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness_entries':
            obj_ = XSDataXdsCompletenessEntry()
            obj_.build(child_)
            self.completeness_entries.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detector_max_res':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDetector_max_res(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'total_completeness':
            obj_ = XSDataXdsCompletenessEntry()
            obj_.build(child_)
            self.setTotal_completeness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'res_override':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRes_override(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness_cutoff':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCompleteness_cutoff(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'isig_cutoff':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setIsig_cutoff(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'r_value_cutoff':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setR_value_cutoff(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cc_half_cutoff':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCc_half_cutoff(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResCutoff" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResCutoff' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResCutoff is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResCutoff.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResCutoff()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResCutoff" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResCutoff()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResCutoff


class XSDataResCutoffResult(XSDataResult):
    def __init__(self, status=None, total_isig=None, total_rfactor=None, total_complete=None, bins=None, res=None):
        XSDataResult.__init__(self, status)
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataDouble":
            self._res = res
        else:
            strMessage = "ERROR! XSDataResCutoffResult constructor argument 'res' is not XSDataDouble but %s" % self._res.__class__.__name__
            raise BaseException(strMessage)
        if bins is None:
            self._bins = []
        elif bins.__class__.__name__ == "list":
            self._bins = bins
        else:
            strMessage = "ERROR! XSDataResCutoffResult constructor argument 'bins' is not list but %s" % self._bins.__class__.__name__
            raise BaseException(strMessage)
        if total_complete is None:
            self._total_complete = None
        elif total_complete.__class__.__name__ == "XSDataDouble":
            self._total_complete = total_complete
        else:
            strMessage = "ERROR! XSDataResCutoffResult constructor argument 'total_complete' is not XSDataDouble but %s" % self._total_complete.__class__.__name__
            raise BaseException(strMessage)
        if total_rfactor is None:
            self._total_rfactor = None
        elif total_rfactor.__class__.__name__ == "XSDataDouble":
            self._total_rfactor = total_rfactor
        else:
            strMessage = "ERROR! XSDataResCutoffResult constructor argument 'total_rfactor' is not XSDataDouble but %s" % self._total_rfactor.__class__.__name__
            raise BaseException(strMessage)
        if total_isig is None:
            self._total_isig = None
        elif total_isig.__class__.__name__ == "XSDataDouble":
            self._total_isig = total_isig
        else:
            strMessage = "ERROR! XSDataResCutoffResult constructor argument 'total_isig' is not XSDataDouble but %s" % self._total_isig.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'res' attribute
    def getRes(self): return self._res
    def setRes(self, res):
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataDouble":
            self._res = res
        else:
            strMessage = "ERROR! XSDataResCutoffResult.setRes argument is not XSDataDouble but %s" % res.__class__.__name__
            raise BaseException(strMessage)
    def delRes(self): self._res = None
    res = property(getRes, setRes, delRes, "Property for res")
    # Methods and properties for the 'bins' attribute
    def getBins(self): return self._bins
    def setBins(self, bins):
        if bins is None:
            self._bins = []
        elif bins.__class__.__name__ == "list":
            self._bins = bins
        else:
            strMessage = "ERROR! XSDataResCutoffResult.setBins argument is not list but %s" % bins.__class__.__name__
            raise BaseException(strMessage)
    def delBins(self): self._bins = None
    bins = property(getBins, setBins, delBins, "Property for bins")
    def addBins(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResCutoffResult.addBins argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._bins.append(value)
        else:
            strMessage = "ERROR! XSDataResCutoffResult.addBins argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertBins(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResCutoffResult.insertBins argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResCutoffResult.insertBins argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._bins[index] = value
        else:
            strMessage = "ERROR! XSDataResCutoffResult.addBins argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'total_complete' attribute
    def getTotal_complete(self): return self._total_complete
    def setTotal_complete(self, total_complete):
        if total_complete is None:
            self._total_complete = None
        elif total_complete.__class__.__name__ == "XSDataDouble":
            self._total_complete = total_complete
        else:
            strMessage = "ERROR! XSDataResCutoffResult.setTotal_complete argument is not XSDataDouble but %s" % total_complete.__class__.__name__
            raise BaseException(strMessage)
    def delTotal_complete(self): self._total_complete = None
    total_complete = property(getTotal_complete, setTotal_complete, delTotal_complete, "Property for total_complete")
    # Methods and properties for the 'total_rfactor' attribute
    def getTotal_rfactor(self): return self._total_rfactor
    def setTotal_rfactor(self, total_rfactor):
        if total_rfactor is None:
            self._total_rfactor = None
        elif total_rfactor.__class__.__name__ == "XSDataDouble":
            self._total_rfactor = total_rfactor
        else:
            strMessage = "ERROR! XSDataResCutoffResult.setTotal_rfactor argument is not XSDataDouble but %s" % total_rfactor.__class__.__name__
            raise BaseException(strMessage)
    def delTotal_rfactor(self): self._total_rfactor = None
    total_rfactor = property(getTotal_rfactor, setTotal_rfactor, delTotal_rfactor, "Property for total_rfactor")
    # Methods and properties for the 'total_isig' attribute
    def getTotal_isig(self): return self._total_isig
    def setTotal_isig(self, total_isig):
        if total_isig is None:
            self._total_isig = None
        elif total_isig.__class__.__name__ == "XSDataDouble":
            self._total_isig = total_isig
        else:
            strMessage = "ERROR! XSDataResCutoffResult.setTotal_isig argument is not XSDataDouble but %s" % total_isig.__class__.__name__
            raise BaseException(strMessage)
    def delTotal_isig(self): self._total_isig = None
    total_isig = property(getTotal_isig, setTotal_isig, delTotal_isig, "Property for total_isig")
    def export(self, outfile, level, name_='XSDataResCutoffResult'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResCutoffResult'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._res is not None:
            self.res.export(outfile, level, name_='res')
        else:
            warnEmptyAttribute("res", "XSDataDouble")
        for bins_ in self.getBins():
            bins_.export(outfile, level, name_='bins')
        if self.getBins() == []:
            warnEmptyAttribute("bins", "XSDataDouble")
        if self._total_complete is not None:
            self.total_complete.export(outfile, level, name_='total_complete')
        else:
            warnEmptyAttribute("total_complete", "XSDataDouble")
        if self._total_rfactor is not None:
            self.total_rfactor.export(outfile, level, name_='total_rfactor')
        else:
            warnEmptyAttribute("total_rfactor", "XSDataDouble")
        if self._total_isig is not None:
            self.total_isig.export(outfile, level, name_='total_isig')
        else:
            warnEmptyAttribute("total_isig", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'res':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRes(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bins':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.bins.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'total_complete':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTotal_complete(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'total_rfactor':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTotal_rfactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'total_isig':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTotal_isig(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResCutoffResult" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResCutoffResult' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResCutoffResult is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResCutoffResult.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResCutoffResult()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResCutoffResult" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResCutoffResult()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResCutoffResult


class XSDataResultXDS(XSDataResult):
    def __init__(self, status=None, filePaths=None):
        XSDataResult.__init__(self, status)
        if filePaths is None:
            self._filePaths = None
        elif filePaths.__class__.__name__ == "XSDataXDSFilePaths":
            self._filePaths = filePaths
        else:
            strMessage = "ERROR! XSDataResultXDS constructor argument 'filePaths' is not XSDataXDSFilePaths but %s" % self._filePaths.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'filePaths' attribute
    def getFilePaths(self): return self._filePaths
    def setFilePaths(self, filePaths):
        if filePaths is None:
            self._filePaths = None
        elif filePaths.__class__.__name__ == "XSDataXDSFilePaths":
            self._filePaths = filePaths
        else:
            strMessage = "ERROR! XSDataResultXDS.setFilePaths argument is not XSDataXDSFilePaths but %s" % filePaths.__class__.__name__
            raise BaseException(strMessage)
    def delFilePaths(self): self._filePaths = None
    filePaths = property(getFilePaths, setFilePaths, delFilePaths, "Property for filePaths")
    def export(self, outfile, level, name_='XSDataResultXDS'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultXDS'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._filePaths is not None:
            self.filePaths.export(outfile, level, name_='filePaths')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'filePaths':
            obj_ = XSDataXDSFilePaths()
            obj_.build(child_)
            self.setFilePaths(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultXDS" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultXDS' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultXDS is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultXDS.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultXDS()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultXDS" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultXDS()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultXDS


class XSDataXdsGenerateInput(XSDataInput):
    def __init__(self, configuration=None, doNoanom=None, doAnom=None, unit_cell=None, spacegroup=None, resolution=None, previous_run_dir=None):
        XSDataInput.__init__(self, configuration)
        if previous_run_dir is None:
            self._previous_run_dir = None
        elif previous_run_dir.__class__.__name__ == "XSDataString":
            self._previous_run_dir = previous_run_dir
        else:
            strMessage = "ERROR! XSDataXdsGenerateInput constructor argument 'previous_run_dir' is not XSDataString but %s" % self._previous_run_dir.__class__.__name__
            raise BaseException(strMessage)
        if resolution is None:
            self._resolution = None
        elif resolution.__class__.__name__ == "XSDataDouble":
            self._resolution = resolution
        else:
            strMessage = "ERROR! XSDataXdsGenerateInput constructor argument 'resolution' is not XSDataDouble but %s" % self._resolution.__class__.__name__
            raise BaseException(strMessage)
        if spacegroup is None:
            self._spacegroup = None
        elif spacegroup.__class__.__name__ == "XSDataInteger":
            self._spacegroup = spacegroup
        else:
            strMessage = "ERROR! XSDataXdsGenerateInput constructor argument 'spacegroup' is not XSDataInteger but %s" % self._spacegroup.__class__.__name__
            raise BaseException(strMessage)
        if unit_cell is None:
            self._unit_cell = None
        elif unit_cell.__class__.__name__ == "XSDataString":
            self._unit_cell = unit_cell
        else:
            strMessage = "ERROR! XSDataXdsGenerateInput constructor argument 'unit_cell' is not XSDataString but %s" % self._unit_cell.__class__.__name__
            raise BaseException(strMessage)
        if doAnom is None:
            self._doAnom = None
        elif doAnom.__class__.__name__ == "XSDataBoolean":
            self._doAnom = doAnom
        else:
            strMessage = "ERROR! XSDataXdsGenerateInput constructor argument 'doAnom' is not XSDataBoolean but %s" % self._doAnom.__class__.__name__
            raise BaseException(strMessage)
        if doNoanom is None:
            self._doNoanom = None
        elif doNoanom.__class__.__name__ == "XSDataBoolean":
            self._doNoanom = doNoanom
        else:
            strMessage = "ERROR! XSDataXdsGenerateInput constructor argument 'doNoanom' is not XSDataBoolean but %s" % self._doNoanom.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'previous_run_dir' attribute
    def getPrevious_run_dir(self): return self._previous_run_dir
    def setPrevious_run_dir(self, previous_run_dir):
        if previous_run_dir is None:
            self._previous_run_dir = None
        elif previous_run_dir.__class__.__name__ == "XSDataString":
            self._previous_run_dir = previous_run_dir
        else:
            strMessage = "ERROR! XSDataXdsGenerateInput.setPrevious_run_dir argument is not XSDataString but %s" % previous_run_dir.__class__.__name__
            raise BaseException(strMessage)
    def delPrevious_run_dir(self): self._previous_run_dir = None
    previous_run_dir = property(getPrevious_run_dir, setPrevious_run_dir, delPrevious_run_dir, "Property for previous_run_dir")
    # Methods and properties for the 'resolution' attribute
    def getResolution(self): return self._resolution
    def setResolution(self, resolution):
        if resolution is None:
            self._resolution = None
        elif resolution.__class__.__name__ == "XSDataDouble":
            self._resolution = resolution
        else:
            strMessage = "ERROR! XSDataXdsGenerateInput.setResolution argument is not XSDataDouble but %s" % resolution.__class__.__name__
            raise BaseException(strMessage)
    def delResolution(self): self._resolution = None
    resolution = property(getResolution, setResolution, delResolution, "Property for resolution")
    # Methods and properties for the 'spacegroup' attribute
    def getSpacegroup(self): return self._spacegroup
    def setSpacegroup(self, spacegroup):
        if spacegroup is None:
            self._spacegroup = None
        elif spacegroup.__class__.__name__ == "XSDataInteger":
            self._spacegroup = spacegroup
        else:
            strMessage = "ERROR! XSDataXdsGenerateInput.setSpacegroup argument is not XSDataInteger but %s" % spacegroup.__class__.__name__
            raise BaseException(strMessage)
    def delSpacegroup(self): self._spacegroup = None
    spacegroup = property(getSpacegroup, setSpacegroup, delSpacegroup, "Property for spacegroup")
    # Methods and properties for the 'unit_cell' attribute
    def getUnit_cell(self): return self._unit_cell
    def setUnit_cell(self, unit_cell):
        if unit_cell is None:
            self._unit_cell = None
        elif unit_cell.__class__.__name__ == "XSDataString":
            self._unit_cell = unit_cell
        else:
            strMessage = "ERROR! XSDataXdsGenerateInput.setUnit_cell argument is not XSDataString but %s" % unit_cell.__class__.__name__
            raise BaseException(strMessage)
    def delUnit_cell(self): self._unit_cell = None
    unit_cell = property(getUnit_cell, setUnit_cell, delUnit_cell, "Property for unit_cell")
    # Methods and properties for the 'doAnom' attribute
    def getDoAnom(self): return self._doAnom
    def setDoAnom(self, doAnom):
        if doAnom is None:
            self._doAnom = None
        elif doAnom.__class__.__name__ == "XSDataBoolean":
            self._doAnom = doAnom
        else:
            strMessage = "ERROR! XSDataXdsGenerateInput.setDoAnom argument is not XSDataBoolean but %s" % doAnom.__class__.__name__
            raise BaseException(strMessage)
    def delDoAnom(self): self._doAnom = None
    doAnom = property(getDoAnom, setDoAnom, delDoAnom, "Property for doAnom")
    # Methods and properties for the 'doNoanom' attribute
    def getDoNoanom(self): return self._doNoanom
    def setDoNoanom(self, doNoanom):
        if doNoanom is None:
            self._doNoanom = None
        elif doNoanom.__class__.__name__ == "XSDataBoolean":
            self._doNoanom = doNoanom
        else:
            strMessage = "ERROR! XSDataXdsGenerateInput.setDoNoanom argument is not XSDataBoolean but %s" % doNoanom.__class__.__name__
            raise BaseException(strMessage)
    def delDoNoanom(self): self._doNoanom = None
    doNoanom = property(getDoNoanom, setDoNoanom, delDoNoanom, "Property for doNoanom")
    def export(self, outfile, level, name_='XSDataXdsGenerateInput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXdsGenerateInput'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._previous_run_dir is not None:
            self.previous_run_dir.export(outfile, level, name_='previous_run_dir')
        else:
            warnEmptyAttribute("previous_run_dir", "XSDataString")
        if self._resolution is not None:
            self.resolution.export(outfile, level, name_='resolution')
        else:
            warnEmptyAttribute("resolution", "XSDataDouble")
        if self._spacegroup is not None:
            self.spacegroup.export(outfile, level, name_='spacegroup')
        if self._unit_cell is not None:
            self.unit_cell.export(outfile, level, name_='unit_cell')
        if self._doAnom is not None:
            self.doAnom.export(outfile, level, name_='doAnom')
        if self._doNoanom is not None:
            self.doNoanom.export(outfile, level, name_='doNoanom')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'previous_run_dir':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setPrevious_run_dir(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolution':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setResolution(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spacegroup':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSpacegroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit_cell':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setUnit_cell(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'doAnom':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setDoAnom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'doNoanom':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setDoNoanom(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXdsGenerateInput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXdsGenerateInput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXdsGenerateInput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXdsGenerateInput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXdsGenerateInput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXdsGenerateInput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXdsGenerateInput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXdsGenerateInput


class XSDataXdsGenerateOutput(XSDataResult):
    def __init__(self, status=None, gxparm=None, integrate_noanom=None, integrate_anom=None, correct_lp_no_anom=None, correct_lp_anom=None, hkl_no_anom=None, hkl_anom=None):
        XSDataResult.__init__(self, status)
        if hkl_anom is None:
            self._hkl_anom = None
        elif hkl_anom.__class__.__name__ == "XSDataString":
            self._hkl_anom = hkl_anom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput constructor argument 'hkl_anom' is not XSDataString but %s" % self._hkl_anom.__class__.__name__
            raise BaseException(strMessage)
        if hkl_no_anom is None:
            self._hkl_no_anom = None
        elif hkl_no_anom.__class__.__name__ == "XSDataString":
            self._hkl_no_anom = hkl_no_anom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput constructor argument 'hkl_no_anom' is not XSDataString but %s" % self._hkl_no_anom.__class__.__name__
            raise BaseException(strMessage)
        if correct_lp_anom is None:
            self._correct_lp_anom = None
        elif correct_lp_anom.__class__.__name__ == "XSDataString":
            self._correct_lp_anom = correct_lp_anom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput constructor argument 'correct_lp_anom' is not XSDataString but %s" % self._correct_lp_anom.__class__.__name__
            raise BaseException(strMessage)
        if correct_lp_no_anom is None:
            self._correct_lp_no_anom = None
        elif correct_lp_no_anom.__class__.__name__ == "XSDataString":
            self._correct_lp_no_anom = correct_lp_no_anom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput constructor argument 'correct_lp_no_anom' is not XSDataString but %s" % self._correct_lp_no_anom.__class__.__name__
            raise BaseException(strMessage)
        if integrate_anom is None:
            self._integrate_anom = None
        elif integrate_anom.__class__.__name__ == "XSDataString":
            self._integrate_anom = integrate_anom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput constructor argument 'integrate_anom' is not XSDataString but %s" % self._integrate_anom.__class__.__name__
            raise BaseException(strMessage)
        if integrate_noanom is None:
            self._integrate_noanom = None
        elif integrate_noanom.__class__.__name__ == "XSDataString":
            self._integrate_noanom = integrate_noanom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput constructor argument 'integrate_noanom' is not XSDataString but %s" % self._integrate_noanom.__class__.__name__
            raise BaseException(strMessage)
        if gxparm is None:
            self._gxparm = None
        elif gxparm.__class__.__name__ == "XSDataString":
            self._gxparm = gxparm
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput constructor argument 'gxparm' is not XSDataString but %s" % self._gxparm.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'hkl_anom' attribute
    def getHkl_anom(self): return self._hkl_anom
    def setHkl_anom(self, hkl_anom):
        if hkl_anom is None:
            self._hkl_anom = None
        elif hkl_anom.__class__.__name__ == "XSDataString":
            self._hkl_anom = hkl_anom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput.setHkl_anom argument is not XSDataString but %s" % hkl_anom.__class__.__name__
            raise BaseException(strMessage)
    def delHkl_anom(self): self._hkl_anom = None
    hkl_anom = property(getHkl_anom, setHkl_anom, delHkl_anom, "Property for hkl_anom")
    # Methods and properties for the 'hkl_no_anom' attribute
    def getHkl_no_anom(self): return self._hkl_no_anom
    def setHkl_no_anom(self, hkl_no_anom):
        if hkl_no_anom is None:
            self._hkl_no_anom = None
        elif hkl_no_anom.__class__.__name__ == "XSDataString":
            self._hkl_no_anom = hkl_no_anom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput.setHkl_no_anom argument is not XSDataString but %s" % hkl_no_anom.__class__.__name__
            raise BaseException(strMessage)
    def delHkl_no_anom(self): self._hkl_no_anom = None
    hkl_no_anom = property(getHkl_no_anom, setHkl_no_anom, delHkl_no_anom, "Property for hkl_no_anom")
    # Methods and properties for the 'correct_lp_anom' attribute
    def getCorrect_lp_anom(self): return self._correct_lp_anom
    def setCorrect_lp_anom(self, correct_lp_anom):
        if correct_lp_anom is None:
            self._correct_lp_anom = None
        elif correct_lp_anom.__class__.__name__ == "XSDataString":
            self._correct_lp_anom = correct_lp_anom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput.setCorrect_lp_anom argument is not XSDataString but %s" % correct_lp_anom.__class__.__name__
            raise BaseException(strMessage)
    def delCorrect_lp_anom(self): self._correct_lp_anom = None
    correct_lp_anom = property(getCorrect_lp_anom, setCorrect_lp_anom, delCorrect_lp_anom, "Property for correct_lp_anom")
    # Methods and properties for the 'correct_lp_no_anom' attribute
    def getCorrect_lp_no_anom(self): return self._correct_lp_no_anom
    def setCorrect_lp_no_anom(self, correct_lp_no_anom):
        if correct_lp_no_anom is None:
            self._correct_lp_no_anom = None
        elif correct_lp_no_anom.__class__.__name__ == "XSDataString":
            self._correct_lp_no_anom = correct_lp_no_anom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput.setCorrect_lp_no_anom argument is not XSDataString but %s" % correct_lp_no_anom.__class__.__name__
            raise BaseException(strMessage)
    def delCorrect_lp_no_anom(self): self._correct_lp_no_anom = None
    correct_lp_no_anom = property(getCorrect_lp_no_anom, setCorrect_lp_no_anom, delCorrect_lp_no_anom, "Property for correct_lp_no_anom")
    # Methods and properties for the 'integrate_anom' attribute
    def getIntegrate_anom(self): return self._integrate_anom
    def setIntegrate_anom(self, integrate_anom):
        if integrate_anom is None:
            self._integrate_anom = None
        elif integrate_anom.__class__.__name__ == "XSDataString":
            self._integrate_anom = integrate_anom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput.setIntegrate_anom argument is not XSDataString but %s" % integrate_anom.__class__.__name__
            raise BaseException(strMessage)
    def delIntegrate_anom(self): self._integrate_anom = None
    integrate_anom = property(getIntegrate_anom, setIntegrate_anom, delIntegrate_anom, "Property for integrate_anom")
    # Methods and properties for the 'integrate_noanom' attribute
    def getIntegrate_noanom(self): return self._integrate_noanom
    def setIntegrate_noanom(self, integrate_noanom):
        if integrate_noanom is None:
            self._integrate_noanom = None
        elif integrate_noanom.__class__.__name__ == "XSDataString":
            self._integrate_noanom = integrate_noanom
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput.setIntegrate_noanom argument is not XSDataString but %s" % integrate_noanom.__class__.__name__
            raise BaseException(strMessage)
    def delIntegrate_noanom(self): self._integrate_noanom = None
    integrate_noanom = property(getIntegrate_noanom, setIntegrate_noanom, delIntegrate_noanom, "Property for integrate_noanom")
    # Methods and properties for the 'gxparm' attribute
    def getGxparm(self): return self._gxparm
    def setGxparm(self, gxparm):
        if gxparm is None:
            self._gxparm = None
        elif gxparm.__class__.__name__ == "XSDataString":
            self._gxparm = gxparm
        else:
            strMessage = "ERROR! XSDataXdsGenerateOutput.setGxparm argument is not XSDataString but %s" % gxparm.__class__.__name__
            raise BaseException(strMessage)
    def delGxparm(self): self._gxparm = None
    gxparm = property(getGxparm, setGxparm, delGxparm, "Property for gxparm")
    def export(self, outfile, level, name_='XSDataXdsGenerateOutput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXdsGenerateOutput'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._hkl_anom is not None:
            self.hkl_anom.export(outfile, level, name_='hkl_anom')
        else:
            warnEmptyAttribute("hkl_anom", "XSDataString")
        if self._hkl_no_anom is not None:
            self.hkl_no_anom.export(outfile, level, name_='hkl_no_anom')
        else:
            warnEmptyAttribute("hkl_no_anom", "XSDataString")
        if self._correct_lp_anom is not None:
            self.correct_lp_anom.export(outfile, level, name_='correct_lp_anom')
        else:
            warnEmptyAttribute("correct_lp_anom", "XSDataString")
        if self._correct_lp_no_anom is not None:
            self.correct_lp_no_anom.export(outfile, level, name_='correct_lp_no_anom')
        else:
            warnEmptyAttribute("correct_lp_no_anom", "XSDataString")
        if self._integrate_anom is not None:
            self.integrate_anom.export(outfile, level, name_='integrate_anom')
        else:
            warnEmptyAttribute("integrate_anom", "XSDataString")
        if self._integrate_noanom is not None:
            self.integrate_noanom.export(outfile, level, name_='integrate_noanom')
        else:
            warnEmptyAttribute("integrate_noanom", "XSDataString")
        if self._gxparm is not None:
            self.gxparm.export(outfile, level, name_='gxparm')
        else:
            warnEmptyAttribute("gxparm", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hkl_anom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setHkl_anom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hkl_no_anom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setHkl_no_anom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'correct_lp_anom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setCorrect_lp_anom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'correct_lp_no_anom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setCorrect_lp_no_anom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'integrate_anom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setIntegrate_anom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'integrate_noanom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setIntegrate_noanom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gxparm':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setGxparm(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXdsGenerateOutput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXdsGenerateOutput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXdsGenerateOutput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXdsGenerateOutput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXdsGenerateOutput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXdsGenerateOutput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXdsGenerateOutput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXdsGenerateOutput


class XSDataXdsOutput(XSDataResult):
    def __init__(self, status=None, xds_run_directory=None, sg_number=None, unit_cell_constants=None, cell_gamma=None, cell_beta=None, cell_alpha=None, cell_c=None, cell_b=None, cell_a=None, coordinates_of_unit_cell_c_axis=None, coordinates_of_unit_cell_b_axis=None, coordinates_of_unit_cell_a_axis=None, crystal_to_detector_distance=None, detector_origin=None, direct_beam_detector_coordinates=None, direct_beam_coordinates=None, crystal_mosaicity=None, total_completeness=None, completeness_entries=None):
        XSDataResult.__init__(self, status)
        if completeness_entries is None:
            self._completeness_entries = []
        elif completeness_entries.__class__.__name__ == "list":
            self._completeness_entries = completeness_entries
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'completeness_entries' is not list but %s" % self._completeness_entries.__class__.__name__
            raise BaseException(strMessage)
        if total_completeness is None:
            self._total_completeness = None
        elif total_completeness.__class__.__name__ == "XSDataXdsCompletenessEntry":
            self._total_completeness = total_completeness
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'total_completeness' is not XSDataXdsCompletenessEntry but %s" % self._total_completeness.__class__.__name__
            raise BaseException(strMessage)
        if crystal_mosaicity is None:
            self._crystal_mosaicity = None
        elif crystal_mosaicity.__class__.__name__ == "XSDataDouble":
            self._crystal_mosaicity = crystal_mosaicity
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'crystal_mosaicity' is not XSDataDouble but %s" % self._crystal_mosaicity.__class__.__name__
            raise BaseException(strMessage)
        if direct_beam_coordinates is None:
            self._direct_beam_coordinates = None
        elif direct_beam_coordinates.__class__.__name__ == "XSDataVectorDouble":
            self._direct_beam_coordinates = direct_beam_coordinates
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'direct_beam_coordinates' is not XSDataVectorDouble but %s" % self._direct_beam_coordinates.__class__.__name__
            raise BaseException(strMessage)
        if direct_beam_detector_coordinates is None:
            self._direct_beam_detector_coordinates = None
        elif direct_beam_detector_coordinates.__class__.__name__ == "XSData2DCoordinates":
            self._direct_beam_detector_coordinates = direct_beam_detector_coordinates
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'direct_beam_detector_coordinates' is not XSData2DCoordinates but %s" % self._direct_beam_detector_coordinates.__class__.__name__
            raise BaseException(strMessage)
        if detector_origin is None:
            self._detector_origin = None
        elif detector_origin.__class__.__name__ == "XSData2DCoordinates":
            self._detector_origin = detector_origin
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'detector_origin' is not XSData2DCoordinates but %s" % self._detector_origin.__class__.__name__
            raise BaseException(strMessage)
        if crystal_to_detector_distance is None:
            self._crystal_to_detector_distance = None
        elif crystal_to_detector_distance.__class__.__name__ == "XSDataDouble":
            self._crystal_to_detector_distance = crystal_to_detector_distance
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'crystal_to_detector_distance' is not XSDataDouble but %s" % self._crystal_to_detector_distance.__class__.__name__
            raise BaseException(strMessage)
        if coordinates_of_unit_cell_a_axis is None:
            self._coordinates_of_unit_cell_a_axis = None
        elif coordinates_of_unit_cell_a_axis.__class__.__name__ == "XSDataVectorDouble":
            self._coordinates_of_unit_cell_a_axis = coordinates_of_unit_cell_a_axis
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'coordinates_of_unit_cell_a_axis' is not XSDataVectorDouble but %s" % self._coordinates_of_unit_cell_a_axis.__class__.__name__
            raise BaseException(strMessage)
        if coordinates_of_unit_cell_b_axis is None:
            self._coordinates_of_unit_cell_b_axis = None
        elif coordinates_of_unit_cell_b_axis.__class__.__name__ == "XSDataVectorDouble":
            self._coordinates_of_unit_cell_b_axis = coordinates_of_unit_cell_b_axis
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'coordinates_of_unit_cell_b_axis' is not XSDataVectorDouble but %s" % self._coordinates_of_unit_cell_b_axis.__class__.__name__
            raise BaseException(strMessage)
        if coordinates_of_unit_cell_c_axis is None:
            self._coordinates_of_unit_cell_c_axis = None
        elif coordinates_of_unit_cell_c_axis.__class__.__name__ == "XSDataVectorDouble":
            self._coordinates_of_unit_cell_c_axis = coordinates_of_unit_cell_c_axis
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'coordinates_of_unit_cell_c_axis' is not XSDataVectorDouble but %s" % self._coordinates_of_unit_cell_c_axis.__class__.__name__
            raise BaseException(strMessage)
        if cell_a is None:
            self._cell_a = None
        elif cell_a.__class__.__name__ == "XSDataDouble":
            self._cell_a = cell_a
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'cell_a' is not XSDataDouble but %s" % self._cell_a.__class__.__name__
            raise BaseException(strMessage)
        if cell_b is None:
            self._cell_b = None
        elif cell_b.__class__.__name__ == "XSDataDouble":
            self._cell_b = cell_b
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'cell_b' is not XSDataDouble but %s" % self._cell_b.__class__.__name__
            raise BaseException(strMessage)
        if cell_c is None:
            self._cell_c = None
        elif cell_c.__class__.__name__ == "XSDataDouble":
            self._cell_c = cell_c
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'cell_c' is not XSDataDouble but %s" % self._cell_c.__class__.__name__
            raise BaseException(strMessage)
        if cell_alpha is None:
            self._cell_alpha = None
        elif cell_alpha.__class__.__name__ == "XSDataDouble":
            self._cell_alpha = cell_alpha
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'cell_alpha' is not XSDataDouble but %s" % self._cell_alpha.__class__.__name__
            raise BaseException(strMessage)
        if cell_beta is None:
            self._cell_beta = None
        elif cell_beta.__class__.__name__ == "XSDataDouble":
            self._cell_beta = cell_beta
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'cell_beta' is not XSDataDouble but %s" % self._cell_beta.__class__.__name__
            raise BaseException(strMessage)
        if cell_gamma is None:
            self._cell_gamma = None
        elif cell_gamma.__class__.__name__ == "XSDataDouble":
            self._cell_gamma = cell_gamma
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'cell_gamma' is not XSDataDouble but %s" % self._cell_gamma.__class__.__name__
            raise BaseException(strMessage)
        if unit_cell_constants is None:
            self._unit_cell_constants = []
        elif unit_cell_constants.__class__.__name__ == "list":
            self._unit_cell_constants = unit_cell_constants
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'unit_cell_constants' is not list but %s" % self._unit_cell_constants.__class__.__name__
            raise BaseException(strMessage)
        if sg_number is None:
            self._sg_number = None
        elif sg_number.__class__.__name__ == "XSDataInteger":
            self._sg_number = sg_number
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'sg_number' is not XSDataInteger but %s" % self._sg_number.__class__.__name__
            raise BaseException(strMessage)
        if xds_run_directory is None:
            self._xds_run_directory = None
        elif xds_run_directory.__class__.__name__ == "XSDataString":
            self._xds_run_directory = xds_run_directory
        else:
            strMessage = "ERROR! XSDataXdsOutput constructor argument 'xds_run_directory' is not XSDataString but %s" % self._xds_run_directory.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'completeness_entries' attribute
    def getCompleteness_entries(self): return self._completeness_entries
    def setCompleteness_entries(self, completeness_entries):
        if completeness_entries is None:
            self._completeness_entries = []
        elif completeness_entries.__class__.__name__ == "list":
            self._completeness_entries = completeness_entries
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCompleteness_entries argument is not list but %s" % completeness_entries.__class__.__name__
            raise BaseException(strMessage)
    def delCompleteness_entries(self): self._completeness_entries = None
    completeness_entries = property(getCompleteness_entries, setCompleteness_entries, delCompleteness_entries, "Property for completeness_entries")
    def addCompleteness_entries(self, value):
        if value is None:
            strMessage = "ERROR! XSDataXdsOutput.addCompleteness_entries argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXdsCompletenessEntry":
            self._completeness_entries.append(value)
        else:
            strMessage = "ERROR! XSDataXdsOutput.addCompleteness_entries argument is not XSDataXdsCompletenessEntry but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertCompleteness_entries(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataXdsOutput.insertCompleteness_entries argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataXdsOutput.insertCompleteness_entries argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXdsCompletenessEntry":
            self._completeness_entries[index] = value
        else:
            strMessage = "ERROR! XSDataXdsOutput.addCompleteness_entries argument is not XSDataXdsCompletenessEntry but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'total_completeness' attribute
    def getTotal_completeness(self): return self._total_completeness
    def setTotal_completeness(self, total_completeness):
        if total_completeness is None:
            self._total_completeness = None
        elif total_completeness.__class__.__name__ == "XSDataXdsCompletenessEntry":
            self._total_completeness = total_completeness
        else:
            strMessage = "ERROR! XSDataXdsOutput.setTotal_completeness argument is not XSDataXdsCompletenessEntry but %s" % total_completeness.__class__.__name__
            raise BaseException(strMessage)
    def delTotal_completeness(self): self._total_completeness = None
    total_completeness = property(getTotal_completeness, setTotal_completeness, delTotal_completeness, "Property for total_completeness")
    # Methods and properties for the 'crystal_mosaicity' attribute
    def getCrystal_mosaicity(self): return self._crystal_mosaicity
    def setCrystal_mosaicity(self, crystal_mosaicity):
        if crystal_mosaicity is None:
            self._crystal_mosaicity = None
        elif crystal_mosaicity.__class__.__name__ == "XSDataDouble":
            self._crystal_mosaicity = crystal_mosaicity
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCrystal_mosaicity argument is not XSDataDouble but %s" % crystal_mosaicity.__class__.__name__
            raise BaseException(strMessage)
    def delCrystal_mosaicity(self): self._crystal_mosaicity = None
    crystal_mosaicity = property(getCrystal_mosaicity, setCrystal_mosaicity, delCrystal_mosaicity, "Property for crystal_mosaicity")
    # Methods and properties for the 'direct_beam_coordinates' attribute
    def getDirect_beam_coordinates(self): return self._direct_beam_coordinates
    def setDirect_beam_coordinates(self, direct_beam_coordinates):
        if direct_beam_coordinates is None:
            self._direct_beam_coordinates = None
        elif direct_beam_coordinates.__class__.__name__ == "XSDataVectorDouble":
            self._direct_beam_coordinates = direct_beam_coordinates
        else:
            strMessage = "ERROR! XSDataXdsOutput.setDirect_beam_coordinates argument is not XSDataVectorDouble but %s" % direct_beam_coordinates.__class__.__name__
            raise BaseException(strMessage)
    def delDirect_beam_coordinates(self): self._direct_beam_coordinates = None
    direct_beam_coordinates = property(getDirect_beam_coordinates, setDirect_beam_coordinates, delDirect_beam_coordinates, "Property for direct_beam_coordinates")
    # Methods and properties for the 'direct_beam_detector_coordinates' attribute
    def getDirect_beam_detector_coordinates(self): return self._direct_beam_detector_coordinates
    def setDirect_beam_detector_coordinates(self, direct_beam_detector_coordinates):
        if direct_beam_detector_coordinates is None:
            self._direct_beam_detector_coordinates = None
        elif direct_beam_detector_coordinates.__class__.__name__ == "XSData2DCoordinates":
            self._direct_beam_detector_coordinates = direct_beam_detector_coordinates
        else:
            strMessage = "ERROR! XSDataXdsOutput.setDirect_beam_detector_coordinates argument is not XSData2DCoordinates but %s" % direct_beam_detector_coordinates.__class__.__name__
            raise BaseException(strMessage)
    def delDirect_beam_detector_coordinates(self): self._direct_beam_detector_coordinates = None
    direct_beam_detector_coordinates = property(getDirect_beam_detector_coordinates, setDirect_beam_detector_coordinates, delDirect_beam_detector_coordinates, "Property for direct_beam_detector_coordinates")
    # Methods and properties for the 'detector_origin' attribute
    def getDetector_origin(self): return self._detector_origin
    def setDetector_origin(self, detector_origin):
        if detector_origin is None:
            self._detector_origin = None
        elif detector_origin.__class__.__name__ == "XSData2DCoordinates":
            self._detector_origin = detector_origin
        else:
            strMessage = "ERROR! XSDataXdsOutput.setDetector_origin argument is not XSData2DCoordinates but %s" % detector_origin.__class__.__name__
            raise BaseException(strMessage)
    def delDetector_origin(self): self._detector_origin = None
    detector_origin = property(getDetector_origin, setDetector_origin, delDetector_origin, "Property for detector_origin")
    # Methods and properties for the 'crystal_to_detector_distance' attribute
    def getCrystal_to_detector_distance(self): return self._crystal_to_detector_distance
    def setCrystal_to_detector_distance(self, crystal_to_detector_distance):
        if crystal_to_detector_distance is None:
            self._crystal_to_detector_distance = None
        elif crystal_to_detector_distance.__class__.__name__ == "XSDataDouble":
            self._crystal_to_detector_distance = crystal_to_detector_distance
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCrystal_to_detector_distance argument is not XSDataDouble but %s" % crystal_to_detector_distance.__class__.__name__
            raise BaseException(strMessage)
    def delCrystal_to_detector_distance(self): self._crystal_to_detector_distance = None
    crystal_to_detector_distance = property(getCrystal_to_detector_distance, setCrystal_to_detector_distance, delCrystal_to_detector_distance, "Property for crystal_to_detector_distance")
    # Methods and properties for the 'coordinates_of_unit_cell_a_axis' attribute
    def getCoordinates_of_unit_cell_a_axis(self): return self._coordinates_of_unit_cell_a_axis
    def setCoordinates_of_unit_cell_a_axis(self, coordinates_of_unit_cell_a_axis):
        if coordinates_of_unit_cell_a_axis is None:
            self._coordinates_of_unit_cell_a_axis = None
        elif coordinates_of_unit_cell_a_axis.__class__.__name__ == "XSDataVectorDouble":
            self._coordinates_of_unit_cell_a_axis = coordinates_of_unit_cell_a_axis
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCoordinates_of_unit_cell_a_axis argument is not XSDataVectorDouble but %s" % coordinates_of_unit_cell_a_axis.__class__.__name__
            raise BaseException(strMessage)
    def delCoordinates_of_unit_cell_a_axis(self): self._coordinates_of_unit_cell_a_axis = None
    coordinates_of_unit_cell_a_axis = property(getCoordinates_of_unit_cell_a_axis, setCoordinates_of_unit_cell_a_axis, delCoordinates_of_unit_cell_a_axis, "Property for coordinates_of_unit_cell_a_axis")
    # Methods and properties for the 'coordinates_of_unit_cell_b_axis' attribute
    def getCoordinates_of_unit_cell_b_axis(self): return self._coordinates_of_unit_cell_b_axis
    def setCoordinates_of_unit_cell_b_axis(self, coordinates_of_unit_cell_b_axis):
        if coordinates_of_unit_cell_b_axis is None:
            self._coordinates_of_unit_cell_b_axis = None
        elif coordinates_of_unit_cell_b_axis.__class__.__name__ == "XSDataVectorDouble":
            self._coordinates_of_unit_cell_b_axis = coordinates_of_unit_cell_b_axis
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCoordinates_of_unit_cell_b_axis argument is not XSDataVectorDouble but %s" % coordinates_of_unit_cell_b_axis.__class__.__name__
            raise BaseException(strMessage)
    def delCoordinates_of_unit_cell_b_axis(self): self._coordinates_of_unit_cell_b_axis = None
    coordinates_of_unit_cell_b_axis = property(getCoordinates_of_unit_cell_b_axis, setCoordinates_of_unit_cell_b_axis, delCoordinates_of_unit_cell_b_axis, "Property for coordinates_of_unit_cell_b_axis")
    # Methods and properties for the 'coordinates_of_unit_cell_c_axis' attribute
    def getCoordinates_of_unit_cell_c_axis(self): return self._coordinates_of_unit_cell_c_axis
    def setCoordinates_of_unit_cell_c_axis(self, coordinates_of_unit_cell_c_axis):
        if coordinates_of_unit_cell_c_axis is None:
            self._coordinates_of_unit_cell_c_axis = None
        elif coordinates_of_unit_cell_c_axis.__class__.__name__ == "XSDataVectorDouble":
            self._coordinates_of_unit_cell_c_axis = coordinates_of_unit_cell_c_axis
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCoordinates_of_unit_cell_c_axis argument is not XSDataVectorDouble but %s" % coordinates_of_unit_cell_c_axis.__class__.__name__
            raise BaseException(strMessage)
    def delCoordinates_of_unit_cell_c_axis(self): self._coordinates_of_unit_cell_c_axis = None
    coordinates_of_unit_cell_c_axis = property(getCoordinates_of_unit_cell_c_axis, setCoordinates_of_unit_cell_c_axis, delCoordinates_of_unit_cell_c_axis, "Property for coordinates_of_unit_cell_c_axis")
    # Methods and properties for the 'cell_a' attribute
    def getCell_a(self): return self._cell_a
    def setCell_a(self, cell_a):
        if cell_a is None:
            self._cell_a = None
        elif cell_a.__class__.__name__ == "XSDataDouble":
            self._cell_a = cell_a
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCell_a argument is not XSDataDouble but %s" % cell_a.__class__.__name__
            raise BaseException(strMessage)
    def delCell_a(self): self._cell_a = None
    cell_a = property(getCell_a, setCell_a, delCell_a, "Property for cell_a")
    # Methods and properties for the 'cell_b' attribute
    def getCell_b(self): return self._cell_b
    def setCell_b(self, cell_b):
        if cell_b is None:
            self._cell_b = None
        elif cell_b.__class__.__name__ == "XSDataDouble":
            self._cell_b = cell_b
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCell_b argument is not XSDataDouble but %s" % cell_b.__class__.__name__
            raise BaseException(strMessage)
    def delCell_b(self): self._cell_b = None
    cell_b = property(getCell_b, setCell_b, delCell_b, "Property for cell_b")
    # Methods and properties for the 'cell_c' attribute
    def getCell_c(self): return self._cell_c
    def setCell_c(self, cell_c):
        if cell_c is None:
            self._cell_c = None
        elif cell_c.__class__.__name__ == "XSDataDouble":
            self._cell_c = cell_c
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCell_c argument is not XSDataDouble but %s" % cell_c.__class__.__name__
            raise BaseException(strMessage)
    def delCell_c(self): self._cell_c = None
    cell_c = property(getCell_c, setCell_c, delCell_c, "Property for cell_c")
    # Methods and properties for the 'cell_alpha' attribute
    def getCell_alpha(self): return self._cell_alpha
    def setCell_alpha(self, cell_alpha):
        if cell_alpha is None:
            self._cell_alpha = None
        elif cell_alpha.__class__.__name__ == "XSDataDouble":
            self._cell_alpha = cell_alpha
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCell_alpha argument is not XSDataDouble but %s" % cell_alpha.__class__.__name__
            raise BaseException(strMessage)
    def delCell_alpha(self): self._cell_alpha = None
    cell_alpha = property(getCell_alpha, setCell_alpha, delCell_alpha, "Property for cell_alpha")
    # Methods and properties for the 'cell_beta' attribute
    def getCell_beta(self): return self._cell_beta
    def setCell_beta(self, cell_beta):
        if cell_beta is None:
            self._cell_beta = None
        elif cell_beta.__class__.__name__ == "XSDataDouble":
            self._cell_beta = cell_beta
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCell_beta argument is not XSDataDouble but %s" % cell_beta.__class__.__name__
            raise BaseException(strMessage)
    def delCell_beta(self): self._cell_beta = None
    cell_beta = property(getCell_beta, setCell_beta, delCell_beta, "Property for cell_beta")
    # Methods and properties for the 'cell_gamma' attribute
    def getCell_gamma(self): return self._cell_gamma
    def setCell_gamma(self, cell_gamma):
        if cell_gamma is None:
            self._cell_gamma = None
        elif cell_gamma.__class__.__name__ == "XSDataDouble":
            self._cell_gamma = cell_gamma
        else:
            strMessage = "ERROR! XSDataXdsOutput.setCell_gamma argument is not XSDataDouble but %s" % cell_gamma.__class__.__name__
            raise BaseException(strMessage)
    def delCell_gamma(self): self._cell_gamma = None
    cell_gamma = property(getCell_gamma, setCell_gamma, delCell_gamma, "Property for cell_gamma")
    # Methods and properties for the 'unit_cell_constants' attribute
    def getUnit_cell_constants(self): return self._unit_cell_constants
    def setUnit_cell_constants(self, unit_cell_constants):
        if unit_cell_constants is None:
            self._unit_cell_constants = []
        elif unit_cell_constants.__class__.__name__ == "list":
            self._unit_cell_constants = unit_cell_constants
        else:
            strMessage = "ERROR! XSDataXdsOutput.setUnit_cell_constants argument is not list but %s" % unit_cell_constants.__class__.__name__
            raise BaseException(strMessage)
    def delUnit_cell_constants(self): self._unit_cell_constants = None
    unit_cell_constants = property(getUnit_cell_constants, setUnit_cell_constants, delUnit_cell_constants, "Property for unit_cell_constants")
    def addUnit_cell_constants(self, value):
        if value is None:
            strMessage = "ERROR! XSDataXdsOutput.addUnit_cell_constants argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._unit_cell_constants.append(value)
        else:
            strMessage = "ERROR! XSDataXdsOutput.addUnit_cell_constants argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertUnit_cell_constants(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataXdsOutput.insertUnit_cell_constants argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataXdsOutput.insertUnit_cell_constants argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._unit_cell_constants[index] = value
        else:
            strMessage = "ERROR! XSDataXdsOutput.addUnit_cell_constants argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'sg_number' attribute
    def getSg_number(self): return self._sg_number
    def setSg_number(self, sg_number):
        if sg_number is None:
            self._sg_number = None
        elif sg_number.__class__.__name__ == "XSDataInteger":
            self._sg_number = sg_number
        else:
            strMessage = "ERROR! XSDataXdsOutput.setSg_number argument is not XSDataInteger but %s" % sg_number.__class__.__name__
            raise BaseException(strMessage)
    def delSg_number(self): self._sg_number = None
    sg_number = property(getSg_number, setSg_number, delSg_number, "Property for sg_number")
    # Methods and properties for the 'xds_run_directory' attribute
    def getXds_run_directory(self): return self._xds_run_directory
    def setXds_run_directory(self, xds_run_directory):
        if xds_run_directory is None:
            self._xds_run_directory = None
        elif xds_run_directory.__class__.__name__ == "XSDataString":
            self._xds_run_directory = xds_run_directory
        else:
            strMessage = "ERROR! XSDataXdsOutput.setXds_run_directory argument is not XSDataString but %s" % xds_run_directory.__class__.__name__
            raise BaseException(strMessage)
    def delXds_run_directory(self): self._xds_run_directory = None
    xds_run_directory = property(getXds_run_directory, setXds_run_directory, delXds_run_directory, "Property for xds_run_directory")
    def export(self, outfile, level, name_='XSDataXdsOutput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXdsOutput'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for completeness_entries_ in self.getCompleteness_entries():
            completeness_entries_.export(outfile, level, name_='completeness_entries')
        if self.getCompleteness_entries() == []:
            warnEmptyAttribute("completeness_entries", "XSDataXdsCompletenessEntry")
        if self._total_completeness is not None:
            self.total_completeness.export(outfile, level, name_='total_completeness')
        else:
            warnEmptyAttribute("total_completeness", "XSDataXdsCompletenessEntry")
        if self._crystal_mosaicity is not None:
            self.crystal_mosaicity.export(outfile, level, name_='crystal_mosaicity')
        else:
            warnEmptyAttribute("crystal_mosaicity", "XSDataDouble")
        if self._direct_beam_coordinates is not None:
            self.direct_beam_coordinates.export(outfile, level, name_='direct_beam_coordinates')
        else:
            warnEmptyAttribute("direct_beam_coordinates", "XSDataVectorDouble")
        if self._direct_beam_detector_coordinates is not None:
            self.direct_beam_detector_coordinates.export(outfile, level, name_='direct_beam_detector_coordinates')
        else:
            warnEmptyAttribute("direct_beam_detector_coordinates", "XSData2DCoordinates")
        if self._detector_origin is not None:
            self.detector_origin.export(outfile, level, name_='detector_origin')
        else:
            warnEmptyAttribute("detector_origin", "XSData2DCoordinates")
        if self._crystal_to_detector_distance is not None:
            self.crystal_to_detector_distance.export(outfile, level, name_='crystal_to_detector_distance')
        else:
            warnEmptyAttribute("crystal_to_detector_distance", "XSDataDouble")
        if self._coordinates_of_unit_cell_a_axis is not None:
            self.coordinates_of_unit_cell_a_axis.export(outfile, level, name_='coordinates_of_unit_cell_a_axis')
        else:
            warnEmptyAttribute("coordinates_of_unit_cell_a_axis", "XSDataVectorDouble")
        if self._coordinates_of_unit_cell_b_axis is not None:
            self.coordinates_of_unit_cell_b_axis.export(outfile, level, name_='coordinates_of_unit_cell_b_axis')
        else:
            warnEmptyAttribute("coordinates_of_unit_cell_b_axis", "XSDataVectorDouble")
        if self._coordinates_of_unit_cell_c_axis is not None:
            self.coordinates_of_unit_cell_c_axis.export(outfile, level, name_='coordinates_of_unit_cell_c_axis')
        else:
            warnEmptyAttribute("coordinates_of_unit_cell_c_axis", "XSDataVectorDouble")
        if self._cell_a is not None:
            self.cell_a.export(outfile, level, name_='cell_a')
        else:
            warnEmptyAttribute("cell_a", "XSDataDouble")
        if self._cell_b is not None:
            self.cell_b.export(outfile, level, name_='cell_b')
        else:
            warnEmptyAttribute("cell_b", "XSDataDouble")
        if self._cell_c is not None:
            self.cell_c.export(outfile, level, name_='cell_c')
        else:
            warnEmptyAttribute("cell_c", "XSDataDouble")
        if self._cell_alpha is not None:
            self.cell_alpha.export(outfile, level, name_='cell_alpha')
        else:
            warnEmptyAttribute("cell_alpha", "XSDataDouble")
        if self._cell_beta is not None:
            self.cell_beta.export(outfile, level, name_='cell_beta')
        else:
            warnEmptyAttribute("cell_beta", "XSDataDouble")
        if self._cell_gamma is not None:
            self.cell_gamma.export(outfile, level, name_='cell_gamma')
        else:
            warnEmptyAttribute("cell_gamma", "XSDataDouble")
        for unit_cell_constants_ in self.getUnit_cell_constants():
            unit_cell_constants_.export(outfile, level, name_='unit_cell_constants')
        if self._sg_number is not None:
            self.sg_number.export(outfile, level, name_='sg_number')
        if self._xds_run_directory is not None:
            self.xds_run_directory.export(outfile, level, name_='xds_run_directory')
        else:
            warnEmptyAttribute("xds_run_directory", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness_entries':
            obj_ = XSDataXdsCompletenessEntry()
            obj_.build(child_)
            self.completeness_entries.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'total_completeness':
            obj_ = XSDataXdsCompletenessEntry()
            obj_.build(child_)
            self.setTotal_completeness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystal_mosaicity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCrystal_mosaicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'direct_beam_coordinates':
            obj_ = XSDataVectorDouble()
            obj_.build(child_)
            self.setDirect_beam_coordinates(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'direct_beam_detector_coordinates':
            obj_ = XSData2DCoordinates()
            obj_.build(child_)
            self.setDirect_beam_detector_coordinates(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detector_origin':
            obj_ = XSData2DCoordinates()
            obj_.build(child_)
            self.setDetector_origin(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'crystal_to_detector_distance':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCrystal_to_detector_distance(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'coordinates_of_unit_cell_a_axis':
            obj_ = XSDataVectorDouble()
            obj_.build(child_)
            self.setCoordinates_of_unit_cell_a_axis(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'coordinates_of_unit_cell_b_axis':
            obj_ = XSDataVectorDouble()
            obj_.build(child_)
            self.setCoordinates_of_unit_cell_b_axis(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'coordinates_of_unit_cell_c_axis':
            obj_ = XSDataVectorDouble()
            obj_.build(child_)
            self.setCoordinates_of_unit_cell_c_axis(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell_a':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCell_a(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell_b':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCell_b(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell_c':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCell_c(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell_alpha':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCell_alpha(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell_beta':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCell_beta(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell_gamma':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCell_gamma(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit_cell_constants':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.unit_cell_constants.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sg_number':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSg_number(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xds_run_directory':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setXds_run_directory(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXdsOutput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXdsOutput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXdsOutput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXdsOutput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXdsOutput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXdsOutput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXdsOutput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXdsOutput


class XSDataXdsOutputFile(XSDataInput):
    def __init__(self, configuration=None, gxparm=None, correct_lp=None):
        XSDataInput.__init__(self, configuration)
        if correct_lp is None:
            self._correct_lp = None
        elif correct_lp.__class__.__name__ == "XSDataFile":
            self._correct_lp = correct_lp
        else:
            strMessage = "ERROR! XSDataXdsOutputFile constructor argument 'correct_lp' is not XSDataFile but %s" % self._correct_lp.__class__.__name__
            raise BaseException(strMessage)
        if gxparm is None:
            self._gxparm = None
        elif gxparm.__class__.__name__ == "XSDataFile":
            self._gxparm = gxparm
        else:
            strMessage = "ERROR! XSDataXdsOutputFile constructor argument 'gxparm' is not XSDataFile but %s" % self._gxparm.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'correct_lp' attribute
    def getCorrect_lp(self): return self._correct_lp
    def setCorrect_lp(self, correct_lp):
        if correct_lp is None:
            self._correct_lp = None
        elif correct_lp.__class__.__name__ == "XSDataFile":
            self._correct_lp = correct_lp
        else:
            strMessage = "ERROR! XSDataXdsOutputFile.setCorrect_lp argument is not XSDataFile but %s" % correct_lp.__class__.__name__
            raise BaseException(strMessage)
    def delCorrect_lp(self): self._correct_lp = None
    correct_lp = property(getCorrect_lp, setCorrect_lp, delCorrect_lp, "Property for correct_lp")
    # Methods and properties for the 'gxparm' attribute
    def getGxparm(self): return self._gxparm
    def setGxparm(self, gxparm):
        if gxparm is None:
            self._gxparm = None
        elif gxparm.__class__.__name__ == "XSDataFile":
            self._gxparm = gxparm
        else:
            strMessage = "ERROR! XSDataXdsOutputFile.setGxparm argument is not XSDataFile but %s" % gxparm.__class__.__name__
            raise BaseException(strMessage)
    def delGxparm(self): self._gxparm = None
    gxparm = property(getGxparm, setGxparm, delGxparm, "Property for gxparm")
    def export(self, outfile, level, name_='XSDataXdsOutputFile'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXdsOutputFile'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._correct_lp is not None:
            self.correct_lp.export(outfile, level, name_='correct_lp')
        else:
            warnEmptyAttribute("correct_lp", "XSDataFile")
        if self._gxparm is not None:
            self.gxparm.export(outfile, level, name_='gxparm')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'correct_lp':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setCorrect_lp(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gxparm':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGxparm(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXdsOutputFile" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXdsOutputFile' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXdsOutputFile is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXdsOutputFile.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXdsOutputFile()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXdsOutputFile" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXdsOutputFile()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXdsOutputFile


class XSDataXscaleParsedOutput(XSDataResult):
    def __init__(self, status=None, completeness_entries=None, total_completeness=None):
        XSDataResult.__init__(self, status)
        if total_completeness is None:
            self._total_completeness = None
        elif total_completeness.__class__.__name__ == "XSDataXscaleCompletenessEntry":
            self._total_completeness = total_completeness
        else:
            strMessage = "ERROR! XSDataXscaleParsedOutput constructor argument 'total_completeness' is not XSDataXscaleCompletenessEntry but %s" % self._total_completeness.__class__.__name__
            raise BaseException(strMessage)
        if completeness_entries is None:
            self._completeness_entries = []
        elif completeness_entries.__class__.__name__ == "list":
            self._completeness_entries = completeness_entries
        else:
            strMessage = "ERROR! XSDataXscaleParsedOutput constructor argument 'completeness_entries' is not list but %s" % self._completeness_entries.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'total_completeness' attribute
    def getTotal_completeness(self): return self._total_completeness
    def setTotal_completeness(self, total_completeness):
        if total_completeness is None:
            self._total_completeness = None
        elif total_completeness.__class__.__name__ == "XSDataXscaleCompletenessEntry":
            self._total_completeness = total_completeness
        else:
            strMessage = "ERROR! XSDataXscaleParsedOutput.setTotal_completeness argument is not XSDataXscaleCompletenessEntry but %s" % total_completeness.__class__.__name__
            raise BaseException(strMessage)
    def delTotal_completeness(self): self._total_completeness = None
    total_completeness = property(getTotal_completeness, setTotal_completeness, delTotal_completeness, "Property for total_completeness")
    # Methods and properties for the 'completeness_entries' attribute
    def getCompleteness_entries(self): return self._completeness_entries
    def setCompleteness_entries(self, completeness_entries):
        if completeness_entries is None:
            self._completeness_entries = []
        elif completeness_entries.__class__.__name__ == "list":
            self._completeness_entries = completeness_entries
        else:
            strMessage = "ERROR! XSDataXscaleParsedOutput.setCompleteness_entries argument is not list but %s" % completeness_entries.__class__.__name__
            raise BaseException(strMessage)
    def delCompleteness_entries(self): self._completeness_entries = None
    completeness_entries = property(getCompleteness_entries, setCompleteness_entries, delCompleteness_entries, "Property for completeness_entries")
    def addCompleteness_entries(self, value):
        if value is None:
            strMessage = "ERROR! XSDataXscaleParsedOutput.addCompleteness_entries argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXscaleCompletenessEntry":
            self._completeness_entries.append(value)
        else:
            strMessage = "ERROR! XSDataXscaleParsedOutput.addCompleteness_entries argument is not XSDataXscaleCompletenessEntry but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertCompleteness_entries(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataXscaleParsedOutput.insertCompleteness_entries argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataXscaleParsedOutput.insertCompleteness_entries argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXscaleCompletenessEntry":
            self._completeness_entries[index] = value
        else:
            strMessage = "ERROR! XSDataXscaleParsedOutput.addCompleteness_entries argument is not XSDataXscaleCompletenessEntry but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataXscaleParsedOutput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXscaleParsedOutput'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._total_completeness is not None:
            self.total_completeness.export(outfile, level, name_='total_completeness')
        else:
            warnEmptyAttribute("total_completeness", "XSDataXscaleCompletenessEntry")
        for completeness_entries_ in self.getCompleteness_entries():
            completeness_entries_.export(outfile, level, name_='completeness_entries')
        if self.getCompleteness_entries() == []:
            warnEmptyAttribute("completeness_entries", "XSDataXscaleCompletenessEntry")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'total_completeness':
            obj_ = XSDataXscaleCompletenessEntry()
            obj_.build(child_)
            self.setTotal_completeness(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness_entries':
            obj_ = XSDataXscaleCompletenessEntry()
            obj_.build(child_)
            self.completeness_entries.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXscaleParsedOutput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXscaleParsedOutput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXscaleParsedOutput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXscaleParsedOutput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleParsedOutput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXscaleParsedOutput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleParsedOutput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXscaleParsedOutput


class XSDataXscaleGeneratedFiles(XSDataResult):
    def __init__(self, status=None, stats_noanom_unmerged=None, lp_noanom_unmerged=None, hkl_noanom_unmerged=None, stats_anom_unmerged=None, lp_anom_unmerged=None, hkl_anom_unmerged=None, stats_noanom_merged=None, lp_noanom_merged=None, hkl_noanom_merged=None, stats_anom_merged=None, lp_anom_merged=None, hkl_anom_merged=None):
        XSDataResult.__init__(self, status)
        if hkl_anom_merged is None:
            self._hkl_anom_merged = None
        elif hkl_anom_merged.__class__.__name__ == "XSDataString":
            self._hkl_anom_merged = hkl_anom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'hkl_anom_merged' is not XSDataString but %s" % self._hkl_anom_merged.__class__.__name__
            raise BaseException(strMessage)
        if lp_anom_merged is None:
            self._lp_anom_merged = None
        elif lp_anom_merged.__class__.__name__ == "XSDataString":
            self._lp_anom_merged = lp_anom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'lp_anom_merged' is not XSDataString but %s" % self._lp_anom_merged.__class__.__name__
            raise BaseException(strMessage)
        if stats_anom_merged is None:
            self._stats_anom_merged = None
        elif stats_anom_merged.__class__.__name__ == "XSDataXscaleParsedOutput":
            self._stats_anom_merged = stats_anom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'stats_anom_merged' is not XSDataXscaleParsedOutput but %s" % self._stats_anom_merged.__class__.__name__
            raise BaseException(strMessage)
        if hkl_noanom_merged is None:
            self._hkl_noanom_merged = None
        elif hkl_noanom_merged.__class__.__name__ == "XSDataString":
            self._hkl_noanom_merged = hkl_noanom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'hkl_noanom_merged' is not XSDataString but %s" % self._hkl_noanom_merged.__class__.__name__
            raise BaseException(strMessage)
        if lp_noanom_merged is None:
            self._lp_noanom_merged = None
        elif lp_noanom_merged.__class__.__name__ == "XSDataString":
            self._lp_noanom_merged = lp_noanom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'lp_noanom_merged' is not XSDataString but %s" % self._lp_noanom_merged.__class__.__name__
            raise BaseException(strMessage)
        if stats_noanom_merged is None:
            self._stats_noanom_merged = None
        elif stats_noanom_merged.__class__.__name__ == "XSDataXscaleParsedOutput":
            self._stats_noanom_merged = stats_noanom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'stats_noanom_merged' is not XSDataXscaleParsedOutput but %s" % self._stats_noanom_merged.__class__.__name__
            raise BaseException(strMessage)
        if hkl_anom_unmerged is None:
            self._hkl_anom_unmerged = None
        elif hkl_anom_unmerged.__class__.__name__ == "XSDataString":
            self._hkl_anom_unmerged = hkl_anom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'hkl_anom_unmerged' is not XSDataString but %s" % self._hkl_anom_unmerged.__class__.__name__
            raise BaseException(strMessage)
        if lp_anom_unmerged is None:
            self._lp_anom_unmerged = None
        elif lp_anom_unmerged.__class__.__name__ == "XSDataString":
            self._lp_anom_unmerged = lp_anom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'lp_anom_unmerged' is not XSDataString but %s" % self._lp_anom_unmerged.__class__.__name__
            raise BaseException(strMessage)
        if stats_anom_unmerged is None:
            self._stats_anom_unmerged = None
        elif stats_anom_unmerged.__class__.__name__ == "XSDataXscaleParsedOutput":
            self._stats_anom_unmerged = stats_anom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'stats_anom_unmerged' is not XSDataXscaleParsedOutput but %s" % self._stats_anom_unmerged.__class__.__name__
            raise BaseException(strMessage)
        if hkl_noanom_unmerged is None:
            self._hkl_noanom_unmerged = None
        elif hkl_noanom_unmerged.__class__.__name__ == "XSDataString":
            self._hkl_noanom_unmerged = hkl_noanom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'hkl_noanom_unmerged' is not XSDataString but %s" % self._hkl_noanom_unmerged.__class__.__name__
            raise BaseException(strMessage)
        if lp_noanom_unmerged is None:
            self._lp_noanom_unmerged = None
        elif lp_noanom_unmerged.__class__.__name__ == "XSDataString":
            self._lp_noanom_unmerged = lp_noanom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'lp_noanom_unmerged' is not XSDataString but %s" % self._lp_noanom_unmerged.__class__.__name__
            raise BaseException(strMessage)
        if stats_noanom_unmerged is None:
            self._stats_noanom_unmerged = None
        elif stats_noanom_unmerged.__class__.__name__ == "XSDataXscaleParsedOutput":
            self._stats_noanom_unmerged = stats_noanom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles constructor argument 'stats_noanom_unmerged' is not XSDataXscaleParsedOutput but %s" % self._stats_noanom_unmerged.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'hkl_anom_merged' attribute
    def getHkl_anom_merged(self): return self._hkl_anom_merged
    def setHkl_anom_merged(self, hkl_anom_merged):
        if hkl_anom_merged is None:
            self._hkl_anom_merged = None
        elif hkl_anom_merged.__class__.__name__ == "XSDataString":
            self._hkl_anom_merged = hkl_anom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setHkl_anom_merged argument is not XSDataString but %s" % hkl_anom_merged.__class__.__name__
            raise BaseException(strMessage)
    def delHkl_anom_merged(self): self._hkl_anom_merged = None
    hkl_anom_merged = property(getHkl_anom_merged, setHkl_anom_merged, delHkl_anom_merged, "Property for hkl_anom_merged")
    # Methods and properties for the 'lp_anom_merged' attribute
    def getLp_anom_merged(self): return self._lp_anom_merged
    def setLp_anom_merged(self, lp_anom_merged):
        if lp_anom_merged is None:
            self._lp_anom_merged = None
        elif lp_anom_merged.__class__.__name__ == "XSDataString":
            self._lp_anom_merged = lp_anom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setLp_anom_merged argument is not XSDataString but %s" % lp_anom_merged.__class__.__name__
            raise BaseException(strMessage)
    def delLp_anom_merged(self): self._lp_anom_merged = None
    lp_anom_merged = property(getLp_anom_merged, setLp_anom_merged, delLp_anom_merged, "Property for lp_anom_merged")
    # Methods and properties for the 'stats_anom_merged' attribute
    def getStats_anom_merged(self): return self._stats_anom_merged
    def setStats_anom_merged(self, stats_anom_merged):
        if stats_anom_merged is None:
            self._stats_anom_merged = None
        elif stats_anom_merged.__class__.__name__ == "XSDataXscaleParsedOutput":
            self._stats_anom_merged = stats_anom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setStats_anom_merged argument is not XSDataXscaleParsedOutput but %s" % stats_anom_merged.__class__.__name__
            raise BaseException(strMessage)
    def delStats_anom_merged(self): self._stats_anom_merged = None
    stats_anom_merged = property(getStats_anom_merged, setStats_anom_merged, delStats_anom_merged, "Property for stats_anom_merged")
    # Methods and properties for the 'hkl_noanom_merged' attribute
    def getHkl_noanom_merged(self): return self._hkl_noanom_merged
    def setHkl_noanom_merged(self, hkl_noanom_merged):
        if hkl_noanom_merged is None:
            self._hkl_noanom_merged = None
        elif hkl_noanom_merged.__class__.__name__ == "XSDataString":
            self._hkl_noanom_merged = hkl_noanom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setHkl_noanom_merged argument is not XSDataString but %s" % hkl_noanom_merged.__class__.__name__
            raise BaseException(strMessage)
    def delHkl_noanom_merged(self): self._hkl_noanom_merged = None
    hkl_noanom_merged = property(getHkl_noanom_merged, setHkl_noanom_merged, delHkl_noanom_merged, "Property for hkl_noanom_merged")
    # Methods and properties for the 'lp_noanom_merged' attribute
    def getLp_noanom_merged(self): return self._lp_noanom_merged
    def setLp_noanom_merged(self, lp_noanom_merged):
        if lp_noanom_merged is None:
            self._lp_noanom_merged = None
        elif lp_noanom_merged.__class__.__name__ == "XSDataString":
            self._lp_noanom_merged = lp_noanom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setLp_noanom_merged argument is not XSDataString but %s" % lp_noanom_merged.__class__.__name__
            raise BaseException(strMessage)
    def delLp_noanom_merged(self): self._lp_noanom_merged = None
    lp_noanom_merged = property(getLp_noanom_merged, setLp_noanom_merged, delLp_noanom_merged, "Property for lp_noanom_merged")
    # Methods and properties for the 'stats_noanom_merged' attribute
    def getStats_noanom_merged(self): return self._stats_noanom_merged
    def setStats_noanom_merged(self, stats_noanom_merged):
        if stats_noanom_merged is None:
            self._stats_noanom_merged = None
        elif stats_noanom_merged.__class__.__name__ == "XSDataXscaleParsedOutput":
            self._stats_noanom_merged = stats_noanom_merged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setStats_noanom_merged argument is not XSDataXscaleParsedOutput but %s" % stats_noanom_merged.__class__.__name__
            raise BaseException(strMessage)
    def delStats_noanom_merged(self): self._stats_noanom_merged = None
    stats_noanom_merged = property(getStats_noanom_merged, setStats_noanom_merged, delStats_noanom_merged, "Property for stats_noanom_merged")
    # Methods and properties for the 'hkl_anom_unmerged' attribute
    def getHkl_anom_unmerged(self): return self._hkl_anom_unmerged
    def setHkl_anom_unmerged(self, hkl_anom_unmerged):
        if hkl_anom_unmerged is None:
            self._hkl_anom_unmerged = None
        elif hkl_anom_unmerged.__class__.__name__ == "XSDataString":
            self._hkl_anom_unmerged = hkl_anom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setHkl_anom_unmerged argument is not XSDataString but %s" % hkl_anom_unmerged.__class__.__name__
            raise BaseException(strMessage)
    def delHkl_anom_unmerged(self): self._hkl_anom_unmerged = None
    hkl_anom_unmerged = property(getHkl_anom_unmerged, setHkl_anom_unmerged, delHkl_anom_unmerged, "Property for hkl_anom_unmerged")
    # Methods and properties for the 'lp_anom_unmerged' attribute
    def getLp_anom_unmerged(self): return self._lp_anom_unmerged
    def setLp_anom_unmerged(self, lp_anom_unmerged):
        if lp_anom_unmerged is None:
            self._lp_anom_unmerged = None
        elif lp_anom_unmerged.__class__.__name__ == "XSDataString":
            self._lp_anom_unmerged = lp_anom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setLp_anom_unmerged argument is not XSDataString but %s" % lp_anom_unmerged.__class__.__name__
            raise BaseException(strMessage)
    def delLp_anom_unmerged(self): self._lp_anom_unmerged = None
    lp_anom_unmerged = property(getLp_anom_unmerged, setLp_anom_unmerged, delLp_anom_unmerged, "Property for lp_anom_unmerged")
    # Methods and properties for the 'stats_anom_unmerged' attribute
    def getStats_anom_unmerged(self): return self._stats_anom_unmerged
    def setStats_anom_unmerged(self, stats_anom_unmerged):
        if stats_anom_unmerged is None:
            self._stats_anom_unmerged = None
        elif stats_anom_unmerged.__class__.__name__ == "XSDataXscaleParsedOutput":
            self._stats_anom_unmerged = stats_anom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setStats_anom_unmerged argument is not XSDataXscaleParsedOutput but %s" % stats_anom_unmerged.__class__.__name__
            raise BaseException(strMessage)
    def delStats_anom_unmerged(self): self._stats_anom_unmerged = None
    stats_anom_unmerged = property(getStats_anom_unmerged, setStats_anom_unmerged, delStats_anom_unmerged, "Property for stats_anom_unmerged")
    # Methods and properties for the 'hkl_noanom_unmerged' attribute
    def getHkl_noanom_unmerged(self): return self._hkl_noanom_unmerged
    def setHkl_noanom_unmerged(self, hkl_noanom_unmerged):
        if hkl_noanom_unmerged is None:
            self._hkl_noanom_unmerged = None
        elif hkl_noanom_unmerged.__class__.__name__ == "XSDataString":
            self._hkl_noanom_unmerged = hkl_noanom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setHkl_noanom_unmerged argument is not XSDataString but %s" % hkl_noanom_unmerged.__class__.__name__
            raise BaseException(strMessage)
    def delHkl_noanom_unmerged(self): self._hkl_noanom_unmerged = None
    hkl_noanom_unmerged = property(getHkl_noanom_unmerged, setHkl_noanom_unmerged, delHkl_noanom_unmerged, "Property for hkl_noanom_unmerged")
    # Methods and properties for the 'lp_noanom_unmerged' attribute
    def getLp_noanom_unmerged(self): return self._lp_noanom_unmerged
    def setLp_noanom_unmerged(self, lp_noanom_unmerged):
        if lp_noanom_unmerged is None:
            self._lp_noanom_unmerged = None
        elif lp_noanom_unmerged.__class__.__name__ == "XSDataString":
            self._lp_noanom_unmerged = lp_noanom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setLp_noanom_unmerged argument is not XSDataString but %s" % lp_noanom_unmerged.__class__.__name__
            raise BaseException(strMessage)
    def delLp_noanom_unmerged(self): self._lp_noanom_unmerged = None
    lp_noanom_unmerged = property(getLp_noanom_unmerged, setLp_noanom_unmerged, delLp_noanom_unmerged, "Property for lp_noanom_unmerged")
    # Methods and properties for the 'stats_noanom_unmerged' attribute
    def getStats_noanom_unmerged(self): return self._stats_noanom_unmerged
    def setStats_noanom_unmerged(self, stats_noanom_unmerged):
        if stats_noanom_unmerged is None:
            self._stats_noanom_unmerged = None
        elif stats_noanom_unmerged.__class__.__name__ == "XSDataXscaleParsedOutput":
            self._stats_noanom_unmerged = stats_noanom_unmerged
        else:
            strMessage = "ERROR! XSDataXscaleGeneratedFiles.setStats_noanom_unmerged argument is not XSDataXscaleParsedOutput but %s" % stats_noanom_unmerged.__class__.__name__
            raise BaseException(strMessage)
    def delStats_noanom_unmerged(self): self._stats_noanom_unmerged = None
    stats_noanom_unmerged = property(getStats_noanom_unmerged, setStats_noanom_unmerged, delStats_noanom_unmerged, "Property for stats_noanom_unmerged")
    def export(self, outfile, level, name_='XSDataXscaleGeneratedFiles'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXscaleGeneratedFiles'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._hkl_anom_merged is not None:
            self.hkl_anom_merged.export(outfile, level, name_='hkl_anom_merged')
        else:
            warnEmptyAttribute("hkl_anom_merged", "XSDataString")
        if self._lp_anom_merged is not None:
            self.lp_anom_merged.export(outfile, level, name_='lp_anom_merged')
        else:
            warnEmptyAttribute("lp_anom_merged", "XSDataString")
        if self._stats_anom_merged is not None:
            self.stats_anom_merged.export(outfile, level, name_='stats_anom_merged')
        else:
            warnEmptyAttribute("stats_anom_merged", "XSDataXscaleParsedOutput")
        if self._hkl_noanom_merged is not None:
            self.hkl_noanom_merged.export(outfile, level, name_='hkl_noanom_merged')
        else:
            warnEmptyAttribute("hkl_noanom_merged", "XSDataString")
        if self._lp_noanom_merged is not None:
            self.lp_noanom_merged.export(outfile, level, name_='lp_noanom_merged')
        else:
            warnEmptyAttribute("lp_noanom_merged", "XSDataString")
        if self._stats_noanom_merged is not None:
            self.stats_noanom_merged.export(outfile, level, name_='stats_noanom_merged')
        else:
            warnEmptyAttribute("stats_noanom_merged", "XSDataXscaleParsedOutput")
        if self._hkl_anom_unmerged is not None:
            self.hkl_anom_unmerged.export(outfile, level, name_='hkl_anom_unmerged')
        else:
            warnEmptyAttribute("hkl_anom_unmerged", "XSDataString")
        if self._lp_anom_unmerged is not None:
            self.lp_anom_unmerged.export(outfile, level, name_='lp_anom_unmerged')
        else:
            warnEmptyAttribute("lp_anom_unmerged", "XSDataString")
        if self._stats_anom_unmerged is not None:
            self.stats_anom_unmerged.export(outfile, level, name_='stats_anom_unmerged')
        else:
            warnEmptyAttribute("stats_anom_unmerged", "XSDataXscaleParsedOutput")
        if self._hkl_noanom_unmerged is not None:
            self.hkl_noanom_unmerged.export(outfile, level, name_='hkl_noanom_unmerged')
        else:
            warnEmptyAttribute("hkl_noanom_unmerged", "XSDataString")
        if self._lp_noanom_unmerged is not None:
            self.lp_noanom_unmerged.export(outfile, level, name_='lp_noanom_unmerged')
        else:
            warnEmptyAttribute("lp_noanom_unmerged", "XSDataString")
        if self._stats_noanom_unmerged is not None:
            self.stats_noanom_unmerged.export(outfile, level, name_='stats_noanom_unmerged')
        else:
            warnEmptyAttribute("stats_noanom_unmerged", "XSDataXscaleParsedOutput")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hkl_anom_merged':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setHkl_anom_merged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lp_anom_merged':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setLp_anom_merged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'stats_anom_merged':
            obj_ = XSDataXscaleParsedOutput()
            obj_.build(child_)
            self.setStats_anom_merged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hkl_noanom_merged':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setHkl_noanom_merged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lp_noanom_merged':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setLp_noanom_merged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'stats_noanom_merged':
            obj_ = XSDataXscaleParsedOutput()
            obj_.build(child_)
            self.setStats_noanom_merged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hkl_anom_unmerged':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setHkl_anom_unmerged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lp_anom_unmerged':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setLp_anom_unmerged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'stats_anom_unmerged':
            obj_ = XSDataXscaleParsedOutput()
            obj_.build(child_)
            self.setStats_anom_unmerged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hkl_noanom_unmerged':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setHkl_noanom_unmerged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lp_noanom_unmerged':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setLp_noanom_unmerged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'stats_noanom_unmerged':
            obj_ = XSDataXscaleParsedOutput()
            obj_.build(child_)
            self.setStats_noanom_unmerged(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXscaleGeneratedFiles" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXscaleGeneratedFiles' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXscaleGeneratedFiles is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXscaleGeneratedFiles.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleGeneratedFiles()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXscaleGeneratedFiles" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleGeneratedFiles()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXscaleGeneratedFiles


class XSDataXscaleInputFile(XSDataInput):
    def __init__(self, configuration=None, res=None, path_noanom=None, path_anom=None):
        XSDataInput.__init__(self, configuration)
        if path_anom is None:
            self._path_anom = None
        elif path_anom.__class__.__name__ == "XSDataString":
            self._path_anom = path_anom
        else:
            strMessage = "ERROR! XSDataXscaleInputFile constructor argument 'path_anom' is not XSDataString but %s" % self._path_anom.__class__.__name__
            raise BaseException(strMessage)
        if path_noanom is None:
            self._path_noanom = None
        elif path_noanom.__class__.__name__ == "XSDataString":
            self._path_noanom = path_noanom
        else:
            strMessage = "ERROR! XSDataXscaleInputFile constructor argument 'path_noanom' is not XSDataString but %s" % self._path_noanom.__class__.__name__
            raise BaseException(strMessage)
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataDouble":
            self._res = res
        else:
            strMessage = "ERROR! XSDataXscaleInputFile constructor argument 'res' is not XSDataDouble but %s" % self._res.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'path_anom' attribute
    def getPath_anom(self): return self._path_anom
    def setPath_anom(self, path_anom):
        if path_anom is None:
            self._path_anom = None
        elif path_anom.__class__.__name__ == "XSDataString":
            self._path_anom = path_anom
        else:
            strMessage = "ERROR! XSDataXscaleInputFile.setPath_anom argument is not XSDataString but %s" % path_anom.__class__.__name__
            raise BaseException(strMessage)
    def delPath_anom(self): self._path_anom = None
    path_anom = property(getPath_anom, setPath_anom, delPath_anom, "Property for path_anom")
    # Methods and properties for the 'path_noanom' attribute
    def getPath_noanom(self): return self._path_noanom
    def setPath_noanom(self, path_noanom):
        if path_noanom is None:
            self._path_noanom = None
        elif path_noanom.__class__.__name__ == "XSDataString":
            self._path_noanom = path_noanom
        else:
            strMessage = "ERROR! XSDataXscaleInputFile.setPath_noanom argument is not XSDataString but %s" % path_noanom.__class__.__name__
            raise BaseException(strMessage)
    def delPath_noanom(self): self._path_noanom = None
    path_noanom = property(getPath_noanom, setPath_noanom, delPath_noanom, "Property for path_noanom")
    # Methods and properties for the 'res' attribute
    def getRes(self): return self._res
    def setRes(self, res):
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataDouble":
            self._res = res
        else:
            strMessage = "ERROR! XSDataXscaleInputFile.setRes argument is not XSDataDouble but %s" % res.__class__.__name__
            raise BaseException(strMessage)
    def delRes(self): self._res = None
    res = property(getRes, setRes, delRes, "Property for res")
    def export(self, outfile, level, name_='XSDataXscaleInputFile'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXscaleInputFile'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._path_anom is not None:
            self.path_anom.export(outfile, level, name_='path_anom')
        if self._path_noanom is not None:
            self.path_noanom.export(outfile, level, name_='path_noanom')
        if self._res is not None:
            self.res.export(outfile, level, name_='res')
        else:
            warnEmptyAttribute("res", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'path_anom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setPath_anom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'path_noanom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setPath_noanom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'res':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRes(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXscaleInputFile" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXscaleInputFile' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXscaleInputFile is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXscaleInputFile.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleInputFile()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXscaleInputFile" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleInputFile()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXscaleInputFile


class XSDataXscaleInput(XSDataInput):
    def __init__(self, configuration=None, bins=None, sg_number=None, unit_cell_constants=None, xds_files=None, friedels_law=None, merge=None):
        XSDataInput.__init__(self, configuration)
        if merge is None:
            self._merge = None
        elif merge.__class__.__name__ == "XSDataBoolean":
            self._merge = merge
        else:
            strMessage = "ERROR! XSDataXscaleInput constructor argument 'merge' is not XSDataBoolean but %s" % self._merge.__class__.__name__
            raise BaseException(strMessage)
        if friedels_law is None:
            self._friedels_law = None
        elif friedels_law.__class__.__name__ == "XSDataBoolean":
            self._friedels_law = friedels_law
        else:
            strMessage = "ERROR! XSDataXscaleInput constructor argument 'friedels_law' is not XSDataBoolean but %s" % self._friedels_law.__class__.__name__
            raise BaseException(strMessage)
        if xds_files is None:
            self._xds_files = []
        elif xds_files.__class__.__name__ == "list":
            self._xds_files = xds_files
        else:
            strMessage = "ERROR! XSDataXscaleInput constructor argument 'xds_files' is not list but %s" % self._xds_files.__class__.__name__
            raise BaseException(strMessage)
        if unit_cell_constants is None:
            self._unit_cell_constants = []
        elif unit_cell_constants.__class__.__name__ == "list":
            self._unit_cell_constants = unit_cell_constants
        else:
            strMessage = "ERROR! XSDataXscaleInput constructor argument 'unit_cell_constants' is not list but %s" % self._unit_cell_constants.__class__.__name__
            raise BaseException(strMessage)
        if sg_number is None:
            self._sg_number = None
        elif sg_number.__class__.__name__ == "XSDataInteger":
            self._sg_number = sg_number
        else:
            strMessage = "ERROR! XSDataXscaleInput constructor argument 'sg_number' is not XSDataInteger but %s" % self._sg_number.__class__.__name__
            raise BaseException(strMessage)
        if bins is None:
            self._bins = []
        elif bins.__class__.__name__ == "list":
            self._bins = bins
        else:
            strMessage = "ERROR! XSDataXscaleInput constructor argument 'bins' is not list but %s" % self._bins.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'merge' attribute
    def getMerge(self): return self._merge
    def setMerge(self, merge):
        if merge is None:
            self._merge = None
        elif merge.__class__.__name__ == "XSDataBoolean":
            self._merge = merge
        else:
            strMessage = "ERROR! XSDataXscaleInput.setMerge argument is not XSDataBoolean but %s" % merge.__class__.__name__
            raise BaseException(strMessage)
    def delMerge(self): self._merge = None
    merge = property(getMerge, setMerge, delMerge, "Property for merge")
    # Methods and properties for the 'friedels_law' attribute
    def getFriedels_law(self): return self._friedels_law
    def setFriedels_law(self, friedels_law):
        if friedels_law is None:
            self._friedels_law = None
        elif friedels_law.__class__.__name__ == "XSDataBoolean":
            self._friedels_law = friedels_law
        else:
            strMessage = "ERROR! XSDataXscaleInput.setFriedels_law argument is not XSDataBoolean but %s" % friedels_law.__class__.__name__
            raise BaseException(strMessage)
    def delFriedels_law(self): self._friedels_law = None
    friedels_law = property(getFriedels_law, setFriedels_law, delFriedels_law, "Property for friedels_law")
    # Methods and properties for the 'xds_files' attribute
    def getXds_files(self): return self._xds_files
    def setXds_files(self, xds_files):
        if xds_files is None:
            self._xds_files = []
        elif xds_files.__class__.__name__ == "list":
            self._xds_files = xds_files
        else:
            strMessage = "ERROR! XSDataXscaleInput.setXds_files argument is not list but %s" % xds_files.__class__.__name__
            raise BaseException(strMessage)
    def delXds_files(self): self._xds_files = None
    xds_files = property(getXds_files, setXds_files, delXds_files, "Property for xds_files")
    def addXds_files(self, value):
        if value is None:
            strMessage = "ERROR! XSDataXscaleInput.addXds_files argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXscaleInputFile":
            self._xds_files.append(value)
        else:
            strMessage = "ERROR! XSDataXscaleInput.addXds_files argument is not XSDataXscaleInputFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertXds_files(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataXscaleInput.insertXds_files argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataXscaleInput.insertXds_files argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXscaleInputFile":
            self._xds_files[index] = value
        else:
            strMessage = "ERROR! XSDataXscaleInput.addXds_files argument is not XSDataXscaleInputFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'unit_cell_constants' attribute
    def getUnit_cell_constants(self): return self._unit_cell_constants
    def setUnit_cell_constants(self, unit_cell_constants):
        if unit_cell_constants is None:
            self._unit_cell_constants = []
        elif unit_cell_constants.__class__.__name__ == "list":
            self._unit_cell_constants = unit_cell_constants
        else:
            strMessage = "ERROR! XSDataXscaleInput.setUnit_cell_constants argument is not list but %s" % unit_cell_constants.__class__.__name__
            raise BaseException(strMessage)
    def delUnit_cell_constants(self): self._unit_cell_constants = None
    unit_cell_constants = property(getUnit_cell_constants, setUnit_cell_constants, delUnit_cell_constants, "Property for unit_cell_constants")
    def addUnit_cell_constants(self, value):
        if value is None:
            strMessage = "ERROR! XSDataXscaleInput.addUnit_cell_constants argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._unit_cell_constants.append(value)
        else:
            strMessage = "ERROR! XSDataXscaleInput.addUnit_cell_constants argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertUnit_cell_constants(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataXscaleInput.insertUnit_cell_constants argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataXscaleInput.insertUnit_cell_constants argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._unit_cell_constants[index] = value
        else:
            strMessage = "ERROR! XSDataXscaleInput.addUnit_cell_constants argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'sg_number' attribute
    def getSg_number(self): return self._sg_number
    def setSg_number(self, sg_number):
        if sg_number is None:
            self._sg_number = None
        elif sg_number.__class__.__name__ == "XSDataInteger":
            self._sg_number = sg_number
        else:
            strMessage = "ERROR! XSDataXscaleInput.setSg_number argument is not XSDataInteger but %s" % sg_number.__class__.__name__
            raise BaseException(strMessage)
    def delSg_number(self): self._sg_number = None
    sg_number = property(getSg_number, setSg_number, delSg_number, "Property for sg_number")
    # Methods and properties for the 'bins' attribute
    def getBins(self): return self._bins
    def setBins(self, bins):
        if bins is None:
            self._bins = []
        elif bins.__class__.__name__ == "list":
            self._bins = bins
        else:
            strMessage = "ERROR! XSDataXscaleInput.setBins argument is not list but %s" % bins.__class__.__name__
            raise BaseException(strMessage)
    def delBins(self): self._bins = None
    bins = property(getBins, setBins, delBins, "Property for bins")
    def addBins(self, value):
        if value is None:
            strMessage = "ERROR! XSDataXscaleInput.addBins argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._bins.append(value)
        else:
            strMessage = "ERROR! XSDataXscaleInput.addBins argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertBins(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataXscaleInput.insertBins argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataXscaleInput.insertBins argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._bins[index] = value
        else:
            strMessage = "ERROR! XSDataXscaleInput.addBins argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataXscaleInput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXscaleInput'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._merge is not None:
            self.merge.export(outfile, level, name_='merge')
        else:
            warnEmptyAttribute("merge", "XSDataBoolean")
        if self._friedels_law is not None:
            self.friedels_law.export(outfile, level, name_='friedels_law')
        else:
            warnEmptyAttribute("friedels_law", "XSDataBoolean")
        for xds_files_ in self.getXds_files():
            xds_files_.export(outfile, level, name_='xds_files')
        if self.getXds_files() == []:
            warnEmptyAttribute("xds_files", "XSDataXscaleInputFile")
        for unit_cell_constants_ in self.getUnit_cell_constants():
            unit_cell_constants_.export(outfile, level, name_='unit_cell_constants')
        if self.getUnit_cell_constants() == []:
            warnEmptyAttribute("unit_cell_constants", "XSDataDouble")
        if self._sg_number is not None:
            self.sg_number.export(outfile, level, name_='sg_number')
        else:
            warnEmptyAttribute("sg_number", "XSDataInteger")
        for bins_ in self.getBins():
            bins_.export(outfile, level, name_='bins')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'merge':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setMerge(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'friedels_law':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setFriedels_law(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xds_files':
            obj_ = XSDataXscaleInputFile()
            obj_.build(child_)
            self.xds_files.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit_cell_constants':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.unit_cell_constants.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sg_number':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSg_number(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bins':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.bins.append(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXscaleInput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXscaleInput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXscaleInput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXscaleInput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleInput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXscaleInput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleInput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXscaleInput


class XSDataXscaleOutput(XSDataResult):
    def __init__(self, status=None, lp_file=None, hkl_file=None, succeeded=None):
        XSDataResult.__init__(self, status)
        if succeeded is None:
            self._succeeded = None
        elif succeeded.__class__.__name__ == "XSDataBoolean":
            self._succeeded = succeeded
        else:
            strMessage = "ERROR! XSDataXscaleOutput constructor argument 'succeeded' is not XSDataBoolean but %s" % self._succeeded.__class__.__name__
            raise BaseException(strMessage)
        if hkl_file is None:
            self._hkl_file = None
        elif hkl_file.__class__.__name__ == "XSDataString":
            self._hkl_file = hkl_file
        else:
            strMessage = "ERROR! XSDataXscaleOutput constructor argument 'hkl_file' is not XSDataString but %s" % self._hkl_file.__class__.__name__
            raise BaseException(strMessage)
        if lp_file is None:
            self._lp_file = None
        elif lp_file.__class__.__name__ == "XSDataString":
            self._lp_file = lp_file
        else:
            strMessage = "ERROR! XSDataXscaleOutput constructor argument 'lp_file' is not XSDataString but %s" % self._lp_file.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'succeeded' attribute
    def getSucceeded(self): return self._succeeded
    def setSucceeded(self, succeeded):
        if succeeded is None:
            self._succeeded = None
        elif succeeded.__class__.__name__ == "XSDataBoolean":
            self._succeeded = succeeded
        else:
            strMessage = "ERROR! XSDataXscaleOutput.setSucceeded argument is not XSDataBoolean but %s" % succeeded.__class__.__name__
            raise BaseException(strMessage)
    def delSucceeded(self): self._succeeded = None
    succeeded = property(getSucceeded, setSucceeded, delSucceeded, "Property for succeeded")
    # Methods and properties for the 'hkl_file' attribute
    def getHkl_file(self): return self._hkl_file
    def setHkl_file(self, hkl_file):
        if hkl_file is None:
            self._hkl_file = None
        elif hkl_file.__class__.__name__ == "XSDataString":
            self._hkl_file = hkl_file
        else:
            strMessage = "ERROR! XSDataXscaleOutput.setHkl_file argument is not XSDataString but %s" % hkl_file.__class__.__name__
            raise BaseException(strMessage)
    def delHkl_file(self): self._hkl_file = None
    hkl_file = property(getHkl_file, setHkl_file, delHkl_file, "Property for hkl_file")
    # Methods and properties for the 'lp_file' attribute
    def getLp_file(self): return self._lp_file
    def setLp_file(self, lp_file):
        if lp_file is None:
            self._lp_file = None
        elif lp_file.__class__.__name__ == "XSDataString":
            self._lp_file = lp_file
        else:
            strMessage = "ERROR! XSDataXscaleOutput.setLp_file argument is not XSDataString but %s" % lp_file.__class__.__name__
            raise BaseException(strMessage)
    def delLp_file(self): self._lp_file = None
    lp_file = property(getLp_file, setLp_file, delLp_file, "Property for lp_file")
    def export(self, outfile, level, name_='XSDataXscaleOutput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXscaleOutput'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._succeeded is not None:
            self.succeeded.export(outfile, level, name_='succeeded')
        else:
            warnEmptyAttribute("succeeded", "XSDataBoolean")
        if self._hkl_file is not None:
            self.hkl_file.export(outfile, level, name_='hkl_file')
        if self._lp_file is not None:
            self.lp_file.export(outfile, level, name_='lp_file')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'succeeded':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setSucceeded(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hkl_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setHkl_file(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lp_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setLp_file(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXscaleOutput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXscaleOutput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXscaleOutput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXscaleOutput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleOutput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXscaleOutput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleOutput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXscaleOutput


class XSDataXscaleParsingInput(XSDataInput):
    def __init__(self, configuration=None, lp_file=None):
        XSDataInput.__init__(self, configuration)
        if lp_file is None:
            self._lp_file = None
        elif lp_file.__class__.__name__ == "XSDataString":
            self._lp_file = lp_file
        else:
            strMessage = "ERROR! XSDataXscaleParsingInput constructor argument 'lp_file' is not XSDataString but %s" % self._lp_file.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'lp_file' attribute
    def getLp_file(self): return self._lp_file
    def setLp_file(self, lp_file):
        if lp_file is None:
            self._lp_file = None
        elif lp_file.__class__.__name__ == "XSDataString":
            self._lp_file = lp_file
        else:
            strMessage = "ERROR! XSDataXscaleParsingInput.setLp_file argument is not XSDataString but %s" % lp_file.__class__.__name__
            raise BaseException(strMessage)
    def delLp_file(self): self._lp_file = None
    lp_file = property(getLp_file, setLp_file, delLp_file, "Property for lp_file")
    def export(self, outfile, level, name_='XSDataXscaleParsingInput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXscaleParsingInput'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._lp_file is not None:
            self.lp_file.export(outfile, level, name_='lp_file')
        else:
            warnEmptyAttribute("lp_file", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lp_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setLp_file(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXscaleParsingInput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXscaleParsingInput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXscaleParsingInput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXscaleParsingInput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleParsingInput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXscaleParsingInput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXscaleParsingInput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXscaleParsingInput


class XSDataInputXDSGenerateBackgroundImage(XSDataInputXDS):
    def __init__(self, configuration=None, filePaths=None, image_link=None, image=None, goniostat=None, detector=None, crystal=None, beam=None):
        XSDataInputXDS.__init__(self, configuration, filePaths, image_link, image, goniostat, detector, crystal, beam)
    def export(self, outfile, level, name_='XSDataInputXDSGenerateBackgroundImage'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputXDSGenerateBackgroundImage'):
        XSDataInputXDS.exportChildren(self, outfile, level, name_)
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        pass
        XSDataInputXDS.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputXDSGenerateBackgroundImage" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputXDSGenerateBackgroundImage' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputXDSGenerateBackgroundImage is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputXDSGenerateBackgroundImage.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputXDSGenerateBackgroundImage()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputXDSGenerateBackgroundImage" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputXDSGenerateBackgroundImage()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputXDSGenerateBackgroundImage


class XSDataInputXDSIndexing(XSDataInputXDS):
    def __init__(self, configuration=None, filePaths=None, image_link=None, image=None, goniostat=None, detector=None, crystal=None, beam=None):
        XSDataInputXDS.__init__(self, configuration, filePaths, image_link, image, goniostat, detector, crystal, beam)
    def export(self, outfile, level, name_='XSDataInputXDSIndexing'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputXDSIndexing'):
        XSDataInputXDS.exportChildren(self, outfile, level, name_)
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        pass
        XSDataInputXDS.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputXDSIndexing" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputXDSIndexing' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputXDSIndexing is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputXDSIndexing.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputXDSIndexing()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputXDSIndexing" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputXDSIndexing()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputXDSIndexing


class XSDataInputXDSIntegration(XSDataInputXDS):
    def __init__(self, configuration=None, filePaths=None, image_link=None, image=None, goniostat=None, detector=None, crystal=None, beam=None):
        XSDataInputXDS.__init__(self, configuration, filePaths, image_link, image, goniostat, detector, crystal, beam)
    def export(self, outfile, level, name_='XSDataInputXDSIntegration'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputXDSIntegration'):
        XSDataInputXDS.exportChildren(self, outfile, level, name_)
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        pass
        XSDataInputXDS.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputXDSIntegration" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputXDSIntegration' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputXDSIntegration is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputXDSIntegration.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputXDSIntegration()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputXDSIntegration" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputXDSIntegration()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputXDSIntegration


class XSDataResultXDSGenerateBackgroundImage(XSDataResultXDS):
    def __init__(self, status=None, filePaths=None, xdsBackgroundImage=None):
        XSDataResultXDS.__init__(self, status, filePaths)
        if xdsBackgroundImage is None:
            self._xdsBackgroundImage = None
        elif xdsBackgroundImage.__class__.__name__ == "XSDataFile":
            self._xdsBackgroundImage = xdsBackgroundImage
        else:
            strMessage = "ERROR! XSDataResultXDSGenerateBackgroundImage constructor argument 'xdsBackgroundImage' is not XSDataFile but %s" % self._xdsBackgroundImage.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'xdsBackgroundImage' attribute
    def getXdsBackgroundImage(self): return self._xdsBackgroundImage
    def setXdsBackgroundImage(self, xdsBackgroundImage):
        if xdsBackgroundImage is None:
            self._xdsBackgroundImage = None
        elif xdsBackgroundImage.__class__.__name__ == "XSDataFile":
            self._xdsBackgroundImage = xdsBackgroundImage
        else:
            strMessage = "ERROR! XSDataResultXDSGenerateBackgroundImage.setXdsBackgroundImage argument is not XSDataFile but %s" % xdsBackgroundImage.__class__.__name__
            raise BaseException(strMessage)
    def delXdsBackgroundImage(self): self._xdsBackgroundImage = None
    xdsBackgroundImage = property(getXdsBackgroundImage, setXdsBackgroundImage, delXdsBackgroundImage, "Property for xdsBackgroundImage")
    def export(self, outfile, level, name_='XSDataResultXDSGenerateBackgroundImage'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultXDSGenerateBackgroundImage'):
        XSDataResultXDS.exportChildren(self, outfile, level, name_)
        if self._xdsBackgroundImage is not None:
            self.xdsBackgroundImage.export(outfile, level, name_='xdsBackgroundImage')
        else:
            warnEmptyAttribute("xdsBackgroundImage", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xdsBackgroundImage':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setXdsBackgroundImage(obj_)
        XSDataResultXDS.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultXDSGenerateBackgroundImage" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultXDSGenerateBackgroundImage' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultXDSGenerateBackgroundImage is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultXDSGenerateBackgroundImage.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultXDSGenerateBackgroundImage()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultXDSGenerateBackgroundImage" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultXDSGenerateBackgroundImage()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultXDSGenerateBackgroundImage


class XSDataResultXDSIndexing(XSDataResultXDS):
    def __init__(self, status=None, filePaths=None, pathToLogFile=None, mosaicity=None, distance=None, beamCentreY=None, beamCentreX=None, unitCell=None, qualityOfFit=None, spaceGroupNumber=None, spaceGroup=None, bravaisLattice=None, latticeCharacter=None):
        XSDataResultXDS.__init__(self, status, filePaths)
        if latticeCharacter is None:
            self._latticeCharacter = None
        elif latticeCharacter.__class__.__name__ == "XSDataInteger":
            self._latticeCharacter = latticeCharacter
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing constructor argument 'latticeCharacter' is not XSDataInteger but %s" % self._latticeCharacter.__class__.__name__
            raise BaseException(strMessage)
        if bravaisLattice is None:
            self._bravaisLattice = None
        elif bravaisLattice.__class__.__name__ == "XSDataString":
            self._bravaisLattice = bravaisLattice
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing constructor argument 'bravaisLattice' is not XSDataString but %s" % self._bravaisLattice.__class__.__name__
            raise BaseException(strMessage)
        if spaceGroup is None:
            self._spaceGroup = None
        elif spaceGroup.__class__.__name__ == "XSDataString":
            self._spaceGroup = spaceGroup
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing constructor argument 'spaceGroup' is not XSDataString but %s" % self._spaceGroup.__class__.__name__
            raise BaseException(strMessage)
        if spaceGroupNumber is None:
            self._spaceGroupNumber = None
        elif spaceGroupNumber.__class__.__name__ == "XSDataInteger":
            self._spaceGroupNumber = spaceGroupNumber
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing constructor argument 'spaceGroupNumber' is not XSDataInteger but %s" % self._spaceGroupNumber.__class__.__name__
            raise BaseException(strMessage)
        if qualityOfFit is None:
            self._qualityOfFit = None
        elif qualityOfFit.__class__.__name__ == "XSDataFloat":
            self._qualityOfFit = qualityOfFit
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing constructor argument 'qualityOfFit' is not XSDataFloat but %s" % self._qualityOfFit.__class__.__name__
            raise BaseException(strMessage)
        if unitCell is None:
            self._unitCell = None
        elif unitCell.__class__.__name__ == "XSDataXDSCell":
            self._unitCell = unitCell
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing constructor argument 'unitCell' is not XSDataXDSCell but %s" % self._unitCell.__class__.__name__
            raise BaseException(strMessage)
        if beamCentreX is None:
            self._beamCentreX = None
        elif beamCentreX.__class__.__name__ == "XSDataFloat":
            self._beamCentreX = beamCentreX
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing constructor argument 'beamCentreX' is not XSDataFloat but %s" % self._beamCentreX.__class__.__name__
            raise BaseException(strMessage)
        if beamCentreY is None:
            self._beamCentreY = None
        elif beamCentreY.__class__.__name__ == "XSDataFloat":
            self._beamCentreY = beamCentreY
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing constructor argument 'beamCentreY' is not XSDataFloat but %s" % self._beamCentreY.__class__.__name__
            raise BaseException(strMessage)
        if distance is None:
            self._distance = None
        elif distance.__class__.__name__ == "XSDataLength":
            self._distance = distance
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing constructor argument 'distance' is not XSDataLength but %s" % self._distance.__class__.__name__
            raise BaseException(strMessage)
        if mosaicity is None:
            self._mosaicity = None
        elif mosaicity.__class__.__name__ == "XSDataAngle":
            self._mosaicity = mosaicity
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing constructor argument 'mosaicity' is not XSDataAngle but %s" % self._mosaicity.__class__.__name__
            raise BaseException(strMessage)
        if pathToLogFile is None:
            self._pathToLogFile = None
        elif pathToLogFile.__class__.__name__ == "XSDataFile":
            self._pathToLogFile = pathToLogFile
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing constructor argument 'pathToLogFile' is not XSDataFile but %s" % self._pathToLogFile.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'latticeCharacter' attribute
    def getLatticeCharacter(self): return self._latticeCharacter
    def setLatticeCharacter(self, latticeCharacter):
        if latticeCharacter is None:
            self._latticeCharacter = None
        elif latticeCharacter.__class__.__name__ == "XSDataInteger":
            self._latticeCharacter = latticeCharacter
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing.setLatticeCharacter argument is not XSDataInteger but %s" % latticeCharacter.__class__.__name__
            raise BaseException(strMessage)
    def delLatticeCharacter(self): self._latticeCharacter = None
    latticeCharacter = property(getLatticeCharacter, setLatticeCharacter, delLatticeCharacter, "Property for latticeCharacter")
    # Methods and properties for the 'bravaisLattice' attribute
    def getBravaisLattice(self): return self._bravaisLattice
    def setBravaisLattice(self, bravaisLattice):
        if bravaisLattice is None:
            self._bravaisLattice = None
        elif bravaisLattice.__class__.__name__ == "XSDataString":
            self._bravaisLattice = bravaisLattice
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing.setBravaisLattice argument is not XSDataString but %s" % bravaisLattice.__class__.__name__
            raise BaseException(strMessage)
    def delBravaisLattice(self): self._bravaisLattice = None
    bravaisLattice = property(getBravaisLattice, setBravaisLattice, delBravaisLattice, "Property for bravaisLattice")
    # Methods and properties for the 'spaceGroup' attribute
    def getSpaceGroup(self): return self._spaceGroup
    def setSpaceGroup(self, spaceGroup):
        if spaceGroup is None:
            self._spaceGroup = None
        elif spaceGroup.__class__.__name__ == "XSDataString":
            self._spaceGroup = spaceGroup
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing.setSpaceGroup argument is not XSDataString but %s" % spaceGroup.__class__.__name__
            raise BaseException(strMessage)
    def delSpaceGroup(self): self._spaceGroup = None
    spaceGroup = property(getSpaceGroup, setSpaceGroup, delSpaceGroup, "Property for spaceGroup")
    # Methods and properties for the 'spaceGroupNumber' attribute
    def getSpaceGroupNumber(self): return self._spaceGroupNumber
    def setSpaceGroupNumber(self, spaceGroupNumber):
        if spaceGroupNumber is None:
            self._spaceGroupNumber = None
        elif spaceGroupNumber.__class__.__name__ == "XSDataInteger":
            self._spaceGroupNumber = spaceGroupNumber
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing.setSpaceGroupNumber argument is not XSDataInteger but %s" % spaceGroupNumber.__class__.__name__
            raise BaseException(strMessage)
    def delSpaceGroupNumber(self): self._spaceGroupNumber = None
    spaceGroupNumber = property(getSpaceGroupNumber, setSpaceGroupNumber, delSpaceGroupNumber, "Property for spaceGroupNumber")
    # Methods and properties for the 'qualityOfFit' attribute
    def getQualityOfFit(self): return self._qualityOfFit
    def setQualityOfFit(self, qualityOfFit):
        if qualityOfFit is None:
            self._qualityOfFit = None
        elif qualityOfFit.__class__.__name__ == "XSDataFloat":
            self._qualityOfFit = qualityOfFit
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing.setQualityOfFit argument is not XSDataFloat but %s" % qualityOfFit.__class__.__name__
            raise BaseException(strMessage)
    def delQualityOfFit(self): self._qualityOfFit = None
    qualityOfFit = property(getQualityOfFit, setQualityOfFit, delQualityOfFit, "Property for qualityOfFit")
    # Methods and properties for the 'unitCell' attribute
    def getUnitCell(self): return self._unitCell
    def setUnitCell(self, unitCell):
        if unitCell is None:
            self._unitCell = None
        elif unitCell.__class__.__name__ == "XSDataXDSCell":
            self._unitCell = unitCell
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing.setUnitCell argument is not XSDataXDSCell but %s" % unitCell.__class__.__name__
            raise BaseException(strMessage)
    def delUnitCell(self): self._unitCell = None
    unitCell = property(getUnitCell, setUnitCell, delUnitCell, "Property for unitCell")
    # Methods and properties for the 'beamCentreX' attribute
    def getBeamCentreX(self): return self._beamCentreX
    def setBeamCentreX(self, beamCentreX):
        if beamCentreX is None:
            self._beamCentreX = None
        elif beamCentreX.__class__.__name__ == "XSDataFloat":
            self._beamCentreX = beamCentreX
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing.setBeamCentreX argument is not XSDataFloat but %s" % beamCentreX.__class__.__name__
            raise BaseException(strMessage)
    def delBeamCentreX(self): self._beamCentreX = None
    beamCentreX = property(getBeamCentreX, setBeamCentreX, delBeamCentreX, "Property for beamCentreX")
    # Methods and properties for the 'beamCentreY' attribute
    def getBeamCentreY(self): return self._beamCentreY
    def setBeamCentreY(self, beamCentreY):
        if beamCentreY is None:
            self._beamCentreY = None
        elif beamCentreY.__class__.__name__ == "XSDataFloat":
            self._beamCentreY = beamCentreY
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing.setBeamCentreY argument is not XSDataFloat but %s" % beamCentreY.__class__.__name__
            raise BaseException(strMessage)
    def delBeamCentreY(self): self._beamCentreY = None
    beamCentreY = property(getBeamCentreY, setBeamCentreY, delBeamCentreY, "Property for beamCentreY")
    # Methods and properties for the 'distance' attribute
    def getDistance(self): return self._distance
    def setDistance(self, distance):
        if distance is None:
            self._distance = None
        elif distance.__class__.__name__ == "XSDataLength":
            self._distance = distance
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing.setDistance argument is not XSDataLength but %s" % distance.__class__.__name__
            raise BaseException(strMessage)
    def delDistance(self): self._distance = None
    distance = property(getDistance, setDistance, delDistance, "Property for distance")
    # Methods and properties for the 'mosaicity' attribute
    def getMosaicity(self): return self._mosaicity
    def setMosaicity(self, mosaicity):
        if mosaicity is None:
            self._mosaicity = None
        elif mosaicity.__class__.__name__ == "XSDataAngle":
            self._mosaicity = mosaicity
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing.setMosaicity argument is not XSDataAngle but %s" % mosaicity.__class__.__name__
            raise BaseException(strMessage)
    def delMosaicity(self): self._mosaicity = None
    mosaicity = property(getMosaicity, setMosaicity, delMosaicity, "Property for mosaicity")
    # Methods and properties for the 'pathToLogFile' attribute
    def getPathToLogFile(self): return self._pathToLogFile
    def setPathToLogFile(self, pathToLogFile):
        if pathToLogFile is None:
            self._pathToLogFile = None
        elif pathToLogFile.__class__.__name__ == "XSDataFile":
            self._pathToLogFile = pathToLogFile
        else:
            strMessage = "ERROR! XSDataResultXDSIndexing.setPathToLogFile argument is not XSDataFile but %s" % pathToLogFile.__class__.__name__
            raise BaseException(strMessage)
    def delPathToLogFile(self): self._pathToLogFile = None
    pathToLogFile = property(getPathToLogFile, setPathToLogFile, delPathToLogFile, "Property for pathToLogFile")
    def export(self, outfile, level, name_='XSDataResultXDSIndexing'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultXDSIndexing'):
        XSDataResultXDS.exportChildren(self, outfile, level, name_)
        if self._latticeCharacter is not None:
            self.latticeCharacter.export(outfile, level, name_='latticeCharacter')
        if self._bravaisLattice is not None:
            self.bravaisLattice.export(outfile, level, name_='bravaisLattice')
        if self._spaceGroup is not None:
            self.spaceGroup.export(outfile, level, name_='spaceGroup')
        if self._spaceGroupNumber is not None:
            self.spaceGroupNumber.export(outfile, level, name_='spaceGroupNumber')
        if self._qualityOfFit is not None:
            self.qualityOfFit.export(outfile, level, name_='qualityOfFit')
        if self._unitCell is not None:
            self.unitCell.export(outfile, level, name_='unitCell')
        if self._beamCentreX is not None:
            self.beamCentreX.export(outfile, level, name_='beamCentreX')
        if self._beamCentreY is not None:
            self.beamCentreY.export(outfile, level, name_='beamCentreY')
        if self._distance is not None:
            self.distance.export(outfile, level, name_='distance')
        if self._mosaicity is not None:
            self.mosaicity.export(outfile, level, name_='mosaicity')
        if self._pathToLogFile is not None:
            self.pathToLogFile.export(outfile, level, name_='pathToLogFile')
        else:
            warnEmptyAttribute("pathToLogFile", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'latticeCharacter':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setLatticeCharacter(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bravaisLattice':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setBravaisLattice(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spaceGroup':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSpaceGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spaceGroupNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSpaceGroupNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'qualityOfFit':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setQualityOfFit(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell':
            obj_ = XSDataXDSCell()
            obj_.build(child_)
            self.setUnitCell(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamCentreX':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setBeamCentreX(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamCentreY':
            obj_ = XSDataFloat()
            obj_.build(child_)
            self.setBeamCentreY(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'distance':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setDistance(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mosaicity':
            obj_ = XSDataAngle()
            obj_.build(child_)
            self.setMosaicity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pathToLogFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPathToLogFile(obj_)
        XSDataResultXDS.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultXDSIndexing" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultXDSIndexing' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultXDSIndexing is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultXDSIndexing.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultXDSIndexing()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultXDSIndexing" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultXDSIndexing()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultXDSIndexing


class XSDataResultXDSIntegration(XSDataResultXDS):
    def __init__(self, status=None, filePaths=None, xdsAsciiHkl=None, bkgpixCbf=None, correctLp=None):
        XSDataResultXDS.__init__(self, status, filePaths)
        if correctLp is None:
            self._correctLp = None
        elif correctLp.__class__.__name__ == "XSDataFile":
            self._correctLp = correctLp
        else:
            strMessage = "ERROR! XSDataResultXDSIntegration constructor argument 'correctLp' is not XSDataFile but %s" % self._correctLp.__class__.__name__
            raise BaseException(strMessage)
        if bkgpixCbf is None:
            self._bkgpixCbf = None
        elif bkgpixCbf.__class__.__name__ == "XSDataFile":
            self._bkgpixCbf = bkgpixCbf
        else:
            strMessage = "ERROR! XSDataResultXDSIntegration constructor argument 'bkgpixCbf' is not XSDataFile but %s" % self._bkgpixCbf.__class__.__name__
            raise BaseException(strMessage)
        if xdsAsciiHkl is None:
            self._xdsAsciiHkl = None
        elif xdsAsciiHkl.__class__.__name__ == "XSDataFile":
            self._xdsAsciiHkl = xdsAsciiHkl
        else:
            strMessage = "ERROR! XSDataResultXDSIntegration constructor argument 'xdsAsciiHkl' is not XSDataFile but %s" % self._xdsAsciiHkl.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'correctLp' attribute
    def getCorrectLp(self): return self._correctLp
    def setCorrectLp(self, correctLp):
        if correctLp is None:
            self._correctLp = None
        elif correctLp.__class__.__name__ == "XSDataFile":
            self._correctLp = correctLp
        else:
            strMessage = "ERROR! XSDataResultXDSIntegration.setCorrectLp argument is not XSDataFile but %s" % correctLp.__class__.__name__
            raise BaseException(strMessage)
    def delCorrectLp(self): self._correctLp = None
    correctLp = property(getCorrectLp, setCorrectLp, delCorrectLp, "Property for correctLp")
    # Methods and properties for the 'bkgpixCbf' attribute
    def getBkgpixCbf(self): return self._bkgpixCbf
    def setBkgpixCbf(self, bkgpixCbf):
        if bkgpixCbf is None:
            self._bkgpixCbf = None
        elif bkgpixCbf.__class__.__name__ == "XSDataFile":
            self._bkgpixCbf = bkgpixCbf
        else:
            strMessage = "ERROR! XSDataResultXDSIntegration.setBkgpixCbf argument is not XSDataFile but %s" % bkgpixCbf.__class__.__name__
            raise BaseException(strMessage)
    def delBkgpixCbf(self): self._bkgpixCbf = None
    bkgpixCbf = property(getBkgpixCbf, setBkgpixCbf, delBkgpixCbf, "Property for bkgpixCbf")
    # Methods and properties for the 'xdsAsciiHkl' attribute
    def getXdsAsciiHkl(self): return self._xdsAsciiHkl
    def setXdsAsciiHkl(self, xdsAsciiHkl):
        if xdsAsciiHkl is None:
            self._xdsAsciiHkl = None
        elif xdsAsciiHkl.__class__.__name__ == "XSDataFile":
            self._xdsAsciiHkl = xdsAsciiHkl
        else:
            strMessage = "ERROR! XSDataResultXDSIntegration.setXdsAsciiHkl argument is not XSDataFile but %s" % xdsAsciiHkl.__class__.__name__
            raise BaseException(strMessage)
    def delXdsAsciiHkl(self): self._xdsAsciiHkl = None
    xdsAsciiHkl = property(getXdsAsciiHkl, setXdsAsciiHkl, delXdsAsciiHkl, "Property for xdsAsciiHkl")
    def export(self, outfile, level, name_='XSDataResultXDSIntegration'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultXDSIntegration'):
        XSDataResultXDS.exportChildren(self, outfile, level, name_)
        if self._correctLp is not None:
            self.correctLp.export(outfile, level, name_='correctLp')
        if self._bkgpixCbf is not None:
            self.bkgpixCbf.export(outfile, level, name_='bkgpixCbf')
        if self._xdsAsciiHkl is not None:
            self.xdsAsciiHkl.export(outfile, level, name_='xdsAsciiHkl')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'correctLp':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setCorrectLp(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bkgpixCbf':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setBkgpixCbf(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'xdsAsciiHkl':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setXdsAsciiHkl(obj_)
        XSDataResultXDS.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultXDSIntegration" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultXDSIntegration' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultXDSIntegration is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultXDSIntegration.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultXDSIntegration()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultXDSIntegration" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultXDSIntegration()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultXDSIntegration



# End of data representation classes.


