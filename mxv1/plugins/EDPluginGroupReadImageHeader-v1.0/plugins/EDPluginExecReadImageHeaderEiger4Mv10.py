#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2014 European Synchrotron Radiation Facility
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



class EDPluginExecReadImageHeaderEiger4Mv10(EDPluginExec):


    def __init__(self):
        """
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputReadImageHeader)
        self.__xsDataResultReadImageHeader = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecReadImageHeaderEiger4Mv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")


    def process(self, _edObject=None):
        EDPluginExec.process(self)
        self.DEBUG("EDPluginExecReadImageHeaderEiger4Mv10.process")
        xsDataInputReadImageHeader = self.getDataInput()
        xsDataFile = xsDataInputReadImageHeader.getImage()
        strPath = xsDataFile.getPath().getValue()
        dictEiger4MHeader = self.readHeaderEiger4M(strPath)
        if (dictEiger4MHeader is None):
            strErrorMessage = "EDPluginExecReadImageHeaderEiger4Mv10.process : Cannot read header : %s" % strPath
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
        else:
            xsDataExperimentalCondition = XSDataExperimentalCondition()
            xsDataDetector = XSDataDetector()

            iNoPixelsX = 2070
            iNoPixelsY = 2167
            xsDataDetector.setNumberPixelX(XSDataInteger(iNoPixelsX))
            xsDataDetector.setNumberPixelY(XSDataInteger(iNoPixelsY))
            # Pixel size
            listPixelSizeXY = dictEiger4MHeader[ "Pixel_size"   ].split(" ")
            fPixelSizeX = float(listPixelSizeXY[0]) * 1000
            xsDataDetector.setPixelSizeX(XSDataLength(fPixelSizeX))
            fPixelSizeY = float(listPixelSizeXY[3]) * 1000
            xsDataDetector.setPixelSizeY(XSDataLength(fPixelSizeY))
            # Beam position
            listBeamPosition = dictEiger4MHeader["Beam_xy"].replace("(", " ").replace(")", " ").replace(",", " ").split()
            fBeamPositionX = float(listBeamPosition[1]) * fPixelSizeX
            fBeamPositionY = float(listBeamPosition[0]) * fPixelSizeY
            xsDataDetector.setBeamPositionX(XSDataLength(fBeamPositionX))
            xsDataDetector.setBeamPositionY(XSDataLength(fBeamPositionY))
            fDistance = float(dictEiger4MHeader[ "Detector_distance" ].split(" ")[0]) * 1000
            xsDataDetector.setDistance(XSDataLength(fDistance))
#            xsDataDetector.setNumberBytesInHeader(XSDataInteger(float(dictEiger4MHeader[ "header_size"   ])))
            xsDataDetector.setSerialNumber(XSDataString(dictEiger4MHeader[ "Detector:"   ]))
#            #xsDataDetector.setBin(                 XSDataString(   dictEiger4MHeader[ "BIN" ] ) ) )
#            #xsDataDetector.setDataType(            XSDataString(   dictEiger4MHeader[ "TYPE" ] ) ) )
#            #xsDataDetector.setByteOrder(           XSDataString(   dictEiger4MHeader[ "BYTE_ORDER" ] ) ) )
#            xsDataDetector.setImageSaturation(XSDataInteger(int(dictEiger4MHeader[ "saturation_level" ])))
            xsDataDetector.setName(XSDataString("EIGER 4M"))
            xsDataDetector.setType(XSDataString("eiger4m"))
            xsDataExperimentalCondition.setDetector(xsDataDetector)

            # Beam object

            xsDataBeam = XSDataBeam()
            xsDataBeam.setWavelength(XSDataWavelength(float(dictEiger4MHeader[ "Wavelength" ].split(" ")[0])))
            xsDataBeam.setExposureTime(XSDataTime(float(dictEiger4MHeader[ "Exposure_time" ].split(" ")[0])))
            xsDataExperimentalCondition.setBeam(xsDataBeam)

            # Goniostat object
            xsDataGoniostat = XSDataGoniostat()
            fRotationAxisStart = float(dictEiger4MHeader[ "Start_angle" ].split(" ")[0])
            fOscillationWidth = float(dictEiger4MHeader[ "Angle_increment" ].split(" ")[0])
            xsDataGoniostat.setRotationAxisStart(XSDataAngle(fRotationAxisStart))
            xsDataGoniostat.setRotationAxisEnd(XSDataAngle(fRotationAxisStart + fOscillationWidth))
            xsDataGoniostat.setOscillationWidth(XSDataAngle(fOscillationWidth))
            xsDataExperimentalCondition.setGoniostat(xsDataGoniostat)
#
            # Create the image object
            xsDataImage = XSDataImage()
            xsDataImage.setPath(XSDataString(strPath))
            if "DateTime" in dictEiger4MHeader:
                strTimeStamp = dictEiger4MHeader[ "DateTime" ]
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
        self.DEBUG("EDPluginExecReadImageHeaderEiger4Mv10.postProcess")
        if (self.__xsDataResultReadImageHeader is not None):
            self.setDataOutput(self.__xsDataResultReadImageHeader)


    def readHeaderEiger4M(self, _strImageFileName):
        """
        Returns an dictionary with the contents of a Pilatus 6M CBF image header.
        """
        dictEiger4M = None
        pyFile = None
        try:
            pyFile = open(_strImageFileName, "rb")
        except:
            self.ERROR("EDPluginExecReadImageHeaderEiger4Mv10.readHeaderEiger4M: couldn't open file: " + _strImageFileName)
            self.setFailure()
        if (pyFile != None):
            self.DEBUG("EDPluginExecReadImageHeaderEiger4Mv10.readHeaderEiger4M: Reading header from image " + _strImageFileName)
            pyFile.seek(0, 0)
            bContinue = True
            iMax = 60
            iIndex = 0
            while bContinue:
                strLine = pyFile.readline().decode('utf-8')
                iIndex += 1
                if (strLine.find("_array_data.header_contents") != -1):
                    dictEiger4M = {}
                if (strLine.find("_array_data.data") != -1) or iIndex > iMax:
                    bContinue = False
                if (dictEiger4M != None) and (strLine[0] == "#"):
                    # Check for date
                    strTmp = strLine[2:].replace("\r\n", "")
                    if strLine[6] == "/" and strLine[10] == "/":
                        dictEiger4M["DateTime"] = strTmp
                    else:
                        strKey = strTmp.split(" ")[0]
                        strValue = strTmp.replace(strKey, "")[1:]
                        dictEiger4M[strKey] = strValue
            pyFile.close()
        return dictEiger4M

