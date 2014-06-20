#!/usr/bin/env python

#
# Generated Fri Jun 20 02:25::00 2014 by EDGenerateDS.
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
}

try:
    from XSDataCommon import XSDataBoolean
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataInteger
    from XSDataCommon import XSDataResult
    from XSDataCommon import XSDataTime
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
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataTime




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



class XSDataInputMXWaitFile(XSDataInput):
    def __init__(self, configuration=None, timeOut=None, expectedSize=None, expectedFile=None):
        XSDataInput.__init__(self, configuration)
        if expectedFile is None:
            self._expectedFile = None
        elif expectedFile.__class__.__name__ == "XSDataFile":
            self._expectedFile = expectedFile
        else:
            strMessage = "ERROR! XSDataInputMXWaitFile constructor argument 'expectedFile' is not XSDataFile but %s" % self._expectedFile.__class__.__name__
            raise BaseException(strMessage)
        if expectedSize is None:
            self._expectedSize = None
        elif expectedSize.__class__.__name__ == "XSDataInteger":
            self._expectedSize = expectedSize
        else:
            strMessage = "ERROR! XSDataInputMXWaitFile constructor argument 'expectedSize' is not XSDataInteger but %s" % self._expectedSize.__class__.__name__
            raise BaseException(strMessage)
        if timeOut is None:
            self._timeOut = None
        elif timeOut.__class__.__name__ == "XSDataTime":
            self._timeOut = timeOut
        else:
            strMessage = "ERROR! XSDataInputMXWaitFile constructor argument 'timeOut' is not XSDataTime but %s" % self._timeOut.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'expectedFile' attribute
    def getExpectedFile(self): return self._expectedFile
    def setExpectedFile(self, expectedFile):
        if expectedFile is None:
            self._expectedFile = None
        elif expectedFile.__class__.__name__ == "XSDataFile":
            self._expectedFile = expectedFile
        else:
            strMessage = "ERROR! XSDataInputMXWaitFile.setExpectedFile argument is not XSDataFile but %s" % expectedFile.__class__.__name__
            raise BaseException(strMessage)
    def delExpectedFile(self): self._expectedFile = None
    expectedFile = property(getExpectedFile, setExpectedFile, delExpectedFile, "Property for expectedFile")
    # Methods and properties for the 'expectedSize' attribute
    def getExpectedSize(self): return self._expectedSize
    def setExpectedSize(self, expectedSize):
        if expectedSize is None:
            self._expectedSize = None
        elif expectedSize.__class__.__name__ == "XSDataInteger":
            self._expectedSize = expectedSize
        else:
            strMessage = "ERROR! XSDataInputMXWaitFile.setExpectedSize argument is not XSDataInteger but %s" % expectedSize.__class__.__name__
            raise BaseException(strMessage)
    def delExpectedSize(self): self._expectedSize = None
    expectedSize = property(getExpectedSize, setExpectedSize, delExpectedSize, "Property for expectedSize")
    # Methods and properties for the 'timeOut' attribute
    def getTimeOut(self): return self._timeOut
    def setTimeOut(self, timeOut):
        if timeOut is None:
            self._timeOut = None
        elif timeOut.__class__.__name__ == "XSDataTime":
            self._timeOut = timeOut
        else:
            strMessage = "ERROR! XSDataInputMXWaitFile.setTimeOut argument is not XSDataTime but %s" % timeOut.__class__.__name__
            raise BaseException(strMessage)
    def delTimeOut(self): self._timeOut = None
    timeOut = property(getTimeOut, setTimeOut, delTimeOut, "Property for timeOut")
    def export(self, outfile, level, name_='XSDataInputMXWaitFile'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputMXWaitFile'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._expectedFile is not None:
            self.expectedFile.export(outfile, level, name_='expectedFile')
        else:
            warnEmptyAttribute("expectedFile", "XSDataFile")
        if self._expectedSize is not None:
            self.expectedSize.export(outfile, level, name_='expectedSize')
        else:
            warnEmptyAttribute("expectedSize", "XSDataInteger")
        if self._timeOut is not None:
            self.timeOut.export(outfile, level, name_='timeOut')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'expectedFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setExpectedFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'expectedSize':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setExpectedSize(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'timeOut':
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setTimeOut(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputMXWaitFile" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputMXWaitFile' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputMXWaitFile is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputMXWaitFile.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputMXWaitFile()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputMXWaitFile" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputMXWaitFile()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputMXWaitFile


class XSDataResultMXWaitFile(XSDataResult):
    def __init__(self, status=None, timedOut=None, actualSize=None, actualFile=None):
        XSDataResult.__init__(self, status)
        if actualFile is None:
            self._actualFile = None
        elif actualFile.__class__.__name__ == "XSDataFile":
            self._actualFile = actualFile
        else:
            strMessage = "ERROR! XSDataResultMXWaitFile constructor argument 'actualFile' is not XSDataFile but %s" % self._actualFile.__class__.__name__
            raise BaseException(strMessage)
        if actualSize is None:
            self._actualSize = None
        elif actualSize.__class__.__name__ == "XSDataInteger":
            self._actualSize = actualSize
        else:
            strMessage = "ERROR! XSDataResultMXWaitFile constructor argument 'actualSize' is not XSDataInteger but %s" % self._actualSize.__class__.__name__
            raise BaseException(strMessage)
        if timedOut is None:
            self._timedOut = None
        elif timedOut.__class__.__name__ == "XSDataBoolean":
            self._timedOut = timedOut
        else:
            strMessage = "ERROR! XSDataResultMXWaitFile constructor argument 'timedOut' is not XSDataBoolean but %s" % self._timedOut.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'actualFile' attribute
    def getActualFile(self): return self._actualFile
    def setActualFile(self, actualFile):
        if actualFile is None:
            self._actualFile = None
        elif actualFile.__class__.__name__ == "XSDataFile":
            self._actualFile = actualFile
        else:
            strMessage = "ERROR! XSDataResultMXWaitFile.setActualFile argument is not XSDataFile but %s" % actualFile.__class__.__name__
            raise BaseException(strMessage)
    def delActualFile(self): self._actualFile = None
    actualFile = property(getActualFile, setActualFile, delActualFile, "Property for actualFile")
    # Methods and properties for the 'actualSize' attribute
    def getActualSize(self): return self._actualSize
    def setActualSize(self, actualSize):
        if actualSize is None:
            self._actualSize = None
        elif actualSize.__class__.__name__ == "XSDataInteger":
            self._actualSize = actualSize
        else:
            strMessage = "ERROR! XSDataResultMXWaitFile.setActualSize argument is not XSDataInteger but %s" % actualSize.__class__.__name__
            raise BaseException(strMessage)
    def delActualSize(self): self._actualSize = None
    actualSize = property(getActualSize, setActualSize, delActualSize, "Property for actualSize")
    # Methods and properties for the 'timedOut' attribute
    def getTimedOut(self): return self._timedOut
    def setTimedOut(self, timedOut):
        if timedOut is None:
            self._timedOut = None
        elif timedOut.__class__.__name__ == "XSDataBoolean":
            self._timedOut = timedOut
        else:
            strMessage = "ERROR! XSDataResultMXWaitFile.setTimedOut argument is not XSDataBoolean but %s" % timedOut.__class__.__name__
            raise BaseException(strMessage)
    def delTimedOut(self): self._timedOut = None
    timedOut = property(getTimedOut, setTimedOut, delTimedOut, "Property for timedOut")
    def export(self, outfile, level, name_='XSDataResultMXWaitFile'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultMXWaitFile'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._actualFile is not None:
            self.actualFile.export(outfile, level, name_='actualFile')
        if self._actualSize is not None:
            self.actualSize.export(outfile, level, name_='actualSize')
        if self._timedOut is not None:
            self.timedOut.export(outfile, level, name_='timedOut')
        else:
            warnEmptyAttribute("timedOut", "XSDataBoolean")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'actualFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setActualFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'actualSize':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setActualSize(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'timedOut':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setTimedOut(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultMXWaitFile" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultMXWaitFile' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultMXWaitFile is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultMXWaitFile.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultMXWaitFile()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultMXWaitFile" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultMXWaitFile()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultMXWaitFile



# End of data representation classes.


