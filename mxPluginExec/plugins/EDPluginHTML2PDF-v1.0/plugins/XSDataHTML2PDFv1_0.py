#!/usr/bin/env python

#
# Generated Mon Mar 14 11:04::06 2016 by EDGenerateDS.
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
    from XSDataCommon import XSDataBoolean
    from XSDataCommon import XSDataString
    from XSDataCommon import XSDataFile
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
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
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



class XSDataInputHTML2PDF(XSDataInput):
    def __init__(self, configuration=None, lowQuality=None, paperSize=None, resultDirectory=None, htmlFile=None):
        XSDataInput.__init__(self, configuration)
        if htmlFile is None:
            self._htmlFile = []
        elif htmlFile.__class__.__name__ == "list":
            self._htmlFile = htmlFile
        else:
            strMessage = "ERROR! XSDataInputHTML2PDF constructor argument 'htmlFile' is not list but %s" % self._htmlFile.__class__.__name__
            raise BaseException(strMessage)
        if resultDirectory is None:
            self._resultDirectory = None
        elif resultDirectory.__class__.__name__ == "XSDataFile":
            self._resultDirectory = resultDirectory
        else:
            strMessage = "ERROR! XSDataInputHTML2PDF constructor argument 'resultDirectory' is not XSDataFile but %s" % self._resultDirectory.__class__.__name__
            raise BaseException(strMessage)
        if paperSize is None:
            self._paperSize = None
        elif paperSize.__class__.__name__ == "XSDataString":
            self._paperSize = paperSize
        else:
            strMessage = "ERROR! XSDataInputHTML2PDF constructor argument 'paperSize' is not XSDataString but %s" % self._paperSize.__class__.__name__
            raise BaseException(strMessage)
        if lowQuality is None:
            self._lowQuality = None
        elif lowQuality.__class__.__name__ == "XSDataBoolean":
            self._lowQuality = lowQuality
        else:
            strMessage = "ERROR! XSDataInputHTML2PDF constructor argument 'lowQuality' is not XSDataBoolean but %s" % self._lowQuality.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'htmlFile' attribute
    def getHtmlFile(self): return self._htmlFile
    def setHtmlFile(self, htmlFile):
        if htmlFile is None:
            self._htmlFile = []
        elif htmlFile.__class__.__name__ == "list":
            self._htmlFile = htmlFile
        else:
            strMessage = "ERROR! XSDataInputHTML2PDF.setHtmlFile argument is not list but %s" % htmlFile.__class__.__name__
            raise BaseException(strMessage)
    def delHtmlFile(self): self._htmlFile = None
    htmlFile = property(getHtmlFile, setHtmlFile, delHtmlFile, "Property for htmlFile")
    def addHtmlFile(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputHTML2PDF.addHtmlFile argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._htmlFile.append(value)
        else:
            strMessage = "ERROR! XSDataInputHTML2PDF.addHtmlFile argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertHtmlFile(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputHTML2PDF.insertHtmlFile argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputHTML2PDF.insertHtmlFile argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._htmlFile[index] = value
        else:
            strMessage = "ERROR! XSDataInputHTML2PDF.addHtmlFile argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'resultDirectory' attribute
    def getResultDirectory(self): return self._resultDirectory
    def setResultDirectory(self, resultDirectory):
        if resultDirectory is None:
            self._resultDirectory = None
        elif resultDirectory.__class__.__name__ == "XSDataFile":
            self._resultDirectory = resultDirectory
        else:
            strMessage = "ERROR! XSDataInputHTML2PDF.setResultDirectory argument is not XSDataFile but %s" % resultDirectory.__class__.__name__
            raise BaseException(strMessage)
    def delResultDirectory(self): self._resultDirectory = None
    resultDirectory = property(getResultDirectory, setResultDirectory, delResultDirectory, "Property for resultDirectory")
    # Methods and properties for the 'paperSize' attribute
    def getPaperSize(self): return self._paperSize
    def setPaperSize(self, paperSize):
        if paperSize is None:
            self._paperSize = None
        elif paperSize.__class__.__name__ == "XSDataString":
            self._paperSize = paperSize
        else:
            strMessage = "ERROR! XSDataInputHTML2PDF.setPaperSize argument is not XSDataString but %s" % paperSize.__class__.__name__
            raise BaseException(strMessage)
    def delPaperSize(self): self._paperSize = None
    paperSize = property(getPaperSize, setPaperSize, delPaperSize, "Property for paperSize")
    # Methods and properties for the 'lowQuality' attribute
    def getLowQuality(self): return self._lowQuality
    def setLowQuality(self, lowQuality):
        if lowQuality is None:
            self._lowQuality = None
        elif lowQuality.__class__.__name__ == "XSDataBoolean":
            self._lowQuality = lowQuality
        else:
            strMessage = "ERROR! XSDataInputHTML2PDF.setLowQuality argument is not XSDataBoolean but %s" % lowQuality.__class__.__name__
            raise BaseException(strMessage)
    def delLowQuality(self): self._lowQuality = None
    lowQuality = property(getLowQuality, setLowQuality, delLowQuality, "Property for lowQuality")
    def export(self, outfile, level, name_='XSDataInputHTML2PDF'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputHTML2PDF'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for htmlFile_ in self.getHtmlFile():
            htmlFile_.export(outfile, level, name_='htmlFile')
        if self.getHtmlFile() == []:
            warnEmptyAttribute("htmlFile", "XSDataFile")
        if self._resultDirectory is not None:
            self.resultDirectory.export(outfile, level, name_='resultDirectory')
        if self._paperSize is not None:
            self.paperSize.export(outfile, level, name_='paperSize')
        if self._lowQuality is not None:
            self.lowQuality.export(outfile, level, name_='lowQuality')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'htmlFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.htmlFile.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resultDirectory':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setResultDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'paperSize':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setPaperSize(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lowQuality':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setLowQuality(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputHTML2PDF" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputHTML2PDF' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputHTML2PDF is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputHTML2PDF.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputHTML2PDF()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputHTML2PDF" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputHTML2PDF()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputHTML2PDF


class XSDataResultHTML2PDF(XSDataResult):
    def __init__(self, status=None, pdfFile=None):
        XSDataResult.__init__(self, status)
        if pdfFile is None:
            self._pdfFile = None
        elif pdfFile.__class__.__name__ == "XSDataFile":
            self._pdfFile = pdfFile
        else:
            strMessage = "ERROR! XSDataResultHTML2PDF constructor argument 'pdfFile' is not XSDataFile but %s" % self._pdfFile.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'pdfFile' attribute
    def getPdfFile(self): return self._pdfFile
    def setPdfFile(self, pdfFile):
        if pdfFile is None:
            self._pdfFile = None
        elif pdfFile.__class__.__name__ == "XSDataFile":
            self._pdfFile = pdfFile
        else:
            strMessage = "ERROR! XSDataResultHTML2PDF.setPdfFile argument is not XSDataFile but %s" % pdfFile.__class__.__name__
            raise BaseException(strMessage)
    def delPdfFile(self): self._pdfFile = None
    pdfFile = property(getPdfFile, setPdfFile, delPdfFile, "Property for pdfFile")
    def export(self, outfile, level, name_='XSDataResultHTML2PDF'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultHTML2PDF'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._pdfFile is not None:
            self.pdfFile.export(outfile, level, name_='pdfFile')
        else:
            warnEmptyAttribute("pdfFile", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdfFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdfFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultHTML2PDF" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultHTML2PDF' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultHTML2PDF is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultHTML2PDF.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultHTML2PDF()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultHTML2PDF" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultHTML2PDF()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultHTML2PDF



# End of data representation classes.


