#!/usr/bin/env python

#
# Generated Thu Jul 4 02:44::24 2019 by EDGenerateDS.
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



class XSDataInputControlXDSAPP(XSDataInput):
    def __init__(self, configuration=None, reprocess=None, useXdsAsciiToXml=None, unitCell=None, spaceGroup=None, hdf5ToCbfDirectory=None, doAnomAndNonanom=None, doAnom=None, processDirectory=None, dataCollectionId=None, endImageNumber=None, startImageNumber=None):
        XSDataInput.__init__(self, configuration)
        if startImageNumber is None:
            self._startImageNumber = None
        elif startImageNumber.__class__.__name__ == "XSDataInteger":
            self._startImageNumber = startImageNumber
        else:
            strMessage = "ERROR! XSDataInputControlXDSAPP constructor argument 'startImageNumber' is not XSDataInteger but %s" % self._startImageNumber.__class__.__name__
            raise BaseException(strMessage)
        if endImageNumber is None:
            self._endImageNumber = None
        elif endImageNumber.__class__.__name__ == "XSDataInteger":
            self._endImageNumber = endImageNumber
        else:
            strMessage = "ERROR! XSDataInputControlXDSAPP constructor argument 'endImageNumber' is not XSDataInteger but %s" % self._endImageNumber.__class__.__name__
            raise BaseException(strMessage)
        if dataCollectionId is None:
            self._dataCollectionId = None
        elif dataCollectionId.__class__.__name__ == "XSDataInteger":
            self._dataCollectionId = dataCollectionId
        else:
            strMessage = "ERROR! XSDataInputControlXDSAPP constructor argument 'dataCollectionId' is not XSDataInteger but %s" % self._dataCollectionId.__class__.__name__
            raise BaseException(strMessage)
        if processDirectory is None:
            self._processDirectory = None
        elif processDirectory.__class__.__name__ == "XSDataFile":
            self._processDirectory = processDirectory
        else:
            strMessage = "ERROR! XSDataInputControlXDSAPP constructor argument 'processDirectory' is not XSDataFile but %s" % self._processDirectory.__class__.__name__
            raise BaseException(strMessage)
        if doAnom is None:
            self._doAnom = None
        elif doAnom.__class__.__name__ == "XSDataBoolean":
            self._doAnom = doAnom
        else:
            strMessage = "ERROR! XSDataInputControlXDSAPP constructor argument 'doAnom' is not XSDataBoolean but %s" % self._doAnom.__class__.__name__
            raise BaseException(strMessage)
        if doAnomAndNonanom is None:
            self._doAnomAndNonanom = None
        elif doAnomAndNonanom.__class__.__name__ == "XSDataBoolean":
            self._doAnomAndNonanom = doAnomAndNonanom
        else:
            strMessage = "ERROR! XSDataInputControlXDSAPP constructor argument 'doAnomAndNonanom' is not XSDataBoolean but %s" % self._doAnomAndNonanom.__class__.__name__
            raise BaseException(strMessage)
        if hdf5ToCbfDirectory is None:
            self._hdf5ToCbfDirectory = None
        elif hdf5ToCbfDirectory.__class__.__name__ == "XSDataFile":
            self._hdf5ToCbfDirectory = hdf5ToCbfDirectory
        else:
            strMessage = "ERROR! XSDataInputControlXDSAPP constructor argument 'hdf5ToCbfDirectory' is not XSDataFile but %s" % self._hdf5ToCbfDirectory.__class__.__name__
            raise BaseException(strMessage)
        if spaceGroup is None:
            self._spaceGroup = None
        elif spaceGroup.__class__.__name__ == "XSDataString":
            self._spaceGroup = spaceGroup
        else:
            strMessage = "ERROR! XSDataInputControlXDSAPP constructor argument 'spaceGroup' is not XSDataString but %s" % self._spaceGroup.__class__.__name__
            raise BaseException(strMessage)
        if unitCell is None:
            self._unitCell = None
        elif unitCell.__class__.__name__ == "XSDataString":
            self._unitCell = unitCell
        else:
            strMessage = "ERROR! XSDataInputControlXDSAPP constructor argument 'unitCell' is not XSDataString but %s" % self._unitCell.__class__.__name__
            raise BaseException(strMessage)
        if useXdsAsciiToXml is None:
            self._useXdsAsciiToXml = None
        elif useXdsAsciiToXml.__class__.__name__ == "XSDataBoolean":
            self._useXdsAsciiToXml = useXdsAsciiToXml
        else:
            strMessage = "ERROR! XSDataInputControlXDSAPP constructor argument 'useXdsAsciiToXml' is not XSDataBoolean but %s" % self._useXdsAsciiToXml.__class__.__name__
            raise BaseException(strMessage)
        if reprocess is None:
            self._reprocess = None
        elif reprocess.__class__.__name__ == "XSDataBoolean":
            self._reprocess = reprocess
        else:
            strMessage = "ERROR! XSDataInputControlXDSAPP constructor argument 'reprocess' is not XSDataBoolean but %s" % self._reprocess.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'startImageNumber' attribute
    def getStartImageNumber(self): return self._startImageNumber
    def setStartImageNumber(self, startImageNumber):
        if startImageNumber is None:
            self._startImageNumber = None
        elif startImageNumber.__class__.__name__ == "XSDataInteger":
            self._startImageNumber = startImageNumber
        else:
            strMessage = "ERROR! XSDataInputControlXDSAPP.setStartImageNumber argument is not XSDataInteger but %s" % startImageNumber.__class__.__name__
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
            strMessage = "ERROR! XSDataInputControlXDSAPP.setEndImageNumber argument is not XSDataInteger but %s" % endImageNumber.__class__.__name__
            raise BaseException(strMessage)
    def delEndImageNumber(self): self._endImageNumber = None
    endImageNumber = property(getEndImageNumber, setEndImageNumber, delEndImageNumber, "Property for endImageNumber")
    # Methods and properties for the 'dataCollectionId' attribute
    def getDataCollectionId(self): return self._dataCollectionId
    def setDataCollectionId(self, dataCollectionId):
        if dataCollectionId is None:
            self._dataCollectionId = None
        elif dataCollectionId.__class__.__name__ == "XSDataInteger":
            self._dataCollectionId = dataCollectionId
        else:
            strMessage = "ERROR! XSDataInputControlXDSAPP.setDataCollectionId argument is not XSDataInteger but %s" % dataCollectionId.__class__.__name__
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
            strMessage = "ERROR! XSDataInputControlXDSAPP.setProcessDirectory argument is not XSDataFile but %s" % processDirectory.__class__.__name__
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
            strMessage = "ERROR! XSDataInputControlXDSAPP.setDoAnom argument is not XSDataBoolean but %s" % doAnom.__class__.__name__
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
            strMessage = "ERROR! XSDataInputControlXDSAPP.setDoAnomAndNonanom argument is not XSDataBoolean but %s" % doAnomAndNonanom.__class__.__name__
            raise BaseException(strMessage)
    def delDoAnomAndNonanom(self): self._doAnomAndNonanom = None
    doAnomAndNonanom = property(getDoAnomAndNonanom, setDoAnomAndNonanom, delDoAnomAndNonanom, "Property for doAnomAndNonanom")
    # Methods and properties for the 'hdf5ToCbfDirectory' attribute
    def getHdf5ToCbfDirectory(self): return self._hdf5ToCbfDirectory
    def setHdf5ToCbfDirectory(self, hdf5ToCbfDirectory):
        if hdf5ToCbfDirectory is None:
            self._hdf5ToCbfDirectory = None
        elif hdf5ToCbfDirectory.__class__.__name__ == "XSDataFile":
            self._hdf5ToCbfDirectory = hdf5ToCbfDirectory
        else:
            strMessage = "ERROR! XSDataInputControlXDSAPP.setHdf5ToCbfDirectory argument is not XSDataFile but %s" % hdf5ToCbfDirectory.__class__.__name__
            raise BaseException(strMessage)
    def delHdf5ToCbfDirectory(self): self._hdf5ToCbfDirectory = None
    hdf5ToCbfDirectory = property(getHdf5ToCbfDirectory, setHdf5ToCbfDirectory, delHdf5ToCbfDirectory, "Property for hdf5ToCbfDirectory")
    # Methods and properties for the 'spaceGroup' attribute
    def getSpaceGroup(self): return self._spaceGroup
    def setSpaceGroup(self, spaceGroup):
        if spaceGroup is None:
            self._spaceGroup = None
        elif spaceGroup.__class__.__name__ == "XSDataString":
            self._spaceGroup = spaceGroup
        else:
            strMessage = "ERROR! XSDataInputControlXDSAPP.setSpaceGroup argument is not XSDataString but %s" % spaceGroup.__class__.__name__
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
            strMessage = "ERROR! XSDataInputControlXDSAPP.setUnitCell argument is not XSDataString but %s" % unitCell.__class__.__name__
            raise BaseException(strMessage)
    def delUnitCell(self): self._unitCell = None
    unitCell = property(getUnitCell, setUnitCell, delUnitCell, "Property for unitCell")
    # Methods and properties for the 'useXdsAsciiToXml' attribute
    def getUseXdsAsciiToXml(self): return self._useXdsAsciiToXml
    def setUseXdsAsciiToXml(self, useXdsAsciiToXml):
        if useXdsAsciiToXml is None:
            self._useXdsAsciiToXml = None
        elif useXdsAsciiToXml.__class__.__name__ == "XSDataBoolean":
            self._useXdsAsciiToXml = useXdsAsciiToXml
        else:
            strMessage = "ERROR! XSDataInputControlXDSAPP.setUseXdsAsciiToXml argument is not XSDataBoolean but %s" % useXdsAsciiToXml.__class__.__name__
            raise BaseException(strMessage)
    def delUseXdsAsciiToXml(self): self._useXdsAsciiToXml = None
    useXdsAsciiToXml = property(getUseXdsAsciiToXml, setUseXdsAsciiToXml, delUseXdsAsciiToXml, "Property for useXdsAsciiToXml")
    # Methods and properties for the 'reprocess' attribute
    def getReprocess(self): return self._reprocess
    def setReprocess(self, reprocess):
        if reprocess is None:
            self._reprocess = None
        elif reprocess.__class__.__name__ == "XSDataBoolean":
            self._reprocess = reprocess
        else:
            strMessage = "ERROR! XSDataInputControlXDSAPP.setReprocess argument is not XSDataBoolean but %s" % reprocess.__class__.__name__
            raise BaseException(strMessage)
    def delReprocess(self): self._reprocess = None
    reprocess = property(getReprocess, setReprocess, delReprocess, "Property for reprocess")
    def export(self, outfile, level, name_='XSDataInputControlXDSAPP'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputControlXDSAPP'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._startImageNumber is not None:
            self.startImageNumber.export(outfile, level, name_='startImageNumber')
        if self._endImageNumber is not None:
            self.endImageNumber.export(outfile, level, name_='endImageNumber')
        if self._dataCollectionId is not None:
            self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
        if self._processDirectory is not None:
            self.processDirectory.export(outfile, level, name_='processDirectory')
        if self._doAnom is not None:
            self.doAnom.export(outfile, level, name_='doAnom')
        if self._doAnomAndNonanom is not None:
            self.doAnomAndNonanom.export(outfile, level, name_='doAnomAndNonanom')
        if self._hdf5ToCbfDirectory is not None:
            self.hdf5ToCbfDirectory.export(outfile, level, name_='hdf5ToCbfDirectory')
        if self._spaceGroup is not None:
            self.spaceGroup.export(outfile, level, name_='spaceGroup')
        if self._unitCell is not None:
            self.unitCell.export(outfile, level, name_='unitCell')
        if self._useXdsAsciiToXml is not None:
            self.useXdsAsciiToXml.export(outfile, level, name_='useXdsAsciiToXml')
        if self._reprocess is not None:
            self.reprocess.export(outfile, level, name_='reprocess')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'startImageNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setStartImageNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'endImageNumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setEndImageNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
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
            nodeName_ == 'hdf5ToCbfDirectory':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setHdf5ToCbfDirectory(obj_)
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
            nodeName_ == 'useXdsAsciiToXml':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setUseXdsAsciiToXml(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'reprocess':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setReprocess(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputControlXDSAPP" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputControlXDSAPP' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputControlXDSAPP is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputControlXDSAPP.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputControlXDSAPP()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputControlXDSAPP" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputControlXDSAPP()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputControlXDSAPP


class XSDataResultControlXDSAPP(XSDataResult):
    def __init__(self, status=None):
        XSDataResult.__init__(self, status)
    def export(self, outfile, level, name_='XSDataResultControlXDSAPP'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultControlXDSAPP'):
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
        self.export( oStreamString, 0, name_="XSDataResultControlXDSAPP" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultControlXDSAPP' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultControlXDSAPP is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultControlXDSAPP.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultControlXDSAPP()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultControlXDSAPP" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultControlXDSAPP()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultControlXDSAPP



# End of data representation classes.


