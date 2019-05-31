#!/usr/bin/env python

#
# Generated Fri May 31 03:13::11 2019 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = { \
 "XSDataCommon": "mxv1/plugins/EDPluginControlCrystFEL-v1.0/datamodel/../../../../kernel/datamodel", \
 "XSDataCommon": "mxv1/plugins/EDPluginControlCrystFEL-v1.0/datamodel/../../../../kernel/datamodel", \
 "XSDataCommon": "mxv1/plugins/EDPluginControlCrystFEL-v1.0/datamodel/../../../../kernel/datamodel", \
 "XSDataCommon": "mxv1/plugins/EDPluginControlCrystFEL-v1.0/datamodel/../../../../kernel/datamodel", \
 "XSDataCommon": "mxv1/plugins/EDPluginControlCrystFEL-v1.0/datamodel/../../../../kernel/datamodel", \
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



class XSDataInputControlCrystFEL(XSDataInput):
    def __init__(self, configuration=None, mtzFile=None, hklFile=None, streamFile=None, imagesFullPath=None, cellFile=None, geomFile=None, processDirectory=None, dataCollectionId=None):
        XSDataInput.__init__(self, configuration)
        if dataCollectionId is None:
            self._dataCollectionId = None
        elif dataCollectionId.__class__.__name__ == "XSDataInteger":
            self._dataCollectionId = dataCollectionId
        else:
            strMessage = "ERROR! XSDataInputControlCrystFEL constructor argument 'dataCollectionId' is not XSDataInteger but %s" % self._dataCollectionId.__class__.__name__
            raise BaseException(strMessage)
        if processDirectory is None:
            self._processDirectory = None
        elif processDirectory.__class__.__name__ == "XSDataFile":
            self._processDirectory = processDirectory
        else:
            strMessage = "ERROR! XSDataInputControlCrystFEL constructor argument 'processDirectory' is not XSDataFile but %s" % self._processDirectory.__class__.__name__
            raise BaseException(strMessage)
        if geomFile is None:
            self._geomFile = None
        elif geomFile.__class__.__name__ == "XSDataString":
            self._geomFile = geomFile
        else:
            strMessage = "ERROR! XSDataInputControlCrystFEL constructor argument 'geomFile' is not XSDataString but %s" % self._geomFile.__class__.__name__
            raise BaseException(strMessage)
        if cellFile is None:
            self._cellFile = None
        elif cellFile.__class__.__name__ == "XSDataString":
            self._cellFile = cellFile
        else:
            strMessage = "ERROR! XSDataInputControlCrystFEL constructor argument 'cellFile' is not XSDataString but %s" % self._cellFile.__class__.__name__
            raise BaseException(strMessage)
        if imagesFullPath is None:
            self._imagesFullPath = None
        elif imagesFullPath.__class__.__name__ == "XSDataString":
            self._imagesFullPath = imagesFullPath
        else:
            strMessage = "ERROR! XSDataInputControlCrystFEL constructor argument 'imagesFullPath' is not XSDataString but %s" % self._imagesFullPath.__class__.__name__
            raise BaseException(strMessage)
        if streamFile is None:
            self._streamFile = None
        elif streamFile.__class__.__name__ == "XSDataString":
            self._streamFile = streamFile
        else:
            strMessage = "ERROR! XSDataInputControlCrystFEL constructor argument 'streamFile' is not XSDataString but %s" % self._streamFile.__class__.__name__
            raise BaseException(strMessage)
        if hklFile is None:
            self._hklFile = None
        elif hklFile.__class__.__name__ == "XSDataString":
            self._hklFile = hklFile
        else:
            strMessage = "ERROR! XSDataInputControlCrystFEL constructor argument 'hklFile' is not XSDataString but %s" % self._hklFile.__class__.__name__
            raise BaseException(strMessage)
        if mtzFile is None:
            self._mtzFile = None
        elif mtzFile.__class__.__name__ == "XSDataString":
            self._mtzFile = mtzFile
        else:
            strMessage = "ERROR! XSDataInputControlCrystFEL constructor argument 'mtzFile' is not XSDataString but %s" % self._mtzFile.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'dataCollectionId' attribute
    def getDataCollectionId(self): return self._dataCollectionId
    def setDataCollectionId(self, dataCollectionId):
        if dataCollectionId is None:
            self._dataCollectionId = None
        elif dataCollectionId.__class__.__name__ == "XSDataInteger":
            self._dataCollectionId = dataCollectionId
        else:
            strMessage = "ERROR! XSDataInputControlCrystFEL.setDataCollectionId argument is not XSDataInteger but %s" % dataCollectionId.__class__.__name__
            raise BaseException(strMessage)
    def delDataCollectionId(self): self._dataCollectionId = None
    dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
    # Methods and properties for the 'processDirectory' attribute
    def getProcessDirectory(self): return self._processDirectory
    def setProcessDirectory(self, processDirectory):
        if processDirectory is None:
            self._processDirectory = None
        elif processDirectory.__class__.__name__ == "XSDataFile":
            self._processDirectory = processDirectory
        else:
            strMessage = "ERROR! XSDataInputControlCrystFEL.setProcessDirectory argument is not XSDataFile but %s" % processDirectory.__class__.__name__
            raise BaseException(strMessage)
    def delProcessDirectory(self): self._processDirectory = None
    processDirectory = property(getProcessDirectory, setProcessDirectory, delProcessDirectory, "Property for processDirectory")
    # Methods and properties for the 'geomFile' attribute
    def getGeomFile(self): return self._geomFile
    def setGeomFile(self, geomFile):
        if geomFile is None:
            self._geomFile = None
        elif geomFile.__class__.__name__ == "XSDataString":
            self._geomFile = geomFile
        else:
            strMessage = "ERROR! XSDataInputControlCrystFEL.setGeomFile argument is not XSDataString but %s" % geomFile.__class__.__name__
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
            strMessage = "ERROR! XSDataInputControlCrystFEL.setCellFile argument is not XSDataString but %s" % cellFile.__class__.__name__
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
            strMessage = "ERROR! XSDataInputControlCrystFEL.setImagesFullPath argument is not XSDataString but %s" % imagesFullPath.__class__.__name__
            raise BaseException(strMessage)
    def delImagesFullPath(self): self._imagesFullPath = None
    imagesFullPath = property(getImagesFullPath, setImagesFullPath, delImagesFullPath, "Property for imagesFullPath")
    # Methods and properties for the 'streamFile' attribute
    def getStreamFile(self): return self._streamFile
    def setStreamFile(self, streamFile):
        if streamFile is None:
            self._streamFile = None
        elif streamFile.__class__.__name__ == "XSDataString":
            self._streamFile = streamFile
        else:
            strMessage = "ERROR! XSDataInputControlCrystFEL.setStreamFile argument is not XSDataString but %s" % streamFile.__class__.__name__
            raise BaseException(strMessage)
    def delStreamFile(self): self._streamFile = None
    streamFile = property(getStreamFile, setStreamFile, delStreamFile, "Property for streamFile")
    # Methods and properties for the 'hklFile' attribute
    def getHklFile(self): return self._hklFile
    def setHklFile(self, hklFile):
        if hklFile is None:
            self._hklFile = None
        elif hklFile.__class__.__name__ == "XSDataString":
            self._hklFile = hklFile
        else:
            strMessage = "ERROR! XSDataInputControlCrystFEL.setHklFile argument is not XSDataString but %s" % hklFile.__class__.__name__
            raise BaseException(strMessage)
    def delHklFile(self): self._hklFile = None
    hklFile = property(getHklFile, setHklFile, delHklFile, "Property for hklFile")
    # Methods and properties for the 'mtzFile' attribute
    def getMtzFile(self): return self._mtzFile
    def setMtzFile(self, mtzFile):
        if mtzFile is None:
            self._mtzFile = None
        elif mtzFile.__class__.__name__ == "XSDataString":
            self._mtzFile = mtzFile
        else:
            strMessage = "ERROR! XSDataInputControlCrystFEL.setMtzFile argument is not XSDataString but %s" % mtzFile.__class__.__name__
            raise BaseException(strMessage)
    def delMtzFile(self): self._mtzFile = None
    mtzFile = property(getMtzFile, setMtzFile, delMtzFile, "Property for mtzFile")
    def export(self, outfile, level, name_='XSDataInputControlCrystFEL'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputControlCrystFEL'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._dataCollectionId is not None:
            self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
        if self._processDirectory is not None:
            self.processDirectory.export(outfile, level, name_='processDirectory')
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
        if self._streamFile is not None:
            self.streamFile.export(outfile, level, name_='streamFile')
        else:
            warnEmptyAttribute("streamFile", "XSDataString")
        if self._hklFile is not None:
            self.hklFile.export(outfile, level, name_='hklFile')
        else:
            warnEmptyAttribute("hklFile", "XSDataString")
        if self._mtzFile is not None:
            self.mtzFile.export(outfile, level, name_='mtzFile')
        else:
            warnEmptyAttribute("mtzFile", "XSDataString")
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
            nodeName_ == 'processDirectory':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setProcessDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
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
            nodeName_ == 'streamFile':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setStreamFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hklFile':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setHklFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mtzFile':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setMtzFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputControlCrystFEL" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputControlCrystFEL' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputControlCrystFEL is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputControlCrystFEL.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputControlCrystFEL()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputControlCrystFEL" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputControlCrystFEL()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputControlCrystFEL


class XSDataResultControlCrystFEL(XSDataResult):
    def __init__(self, status=None):
        XSDataResult.__init__(self, status)
    def export(self, outfile, level, name_='XSDataResultControlCrystFEL'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultControlCrystFEL'):
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
        self.export( oStreamString, 0, name_="XSDataResultControlCrystFEL" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultControlCrystFEL' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultControlCrystFEL is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultControlCrystFEL.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultControlCrystFEL()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultControlCrystFEL" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultControlCrystFEL()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultControlCrystFEL



# End of data representation classes.


