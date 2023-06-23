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

__authors__ = ["Olof Svensson"]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20171016"
__status__ = "beta"

import os
import time

from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDUtilsTable              import EDUtilsTable
from EDUtilsFile import EDUtilsFile

from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

from XSDataDnaTables import dna_tables

from XSDataFbestv1_0 import XSDataInputFbest
from XSDataFbestv1_0 import XSDataResultFbest

class EDPluginFbestv1_0(EDPluginExecProcessScript):
    """
    This plugin runs the Fbest program written by Sasha Popov:

    This is the help for Fbest - fbest --help:
    linsvensson:~ % fbest --help

    Program fbest /A.Popov /
     Fast estimation exposure time accounting radiation damage
    Version 1.0.0 //  01.07.2017
    
    SYNOPSIS
    fbest  -f {flux} -res {resolution} [OPTIONS]
    
    OPTIONS
    --help gives help message
     -------all sizes in microns, dose in MGy---
    -bh {beamH}      default=45
    -bv {beamV}      default=35
    -w {wavelength}  default=1.0
    -a {aperture}    default not
    -sx {slitX} -sy {slitY} 
    -rot {totation_range}  default=180.0 
    -rst {rot_width}       default=0.1
    -tlim {t_exp min}      default=0.037 s 
    -Dmax {dose_limit}     default=30
    -dose {dose_rate}      default - calculate using flux
    -sen {sensitivity}     default=1 (cryo), roomT = 20 - 100
    -cs  {crystal size}    default=beam_size    
    """


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputFbest)
        self.setDataOutput(XSDataResultFbest())


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginFbestv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginFbestv1_0.preProcess")
        self.setScriptLogFileName("fbest.log")
        xsDataInputFbest = self.getDataInput()
        self.setScriptCommandline(self.generateCommands(xsDataInputFbest))



    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginFbestv1_0.postProcess")
        self.dataOutput = self.parseOutput(os.path.join(self.getWorkingDirectory(),
                                                        self.getScriptLogFileName()))


    def generateCommands(self, _xsDataInputFbest):
        """
        This method creates a list of commands for fbest
        """
        self.DEBUG("EDPluginFbestv1_0.generateCommands")

        strScriptCommandLine = " -f {0:.3g}".format(_xsDataInputFbest.flux.value)

        strScriptCommandLine += " -res {0:.2f}".format(_xsDataInputFbest.resolution.value)

        if _xsDataInputFbest.beamH is not None:
            strScriptCommandLine += " -bh {0:.3f}".format(_xsDataInputFbest.beamH.value)

        if _xsDataInputFbest.beamV is not None:
            strScriptCommandLine += " -bv {0:.3f}".format(_xsDataInputFbest.beamV.value)

        if _xsDataInputFbest.wavelength is not None:
            strScriptCommandLine += " -w {0:.3f}".format(_xsDataInputFbest.wavelength.value)

        if _xsDataInputFbest.aperture is not None:
            strScriptCommandLine += " -a {0:.3f}".format(_xsDataInputFbest.aperture.value)

        if _xsDataInputFbest.slitX is not None:
            strScriptCommandLine += " -sx {0:.3f}".format(_xsDataInputFbest.slitX.value)

        if _xsDataInputFbest.slitY is not None:
            strScriptCommandLine += " -sy {0:.3f}".format(_xsDataInputFbest.slitY.value)

        if _xsDataInputFbest.rotationRange is not None:
            strScriptCommandLine += " -rot {0:.3f}".format(_xsDataInputFbest.rotationRange.value)

        if _xsDataInputFbest.rotationWidth is not None:
            strScriptCommandLine += " -rst {0:.3f}".format(_xsDataInputFbest.rotationWidth.value)

        if _xsDataInputFbest.minExposureTime is not None:
            strScriptCommandLine += " -tlim {0:.3f}".format(_xsDataInputFbest.minExposureTime.value)

        if _xsDataInputFbest.doseLimit is not None:
            strScriptCommandLine += " -Dmax {0:.1f}".format(_xsDataInputFbest.doseLimit.value)

        if _xsDataInputFbest.doseRate is not None:
            strScriptCommandLine += " -dose {0:.1f}".format(_xsDataInputFbest.doseRate.value)

        if _xsDataInputFbest.sensitivity is not None:
            strScriptCommandLine += " -sen {0:.1f}".format(_xsDataInputFbest.sensitivity.value)

        if _xsDataInputFbest.crystalSize is not None:
            strScriptCommandLine += " -cs {0:.3f}".format(_xsDataInputFbest.crystalSize.value)

        return strScriptCommandLine


    def parseOutput(self, _strFileName):
        """
        This method parses the output of dozor
        """
        xsDataResultFbest = XSDataResultFbest()
        strOutput = EDUtilsFile.readFile(_strFileName)
        listOutput = strOutput.split("\n")
        xsDataResultFbest.fbestLogFile = XSDataFile(XSDataString(_strFileName))
        for strLine in listOutput:
            listLine = strLine.split("=")
            if len(listLine) == 2:
                label = listLine[0].strip()
                value = listLine[1].strip()
                try:
                    if label == "Exposure time per image":
                        xsDataResultFbest.exposureTimePerImage = XSDataDouble(value)
                    elif label == "Transmission":
                        xsDataResultFbest.transmission = XSDataDouble(value)
                    elif label == "Number of images":
                        xsDataResultFbest.numberOfImages = XSDataDouble(value)
                    elif label == "Rotation width":
                        xsDataResultFbest.rotationWidth = XSDataDouble(value)
                    elif label == "Resolition":
                        xsDataResultFbest.resolution = XSDataDouble(value)
                    elif label == "Total dose, MGy":
                        xsDataResultFbest.totalDose = XSDataDouble(value)
                    elif label == "Total exposure time":
                        xsDataResultFbest.totalExposureTime = XSDataDouble(value)
                    elif label == "Dose Rate MGy/s":
                        xsDataResultFbest.doseRate = XSDataDouble(value)
                    elif label == "Sensitivity":
                        xsDataResultFbest.sensitivity = XSDataDouble(value)
                    elif label == "Min.Exposure":
                        xsDataResultFbest.minExposure = XSDataDouble(value)
                except:
                    self.warning("FBest: Cannot parse value for {0} - vale is {1}".format(label, value))

        return xsDataResultFbest


