#!/usr/bin/env python

#
# Generated Tue Oct 23 02:34::56 2018 by EDGenerateDS.
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



class XSDataInputXDSAPP(XSDataInput):
    def __init__(self, configuration=None, spacegroup=None, anomalous=None, endImageNumber=None, startImageNumber=None, image=None):
        XSDataInput.__init__(self, configuration)
        if image is None:
            self._image = None
        elif image.__class__.__name__ == "XSDataFile":
            self._image = image
        else:
            strMessage = "ERROR! XSDataInputXDSAPP constructor argument 'image' is not XSDataFile but %s" % self._image.__class__.__name__
            raise BaseException(strMessage)
        if startImageNumber is None:
            self._startImageNumber = None
        elif startImageNumber.__class__.__name__ == "XSDataInteger":
            self._startImageNumber = startImageNumber
        else:
            strMessage = "ERROR! XSDataInputXDSAPP constructor argument 'startImageNumber' is not XSDataInteger but %s" % self._startImageNumber.__class__.__name__
            raise BaseException(strMessage)
        if endImageNumber is None:
            self._endImageNumber = None
        elif endImageNumber.__class__.__name__ == "XSDataInteger":
            self._endImageNumber = endImageNumber
        else:
            strMessage = "ERROR! XSDataInputXDSAPP constructor argument 'endImageNumber' is not XSDataInteger but %s" % self._endImageNumber.__class__.__name__
            raise BaseException(strMessage)
        if anomalous is None:
            self._anomalous = None
        elif anomalous.__class__.__name__ == "XSDataBoolean":
            self._anomalous = anomalous
        else:
            strMessage = "ERROR! XSDataInputXDSAPP constructor argument 'anomalous' is not XSDataBoolean but %s" % self._anomalous.__class__.__name__
            raise BaseException(strMessage)
        if spacegroup is None:
            self._spacegroup = None
        elif spacegroup.__class__.__name__ == "XSDataString":
            self._spacegroup = spacegroup
        else:
            strMessage = "ERROR! XSDataInputXDSAPP constructor argument 'spacegroup' is not XSDataString but %s" % self._spacegroup.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'image' attribute
    def getImage(self): return self._image
    def setImage(self, image):
        if image is None:
            self._image = None
        elif image.__class__.__name__ == "XSDataFile":
            self._image = image
        else:
            strMessage = "ERROR! XSDataInputXDSAPP.setImage argument is not XSDataFile but %s" % image.__class__.__name__
            raise BaseException(strMessage)
    def delImage(self): self._image = None
    image = property(getImage, setImage, delImage, "Property for image")
    # Methods and properties for the 'startImageNumber' attribute
    def getStartImageNumber(self): return self._startImageNumber
    def setStartImageNumber(self, startImageNumber):
        if startImageNumber is None:
            self._startImageNumber = None
        elif startImageNumber.__class__.__name__ == "XSDataInteger":
            self._startImageNumber = startImageNumber
        else:
            strMessage = "ERROR! XSDataInputXDSAPP.setStartImageNumber argument is not XSDataInteger but %s" % startImageNumber.__class__.__name__
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
            strMessage = "ERROR! XSDataInputXDSAPP.setEndImageNumber argument is not XSDataInteger but %s" % endImageNumber.__class__.__name__
            raise BaseException(strMessage)
    def delEndImageNumber(self): self._endImageNumber = None
    endImageNumber = property(getEndImageNumber, setEndImageNumber, delEndImageNumber, "Property for endImageNumber")
    # Methods and properties for the 'anomalous' attribute
    def getAnomalous(self): return self._anomalous
    def setAnomalous(self, anomalous):
        if anomalous is None:
            self._anomalous = None
        elif anomalous.__class__.__name__ == "XSDataBoolean":
            self._anomalous = anomalous
        else:
            strMessage = "ERROR! XSDataInputXDSAPP.setAnomalous argument is not XSDataBoolean but %s" % anomalous.__class__.__name__
            raise BaseException(strMessage)
    def delAnomalous(self): self._anomalous = None
    anomalous = property(getAnomalous, setAnomalous, delAnomalous, "Property for anomalous")
    # Methods and properties for the 'spacegroup' attribute
    def getSpacegroup(self): return self._spacegroup
    def setSpacegroup(self, spacegroup):
        if spacegroup is None:
            self._spacegroup = None
        elif spacegroup.__class__.__name__ == "XSDataString":
            self._spacegroup = spacegroup
        else:
            strMessage = "ERROR! XSDataInputXDSAPP.setSpacegroup argument is not XSDataString but %s" % spacegroup.__class__.__name__
            raise BaseException(strMessage)
    def delSpacegroup(self): self._spacegroup = None
    spacegroup = property(getSpacegroup, setSpacegroup, delSpacegroup, "Property for spacegroup")
    def export(self, outfile, level, name_='XSDataInputXDSAPP'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputXDSAPP'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._image is not None:
            self.image.export(outfile, level, name_='image')
        else:
            warnEmptyAttribute("image", "XSDataFile")
        if self._startImageNumber is not None:
            self.startImageNumber.export(outfile, level, name_='startImageNumber')
        if self._endImageNumber is not None:
            self.endImageNumber.export(outfile, level, name_='endImageNumber')
        if self._anomalous is not None:
            self.anomalous.export(outfile, level, name_='anomalous')
        if self._spacegroup is not None:
            self.spacegroup.export(outfile, level, name_='spacegroup')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'image':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
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
            nodeName_ == 'anomalous':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setAnomalous(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spacegroup':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSpacegroup(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputXDSAPP" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputXDSAPP' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputXDSAPP is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputXDSAPP.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputXDSAPP()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputXDSAPP" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputXDSAPP()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputXDSAPP


class XSDataResultXDSAPP(XSDataResult):
    def __init__(self, status=None, cv=None, hkl=None, mtz_F_plus_F_minus=None, mtz_I=None, mtz_F=None, XDS_INP=None, XSCALE_LP=None, XDS_ASCII_HKL_1=None, XDS_ASCII_HKL=None, correctLP=None, phenixXtriageLog=None, pointlessLog=None, logFile=None):
        XSDataResult.__init__(self, status)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultXDSAPP constructor argument 'logFile' is not XSDataFile but %s" % self._logFile.__class__.__name__
            raise BaseException(strMessage)
        if pointlessLog is None:
            self._pointlessLog = None
        elif pointlessLog.__class__.__name__ == "XSDataFile":
            self._pointlessLog = pointlessLog
        else:
            strMessage = "ERROR! XSDataResultXDSAPP constructor argument 'pointlessLog' is not XSDataFile but %s" % self._pointlessLog.__class__.__name__
            raise BaseException(strMessage)
        if phenixXtriageLog is None:
            self._phenixXtriageLog = None
        elif phenixXtriageLog.__class__.__name__ == "XSDataFile":
            self._phenixXtriageLog = phenixXtriageLog
        else:
            strMessage = "ERROR! XSDataResultXDSAPP constructor argument 'phenixXtriageLog' is not XSDataFile but %s" % self._phenixXtriageLog.__class__.__name__
            raise BaseException(strMessage)
        if correctLP is None:
            self._correctLP = None
        elif correctLP.__class__.__name__ == "XSDataFile":
            self._correctLP = correctLP
        else:
            strMessage = "ERROR! XSDataResultXDSAPP constructor argument 'correctLP' is not XSDataFile but %s" % self._correctLP.__class__.__name__
            raise BaseException(strMessage)
        if XDS_ASCII_HKL is None:
            self._XDS_ASCII_HKL = None
        elif XDS_ASCII_HKL.__class__.__name__ == "XSDataFile":
            self._XDS_ASCII_HKL = XDS_ASCII_HKL
        else:
            strMessage = "ERROR! XSDataResultXDSAPP constructor argument 'XDS_ASCII_HKL' is not XSDataFile but %s" % self._XDS_ASCII_HKL.__class__.__name__
            raise BaseException(strMessage)
        if XDS_ASCII_HKL_1 is None:
            self._XDS_ASCII_HKL_1 = None
        elif XDS_ASCII_HKL_1.__class__.__name__ == "XSDataFile":
            self._XDS_ASCII_HKL_1 = XDS_ASCII_HKL_1
        else:
            strMessage = "ERROR! XSDataResultXDSAPP constructor argument 'XDS_ASCII_HKL_1' is not XSDataFile but %s" % self._XDS_ASCII_HKL_1.__class__.__name__
            raise BaseException(strMessage)
        if XSCALE_LP is None:
            self._XSCALE_LP = None
        elif XSCALE_LP.__class__.__name__ == "XSDataFile":
            self._XSCALE_LP = XSCALE_LP
        else:
            strMessage = "ERROR! XSDataResultXDSAPP constructor argument 'XSCALE_LP' is not XSDataFile but %s" % self._XSCALE_LP.__class__.__name__
            raise BaseException(strMessage)
        if XDS_INP is None:
            self._XDS_INP = None
        elif XDS_INP.__class__.__name__ == "XSDataFile":
            self._XDS_INP = XDS_INP
        else:
            strMessage = "ERROR! XSDataResultXDSAPP constructor argument 'XDS_INP' is not XSDataFile but %s" % self._XDS_INP.__class__.__name__
            raise BaseException(strMessage)
        if mtz_F is None:
            self._mtz_F = []
        elif mtz_F.__class__.__name__ == "list":
            self._mtz_F = mtz_F
        else:
            strMessage = "ERROR! XSDataResultXDSAPP constructor argument 'mtz_F' is not list but %s" % self._mtz_F.__class__.__name__
            raise BaseException(strMessage)
        if mtz_I is None:
            self._mtz_I = []
        elif mtz_I.__class__.__name__ == "list":
            self._mtz_I = mtz_I
        else:
            strMessage = "ERROR! XSDataResultXDSAPP constructor argument 'mtz_I' is not list but %s" % self._mtz_I.__class__.__name__
            raise BaseException(strMessage)
        if mtz_F_plus_F_minus is None:
            self._mtz_F_plus_F_minus = []
        elif mtz_F_plus_F_minus.__class__.__name__ == "list":
            self._mtz_F_plus_F_minus = mtz_F_plus_F_minus
        else:
            strMessage = "ERROR! XSDataResultXDSAPP constructor argument 'mtz_F_plus_F_minus' is not list but %s" % self._mtz_F_plus_F_minus.__class__.__name__
            raise BaseException(strMessage)
        if hkl is None:
            self._hkl = []
        elif hkl.__class__.__name__ == "list":
            self._hkl = hkl
        else:
            strMessage = "ERROR! XSDataResultXDSAPP constructor argument 'hkl' is not list but %s" % self._hkl.__class__.__name__
            raise BaseException(strMessage)
        if cv is None:
            self._cv = []
        elif cv.__class__.__name__ == "list":
            self._cv = cv
        else:
            strMessage = "ERROR! XSDataResultXDSAPP constructor argument 'cv' is not list but %s" % self._cv.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.setLogFile argument is not XSDataFile but %s" % logFile.__class__.__name__
            raise BaseException(strMessage)
    def delLogFile(self): self._logFile = None
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    # Methods and properties for the 'pointlessLog' attribute
    def getPointlessLog(self): return self._pointlessLog
    def setPointlessLog(self, pointlessLog):
        if pointlessLog is None:
            self._pointlessLog = None
        elif pointlessLog.__class__.__name__ == "XSDataFile":
            self._pointlessLog = pointlessLog
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.setPointlessLog argument is not XSDataFile but %s" % pointlessLog.__class__.__name__
            raise BaseException(strMessage)
    def delPointlessLog(self): self._pointlessLog = None
    pointlessLog = property(getPointlessLog, setPointlessLog, delPointlessLog, "Property for pointlessLog")
    # Methods and properties for the 'phenixXtriageLog' attribute
    def getPhenixXtriageLog(self): return self._phenixXtriageLog
    def setPhenixXtriageLog(self, phenixXtriageLog):
        if phenixXtriageLog is None:
            self._phenixXtriageLog = None
        elif phenixXtriageLog.__class__.__name__ == "XSDataFile":
            self._phenixXtriageLog = phenixXtriageLog
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.setPhenixXtriageLog argument is not XSDataFile but %s" % phenixXtriageLog.__class__.__name__
            raise BaseException(strMessage)
    def delPhenixXtriageLog(self): self._phenixXtriageLog = None
    phenixXtriageLog = property(getPhenixXtriageLog, setPhenixXtriageLog, delPhenixXtriageLog, "Property for phenixXtriageLog")
    # Methods and properties for the 'correctLP' attribute
    def getCorrectLP(self): return self._correctLP
    def setCorrectLP(self, correctLP):
        if correctLP is None:
            self._correctLP = None
        elif correctLP.__class__.__name__ == "XSDataFile":
            self._correctLP = correctLP
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.setCorrectLP argument is not XSDataFile but %s" % correctLP.__class__.__name__
            raise BaseException(strMessage)
    def delCorrectLP(self): self._correctLP = None
    correctLP = property(getCorrectLP, setCorrectLP, delCorrectLP, "Property for correctLP")
    # Methods and properties for the 'XDS_ASCII_HKL' attribute
    def getXDS_ASCII_HKL(self): return self._XDS_ASCII_HKL
    def setXDS_ASCII_HKL(self, XDS_ASCII_HKL):
        if XDS_ASCII_HKL is None:
            self._XDS_ASCII_HKL = None
        elif XDS_ASCII_HKL.__class__.__name__ == "XSDataFile":
            self._XDS_ASCII_HKL = XDS_ASCII_HKL
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.setXDS_ASCII_HKL argument is not XSDataFile but %s" % XDS_ASCII_HKL.__class__.__name__
            raise BaseException(strMessage)
    def delXDS_ASCII_HKL(self): self._XDS_ASCII_HKL = None
    XDS_ASCII_HKL = property(getXDS_ASCII_HKL, setXDS_ASCII_HKL, delXDS_ASCII_HKL, "Property for XDS_ASCII_HKL")
    # Methods and properties for the 'XDS_ASCII_HKL_1' attribute
    def getXDS_ASCII_HKL_1(self): return self._XDS_ASCII_HKL_1
    def setXDS_ASCII_HKL_1(self, XDS_ASCII_HKL_1):
        if XDS_ASCII_HKL_1 is None:
            self._XDS_ASCII_HKL_1 = None
        elif XDS_ASCII_HKL_1.__class__.__name__ == "XSDataFile":
            self._XDS_ASCII_HKL_1 = XDS_ASCII_HKL_1
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.setXDS_ASCII_HKL_1 argument is not XSDataFile but %s" % XDS_ASCII_HKL_1.__class__.__name__
            raise BaseException(strMessage)
    def delXDS_ASCII_HKL_1(self): self._XDS_ASCII_HKL_1 = None
    XDS_ASCII_HKL_1 = property(getXDS_ASCII_HKL_1, setXDS_ASCII_HKL_1, delXDS_ASCII_HKL_1, "Property for XDS_ASCII_HKL_1")
    # Methods and properties for the 'XSCALE_LP' attribute
    def getXSCALE_LP(self): return self._XSCALE_LP
    def setXSCALE_LP(self, XSCALE_LP):
        if XSCALE_LP is None:
            self._XSCALE_LP = None
        elif XSCALE_LP.__class__.__name__ == "XSDataFile":
            self._XSCALE_LP = XSCALE_LP
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.setXSCALE_LP argument is not XSDataFile but %s" % XSCALE_LP.__class__.__name__
            raise BaseException(strMessage)
    def delXSCALE_LP(self): self._XSCALE_LP = None
    XSCALE_LP = property(getXSCALE_LP, setXSCALE_LP, delXSCALE_LP, "Property for XSCALE_LP")
    # Methods and properties for the 'XDS_INP' attribute
    def getXDS_INP(self): return self._XDS_INP
    def setXDS_INP(self, XDS_INP):
        if XDS_INP is None:
            self._XDS_INP = None
        elif XDS_INP.__class__.__name__ == "XSDataFile":
            self._XDS_INP = XDS_INP
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.setXDS_INP argument is not XSDataFile but %s" % XDS_INP.__class__.__name__
            raise BaseException(strMessage)
    def delXDS_INP(self): self._XDS_INP = None
    XDS_INP = property(getXDS_INP, setXDS_INP, delXDS_INP, "Property for XDS_INP")
    # Methods and properties for the 'mtz_F' attribute
    def getMtz_F(self): return self._mtz_F
    def setMtz_F(self, mtz_F):
        if mtz_F is None:
            self._mtz_F = []
        elif mtz_F.__class__.__name__ == "list":
            self._mtz_F = mtz_F
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.setMtz_F argument is not list but %s" % mtz_F.__class__.__name__
            raise BaseException(strMessage)
    def delMtz_F(self): self._mtz_F = None
    mtz_F = property(getMtz_F, setMtz_F, delMtz_F, "Property for mtz_F")
    def addMtz_F(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultXDSAPP.addMtz_F argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._mtz_F.append(value)
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.addMtz_F argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertMtz_F(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultXDSAPP.insertMtz_F argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultXDSAPP.insertMtz_F argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._mtz_F[index] = value
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.addMtz_F argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'mtz_I' attribute
    def getMtz_I(self): return self._mtz_I
    def setMtz_I(self, mtz_I):
        if mtz_I is None:
            self._mtz_I = []
        elif mtz_I.__class__.__name__ == "list":
            self._mtz_I = mtz_I
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.setMtz_I argument is not list but %s" % mtz_I.__class__.__name__
            raise BaseException(strMessage)
    def delMtz_I(self): self._mtz_I = None
    mtz_I = property(getMtz_I, setMtz_I, delMtz_I, "Property for mtz_I")
    def addMtz_I(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultXDSAPP.addMtz_I argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._mtz_I.append(value)
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.addMtz_I argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertMtz_I(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultXDSAPP.insertMtz_I argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultXDSAPP.insertMtz_I argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._mtz_I[index] = value
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.addMtz_I argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'mtz_F_plus_F_minus' attribute
    def getMtz_F_plus_F_minus(self): return self._mtz_F_plus_F_minus
    def setMtz_F_plus_F_minus(self, mtz_F_plus_F_minus):
        if mtz_F_plus_F_minus is None:
            self._mtz_F_plus_F_minus = []
        elif mtz_F_plus_F_minus.__class__.__name__ == "list":
            self._mtz_F_plus_F_minus = mtz_F_plus_F_minus
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.setMtz_F_plus_F_minus argument is not list but %s" % mtz_F_plus_F_minus.__class__.__name__
            raise BaseException(strMessage)
    def delMtz_F_plus_F_minus(self): self._mtz_F_plus_F_minus = None
    mtz_F_plus_F_minus = property(getMtz_F_plus_F_minus, setMtz_F_plus_F_minus, delMtz_F_plus_F_minus, "Property for mtz_F_plus_F_minus")
    def addMtz_F_plus_F_minus(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultXDSAPP.addMtz_F_plus_F_minus argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._mtz_F_plus_F_minus.append(value)
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.addMtz_F_plus_F_minus argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertMtz_F_plus_F_minus(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultXDSAPP.insertMtz_F_plus_F_minus argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultXDSAPP.insertMtz_F_plus_F_minus argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._mtz_F_plus_F_minus[index] = value
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.addMtz_F_plus_F_minus argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'hkl' attribute
    def getHkl(self): return self._hkl
    def setHkl(self, hkl):
        if hkl is None:
            self._hkl = []
        elif hkl.__class__.__name__ == "list":
            self._hkl = hkl
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.setHkl argument is not list but %s" % hkl.__class__.__name__
            raise BaseException(strMessage)
    def delHkl(self): self._hkl = None
    hkl = property(getHkl, setHkl, delHkl, "Property for hkl")
    def addHkl(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultXDSAPP.addHkl argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._hkl.append(value)
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.addHkl argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertHkl(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultXDSAPP.insertHkl argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultXDSAPP.insertHkl argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._hkl[index] = value
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.addHkl argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'cv' attribute
    def getCv(self): return self._cv
    def setCv(self, cv):
        if cv is None:
            self._cv = []
        elif cv.__class__.__name__ == "list":
            self._cv = cv
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.setCv argument is not list but %s" % cv.__class__.__name__
            raise BaseException(strMessage)
    def delCv(self): self._cv = None
    cv = property(getCv, setCv, delCv, "Property for cv")
    def addCv(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultXDSAPP.addCv argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._cv.append(value)
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.addCv argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertCv(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultXDSAPP.insertCv argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultXDSAPP.insertCv argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._cv[index] = value
        else:
            strMessage = "ERROR! XSDataResultXDSAPP.addCv argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataResultXDSAPP'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultXDSAPP'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_='logFile')
        if self._pointlessLog is not None:
            self.pointlessLog.export(outfile, level, name_='pointlessLog')
        if self._phenixXtriageLog is not None:
            self.phenixXtriageLog.export(outfile, level, name_='phenixXtriageLog')
        if self._correctLP is not None:
            self.correctLP.export(outfile, level, name_='correctLP')
        if self._XDS_ASCII_HKL is not None:
            self.XDS_ASCII_HKL.export(outfile, level, name_='XDS_ASCII_HKL')
        if self._XDS_ASCII_HKL_1 is not None:
            self.XDS_ASCII_HKL_1.export(outfile, level, name_='XDS_ASCII_HKL_1')
        if self._XSCALE_LP is not None:
            self.XSCALE_LP.export(outfile, level, name_='XSCALE_LP')
        if self._XDS_INP is not None:
            self.XDS_INP.export(outfile, level, name_='XDS_INP')
        for mtz_F_ in self.getMtz_F():
            mtz_F_.export(outfile, level, name_='mtz_F')
        for mtz_I_ in self.getMtz_I():
            mtz_I_.export(outfile, level, name_='mtz_I')
        for mtz_F_plus_F_minus_ in self.getMtz_F_plus_F_minus():
            mtz_F_plus_F_minus_.export(outfile, level, name_='mtz_F_plus_F_minus')
        for hkl_ in self.getHkl():
            hkl_.export(outfile, level, name_='hkl')
        for cv_ in self.getCv():
            cv_.export(outfile, level, name_='cv')
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
            nodeName_ == 'pointlessLog':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPointlessLog(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'phenixXtriageLog':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPhenixXtriageLog(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'correctLP':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setCorrectLP(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XDS_ASCII_HKL':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setXDS_ASCII_HKL(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XDS_ASCII_HKL_1':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setXDS_ASCII_HKL_1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XSCALE_LP':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setXSCALE_LP(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'XDS_INP':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setXDS_INP(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mtz_F':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.mtz_F.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mtz_I':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.mtz_I.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mtz_F_plus_F_minus':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.mtz_F_plus_F_minus.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'hkl':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.hkl.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'cv':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.cv.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultXDSAPP" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultXDSAPP' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultXDSAPP is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultXDSAPP.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultXDSAPP()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultXDSAPP" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultXDSAPP()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultXDSAPP



# End of data representation classes.


