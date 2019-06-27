#!/usr/bin/env python

#
# Generated Thu Jun 6 11:26::40 2019 by EDGenerateDS.
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
 "XSDataCommon": "mxPluginExec/plugins/EDPluginGroupCrystFEL-v1.0/datamodel/../../../../kernel/datamodel", \
}

try:
    from XSDataCommon import XSDataDouble
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
from XSDataCommon import XSDataDouble
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
    def __init__(self, configuration=None, baseFileName=None, resCutOff=None, spaceGroup=None, pointGroup=None, imagesFullPath=None, cellFile=None, geomFile=None):
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
        if imagesFullPath is None:
            self._imagesFullPath = None
        elif imagesFullPath.__class__.__name__ == "XSDataString":
            self._imagesFullPath = imagesFullPath
        else:
            strMessage = "ERROR! XSDataInputCrystFEL constructor argument 'imagesFullPath' is not XSDataString but %s" % self._imagesFullPath.__class__.__name__
            raise BaseException(strMessage)
        if pointGroup is None:
            self._pointGroup = None
        elif pointGroup.__class__.__name__ == "XSDataString":
            self._pointGroup = pointGroup
        else:
            strMessage = "ERROR! XSDataInputCrystFEL constructor argument 'pointGroup' is not XSDataString but %s" % self._pointGroup.__class__.__name__
            raise BaseException(strMessage)
        if spaceGroup is None:
            self._spaceGroup = None
        elif spaceGroup.__class__.__name__ == "XSDataString":
            self._spaceGroup = spaceGroup
        else:
            strMessage = "ERROR! XSDataInputCrystFEL constructor argument 'spaceGroup' is not XSDataString but %s" % self._spaceGroup.__class__.__name__
            raise BaseException(strMessage)
        if resCutOff is None:
            self._resCutOff = None
        elif resCutOff.__class__.__name__ == "XSDataString":
            self._resCutOff = resCutOff
        else:
            strMessage = "ERROR! XSDataInputCrystFEL constructor argument 'resCutOff' is not XSDataString but %s" % self._resCutOff.__class__.__name__
            raise BaseException(strMessage)
        if baseFileName is None:
            self._baseFileName = None
        elif baseFileName.__class__.__name__ == "XSDataString":
            self._baseFileName = baseFileName
        else:
            strMessage = "ERROR! XSDataInputCrystFEL constructor argument 'baseFileName' is not XSDataString but %s" % self._baseFileName.__class__.__name__
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
    # Methods and properties for the 'imagesFullPath' attribute
    def getImagesFullPath(self): return self._imagesFullPath
    def setImagesFullPath(self, imagesFullPath):
        if imagesFullPath is None:
            self._imagesFullPath = None
        elif imagesFullPath.__class__.__name__ == "XSDataString":
            self._imagesFullPath = imagesFullPath
        else:
            strMessage = "ERROR! XSDataInputCrystFEL.setImagesFullPath argument is not XSDataString but %s" % imagesFullPath.__class__.__name__
            raise BaseException(strMessage)
    def delImagesFullPath(self): self._imagesFullPath = None
    imagesFullPath = property(getImagesFullPath, setImagesFullPath, delImagesFullPath, "Property for imagesFullPath")
    # Methods and properties for the 'pointGroup' attribute
    def getPointGroup(self): return self._pointGroup
    def setPointGroup(self, pointGroup):
        if pointGroup is None:
            self._pointGroup = None
        elif pointGroup.__class__.__name__ == "XSDataString":
            self._pointGroup = pointGroup
        else:
            strMessage = "ERROR! XSDataInputCrystFEL.setPointGroup argument is not XSDataString but %s" % pointGroup.__class__.__name__
            raise BaseException(strMessage)
    def delPointGroup(self): self._pointGroup = None
    pointGroup = property(getPointGroup, setPointGroup, delPointGroup, "Property for pointGroup")
    # Methods and properties for the 'spaceGroup' attribute
    def getSpaceGroup(self): return self._spaceGroup
    def setSpaceGroup(self, spaceGroup):
        if spaceGroup is None:
            self._spaceGroup = None
        elif spaceGroup.__class__.__name__ == "XSDataString":
            self._spaceGroup = spaceGroup
        else:
            strMessage = "ERROR! XSDataInputCrystFEL.setSpaceGroup argument is not XSDataString but %s" % spaceGroup.__class__.__name__
            raise BaseException(strMessage)
    def delSpaceGroup(self): self._spaceGroup = None
    spaceGroup = property(getSpaceGroup, setSpaceGroup, delSpaceGroup, "Property for spaceGroup")
    # Methods and properties for the 'resCutOff' attribute
    def getResCutOff(self): return self._resCutOff
    def setResCutOff(self, resCutOff):
        if resCutOff is None:
            self._resCutOff = None
        elif resCutOff.__class__.__name__ == "XSDataString":
            self._resCutOff = resCutOff
        else:
            strMessage = "ERROR! XSDataInputCrystFEL.setResCutOff argument is not XSDataString but %s" % resCutOff.__class__.__name__
            raise BaseException(strMessage)
    def delResCutOff(self): self._resCutOff = None
    resCutOff = property(getResCutOff, setResCutOff, delResCutOff, "Property for resCutOff")
    # Methods and properties for the 'baseFileName' attribute
    def getBaseFileName(self): return self._baseFileName
    def setBaseFileName(self, baseFileName):
        if baseFileName is None:
            self._baseFileName = None
        elif baseFileName.__class__.__name__ == "XSDataString":
            self._baseFileName = baseFileName
        else:
            strMessage = "ERROR! XSDataInputCrystFEL.setBaseFileName argument is not XSDataString but %s" % baseFileName.__class__.__name__
            raise BaseException(strMessage)
    def delBaseFileName(self): self._baseFileName = None
    baseFileName = property(getBaseFileName, setBaseFileName, delBaseFileName, "Property for baseFileName")
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
        if self._imagesFullPath is not None:
            self.imagesFullPath.export(outfile, level, name_='imagesFullPath')
        else:
            warnEmptyAttribute("imagesFullPath", "XSDataString")
        if self._pointGroup is not None:
            self.pointGroup.export(outfile, level, name_='pointGroup')
        else:
            warnEmptyAttribute("pointGroup", "XSDataString")
        if self._spaceGroup is not None:
            self.spaceGroup.export(outfile, level, name_='spaceGroup')
        else:
            warnEmptyAttribute("spaceGroup", "XSDataString")
        if self._resCutOff is not None:
            self.resCutOff.export(outfile, level, name_='resCutOff')
        else:
            warnEmptyAttribute("resCutOff", "XSDataString")
        if self._baseFileName is not None:
            self.baseFileName.export(outfile, level, name_='baseFileName')
        else:
            warnEmptyAttribute("baseFileName", "XSDataString")
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
            nodeName_ == 'imagesFullPath':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setImagesFullPath(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pointGroup':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setPointGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spaceGroup':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSpaceGroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resCutOff':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setResCutOff(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'baseFileName':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setBaseFileName(obj_)
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
    def __init__(self, status=None, logFiles=None, summaryFile=None, dataFiles=None, comment=None, resolutionLimitHigh=None, resolutionLimitLow=None, overallCC=None, overallRsplit=None, overallSnr=None, overallRed=None, overallCompl=None):
        XSDataResult.__init__(self, status)
        if overallCompl is None:
            self._overallCompl = None
        elif overallCompl.__class__.__name__ == "XSDataDouble":
            self._overallCompl = overallCompl
        else:
            strMessage = "ERROR! XSDataResultCrystFEL constructor argument 'overallCompl' is not XSDataDouble but %s" % self._overallCompl.__class__.__name__
            raise BaseException(strMessage)
        if overallRed is None:
            self._overallRed = None
        elif overallRed.__class__.__name__ == "XSDataDouble":
            self._overallRed = overallRed
        else:
            strMessage = "ERROR! XSDataResultCrystFEL constructor argument 'overallRed' is not XSDataDouble but %s" % self._overallRed.__class__.__name__
            raise BaseException(strMessage)
        if overallSnr is None:
            self._overallSnr = None
        elif overallSnr.__class__.__name__ == "XSDataDouble":
            self._overallSnr = overallSnr
        else:
            strMessage = "ERROR! XSDataResultCrystFEL constructor argument 'overallSnr' is not XSDataDouble but %s" % self._overallSnr.__class__.__name__
            raise BaseException(strMessage)
        if overallRsplit is None:
            self._overallRsplit = None
        elif overallRsplit.__class__.__name__ == "XSDataDouble":
            self._overallRsplit = overallRsplit
        else:
            strMessage = "ERROR! XSDataResultCrystFEL constructor argument 'overallRsplit' is not XSDataDouble but %s" % self._overallRsplit.__class__.__name__
            raise BaseException(strMessage)
        if overallCC is None:
            self._overallCC = None
        elif overallCC.__class__.__name__ == "XSDataDouble":
            self._overallCC = overallCC
        else:
            strMessage = "ERROR! XSDataResultCrystFEL constructor argument 'overallCC' is not XSDataDouble but %s" % self._overallCC.__class__.__name__
            raise BaseException(strMessage)
        if resolutionLimitLow is None:
            self._resolutionLimitLow = None
        elif resolutionLimitLow.__class__.__name__ == "XSDataDouble":
            self._resolutionLimitLow = resolutionLimitLow
        else:
            strMessage = "ERROR! XSDataResultCrystFEL constructor argument 'resolutionLimitLow' is not XSDataDouble but %s" % self._resolutionLimitLow.__class__.__name__
            raise BaseException(strMessage)
        if resolutionLimitHigh is None:
            self._resolutionLimitHigh = None
        elif resolutionLimitHigh.__class__.__name__ == "XSDataDouble":
            self._resolutionLimitHigh = resolutionLimitHigh
        else:
            strMessage = "ERROR! XSDataResultCrystFEL constructor argument 'resolutionLimitHigh' is not XSDataDouble but %s" % self._resolutionLimitHigh.__class__.__name__
            raise BaseException(strMessage)
        if comment is None:
            self._comment = None
        elif comment.__class__.__name__ == "XSDataString":
            self._comment = comment
        else:
            strMessage = "ERROR! XSDataResultCrystFEL constructor argument 'comment' is not XSDataString but %s" % self._comment.__class__.__name__
            raise BaseException(strMessage)
        if dataFiles is None:
            self._dataFiles = []
        elif dataFiles.__class__.__name__ == "list":
            self._dataFiles = dataFiles
        else:
            strMessage = "ERROR! XSDataResultCrystFEL constructor argument 'dataFiles' is not list but %s" % self._dataFiles.__class__.__name__
            raise BaseException(strMessage)
        if summaryFile is None:
            self._summaryFile = None
        elif summaryFile.__class__.__name__ == "XSDataFile":
            self._summaryFile = summaryFile
        else:
            strMessage = "ERROR! XSDataResultCrystFEL constructor argument 'summaryFile' is not XSDataFile but %s" % self._summaryFile.__class__.__name__
            raise BaseException(strMessage)
        if logFiles is None:
            self._logFiles = []
        elif logFiles.__class__.__name__ == "list":
            self._logFiles = logFiles
        else:
            strMessage = "ERROR! XSDataResultCrystFEL constructor argument 'logFiles' is not list but %s" % self._logFiles.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'overallCompl' attribute
    def getOverallCompl(self): return self._overallCompl
    def setOverallCompl(self, overallCompl):
        if overallCompl is None:
            self._overallCompl = None
        elif overallCompl.__class__.__name__ == "XSDataDouble":
            self._overallCompl = overallCompl
        else:
            strMessage = "ERROR! XSDataResultCrystFEL.setOverallCompl argument is not XSDataDouble but %s" % overallCompl.__class__.__name__
            raise BaseException(strMessage)
    def delOverallCompl(self): self._overallCompl = None
    overallCompl = property(getOverallCompl, setOverallCompl, delOverallCompl, "Property for overallCompl")
    # Methods and properties for the 'overallRed' attribute
    def getOverallRed(self): return self._overallRed
    def setOverallRed(self, overallRed):
        if overallRed is None:
            self._overallRed = None
        elif overallRed.__class__.__name__ == "XSDataDouble":
            self._overallRed = overallRed
        else:
            strMessage = "ERROR! XSDataResultCrystFEL.setOverallRed argument is not XSDataDouble but %s" % overallRed.__class__.__name__
            raise BaseException(strMessage)
    def delOverallRed(self): self._overallRed = None
    overallRed = property(getOverallRed, setOverallRed, delOverallRed, "Property for overallRed")
    # Methods and properties for the 'overallSnr' attribute
    def getOverallSnr(self): return self._overallSnr
    def setOverallSnr(self, overallSnr):
        if overallSnr is None:
            self._overallSnr = None
        elif overallSnr.__class__.__name__ == "XSDataDouble":
            self._overallSnr = overallSnr
        else:
            strMessage = "ERROR! XSDataResultCrystFEL.setOverallSnr argument is not XSDataDouble but %s" % overallSnr.__class__.__name__
            raise BaseException(strMessage)
    def delOverallSnr(self): self._overallSnr = None
    overallSnr = property(getOverallSnr, setOverallSnr, delOverallSnr, "Property for overallSnr")
    # Methods and properties for the 'overallRsplit' attribute
    def getOverallRsplit(self): return self._overallRsplit
    def setOverallRsplit(self, overallRsplit):
        if overallRsplit is None:
            self._overallRsplit = None
        elif overallRsplit.__class__.__name__ == "XSDataDouble":
            self._overallRsplit = overallRsplit
        else:
            strMessage = "ERROR! XSDataResultCrystFEL.setOverallRsplit argument is not XSDataDouble but %s" % overallRsplit.__class__.__name__
            raise BaseException(strMessage)
    def delOverallRsplit(self): self._overallRsplit = None
    overallRsplit = property(getOverallRsplit, setOverallRsplit, delOverallRsplit, "Property for overallRsplit")
    # Methods and properties for the 'overallCC' attribute
    def getOverallCC(self): return self._overallCC
    def setOverallCC(self, overallCC):
        if overallCC is None:
            self._overallCC = None
        elif overallCC.__class__.__name__ == "XSDataDouble":
            self._overallCC = overallCC
        else:
            strMessage = "ERROR! XSDataResultCrystFEL.setOverallCC argument is not XSDataDouble but %s" % overallCC.__class__.__name__
            raise BaseException(strMessage)
    def delOverallCC(self): self._overallCC = None
    overallCC = property(getOverallCC, setOverallCC, delOverallCC, "Property for overallCC")
    # Methods and properties for the 'resolutionLimitLow' attribute
    def getResolutionLimitLow(self): return self._resolutionLimitLow
    def setResolutionLimitLow(self, resolutionLimitLow):
        if resolutionLimitLow is None:
            self._resolutionLimitLow = None
        elif resolutionLimitLow.__class__.__name__ == "XSDataDouble":
            self._resolutionLimitLow = resolutionLimitLow
        else:
            strMessage = "ERROR! XSDataResultCrystFEL.setResolutionLimitLow argument is not XSDataDouble but %s" % resolutionLimitLow.__class__.__name__
            raise BaseException(strMessage)
    def delResolutionLimitLow(self): self._resolutionLimitLow = None
    resolutionLimitLow = property(getResolutionLimitLow, setResolutionLimitLow, delResolutionLimitLow, "Property for resolutionLimitLow")
    # Methods and properties for the 'resolutionLimitHigh' attribute
    def getResolutionLimitHigh(self): return self._resolutionLimitHigh
    def setResolutionLimitHigh(self, resolutionLimitHigh):
        if resolutionLimitHigh is None:
            self._resolutionLimitHigh = None
        elif resolutionLimitHigh.__class__.__name__ == "XSDataDouble":
            self._resolutionLimitHigh = resolutionLimitHigh
        else:
            strMessage = "ERROR! XSDataResultCrystFEL.setResolutionLimitHigh argument is not XSDataDouble but %s" % resolutionLimitHigh.__class__.__name__
            raise BaseException(strMessage)
    def delResolutionLimitHigh(self): self._resolutionLimitHigh = None
    resolutionLimitHigh = property(getResolutionLimitHigh, setResolutionLimitHigh, delResolutionLimitHigh, "Property for resolutionLimitHigh")
    # Methods and properties for the 'comment' attribute
    def getComment(self): return self._comment
    def setComment(self, comment):
        if comment is None:
            self._comment = None
        elif comment.__class__.__name__ == "XSDataString":
            self._comment = comment
        else:
            strMessage = "ERROR! XSDataResultCrystFEL.setComment argument is not XSDataString but %s" % comment.__class__.__name__
            raise BaseException(strMessage)
    def delComment(self): self._comment = None
    comment = property(getComment, setComment, delComment, "Property for comment")
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
    # Methods and properties for the 'summaryFile' attribute
    def getSummaryFile(self): return self._summaryFile
    def setSummaryFile(self, summaryFile):
        if summaryFile is None:
            self._summaryFile = None
        elif summaryFile.__class__.__name__ == "XSDataFile":
            self._summaryFile = summaryFile
        else:
            strMessage = "ERROR! XSDataResultCrystFEL.setSummaryFile argument is not XSDataFile but %s" % summaryFile.__class__.__name__
            raise BaseException(strMessage)
    def delSummaryFile(self): self._summaryFile = None
    summaryFile = property(getSummaryFile, setSummaryFile, delSummaryFile, "Property for summaryFile")
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
        if self._overallCompl is not None:
            self.overallCompl.export(outfile, level, name_='overallCompl')
        else:
            warnEmptyAttribute("overallCompl", "XSDataDouble")
        if self._overallRed is not None:
            self.overallRed.export(outfile, level, name_='overallRed')
        else:
            warnEmptyAttribute("overallRed", "XSDataDouble")
        if self._overallSnr is not None:
            self.overallSnr.export(outfile, level, name_='overallSnr')
        else:
            warnEmptyAttribute("overallSnr", "XSDataDouble")
        if self._overallRsplit is not None:
            self.overallRsplit.export(outfile, level, name_='overallRsplit')
        else:
            warnEmptyAttribute("overallRsplit", "XSDataDouble")
        if self._overallCC is not None:
            self.overallCC.export(outfile, level, name_='overallCC')
        else:
            warnEmptyAttribute("overallCC", "XSDataDouble")
        if self._resolutionLimitLow is not None:
            self.resolutionLimitLow.export(outfile, level, name_='resolutionLimitLow')
        else:
            warnEmptyAttribute("resolutionLimitLow", "XSDataDouble")
        if self._resolutionLimitHigh is not None:
            self.resolutionLimitHigh.export(outfile, level, name_='resolutionLimitHigh')
        else:
            warnEmptyAttribute("resolutionLimitHigh", "XSDataDouble")
        if self._comment is not None:
            self.comment.export(outfile, level, name_='comment')
        else:
            warnEmptyAttribute("comment", "XSDataString")
        for dataFiles_ in self.getDataFiles():
            dataFiles_.export(outfile, level, name_='dataFiles')
        if self.getDataFiles() == []:
            warnEmptyAttribute("dataFiles", "XSDataFile")
        if self._summaryFile is not None:
            self.summaryFile.export(outfile, level, name_='summaryFile')
        else:
            warnEmptyAttribute("summaryFile", "XSDataFile")
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
            nodeName_ == 'overallCompl':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setOverallCompl(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'overallRed':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setOverallRed(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'overallSnr':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setOverallSnr(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'overallRsplit':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setOverallRsplit(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'overallCC':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setOverallCC(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolutionLimitLow':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setResolutionLimitLow(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resolutionLimitHigh':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setResolutionLimitHigh(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comment':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setComment(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataFiles':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.dataFiles.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'summaryFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSummaryFile(obj_)
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


