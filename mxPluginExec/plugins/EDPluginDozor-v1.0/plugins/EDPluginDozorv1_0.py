# coding: utf8
#
#    Project: MX Plugin Exec
#             http://www.edna-site.org
#
#    Copyright (C) ESRF
#
#    Principal author:       Olof Svensson
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

__author__ = "Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os
import time
import shlex
import distro
import pprint
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDUtilsTable              import EDUtilsTable
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsFile import EDUtilsFile

EDFactoryPluginStatic.loadModule("markupv1_10")
import markupv1_10

from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataAngle

from XSDataDnaTables import dna_tables

from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString

from XSDataDozorv1_0 import XSDataInputDozor
from XSDataDozorv1_0 import XSDataResultDozor
from XSDataDozorv1_0 import XSDataImageDozor

class EDPluginDozorv1_0(EDPluginExecProcessScript):
    """
    This plugin runs the Dozor program written by Sasha Popov
    """


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputDozor)
        self.setDataOutput(XSDataResultDozor())
        self.strImageLinkSubDirectory = "img"
        self.defaultFractionPolarization = 0.99
        self.defaultImageStep = 1
        self.startingAngle = 0.0
        self.firstImageNumber = None
        self.oscillationRange = None
        self.overlap = 0.0
        self.ixMin = None
        self.iyMin = None
        self.ixMax = None
        self.iyMax = None
        # Default values for ESRF Pilatus6M id30b: 1,1230; 1228,1298
        self.ixMinPilatus6m = 1
        self.ixMaxPilatus6m = 1230
        self.iyMinPilatus6m = 1228
        self.iyMaxPilatus6m = 1298
        # Default values for ESRF Pilatus2M : ID30a1: 1,776; 826,894
        self.ixMinPilatus2m = 1
        self.ixMaxPilatus2m = 776
        self.iyMinPilatus2m = 826
        self.iyMaxPilatus2m = 894
        # Default values for ESRF Eiger4M : ID30a3: 1,1120; 1025,1140
        self.ixMinEiger4m = 1
        self.ixMaxEiger4m = 1120
        self.iyMinEiger4m = 1025
        self.iyMaxEiger4m = 1140
        # Default values for ESRF Eiger16M : ID23eh1: 1, 2159, 2087, 2312
        self.ixMinEiger16m = 1
        self.ixMaxEiger16m = 2159
        self.iyMinEiger16m = 2087
        self.iyMaxEiger16m = 2312
        # Bad zones
        self.strBad_zona = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginDozorv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")

    def getLibraryName(self, libraryType, doSubmit=False):
        libraryName = 'library_' + libraryType
        idName, version, codename = distro.linux_distribution()
        if 'Debian' in idName:
            libraryName += '_debian_'
        elif idName == 'Ubuntu':
            libraryName += '_ubuntu_'
        else:
            raise RuntimeError('ExecDozor: unknown os name {0}'.format(idName))
        libraryName += version
        return libraryName

    def configure(self):
        EDPluginExecProcessScript.configure(self)
        self.DEBUG("EDPluginXOalignv1_0.configure")
        self.ixMin = self.config.get("ix_min", None)
        self.iyMin = self.config.get("iy_min", None)
        self.ixMax = self.config.get("ix_max", None)
        self.iyMax = self.config.get("iy_max", None)
        # Eventual bad zones
        self.strBad_zona = self.config.get("bad_zona", None)
        self.library_cbf = self.config.get(self.getLibraryName("cbf"))
        self.library_h5 = self.config.get(self.getLibraryName("h5"))

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginDozorv1_0.preProcess")
        xsDataInputDozor = self.getDataInput()
        # First image number and osc range for output angle calculations
        self.firstImageNumber = xsDataInputDozor.firstImageNumber.value
        self.oscillationRange = xsDataInputDozor.oscillationRange.value
        if xsDataInputDozor.overlap is not None:
            self.overlap = xsDataInputDozor.overlap.value
        if xsDataInputDozor.radiationDamage is not None and xsDataInputDozor.radiationDamage.value:
            self.setScriptCommandline("-pall -rd dozor.dat")
        else:
            self.setScriptCommandline("-pall -p dozor.dat")
        strCommands = self.generateCommands(xsDataInputDozor, _library_cbf=self.library_cbf, _library_h5=self.library_h5)
        EDUtilsFile.writeFile(os.path.join(self.getWorkingDirectory(), "dozor.dat"), strCommands)

    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginDozorv1_0.postProcess")
        self.dataOutput = self.parseOutput(os.path.join(self.getWorkingDirectory(),
                                                        self.getScriptLogFileName()))



    def generateCommands(self, _xsDataInputDozor, _library_cbf=None, _library_h5=None):
        """
        This method creates the input file for dozor
        """
        self.DEBUG("EDPluginDozorv1_0.generateCommands")
        strCommandText = None
        if _xsDataInputDozor.detectorType.value == "pilatus2m":
            library = _library_cbf
            nx = 1475
            ny = 1679
            pixel = 0.172
            if self.ixMin is None or self.ixMax is None or self.iyMin is None or self.iyMax is None:
                self.ixMin = self.ixMinPilatus2m
                self.ixMax = self.ixMaxPilatus2m
                self.iyMin = self.iyMinPilatus2m
                self.iyMax = self.iyMaxPilatus2m
        elif _xsDataInputDozor.detectorType.value == "pilatus6m":
            library = _library_cbf
            nx = 2463
            ny = 2527
            pixel = 0.172
            if self.ixMin is None or self.ixMax is None or self.iyMin is None or self.iyMax is None:
                self.ixMin = self.ixMinPilatus6m
                self.ixMax = self.ixMaxPilatus6m
                self.iyMin = self.iyMinPilatus6m
                self.iyMax = self.iyMaxPilatus6m
        elif _xsDataInputDozor.detectorType.value == "eiger4m":
            library = _library_cbf
            nx = 2070
            ny = 2167
            pixel = 0.075
            if self.ixMin is None or self.ixMax is None or self.iyMin is None or self.iyMax is None:
                self.ixMin = self.ixMinEiger4m
                self.ixMax = self.ixMaxEiger4m
                self.iyMin = self.iyMinEiger4m
                self.iyMax = self.iyMaxEiger4m
        elif _xsDataInputDozor.detectorType.value == "eiger9m":
            library = _library_cbf
            nx = 3108
            ny = 3262
            pixel = 0.075
            if self.ixMin is None or self.ixMax is None or self.iyMin is None or self.iyMax is None:
                self.ixMin = self.ixMinEiger4m
                self.ixMax = self.ixMaxEiger4m
                self.iyMin = self.iyMinEiger4m
                self.iyMax = self.iyMaxEiger4m
        elif _xsDataInputDozor.detectorType.value == "eiger16m":
            library = _library_cbf
            nx = 4150
            ny = 4371
            pixel = 0.075
            if self.ixMin is None or self.ixMax is None or self.iyMin is None or self.iyMax is None:
                self.ixMin = self.ixMinEiger16m
                self.ixMax = self.ixMaxEiger16m
                self.iyMin = self.iyMinEiger16m
                self.iyMax = self.iyMaxEiger16m
        elif _xsDataInputDozor.detectorType.value == "eiger2_16m":
            library = _library_cbf
            nx = 4148
            ny = 4362
            pixel = 0.075
            if self.ixMin is None or self.ixMax is None or self.iyMin is None or self.iyMax is None:
                self.ixMin = self.ixMinEiger16m
                self.ixMax = self.ixMaxEiger16m
                self.iyMin = self.iyMinEiger16m
                self.iyMax = self.iyMaxEiger16m
        else:
            raise RuntimeError("Detector type not recognised: {0}".format(_xsDataInputDozor.detectorType.value))
        if _xsDataInputDozor is not None:
            self.setProcessInfo("name template: %s, first image no: %d, no images: %d" % (
                os.path.basename(_xsDataInputDozor.nameTemplateImage.value),
                _xsDataInputDozor.firstImageNumber.value,
                _xsDataInputDozor.numberImages.value))
            strCommandText = "!\n"
            strCommandText += "detector %s\n" % _xsDataInputDozor.detectorType.value
            strCommandText += "library %s\n" % library
            strCommandText += "nx %d\n" % nx
            strCommandText += "ny %d\n" % ny
            strCommandText += "pixel %f\n" % pixel
            strCommandText += "exposure %.3f\n" % _xsDataInputDozor.exposureTime.value
            strCommandText += "spot_size %d\n" % _xsDataInputDozor.spotSize.value
            strCommandText += "spot_level 6\n"
            strCommandText += "detector_distance %.3f\n" % _xsDataInputDozor.detectorDistance.value
            strCommandText += "X-ray_wavelength %.3f\n" % _xsDataInputDozor.wavelength.value
            if _xsDataInputDozor.fractionPolarization is None:
                fractionPolarization = self.defaultFractionPolarization
            else:
                fractionPolarization = _xsDataInputDozor.fractionPolarization.value
            strCommandText += "fraction_polarization %.3f\n" % fractionPolarization
            strCommandText += "pixel_min 0\n"
            strCommandText += "pixel_max 64000\n"
            if self.ixMin is not None:
                strCommandText += "ix_min %d\n" % self.ixMin
                strCommandText += "ix_max %d\n" % self.ixMax
                strCommandText += "iy_min %d\n" % self.iyMin
                strCommandText += "iy_max %d\n" % self.iyMax
            if self.strBad_zona is not None:
                strCommandText += "bad_zona %s\n" % self.strBad_zona
            strCommandText += "orgx %.1f\n" % _xsDataInputDozor.orgx.value
            strCommandText += "orgy %.1f\n" % _xsDataInputDozor.orgy.value
            strCommandText += "oscillation_range %.3f\n" % _xsDataInputDozor.oscillationRange.value
            if _xsDataInputDozor.imageStep is None:
                imageStep = self.defaultImageStep
            else:
                imageStep = _xsDataInputDozor.imageStep.value
            strCommandText += "image_step %.3f\n" % imageStep
            if _xsDataInputDozor.startingAngle is None:
                self.startingAngle = self.defaultStartingAngle
            else:
                self.startingAngle = _xsDataInputDozor.startingAngle.value
            strCommandText += "starting_angle %.3f\n" % self.startingAngle
            strCommandText += "first_image_number %d\n" % _xsDataInputDozor.firstImageNumber.value
            strCommandText += "number_images %d\n" % _xsDataInputDozor.numberImages.value
            if _xsDataInputDozor.wedgeNumber is not None:
                strCommandText += "wedge_number %d\n" % _xsDataInputDozor.wedgeNumber.value
            strCommandText += "name_template_image %s\n" % _xsDataInputDozor.nameTemplateImage.value
            strCommandText += "end\n"
        return strCommandText


    def parseOutput(self, _strFileName):
        """
        This method parses the output of dozor
        """
        xsDataResultDozor = XSDataResultDozor()
        strOutput = EDUtilsFile.readFile(_strFileName)
        # Skip the four first lines
        listOutput = strOutput.split("\n")[6:]
        strWorkingDir = os.path.dirname(_strFileName)

        for strLine in listOutput:
            # Remove "|"
            listLine = shlex.split(strLine.replace("|", " "))
            if len(listLine) > 0 and listLine[0].isdigit():
                xsDataImageDozor = XSDataImageDozor()
                imageNumber = int(listLine[0])
                angle = self.startingAngle + (imageNumber - self.firstImageNumber) * (self.oscillationRange - self.overlap) + self.oscillationRange / 2.0
                xsDataImageDozor.number = XSDataInteger(imageNumber)
                xsDataImageDozor.angle = XSDataAngle(angle)

                xsDataImageDozor.spotsNumOf = XSDataInteger(0)
                xsDataImageDozor.spotsIntAver = XSDataDouble(0)
                xsDataImageDozor.spotsResolution = XSDataDouble(0)
                xsDataImageDozor.mainScore = XSDataDouble(0)
                xsDataImageDozor.spotScore = XSDataDouble(0)
                xsDataImageDozor.visibleResolution = XSDataDouble(40)
                try:
                    if listLine[5].startswith("-") or len(listLine) < 11:
                        xsDataImageDozor.spotsNumOf = XSDataInteger(listLine[1])
                        xsDataImageDozor.spotsIntAver = self.parseDouble(listLine[2])
                        xsDataImageDozor.spotsRfactor = self.parseDouble(listLine[3])
                        xsDataImageDozor.spotsResolution = self.parseDouble(listLine[4])
                        xsDataImageDozor.mainScore = self.parseDouble(listLine[8])
                        xsDataImageDozor.spotScore = self.parseDouble(listLine[9])
                        xsDataImageDozor.visibleResolution = self.parseDouble(listLine[10])
                    else:
                        xsDataImageDozor.spotsNumOf = XSDataInteger(listLine[1])
                        xsDataImageDozor.spotsIntAver = self.parseDouble(listLine[2])
                        xsDataImageDozor.spotsRfactor = self.parseDouble(listLine[3])
                        xsDataImageDozor.spotsResolution = self.parseDouble(listLine[4])
                        xsDataImageDozor.powderWilsonScale = self.parseDouble(listLine[5])
                        xsDataImageDozor.powderWilsonBfactor = self.parseDouble(listLine[6])
                        xsDataImageDozor.powderWilsonResolution = self.parseDouble(listLine[7])
                        xsDataImageDozor.powderWilsonCorrelation = self.parseDouble(listLine[8])
                        xsDataImageDozor.powderWilsonRfactor = self.parseDouble(listLine[9])
                        xsDataImageDozor.mainScore = self.parseDouble(listLine[10])
                        xsDataImageDozor.spotScore = self.parseDouble(listLine[11])
                        xsDataImageDozor.visibleResolution = self.parseDouble(listLine[12])
                except:
                    pass
                # Dozor spot file
                if strWorkingDir is not None:
                    strSpotFile = os.path.join(strWorkingDir, "%05d.spot" % xsDataImageDozor.number.value)
                    if os.path.exists(strSpotFile):
                        xsDataImageDozor.spotFile = XSDataFile(XSDataString(strSpotFile))
