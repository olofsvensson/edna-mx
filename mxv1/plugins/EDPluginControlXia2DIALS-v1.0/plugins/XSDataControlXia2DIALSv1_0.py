#!/usr/bin/env python

#
# Generated Wed Jan 17 02:58::53 2024 by EDGenerateDS.
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
}

try:
    from XSDataCommon import XSDataRange
    from XSDataCommon import XSDataBoolean
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
from XSDataCommon import XSDataRange
from XSDataCommon import XSDataBoolean
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



class XSDataInputControlXia2DIALS(XSDataInput):
    def __init__(self, configuration=None, exclude_range=None, reprocess=None, endFrame=None, startFrame=None, unitCell=None, spaceGroup=None, doAnomAndNonanom=None, doAnom=None, processDirectory=None, icatProcessDataDir=None, dataCollectionId=None):
        XSDataInput.__init__(self, configuration)
        if dataCollectionId is None:
            self._dataCollectionId = None
        elif dataCollectionId.__class__.__name__ == "XSDataInteger":
            self._dataCollectionId = dataCollectionId
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS constructor argument 'dataCollectionId' is not XSDataInteger but %s" % self._dataCollectionId.__class__.__name__
            raise BaseException(strMessage)
        if icatProcessDataDir is None:
            self._icatProcessDataDir = None
        elif icatProcessDataDir.__class__.__name__ == "XSDataFile":
            self._icatProcessDataDir = icatProcessDataDir
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS constructor argument 'icatProcessDataDir' is not XSDataFile but %s" % self._icatProcessDataDir.__class__.__name__
            raise BaseException(strMessage)
        if processDirectory is None:
            self._processDirectory = None
        elif processDirectory.__class__.__name__ == "XSDataFile":
            self._processDirectory = processDirectory
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS constructor argument 'processDirectory' is not XSDataFile but %s" % self._processDirectory.__class__.__name__
            raise BaseException(strMessage)
        if doAnom is None:
            self._doAnom = None
        elif doAnom.__class__.__name__ == "XSDataBoolean":
            self._doAnom = doAnom
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS constructor argument 'doAnom' is not XSDataBoolean but %s" % self._doAnom.__class__.__name__
            raise BaseException(strMessage)
        if doAnomAndNonanom is None:
            self._doAnomAndNonanom = None
        elif doAnomAndNonanom.__class__.__name__ == "XSDataBoolean":
            self._doAnomAndNonanom = doAnomAndNonanom
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS constructor argument 'doAnomAndNonanom' is not XSDataBoolean but %s" % self._doAnomAndNonanom.__class__.__name__
            raise BaseException(strMessage)
        if spaceGroup is None:
            self._spaceGroup = None
        elif spaceGroup.__class__.__name__ == "XSDataString":
            self._spaceGroup = spaceGroup
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS constructor argument 'spaceGroup' is not XSDataString but %s" % self._spaceGroup.__class__.__name__
            raise BaseException(strMessage)
        if unitCell is None:
            self._unitCell = None
        elif unitCell.__class__.__name__ == "XSDataString":
            self._unitCell = unitCell
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS constructor argument 'unitCell' is not XSDataString but %s" % self._unitCell.__class__.__name__
            raise BaseException(strMessage)
        if startFrame is None:
            self._startFrame = None
        elif startFrame.__class__.__name__ == "XSDataInteger":
            self._startFrame = startFrame
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS constructor argument 'startFrame' is not XSDataInteger but %s" % self._startFrame.__class__.__name__
            raise BaseException(strMessage)
        if endFrame is None:
            self._endFrame = None
        elif endFrame.__class__.__name__ == "XSDataInteger":
            self._endFrame = endFrame
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS constructor argument 'endFrame' is not XSDataInteger but %s" % self._endFrame.__class__.__name__
            raise BaseException(strMessage)
        if reprocess is None:
            self._reprocess = None
        elif reprocess.__class__.__name__ == "XSDataBoolean":
            self._reprocess = reprocess
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS constructor argument 'reprocess' is not XSDataBoolean but %s" % self._reprocess.__class__.__name__
            raise BaseException(strMessage)
        if exclude_range is None:
            self._exclude_range = []
        elif exclude_range.__class__.__name__ == "list":
            self._exclude_range = exclude_range
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS constructor argument 'exclude_range' is not list but %s" % self._exclude_range.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'dataCollectionId' attribute
    def getDataCollectionId(self): return self._dataCollectionId
    def setDataCollectionId(self, dataCollectionId):
        if dataCollectionId is None:
            self._dataCollectionId = None
        elif dataCollectionId.__class__.__name__ == "XSDataInteger":
            self._dataCollectionId = dataCollectionId
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS.setDataCollectionId argument is not XSDataInteger but %s" % dataCollectionId.__class__.__name__
            raise BaseException(strMessage)
    def delDataCollectionId(self): self._dataCollectionId = None
    dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
    # Methods and properties for the 'icatProcessDataDir' attribute
    def getIcatProcessDataDir(self): return self._icatProcessDataDir
    def setIcatProcessDataDir(self, icatProcessDataDir):
        if icatProcessDataDir is None:
            self._icatProcessDataDir = None
        elif icatProcessDataDir.__class__.__name__ == "XSDataFile":
            self._icatProcessDataDir = icatProcessDataDir
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS.setIcatProcessDataDir argument is not XSDataFile but %s" % icatProcessDataDir.__class__.__name__
            raise BaseException(strMessage)
    def delIcatProcessDataDir(self): self._icatProcessDataDir = None
    icatProcessDataDir = property(getIcatProcessDataDir, setIcatProcessDataDir, delIcatProcessDataDir, "Property for icatProcessDataDir")
    # Methods and properties for the 'processDirectory' attribute
    def getProcessDirectory(self): return self._processDirectory
    def setProcessDirectory(self, processDirectory):
        if processDirectory is None:
            self._processDirectory = None
        elif processDirectory.__class__.__name__ == "XSDataFile":
            self._processDirectory = processDirectory
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS.setProcessDirectory argument is not XSDataFile but %s" % processDirectory.__class__.__name__
            raise BaseException(strMessage)
    def delProcessDirectory(self): self._processDirectory = None
    processDirectory = property(getProcessDirectory, setProcessDirectory, delProcessDirectory, "Property for processDirectory")
    # Methods and properties for the 'doAnom' attribute
    def getDoAnom(self): return self._doAnom
    def setDoAnom(self, doAnom):
        if doAnom is None:
            self._doAnom = None
        elif doAnom.__class__.__name__ == "XSDataBoolean":
            self._doAnom = doAnom
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS.setDoAnom argument is not XSDataBoolean but %s" % doAnom.__class__.__name__
            raise BaseException(strMessage)
    def delDoAnom(self): self._doAnom = None
    doAnom = property(getDoAnom, setDoAnom, delDoAnom, "Property for doAnom")
    # Methods and properties for the 'doAnomAndNonanom' attribute
    def getDoAnomAndNonanom(self): return self._doAnomAndNonanom
    def setDoAnomAndNonanom(self, doAnomAndNonanom):
        if doAnomAndNonanom is None:
            self._doAnomAndNonanom = None
        elif doAnomAndNonanom.__class__.__name__ == "XSDataBoolean":
            self._doAnomAndNonanom = doAnomAndNonanom
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS.setDoAnomAndNonanom argument is not XSDataBoolean but %s" % doAnomAndNonanom.__class__.__name__
            raise BaseException(strMessage)
    def delDoAnomAndNonanom(self): self._doAnomAndNonanom = None
    doAnomAndNonanom = property(getDoAnomAndNonanom, setDoAnomAndNonanom, delDoAnomAndNonanom, "Property for doAnomAndNonanom")
    # Methods and properties for the 'spaceGroup' attribute
    def getSpaceGroup(self): return self._spaceGroup
    def setSpaceGroup(self, spaceGroup):
        if spaceGroup is None:
            self._spaceGroup = None
        elif spaceGroup.__class__.__name__ == "XSDataString":
            self._spaceGroup = spaceGroup
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS.setSpaceGroup argument is not XSDataString but %s" % spaceGroup.__class__.__name__
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
            strMessage = "ERROR! XSDataInputControlXia2DIALS.setUnitCell argument is not XSDataString but %s" % unitCell.__class__.__name__
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
            strMessage = "ERROR! XSDataInputControlXia2DIALS.setStartFrame argument is not XSDataInteger but %s" % startFrame.__class__.__name__
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
            strMessage = "ERROR! XSDataInputControlXia2DIALS.setEndFrame argument is not XSDataInteger but %s" % endFrame.__class__.__name__
            raise BaseException(strMessage)
    def delEndFrame(self): self._endFrame = None
    endFrame = property(getEndFrame, setEndFrame, delEndFrame, "Property for endFrame")
    # Methods and properties for the 'reprocess' attribute
    def getReprocess(self): return self._reprocess
    def setReprocess(self, reprocess):
        if reprocess is None:
            self._reprocess = None
        elif reprocess.__class__.__name__ == "XSDataBoolean":
            self._reprocess = reprocess
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS.setReprocess argument is not XSDataBoolean but %s" % reprocess.__class__.__name__
            raise BaseException(strMessage)
    def delReprocess(self): self._reprocess = None
    reprocess = property(getReprocess, setReprocess, delReprocess, "Property for reprocess")
    # Methods and properties for the 'exclude_range' attribute
    def getExclude_range(self): return self._exclude_range
    def setExclude_range(self, exclude_range):
        if exclude_range is None:
            self._exclude_range = []
        elif exclude_range.__class__.__name__ == "list":
            self._exclude_range = exclude_range
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS.setExclude_range argument is not list but %s" % exclude_range.__class__.__name__
            raise BaseException(strMessage)
    def delExclude_range(self): self._exclude_range = None
    exclude_range = property(getExclude_range, setExclude_range, delExclude_range, "Property for exclude_range")
    def addExclude_range(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputControlXia2DIALS.addExclude_range argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataRange":
            self._exclude_range.append(value)
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS.addExclude_range argument is not XSDataRange but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertExclude_range(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputControlXia2DIALS.insertExclude_range argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputControlXia2DIALS.insertExclude_range argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataRange":
            self._exclude_range[index] = value
        else:
            strMessage = "ERROR! XSDataInputControlXia2DIALS.addExclude_range argument is not XSDataRange but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataInputControlXia2DIALS'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputControlXia2DIALS'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._dataCollectionId is not None:
            self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
        if self._icatProcessDataDir is not None:
            self.icatProcessDataDir.export(outfile, level, name_='icatProcessDataDir')
        if self._processDirectory is not None:
            self.processDirectory.export(outfile, level, name_='processDirectory')
        if self._doAnom is not None:
            self.doAnom.export(outfile, level, name_='doAnom')
        if self._doAnomAndNonanom is not None:
            self.doAnomAndNonanom.export(outfile, level, name_='doAnomAndNonanom')
        if self._spaceGroup is not None:
            self.spaceGroup.export(outfile, level, name_='spaceGroup')
        if self._unitCell is not None:
            self.unitCell.export(outfile, level, name_='unitCell')
        if self._startFrame is not None:
            self.startFrame.export(outfile, level, name_='startFrame')
        if self._endFrame is not None:
            self.endFrame.export(outfile, level, name_='endFrame')
        if self._reprocess is not None:
            self.reprocess.export(outfile, level, name_='reprocess')
        for exclude_range_ in self.getExclude_range():
            exclude_range_.export(outfile, level, name_='exclude_range')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setDataCollectionId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'icatProcessDataDir':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setIcatProcessDataDir(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'processDirectory':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setProcessDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'doAnom':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setDoAnom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'doAnomAndNonanom':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setDoAnomAndNonanom(obj_)
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
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'reprocess':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setReprocess(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'exclude_range':
            obj_ = XSDataRange()
            obj_.build(child_)
            self.exclude_range.append(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputControlXia2DIALS" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputControlXia2DIALS' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputControlXia2DIALS is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputControlXia2DIALS.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputControlXia2DIALS()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputControlXia2DIALS" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputControlXia2DIALS()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputControlXia2DIALS


class XSDataResultControlXia2DIALS(XSDataResult):
    def __init__(self, status=None):
        XSDataResult.__init__(self, status)
    def export(self, outfile, level, name_='XSDataResultControlXia2DIALS'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultControlXia2DIALS'):
        XSDataResult.exportChildren(self, outfile, level, name_)
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        pass
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultControlXia2DIALS" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultControlXia2DIALS' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultControlXia2DIALS is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultControlXia2DIALS.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultControlXia2DIALS()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultControlXia2DIALS" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultControlXia2DIALS()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultControlXia2DIALS



# End of data representation classes.


