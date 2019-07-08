#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2017 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona", "Michael Hellmig" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
import struct

from EDVerbose      import EDVerbose
from EDMessage      import EDMessage
from EDUtilsImage   import EDUtilsImage

from EDPluginExec import EDPluginExec

from XSDataCommon import XSDataWavelength
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataString
from XSDataCommon import XSDataInteger

from XSDataMXv1 import XSDataExperimentalCondition
from XSDataMXv1 import XSDataSubWedge
from XSDataMXv1 import XSDataDetector
from XSDataMXv1 import XSDataBeam
from XSDataMXv1 import XSDataGoniostat
from XSDataMXv1 import XSDataInputReadImageHeader
from XSDataMXv1 import XSDataResultReadImageHeader



class EDPluginExecReadImageHeaderEiger9Mv10(EDPluginExec):


    def __init__(self):
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputReadImageHeader)
        self.__xsDataResultReadImageHeader = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecReadImageHeaderEiger9Mv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")


    def process(self, _edObject=None):
        EDPluginExec.process(self)
        self.DEBUG("EDPluginExecReadImageHeaderEiger9Mv10.process")
        xsDataInputReadImageHeader = self.getDataInput()
        xsDataFile = xsDataInputReadImageHeader.getImage()
        strPath = xsDataFile.getPath().getValue()
        dictEiger9MHeader = self.readHeaderEiger9M(strPath)
        if (dictEiger9MHeader is None):
            strErrorMessage = "EDPluginExecReadImageHeaderEiger9Mv10.process : Cannot read header : %s" % strPath
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
        else:
            xsDataExperimentalCondition = XSDataExperimentalCondition()
            xsDataDetector = XSDataDetector()

            iNoPixelsX = 3110
            iNoPixelsY = 3269
            xsDataDetector.setNumberPixelX(XSDataInteger(iNoPixelsX))
            xsDataDetector.setNumberPixelY(XSDataInteger(iNoPixelsY))
            # Pixel size
            listPixelSizeXY = dictEiger9MHeader[ "Pixel_size"   ].split(" ")
            fPixelSizeX = float(listPixelSizeXY[0]) * 1000
            xsDataDetector.setPixelSizeX(XSDataLength(fPixelSizeX))
            fPixelSizeY = float(listPixelSizeXY[3]) * 1000
            xsDataDetector.setPixelSizeY(XSDataLength(fPixelSizeY))
            # Beam position
            listBeamPosition = dictEiger9MHeader["Beam_xy"].replace("(", " ").replace(")", " ").replace(",", " ").split()
            fBeamPositionX = float(listBeamPosition[1]) * fPixelSizeX
            fBeamPositionY = float(listBeamPosition[0]) * fPixelSizeY
            xsDataDetector.setBeamPositionX(XSDataLength(fBeamPositionX))
            xsDataDetector.setBeamPositionY(XSDataLength(fBeamPositionY))
            fDistance = float(dictEiger9MHeader[ "Detector_distance" ].split(" ")[0]) * 1000
            xsDataDetector.setDistance(XSDataLength(fDistance))
#            xsDataDetector.setNumberBytesInHeader(XSDataInteger(float(dictEiger9MHeader[ "header_size"   ])))
            xsDataDetector.setSerialNumber(XSDataString(dictEiger9MHeader[ "Detector:"   ]))
#            #xsDataDetector.setBin(                 XSDataString(   dictEiger9MHeader[ "BIN" ] ) ) )
#            #xsDataDetector.setDataType(            XSDataString(   dictEiger9MHeader[ "TYPE" ] ) ) )
#            #xsDataDetector.setByteOrder(           XSDataString(   dictEiger9MHeader[ "BYTE_ORDER" ] ) ) )
#            xsDataDetector.setImageSaturation(XSDataInteger(int(dictEiger9MHeader[ "saturation_level" ])))
            xsDataDetector.setName(XSDataString("EIGER 9M"))
            xsDataDetector.setType(XSDataString("eiger9m"))
            xsDataExperimentalCondition.setDetector(xsDataDetector)

            # Beam object

            xsDataBeam = XSDataBeam()
            xsDataBeam.setWavelength(XSDataWavelength(float(dictEiger9MHeader[ "Wavelength" ].split(" ")[0])))
            xsDataBeam.setExposureTime(XSDataTime(float(dictEiger9MHeader[ "Exposure_time" ].split(" ")[0])))
            xsDataExperimentalCondition.setBeam(xsDataBeam)

            # Goniostat object
            xsDataGoniostat = XSDataGoniostat()
            fRotationAxisStart = float(dictEiger9MHeader[ "Start_angle" ].split(" ")[0])
            fOscillationWidth = float(dictEiger9MHeader[ "Angle_increment" ].split(" ")[0])
            xsDataGoniostat.setRotationAxisStart(XSDataAngle(fRotationAxisStart))
            xsDataGoniostat.setRotationAxisEnd(XSDataAngle(fRotationAxisStart + fOscillationWidth))
            xsDataGoniostat.setOscillationWidth(XSDataAngle(fOscillationWidth))
            xsDataExperimentalCondition.setGoniostat(xsDataGoniostat)
#
            # Create the image object
            xsDataImage = XSDataImage()
            xsDataImage.setPath(XSDataString(strPath))
            if "DateTime" in dictEiger9MHeader:
                strTimeStamp = dictEiger9MHeader[ "DateTime" ]
                xsDataImage.setDate(XSDataString(strTimeStamp))
            iImageNumber = EDUtilsImage.getImageNumber(strPath)
            xsDataImage.setNumber(XSDataInteger(iImageNumber))

            xsDataSubWedge = XSDataSubWedge()
            xsDataSubWedge.setExperimentalCondition(xsDataExperimentalCondition)
            xsDataSubWedge.addImage(xsDataImage)

            self.__xsDataResultReadImageHeader = XSDataResultReadImageHeader()
            self.__xsDataResultReadImageHeader.setSubWedge(xsDataSubWedge)


    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginExecReadImageHeaderEiger9Mv10.postProcess")
        if (self.__xsDataResultReadImageHeader is not None):
            self.setDataOutput(self.__xsDataResultReadImageHeader)


    def readHeaderEiger9M(self, _strImageFileName):
        """
        Returns an dictionary with the contents of a Pilatus 6M CBF image header.
        """
        dictEiger9M = None
        pyFile = None
        try:
            pyFile = open(_strImageFileName, "rb")
        except:
            self.ERROR("EDPluginExecReadImageHeaderEiger9Mv10.readHeaderEiger9M: couldn't open file: " + _strImageFileName)
            self.setFailure()
        if (pyFile != None):
            self.DEBUG("EDPluginExecReadImageHeaderEiger9Mv10.readHeaderEiger9M: Reading header from image " + _strImageFileName)
            pyFile.seek(0, 0)
            bContinue = True
            iMax = 60
            iIndex = 0
            while bContinue:
                strLine = pyFile.readline().decode('utf-8')
                iIndex += 1
                if (strLine.find("_array_data.header_contents") != -1):
                    dictEiger9M = {}
                if (strLine.find("_array_data.data") != -1) or iIndex > iMax:
                    bContinue = False
                if (dictEiger9M != None) and (strLine[0] == "#"):
                    # Check for date
                    strTmp = strLine[2:].replace("\r\n", "")
                    if strLine[6] == "/" and strLine[10] == "/":
                        dictEiger9M["DateTime"] = strTmp
                    else:
                        strKey = strTmp.split(" ")[0]
                        strValue = strTmp.replace(strKey, "")[1:]
                        dictEiger9M[strKey] = strValue
            pyFile.close()
        return dictEiger9M

