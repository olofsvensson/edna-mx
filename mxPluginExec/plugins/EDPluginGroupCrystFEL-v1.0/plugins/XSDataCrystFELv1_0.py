#!/usr/bin/env python

#
# Generated Fri May 31 01:58::52 2019 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = { \
 "XSDataCommon": "mxPluginExec/plugins/EDPluginGroupCrystFEL-v1.0/datamodel/../../../../kernel/datamodel", \
 "XSDataCommon": "mxPluginExec/plugins/EDPluginGroupCrystFEL-v1.0/datamodel/../../../../kernel/datamodel", \
 "XSDataCommon": "mxPluginExec/plugins/EDPluginGroupCrystFEL-v1.0/datamodel/../../../../kernel/datamodel", \
 "XSDataCommon": "mxPluginExec/plugins/EDPluginGroupCrystFEL-v1.0/datamodel/../../../../kernel/datamodel", \
}

try:
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataInput
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



class XSDataInputCrystFEL(XSDataInput):
    def __init__(self, configuration=None, imagesFullPathFile=None, cellFile=None, geomFile=None):
        XSDataInput.__init__(self, configuration)
        if geomFile is None:
            self._geomFile = None
        elif geomFile.__class__.__name__ == "XSDataString":
            self._geomFile = geomFile
        else:
            strMessage = "ERROR! XSDataInputCrystFEL constructor argument 'geomFile' is not XSDataString but %s" % self._geomFile.__class__.__name__
            raise BaseException(strMessage)
        if cellFile is None:
            self._cellFile = None
        elif cellFile.__class__.__name__ == "XSDataString":
            self._cellFile = cellFile
        else:
            strMessage = "ERROR! XSDataInputCrystFEL constructor argument 'cellFile' is not XSDataString but %s" % self._cellFile.__class__.__name__
            raise BaseException(strMessage)
        if imagesFullPathFile is None:
            self._imagesFullPathFile = None
        elif imagesFullPathFile.__class__.__name__ == "XSDataString":
            self._imagesFullPathFile = imagesFullPathFile
        else:
            strMessage = "ERROR! XSDataInputCrystFEL constructor argument 'imagesFullPathFile' is not XSDataString but %s" % self._imagesFullPathFile.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'geomFile' attribute
    def getGeomFile(self): return self._geomFile
    def setGeomFile(self, geomFile):
        if geomFile is None:
            self._geomFile = None
        elif geomFile.__class__.__name__ == "XSDataString":
            self._geomFile = geomFile
        else:
            strMessage = "ERROR! XSDataInputCrystFEL.setGeomFile argument is not XSDataString but %s" % geomFile.__class__.__name__
            raise BaseException(strMessage)
    def delGeomFile(self): self._geomFile = None
    geomFile = property(getGeomFile, setGeomFile, delGeomFile, "Property for geomFile")
    # Methods and properties for the 'cellFile' attribute
    def getCellFile(self): return self._cellFile
    def setCellFile(self, cellFile):
        if cellFile is None:
            self._cellFile = None
        elif cellFile.__class__.__name__ == "XSDataString":
            self._cellFile = cellFile
        else:
            strMessage = "ERROR! XSDataInputCrystFEL.setCellFile argument is not XSDataString but %s" % cellFile.__class__.__name__
            raise BaseException(strMessage)
    def delCellFile(self): self._cellFile = None
    cellFile = property(getCellFile, setCellFile, delCellFile, "Property for cellFile")
    # Methods and properties for the 'imagesFullPathFile' attribute
    def getImagesFullPathFile(self): return self._imagesFullPathFile
    def setImagesFullPathFile(self, imagesFullPathFile):
        if imagesFullPathFile is None:
            self._imagesFullPathFile = None
        elif imagesFullPathFile.__class__.__name__ == "XSDataString":
            self._imagesFullPathFile = imagesFullPathFile
        else:
            strMessage = "ERROR! XSDataInputCrystFEL.setImagesFullPathFile argument is not XSDataString but %s" % imagesFullPathFile.__class__.__name__
            raise BaseException(strMessage)
    def delImagesFullPathFile(self): self._imagesFullPathFile = None
    imagesFullPathFile = property(getImagesFullPathFile, setImagesFullPathFile, delImagesFullPathFile, "Property for imagesFullPathFile")
    def export(self, outfile, level, name_='XSDataInputCrystFEL'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputCrystFEL'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._geomFile is not None:
            self.geomFile.export(outfile, level, name_='geomFile')
        else:
            warnEmptyAttribute("geomFile", "XSDataString")
        if self._cellFile is not None:
            self.cellFile.export(outfile, level, name_='cellFile')
        else:
            warnEmptyAttribute("cellFile", "XSDataString")
        if self._imagesFullPathFile is not None:
            self.imagesFullPathFile.export(outfile, level, name_='imagesFullPathFile')
        else:
            warnEmptyAttribute("imagesFullPathFile", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'geomFile':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setGeomFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cellFile':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setCellFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imagesFullPathFile':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setImagesFullPathFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputCrystFEL" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputCrystFEL' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputCrystFEL is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputCrystFEL.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputCrystFEL()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputCrystFEL" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputCrystFEL()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputCrystFEL


class XSDataResultCrystFEL(XSDataResult):
    def __init__(self, status=None, logFiles=None, summary=None, ispybXML=None, dataFiles=None, htmlFile=None, logFile=None):
        XSDataResult.__init__(self, status)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultCrystFEL constructor argument 'logFile' is not XSDataFile but %s" % self._logFile.__class__.__name__
            raise BaseException(strMessage)
        if htmlFile is None:
            self._htmlFile = None
        elif htmlFile.__class__.__name__ == "XSDataFile":
            self._htmlFile = htmlFile
        else:
            strMessage = "ERROR! XSDataResultCrystFEL constructor argument 'htmlFile' is not XSDataFile but %s" % self._htmlFile.__class__.__name__
            raise BaseException(strMessage)
        if dataFiles is None:
            self._dataFiles = []
        elif dataFiles.__class__.__name__ == "list":
            self._dataFiles = dataFiles
        else:
            strMessage = "ERROR! XSDataResultCrystFEL constructor argument 'dataFiles' is not list but %s" % self._dataFiles.__class__.__name__
            raise BaseException(strMessage)
        if ispybXML is None:
            self._ispybXML = None
        elif ispybXML.__class__.__name__ == "XSDataFile":
            self._ispybXML = ispybXML
        else:
            strMessage = "ERROR! XSDataResultCrystFEL constructor argument 'ispybXML' is not XSDataFile but %s" % self._ispybXML.__class__.__name__
            raise BaseException(strMessage)
        if summary is None:
            self._summary = None
        elif summary.__class__.__name__ == "XSDataFile":
            self._summary = summary
        else:
            strMessage = "ERROR! XSDataResultCrystFEL constructor argument 'summary' is not XSDataFile but %s" % self._summary.__class__.__name__
            raise BaseException(strMessage)
        if logFiles is None:
            self._logFiles = []
        elif logFiles.__class__.__name__ == "list":
            self._logFiles = logFiles
        else:
            strMessage = "ERROR! XSDataResultCrystFEL constructor argument 'logFiles' is not list but %s" % self._logFiles.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultCrystFEL.setLogFile argument is not XSDataFile but %s" % logFile.__class__.__name__
            raise BaseException(strMessage)
    def delLogFile(self): self._logFile = None
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    # Methods and properties for the 'htmlFile' attribute
    def getHtmlFile(self): return self._htmlFile
    def setHtmlFile(self, htmlFile):
        if htmlFile is None:
            self._htmlFile = None
        elif htmlFile.__class__.__name__ == "XSDataFile":
            self._htmlFile = htmlFile
        else:
            strMessage = "ERROR! XSDataResultCrystFEL.setHtmlFile argument is not XSDataFile but %s" % htmlFile.__class__.__name__
            raise BaseException(strMessage)
    def delHtmlFile(self): self._htmlFile = None
    htmlFile = property(getHtmlFile, setHtmlFile, delHtmlFile, "Property for htmlFile")
    # Methods and properties for the 'dataFiles' attribute
    def getDataFiles(self): return self._dataFiles
    def setDataFiles(self, dataFiles):
        if dataFiles is None:
            self._dataFiles = []
        elif dataFiles.__class__.__name__ == "list":
            self._dataFiles = dataFiles
        else:
            strMessage = "ERROR! XSDataResultCrystFEL.setDataFiles argument is not list but %s" % dataFiles.__class__.__name__
            raise BaseException(strMessage)
    def delDataFiles(self): self._dataFiles = None
    dataFiles = property(getDataFiles, setDataFiles, delDataFiles, "Property for dataFiles")
    def addDataFiles(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultCrystFEL.addDataFiles argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._dataFiles.append(value)
        else:
            strMessage = "ERROR! XSDataResultCrystFEL.addDataFiles argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertDataFiles(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultCrystFEL.insertDataFiles argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultCrystFEL.insertDataFiles argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._dataFiles[index] = value
        else:
            strMessage = "ERROR! XSDataResultCrystFEL.addDataFiles argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'ispybXML' attribute
    def getIspybXML(self): return self._ispybXML
    def setIspybXML(self, ispybXML):
        if ispybXML is None:
            self._ispybXML = None
        elif ispybXML.__class__.__name__ == "XSDataFile":
            self._ispybXML = ispybXML
        else:
            strMessage = "ERROR! XSDataResultCrystFEL.setIspybXML argument is not XSDataFile but %s" % ispybXML.__class__.__name__
            raise BaseException(strMessage)
    def delIspybXML(self): self._ispybXML = None
    ispybXML = property(getIspybXML, setIspybXML, delIspybXML, "Property for ispybXML")
    # Methods and properties for the 'summary' attribute
    def getSummary(self): return self._summary
    def setSummary(self, summary):
        if summary is None:
            self._summary = None
        elif summary.__class__.__name__ == "XSDataFile":
            self._summary = summary
        else:
            strMessage = "ERROR! XSDataResultCrystFEL.setSummary argument is not XSDataFile but %s" % summary.__class__.__name__
            raise BaseException(strMessage)
    def delSummary(self): self._summary = None
    summary = property(getSummary, setSummary, delSummary, "Property for summary")
    # Methods and properties for the 'logFiles' attribute
    def getLogFiles(self): return self._logFiles
    def setLogFiles(self, logFiles):
        if logFiles is None:
            self._logFiles = []
        elif logFiles.__class__.__name__ == "list":
            self._logFiles = logFiles
        else:
            strMessage = "ERROR! XSDataResultCrystFEL.setLogFiles argument is not list but %s" % logFiles.__class__.__name__
            raise BaseException(strMessage)
    def delLogFiles(self): self._logFiles = None
    logFiles = property(getLogFiles, setLogFiles, delLogFiles, "Property for logFiles")
    def addLogFiles(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultCrystFEL.addLogFiles argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._logFiles.append(value)
        else:
            strMessage = "ERROR! XSDataResultCrystFEL.addLogFiles argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertLogFiles(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultCrystFEL.insertLogFiles argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultCrystFEL.insertLogFiles argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._logFiles[index] = value
        else:
            strMessage = "ERROR! XSDataResultCrystFEL.addLogFiles argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataResultCrystFEL'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultCrystFEL'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_='logFile')
        else:
            warnEmptyAttribute("logFile", "XSDataFile")
        if self._htmlFile is not None:
            self.htmlFile.export(outfile, level, name_='htmlFile')
        else:
            warnEmptyAttribute("htmlFile", "XSDataFile")
        for dataFiles_ in self.getDataFiles():
            dataFiles_.export(outfile, level, name_='dataFiles')
        if self.getDataFiles() == []:
            warnEmptyAttribute("dataFiles", "XSDataFile")
        if self._ispybXML is not None:
            self.ispybXML.export(outfile, level, name_='ispybXML')
        else:
            warnEmptyAttribute("ispybXML", "XSDataFile")
        if self._summary is not None:
            self.summary.export(outfile, level, name_='summary')
        else:
            warnEmptyAttribute("summary", "XSDataFile")
        for logFiles_ in self.getLogFiles():
            logFiles_.export(outfile, level, name_='logFiles')
        if self.getLogFiles() == []:
            warnEmptyAttribute("logFiles", "XSDataFile")
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
            nodeName_ == 'htmlFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setHtmlFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataFiles':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.dataFiles.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ispybXML':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setIspybXML(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'summary':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSummary(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'logFiles':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.logFiles.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultCrystFEL" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultCrystFEL' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultCrystFEL is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultCrystFEL.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultCrystFEL()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultCrystFEL" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultCrystFEL()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultCrystFEL



# End of data representation classes.


