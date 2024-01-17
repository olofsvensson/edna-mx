#!/usr/bin/env python

#
# Generated Wed Jan 17 02:58::16 2024 by EDGenerateDS.
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
}

try:
    from XSDataCommon import XSDataRange
    from XSDataCommon import XSDataBoolean
    from XSDataCommon import XSDataDouble
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
from XSDataCommon import XSDataDouble
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



class XSDataInputControlAutoPROC(XSDataInput):
    def __init__(self, configuration=None, exclude_range=None, highResolutionLimit=None, lowResolutionLimit=None, reprocess=None, cell=None, symm=None, doAnomAndNonanom=None, doAnom=None, processDirectory=None, toN=None, fromN=None, templateN=None, dirN=None, icatProcessDataDir=None, dataCollectionId=None):
        XSDataInput.__init__(self, configuration)
        if dataCollectionId is None:
            self._dataCollectionId = None
        elif dataCollectionId.__class__.__name__ == "XSDataInteger":
            self._dataCollectionId = dataCollectionId
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC constructor argument 'dataCollectionId' is not XSDataInteger but %s" % self._dataCollectionId.__class__.__name__
            raise BaseException(strMessage)
        if icatProcessDataDir is None:
            self._icatProcessDataDir = None
        elif icatProcessDataDir.__class__.__name__ == "XSDataFile":
            self._icatProcessDataDir = icatProcessDataDir
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC constructor argument 'icatProcessDataDir' is not XSDataFile but %s" % self._icatProcessDataDir.__class__.__name__
            raise BaseException(strMessage)
        if dirN is None:
            self._dirN = None
        elif dirN.__class__.__name__ == "XSDataFile":
            self._dirN = dirN
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC constructor argument 'dirN' is not XSDataFile but %s" % self._dirN.__class__.__name__
            raise BaseException(strMessage)
        if templateN is None:
            self._templateN = None
        elif templateN.__class__.__name__ == "XSDataString":
            self._templateN = templateN
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC constructor argument 'templateN' is not XSDataString but %s" % self._templateN.__class__.__name__
            raise BaseException(strMessage)
        if fromN is None:
            self._fromN = None
        elif fromN.__class__.__name__ == "XSDataInteger":
            self._fromN = fromN
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC constructor argument 'fromN' is not XSDataInteger but %s" % self._fromN.__class__.__name__
            raise BaseException(strMessage)
        if toN is None:
            self._toN = None
        elif toN.__class__.__name__ == "XSDataInteger":
            self._toN = toN
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC constructor argument 'toN' is not XSDataInteger but %s" % self._toN.__class__.__name__
            raise BaseException(strMessage)
        if processDirectory is None:
            self._processDirectory = None
        elif processDirectory.__class__.__name__ == "XSDataFile":
            self._processDirectory = processDirectory
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC constructor argument 'processDirectory' is not XSDataFile but %s" % self._processDirectory.__class__.__name__
            raise BaseException(strMessage)
        if doAnom is None:
            self._doAnom = None
        elif doAnom.__class__.__name__ == "XSDataBoolean":
            self._doAnom = doAnom
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC constructor argument 'doAnom' is not XSDataBoolean but %s" % self._doAnom.__class__.__name__
            raise BaseException(strMessage)
        if doAnomAndNonanom is None:
            self._doAnomAndNonanom = None
        elif doAnomAndNonanom.__class__.__name__ == "XSDataBoolean":
            self._doAnomAndNonanom = doAnomAndNonanom
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC constructor argument 'doAnomAndNonanom' is not XSDataBoolean but %s" % self._doAnomAndNonanom.__class__.__name__
            raise BaseException(strMessage)
        if symm is None:
            self._symm = None
        elif symm.__class__.__name__ == "XSDataString":
            self._symm = symm
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC constructor argument 'symm' is not XSDataString but %s" % self._symm.__class__.__name__
            raise BaseException(strMessage)
        if cell is None:
            self._cell = None
        elif cell.__class__.__name__ == "XSDataString":
            self._cell = cell
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC constructor argument 'cell' is not XSDataString but %s" % self._cell.__class__.__name__
            raise BaseException(strMessage)
        if reprocess is None:
            self._reprocess = None
        elif reprocess.__class__.__name__ == "XSDataBoolean":
            self._reprocess = reprocess
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC constructor argument 'reprocess' is not XSDataBoolean but %s" % self._reprocess.__class__.__name__
            raise BaseException(strMessage)
        if lowResolutionLimit is None:
            self._lowResolutionLimit = None
        elif lowResolutionLimit.__class__.__name__ == "XSDataDouble":
            self._lowResolutionLimit = lowResolutionLimit
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC constructor argument 'lowResolutionLimit' is not XSDataDouble but %s" % self._lowResolutionLimit.__class__.__name__
            raise BaseException(strMessage)
        if highResolutionLimit is None:
            self._highResolutionLimit = None
        elif highResolutionLimit.__class__.__name__ == "XSDataDouble":
            self._highResolutionLimit = highResolutionLimit
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC constructor argument 'highResolutionLimit' is not XSDataDouble but %s" % self._highResolutionLimit.__class__.__name__
            raise BaseException(strMessage)
        if exclude_range is None:
            self._exclude_range = []
        elif exclude_range.__class__.__name__ == "list":
            self._exclude_range = exclude_range
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC constructor argument 'exclude_range' is not list but %s" % self._exclude_range.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'dataCollectionId' attribute
    def getDataCollectionId(self): return self._dataCollectionId
    def setDataCollectionId(self, dataCollectionId):
        if dataCollectionId is None:
            self._dataCollectionId = None
        elif dataCollectionId.__class__.__name__ == "XSDataInteger":
            self._dataCollectionId = dataCollectionId
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC.setDataCollectionId argument is not XSDataInteger but %s" % dataCollectionId.__class__.__name__
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
            strMessage = "ERROR! XSDataInputControlAutoPROC.setIcatProcessDataDir argument is not XSDataFile but %s" % icatProcessDataDir.__class__.__name__
            raise BaseException(strMessage)
    def delIcatProcessDataDir(self): self._icatProcessDataDir = None
    icatProcessDataDir = property(getIcatProcessDataDir, setIcatProcessDataDir, delIcatProcessDataDir, "Property for icatProcessDataDir")
    # Methods and properties for the 'dirN' attribute
    def getDirN(self): return self._dirN
    def setDirN(self, dirN):
        if dirN is None:
            self._dirN = None
        elif dirN.__class__.__name__ == "XSDataFile":
            self._dirN = dirN
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC.setDirN argument is not XSDataFile but %s" % dirN.__class__.__name__
            raise BaseException(strMessage)
    def delDirN(self): self._dirN = None
    dirN = property(getDirN, setDirN, delDirN, "Property for dirN")
    # Methods and properties for the 'templateN' attribute
    def getTemplateN(self): return self._templateN
    def setTemplateN(self, templateN):
        if templateN is None:
            self._templateN = None
        elif templateN.__class__.__name__ == "XSDataString":
            self._templateN = templateN
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC.setTemplateN argument is not XSDataString but %s" % templateN.__class__.__name__
            raise BaseException(strMessage)
    def delTemplateN(self): self._templateN = None
    templateN = property(getTemplateN, setTemplateN, delTemplateN, "Property for templateN")
    # Methods and properties for the 'fromN' attribute
    def getFromN(self): return self._fromN
    def setFromN(self, fromN):
        if fromN is None:
            self._fromN = None
        elif fromN.__class__.__name__ == "XSDataInteger":
            self._fromN = fromN
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC.setFromN argument is not XSDataInteger but %s" % fromN.__class__.__name__
            raise BaseException(strMessage)
    def delFromN(self): self._fromN = None
    fromN = property(getFromN, setFromN, delFromN, "Property for fromN")
    # Methods and properties for the 'toN' attribute
    def getToN(self): return self._toN
    def setToN(self, toN):
        if toN is None:
            self._toN = None
        elif toN.__class__.__name__ == "XSDataInteger":
            self._toN = toN
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC.setToN argument is not XSDataInteger but %s" % toN.__class__.__name__
            raise BaseException(strMessage)
    def delToN(self): self._toN = None
    toN = property(getToN, setToN, delToN, "Property for toN")
    # Methods and properties for the 'processDirectory' attribute
    def getProcessDirectory(self): return self._processDirectory
    def setProcessDirectory(self, processDirectory):
        if processDirectory is None:
            self._processDirectory = None
        elif processDirectory.__class__.__name__ == "XSDataFile":
            self._processDirectory = processDirectory
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC.setProcessDirectory argument is not XSDataFile but %s" % processDirectory.__class__.__name__
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
            strMessage = "ERROR! XSDataInputControlAutoPROC.setDoAnom argument is not XSDataBoolean but %s" % doAnom.__class__.__name__
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
            strMessage = "ERROR! XSDataInputControlAutoPROC.setDoAnomAndNonanom argument is not XSDataBoolean but %s" % doAnomAndNonanom.__class__.__name__
            raise BaseException(strMessage)
    def delDoAnomAndNonanom(self): self._doAnomAndNonanom = None
    doAnomAndNonanom = property(getDoAnomAndNonanom, setDoAnomAndNonanom, delDoAnomAndNonanom, "Property for doAnomAndNonanom")
    # Methods and properties for the 'symm' attribute
    def getSymm(self): return self._symm
    def setSymm(self, symm):
        if symm is None:
            self._symm = None
        elif symm.__class__.__name__ == "XSDataString":
            self._symm = symm
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC.setSymm argument is not XSDataString but %s" % symm.__class__.__name__
            raise BaseException(strMessage)
    def delSymm(self): self._symm = None
    symm = property(getSymm, setSymm, delSymm, "Property for symm")
    # Methods and properties for the 'cell' attribute
    def getCell(self): return self._cell
    def setCell(self, cell):
        if cell is None:
            self._cell = None
        elif cell.__class__.__name__ == "XSDataString":
            self._cell = cell
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC.setCell argument is not XSDataString but %s" % cell.__class__.__name__
            raise BaseException(strMessage)
    def delCell(self): self._cell = None
    cell = property(getCell, setCell, delCell, "Property for cell")
    # Methods and properties for the 'reprocess' attribute
    def getReprocess(self): return self._reprocess
    def setReprocess(self, reprocess):
        if reprocess is None:
            self._reprocess = None
        elif reprocess.__class__.__name__ == "XSDataBoolean":
            self._reprocess = reprocess
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC.setReprocess argument is not XSDataBoolean but %s" % reprocess.__class__.__name__
            raise BaseException(strMessage)
    def delReprocess(self): self._reprocess = None
    reprocess = property(getReprocess, setReprocess, delReprocess, "Property for reprocess")
    # Methods and properties for the 'lowResolutionLimit' attribute
    def getLowResolutionLimit(self): return self._lowResolutionLimit
    def setLowResolutionLimit(self, lowResolutionLimit):
        if lowResolutionLimit is None:
            self._lowResolutionLimit = None
        elif lowResolutionLimit.__class__.__name__ == "XSDataDouble":
            self._lowResolutionLimit = lowResolutionLimit
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC.setLowResolutionLimit argument is not XSDataDouble but %s" % lowResolutionLimit.__class__.__name__
            raise BaseException(strMessage)
    def delLowResolutionLimit(self): self._lowResolutionLimit = None
    lowResolutionLimit = property(getLowResolutionLimit, setLowResolutionLimit, delLowResolutionLimit, "Property for lowResolutionLimit")
    # Methods and properties for the 'highResolutionLimit' attribute
    def getHighResolutionLimit(self): return self._highResolutionLimit
    def setHighResolutionLimit(self, highResolutionLimit):
        if highResolutionLimit is None:
            self._highResolutionLimit = None
        elif highResolutionLimit.__class__.__name__ == "XSDataDouble":
            self._highResolutionLimit = highResolutionLimit
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC.setHighResolutionLimit argument is not XSDataDouble but %s" % highResolutionLimit.__class__.__name__
            raise BaseException(strMessage)
    def delHighResolutionLimit(self): self._highResolutionLimit = None
    highResolutionLimit = property(getHighResolutionLimit, setHighResolutionLimit, delHighResolutionLimit, "Property for highResolutionLimit")
    # Methods and properties for the 'exclude_range' attribute
    def getExclude_range(self): return self._exclude_range
    def setExclude_range(self, exclude_range):
        if exclude_range is None:
            self._exclude_range = []
        elif exclude_range.__class__.__name__ == "list":
            self._exclude_range = exclude_range
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC.setExclude_range argument is not list but %s" % exclude_range.__class__.__name__
            raise BaseException(strMessage)
    def delExclude_range(self): self._exclude_range = None
    exclude_range = property(getExclude_range, setExclude_range, delExclude_range, "Property for exclude_range")
    def addExclude_range(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputControlAutoPROC.addExclude_range argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataRange":
            self._exclude_range.append(value)
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC.addExclude_range argument is not XSDataRange but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertExclude_range(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputControlAutoPROC.insertExclude_range argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputControlAutoPROC.insertExclude_range argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataRange":
            self._exclude_range[index] = value
        else:
            strMessage = "ERROR! XSDataInputControlAutoPROC.addExclude_range argument is not XSDataRange but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataInputControlAutoPROC'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputControlAutoPROC'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._dataCollectionId is not None:
            self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
        if self._icatProcessDataDir is not None:
            self.icatProcessDataDir.export(outfile, level, name_='icatProcessDataDir')
        if self._dirN is not None:
            self.dirN.export(outfile, level, name_='dirN')
        if self._templateN is not None:
            self.templateN.export(outfile, level, name_='templateN')
        if self._fromN is not None:
            self.fromN.export(outfile, level, name_='fromN')
        if self._toN is not None:
            self.toN.export(outfile, level, name_='toN')
        if self._processDirectory is not None:
            self.processDirectory.export(outfile, level, name_='processDirectory')
        if self._doAnom is not None:
            self.doAnom.export(outfile, level, name_='doAnom')
        if self._doAnomAndNonanom is not None:
            self.doAnomAndNonanom.export(outfile, level, name_='doAnomAndNonanom')
        if self._symm is not None:
            self.symm.export(outfile, level, name_='symm')
        if self._cell is not None:
            self.cell.export(outfile, level, name_='cell')
        if self._reprocess is not None:
            self.reprocess.export(outfile, level, name_='reprocess')
        if self._lowResolutionLimit is not None:
            self.lowResolutionLimit.export(outfile, level, name_='lowResolutionLimit')
        if self._highResolutionLimit is not None:
            self.highResolutionLimit.export(outfile, level, name_='highResolutionLimit')
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
            nodeName_ == 'dirN':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'templateN':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setTemplateN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fromN':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFromN(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'toN':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setToN(obj_)
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
            nodeName_ == 'symm':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSymm(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cell':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setCell(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'reprocess':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setReprocess(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lowResolutionLimit':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setLowResolutionLimit(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'highResolutionLimit':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setHighResolutionLimit(obj_)
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
        self.export( oStreamString, 0, name_="XSDataInputControlAutoPROC" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputControlAutoPROC' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputControlAutoPROC is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputControlAutoPROC.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputControlAutoPROC()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputControlAutoPROC" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputControlAutoPROC()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputControlAutoPROC


class XSDataResultControlAutoPROC(XSDataResult):
    def __init__(self, status=None):
        XSDataResult.__init__(self, status)
    def export(self, outfile, level, name_='XSDataResultControlAutoPROC'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultControlAutoPROC'):
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
        self.export( oStreamString, 0, name_="XSDataResultControlAutoPROC" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultControlAutoPROC' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultControlAutoPROC is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultControlAutoPROC.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultControlAutoPROC()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultControlAutoPROC" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultControlAutoPROC()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultControlAutoPROC



# End of data representation classes.


