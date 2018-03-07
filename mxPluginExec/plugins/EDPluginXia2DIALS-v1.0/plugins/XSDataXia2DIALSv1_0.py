#!/usr/bin/env python

#
# Generated Wed Mar 7 10:35::49 2018 by EDGenerateDS.
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
    from XSDataCommon import XSDataString
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
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataString
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



class XSDataInputXia2DIALS(XSDataInput):
    def __init__(self, configuration=None, endFrame=None, startFrame=None, unitCell=None, spaceGroup=None, anomalous=None, image=None):
        XSDataInput.__init__(self, configuration)
        if image is None:
            self._image = []
        elif image.__class__.__name__ == "list":
            self._image = image
        else:
            strMessage = "ERROR! XSDataInputXia2DIALS constructor argument 'image' is not list but %s" % self._image.__class__.__name__
            raise BaseException(strMessage)
        if anomalous is None:
            self._anomalous = None
        elif anomalous.__class__.__name__ == "XSDataBoolean":
            self._anomalous = anomalous
        else:
            strMessage = "ERROR! XSDataInputXia2DIALS constructor argument 'anomalous' is not XSDataBoolean but %s" % self._anomalous.__class__.__name__
            raise BaseException(strMessage)
        if spaceGroup is None:
            self._spaceGroup = None
        elif spaceGroup.__class__.__name__ == "XSDataString":
            self._spaceGroup = spaceGroup
        else:
            strMessage = "ERROR! XSDataInputXia2DIALS constructor argument 'spaceGroup' is not XSDataString but %s" % self._spaceGroup.__class__.__name__
            raise BaseException(strMessage)
        if unitCell is None:
            self._unitCell = None
        elif unitCell.__class__.__name__ == "XSDataString":
            self._unitCell = unitCell
        else:
            strMessage = "ERROR! XSDataInputXia2DIALS constructor argument 'unitCell' is not XSDataString but %s" % self._unitCell.__class__.__name__
            raise BaseException(strMessage)
        if startFrame is None:
            self._startFrame = None
        elif startFrame.__class__.__name__ == "XSDataInteger":
            self._startFrame = startFrame
        else:
            strMessage = "ERROR! XSDataInputXia2DIALS constructor argument 'startFrame' is not XSDataInteger but %s" % self._startFrame.__class__.__name__
            raise BaseException(strMessage)
        if endFrame is None:
            self._endFrame = None
        elif endFrame.__class__.__name__ == "XSDataInteger":
            self._endFrame = endFrame
        else:
            strMessage = "ERROR! XSDataInputXia2DIALS constructor argument 'endFrame' is not XSDataInteger but %s" % self._endFrame.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'image' attribute
    def getImage(self): return self._image
    def setImage(self, image):
        if image is None:
            self._image = []
        elif image.__class__.__name__ == "list":
            self._image = image
        else:
            strMessage = "ERROR! XSDataInputXia2DIALS.setImage argument is not list but %s" % image.__class__.__name__
            raise BaseException(strMessage)
    def delImage(self): self._image = None
    image = property(getImage, setImage, delImage, "Property for image")
    def addImage(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputXia2DIALS.addImage argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._image.append(value)
        else:
            strMessage = "ERROR! XSDataInputXia2DIALS.addImage argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertImage(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputXia2DIALS.insertImage argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputXia2DIALS.insertImage argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._image[index] = value
        else:
            strMessage = "ERROR! XSDataInputXia2DIALS.addImage argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'anomalous' attribute
    def getAnomalous(self): return self._anomalous
    def setAnomalous(self, anomalous):
        if anomalous is None:
            self._anomalous = None
        elif anomalous.__class__.__name__ == "XSDataBoolean":
            self._anomalous = anomalous
        else:
            strMessage = "ERROR! XSDataInputXia2DIALS.setAnomalous argument is not XSDataBoolean but %s" % anomalous.__class__.__name__
            raise BaseException(strMessage)
    def delAnomalous(self): self._anomalous = None
    anomalous = property(getAnomalous, setAnomalous, delAnomalous, "Property for anomalous")
    # Methods and properties for the 'spaceGroup' attribute
    def getSpaceGroup(self): return self._spaceGroup
    def setSpaceGroup(self, spaceGroup):
        if spaceGroup is None:
            self._spaceGroup = None
        elif spaceGroup.__class__.__name__ == "XSDataString":
            self._spaceGroup = spaceGroup
        else:
            strMessage = "ERROR! XSDataInputXia2DIALS.setSpaceGroup argument is not XSDataString but %s" % spaceGroup.__class__.__name__
            raise BaseException(strMessage)
    def delSpaceGroup(self): self._spaceGroup = None
    spaceGroup = property(getSpaceGroup, setSpaceGroup, delSpaceGroup, "Property for spaceGroup")
    # Methods and properties for the 'unitCell' attribute
    def getUnitCell(self): return self._unitCell
    def setUnitCell(self, unitCell):
        if unitCell is None:
            self._unitCell = None
        elif unitCell.__class__.__name__ == "XSDataString":
            self._unitCell = unitCell
        else:
            strMessage = "ERROR! XSDataInputXia2DIALS.setUnitCell argument is not XSDataString but %s" % unitCell.__class__.__name__
            raise BaseException(strMessage)
    def delUnitCell(self): self._unitCell = None
    unitCell = property(getUnitCell, setUnitCell, delUnitCell, "Property for unitCell")
    # Methods and properties for the 'startFrame' attribute
    def getStartFrame(self): return self._startFrame
    def setStartFrame(self, startFrame):
        if startFrame is None:
            self._startFrame = None
        elif startFrame.__class__.__name__ == "XSDataInteger":
            self._startFrame = startFrame
        else:
            strMessage = "ERROR! XSDataInputXia2DIALS.setStartFrame argument is not XSDataInteger but %s" % startFrame.__class__.__name__
            raise BaseException(strMessage)
    def delStartFrame(self): self._startFrame = None
    startFrame = property(getStartFrame, setStartFrame, delStartFrame, "Property for startFrame")
    # Methods and properties for the 'endFrame' attribute
    def getEndFrame(self): return self._endFrame
    def setEndFrame(self, endFrame):
        if endFrame is None:
            self._endFrame = None
        elif endFrame.__class__.__name__ == "XSDataInteger":
            self._endFrame = endFrame
        else:
            strMessage = "ERROR! XSDataInputXia2DIALS.setEndFrame argument is not XSDataInteger but %s" % endFrame.__class__.__name__
            raise BaseException(strMessage)
    def delEndFrame(self): self._endFrame = None
    endFrame = property(getEndFrame, setEndFrame, delEndFrame, "Property for endFrame")
    def export(self, outfile, level, name_='XSDataInputXia2DIALS'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputXia2DIALS'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for image_ in self.getImage():
            image_.export(outfile, level, name_='image')
        if self.getImage() == []:
            warnEmptyAttribute("image", "XSDataFile")
        if self._anomalous is not None:
            self.anomalous.export(outfile, level, name_='anomalous')
        if self._spaceGroup is not None:
            self.spaceGroup.export(outfile, level, name_='spaceGroup')
        if self._unitCell is not None:
            self.unitCell.export(outfile, level, name_='unitCell')
        if self._startFrame is not None:
            self.startFrame.export(outfile, level, name_='startFrame')
        if self._endFrame is not None:
            self.endFrame.export(outfile, level, name_='endFrame')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.image.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'anomalous':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setAnomalous(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spaceGroup':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSpaceGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unitCell':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setUnitCell(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'startFrame':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setStartFrame(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'endFrame':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setEndFrame(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputXia2DIALS" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputXia2DIALS' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputXia2DIALS is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputXia2DIALS.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputXia2DIALS()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputXia2DIALS" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputXia2DIALS()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputXia2DIALS


class XSDataResultXia2DIALS(XSDataResult):
    def __init__(self, status=None, logFiles=None, summary=None, ispybXML=None, dataFiles=None, htmlFile=None, logFile=None):
        XSDataResult.__init__(self, status)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultXia2DIALS constructor argument 'logFile' is not XSDataFile but %s" % self._logFile.__class__.__name__
            raise BaseException(strMessage)
        if htmlFile is None:
            self._htmlFile = None
        elif htmlFile.__class__.__name__ == "XSDataFile":
            self._htmlFile = htmlFile
        else:
            strMessage = "ERROR! XSDataResultXia2DIALS constructor argument 'htmlFile' is not XSDataFile but %s" % self._htmlFile.__class__.__name__
            raise BaseException(strMessage)
        if dataFiles is None:
            self._dataFiles = []
        elif dataFiles.__class__.__name__ == "list":
            self._dataFiles = dataFiles
        else:
            strMessage = "ERROR! XSDataResultXia2DIALS constructor argument 'dataFiles' is not list but %s" % self._dataFiles.__class__.__name__
            raise BaseException(strMessage)
        if ispybXML is None:
            self._ispybXML = None
        elif ispybXML.__class__.__name__ == "XSDataFile":
            self._ispybXML = ispybXML
        else:
            strMessage = "ERROR! XSDataResultXia2DIALS constructor argument 'ispybXML' is not XSDataFile but %s" % self._ispybXML.__class__.__name__
            raise BaseException(strMessage)
        if summary is None:
            self._summary = None
        elif summary.__class__.__name__ == "XSDataFile":
            self._summary = summary
        else:
            strMessage = "ERROR! XSDataResultXia2DIALS constructor argument 'summary' is not XSDataFile but %s" % self._summary.__class__.__name__
            raise BaseException(strMessage)
        if logFiles is None:
            self._logFiles = []
        elif logFiles.__class__.__name__ == "list":
            self._logFiles = logFiles
        else:
            strMessage = "ERROR! XSDataResultXia2DIALS constructor argument 'logFiles' is not list but %s" % self._logFiles.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultXia2DIALS.setLogFile argument is not XSDataFile but %s" % logFile.__class__.__name__
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
            strMessage = "ERROR! XSDataResultXia2DIALS.setHtmlFile argument is not XSDataFile but %s" % htmlFile.__class__.__name__
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
            strMessage = "ERROR! XSDataResultXia2DIALS.setDataFiles argument is not list but %s" % dataFiles.__class__.__name__
            raise BaseException(strMessage)
    def delDataFiles(self): self._dataFiles = None
    dataFiles = property(getDataFiles, setDataFiles, delDataFiles, "Property for dataFiles")
    def addDataFiles(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultXia2DIALS.addDataFiles argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._dataFiles.append(value)
        else:
            strMessage = "ERROR! XSDataResultXia2DIALS.addDataFiles argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertDataFiles(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultXia2DIALS.insertDataFiles argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultXia2DIALS.insertDataFiles argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._dataFiles[index] = value
        else:
            strMessage = "ERROR! XSDataResultXia2DIALS.addDataFiles argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'ispybXML' attribute
    def getIspybXML(self): return self._ispybXML
    def setIspybXML(self, ispybXML):
        if ispybXML is None:
            self._ispybXML = None
        elif ispybXML.__class__.__name__ == "XSDataFile":
            self._ispybXML = ispybXML
        else:
            strMessage = "ERROR! XSDataResultXia2DIALS.setIspybXML argument is not XSDataFile but %s" % ispybXML.__class__.__name__
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
            strMessage = "ERROR! XSDataResultXia2DIALS.setSummary argument is not XSDataFile but %s" % summary.__class__.__name__
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
            strMessage = "ERROR! XSDataResultXia2DIALS.setLogFiles argument is not list but %s" % logFiles.__class__.__name__
            raise BaseException(strMessage)
    def delLogFiles(self): self._logFiles = None
    logFiles = property(getLogFiles, setLogFiles, delLogFiles, "Property for logFiles")
    def addLogFiles(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultXia2DIALS.addLogFiles argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._logFiles.append(value)
        else:
            strMessage = "ERROR! XSDataResultXia2DIALS.addLogFiles argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertLogFiles(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultXia2DIALS.insertLogFiles argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultXia2DIALS.insertLogFiles argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._logFiles[index] = value
        else:
            strMessage = "ERROR! XSDataResultXia2DIALS.addLogFiles argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataResultXia2DIALS'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultXia2DIALS'):
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
        self.export( oStreamString, 0, name_="XSDataResultXia2DIALS" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultXia2DIALS' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultXia2DIALS is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultXia2DIALS.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultXia2DIALS()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultXia2DIALS" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultXia2DIALS()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultXia2DIALS



# End of data representation classes.


