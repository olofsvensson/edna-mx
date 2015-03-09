#!/usr/bin/env python

#
# Generated Thu Mar 5 03:37::02 2015 by EDGenerateDS.
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



class XSDataInputControlH5ToCBF(XSDataInput):
    def __init__(self, configuration=None, hdf5File=None, imageNumber=None):
        XSDataInput.__init__(self, configuration)
        if imageNumber is None:
            self._imageNumber = None
        elif imageNumber.__class__.__name__ == "XSDataInteger":
            self._imageNumber = imageNumber
        else:
            strMessage = "ERROR! XSDataInputControlH5ToCBF constructor argument 'imageNumber' is not XSDataInteger but %s" % self._imageNumber.__class__.__name__
            raise BaseException(strMessage)
        if hdf5File is None:
            self._hdf5File = None
        elif hdf5File.__class__.__name__ == "XSDataFile":
            self._hdf5File = hdf5File
        else:
            strMessage = "ERROR! XSDataInputControlH5ToCBF constructor argument 'hdf5File' is not XSDataFile but %s" % self._hdf5File.__class__.__name__
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
        if self._hdf5File is not None:
            self.hdf5File.export(outfile, level, name_='hdf5File')
        else:
            warnEmptyAttribute("hdf5File", "XSDataFile")
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
            nodeName_ == 'hdf5File':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setHdf5File(obj_)
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
    def __init__(self, status=None, outputCBFFile=None):
        XSDataResult.__init__(self, status)
        if outputCBFFile is None:
            self._outputCBFFile = None
        elif outputCBFFile.__class__.__name__ == "XSDataFile":
            self._outputCBFFile = outputCBFFile
        else:
            strMessage = "ERROR! XSDataResultControlH5ToCBF constructor argument 'outputCBFFile' is not XSDataFile but %s" % self._outputCBFFile.__class__.__name__
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


