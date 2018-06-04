#!/usr/bin/env python

#
# Generated Thu May 17 11:11::09 2018 by EDGenerateDS.
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
    from XSDataCommon import XSData
    from XSDataCommon import XSDataBoolean
    from XSDataCommon import XSDataDouble
    from XSDataCommon import XSDataResult
    from XSDataCommon import XSDataString
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataInteger
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
from XSDataCommon import XSData
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger




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



class XSDataAutoPROCIdentifier(XSData):
    def __init__(self, toN=None, fromN=None, templateN=None, dirN=None, idN=None):
        XSData.__init__(self, )
        if idN is None:
            self._idN = None
        elif idN.__class__.__name__ == "XSDataString":
            self._idN = idN
        else:
            strMessage = "ERROR! XSDataAutoPROCIdentifier constructor argument 'idN' is not XSDataString but %s" % self._idN.__class__.__name__
            raise BaseException(strMessage)
        if dirN is None:
            self._dirN = None
        elif dirN.__class__.__name__ == "XSDataFile":
            self._dirN = dirN
        else:
            strMessage = "ERROR! XSDataAutoPROCIdentifier constructor argument 'dirN' is not XSDataFile but %s" % self._dirN.__class__.__name__
            raise BaseException(strMessage)
        if templateN is None:
            self._templateN = None
        elif templateN.__class__.__name__ == "XSDataString":
            self._templateN = templateN
        else:
            strMessage = "ERROR! XSDataAutoPROCIdentifier constructor argument 'templateN' is not XSDataString but %s" % self._templateN.__class__.__name__
            raise BaseException(strMessage)
        if fromN is None:
            self._fromN = None
        elif fromN.__class__.__name__ == "XSDataInteger":
            self._fromN = fromN
        else:
            strMessage = "ERROR! XSDataAutoPROCIdentifier constructor argument 'fromN' is not XSDataInteger but %s" % self._fromN.__class__.__name__
            raise BaseException(strMessage)
        if toN is None:
            self._toN = None
        elif toN.__class__.__name__ == "XSDataInteger":
            self._toN = toN
        else:
            strMessage = "ERROR! XSDataAutoPROCIdentifier constructor argument 'toN' is not XSDataInteger but %s" % self._toN.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'idN' attribute
    def getIdN(self): return self._idN
    def setIdN(self, idN):
        if idN is None:
            self._idN = None
        elif idN.__class__.__name__ == "XSDataString":
            self._idN = idN
        else:
            strMessage = "ERROR! XSDataAutoPROCIdentifier.setIdN argument is not XSDataString but %s" % idN.__class__.__name__
            raise BaseException(strMessage)
    def delIdN(self): self._idN = None
    idN = property(getIdN, setIdN, delIdN, "Property for idN")
    # Methods and properties for the 'dirN' attribute
    def getDirN(self): return self._dirN
    def setDirN(self, dirN):
        if dirN is None:
            self._dirN = None
        elif dirN.__class__.__name__ == "XSDataFile":
            self._dirN = dirN
        else:
            strMessage = "ERROR! XSDataAutoPROCIdentifier.setDirN argument is not XSDataFile but %s" % dirN.__class__.__name__
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
            strMessage = "ERROR! XSDataAutoPROCIdentifier.setTemplateN argument is not XSDataString but %s" % templateN.__class__.__name__
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
            strMessage = "ERROR! XSDataAutoPROCIdentifier.setFromN argument is not XSDataInteger but %s" % fromN.__class__.__name__
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
            strMessage = "ERROR! XSDataAutoPROCIdentifier.setToN argument is not XSDataInteger but %s" % toN.__class__.__name__
            raise BaseException(strMessage)
    def delToN(self): self._toN = None
    toN = property(getToN, setToN, delToN, "Property for toN")
    def export(self, outfile, level, name_='XSDataAutoPROCIdentifier'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataAutoPROCIdentifier'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._idN is not None:
            self.idN.export(outfile, level, name_='idN')
        else:
            warnEmptyAttribute("idN", "XSDataString")
        if self._dirN is not None:
            self.dirN.export(outfile, level, name_='dirN')
        else:
            warnEmptyAttribute("dirN", "XSDataFile")
        if self._templateN is not None:
            self.templateN.export(outfile, level, name_='templateN')
        else:
            warnEmptyAttribute("templateN", "XSDataString")
        if self._fromN is not None:
            self.fromN.export(outfile, level, name_='fromN')
        else:
            warnEmptyAttribute("fromN", "XSDataInteger")
        if self._toN is not None:
            self.toN.export(outfile, level, name_='toN')
        else:
            warnEmptyAttribute("toN", "XSDataInteger")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'idN':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setIdN(obj_)
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
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataAutoPROCIdentifier" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataAutoPROCIdentifier' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataAutoPROCIdentifier is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataAutoPROCIdentifier.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAutoPROCIdentifier()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataAutoPROCIdentifier" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAutoPROCIdentifier()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataAutoPROCIdentifier


class XSDataInputAutoPROC(XSDataInput):
    def __init__(self, configuration=None, cell=None, symm=None, masterH5=None, refMTZ=None, anomalous=None, highResolutionLimit=None, lowResolutionLimit=None, identifier=None):
        XSDataInput.__init__(self, configuration)
        if identifier is None:
            self._identifier = []
        elif identifier.__class__.__name__ == "list":
            self._identifier = identifier
        else:
            strMessage = "ERROR! XSDataInputAutoPROC constructor argument 'identifier' is not list but %s" % self._identifier.__class__.__name__
            raise BaseException(strMessage)
        if lowResolutionLimit is None:
            self._lowResolutionLimit = None
        elif lowResolutionLimit.__class__.__name__ == "XSDataDouble":
            self._lowResolutionLimit = lowResolutionLimit
        else:
            strMessage = "ERROR! XSDataInputAutoPROC constructor argument 'lowResolutionLimit' is not XSDataDouble but %s" % self._lowResolutionLimit.__class__.__name__
            raise BaseException(strMessage)
        if highResolutionLimit is None:
            self._highResolutionLimit = None
        elif highResolutionLimit.__class__.__name__ == "XSDataDouble":
            self._highResolutionLimit = highResolutionLimit
        else:
            strMessage = "ERROR! XSDataInputAutoPROC constructor argument 'highResolutionLimit' is not XSDataDouble but %s" % self._highResolutionLimit.__class__.__name__
            raise BaseException(strMessage)
        if anomalous is None:
            self._anomalous = None
        elif anomalous.__class__.__name__ == "XSDataBoolean":
            self._anomalous = anomalous
        else:
            strMessage = "ERROR! XSDataInputAutoPROC constructor argument 'anomalous' is not XSDataBoolean but %s" % self._anomalous.__class__.__name__
            raise BaseException(strMessage)
        if refMTZ is None:
            self._refMTZ = None
        elif refMTZ.__class__.__name__ == "XSDataFile":
            self._refMTZ = refMTZ
        else:
            strMessage = "ERROR! XSDataInputAutoPROC constructor argument 'refMTZ' is not XSDataFile but %s" % self._refMTZ.__class__.__name__
            raise BaseException(strMessage)
        if masterH5 is None:
            self._masterH5 = None
        elif masterH5.__class__.__name__ == "XSDataFile":
            self._masterH5 = masterH5
        else:
            strMessage = "ERROR! XSDataInputAutoPROC constructor argument 'masterH5' is not XSDataFile but %s" % self._masterH5.__class__.__name__
            raise BaseException(strMessage)
        if symm is None:
            self._symm = None
        elif symm.__class__.__name__ == "XSDataString":
            self._symm = symm
        else:
            strMessage = "ERROR! XSDataInputAutoPROC constructor argument 'symm' is not XSDataString but %s" % self._symm.__class__.__name__
            raise BaseException(strMessage)
        if cell is None:
            self._cell = None
        elif cell.__class__.__name__ == "XSDataString":
            self._cell = cell
        else:
            strMessage = "ERROR! XSDataInputAutoPROC constructor argument 'cell' is not XSDataString but %s" % self._cell.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'identifier' attribute
    def getIdentifier(self): return self._identifier
    def setIdentifier(self, identifier):
        if identifier is None:
            self._identifier = []
        elif identifier.__class__.__name__ == "list":
            self._identifier = identifier
        else:
            strMessage = "ERROR! XSDataInputAutoPROC.setIdentifier argument is not list but %s" % identifier.__class__.__name__
            raise BaseException(strMessage)
    def delIdentifier(self): self._identifier = None
    identifier = property(getIdentifier, setIdentifier, delIdentifier, "Property for identifier")
    def addIdentifier(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputAutoPROC.addIdentifier argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataAutoPROCIdentifier":
            self._identifier.append(value)
        else:
            strMessage = "ERROR! XSDataInputAutoPROC.addIdentifier argument is not XSDataAutoPROCIdentifier but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertIdentifier(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputAutoPROC.insertIdentifier argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputAutoPROC.insertIdentifier argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataAutoPROCIdentifier":
            self._identifier[index] = value
        else:
            strMessage = "ERROR! XSDataInputAutoPROC.addIdentifier argument is not XSDataAutoPROCIdentifier but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'lowResolutionLimit' attribute
    def getLowResolutionLimit(self): return self._lowResolutionLimit
    def setLowResolutionLimit(self, lowResolutionLimit):
        if lowResolutionLimit is None:
            self._lowResolutionLimit = None
        elif lowResolutionLimit.__class__.__name__ == "XSDataDouble":
            self._lowResolutionLimit = lowResolutionLimit
        else:
            strMessage = "ERROR! XSDataInputAutoPROC.setLowResolutionLimit argument is not XSDataDouble but %s" % lowResolutionLimit.__class__.__name__
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
            strMessage = "ERROR! XSDataInputAutoPROC.setHighResolutionLimit argument is not XSDataDouble but %s" % highResolutionLimit.__class__.__name__
            raise BaseException(strMessage)
    def delHighResolutionLimit(self): self._highResolutionLimit = None
    highResolutionLimit = property(getHighResolutionLimit, setHighResolutionLimit, delHighResolutionLimit, "Property for highResolutionLimit")
    # Methods and properties for the 'anomalous' attribute
    def getAnomalous(self): return self._anomalous
    def setAnomalous(self, anomalous):
        if anomalous is None:
            self._anomalous = None
        elif anomalous.__class__.__name__ == "XSDataBoolean":
            self._anomalous = anomalous
        else:
            strMessage = "ERROR! XSDataInputAutoPROC.setAnomalous argument is not XSDataBoolean but %s" % anomalous.__class__.__name__
            raise BaseException(strMessage)
    def delAnomalous(self): self._anomalous = None
    anomalous = property(getAnomalous, setAnomalous, delAnomalous, "Property for anomalous")
    # Methods and properties for the 'refMTZ' attribute
    def getRefMTZ(self): return self._refMTZ
    def setRefMTZ(self, refMTZ):
        if refMTZ is None:
            self._refMTZ = None
        elif refMTZ.__class__.__name__ == "XSDataFile":
            self._refMTZ = refMTZ
        else:
            strMessage = "ERROR! XSDataInputAutoPROC.setRefMTZ argument is not XSDataFile but %s" % refMTZ.__class__.__name__
            raise BaseException(strMessage)
    def delRefMTZ(self): self._refMTZ = None
    refMTZ = property(getRefMTZ, setRefMTZ, delRefMTZ, "Property for refMTZ")
    # Methods and properties for the 'masterH5' attribute
    def getMasterH5(self): return self._masterH5
    def setMasterH5(self, masterH5):
        if masterH5 is None:
            self._masterH5 = None
        elif masterH5.__class__.__name__ == "XSDataFile":
            self._masterH5 = masterH5
        else:
            strMessage = "ERROR! XSDataInputAutoPROC.setMasterH5 argument is not XSDataFile but %s" % masterH5.__class__.__name__
            raise BaseException(strMessage)
    def delMasterH5(self): self._masterH5 = None
    masterH5 = property(getMasterH5, setMasterH5, delMasterH5, "Property for masterH5")
    # Methods and properties for the 'symm' attribute
    def getSymm(self): return self._symm
    def setSymm(self, symm):
        if symm is None:
            self._symm = None
        elif symm.__class__.__name__ == "XSDataString":
            self._symm = symm
        else:
            strMessage = "ERROR! XSDataInputAutoPROC.setSymm argument is not XSDataString but %s" % symm.__class__.__name__
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
            strMessage = "ERROR! XSDataInputAutoPROC.setCell argument is not XSDataString but %s" % cell.__class__.__name__
            raise BaseException(strMessage)
    def delCell(self): self._cell = None
    cell = property(getCell, setCell, delCell, "Property for cell")
    def export(self, outfile, level, name_='XSDataInputAutoPROC'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputAutoPROC'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for identifier_ in self.getIdentifier():
            identifier_.export(outfile, level, name_='identifier')
        if self.getIdentifier() == []:
            warnEmptyAttribute("identifier", "XSDataAutoPROCIdentifier")
        if self._lowResolutionLimit is not None:
            self.lowResolutionLimit.export(outfile, level, name_='lowResolutionLimit')
        if self._highResolutionLimit is not None:
            self.highResolutionLimit.export(outfile, level, name_='highResolutionLimit')
        if self._anomalous is not None:
            self.anomalous.export(outfile, level, name_='anomalous')
        if self._refMTZ is not None:
            self.refMTZ.export(outfile, level, name_='refMTZ')
        if self._masterH5 is not None:
            self.masterH5.export(outfile, level, name_='masterH5')
        if self._symm is not None:
            self.symm.export(outfile, level, name_='symm')
        if self._cell is not None:
            self.cell.export(outfile, level, name_='cell')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'identifier':
            obj_ = XSDataAutoPROCIdentifier()
            obj_.build(child_)
            self.identifier.append(obj_)
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
            nodeName_ == 'anomalous':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setAnomalous(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refMTZ':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setRefMTZ(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'masterH5':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setMasterH5(obj_)
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
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputAutoPROC" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputAutoPROC' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputAutoPROC is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputAutoPROC.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputAutoPROC()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputAutoPROC" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputAutoPROC()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputAutoPROC


class XSDataResultAutoPROC(XSDataResult):
    def __init__(self, status=None, reportPdf_staraniso=None, reportPdf=None, ispybXML_staraniso=None, ispybXML=None, processDirectory=None, workingDirectory=None, logFile=None):
        XSDataResult.__init__(self, status)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultAutoPROC constructor argument 'logFile' is not XSDataFile but %s" % self._logFile.__class__.__name__
            raise BaseException(strMessage)
        if workingDirectory is None:
            self._workingDirectory = None
        elif workingDirectory.__class__.__name__ == "XSDataFile":
            self._workingDirectory = workingDirectory
        else:
            strMessage = "ERROR! XSDataResultAutoPROC constructor argument 'workingDirectory' is not XSDataFile but %s" % self._workingDirectory.__class__.__name__
            raise BaseException(strMessage)
        if processDirectory is None:
            self._processDirectory = []
        elif processDirectory.__class__.__name__ == "list":
            self._processDirectory = processDirectory
        else:
            strMessage = "ERROR! XSDataResultAutoPROC constructor argument 'processDirectory' is not list but %s" % self._processDirectory.__class__.__name__
            raise BaseException(strMessage)
        if ispybXML is None:
            self._ispybXML = None
        elif ispybXML.__class__.__name__ == "XSDataFile":
            self._ispybXML = ispybXML
        else:
            strMessage = "ERROR! XSDataResultAutoPROC constructor argument 'ispybXML' is not XSDataFile but %s" % self._ispybXML.__class__.__name__
            raise BaseException(strMessage)
        if ispybXML_staraniso is None:
            self._ispybXML_staraniso = None
        elif ispybXML_staraniso.__class__.__name__ == "XSDataFile":
            self._ispybXML_staraniso = ispybXML_staraniso
        else:
            strMessage = "ERROR! XSDataResultAutoPROC constructor argument 'ispybXML_staraniso' is not XSDataFile but %s" % self._ispybXML_staraniso.__class__.__name__
            raise BaseException(strMessage)
        if reportPdf is None:
            self._reportPdf = None
        elif reportPdf.__class__.__name__ == "XSDataFile":
            self._reportPdf = reportPdf
        else:
            strMessage = "ERROR! XSDataResultAutoPROC constructor argument 'reportPdf' is not XSDataFile but %s" % self._reportPdf.__class__.__name__
            raise BaseException(strMessage)
        if reportPdf_staraniso is None:
            self._reportPdf_staraniso = None
        elif reportPdf_staraniso.__class__.__name__ == "XSDataFile":
            self._reportPdf_staraniso = reportPdf_staraniso
        else:
            strMessage = "ERROR! XSDataResultAutoPROC constructor argument 'reportPdf_staraniso' is not XSDataFile but %s" % self._reportPdf_staraniso.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultAutoPROC.setLogFile argument is not XSDataFile but %s" % logFile.__class__.__name__
            raise BaseException(strMessage)
    def delLogFile(self): self._logFile = None
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    # Methods and properties for the 'workingDirectory' attribute
    def getWorkingDirectory(self): return self._workingDirectory
    def setWorkingDirectory(self, workingDirectory):
        if workingDirectory is None:
            self._workingDirectory = None
        elif workingDirectory.__class__.__name__ == "XSDataFile":
            self._workingDirectory = workingDirectory
        else:
            strMessage = "ERROR! XSDataResultAutoPROC.setWorkingDirectory argument is not XSDataFile but %s" % workingDirectory.__class__.__name__
            raise BaseException(strMessage)
    def delWorkingDirectory(self): self._workingDirectory = None
    workingDirectory = property(getWorkingDirectory, setWorkingDirectory, delWorkingDirectory, "Property for workingDirectory")
    # Methods and properties for the 'processDirectory' attribute
    def getProcessDirectory(self): return self._processDirectory
    def setProcessDirectory(self, processDirectory):
        if processDirectory is None:
            self._processDirectory = []
        elif processDirectory.__class__.__name__ == "list":
            self._processDirectory = processDirectory
        else:
            strMessage = "ERROR! XSDataResultAutoPROC.setProcessDirectory argument is not list but %s" % processDirectory.__class__.__name__
            raise BaseException(strMessage)
    def delProcessDirectory(self): self._processDirectory = None
    processDirectory = property(getProcessDirectory, setProcessDirectory, delProcessDirectory, "Property for processDirectory")
    def addProcessDirectory(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultAutoPROC.addProcessDirectory argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._processDirectory.append(value)
        else:
            strMessage = "ERROR! XSDataResultAutoPROC.addProcessDirectory argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertProcessDirectory(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultAutoPROC.insertProcessDirectory argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultAutoPROC.insertProcessDirectory argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._processDirectory[index] = value
        else:
            strMessage = "ERROR! XSDataResultAutoPROC.addProcessDirectory argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'ispybXML' attribute
    def getIspybXML(self): return self._ispybXML
    def setIspybXML(self, ispybXML):
        if ispybXML is None:
            self._ispybXML = None
        elif ispybXML.__class__.__name__ == "XSDataFile":
            self._ispybXML = ispybXML
        else:
            strMessage = "ERROR! XSDataResultAutoPROC.setIspybXML argument is not XSDataFile but %s" % ispybXML.__class__.__name__
            raise BaseException(strMessage)
    def delIspybXML(self): self._ispybXML = None
    ispybXML = property(getIspybXML, setIspybXML, delIspybXML, "Property for ispybXML")
    # Methods and properties for the 'ispybXML_staraniso' attribute
    def getIspybXML_staraniso(self): return self._ispybXML_staraniso
    def setIspybXML_staraniso(self, ispybXML_staraniso):
        if ispybXML_staraniso is None:
            self._ispybXML_staraniso = None
        elif ispybXML_staraniso.__class__.__name__ == "XSDataFile":
            self._ispybXML_staraniso = ispybXML_staraniso
        else:
            strMessage = "ERROR! XSDataResultAutoPROC.setIspybXML_staraniso argument is not XSDataFile but %s" % ispybXML_staraniso.__class__.__name__
            raise BaseException(strMessage)
    def delIspybXML_staraniso(self): self._ispybXML_staraniso = None
    ispybXML_staraniso = property(getIspybXML_staraniso, setIspybXML_staraniso, delIspybXML_staraniso, "Property for ispybXML_staraniso")
    # Methods and properties for the 'reportPdf' attribute
    def getReportPdf(self): return self._reportPdf
    def setReportPdf(self, reportPdf):
        if reportPdf is None:
            self._reportPdf = None
        elif reportPdf.__class__.__name__ == "XSDataFile":
            self._reportPdf = reportPdf
        else:
            strMessage = "ERROR! XSDataResultAutoPROC.setReportPdf argument is not XSDataFile but %s" % reportPdf.__class__.__name__
            raise BaseException(strMessage)
    def delReportPdf(self): self._reportPdf = None
    reportPdf = property(getReportPdf, setReportPdf, delReportPdf, "Property for reportPdf")
    # Methods and properties for the 'reportPdf_staraniso' attribute
    def getReportPdf_staraniso(self): return self._reportPdf_staraniso
    def setReportPdf_staraniso(self, reportPdf_staraniso):
        if reportPdf_staraniso is None:
            self._reportPdf_staraniso = None
        elif reportPdf_staraniso.__class__.__name__ == "XSDataFile":
            self._reportPdf_staraniso = reportPdf_staraniso
        else:
            strMessage = "ERROR! XSDataResultAutoPROC.setReportPdf_staraniso argument is not XSDataFile but %s" % reportPdf_staraniso.__class__.__name__
            raise BaseException(strMessage)
    def delReportPdf_staraniso(self): self._reportPdf_staraniso = None
    reportPdf_staraniso = property(getReportPdf_staraniso, setReportPdf_staraniso, delReportPdf_staraniso, "Property for reportPdf_staraniso")
    def export(self, outfile, level, name_='XSDataResultAutoPROC'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultAutoPROC'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_='logFile')
        else:
            warnEmptyAttribute("logFile", "XSDataFile")
        if self._workingDirectory is not None:
            self.workingDirectory.export(outfile, level, name_='workingDirectory')
        else:
            warnEmptyAttribute("workingDirectory", "XSDataFile")
        for processDirectory_ in self.getProcessDirectory():
            processDirectory_.export(outfile, level, name_='processDirectory')
        if self.getProcessDirectory() == []:
            warnEmptyAttribute("processDirectory", "XSDataFile")
        if self._ispybXML is not None:
            self.ispybXML.export(outfile, level, name_='ispybXML')
        if self._ispybXML_staraniso is not None:
            self.ispybXML_staraniso.export(outfile, level, name_='ispybXML_staraniso')
        if self._reportPdf is not None:
            self.reportPdf.export(outfile, level, name_='reportPdf')
        if self._reportPdf_staraniso is not None:
            self.reportPdf_staraniso.export(outfile, level, name_='reportPdf_staraniso')
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
            nodeName_ == 'workingDirectory':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setWorkingDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'processDirectory':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.processDirectory.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ispybXML':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setIspybXML(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ispybXML_staraniso':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setIspybXML_staraniso(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'reportPdf':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setReportPdf(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'reportPdf_staraniso':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setReportPdf_staraniso(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultAutoPROC" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultAutoPROC' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultAutoPROC is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultAutoPROC.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultAutoPROC()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultAutoPROC" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultAutoPROC()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultAutoPROC



# End of data representation classes.


