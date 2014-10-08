#!/usr/bin/env python

#
# Generated Wed Oct 8 10:06::21 2014 by EDGenerateDS.
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
}

try:
    from XSDataCommon import XSDataResult
    from XSDataCommon import XSDataString
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataInput
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
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput




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



class XSDataInputDimple(XSDataInput):
    def __init__(self, configuration=None, pdbfile=None, mtzfile=None):
        XSDataInput.__init__(self, configuration)
        if mtzfile is None:
            self._mtzfile = None
        elif mtzfile.__class__.__name__ == "XSDataFile":
            self._mtzfile = mtzfile
        else:
            strMessage = "ERROR! XSDataInputDimple constructor argument 'mtzfile' is not XSDataFile but %s" % self._mtzfile.__class__.__name__
            raise BaseException(strMessage)
        if pdbfile is None:
            self._pdbfile = None
        elif pdbfile.__class__.__name__ == "XSDataFile":
            self._pdbfile = pdbfile
        else:
            strMessage = "ERROR! XSDataInputDimple constructor argument 'pdbfile' is not XSDataFile but %s" % self._pdbfile.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'mtzfile' attribute
    def getMtzfile(self): return self._mtzfile
    def setMtzfile(self, mtzfile):
        if mtzfile is None:
            self._mtzfile = None
        elif mtzfile.__class__.__name__ == "XSDataFile":
            self._mtzfile = mtzfile
        else:
            strMessage = "ERROR! XSDataInputDimple.setMtzfile argument is not XSDataFile but %s" % mtzfile.__class__.__name__
            raise BaseException(strMessage)
    def delMtzfile(self): self._mtzfile = None
    mtzfile = property(getMtzfile, setMtzfile, delMtzfile, "Property for mtzfile")
    # Methods and properties for the 'pdbfile' attribute
    def getPdbfile(self): return self._pdbfile
    def setPdbfile(self, pdbfile):
        if pdbfile is None:
            self._pdbfile = None
        elif pdbfile.__class__.__name__ == "XSDataFile":
            self._pdbfile = pdbfile
        else:
            strMessage = "ERROR! XSDataInputDimple.setPdbfile argument is not XSDataFile but %s" % pdbfile.__class__.__name__
            raise BaseException(strMessage)
    def delPdbfile(self): self._pdbfile = None
    pdbfile = property(getPdbfile, setPdbfile, delPdbfile, "Property for pdbfile")
    def export(self, outfile, level, name_='XSDataInputDimple'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDimple'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._mtzfile is not None:
            self.mtzfile.export(outfile, level, name_='mtzfile')
        else:
            warnEmptyAttribute("mtzfile", "XSDataFile")
        if self._pdbfile is not None:
            self.pdbfile.export(outfile, level, name_='pdbfile')
        else:
            warnEmptyAttribute("pdbfile", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mtzfile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setMtzfile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbfile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdbfile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDimple" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDimple' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDimple is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDimple.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDimple()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDimple" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDimple()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDimple


class XSDataInputMtz2Various(XSDataInput):
    def __init__(self, configuration=None, format=None, output=None, labin=None, mtzfile=None):
        XSDataInput.__init__(self, configuration)
        if mtzfile is None:
            self._mtzfile = None
        elif mtzfile.__class__.__name__ == "XSDataFile":
            self._mtzfile = mtzfile
        else:
            strMessage = "ERROR! XSDataInputMtz2Various constructor argument 'mtzfile' is not XSDataFile but %s" % self._mtzfile.__class__.__name__
            raise BaseException(strMessage)
        if labin is None:
            self._labin = []
        elif labin.__class__.__name__ == "list":
            self._labin = labin
        else:
            strMessage = "ERROR! XSDataInputMtz2Various constructor argument 'labin' is not list but %s" % self._labin.__class__.__name__
            raise BaseException(strMessage)
        if output is None:
            self._output = None
        elif output.__class__.__name__ == "XSDataString":
            self._output = output
        else:
            strMessage = "ERROR! XSDataInputMtz2Various constructor argument 'output' is not XSDataString but %s" % self._output.__class__.__name__
            raise BaseException(strMessage)
        if format is None:
            self._format = None
        elif format.__class__.__name__ == "XSDataString":
            self._format = format
        else:
            strMessage = "ERROR! XSDataInputMtz2Various constructor argument 'format' is not XSDataString but %s" % self._format.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'mtzfile' attribute
    def getMtzfile(self): return self._mtzfile
    def setMtzfile(self, mtzfile):
        if mtzfile is None:
            self._mtzfile = None
        elif mtzfile.__class__.__name__ == "XSDataFile":
            self._mtzfile = mtzfile
        else:
            strMessage = "ERROR! XSDataInputMtz2Various.setMtzfile argument is not XSDataFile but %s" % mtzfile.__class__.__name__
            raise BaseException(strMessage)
    def delMtzfile(self): self._mtzfile = None
    mtzfile = property(getMtzfile, setMtzfile, delMtzfile, "Property for mtzfile")
    # Methods and properties for the 'labin' attribute
    def getLabin(self): return self._labin
    def setLabin(self, labin):
        if labin is None:
            self._labin = []
        elif labin.__class__.__name__ == "list":
            self._labin = labin
        else:
            strMessage = "ERROR! XSDataInputMtz2Various.setLabin argument is not list but %s" % labin.__class__.__name__
            raise BaseException(strMessage)
    def delLabin(self): self._labin = None
    labin = property(getLabin, setLabin, delLabin, "Property for labin")
    def addLabin(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputMtz2Various.addLabin argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataString":
            self._labin.append(value)
        else:
            strMessage = "ERROR! XSDataInputMtz2Various.addLabin argument is not XSDataString but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertLabin(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputMtz2Various.insertLabin argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputMtz2Various.insertLabin argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataString":
            self._labin[index] = value
        else:
            strMessage = "ERROR! XSDataInputMtz2Various.addLabin argument is not XSDataString but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'output' attribute
    def getOutput(self): return self._output
    def setOutput(self, output):
        if output is None:
            self._output = None
        elif output.__class__.__name__ == "XSDataString":
            self._output = output
        else:
            strMessage = "ERROR! XSDataInputMtz2Various.setOutput argument is not XSDataString but %s" % output.__class__.__name__
            raise BaseException(strMessage)
    def delOutput(self): self._output = None
    output = property(getOutput, setOutput, delOutput, "Property for output")
    # Methods and properties for the 'format' attribute
    def getFormat(self): return self._format
    def setFormat(self, format):
        if format is None:
            self._format = None
        elif format.__class__.__name__ == "XSDataString":
            self._format = format
        else:
            strMessage = "ERROR! XSDataInputMtz2Various.setFormat argument is not XSDataString but %s" % format.__class__.__name__
            raise BaseException(strMessage)
    def delFormat(self): self._format = None
    format = property(getFormat, setFormat, delFormat, "Property for format")
    def export(self, outfile, level, name_='XSDataInputMtz2Various'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputMtz2Various'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._mtzfile is not None:
            self.mtzfile.export(outfile, level, name_='mtzfile')
        else:
            warnEmptyAttribute("mtzfile", "XSDataFile")
        for labin_ in self.getLabin():
            labin_.export(outfile, level, name_='labin')
        if self.getLabin() == []:
            warnEmptyAttribute("labin", "XSDataString")
        if self._output is not None:
            self.output.export(outfile, level, name_='output')
        if self._format is not None:
            self.format.export(outfile, level, name_='format')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mtzfile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setMtzfile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'labin':
            obj_ = XSDataString()
            obj_.build(child_)
            self.labin.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'output':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setOutput(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'format':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setFormat(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputMtz2Various" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputMtz2Various' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputMtz2Various is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputMtz2Various.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputMtz2Various()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputMtz2Various" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputMtz2Various()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputMtz2Various


class XSDataResultDimple(XSDataResult):
    def __init__(self, status=None, blobfile=None):
        XSDataResult.__init__(self, status)
        if blobfile is None:
            self._blobfile = []
        elif blobfile.__class__.__name__ == "list":
            self._blobfile = blobfile
        else:
            strMessage = "ERROR! XSDataResultDimple constructor argument 'blobfile' is not list but %s" % self._blobfile.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'blobfile' attribute
    def getBlobfile(self): return self._blobfile
    def setBlobfile(self, blobfile):
        if blobfile is None:
            self._blobfile = []
        elif blobfile.__class__.__name__ == "list":
            self._blobfile = blobfile
        else:
            strMessage = "ERROR! XSDataResultDimple.setBlobfile argument is not list but %s" % blobfile.__class__.__name__
            raise BaseException(strMessage)
    def delBlobfile(self): self._blobfile = None
    blobfile = property(getBlobfile, setBlobfile, delBlobfile, "Property for blobfile")
    def addBlobfile(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultDimple.addBlobfile argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._blobfile.append(value)
        else:
            strMessage = "ERROR! XSDataResultDimple.addBlobfile argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertBlobfile(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultDimple.insertBlobfile argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultDimple.insertBlobfile argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._blobfile[index] = value
        else:
            strMessage = "ERROR! XSDataResultDimple.addBlobfile argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataResultDimple'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDimple'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for blobfile_ in self.getBlobfile():
            blobfile_.export(outfile, level, name_='blobfile')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'blobfile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.blobfile.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDimple" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDimple' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDimple is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDimple.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDimple()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDimple" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDimple()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDimple


class XSDataResultMtz2Various(XSDataResult):
    def __init__(self, status=None, hklfile=None):
        XSDataResult.__init__(self, status)
        if hklfile is None:
            self._hklfile = None
        elif hklfile.__class__.__name__ == "XSDataFile":
            self._hklfile = hklfile
        else:
            strMessage = "ERROR! XSDataResultMtz2Various constructor argument 'hklfile' is not XSDataFile but %s" % self._hklfile.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'hklfile' attribute
    def getHklfile(self): return self._hklfile
    def setHklfile(self, hklfile):
        if hklfile is None:
            self._hklfile = None
        elif hklfile.__class__.__name__ == "XSDataFile":
            self._hklfile = hklfile
        else:
            strMessage = "ERROR! XSDataResultMtz2Various.setHklfile argument is not XSDataFile but %s" % hklfile.__class__.__name__
            raise BaseException(strMessage)
    def delHklfile(self): self._hklfile = None
    hklfile = property(getHklfile, setHklfile, delHklfile, "Property for hklfile")
    def export(self, outfile, level, name_='XSDataResultMtz2Various'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultMtz2Various'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._hklfile is not None:
            self.hklfile.export(outfile, level, name_='hklfile')
        else:
            warnEmptyAttribute("hklfile", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hklfile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setHklfile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultMtz2Various" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultMtz2Various' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultMtz2Various is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultMtz2Various.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultMtz2Various()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultMtz2Various" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultMtz2Various()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultMtz2Various



# End of data representation classes.


