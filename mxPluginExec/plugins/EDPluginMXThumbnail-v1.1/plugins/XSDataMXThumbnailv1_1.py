#!/usr/bin/env python

#
# Generated Tue May 19 09:23::46 2015 by EDGenerateDS.
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
}

try:
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataInteger
    from XSDataCommon import XSDataResult
    from XSDataCommon import XSDataString
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
from XSDataCommon import XSDataString




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



class XSDataInputMXThumbnail(XSDataInput):
    def __init__(self, configuration=None, format=None, outputPath=None, width=None, height=None, image=None):
        XSDataInput.__init__(self, configuration)
        if image is None:
            self._image = None
        elif image.__class__.__name__ == "XSDataFile":
            self._image = image
        else:
            strMessage = "ERROR! XSDataInputMXThumbnail constructor argument 'image' is not XSDataFile but %s" % self._image.__class__.__name__
            raise BaseException(strMessage)
        if height is None:
            self._height = None
        elif height.__class__.__name__ == "XSDataInteger":
            self._height = height
        else:
            strMessage = "ERROR! XSDataInputMXThumbnail constructor argument 'height' is not XSDataInteger but %s" % self._height.__class__.__name__
            raise BaseException(strMessage)
        if width is None:
            self._width = None
        elif width.__class__.__name__ == "XSDataInteger":
            self._width = width
        else:
            strMessage = "ERROR! XSDataInputMXThumbnail constructor argument 'width' is not XSDataInteger but %s" % self._width.__class__.__name__
            raise BaseException(strMessage)
        if outputPath is None:
            self._outputPath = None
        elif outputPath.__class__.__name__ == "XSDataFile":
            self._outputPath = outputPath
        else:
            strMessage = "ERROR! XSDataInputMXThumbnail constructor argument 'outputPath' is not XSDataFile but %s" % self._outputPath.__class__.__name__
            raise BaseException(strMessage)
        if format is None:
            self._format = None
        elif format.__class__.__name__ == "XSDataString":
            self._format = format
        else:
            strMessage = "ERROR! XSDataInputMXThumbnail constructor argument 'format' is not XSDataString but %s" % self._format.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'image' attribute
    def getImage(self): return self._image
    def setImage(self, image):
        if image is None:
            self._image = None
        elif image.__class__.__name__ == "XSDataFile":
            self._image = image
        else:
            strMessage = "ERROR! XSDataInputMXThumbnail.setImage argument is not XSDataFile but %s" % image.__class__.__name__
            raise BaseException(strMessage)
    def delImage(self): self._image = None
    image = property(getImage, setImage, delImage, "Property for image")
    # Methods and properties for the 'height' attribute
    def getHeight(self): return self._height
    def setHeight(self, height):
        if height is None:
            self._height = None
        elif height.__class__.__name__ == "XSDataInteger":
            self._height = height
        else:
            strMessage = "ERROR! XSDataInputMXThumbnail.setHeight argument is not XSDataInteger but %s" % height.__class__.__name__
            raise BaseException(strMessage)
    def delHeight(self): self._height = None
    height = property(getHeight, setHeight, delHeight, "Property for height")
    # Methods and properties for the 'width' attribute
    def getWidth(self): return self._width
    def setWidth(self, width):
        if width is None:
            self._width = None
        elif width.__class__.__name__ == "XSDataInteger":
            self._width = width
        else:
            strMessage = "ERROR! XSDataInputMXThumbnail.setWidth argument is not XSDataInteger but %s" % width.__class__.__name__
            raise BaseException(strMessage)
    def delWidth(self): self._width = None
    width = property(getWidth, setWidth, delWidth, "Property for width")
    # Methods and properties for the 'outputPath' attribute
    def getOutputPath(self): return self._outputPath
    def setOutputPath(self, outputPath):
        if outputPath is None:
            self._outputPath = None
        elif outputPath.__class__.__name__ == "XSDataFile":
            self._outputPath = outputPath
        else:
            strMessage = "ERROR! XSDataInputMXThumbnail.setOutputPath argument is not XSDataFile but %s" % outputPath.__class__.__name__
            raise BaseException(strMessage)
    def delOutputPath(self): self._outputPath = None
    outputPath = property(getOutputPath, setOutputPath, delOutputPath, "Property for outputPath")
    # Methods and properties for the 'format' attribute
    def getFormat(self): return self._format
    def setFormat(self, format):
        if format is None:
            self._format = None
        elif format.__class__.__name__ == "XSDataString":
            self._format = format
        else:
            strMessage = "ERROR! XSDataInputMXThumbnail.setFormat argument is not XSDataString but %s" % format.__class__.__name__
            raise BaseException(strMessage)
    def delFormat(self): self._format = None
    format = property(getFormat, setFormat, delFormat, "Property for format")
    def export(self, outfile, level, name_='XSDataInputMXThumbnail'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputMXThumbnail'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._image is not None:
            self.image.export(outfile, level, name_='image')
        else:
            warnEmptyAttribute("image", "XSDataFile")
        if self._height is not None:
            self.height.export(outfile, level, name_='height')
        if self._width is not None:
            self.width.export(outfile, level, name_='width')
        if self._outputPath is not None:
            self.outputPath.export(outfile, level, name_='outputPath')
        if self._format is not None:
            self.format.export(outfile, level, name_='format')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'height':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setHeight(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'width':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setWidth(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputPath':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutputPath(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'format':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setFormat(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputMXThumbnail" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputMXThumbnail' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputMXThumbnail is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputMXThumbnail.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputMXThumbnail()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputMXThumbnail" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputMXThumbnail()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputMXThumbnail


class XSDataResultMXThumbnail(XSDataResult):
    def __init__(self, status=None, thumbnail=None):
        XSDataResult.__init__(self, status)
        if thumbnail is None:
            self._thumbnail = None
        elif thumbnail.__class__.__name__ == "XSDataFile":
            self._thumbnail = thumbnail
        else:
            strMessage = "ERROR! XSDataResultMXThumbnail constructor argument 'thumbnail' is not XSDataFile but %s" % self._thumbnail.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'thumbnail' attribute
    def getThumbnail(self): return self._thumbnail
    def setThumbnail(self, thumbnail):
        if thumbnail is None:
            self._thumbnail = None
        elif thumbnail.__class__.__name__ == "XSDataFile":
            self._thumbnail = thumbnail
        else:
            strMessage = "ERROR! XSDataResultMXThumbnail.setThumbnail argument is not XSDataFile but %s" % thumbnail.__class__.__name__
            raise BaseException(strMessage)
    def delThumbnail(self): self._thumbnail = None
    thumbnail = property(getThumbnail, setThumbnail, delThumbnail, "Property for thumbnail")
    def export(self, outfile, level, name_='XSDataResultMXThumbnail'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultMXThumbnail'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._thumbnail is not None:
            self.thumbnail.export(outfile, level, name_='thumbnail')
        else:
            warnEmptyAttribute("thumbnail", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'thumbnail':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setThumbnail(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultMXThumbnail" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultMXThumbnail' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultMXThumbnail is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultMXThumbnail.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultMXThumbnail()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultMXThumbnail" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultMXThumbnail()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultMXThumbnail



# End of data representation classes.


