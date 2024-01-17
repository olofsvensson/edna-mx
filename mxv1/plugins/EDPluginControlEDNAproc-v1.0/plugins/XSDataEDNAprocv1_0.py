#!/usr/bin/env python

#
# Generated Wed Jan 17 02:58::35 2024 by EDGenerateDS.
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



class XSDataEDNAprocImport(XSDataInput):
    def __init__(self, configuration=None, choose_spacegroup=None, image_prefix=None, nres=None, res=None, end_image=None, start_image=None, dataCollectionID=None, output_directory=None, input_noanom=None, input_anom=None):
        XSDataInput.__init__(self, configuration)
        if input_anom is None:
            self._input_anom = None
        elif input_anom.__class__.__name__ == "XSDataString":
            self._input_anom = input_anom
        else:
            strMessage = "ERROR! XSDataEDNAprocImport constructor argument 'input_anom' is not XSDataString but %s" % self._input_anom.__class__.__name__
            raise BaseException(strMessage)
        if input_noanom is None:
            self._input_noanom = None
        elif input_noanom.__class__.__name__ == "XSDataString":
            self._input_noanom = input_noanom
        else:
            strMessage = "ERROR! XSDataEDNAprocImport constructor argument 'input_noanom' is not XSDataString but %s" % self._input_noanom.__class__.__name__
            raise BaseException(strMessage)
        if output_directory is None:
            self._output_directory = None
        elif output_directory.__class__.__name__ == "XSDataString":
            self._output_directory = output_directory
        else:
            strMessage = "ERROR! XSDataEDNAprocImport constructor argument 'output_directory' is not XSDataString but %s" % self._output_directory.__class__.__name__
            raise BaseException(strMessage)
        if dataCollectionID is None:
            self._dataCollectionID = None
        elif dataCollectionID.__class__.__name__ == "XSDataInteger":
            self._dataCollectionID = dataCollectionID
        else:
            strMessage = "ERROR! XSDataEDNAprocImport constructor argument 'dataCollectionID' is not XSDataInteger but %s" % self._dataCollectionID.__class__.__name__
            raise BaseException(strMessage)
        if start_image is None:
            self._start_image = None
        elif start_image.__class__.__name__ == "XSDataInteger":
            self._start_image = start_image
        else:
            strMessage = "ERROR! XSDataEDNAprocImport constructor argument 'start_image' is not XSDataInteger but %s" % self._start_image.__class__.__name__
            raise BaseException(strMessage)
        if end_image is None:
            self._end_image = None
        elif end_image.__class__.__name__ == "XSDataInteger":
            self._end_image = end_image
        else:
            strMessage = "ERROR! XSDataEDNAprocImport constructor argument 'end_image' is not XSDataInteger but %s" % self._end_image.__class__.__name__
            raise BaseException(strMessage)
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataDouble":
            self._res = res
        else:
            strMessage = "ERROR! XSDataEDNAprocImport constructor argument 'res' is not XSDataDouble but %s" % self._res.__class__.__name__
            raise BaseException(strMessage)
        if nres is None:
            self._nres = None
        elif nres.__class__.__name__ == "XSDataDouble":
            self._nres = nres
        else:
            strMessage = "ERROR! XSDataEDNAprocImport constructor argument 'nres' is not XSDataDouble but %s" % self._nres.__class__.__name__
            raise BaseException(strMessage)
        if image_prefix is None:
            self._image_prefix = None
        elif image_prefix.__class__.__name__ == "XSDataString":
            self._image_prefix = image_prefix
        else:
            strMessage = "ERROR! XSDataEDNAprocImport constructor argument 'image_prefix' is not XSDataString but %s" % self._image_prefix.__class__.__name__
            raise BaseException(strMessage)
        if choose_spacegroup is None:
            self._choose_spacegroup = None
        elif choose_spacegroup.__class__.__name__ == "XSDataString":
            self._choose_spacegroup = choose_spacegroup
        else:
            strMessage = "ERROR! XSDataEDNAprocImport constructor argument 'choose_spacegroup' is not XSDataString but %s" % self._choose_spacegroup.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'input_anom' attribute
    def getInput_anom(self): return self._input_anom
    def setInput_anom(self, input_anom):
        if input_anom is None:
            self._input_anom = None
        elif input_anom.__class__.__name__ == "XSDataString":
            self._input_anom = input_anom
        else:
            strMessage = "ERROR! XSDataEDNAprocImport.setInput_anom argument is not XSDataString but %s" % input_anom.__class__.__name__
            raise BaseException(strMessage)
    def delInput_anom(self): self._input_anom = None
    input_anom = property(getInput_anom, setInput_anom, delInput_anom, "Property for input_anom")
    # Methods and properties for the 'input_noanom' attribute
    def getInput_noanom(self): return self._input_noanom
    def setInput_noanom(self, input_noanom):
        if input_noanom is None:
            self._input_noanom = None
        elif input_noanom.__class__.__name__ == "XSDataString":
            self._input_noanom = input_noanom
        else:
            strMessage = "ERROR! XSDataEDNAprocImport.setInput_noanom argument is not XSDataString but %s" % input_noanom.__class__.__name__
            raise BaseException(strMessage)
    def delInput_noanom(self): self._input_noanom = None
    input_noanom = property(getInput_noanom, setInput_noanom, delInput_noanom, "Property for input_noanom")
    # Methods and properties for the 'output_directory' attribute
    def getOutput_directory(self): return self._output_directory
    def setOutput_directory(self, output_directory):
        if output_directory is None:
            self._output_directory = None
        elif output_directory.__class__.__name__ == "XSDataString":
            self._output_directory = output_directory
        else:
            strMessage = "ERROR! XSDataEDNAprocImport.setOutput_directory argument is not XSDataString but %s" % output_directory.__class__.__name__
            raise BaseException(strMessage)
    def delOutput_directory(self): self._output_directory = None
    output_directory = property(getOutput_directory, setOutput_directory, delOutput_directory, "Property for output_directory")
    # Methods and properties for the 'dataCollectionID' attribute
    def getDataCollectionID(self): return self._dataCollectionID
    def setDataCollectionID(self, dataCollectionID):
        if dataCollectionID is None:
            self._dataCollectionID = None
        elif dataCollectionID.__class__.__name__ == "XSDataInteger":
            self._dataCollectionID = dataCollectionID
        else:
            strMessage = "ERROR! XSDataEDNAprocImport.setDataCollectionID argument is not XSDataInteger but %s" % dataCollectionID.__class__.__name__
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
            strMessage = "ERROR! XSDataEDNAprocImport.setStart_image argument is not XSDataInteger but %s" % start_image.__class__.__name__
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
            strMessage = "ERROR! XSDataEDNAprocImport.setEnd_image argument is not XSDataInteger but %s" % end_image.__class__.__name__
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
            strMessage = "ERROR! XSDataEDNAprocImport.setRes argument is not XSDataDouble but %s" % res.__class__.__name__
            raise BaseException(strMessage)
    def delRes(self): self._res = None
    res = property(getRes, setRes, delRes, "Property for res")
    # Methods and properties for the 'nres' attribute
    def getNres(self): return self._nres
    def setNres(self, nres):
        if nres is None:
            self._nres = None
        elif nres.__class__.__name__ == "XSDataDouble":
            self._nres = nres
        else:
            strMessage = "ERROR! XSDataEDNAprocImport.setNres argument is not XSDataDouble but %s" % nres.__class__.__name__
            raise BaseException(strMessage)
    def delNres(self): self._nres = None
    nres = property(getNres, setNres, delNres, "Property for nres")
    # Methods and properties for the 'image_prefix' attribute
    def getImage_prefix(self): return self._image_prefix
    def setImage_prefix(self, image_prefix):
        if image_prefix is None:
            self._image_prefix = None
        elif image_prefix.__class__.__name__ == "XSDataString":
            self._image_prefix = image_prefix
        else:
            strMessage = "ERROR! XSDataEDNAprocImport.setImage_prefix argument is not XSDataString but %s" % image_prefix.__class__.__name__
            raise BaseException(strMessage)
    def delImage_prefix(self): self._image_prefix = None
    image_prefix = property(getImage_prefix, setImage_prefix, delImage_prefix, "Property for image_prefix")
    # Methods and properties for the 'choose_spacegroup' attribute
    def getChoose_spacegroup(self): return self._choose_spacegroup
    def setChoose_spacegroup(self, choose_spacegroup):
        if choose_spacegroup is None:
            self._choose_spacegroup = None
        elif choose_spacegroup.__class__.__name__ == "XSDataString":
            self._choose_spacegroup = choose_spacegroup
        else:
            strMessage = "ERROR! XSDataEDNAprocImport.setChoose_spacegroup argument is not XSDataString but %s" % choose_spacegroup.__class__.__name__
            raise BaseException(strMessage)
    def delChoose_spacegroup(self): self._choose_spacegroup = None
    choose_spacegroup = property(getChoose_spacegroup, setChoose_spacegroup, delChoose_spacegroup, "Property for choose_spacegroup")
    def export(self, outfile, level, name_='XSDataEDNAprocImport'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataEDNAprocImport'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._input_anom is not None:
            self.input_anom.export(outfile, level, name_='input_anom')
        else:
            warnEmptyAttribute("input_anom", "XSDataString")
        if self._input_noanom is not None:
            self.input_noanom.export(outfile, level, name_='input_noanom')
        else:
            warnEmptyAttribute("input_noanom", "XSDataString")
        if self._output_directory is not None:
            self.output_directory.export(outfile, level, name_='output_directory')
        else:
            warnEmptyAttribute("output_directory", "XSDataString")
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
        if self._nres is not None:
            self.nres.export(outfile, level, name_='nres')
        else:
            warnEmptyAttribute("nres", "XSDataDouble")
        if self._image_prefix is not None:
            self.image_prefix.export(outfile, level, name_='image_prefix')
        if self._choose_spacegroup is not None:
            self.choose_spacegroup.export(outfile, level, name_='choose_spacegroup')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'input_anom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setInput_anom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'input_noanom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setInput_noanom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'output_directory':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setOutput_directory(obj_)
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
            nodeName_ == 'nres':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setNres(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image_prefix':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setImage_prefix(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'choose_spacegroup':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setChoose_spacegroup(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataEDNAprocImport" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataEDNAprocImport' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataEDNAprocImport is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataEDNAprocImport.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataEDNAprocImport()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataEDNAprocImport" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataEDNAprocImport()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataEDNAprocImport


class XSDataEDNAprocImportOut(XSDataResult):
    def __init__(self, status=None, aimless_log_noanom=None, aimless_log_anom=None, pointless_cell=None, pointless_sgstring=None, pointless_sgnumber=None, files=None):
        XSDataResult.__init__(self, status)
        if files is None:
            self._files = []
        elif files.__class__.__name__ == "list":
            self._files = files
        else:
            strMessage = "ERROR! XSDataEDNAprocImportOut constructor argument 'files' is not list but %s" % self._files.__class__.__name__
            raise BaseException(strMessage)
        if pointless_sgnumber is None:
            self._pointless_sgnumber = None
        elif pointless_sgnumber.__class__.__name__ == "XSDataInteger":
            self._pointless_sgnumber = pointless_sgnumber
        else:
            strMessage = "ERROR! XSDataEDNAprocImportOut constructor argument 'pointless_sgnumber' is not XSDataInteger but %s" % self._pointless_sgnumber.__class__.__name__
            raise BaseException(strMessage)
        if pointless_sgstring is None:
            self._pointless_sgstring = None
        elif pointless_sgstring.__class__.__name__ == "XSDataString":
            self._pointless_sgstring = pointless_sgstring
        else:
            strMessage = "ERROR! XSDataEDNAprocImportOut constructor argument 'pointless_sgstring' is not XSDataString but %s" % self._pointless_sgstring.__class__.__name__
            raise BaseException(strMessage)
        if pointless_cell is None:
            self._pointless_cell = []
        elif pointless_cell.__class__.__name__ == "list":
            self._pointless_cell = pointless_cell
        else:
            strMessage = "ERROR! XSDataEDNAprocImportOut constructor argument 'pointless_cell' is not list but %s" % self._pointless_cell.__class__.__name__
            raise BaseException(strMessage)
        if aimless_log_anom is None:
            self._aimless_log_anom = None
        elif aimless_log_anom.__class__.__name__ == "XSDataString":
            self._aimless_log_anom = aimless_log_anom
        else:
            strMessage = "ERROR! XSDataEDNAprocImportOut constructor argument 'aimless_log_anom' is not XSDataString but %s" % self._aimless_log_anom.__class__.__name__
            raise BaseException(strMessage)
        if aimless_log_noanom is None:
            self._aimless_log_noanom = None
        elif aimless_log_noanom.__class__.__name__ == "XSDataString":
            self._aimless_log_noanom = aimless_log_noanom
        else:
            strMessage = "ERROR! XSDataEDNAprocImportOut constructor argument 'aimless_log_noanom' is not XSDataString but %s" % self._aimless_log_noanom.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'files' attribute
    def getFiles(self): return self._files
    def setFiles(self, files):
        if files is None:
            self._files = []
        elif files.__class__.__name__ == "list":
            self._files = files
        else:
            strMessage = "ERROR! XSDataEDNAprocImportOut.setFiles argument is not list but %s" % files.__class__.__name__
            raise BaseException(strMessage)
    def delFiles(self): self._files = None
    files = property(getFiles, setFiles, delFiles, "Property for files")
    def addFiles(self, value):
        if value is None:
            strMessage = "ERROR! XSDataEDNAprocImportOut.addFiles argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataString":
            self._files.append(value)
        else:
            strMessage = "ERROR! XSDataEDNAprocImportOut.addFiles argument is not XSDataString but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertFiles(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataEDNAprocImportOut.insertFiles argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataEDNAprocImportOut.insertFiles argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataString":
            self._files[index] = value
        else:
            strMessage = "ERROR! XSDataEDNAprocImportOut.addFiles argument is not XSDataString but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'pointless_sgnumber' attribute
    def getPointless_sgnumber(self): return self._pointless_sgnumber
    def setPointless_sgnumber(self, pointless_sgnumber):
        if pointless_sgnumber is None:
            self._pointless_sgnumber = None
        elif pointless_sgnumber.__class__.__name__ == "XSDataInteger":
            self._pointless_sgnumber = pointless_sgnumber
        else:
            strMessage = "ERROR! XSDataEDNAprocImportOut.setPointless_sgnumber argument is not XSDataInteger but %s" % pointless_sgnumber.__class__.__name__
            raise BaseException(strMessage)
    def delPointless_sgnumber(self): self._pointless_sgnumber = None
    pointless_sgnumber = property(getPointless_sgnumber, setPointless_sgnumber, delPointless_sgnumber, "Property for pointless_sgnumber")
    # Methods and properties for the 'pointless_sgstring' attribute
    def getPointless_sgstring(self): return self._pointless_sgstring
    def setPointless_sgstring(self, pointless_sgstring):
        if pointless_sgstring is None:
            self._pointless_sgstring = None
        elif pointless_sgstring.__class__.__name__ == "XSDataString":
            self._pointless_sgstring = pointless_sgstring
        else:
            strMessage = "ERROR! XSDataEDNAprocImportOut.setPointless_sgstring argument is not XSDataString but %s" % pointless_sgstring.__class__.__name__
            raise BaseException(strMessage)
    def delPointless_sgstring(self): self._pointless_sgstring = None
    pointless_sgstring = property(getPointless_sgstring, setPointless_sgstring, delPointless_sgstring, "Property for pointless_sgstring")
    # Methods and properties for the 'pointless_cell' attribute
    def getPointless_cell(self): return self._pointless_cell
    def setPointless_cell(self, pointless_cell):
        if pointless_cell is None:
            self._pointless_cell = []
        elif pointless_cell.__class__.__name__ == "list":
            self._pointless_cell = pointless_cell
        else:
            strMessage = "ERROR! XSDataEDNAprocImportOut.setPointless_cell argument is not list but %s" % pointless_cell.__class__.__name__
            raise BaseException(strMessage)
    def delPointless_cell(self): self._pointless_cell = None
    pointless_cell = property(getPointless_cell, setPointless_cell, delPointless_cell, "Property for pointless_cell")
    def addPointless_cell(self, value):
        if value is None:
            strMessage = "ERROR! XSDataEDNAprocImportOut.addPointless_cell argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._pointless_cell.append(value)
        else:
            strMessage = "ERROR! XSDataEDNAprocImportOut.addPointless_cell argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertPointless_cell(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataEDNAprocImportOut.insertPointless_cell argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataEDNAprocImportOut.insertPointless_cell argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._pointless_cell[index] = value
        else:
            strMessage = "ERROR! XSDataEDNAprocImportOut.addPointless_cell argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'aimless_log_anom' attribute
    def getAimless_log_anom(self): return self._aimless_log_anom
    def setAimless_log_anom(self, aimless_log_anom):
        if aimless_log_anom is None:
            self._aimless_log_anom = None
        elif aimless_log_anom.__class__.__name__ == "XSDataString":
            self._aimless_log_anom = aimless_log_anom
        else:
            strMessage = "ERROR! XSDataEDNAprocImportOut.setAimless_log_anom argument is not XSDataString but %s" % aimless_log_anom.__class__.__name__
            raise BaseException(strMessage)
    def delAimless_log_anom(self): self._aimless_log_anom = None
    aimless_log_anom = property(getAimless_log_anom, setAimless_log_anom, delAimless_log_anom, "Property for aimless_log_anom")
    # Methods and properties for the 'aimless_log_noanom' attribute
    def getAimless_log_noanom(self): return self._aimless_log_noanom
    def setAimless_log_noanom(self, aimless_log_noanom):
        if aimless_log_noanom is None:
            self._aimless_log_noanom = None
        elif aimless_log_noanom.__class__.__name__ == "XSDataString":
            self._aimless_log_noanom = aimless_log_noanom
        else:
            strMessage = "ERROR! XSDataEDNAprocImportOut.setAimless_log_noanom argument is not XSDataString but %s" % aimless_log_noanom.__class__.__name__
            raise BaseException(strMessage)
    def delAimless_log_noanom(self): self._aimless_log_noanom = None
    aimless_log_noanom = property(getAimless_log_noanom, setAimless_log_noanom, delAimless_log_noanom, "Property for aimless_log_noanom")
    def export(self, outfile, level, name_='XSDataEDNAprocImportOut'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataEDNAprocImportOut'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for files_ in self.getFiles():
            files_.export(outfile, level, name_='files')
        if self.getFiles() == []:
            warnEmptyAttribute("files", "XSDataString")
        if self._pointless_sgnumber is not None:
            self.pointless_sgnumber.export(outfile, level, name_='pointless_sgnumber')
        else:
            warnEmptyAttribute("pointless_sgnumber", "XSDataInteger")
        if self._pointless_sgstring is not None:
            self.pointless_sgstring.export(outfile, level, name_='pointless_sgstring')
        else:
            warnEmptyAttribute("pointless_sgstring", "XSDataString")
        for pointless_cell_ in self.getPointless_cell():
            pointless_cell_.export(outfile, level, name_='pointless_cell')
        if self.getPointless_cell() == []:
            warnEmptyAttribute("pointless_cell", "XSDataDouble")
        if self._aimless_log_anom is not None:
            self.aimless_log_anom.export(outfile, level, name_='aimless_log_anom')
        else:
            warnEmptyAttribute("aimless_log_anom", "XSDataString")
        if self._aimless_log_noanom is not None:
            self.aimless_log_noanom.export(outfile, level, name_='aimless_log_noanom')
        else:
            warnEmptyAttribute("aimless_log_noanom", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'files':
            obj_ = XSDataString()
            obj_.build(child_)
            self.files.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pointless_sgnumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setPointless_sgnumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pointless_sgstring':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setPointless_sgstring(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pointless_cell':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.pointless_cell.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aimless_log_anom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setAimless_log_anom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aimless_log_noanom':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setAimless_log_noanom(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataEDNAprocImportOut" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataEDNAprocImportOut' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataEDNAprocImportOut is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataEDNAprocImportOut.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataEDNAprocImportOut()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataEDNAprocImportOut" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataEDNAprocImportOut()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataEDNAprocImportOut


class XSDataEDNAprocInput(XSDataInput):
    def __init__(self, configuration=None, doAnomAndNonanom=None, doAnom=None, reprocess=None, exclude_range=None, end_image=None, start_image=None, output_file=None, unit_cell=None, spacegroup=None, nres=None, low_resolution_limit=None, detector_max_res=None, icat_processed_data_dir=None, data_collection_id=None, cc_half_cutoff=None, r_value_cutoff=None, isig_cutoff=None, completeness_cutoff=None, res_override=None, input_file=None):
        XSDataInput.__init__(self, configuration)
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataFile":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'input_file' is not XSDataFile but %s" % self._input_file.__class__.__name__
            raise BaseException(strMessage)
        if res_override is None:
            self._res_override = None
        elif res_override.__class__.__name__ == "XSDataDouble":
            self._res_override = res_override
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'res_override' is not XSDataDouble but %s" % self._res_override.__class__.__name__
            raise BaseException(strMessage)
        if completeness_cutoff is None:
            self._completeness_cutoff = None
        elif completeness_cutoff.__class__.__name__ == "XSDataDouble":
            self._completeness_cutoff = completeness_cutoff
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'completeness_cutoff' is not XSDataDouble but %s" % self._completeness_cutoff.__class__.__name__
            raise BaseException(strMessage)
        if isig_cutoff is None:
            self._isig_cutoff = None
        elif isig_cutoff.__class__.__name__ == "XSDataDouble":
            self._isig_cutoff = isig_cutoff
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'isig_cutoff' is not XSDataDouble but %s" % self._isig_cutoff.__class__.__name__
            raise BaseException(strMessage)
        if r_value_cutoff is None:
            self._r_value_cutoff = None
        elif r_value_cutoff.__class__.__name__ == "XSDataDouble":
            self._r_value_cutoff = r_value_cutoff
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'r_value_cutoff' is not XSDataDouble but %s" % self._r_value_cutoff.__class__.__name__
            raise BaseException(strMessage)
        if cc_half_cutoff is None:
            self._cc_half_cutoff = None
        elif cc_half_cutoff.__class__.__name__ == "XSDataDouble":
            self._cc_half_cutoff = cc_half_cutoff
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'cc_half_cutoff' is not XSDataDouble but %s" % self._cc_half_cutoff.__class__.__name__
            raise BaseException(strMessage)
        if data_collection_id is None:
            self._data_collection_id = None
        elif data_collection_id.__class__.__name__ == "XSDataInteger":
            self._data_collection_id = data_collection_id
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'data_collection_id' is not XSDataInteger but %s" % self._data_collection_id.__class__.__name__
            raise BaseException(strMessage)
        if icat_processed_data_dir is None:
            self._icat_processed_data_dir = None
        elif icat_processed_data_dir.__class__.__name__ == "XSDataString":
            self._icat_processed_data_dir = icat_processed_data_dir
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'icat_processed_data_dir' is not XSDataString but %s" % self._icat_processed_data_dir.__class__.__name__
            raise BaseException(strMessage)
        if detector_max_res is None:
            self._detector_max_res = None
        elif detector_max_res.__class__.__name__ == "XSDataDouble":
            self._detector_max_res = detector_max_res
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'detector_max_res' is not XSDataDouble but %s" % self._detector_max_res.__class__.__name__
            raise BaseException(strMessage)
        if low_resolution_limit is None:
            self._low_resolution_limit = None
        elif low_resolution_limit.__class__.__name__ == "XSDataDouble":
            self._low_resolution_limit = low_resolution_limit
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'low_resolution_limit' is not XSDataDouble but %s" % self._low_resolution_limit.__class__.__name__
            raise BaseException(strMessage)
        if nres is None:
            self._nres = None
        elif nres.__class__.__name__ == "XSDataDouble":
            self._nres = nres
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'nres' is not XSDataDouble but %s" % self._nres.__class__.__name__
            raise BaseException(strMessage)
        if spacegroup is None:
            self._spacegroup = None
        elif spacegroup.__class__.__name__ == "XSDataString":
            self._spacegroup = spacegroup
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'spacegroup' is not XSDataString but %s" % self._spacegroup.__class__.__name__
            raise BaseException(strMessage)
        if unit_cell is None:
            self._unit_cell = None
        elif unit_cell.__class__.__name__ == "XSDataString":
            self._unit_cell = unit_cell
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'unit_cell' is not XSDataString but %s" % self._unit_cell.__class__.__name__
            raise BaseException(strMessage)
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataFile":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'output_file' is not XSDataFile but %s" % self._output_file.__class__.__name__
            raise BaseException(strMessage)
        if start_image is None:
            self._start_image = None
        elif start_image.__class__.__name__ == "XSDataInteger":
            self._start_image = start_image
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'start_image' is not XSDataInteger but %s" % self._start_image.__class__.__name__
            raise BaseException(strMessage)
        if end_image is None:
            self._end_image = None
        elif end_image.__class__.__name__ == "XSDataInteger":
            self._end_image = end_image
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'end_image' is not XSDataInteger but %s" % self._end_image.__class__.__name__
            raise BaseException(strMessage)
        if exclude_range is None:
            self._exclude_range = []
        elif exclude_range.__class__.__name__ == "list":
            self._exclude_range = exclude_range
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'exclude_range' is not list but %s" % self._exclude_range.__class__.__name__
            raise BaseException(strMessage)
        if reprocess is None:
            self._reprocess = None
        elif reprocess.__class__.__name__ == "XSDataBoolean":
            self._reprocess = reprocess
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'reprocess' is not XSDataBoolean but %s" % self._reprocess.__class__.__name__
            raise BaseException(strMessage)
        if doAnom is None:
            self._doAnom = None
        elif doAnom.__class__.__name__ == "XSDataBoolean":
            self._doAnom = doAnom
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'doAnom' is not XSDataBoolean but %s" % self._doAnom.__class__.__name__
            raise BaseException(strMessage)
        if doAnomAndNonanom is None:
            self._doAnomAndNonanom = None
        elif doAnomAndNonanom.__class__.__name__ == "XSDataBoolean":
            self._doAnomAndNonanom = doAnomAndNonanom
        else:
            strMessage = "ERROR! XSDataEDNAprocInput constructor argument 'doAnomAndNonanom' is not XSDataBoolean but %s" % self._doAnomAndNonanom.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'input_file' attribute
    def getInput_file(self): return self._input_file
    def setInput_file(self, input_file):
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataFile":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.setInput_file argument is not XSDataFile but %s" % input_file.__class__.__name__
            raise BaseException(strMessage)
    def delInput_file(self): self._input_file = None
    input_file = property(getInput_file, setInput_file, delInput_file, "Property for input_file")
    # Methods and properties for the 'res_override' attribute
    def getRes_override(self): return self._res_override
    def setRes_override(self, res_override):
        if res_override is None:
            self._res_override = None
        elif res_override.__class__.__name__ == "XSDataDouble":
            self._res_override = res_override
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.setRes_override argument is not XSDataDouble but %s" % res_override.__class__.__name__
            raise BaseException(strMessage)
    def delRes_override(self): self._res_override = None
    res_override = property(getRes_override, setRes_override, delRes_override, "Property for res_override")
    # Methods and properties for the 'completeness_cutoff' attribute
    def getCompleteness_cutoff(self): return self._completeness_cutoff
    def setCompleteness_cutoff(self, completeness_cutoff):
        if completeness_cutoff is None:
            self._completeness_cutoff = None
        elif completeness_cutoff.__class__.__name__ == "XSDataDouble":
            self._completeness_cutoff = completeness_cutoff
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.setCompleteness_cutoff argument is not XSDataDouble but %s" % completeness_cutoff.__class__.__name__
            raise BaseException(strMessage)
    def delCompleteness_cutoff(self): self._completeness_cutoff = None
    completeness_cutoff = property(getCompleteness_cutoff, setCompleteness_cutoff, delCompleteness_cutoff, "Property for completeness_cutoff")
    # Methods and properties for the 'isig_cutoff' attribute
    def getIsig_cutoff(self): return self._isig_cutoff
    def setIsig_cutoff(self, isig_cutoff):
        if isig_cutoff is None:
            self._isig_cutoff = None
        elif isig_cutoff.__class__.__name__ == "XSDataDouble":
            self._isig_cutoff = isig_cutoff
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.setIsig_cutoff argument is not XSDataDouble but %s" % isig_cutoff.__class__.__name__
            raise BaseException(strMessage)
    def delIsig_cutoff(self): self._isig_cutoff = None
    isig_cutoff = property(getIsig_cutoff, setIsig_cutoff, delIsig_cutoff, "Property for isig_cutoff")
    # Methods and properties for the 'r_value_cutoff' attribute
    def getR_value_cutoff(self): return self._r_value_cutoff
    def setR_value_cutoff(self, r_value_cutoff):
        if r_value_cutoff is None:
            self._r_value_cutoff = None
        elif r_value_cutoff.__class__.__name__ == "XSDataDouble":
            self._r_value_cutoff = r_value_cutoff
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.setR_value_cutoff argument is not XSDataDouble but %s" % r_value_cutoff.__class__.__name__
            raise BaseException(strMessage)
    def delR_value_cutoff(self): self._r_value_cutoff = None
    r_value_cutoff = property(getR_value_cutoff, setR_value_cutoff, delR_value_cutoff, "Property for r_value_cutoff")
    # Methods and properties for the 'cc_half_cutoff' attribute
    def getCc_half_cutoff(self): return self._cc_half_cutoff
    def setCc_half_cutoff(self, cc_half_cutoff):
        if cc_half_cutoff is None:
            self._cc_half_cutoff = None
        elif cc_half_cutoff.__class__.__name__ == "XSDataDouble":
            self._cc_half_cutoff = cc_half_cutoff
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.setCc_half_cutoff argument is not XSDataDouble but %s" % cc_half_cutoff.__class__.__name__
            raise BaseException(strMessage)
    def delCc_half_cutoff(self): self._cc_half_cutoff = None
    cc_half_cutoff = property(getCc_half_cutoff, setCc_half_cutoff, delCc_half_cutoff, "Property for cc_half_cutoff")
    # Methods and properties for the 'data_collection_id' attribute
    def getData_collection_id(self): return self._data_collection_id
    def setData_collection_id(self, data_collection_id):
        if data_collection_id is None:
            self._data_collection_id = None
        elif data_collection_id.__class__.__name__ == "XSDataInteger":
            self._data_collection_id = data_collection_id
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.setData_collection_id argument is not XSDataInteger but %s" % data_collection_id.__class__.__name__
            raise BaseException(strMessage)
    def delData_collection_id(self): self._data_collection_id = None
    data_collection_id = property(getData_collection_id, setData_collection_id, delData_collection_id, "Property for data_collection_id")
    # Methods and properties for the 'icat_processed_data_dir' attribute
    def getIcat_processed_data_dir(self): return self._icat_processed_data_dir
    def setIcat_processed_data_dir(self, icat_processed_data_dir):
        if icat_processed_data_dir is None:
            self._icat_processed_data_dir = None
        elif icat_processed_data_dir.__class__.__name__ == "XSDataString":
            self._icat_processed_data_dir = icat_processed_data_dir
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.setIcat_processed_data_dir argument is not XSDataString but %s" % icat_processed_data_dir.__class__.__name__
            raise BaseException(strMessage)
    def delIcat_processed_data_dir(self): self._icat_processed_data_dir = None
    icat_processed_data_dir = property(getIcat_processed_data_dir, setIcat_processed_data_dir, delIcat_processed_data_dir, "Property for icat_processed_data_dir")
    # Methods and properties for the 'detector_max_res' attribute
    def getDetector_max_res(self): return self._detector_max_res
    def setDetector_max_res(self, detector_max_res):
        if detector_max_res is None:
            self._detector_max_res = None
        elif detector_max_res.__class__.__name__ == "XSDataDouble":
            self._detector_max_res = detector_max_res
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.setDetector_max_res argument is not XSDataDouble but %s" % detector_max_res.__class__.__name__
            raise BaseException(strMessage)
    def delDetector_max_res(self): self._detector_max_res = None
    detector_max_res = property(getDetector_max_res, setDetector_max_res, delDetector_max_res, "Property for detector_max_res")
    # Methods and properties for the 'low_resolution_limit' attribute
    def getLow_resolution_limit(self): return self._low_resolution_limit
    def setLow_resolution_limit(self, low_resolution_limit):
        if low_resolution_limit is None:
            self._low_resolution_limit = None
        elif low_resolution_limit.__class__.__name__ == "XSDataDouble":
            self._low_resolution_limit = low_resolution_limit
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.setLow_resolution_limit argument is not XSDataDouble but %s" % low_resolution_limit.__class__.__name__
            raise BaseException(strMessage)
    def delLow_resolution_limit(self): self._low_resolution_limit = None
    low_resolution_limit = property(getLow_resolution_limit, setLow_resolution_limit, delLow_resolution_limit, "Property for low_resolution_limit")
    # Methods and properties for the 'nres' attribute
    def getNres(self): return self._nres
    def setNres(self, nres):
        if nres is None:
            self._nres = None
        elif nres.__class__.__name__ == "XSDataDouble":
            self._nres = nres
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.setNres argument is not XSDataDouble but %s" % nres.__class__.__name__
            raise BaseException(strMessage)
    def delNres(self): self._nres = None
    nres = property(getNres, setNres, delNres, "Property for nres")
    # Methods and properties for the 'spacegroup' attribute
    def getSpacegroup(self): return self._spacegroup
    def setSpacegroup(self, spacegroup):
        if spacegroup is None:
            self._spacegroup = None
        elif spacegroup.__class__.__name__ == "XSDataString":
            self._spacegroup = spacegroup
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.setSpacegroup argument is not XSDataString but %s" % spacegroup.__class__.__name__
            raise BaseException(strMessage)
    def delSpacegroup(self): self._spacegroup = None
    spacegroup = property(getSpacegroup, setSpacegroup, delSpacegroup, "Property for spacegroup")
    # Methods and properties for the 'unit_cell' attribute
    def getUnit_cell(self): return self._unit_cell
    def setUnit_cell(self, unit_cell):
        if unit_cell is None:
            self._unit_cell = None
        elif unit_cell.__class__.__name__ == "XSDataString":
            self._unit_cell = unit_cell
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.setUnit_cell argument is not XSDataString but %s" % unit_cell.__class__.__name__
            raise BaseException(strMessage)
    def delUnit_cell(self): self._unit_cell = None
    unit_cell = property(getUnit_cell, setUnit_cell, delUnit_cell, "Property for unit_cell")
    # Methods and properties for the 'output_file' attribute
    def getOutput_file(self): return self._output_file
    def setOutput_file(self, output_file):
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataFile":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.setOutput_file argument is not XSDataFile but %s" % output_file.__class__.__name__
            raise BaseException(strMessage)
    def delOutput_file(self): self._output_file = None
    output_file = property(getOutput_file, setOutput_file, delOutput_file, "Property for output_file")
    # Methods and properties for the 'start_image' attribute
    def getStart_image(self): return self._start_image
    def setStart_image(self, start_image):
        if start_image is None:
            self._start_image = None
        elif start_image.__class__.__name__ == "XSDataInteger":
            self._start_image = start_image
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.setStart_image argument is not XSDataInteger but %s" % start_image.__class__.__name__
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
            strMessage = "ERROR! XSDataEDNAprocInput.setEnd_image argument is not XSDataInteger but %s" % end_image.__class__.__name__
            raise BaseException(strMessage)
    def delEnd_image(self): self._end_image = None
    end_image = property(getEnd_image, setEnd_image, delEnd_image, "Property for end_image")
    # Methods and properties for the 'exclude_range' attribute
    def getExclude_range(self): return self._exclude_range
    def setExclude_range(self, exclude_range):
        if exclude_range is None:
            self._exclude_range = []
        elif exclude_range.__class__.__name__ == "list":
            self._exclude_range = exclude_range
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.setExclude_range argument is not list but %s" % exclude_range.__class__.__name__
            raise BaseException(strMessage)
    def delExclude_range(self): self._exclude_range = None
    exclude_range = property(getExclude_range, setExclude_range, delExclude_range, "Property for exclude_range")
    def addExclude_range(self, value):
        if value is None:
            strMessage = "ERROR! XSDataEDNAprocInput.addExclude_range argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataRange":
            self._exclude_range.append(value)
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.addExclude_range argument is not XSDataRange but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertExclude_range(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataEDNAprocInput.insertExclude_range argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataEDNAprocInput.insertExclude_range argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataRange":
            self._exclude_range[index] = value
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.addExclude_range argument is not XSDataRange but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'reprocess' attribute
    def getReprocess(self): return self._reprocess
    def setReprocess(self, reprocess):
        if reprocess is None:
            self._reprocess = None
        elif reprocess.__class__.__name__ == "XSDataBoolean":
            self._reprocess = reprocess
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.setReprocess argument is not XSDataBoolean but %s" % reprocess.__class__.__name__
            raise BaseException(strMessage)
    def delReprocess(self): self._reprocess = None
    reprocess = property(getReprocess, setReprocess, delReprocess, "Property for reprocess")
    # Methods and properties for the 'doAnom' attribute
    def getDoAnom(self): return self._doAnom
    def setDoAnom(self, doAnom):
        if doAnom is None:
            self._doAnom = None
        elif doAnom.__class__.__name__ == "XSDataBoolean":
            self._doAnom = doAnom
        else:
            strMessage = "ERROR! XSDataEDNAprocInput.setDoAnom argument is not XSDataBoolean but %s" % doAnom.__class__.__name__
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
            strMessage = "ERROR! XSDataEDNAprocInput.setDoAnomAndNonanom argument is not XSDataBoolean but %s" % doAnomAndNonanom.__class__.__name__
            raise BaseException(strMessage)
    def delDoAnomAndNonanom(self): self._doAnomAndNonanom = None
    doAnomAndNonanom = property(getDoAnomAndNonanom, setDoAnomAndNonanom, delDoAnomAndNonanom, "Property for doAnomAndNonanom")
    def export(self, outfile, level, name_='XSDataEDNAprocInput'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataEDNAprocInput'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._input_file is not None:
            self.input_file.export(outfile, level, name_='input_file')
        else:
            warnEmptyAttribute("input_file", "XSDataFile")
        if self._res_override is not None:
            self.res_override.export(outfile, level, name_='res_override')
        if self._completeness_cutoff is not None:
            self.completeness_cutoff.export(outfile, level, name_='completeness_cutoff')
        if self._isig_cutoff is not None:
            self.isig_cutoff.export(outfile, level, name_='isig_cutoff')
        if self._r_value_cutoff is not None:
            self.r_value_cutoff.export(outfile, level, name_='r_value_cutoff')
        if self._cc_half_cutoff is not None:
            self.cc_half_cutoff.export(outfile, level, name_='cc_half_cutoff')
        if self._data_collection_id is not None:
            self.data_collection_id.export(outfile, level, name_='data_collection_id')
        if self._icat_processed_data_dir is not None:
            self.icat_processed_data_dir.export(outfile, level, name_='icat_processed_data_dir')
        if self._detector_max_res is not None:
            self.detector_max_res.export(outfile, level, name_='detector_max_res')
        if self._low_resolution_limit is not None:
            self.low_resolution_limit.export(outfile, level, name_='low_resolution_limit')
        if self._nres is not None:
            self.nres.export(outfile, level, name_='nres')
        if self._spacegroup is not None:
            self.spacegroup.export(outfile, level, name_='spacegroup')
        if self._unit_cell is not None:
            self.unit_cell.export(outfile, level, name_='unit_cell')
        if self._output_file is not None:
            self.output_file.export(outfile, level, name_='output_file')
        if self._start_image is not None:
            self.start_image.export(outfile, level, name_='start_image')
        if self._end_image is not None:
            self.end_image.export(outfile, level, name_='end_image')
        for exclude_range_ in self.getExclude_range():
            exclude_range_.export(outfile, level, name_='exclude_range')
        if self._reprocess is not None:
            self.reprocess.export(outfile, level, name_='reprocess')
        if self._doAnom is not None:
            self.doAnom.export(outfile, level, name_='doAnom')
        if self._doAnomAndNonanom is not None:
            self.doAnomAndNonanom.export(outfile, level, name_='doAnomAndNonanom')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'input_file':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setInput_file(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'res_override':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRes_override(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'completeness_cutoff':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCompleteness_cutoff(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'isig_cutoff':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setIsig_cutoff(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'r_value_cutoff':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setR_value_cutoff(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cc_half_cutoff':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCc_half_cutoff(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'data_collection_id':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setData_collection_id(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'icat_processed_data_dir':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setIcat_processed_data_dir(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detector_max_res':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDetector_max_res(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'low_resolution_limit':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setLow_resolution_limit(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nres':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setNres(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spacegroup':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSpacegroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit_cell':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setUnit_cell(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'output_file':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutput_file(obj_)
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
            nodeName_ == 'exclude_range':
            obj_ = XSDataRange()
            obj_.build(child_)
            self.exclude_range.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'reprocess':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setReprocess(obj_)
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
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataEDNAprocInput" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataEDNAprocInput' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataEDNAprocInput is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataEDNAprocInput.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataEDNAprocInput()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataEDNAprocInput" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataEDNAprocInput()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataEDNAprocInput


class XSDataFileConversion(XSDataInput):
    def __init__(self, configuration=None, image_prefix=None, choose_spacegroup=None, anom=None, nres=None, res=None, end_image=None, start_image=None, dataCollectionID=None, output_file=None, input_file=None):
        XSDataInput.__init__(self, configuration)
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataFileConversion constructor argument 'input_file' is not XSDataString but %s" % self._input_file.__class__.__name__
            raise BaseException(strMessage)
        if output_file is None:
            self._output_file = None
        elif output_file.__class__.__name__ == "XSDataString":
            self._output_file = output_file
        else:
            strMessage = "ERROR! XSDataFileConversion constructor argument 'output_file' is not XSDataString but %s" % self._output_file.__class__.__name__
            raise BaseException(strMessage)
        if dataCollectionID is None:
            self._dataCollectionID = None
        elif dataCollectionID.__class__.__name__ == "XSDataInteger":
            self._dataCollectionID = dataCollectionID
        else:
            strMessage = "ERROR! XSDataFileConversion constructor argument 'dataCollectionID' is not XSDataInteger but %s" % self._dataCollectionID.__class__.__name__
            raise BaseException(strMessage)
        if start_image is None:
            self._start_image = None
        elif start_image.__class__.__name__ == "XSDataInteger":
            self._start_image = start_image
        else:
            strMessage = "ERROR! XSDataFileConversion constructor argument 'start_image' is not XSDataInteger but %s" % self._start_image.__class__.__name__
            raise BaseException(strMessage)
        if end_image is None:
            self._end_image = None
        elif end_image.__class__.__name__ == "XSDataInteger":
            self._end_image = end_image
        else:
            strMessage = "ERROR! XSDataFileConversion constructor argument 'end_image' is not XSDataInteger but %s" % self._end_image.__class__.__name__
            raise BaseException(strMessage)
        if res is None:
            self._res = None
        elif res.__class__.__name__ == "XSDataDouble":
            self._res = res
        else:
            strMessage = "ERROR! XSDataFileConversion constructor argument 'res' is not XSDataDouble but %s" % self._res.__class__.__name__
            raise BaseException(strMessage)
        if nres is None:
            self._nres = None
        elif nres.__class__.__name__ == "XSDataDouble":
            self._nres = nres
        else:
            strMessage = "ERROR! XSDataFileConversion constructor argument 'nres' is not XSDataDouble but %s" % self._nres.__class__.__name__
            raise BaseException(strMessage)
        if anom is None:
            self._anom = None
        elif anom.__class__.__name__ == "XSDataBoolean":
            self._anom = anom
        else:
            strMessage = "ERROR! XSDataFileConversion constructor argument 'anom' is not XSDataBoolean but %s" % self._anom.__class__.__name__
            raise BaseException(strMessage)
        if choose_spacegroup is None:
            self._choose_spacegroup = None
        elif choose_spacegroup.__class__.__name__ == "XSDataString":
            self._choose_spacegroup = choose_spacegroup
        else:
            strMessage = "ERROR! XSDataFileConversion constructor argument 'choose_spacegroup' is not XSDataString but %s" % self._choose_spacegroup.__class__.__name__
            raise BaseException(strMessage)
        if image_prefix is None:
            self._image_prefix = None
        elif image_prefix.__class__.__name__ == "XSDataString":
            self._image_prefix = image_prefix
        else:
            strMessage = "ERROR! XSDataFileConversion constructor argument 'image_prefix' is not XSDataString but %s" % self._image_prefix.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'input_file' attribute
    def getInput_file(self): return self._input_file
    def setInput_file(self, input_file):
        if input_file is None:
            self._input_file = None
        elif input_file.__class__.__name__ == "XSDataString":
            self._input_file = input_file
        else:
            strMessage = "ERROR! XSDataFileConversion.setInput_file argument is not XSDataString but %s" % input_file.__class__.__name__
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
            strMessage = "ERROR! XSDataFileConversion.setOutput_file argument is not XSDataString but %s" % output_file.__class__.__name__
            raise BaseException(strMessage)
    def delOutput_file(self): self._output_file = None
    output_file = property(getOutput_file, setOutput_file, delOutput_file, "Property for output_file")
    # Methods and properties for the 'dataCollectionID' attribute
    def getDataCollectionID(self): return self._dataCollectionID
    def setDataCollectionID(self, dataCollectionID):
        if dataCollectionID is None:
            self._dataCollectionID = None
        elif dataCollectionID.__class__.__name__ == "XSDataInteger":
            self._dataCollectionID = dataCollectionID
        else:
            strMessage = "ERROR! XSDataFileConversion.setDataCollectionID argument is not XSDataInteger but %s" % dataCollectionID.__class__.__name__
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
            strMessage = "ERROR! XSDataFileConversion.setStart_image argument is not XSDataInteger but %s" % start_image.__class__.__name__
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
            strMessage = "ERROR! XSDataFileConversion.setEnd_image argument is not XSDataInteger but %s" % end_image.__class__.__name__
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
            strMessage = "ERROR! XSDataFileConversion.setRes argument is not XSDataDouble but %s" % res.__class__.__name__
            raise BaseException(strMessage)
    def delRes(self): self._res = None
    res = property(getRes, setRes, delRes, "Property for res")
    # Methods and properties for the 'nres' attribute
    def getNres(self): return self._nres
    def setNres(self, nres):
        if nres is None:
            self._nres = None
        elif nres.__class__.__name__ == "XSDataDouble":
            self._nres = nres
        else:
            strMessage = "ERROR! XSDataFileConversion.setNres argument is not XSDataDouble but %s" % nres.__class__.__name__
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
            strMessage = "ERROR! XSDataFileConversion.setAnom argument is not XSDataBoolean but %s" % anom.__class__.__name__
            raise BaseException(strMessage)
    def delAnom(self): self._anom = None
    anom = property(getAnom, setAnom, delAnom, "Property for anom")
    # Methods and properties for the 'choose_spacegroup' attribute
    def getChoose_spacegroup(self): return self._choose_spacegroup
    def setChoose_spacegroup(self, choose_spacegroup):
        if choose_spacegroup is None:
            self._choose_spacegroup = None
        elif choose_spacegroup.__class__.__name__ == "XSDataString":
            self._choose_spacegroup = choose_spacegroup
        else:
            strMessage = "ERROR! XSDataFileConversion.setChoose_spacegroup argument is not XSDataString but %s" % choose_spacegroup.__class__.__name__
            raise BaseException(strMessage)
    def delChoose_spacegroup(self): self._choose_spacegroup = None
    choose_spacegroup = property(getChoose_spacegroup, setChoose_spacegroup, delChoose_spacegroup, "Property for choose_spacegroup")
    # Methods and properties for the 'image_prefix' attribute
    def getImage_prefix(self): return self._image_prefix
    def setImage_prefix(self, image_prefix):
        if image_prefix is None:
            self._image_prefix = None
        elif image_prefix.__class__.__name__ == "XSDataString":
            self._image_prefix = image_prefix
        else:
            strMessage = "ERROR! XSDataFileConversion.setImage_prefix argument is not XSDataString but %s" % image_prefix.__class__.__name__
            raise BaseException(strMessage)
    def delImage_prefix(self): self._image_prefix = None
    image_prefix = property(getImage_prefix, setImage_prefix, delImage_prefix, "Property for image_prefix")
    def export(self, outfile, level, name_='XSDataFileConversion'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataFileConversion'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._input_file is not None:
            self.input_file.export(outfile, level, name_='input_file')
        else:
            warnEmptyAttribute("input_file", "XSDataString")
        if self._output_file is not None:
            self.output_file.export(outfile, level, name_='output_file')
        else:
            warnEmptyAttribute("output_file", "XSDataString")
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
        if self._nres is not None:
            self.nres.export(outfile, level, name_='nres')
        else:
            warnEmptyAttribute("nres", "XSDataDouble")
        if self._anom is not None:
            self.anom.export(outfile, level, name_='anom')
        else:
            warnEmptyAttribute("anom", "XSDataBoolean")
        if self._choose_spacegroup is not None:
            self.choose_spacegroup.export(outfile, level, name_='choose_spacegroup')
        if self._image_prefix is not None:
            self.image_prefix.export(outfile, level, name_='image_prefix')
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
            nodeName_ == 'choose_spacegroup':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setChoose_spacegroup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image_prefix':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setImage_prefix(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataFileConversion" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataFileConversion' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataFileConversion is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataFileConversion.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFileConversion()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataFileConversion" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFileConversion()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataFileConversion


class XSDataFileConversionOut(XSDataResult):
    def __init__(self, status=None, aimless_log=None, pointless_cell=None, pointless_sgstring=None, pointless_sgnumber=None):
        XSDataResult.__init__(self, status)
        if pointless_sgnumber is None:
            self._pointless_sgnumber = None
        elif pointless_sgnumber.__class__.__name__ == "XSDataInteger":
            self._pointless_sgnumber = pointless_sgnumber
        else:
            strMessage = "ERROR! XSDataFileConversionOut constructor argument 'pointless_sgnumber' is not XSDataInteger but %s" % self._pointless_sgnumber.__class__.__name__
            raise BaseException(strMessage)
        if pointless_sgstring is None:
            self._pointless_sgstring = None
        elif pointless_sgstring.__class__.__name__ == "XSDataString":
            self._pointless_sgstring = pointless_sgstring
        else:
            strMessage = "ERROR! XSDataFileConversionOut constructor argument 'pointless_sgstring' is not XSDataString but %s" % self._pointless_sgstring.__class__.__name__
            raise BaseException(strMessage)
        if pointless_cell is None:
            self._pointless_cell = []
        elif pointless_cell.__class__.__name__ == "list":
            self._pointless_cell = pointless_cell
        else:
            strMessage = "ERROR! XSDataFileConversionOut constructor argument 'pointless_cell' is not list but %s" % self._pointless_cell.__class__.__name__
            raise BaseException(strMessage)
        if aimless_log is None:
            self._aimless_log = None
        elif aimless_log.__class__.__name__ == "XSDataString":
            self._aimless_log = aimless_log
        else:
            strMessage = "ERROR! XSDataFileConversionOut constructor argument 'aimless_log' is not XSDataString but %s" % self._aimless_log.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'pointless_sgnumber' attribute
    def getPointless_sgnumber(self): return self._pointless_sgnumber
    def setPointless_sgnumber(self, pointless_sgnumber):
        if pointless_sgnumber is None:
            self._pointless_sgnumber = None
        elif pointless_sgnumber.__class__.__name__ == "XSDataInteger":
            self._pointless_sgnumber = pointless_sgnumber
        else:
            strMessage = "ERROR! XSDataFileConversionOut.setPointless_sgnumber argument is not XSDataInteger but %s" % pointless_sgnumber.__class__.__name__
            raise BaseException(strMessage)
    def delPointless_sgnumber(self): self._pointless_sgnumber = None
    pointless_sgnumber = property(getPointless_sgnumber, setPointless_sgnumber, delPointless_sgnumber, "Property for pointless_sgnumber")
    # Methods and properties for the 'pointless_sgstring' attribute
    def getPointless_sgstring(self): return self._pointless_sgstring
    def setPointless_sgstring(self, pointless_sgstring):
        if pointless_sgstring is None:
            self._pointless_sgstring = None
        elif pointless_sgstring.__class__.__name__ == "XSDataString":
            self._pointless_sgstring = pointless_sgstring
        else:
            strMessage = "ERROR! XSDataFileConversionOut.setPointless_sgstring argument is not XSDataString but %s" % pointless_sgstring.__class__.__name__
            raise BaseException(strMessage)
    def delPointless_sgstring(self): self._pointless_sgstring = None
    pointless_sgstring = property(getPointless_sgstring, setPointless_sgstring, delPointless_sgstring, "Property for pointless_sgstring")
    # Methods and properties for the 'pointless_cell' attribute
    def getPointless_cell(self): return self._pointless_cell
    def setPointless_cell(self, pointless_cell):
        if pointless_cell is None:
            self._pointless_cell = []
        elif pointless_cell.__class__.__name__ == "list":
            self._pointless_cell = pointless_cell
        else:
            strMessage = "ERROR! XSDataFileConversionOut.setPointless_cell argument is not list but %s" % pointless_cell.__class__.__name__
            raise BaseException(strMessage)
    def delPointless_cell(self): self._pointless_cell = None
    pointless_cell = property(getPointless_cell, setPointless_cell, delPointless_cell, "Property for pointless_cell")
    def addPointless_cell(self, value):
        if value is None:
            strMessage = "ERROR! XSDataFileConversionOut.addPointless_cell argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._pointless_cell.append(value)
        else:
            strMessage = "ERROR! XSDataFileConversionOut.addPointless_cell argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertPointless_cell(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataFileConversionOut.insertPointless_cell argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataFileConversionOut.insertPointless_cell argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._pointless_cell[index] = value
        else:
            strMessage = "ERROR! XSDataFileConversionOut.addPointless_cell argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'aimless_log' attribute
    def getAimless_log(self): return self._aimless_log
    def setAimless_log(self, aimless_log):
        if aimless_log is None:
            self._aimless_log = None
        elif aimless_log.__class__.__name__ == "XSDataString":
            self._aimless_log = aimless_log
        else:
            strMessage = "ERROR! XSDataFileConversionOut.setAimless_log argument is not XSDataString but %s" % aimless_log.__class__.__name__
            raise BaseException(strMessage)
    def delAimless_log(self): self._aimless_log = None
    aimless_log = property(getAimless_log, setAimless_log, delAimless_log, "Property for aimless_log")
    def export(self, outfile, level, name_='XSDataFileConversionOut'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataFileConversionOut'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._pointless_sgnumber is not None:
            self.pointless_sgnumber.export(outfile, level, name_='pointless_sgnumber')
        else:
            warnEmptyAttribute("pointless_sgnumber", "XSDataInteger")
        if self._pointless_sgstring is not None:
            self.pointless_sgstring.export(outfile, level, name_='pointless_sgstring')
        else:
            warnEmptyAttribute("pointless_sgstring", "XSDataString")
        for pointless_cell_ in self.getPointless_cell():
            pointless_cell_.export(outfile, level, name_='pointless_cell')
        if self.getPointless_cell() == []:
            warnEmptyAttribute("pointless_cell", "XSDataDouble")
        if self._aimless_log is not None:
            self.aimless_log.export(outfile, level, name_='aimless_log')
        else:
            warnEmptyAttribute("aimless_log", "XSDataString")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pointless_sgnumber':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setPointless_sgnumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pointless_sgstring':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setPointless_sgstring(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pointless_cell':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.pointless_cell.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aimless_log':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setAimless_log(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataFileConversionOut" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataFileConversionOut' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataFileConversionOut is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataFileConversionOut.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFileConversionOut()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataFileConversionOut" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFileConversionOut()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataFileConversionOut


class XSDataInputControlDimple(XSDataInput):
    def __init__(self, configuration=None, resultsDirectory=None, autoProcProgramId=None, pdbDirectory=None, beamline=None, sessionDate=None, proposal=None, imagePrefix=None, pyarchPath=None, mtzFile=None, dataCollectionId=None):
        XSDataInput.__init__(self, configuration)
        if dataCollectionId is None:
            self._dataCollectionId = None
        elif dataCollectionId.__class__.__name__ == "XSDataInteger":
            self._dataCollectionId = dataCollectionId
        else:
            strMessage = "ERROR! XSDataInputControlDimple constructor argument 'dataCollectionId' is not XSDataInteger but %s" % self._dataCollectionId.__class__.__name__
            raise BaseException(strMessage)
        if mtzFile is None:
            self._mtzFile = None
        elif mtzFile.__class__.__name__ == "XSDataFile":
            self._mtzFile = mtzFile
        else:
            strMessage = "ERROR! XSDataInputControlDimple constructor argument 'mtzFile' is not XSDataFile but %s" % self._mtzFile.__class__.__name__
            raise BaseException(strMessage)
        if pyarchPath is None:
            self._pyarchPath = None
        elif pyarchPath.__class__.__name__ == "XSDataFile":
            self._pyarchPath = pyarchPath
        else:
            strMessage = "ERROR! XSDataInputControlDimple constructor argument 'pyarchPath' is not XSDataFile but %s" % self._pyarchPath.__class__.__name__
            raise BaseException(strMessage)
        if imagePrefix is None:
            self._imagePrefix = None
        elif imagePrefix.__class__.__name__ == "XSDataString":
            self._imagePrefix = imagePrefix
        else:
            strMessage = "ERROR! XSDataInputControlDimple constructor argument 'imagePrefix' is not XSDataString but %s" % self._imagePrefix.__class__.__name__
            raise BaseException(strMessage)
        if proposal is None:
            self._proposal = None
        elif proposal.__class__.__name__ == "XSDataString":
            self._proposal = proposal
        else:
            strMessage = "ERROR! XSDataInputControlDimple constructor argument 'proposal' is not XSDataString but %s" % self._proposal.__class__.__name__
            raise BaseException(strMessage)
        if sessionDate is None:
            self._sessionDate = None
        elif sessionDate.__class__.__name__ == "XSDataString":
            self._sessionDate = sessionDate
        else:
            strMessage = "ERROR! XSDataInputControlDimple constructor argument 'sessionDate' is not XSDataString but %s" % self._sessionDate.__class__.__name__
            raise BaseException(strMessage)
        if beamline is None:
            self._beamline = None
        elif beamline.__class__.__name__ == "XSDataString":
            self._beamline = beamline
        else:
            strMessage = "ERROR! XSDataInputControlDimple constructor argument 'beamline' is not XSDataString but %s" % self._beamline.__class__.__name__
            raise BaseException(strMessage)
        if pdbDirectory is None:
            self._pdbDirectory = None
        elif pdbDirectory.__class__.__name__ == "XSDataFile":
            self._pdbDirectory = pdbDirectory
        else:
            strMessage = "ERROR! XSDataInputControlDimple constructor argument 'pdbDirectory' is not XSDataFile but %s" % self._pdbDirectory.__class__.__name__
            raise BaseException(strMessage)
        if autoProcProgramId is None:
            self._autoProcProgramId = None
        elif autoProcProgramId.__class__.__name__ == "XSDataInteger":
            self._autoProcProgramId = autoProcProgramId
        else:
            strMessage = "ERROR! XSDataInputControlDimple constructor argument 'autoProcProgramId' is not XSDataInteger but %s" % self._autoProcProgramId.__class__.__name__
            raise BaseException(strMessage)
        if resultsDirectory is None:
            self._resultsDirectory = None
        elif resultsDirectory.__class__.__name__ == "XSDataFile":
            self._resultsDirectory = resultsDirectory
        else:
            strMessage = "ERROR! XSDataInputControlDimple constructor argument 'resultsDirectory' is not XSDataFile but %s" % self._resultsDirectory.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'dataCollectionId' attribute
    def getDataCollectionId(self): return self._dataCollectionId
    def setDataCollectionId(self, dataCollectionId):
        if dataCollectionId is None:
            self._dataCollectionId = None
        elif dataCollectionId.__class__.__name__ == "XSDataInteger":
            self._dataCollectionId = dataCollectionId
        else:
            strMessage = "ERROR! XSDataInputControlDimple.setDataCollectionId argument is not XSDataInteger but %s" % dataCollectionId.__class__.__name__
            raise BaseException(strMessage)
    def delDataCollectionId(self): self._dataCollectionId = None
    dataCollectionId = property(getDataCollectionId, setDataCollectionId, delDataCollectionId, "Property for dataCollectionId")
    # Methods and properties for the 'mtzFile' attribute
    def getMtzFile(self): return self._mtzFile
    def setMtzFile(self, mtzFile):
        if mtzFile is None:
            self._mtzFile = None
        elif mtzFile.__class__.__name__ == "XSDataFile":
            self._mtzFile = mtzFile
        else:
            strMessage = "ERROR! XSDataInputControlDimple.setMtzFile argument is not XSDataFile but %s" % mtzFile.__class__.__name__
            raise BaseException(strMessage)
    def delMtzFile(self): self._mtzFile = None
    mtzFile = property(getMtzFile, setMtzFile, delMtzFile, "Property for mtzFile")
    # Methods and properties for the 'pyarchPath' attribute
    def getPyarchPath(self): return self._pyarchPath
    def setPyarchPath(self, pyarchPath):
        if pyarchPath is None:
            self._pyarchPath = None
        elif pyarchPath.__class__.__name__ == "XSDataFile":
            self._pyarchPath = pyarchPath
        else:
            strMessage = "ERROR! XSDataInputControlDimple.setPyarchPath argument is not XSDataFile but %s" % pyarchPath.__class__.__name__
            raise BaseException(strMessage)
    def delPyarchPath(self): self._pyarchPath = None
    pyarchPath = property(getPyarchPath, setPyarchPath, delPyarchPath, "Property for pyarchPath")
    # Methods and properties for the 'imagePrefix' attribute
    def getImagePrefix(self): return self._imagePrefix
    def setImagePrefix(self, imagePrefix):
        if imagePrefix is None:
            self._imagePrefix = None
        elif imagePrefix.__class__.__name__ == "XSDataString":
            self._imagePrefix = imagePrefix
        else:
            strMessage = "ERROR! XSDataInputControlDimple.setImagePrefix argument is not XSDataString but %s" % imagePrefix.__class__.__name__
            raise BaseException(strMessage)
    def delImagePrefix(self): self._imagePrefix = None
    imagePrefix = property(getImagePrefix, setImagePrefix, delImagePrefix, "Property for imagePrefix")
    # Methods and properties for the 'proposal' attribute
    def getProposal(self): return self._proposal
    def setProposal(self, proposal):
        if proposal is None:
            self._proposal = None
        elif proposal.__class__.__name__ == "XSDataString":
            self._proposal = proposal
        else:
            strMessage = "ERROR! XSDataInputControlDimple.setProposal argument is not XSDataString but %s" % proposal.__class__.__name__
            raise BaseException(strMessage)
    def delProposal(self): self._proposal = None
    proposal = property(getProposal, setProposal, delProposal, "Property for proposal")
    # Methods and properties for the 'sessionDate' attribute
    def getSessionDate(self): return self._sessionDate
    def setSessionDate(self, sessionDate):
        if sessionDate is None:
            self._sessionDate = None
        elif sessionDate.__class__.__name__ == "XSDataString":
            self._sessionDate = sessionDate
        else:
            strMessage = "ERROR! XSDataInputControlDimple.setSessionDate argument is not XSDataString but %s" % sessionDate.__class__.__name__
            raise BaseException(strMessage)
    def delSessionDate(self): self._sessionDate = None
    sessionDate = property(getSessionDate, setSessionDate, delSessionDate, "Property for sessionDate")
    # Methods and properties for the 'beamline' attribute
    def getBeamline(self): return self._beamline
    def setBeamline(self, beamline):
        if beamline is None:
            self._beamline = None
        elif beamline.__class__.__name__ == "XSDataString":
            self._beamline = beamline
        else:
            strMessage = "ERROR! XSDataInputControlDimple.setBeamline argument is not XSDataString but %s" % beamline.__class__.__name__
            raise BaseException(strMessage)
    def delBeamline(self): self._beamline = None
    beamline = property(getBeamline, setBeamline, delBeamline, "Property for beamline")
    # Methods and properties for the 'pdbDirectory' attribute
    def getPdbDirectory(self): return self._pdbDirectory
    def setPdbDirectory(self, pdbDirectory):
        if pdbDirectory is None:
            self._pdbDirectory = None
        elif pdbDirectory.__class__.__name__ == "XSDataFile":
            self._pdbDirectory = pdbDirectory
        else:
            strMessage = "ERROR! XSDataInputControlDimple.setPdbDirectory argument is not XSDataFile but %s" % pdbDirectory.__class__.__name__
            raise BaseException(strMessage)
    def delPdbDirectory(self): self._pdbDirectory = None
    pdbDirectory = property(getPdbDirectory, setPdbDirectory, delPdbDirectory, "Property for pdbDirectory")
    # Methods and properties for the 'autoProcProgramId' attribute
    def getAutoProcProgramId(self): return self._autoProcProgramId
    def setAutoProcProgramId(self, autoProcProgramId):
        if autoProcProgramId is None:
            self._autoProcProgramId = None
        elif autoProcProgramId.__class__.__name__ == "XSDataInteger":
            self._autoProcProgramId = autoProcProgramId
        else:
            strMessage = "ERROR! XSDataInputControlDimple.setAutoProcProgramId argument is not XSDataInteger but %s" % autoProcProgramId.__class__.__name__
            raise BaseException(strMessage)
    def delAutoProcProgramId(self): self._autoProcProgramId = None
    autoProcProgramId = property(getAutoProcProgramId, setAutoProcProgramId, delAutoProcProgramId, "Property for autoProcProgramId")
    # Methods and properties for the 'resultsDirectory' attribute
    def getResultsDirectory(self): return self._resultsDirectory
    def setResultsDirectory(self, resultsDirectory):
        if resultsDirectory is None:
            self._resultsDirectory = None
        elif resultsDirectory.__class__.__name__ == "XSDataFile":
            self._resultsDirectory = resultsDirectory
        else:
            strMessage = "ERROR! XSDataInputControlDimple.setResultsDirectory argument is not XSDataFile but %s" % resultsDirectory.__class__.__name__
            raise BaseException(strMessage)
    def delResultsDirectory(self): self._resultsDirectory = None
    resultsDirectory = property(getResultsDirectory, setResultsDirectory, delResultsDirectory, "Property for resultsDirectory")
    def export(self, outfile, level, name_='XSDataInputControlDimple'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputControlDimple'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._dataCollectionId is not None:
            self.dataCollectionId.export(outfile, level, name_='dataCollectionId')
        else:
            warnEmptyAttribute("dataCollectionId", "XSDataInteger")
        if self._mtzFile is not None:
            self.mtzFile.export(outfile, level, name_='mtzFile')
        else:
            warnEmptyAttribute("mtzFile", "XSDataFile")
        if self._pyarchPath is not None:
            self.pyarchPath.export(outfile, level, name_='pyarchPath')
        else:
            warnEmptyAttribute("pyarchPath", "XSDataFile")
        if self._imagePrefix is not None:
            self.imagePrefix.export(outfile, level, name_='imagePrefix')
        else:
            warnEmptyAttribute("imagePrefix", "XSDataString")
        if self._proposal is not None:
            self.proposal.export(outfile, level, name_='proposal')
        else:
            warnEmptyAttribute("proposal", "XSDataString")
        if self._sessionDate is not None:
            self.sessionDate.export(outfile, level, name_='sessionDate')
        else:
            warnEmptyAttribute("sessionDate", "XSDataString")
        if self._beamline is not None:
            self.beamline.export(outfile, level, name_='beamline')
        else:
            warnEmptyAttribute("beamline", "XSDataString")
        if self._pdbDirectory is not None:
            self.pdbDirectory.export(outfile, level, name_='pdbDirectory')
        if self._autoProcProgramId is not None:
            self.autoProcProgramId.export(outfile, level, name_='autoProcProgramId')
        if self._resultsDirectory is not None:
            self.resultsDirectory.export(outfile, level, name_='resultsDirectory')
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
            nodeName_ == 'mtzFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setMtzFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pyarchPath':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPyarchPath(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'imagePrefix':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setImagePrefix(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'proposal':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setProposal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sessionDate':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSessionDate(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamline':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setBeamline(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbDirectory':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdbDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoProcProgramId':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setAutoProcProgramId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'resultsDirectory':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setResultsDirectory(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputControlDimple" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputControlDimple' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputControlDimple is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputControlDimple.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputControlDimple()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputControlDimple" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputControlDimple()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputControlDimple


class XSDataResultControlDimple(XSDataResult):
    def __init__(self, status=None, dimpleExecutedSuccessfully=None):
        XSDataResult.__init__(self, status)
        if dimpleExecutedSuccessfully is None:
            self._dimpleExecutedSuccessfully = None
        elif dimpleExecutedSuccessfully.__class__.__name__ == "XSDataBoolean":
            self._dimpleExecutedSuccessfully = dimpleExecutedSuccessfully
        else:
            strMessage = "ERROR! XSDataResultControlDimple constructor argument 'dimpleExecutedSuccessfully' is not XSDataBoolean but %s" % self._dimpleExecutedSuccessfully.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'dimpleExecutedSuccessfully' attribute
    def getDimpleExecutedSuccessfully(self): return self._dimpleExecutedSuccessfully
    def setDimpleExecutedSuccessfully(self, dimpleExecutedSuccessfully):
        if dimpleExecutedSuccessfully is None:
            self._dimpleExecutedSuccessfully = None
        elif dimpleExecutedSuccessfully.__class__.__name__ == "XSDataBoolean":
            self._dimpleExecutedSuccessfully = dimpleExecutedSuccessfully
        else:
            strMessage = "ERROR! XSDataResultControlDimple.setDimpleExecutedSuccessfully argument is not XSDataBoolean but %s" % dimpleExecutedSuccessfully.__class__.__name__
            raise BaseException(strMessage)
    def delDimpleExecutedSuccessfully(self): self._dimpleExecutedSuccessfully = None
    dimpleExecutedSuccessfully = property(getDimpleExecutedSuccessfully, setDimpleExecutedSuccessfully, delDimpleExecutedSuccessfully, "Property for dimpleExecutedSuccessfully")
    def export(self, outfile, level, name_='XSDataResultControlDimple'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultControlDimple'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._dimpleExecutedSuccessfully is not None:
            self.dimpleExecutedSuccessfully.export(outfile, level, name_='dimpleExecutedSuccessfully')
        else:
            warnEmptyAttribute("dimpleExecutedSuccessfully", "XSDataBoolean")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dimpleExecutedSuccessfully':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setDimpleExecutedSuccessfully(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultControlDimple" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultControlDimple' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultControlDimple is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultControlDimple.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultControlDimple()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultControlDimple" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultControlDimple()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultControlDimple



# End of data representation classes.


