#!/usr/bin/env python

#
# Generated Thu Mar 26 09:44::58 2015 by EDGenerateDS.
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
    from XSDataCommon import XSData
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
from XSDataCommon import XSData
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



class XSDataXOalignSolution(XSData):
    def __init__(self, settings=None, phi=None, kappa=None):
        XSData.__init__(self, )
        if kappa is None:
            self._kappa = None
        elif kappa.__class__.__name__ == "XSDataDouble":
            self._kappa = kappa
        else:
            strMessage = "ERROR! XSDataXOalignSolution constructor argument 'kappa' is not XSDataDouble but %s" % self._kappa.__class__.__name__
            raise BaseException(strMessage)
        if phi is None:
            self._phi = None
        elif phi.__class__.__name__ == "XSDataDouble":
            self._phi = phi
        else:
            strMessage = "ERROR! XSDataXOalignSolution constructor argument 'phi' is not XSDataDouble but %s" % self._phi.__class__.__name__
            raise BaseException(strMessage)
        if settings is None:
            self._settings = None
        elif settings.__class__.__name__ == "XSDataString":
            self._settings = settings
        else:
            strMessage = "ERROR! XSDataXOalignSolution constructor argument 'settings' is not XSDataString but %s" % self._settings.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'kappa' attribute
    def getKappa(self): return self._kappa
    def setKappa(self, kappa):
        if kappa is None:
            self._kappa = None
        elif kappa.__class__.__name__ == "XSDataDouble":
            self._kappa = kappa
        else:
            strMessage = "ERROR! XSDataXOalignSolution.setKappa argument is not XSDataDouble but %s" % kappa.__class__.__name__
            raise BaseException(strMessage)
    def delKappa(self): self._kappa = None
    kappa = property(getKappa, setKappa, delKappa, "Property for kappa")
    # Methods and properties for the 'phi' attribute
    def getPhi(self): return self._phi
    def setPhi(self, phi):
        if phi is None:
            self._phi = None
        elif phi.__class__.__name__ == "XSDataDouble":
            self._phi = phi
        else:
            strMessage = "ERROR! XSDataXOalignSolution.setPhi argument is not XSDataDouble but %s" % phi.__class__.__name__
            raise BaseException(strMessage)
    def delPhi(self): self._phi = None
    phi = property(getPhi, setPhi, delPhi, "Property for phi")
    # Methods and properties for the 'settings' attribute
    def getSettings(self): return self._settings
    def setSettings(self, settings):
        if settings is None:
            self._settings = None
        elif settings.__class__.__name__ == "XSDataString":
            self._settings = settings
        else:
            strMessage = "ERROR! XSDataXOalignSolution.setSettings argument is not XSDataString but %s" % settings.__class__.__name__
            raise BaseException(strMessage)
    def delSettings(self): self._settings = None
    settings = property(getSettings, setSettings, delSettings, "Property for settings")
    def export(self, outfile, level, name_='XSDataXOalignSolution'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataXOalignSolution'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._kappa is not None:
            self.kappa.export(outfile, level, name_='kappa')
        else:
            warnEmptyAttribute("kappa", "XSDataDouble")
        if self._phi is not None:
            self.phi.export(outfile, level, name_='phi')
        else:
            warnEmptyAttribute("phi", "XSDataDouble")
        if self._settings is not None:
            self.settings.export(outfile, level, name_='settings')
        else:
            warnEmptyAttribute("settings", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kappa':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setKappa(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phi':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setPhi(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'settings':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSettings(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataXOalignSolution" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataXOalignSolution' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataXOalignSolution is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataXOalignSolution.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataXOalignSolution()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataXOalignSolution" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataXOalignSolution()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataXOalignSolution


class XSDataInputXOalign(XSDataInput):
    def __init__(self, configuration=None, mosflmMat=None):
        XSDataInput.__init__(self, configuration)
        if mosflmMat is None:
            self._mosflmMat = None
        elif mosflmMat.__class__.__name__ == "XSDataFile":
            self._mosflmMat = mosflmMat
        else:
            strMessage = "ERROR! XSDataInputXOalign constructor argument 'mosflmMat' is not XSDataFile but %s" % self._mosflmMat.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'mosflmMat' attribute
    def getMosflmMat(self): return self._mosflmMat
    def setMosflmMat(self, mosflmMat):
        if mosflmMat is None:
            self._mosflmMat = None
        elif mosflmMat.__class__.__name__ == "XSDataFile":
            self._mosflmMat = mosflmMat
        else:
            strMessage = "ERROR! XSDataInputXOalign.setMosflmMat argument is not XSDataFile but %s" % mosflmMat.__class__.__name__
            raise BaseException(strMessage)
    def delMosflmMat(self): self._mosflmMat = None
    mosflmMat = property(getMosflmMat, setMosflmMat, delMosflmMat, "Property for mosflmMat")
    def export(self, outfile, level, name_='XSDataInputXOalign'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputXOalign'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._mosflmMat is not None:
            self.mosflmMat.export(outfile, level, name_='mosflmMat')
        else:
            warnEmptyAttribute("mosflmMat", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mosflmMat':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setMosflmMat(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputXOalign" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputXOalign' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputXOalign is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputXOalign.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputXOalign()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputXOalign" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputXOalign()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputXOalign


class XSDataResultXOalign(XSDataResult):
    def __init__(self, status=None, solution=None, logFile=None):
        XSDataResult.__init__(self, status)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultXOalign constructor argument 'logFile' is not XSDataFile but %s" % self._logFile.__class__.__name__
            raise BaseException(strMessage)
        if solution is None:
            self._solution = []
        elif solution.__class__.__name__ == "list":
            self._solution = solution
        else:
            strMessage = "ERROR! XSDataResultXOalign constructor argument 'solution' is not list but %s" % self._solution.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultXOalign.setLogFile argument is not XSDataFile but %s" % logFile.__class__.__name__
            raise BaseException(strMessage)
    def delLogFile(self): self._logFile = None
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    # Methods and properties for the 'solution' attribute
    def getSolution(self): return self._solution
    def setSolution(self, solution):
        if solution is None:
            self._solution = []
        elif solution.__class__.__name__ == "list":
            self._solution = solution
        else:
            strMessage = "ERROR! XSDataResultXOalign.setSolution argument is not list but %s" % solution.__class__.__name__
            raise BaseException(strMessage)
    def delSolution(self): self._solution = None
    solution = property(getSolution, setSolution, delSolution, "Property for solution")
    def addSolution(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultXOalign.addSolution argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXOalignSolution":
            self._solution.append(value)
        else:
            strMessage = "ERROR! XSDataResultXOalign.addSolution argument is not XSDataXOalignSolution but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertSolution(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultXOalign.insertSolution argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultXOalign.insertSolution argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataXOalignSolution":
            self._solution[index] = value
        else:
            strMessage = "ERROR! XSDataResultXOalign.addSolution argument is not XSDataXOalignSolution but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataResultXOalign'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultXOalign'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_='logFile')
        for solution_ in self.getSolution():
            solution_.export(outfile, level, name_='solution')
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
            nodeName_ == 'solution':
            obj_ = XSDataXOalignSolution()
            obj_.build(child_)
            self.solution.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultXOalign" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultXOalign' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultXOalign is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultXOalign.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultXOalign()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultXOalign" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultXOalign()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultXOalign



# End of data representation classes.


