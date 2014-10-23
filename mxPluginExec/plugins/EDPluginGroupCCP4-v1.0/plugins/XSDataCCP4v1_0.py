#!/usr/bin/env python

#
# Generated Tue Oct 21 12:24::57 2014 by EDGenerateDS.
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



class XSDataAimless(XSDataInput):
    def __init__(self, configuration=None, anom=None, res=None, end_image=None, start_image=None, dataCollectionID=None, command_file=None, output_file=None, input_file=None):
        XSDataInput.__init__(self, configuration)
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataAimless constructor argument 'input_file' is not XSDataString but %s" % self._input_file.__class__.__name__
            raise BaseException(strMessage)
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataString":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataAimless constructor argument 'output_file' is not XSDataString but %s" % self._output_file.__class__.__name__
            raise BaseException(strMessage)
        if command_file is None:
            self._command_file = None
        elif command_file.__class__.__name__ == "XSDataString":
            self._command_file = command_file
        else:
            strMessage = "ERROR! XSDataAimless constructor argument 'command_file' is not XSDataString but %s" % self._command_file.__class__.__name__
            raise BaseException(strMessage)
        if dataCollectionID is None:
            self._dataCollectionID = None
        elif dataCollectionID.__class__.__name__ == "XSDataInteger":
            self._dataCollectionID = dataCollectionID
        else:
            strMessage = "ERROR! XSDataAimless constructor argument 'dataCollectionID' is not XSDataInteger but %s" % self._dataCollectionID.__class__.__name__
            raise BaseException(strMessage)
        if start_image is None:
            self._start_image = None
        elif start_image.__class__.__name__ == "XSDataInteger":
            self._start_image = start_image
        else:
            strMessage = "ERROR! XSDataAimless constructor argument 'start_image' is not XSDataInteger but %s" % self._start_image.__class__.__name__
            raise BaseException(strMessage)
        if end_image is None:
            self._end_image = None
        elif end_image.__class__.__name__ == "XSDataInteger":
            self._end_image = end_image
        else:
            strMessage = "ERROR! XSDataAimless constructor argument 'end_image' is not XSDataInteger but %s" % self._end_image.__class__.__name__
            raise BaseException(strMessage)
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataDouble":
            self._res = res
        else:
            strMessage = "ERROR! XSDataAimless constructor argument 'res' is not XSDataDouble but %s" % self._res.__class__.__name__
            raise BaseException(strMessage)
        if anom is None:
            self._anom = None
        elif anom.__class__.__name__ == "XSDataBoolean":
            self._anom = anom
        else:
            strMessage = "ERROR! XSDataAimless constructor argument 'anom' is not XSDataBoolean but %s" % self._anom.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'input_file' attribute
    def getInput_file(self): return self._input_file
    def setInput_file(self, input_file):
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataAimless.setInput_file argument is not XSDataString but %s" % input_file.__class__.__name__
            raise BaseException(strMessage)
    def delInput_file(self): self._input_file = None
    input_file = property(getInput_file, setInput_file, delInput_file, "Property for input_file")
    # Methods and properties for the 'output_file' attribute
    def getOutput_file(self): return self._output_file
    def setOutput_file(self, output_file):
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataString":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataAimless.setOutput_file argument is not XSDataString but %s" % output_file.__class__.__name__
            raise BaseException(strMessage)
    def delOutput_file(self): self._output_file = None
    output_file = property(getOutput_file, setOutput_file, delOutput_file, "Property for output_file")
    # Methods and properties for the 'command_file' attribute
    def getCommand_file(self): return self._command_file
    def setCommand_file(self, command_file):
        if command_file is None:
            self._command_file = None
        elif command_file.__class__.__name__ == "XSDataString":
            self._command_file = command_file
        else:
            strMessage = "ERROR! XSDataAimless.setCommand_file argument is not XSDataString but %s" % command_file.__class__.__name__
            raise BaseException(strMessage)
    def delCommand_file(self): self._command_file = None
    command_file = property(getCommand_file, setCommand_file, delCommand_file, "Property for command_file")
    # Methods and properties for the 'dataCollectionID' attribute
    def getDataCollectionID(self): return self._dataCollectionID
    def setDataCollectionID(self, dataCollectionID):
        if dataCollectionID is None:
            self._dataCollectionID = None
        elif dataCollectionID.__class__.__name__ == "XSDataInteger":
            self._dataCollectionID = dataCollectionID
        else:
            strMessage = "ERROR! XSDataAimless.setDataCollectionID argument is not XSDataInteger but %s" % dataCollectionID.__class__.__name__
            raise BaseException(strMessage)
    def delDataCollectionID(self): self._dataCollectionID = None
    dataCollectionID = property(getDataCollectionID, setDataCollectionID, delDataCollectionID, "Property for dataCollectionID")
    # Methods and properties for the 'start_image' attribute
    def getStart_image(self): return self._start_image
    def setStart_image(self, start_image):
        if start_image is None:
            self._start_image = None
        elif start_image.__class__.__name__ == "XSDataInteger":
            self._start_image = start_image
        else:
            strMessage = "ERROR! XSDataAimless.setStart_image argument is not XSDataInteger but %s" % start_image.__class__.__name__
            raise BaseException(strMessage)
    def delStart_image(self): self._start_image = None
    start_image = property(getStart_image, setStart_image, delStart_image, "Property for start_image")
    # Methods and properties for the 'end_image' attribute
    def getEnd_image(self): return self._end_image
    def setEnd_image(self, end_image):
        if end_image is None:
            self._end_image = None
        elif end_image.__class__.__name__ == "XSDataInteger":
            self._end_image = end_image
        else:
            strMessage = "ERROR! XSDataAimless.setEnd_image argument is not XSDataInteger but %s" % end_image.__class__.__name__
            raise BaseException(strMessage)
    def delEnd_image(self): self._end_image = None
    end_image = property(getEnd_image, setEnd_image, delEnd_image, "Property for end_image")
    # Methods and properties for the 'res' attribute
    def getRes(self): return self._res
    def setRes(self, res):
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataDouble":
            self._res = res
        else:
            strMessage = "ERROR! XSDataAimless.setRes argument is not XSDataDouble but %s" % res.__class__.__name__
            raise BaseException(strMessage)
    def delRes(self): self._res = None
    res = property(getRes, setRes, delRes, "Property for res")
    # Methods and properties for the 'anom' attribute
    def getAnom(self): return self._anom
    def setAnom(self, anom):
        if anom is None:
            self._anom = None
        elif anom.__class__.__name__ == "XSDataBoolean":
            self._anom = anom
        else:
            strMessage = "ERROR! XSDataAimless.setAnom argument is not XSDataBoolean but %s" % anom.__class__.__name__
            raise BaseException(strMessage)
    def delAnom(self): self._anom = None
    anom = property(getAnom, setAnom, delAnom, "Property for anom")
    def export(self, outfile, level, name_='XSDataAimless'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataAimless'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._input_file is not None:
            self.input_file.export(outfile, level, name_='input_file')
        else:
            warnEmptyAttribute("input_file", "XSDataString")
        if self._output_file is not None:
            self.output_file.export(outfile, level, name_='output_file')
        else:
            warnEmptyAttribute("output_file", "XSDataString")
        if self._command_file is not None:
            self.command_file.export(outfile, level, name_='command_file')
        else:
            warnEmptyAttribute("command_file", "XSDataString")
        if self._dataCollectionID is not None:
            self.dataCollectionID.export(outfile, level, name_='dataCollectionID')
        else:
            warnEmptyAttribute("dataCollectionID", "XSDataInteger")
        if self._start_image is not None:
            self.start_image.export(outfile, level, name_='start_image')
        else:
            warnEmptyAttribute("start_image", "XSDataInteger")
        if self._end_image is not None:
            self.end_image.export(outfile, level, name_='end_image')
        else:
            warnEmptyAttribute("end_image", "XSDataInteger")
        if self._res is not None:
            self.res.export(outfile, level, name_='res')
        else:
            warnEmptyAttribute("res", "XSDataDouble")
        if self._anom is not None:
            self.anom.export(outfile, level, name_='anom')
        else:
            warnEmptyAttribute("anom", "XSDataBoolean")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'input_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setInput_file(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'output_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setOutput_file(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'command_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setCommand_file(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dataCollectionID':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setDataCollectionID(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'start_image':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setStart_image(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'end_image':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setEnd_image(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'res':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRes(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'anom':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setAnom(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataAimless" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataAimless' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataAimless is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataAimless.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAimless()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataAimless" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAimless()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataAimless


class XSDataInputDimple(XSDataInput):
    def __init__(self, configuration=None, pdb=None, mtz=None):
        XSDataInput.__init__(self, configuration)
        if mtz is None:
            self._mtz = None
        elif mtz.__class__.__name__ == "XSDataFile":
            self._mtz = mtz
        else:
            strMessage = "ERROR! XSDataInputDimple constructor argument 'mtz' is not XSDataFile but %s" % self._mtz.__class__.__name__
            raise BaseException(strMessage)
        if pdb is None:
            self._pdb = None
        elif pdb.__class__.__name__ == "XSDataFile":
            self._pdb = pdb
        else:
            strMessage = "ERROR! XSDataInputDimple constructor argument 'pdb' is not XSDataFile but %s" % self._pdb.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'mtz' attribute
    def getMtz(self): return self._mtz
    def setMtz(self, mtz):
        if mtz is None:
            self._mtz = None
        elif mtz.__class__.__name__ == "XSDataFile":
            self._mtz = mtz
        else:
            strMessage = "ERROR! XSDataInputDimple.setMtz argument is not XSDataFile but %s" % mtz.__class__.__name__
            raise BaseException(strMessage)
    def delMtz(self): self._mtz = None
    mtz = property(getMtz, setMtz, delMtz, "Property for mtz")
    # Methods and properties for the 'pdb' attribute
    def getPdb(self): return self._pdb
    def setPdb(self, pdb):
        if pdb is None:
            self._pdb = None
        elif pdb.__class__.__name__ == "XSDataFile":
            self._pdb = pdb
        else:
            strMessage = "ERROR! XSDataInputDimple.setPdb argument is not XSDataFile but %s" % pdb.__class__.__name__
            raise BaseException(strMessage)
    def delPdb(self): self._pdb = None
    pdb = property(getPdb, setPdb, delPdb, "Property for pdb")
    def export(self, outfile, level, name_='XSDataInputDimple'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDimple'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._mtz is not None:
            self.mtz.export(outfile, level, name_='mtz')
        else:
            warnEmptyAttribute("mtz", "XSDataFile")
        if self._pdb is not None:
            self.pdb.export(outfile, level, name_='pdb')
        else:
            warnEmptyAttribute("pdb", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mtz':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setMtz(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdb':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdb(obj_)
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


class XSDataPointless(XSDataInput):
    def __init__(self, configuration=None, output_file=None, input_file=None):
        XSDataInput.__init__(self, configuration)
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataPointless constructor argument 'input_file' is not XSDataString but %s" % self._input_file.__class__.__name__
            raise BaseException(strMessage)
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataString":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataPointless constructor argument 'output_file' is not XSDataString but %s" % self._output_file.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'input_file' attribute
    def getInput_file(self): return self._input_file
    def setInput_file(self, input_file):
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataPointless.setInput_file argument is not XSDataString but %s" % input_file.__class__.__name__
            raise BaseException(strMessage)
    def delInput_file(self): self._input_file = None
    input_file = property(getInput_file, setInput_file, delInput_file, "Property for input_file")
    # Methods and properties for the 'output_file' attribute
    def getOutput_file(self): return self._output_file
    def setOutput_file(self, output_file):
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataString":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataPointless.setOutput_file argument is not XSDataString but %s" % output_file.__class__.__name__
            raise BaseException(strMessage)
    def delOutput_file(self): self._output_file = None
    output_file = property(getOutput_file, setOutput_file, delOutput_file, "Property for output_file")
    def export(self, outfile, level, name_='XSDataPointless'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataPointless'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._input_file is not None:
            self.input_file.export(outfile, level, name_='input_file')
        else:
            warnEmptyAttribute("input_file", "XSDataString")
        if self._output_file is not None:
            self.output_file.export(outfile, level, name_='output_file')
        else:
            warnEmptyAttribute("output_file", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'input_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setInput_file(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'output_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setOutput_file(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataPointless" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataPointless' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataPointless is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataPointless.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataPointless()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataPointless" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataPointless()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataPointless


class XSDataPointlessOut(XSDataResult):
    def __init__(self, status=None, sgstr=None, sgnumber=None):
        XSDataResult.__init__(self, status)
        if sgnumber is None:
            self._sgnumber = None
        elif sgnumber.__class__.__name__ == "XSDataInteger":
            self._sgnumber = sgnumber
        else:
            strMessage = "ERROR! XSDataPointlessOut constructor argument 'sgnumber' is not XSDataInteger but %s" % self._sgnumber.__class__.__name__
            raise BaseException(strMessage)
        if sgstr is None:
            self._sgstr = None
        elif sgstr.__class__.__name__ == "XSDataString":
            self._sgstr = sgstr
        else:
            strMessage = "ERROR! XSDataPointlessOut constructor argument 'sgstr' is not XSDataString but %s" % self._sgstr.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'sgnumber' attribute
    def getSgnumber(self): return self._sgnumber
    def setSgnumber(self, sgnumber):
        if sgnumber is None:
            self._sgnumber = None
        elif sgnumber.__class__.__name__ == "XSDataInteger":
            self._sgnumber = sgnumber
        else:
            strMessage = "ERROR! XSDataPointlessOut.setSgnumber argument is not XSDataInteger but %s" % sgnumber.__class__.__name__
            raise BaseException(strMessage)
    def delSgnumber(self): self._sgnumber = None
    sgnumber = property(getSgnumber, setSgnumber, delSgnumber, "Property for sgnumber")
    # Methods and properties for the 'sgstr' attribute
    def getSgstr(self): return self._sgstr
    def setSgstr(self, sgstr):
        if sgstr is None:
            self._sgstr = None
        elif sgstr.__class__.__name__ == "XSDataString":
            self._sgstr = sgstr
        else:
            strMessage = "ERROR! XSDataPointlessOut.setSgstr argument is not XSDataString but %s" % sgstr.__class__.__name__
            raise BaseException(strMessage)
    def delSgstr(self): self._sgstr = None
    sgstr = property(getSgstr, setSgstr, delSgstr, "Property for sgstr")
    def export(self, outfile, level, name_='XSDataPointlessOut'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataPointlessOut'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._sgnumber is not None:
            self.sgnumber.export(outfile, level, name_='sgnumber')
        if self._sgstr is not None:
            self.sgstr.export(outfile, level, name_='sgstr')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sgnumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSgnumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sgstr':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSgstr(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataPointlessOut" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataPointlessOut' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataPointlessOut is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataPointlessOut.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataPointlessOut()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataPointlessOut" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataPointlessOut()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataPointlessOut


class XSDataResultDimple(XSDataResult):
    def __init__(self, status=None, refmac5restrLog=None, findBlobsLog=None, log=None, finalPdb=None, finalMtz=None, blob=None):
        XSDataResult.__init__(self, status)
        if blob is None:
            self._blob = []
        elif blob.__class__.__name__ == "list":
            self._blob = blob
        else:
            strMessage = "ERROR! XSDataResultDimple constructor argument 'blob' is not list but %s" % self._blob.__class__.__name__
            raise BaseException(strMessage)
        if finalMtz is None:
            self._finalMtz = None
        elif finalMtz.__class__.__name__ == "XSDataFile":
            self._finalMtz = finalMtz
        else:
            strMessage = "ERROR! XSDataResultDimple constructor argument 'finalMtz' is not XSDataFile but %s" % self._finalMtz.__class__.__name__
            raise BaseException(strMessage)
        if finalPdb is None:
            self._finalPdb = None
        elif finalPdb.__class__.__name__ == "XSDataFile":
            self._finalPdb = finalPdb
        else:
            strMessage = "ERROR! XSDataResultDimple constructor argument 'finalPdb' is not XSDataFile but %s" % self._finalPdb.__class__.__name__
            raise BaseException(strMessage)
        if log is None:
            self._log = None
        elif log.__class__.__name__ == "XSDataFile":
            self._log = log
        else:
            strMessage = "ERROR! XSDataResultDimple constructor argument 'log' is not XSDataFile but %s" % self._log.__class__.__name__
            raise BaseException(strMessage)
        if findBlobsLog is None:
            self._findBlobsLog = None
        elif findBlobsLog.__class__.__name__ == "XSDataFile":
            self._findBlobsLog = findBlobsLog
        else:
            strMessage = "ERROR! XSDataResultDimple constructor argument 'findBlobsLog' is not XSDataFile but %s" % self._findBlobsLog.__class__.__name__
            raise BaseException(strMessage)
        if refmac5restrLog is None:
            self._refmac5restrLog = None
        elif refmac5restrLog.__class__.__name__ == "XSDataFile":
            self._refmac5restrLog = refmac5restrLog
        else:
            strMessage = "ERROR! XSDataResultDimple constructor argument 'refmac5restrLog' is not XSDataFile but %s" % self._refmac5restrLog.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'blob' attribute
    def getBlob(self): return self._blob
    def setBlob(self, blob):
        if blob is None:
            self._blob = []
        elif blob.__class__.__name__ == "list":
            self._blob = blob
        else:
            strMessage = "ERROR! XSDataResultDimple.setBlob argument is not list but %s" % blob.__class__.__name__
            raise BaseException(strMessage)
    def delBlob(self): self._blob = None
    blob = property(getBlob, setBlob, delBlob, "Property for blob")
    def addBlob(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultDimple.addBlob argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._blob.append(value)
        else:
            strMessage = "ERROR! XSDataResultDimple.addBlob argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertBlob(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultDimple.insertBlob argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultDimple.insertBlob argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._blob[index] = value
        else:
            strMessage = "ERROR! XSDataResultDimple.addBlob argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'finalMtz' attribute
    def getFinalMtz(self): return self._finalMtz
    def setFinalMtz(self, finalMtz):
        if finalMtz is None:
            self._finalMtz = None
        elif finalMtz.__class__.__name__ == "XSDataFile":
            self._finalMtz = finalMtz
        else:
            strMessage = "ERROR! XSDataResultDimple.setFinalMtz argument is not XSDataFile but %s" % finalMtz.__class__.__name__
            raise BaseException(strMessage)
    def delFinalMtz(self): self._finalMtz = None
    finalMtz = property(getFinalMtz, setFinalMtz, delFinalMtz, "Property for finalMtz")
    # Methods and properties for the 'finalPdb' attribute
    def getFinalPdb(self): return self._finalPdb
    def setFinalPdb(self, finalPdb):
        if finalPdb is None:
            self._finalPdb = None
        elif finalPdb.__class__.__name__ == "XSDataFile":
            self._finalPdb = finalPdb
        else:
            strMessage = "ERROR! XSDataResultDimple.setFinalPdb argument is not XSDataFile but %s" % finalPdb.__class__.__name__
            raise BaseException(strMessage)
    def delFinalPdb(self): self._finalPdb = None
    finalPdb = property(getFinalPdb, setFinalPdb, delFinalPdb, "Property for finalPdb")
    # Methods and properties for the 'log' attribute
    def getLog(self): return self._log
    def setLog(self, log):
        if log is None:
            self._log = None
        elif log.__class__.__name__ == "XSDataFile":
            self._log = log
        else:
            strMessage = "ERROR! XSDataResultDimple.setLog argument is not XSDataFile but %s" % log.__class__.__name__
            raise BaseException(strMessage)
    def delLog(self): self._log = None
    log = property(getLog, setLog, delLog, "Property for log")
    # Methods and properties for the 'findBlobsLog' attribute
    def getFindBlobsLog(self): return self._findBlobsLog
    def setFindBlobsLog(self, findBlobsLog):
        if findBlobsLog is None:
            self._findBlobsLog = None
        elif findBlobsLog.__class__.__name__ == "XSDataFile":
            self._findBlobsLog = findBlobsLog
        else:
            strMessage = "ERROR! XSDataResultDimple.setFindBlobsLog argument is not XSDataFile but %s" % findBlobsLog.__class__.__name__
            raise BaseException(strMessage)
    def delFindBlobsLog(self): self._findBlobsLog = None
    findBlobsLog = property(getFindBlobsLog, setFindBlobsLog, delFindBlobsLog, "Property for findBlobsLog")
    # Methods and properties for the 'refmac5restrLog' attribute
    def getRefmac5restrLog(self): return self._refmac5restrLog
    def setRefmac5restrLog(self, refmac5restrLog):
        if refmac5restrLog is None:
            self._refmac5restrLog = None
        elif refmac5restrLog.__class__.__name__ == "XSDataFile":
            self._refmac5restrLog = refmac5restrLog
        else:
            strMessage = "ERROR! XSDataResultDimple.setRefmac5restrLog argument is not XSDataFile but %s" % refmac5restrLog.__class__.__name__
            raise BaseException(strMessage)
    def delRefmac5restrLog(self): self._refmac5restrLog = None
    refmac5restrLog = property(getRefmac5restrLog, setRefmac5restrLog, delRefmac5restrLog, "Property for refmac5restrLog")
    def export(self, outfile, level, name_='XSDataResultDimple'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDimple'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for blob_ in self.getBlob():
            blob_.export(outfile, level, name_='blob')
        if self._finalMtz is not None:
            self.finalMtz.export(outfile, level, name_='finalMtz')
        if self._finalPdb is not None:
            self.finalPdb.export(outfile, level, name_='finalPdb')
        if self._log is not None:
            self.log.export(outfile, level, name_='log')
        if self._findBlobsLog is not None:
            self.findBlobsLog.export(outfile, level, name_='findBlobsLog')
        if self._refmac5restrLog is not None:
            self.refmac5restrLog.export(outfile, level, name_='refmac5restrLog')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'blob':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.blob.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'finalMtz':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setFinalMtz(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'finalPdb':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setFinalPdb(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'log':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLog(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'findBlobsLog':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setFindBlobsLog(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'refmac5restrLog':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setRefmac5restrLog(obj_)
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


class XSDataTruncate(XSDataInput):
    def __init__(self, configuration=None, res=None, anom=None, nres=None, output_file=None, input_file=None):
        XSDataInput.__init__(self, configuration)
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataTruncate constructor argument 'input_file' is not XSDataString but %s" % self._input_file.__class__.__name__
            raise BaseException(strMessage)
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataString":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataTruncate constructor argument 'output_file' is not XSDataString but %s" % self._output_file.__class__.__name__
            raise BaseException(strMessage)
        if nres is None:
            self._nres = None
        elif nres.__class__.__name__ == "XSDataDouble":
            self._nres = nres
        else:
            strMessage = "ERROR! XSDataTruncate constructor argument 'nres' is not XSDataDouble but %s" % self._nres.__class__.__name__
            raise BaseException(strMessage)
        if anom is None:
            self._anom = None
        elif anom.__class__.__name__ == "XSDataBoolean":
            self._anom = anom
        else:
            strMessage = "ERROR! XSDataTruncate constructor argument 'anom' is not XSDataBoolean but %s" % self._anom.__class__.__name__
            raise BaseException(strMessage)
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataDouble":
            self._res = res
        else:
            strMessage = "ERROR! XSDataTruncate constructor argument 'res' is not XSDataDouble but %s" % self._res.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'input_file' attribute
    def getInput_file(self): return self._input_file
    def setInput_file(self, input_file):
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataTruncate.setInput_file argument is not XSDataString but %s" % input_file.__class__.__name__
            raise BaseException(strMessage)
    def delInput_file(self): self._input_file = None
    input_file = property(getInput_file, setInput_file, delInput_file, "Property for input_file")
    # Methods and properties for the 'output_file' attribute
    def getOutput_file(self): return self._output_file
    def setOutput_file(self, output_file):
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataString":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataTruncate.setOutput_file argument is not XSDataString but %s" % output_file.__class__.__name__
            raise BaseException(strMessage)
    def delOutput_file(self): self._output_file = None
    output_file = property(getOutput_file, setOutput_file, delOutput_file, "Property for output_file")
    # Methods and properties for the 'nres' attribute
    def getNres(self): return self._nres
    def setNres(self, nres):
        if nres is None:
            self._nres = None
        elif nres.__class__.__name__ == "XSDataDouble":
            self._nres = nres
        else:
            strMessage = "ERROR! XSDataTruncate.setNres argument is not XSDataDouble but %s" % nres.__class__.__name__
            raise BaseException(strMessage)
    def delNres(self): self._nres = None
    nres = property(getNres, setNres, delNres, "Property for nres")
    # Methods and properties for the 'anom' attribute
    def getAnom(self): return self._anom
    def setAnom(self, anom):
        if anom is None:
            self._anom = None
        elif anom.__class__.__name__ == "XSDataBoolean":
            self._anom = anom
        else:
            strMessage = "ERROR! XSDataTruncate.setAnom argument is not XSDataBoolean but %s" % anom.__class__.__name__
            raise BaseException(strMessage)
    def delAnom(self): self._anom = None
    anom = property(getAnom, setAnom, delAnom, "Property for anom")
    # Methods and properties for the 'res' attribute
    def getRes(self): return self._res
    def setRes(self, res):
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataDouble":
            self._res = res
        else:
            strMessage = "ERROR! XSDataTruncate.setRes argument is not XSDataDouble but %s" % res.__class__.__name__
            raise BaseException(strMessage)
    def delRes(self): self._res = None
    res = property(getRes, setRes, delRes, "Property for res")
    def export(self, outfile, level, name_='XSDataTruncate'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataTruncate'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._input_file is not None:
            self.input_file.export(outfile, level, name_='input_file')
        else:
            warnEmptyAttribute("input_file", "XSDataString")
        if self._output_file is not None:
            self.output_file.export(outfile, level, name_='output_file')
        else:
            warnEmptyAttribute("output_file", "XSDataString")
        if self._nres is not None:
            self.nres.export(outfile, level, name_='nres')
        else:
            warnEmptyAttribute("nres", "XSDataDouble")
        if self._anom is not None:
            self.anom.export(outfile, level, name_='anom')
        else:
            warnEmptyAttribute("anom", "XSDataBoolean")
        if self._res is not None:
            self.res.export(outfile, level, name_='res')
        else:
            warnEmptyAttribute("res", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'input_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setInput_file(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'output_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setOutput_file(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nres':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setNres(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'anom':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setAnom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'res':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRes(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataTruncate" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataTruncate' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataTruncate is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataTruncate.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataTruncate()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataTruncate" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataTruncate()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataTruncate


class XSDataUniqueify(XSDataInput):
    def __init__(self, configuration=None, output_file=None, input_file=None):
        XSDataInput.__init__(self, configuration)
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataUniqueify constructor argument 'input_file' is not XSDataString but %s" % self._input_file.__class__.__name__
            raise BaseException(strMessage)
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataString":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataUniqueify constructor argument 'output_file' is not XSDataString but %s" % self._output_file.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'input_file' attribute
    def getInput_file(self): return self._input_file
    def setInput_file(self, input_file):
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataUniqueify.setInput_file argument is not XSDataString but %s" % input_file.__class__.__name__
            raise BaseException(strMessage)
    def delInput_file(self): self._input_file = None
    input_file = property(getInput_file, setInput_file, delInput_file, "Property for input_file")
    # Methods and properties for the 'output_file' attribute
    def getOutput_file(self): return self._output_file
    def setOutput_file(self, output_file):
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataString":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataUniqueify.setOutput_file argument is not XSDataString but %s" % output_file.__class__.__name__
            raise BaseException(strMessage)
    def delOutput_file(self): self._output_file = None
    output_file = property(getOutput_file, setOutput_file, delOutput_file, "Property for output_file")
    def export(self, outfile, level, name_='XSDataUniqueify'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataUniqueify'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._input_file is not None:
            self.input_file.export(outfile, level, name_='input_file')
        else:
            warnEmptyAttribute("input_file", "XSDataString")
        if self._output_file is not None:
            self.output_file.export(outfile, level, name_='output_file')
        else:
            warnEmptyAttribute("output_file", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'input_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setInput_file(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'output_file':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setOutput_file(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataUniqueify" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataUniqueify' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataUniqueify is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataUniqueify.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataUniqueify()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataUniqueify" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataUniqueify()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataUniqueify



# End of data representation classes.