#                #print xsDataImageDozor.marshal()
                xsDataResultDozor.addImageDozor(xsDataImageDozor)
            elif strLine.startswith("h"):
                xsDataResultDozor.halfDoseTime = XSDataDouble(strLine.split("=")[1].split()[0])

        # Check if mtv plot file exists
        mtvFileName = "dozor_rd.mtv"
        mtvFilePath = os.path.join(strWorkingDir, mtvFileName)
        if os.path.exists(mtvFilePath):
            xsDataResultDozor.plotmtvFile = XSDataFile(XSDataString(mtvFilePath))
            xsDataResultDozor.pngPlots = self.generatePngPlots(mtvFilePath, strWorkingDir)

        return xsDataResultDozor

    def parseDouble(self, _strValue):
        returnValue = None
        try:
            returnValue = XSDataDouble(_strValue)
        except Exception as ex:
            self.warning("Error when trying to parse '" + _strValue + "': %r" % ex)
        return returnValue

    def generatePngPlots(self, _plotmtvFile, _workingDir):
        listXSFile = []
        # Create plot dictionary
        with open(_plotmtvFile) as f:
            listLines = f.readlines()
        dictPlot = None
        plotData = None
        listPlots = []
        index = 0
        while index < len(listLines):
            # print("0" + listLines[index])
            if listLines[index].startswith("$"):
                dictPlot = {}
                dictPlotList = []
                listPlots.append(dictPlot)
                dictPlot["plotList"] = dictPlotList
                index += 1
                dictPlot["name"] = listLines[index].split("'")[1]
                index += 1
                # print(listLines[index])
                while listLines[index].startswith("%"):
                    listLine = listLines[index].split("=")
                    # print(listLine)
                    label = listLine[0][1:].strip()
                    # print("label: " + str([label]))
                    if "'" in listLine[1]:
                        value = listLine[1].split("'")[1]
                    else:
                        value = listLine[1]
                    value = value.replace("\n", "").strip()
                    # print("value: " + str([value]))
                    dictPlot[label] = value
                    index += 1
                    # print(listLines[index])
            elif listLines[index].startswith("#"):
                dictSubPlot = {}
                dictPlotList.append(dictSubPlot)
                plotName = listLines[index].split("#")[1].replace("\n", "").strip()
                dictSubPlot["name"] = plotName
                index += 1
                # print("1" + listLines[index])
                while listLines[index].startswith("%"):
                    listLine = listLines[index].split("=")
                    # print(listLine)
                    label = listLine[0][1:].strip()
                    # print("label: " + str([label]))
                    if "'" in listLine[1]:
                        value = listLine[1].split("'")[1]
                    else:
                        value = listLine[1]
                    value = value.replace("\n", "").strip()
                    # print("value: " + str([value]))
                    dictSubPlot[label] = value
                    index += 1
                    # print(listLines[index])
                dictSubPlot["xValues"] = []
                dictSubPlot["yValues"] = []
            else:
                listData = listLines[index].replace("\n", "").split()
                dictSubPlot["xValues"].append(float(listData[0]))
                dictSubPlot["yValues"].append(float(listData[1]))
                index += 1
        # pprint.pprint(listPlots)
        # Generate the plots
        for mtvplot in listPlots:
            listLegend = []
            xmin = None
            xmax = None
            ymin = None
            ymax = None
            for subPlot in mtvplot["plotList"]:
                xmin1 = min(subPlot["xValues"])
                if xmin is None or xmin > xmin1:
                    xmin = xmin1
                xmax1 = max(subPlot["xValues"])
                if xmax is None or xmax < xmax1:
                    xmax = xmax1
                ymin1 = min(subPlot["yValues"])
                if ymin is None or ymin > ymin1:
                    ymin = ymin1
                ymax1 = max(subPlot["yValues"])
                if ymax is None or ymax < ymax1:
                    ymax = ymax1
            if "xmin" in mtvplot:
                xmin = float(mtvplot["xmin"])
            if "ymin" in mtvplot:
                ymin = float(mtvplot["ymin"])
            plt.xlim(xmin, xmax)
            plt.ylim(ymin, ymax)
            plt.xlabel(mtvplot["xlabel"])
            plt.ylabel(mtvplot["ylabel"])
            plt.title(mtvplot["name"])
            for subPlot in mtvplot["plotList"]:
                if "markercolor" in subPlot:
                    style = "bs-."
                else:
                    style = "r"
                plt.plot(subPlot["xValues"], subPlot["yValues"], style, linewidth=2)
                listLegend.append(subPlot["linelabel"])
            plt.legend(listLegend, loc='lower right')
            plotPath = os.path.join(_workingDir, mtvplot["name"].replace(" ", "").replace(".", "_") + ".png")
            plt.savefig(plotPath, bbox_inches='tight', dpi=75)
            plt.close()
            listXSFile.append(XSDataFile(XSDataString(plotPath)))
        return listXSFile
