#!/usr/bin/env python

#
# Generated Thu Sep 1 04:30::04 2016 by EDGenerateDS.
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



class XSDataInputH5ToCBF(XSDataInput):
    def __init__(self, configuration=None, endImageNumber=None, startImageNumber=None, forcedOutputImageNumber=None, forcedOutputDirectory=None, hdf5File=None, hdf5ImageNumber=None, imageNumber=None):
        XSDataInput.__init__(self, configuration)
        if imageNumber is None:
            self._imageNumber = None
        elif imageNumber.__class__.__name__ == "XSDataInteger":
            self._imageNumber = imageNumber
        else:
            strMessage = "ERROR! XSDataInputH5ToCBF constructor argument 'imageNumber' is not XSDataInteger but %s" % self._imageNumber.__class__.__name__
            raise BaseException(strMessage)
        if hdf5ImageNumber is None:
            self._hdf5ImageNumber = None
        elif hdf5ImageNumber.__class__.__name__ == "XSDataInteger":
            self._hdf5ImageNumber = hdf5ImageNumber
        else:
            strMessage = "ERROR! XSDataInputH5ToCBF constructor argument 'hdf5ImageNumber' is not XSDataInteger but %s" % self._hdf5ImageNumber.__class__.__name__
            raise BaseException(strMessage)
        if hdf5File is None:
            self._hdf5File = None
        elif hdf5File.__class__.__name__ == "XSDataFile":
            self._hdf5File = hdf5File
        else:
            strMessage = "ERROR! XSDataInputH5ToCBF constructor argument 'hdf5File' is not XSDataFile but %s" % self._hdf5File.__class__.__name__
            raise BaseException(strMessage)
        if forcedOutputDirectory is None:
            self._forcedOutputDirectory = None
        elif forcedOutputDirectory.__class__.__name__ == "XSDataFile":
            self._forcedOutputDirectory = forcedOutputDirectory
        else:
            strMessage = "ERROR! XSDataInputH5ToCBF constructor argument 'forcedOutputDirectory' is not XSDataFile but %s" % self._forcedOutputDirectory.__class__.__name__
            raise BaseException(strMessage)
        if forcedOutputImageNumber is None:
            self._forcedOutputImageNumber = None
        elif forcedOutputImageNumber.__class__.__name__ == "XSDataInteger":
            self._forcedOutputImageNumber = forcedOutputImageNumber
        else:
            strMessage = "ERROR! XSDataInputH5ToCBF constructor argument 'forcedOutputImageNumber' is not XSDataInteger but %s" % self._forcedOutputImageNumber.__class__.__name__
            raise BaseException(strMessage)
        if startImageNumber is None:
            self._startImageNumber = None
        elif startImageNumber.__class__.__name__ == "XSDataInteger":
            self._startImageNumber = startImageNumber
        else:
            strMessage = "ERROR! XSDataInputH5ToCBF constructor argument 'startImageNumber' is not XSDataInteger but %s" % self._startImageNumber.__class__.__name__
            raise BaseException(strMessage)
        if endImageNumber is None:
            self._endImageNumber = None
        elif endImageNumber.__class__.__name__ == "XSDataInteger":
            self._endImageNumber = endImageNumber
        else:
            strMessage = "ERROR! XSDataInputH5ToCBF constructor argument 'endImageNumber' is not XSDataInteger but %s" % self._endImageNumber.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'imageNumber' attribute
    def getImageNumber(self): return self._imageNumber
    def setImageNumber(self, imageNumber):
        if imageNumber is None:
            self._imageNumber = None
        elif imageNumber.__class__.__name__ == "XSDataInteger":
            self._imageNumber = imageNumber
        else:
            strMessage = "ERROR! XSDataInputH5ToCBF.setImageNumber argument is not XSDataInteger but %s" % imageNumber.__class__.__name__
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
            strMessage = "ERROR! XSDataInputH5ToCBF.setHdf5ImageNumber argument is not XSDataInteger but %s" % hdf5ImageNumber.__class__.__name__
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
            strMessage = "ERROR! XSDataInputH5ToCBF.setHdf5File argument is not XSDataFile but %s" % hdf5File.__class__.__name__
            raise BaseException(strMessage)
    def delHdf5File(self): self._hdf5File = None
    hdf5File = property(getHdf5File, setHdf5File, delHdf5File, "Property for hdf5File")
    # Methods and properties for the 'forcedOutputDirectory' attribute
    def getForcedOutputDirectory(self): return self._forcedOutputDirectory
    def setForcedOutputDirectory(self, forcedOutputDirectory):
        if forcedOutputDirectory is None:
            self._forcedOutputDirectory = None
        elif forcedOutputDirectory.__class__.__name__ == "XSDataFile":
            self._forcedOutputDirectory = forcedOutputDirectory
        else:
            strMessage = "ERROR! XSDataInputH5ToCBF.setForcedOutputDirectory argument is not XSDataFile but %s" % forcedOutputDirectory.__class__.__name__
            raise BaseException(strMessage)
    def delForcedOutputDirectory(self): self._forcedOutputDirectory = None
    forcedOutputDirectory = property(getForcedOutputDirectory, setForcedOutputDirectory, delForcedOutputDirectory, "Property for forcedOutputDirectory")
    # Methods and properties for the 'forcedOutputImageNumber' attribute
    def getForcedOutputImageNumber(self): return self._forcedOutputImageNumber
    def setForcedOutputImageNumber(self, forcedOutputImageNumber):
        if forcedOutputImageNumber is None:
            self._forcedOutputImageNumber = None
        elif forcedOutputImageNumber.__class__.__name__ == "XSDataInteger":
            self._forcedOutputImageNumber = forcedOutputImageNumber
        else:
            strMessage = "ERROR! XSDataInputH5ToCBF.setForcedOutputImageNumber argument is not XSDataInteger but %s" % forcedOutputImageNumber.__class__.__name__
            raise BaseException(strMessage)
    def delForcedOutputImageNumber(self): self._forcedOutputImageNumber = None
    forcedOutputImageNumber = property(getForcedOutputImageNumber, setForcedOutputImageNumber, delForcedOutputImageNumber, "Property for forcedOutputImageNumber")
    # Methods and properties for the 'startImageNumber' attribute
    def getStartImageNumber(self): return self._startImageNumber
    def setStartImageNumber(self, startImageNumber):
        if startImageNumber is None:
            self._startImageNumber = None
        elif startImageNumber.__class__.__name__ == "XSDataInteger":
            self._startImageNumber = startImageNumber
        else:
            strMessage = "ERROR! XSDataInputH5ToCBF.setStartImageNumber argument is not XSDataInteger but %s" % startImageNumber.__class__.__name__
            raise BaseException(strMessage)
    def delStartImageNumber(self): self._startImageNumber = None
    startImageNumber = property(getStartImageNumber, setStartImageNumber, delStartImageNumber, "Property for startImageNumber")
    # Methods and properties for the 'endImageNumber' attribute
    def getEndImageNumber(self): return self._endImageNumber
    def setEndImageNumber(self, endImageNumber):
        if endImageNumber is None:
            self._endImageNumber = None
        elif endImageNumber.__class__.__name__ == "XSDataInteger":
            self._endImageNumber = endImageNumber
        else:
            strMessage = "ERROR! XSDataInputH5ToCBF.setEndImageNumber argument is not XSDataInteger but %s" % endImageNumber.__class__.__name__
            raise BaseException(strMessage)
    def delEndImageNumber(self): self._endImageNumber = None
    endImageNumber = property(getEndImageNumber, setEndImageNumber, delEndImageNumber, "Property for endImageNumber")
    def export(self, outfile, level, name_='XSDataInputH5ToCBF'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputH5ToCBF'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._imageNumber is not None:
            self.imageNumber.export(outfile, level, name_='imageNumber')
        if self._hdf5ImageNumber is not None:
            self.hdf5ImageNumber.export(outfile, level, name_='hdf5ImageNumber')
        if self._hdf5File is not None:
            self.hdf5File.export(outfile, level, name_='hdf5File')
        else:
            warnEmptyAttribute("hdf5File", "XSDataFile")
        if self._forcedOutputDirectory is not None:
            self.forcedOutputDirectory.export(outfile, level, name_='forcedOutputDirectory')
        if self._forcedOutputImageNumber is not None:
            self.forcedOutputImageNumber.export(outfile, level, name_='forcedOutputImageNumber')
        if self._startImageNumber is not None:
            self.startImageNumber.export(outfile, level, name_='startImageNumber')
        if self._endImageNumber is not None:
            self.endImageNumber.export(outfile, level, name_='endImageNumber')
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
            nodeName_ == 'forcedOutputDirectory':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setForcedOutputDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'forcedOutputImageNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setForcedOutputImageNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'startImageNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setStartImageNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'endImageNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setEndImageNumber(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputH5ToCBF" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputH5ToCBF' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputH5ToCBF is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputH5ToCBF.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputH5ToCBF()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputH5ToCBF" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputH5ToCBF()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputH5ToCBF


class XSDataResultH5ToCBF(XSDataResult):
    def __init__(self, status=None, outputCBFFileTemplate=None, outputCBFFile=None):
        XSDataResult.__init__(self, status)
        if outputCBFFile is None:
            self._outputCBFFile = None
        elif outputCBFFile.__class__.__name__ == "XSDataFile":
            self._outputCBFFile = outputCBFFile
        else:
            strMessage = "ERROR! XSDataResultH5ToCBF constructor argument 'outputCBFFile' is not XSDataFile but %s" % self._outputCBFFile.__class__.__name__
            raise BaseException(strMessage)
        if outputCBFFileTemplate is None:
            self._outputCBFFileTemplate = None
        elif outputCBFFileTemplate.__class__.__name__ == "XSDataFile":
            self._outputCBFFileTemplate = outputCBFFileTemplate
        else:
            strMessage = "ERROR! XSDataResultH5ToCBF constructor argument 'outputCBFFileTemplate' is not XSDataFile but %s" % self._outputCBFFileTemplate.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'outputCBFFile' attribute
    def getOutputCBFFile(self): return self._outputCBFFile
    def setOutputCBFFile(self, outputCBFFile):
        if outputCBFFile is None:
            self._outputCBFFile = None
        elif outputCBFFile.__class__.__name__ == "XSDataFile":
            self._outputCBFFile = outputCBFFile
        else:
            strMessage = "ERROR! XSDataResultH5ToCBF.setOutputCBFFile argument is not XSDataFile but %s" % outputCBFFile.__class__.__name__
            raise BaseException(strMessage)
    def delOutputCBFFile(self): self._outputCBFFile = None
    outputCBFFile = property(getOutputCBFFile, setOutputCBFFile, delOutputCBFFile, "Property for outputCBFFile")
    # Methods and properties for the 'outputCBFFileTemplate' attribute
    def getOutputCBFFileTemplate(self): return self._outputCBFFileTemplate
    def setOutputCBFFileTemplate(self, outputCBFFileTemplate):
        if outputCBFFileTemplate is None:
            self._outputCBFFileTemplate = None
        elif outputCBFFileTemplate.__class__.__name__ == "XSDataFile":
            self._outputCBFFileTemplate = outputCBFFileTemplate
        else:
            strMessage = "ERROR! XSDataResultH5ToCBF.setOutputCBFFileTemplate argument is not XSDataFile but %s" % outputCBFFileTemplate.__class__.__name__
            raise BaseException(strMessage)
    def delOutputCBFFileTemplate(self): self._outputCBFFileTemplate = None
    outputCBFFileTemplate = property(getOutputCBFFileTemplate, setOutputCBFFileTemplate, delOutputCBFFileTemplate, "Property for outputCBFFileTemplate")
    def export(self, outfile, level, name_='XSDataResultH5ToCBF'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultH5ToCBF'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._outputCBFFile is not None:
            self.outputCBFFile.export(outfile, level, name_='outputCBFFile')
        if self._outputCBFFileTemplate is not None:
            self.outputCBFFileTemplate.export(outfile, level, name_='outputCBFFileTemplate')
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
            nodeName_ == 'outputCBFFileTemplate':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutputCBFFileTemplate(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultH5ToCBF" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultH5ToCBF' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultH5ToCBF is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultH5ToCBF.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultH5ToCBF()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultH5ToCBF" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultH5ToCBF()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultH5ToCBF



# End of data representation classes.


