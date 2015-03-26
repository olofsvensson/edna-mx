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
import sys
import time

from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsFile import EDUtilsFile

from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

from XSDataXOalignv1_0 import XSDataXOalignSolution
from XSDataXOalignv1_0 import XSDataInputXOalign
from XSDataXOalignv1_0 import XSDataResultXOalign

class EDPluginXOalignv1_0(EDPluginExecProcessScript):
    """
    This plugin runs the XOalign program written by Pierre Legrand
    """
    

    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputXOalign)
        self.setDataOutput(XSDataResultXOalign())
        self.xoalignPythonpath = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginXOalignv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.getMosflmMat(), "Mosflm mat file path is None")

    def configure(self):
        EDPluginExecProcessScript.configure(self)
        self.DEBUG("EDPluginXOalignv1_0.configure")
        self.strOmegaRot = self.config.get("OmegaRot")
        self.strKappaRot = self.config.get("KappaRot")
        self.strPhiRot   = self.config.get("PhiRot")
        self.strName     = self.config.get("Name")

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginXOalignv1_0.preProcess")
        xsDataInputXOalign = self.dataInput
        # Read the MOSFLM mat file
        strMosflmMat = EDUtilsFile.readFile(xsDataInputXOalign.mosflmMat.path.value)
        # Split the file at the "SYMM" keyword
        strMat, strSymm = strMosflmMat.split("SYMM")
        # Write the mat file without the symm to the working directory
        strMosflmMatFilePath = os.path.join(self.getWorkingDirectory(), "mosflm.mat")
        EDUtilsFile.writeFile(strMosflmMatFilePath, strMat)
        # Construct the command line
        self.setScriptCommandline(self.generateCommands(xsDataInputXOalign, strSymm.strip(), strMosflmMatFilePath))
        
        
    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginXOalignv1_0.postProcess")
        strPathLogFile = os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName())
        if os.path.exists(strPathLogFile):
            xsDataResultXOalign = self.parseLogFile(strPathLogFile)
            xsDataResultXOalign.logFile = XSDataFile(XSDataString(strPathLogFile))
            self.dataOutput = xsDataResultXOalign
    
            
    def finallyProcess(self, _edObject=None):
        EDPluginExecProcessScript.finallyProcess(self)
        self.DEBUG("EDPluginXOalignv1_0.finallyProcess")

    def generateCommands(self, _xsDataInputRdfit, _strSymmetry, _strMosflmMatFilePath):
        """
        This method creates a list of commands for mtz2various
        """
        self.DEBUG("EDPluginExecMtz2Variousv1_0.generateCommands")
        strScriptCommandLine = ""
        if _xsDataInputRdfit is not None:
            
            strScriptCommandLine += "-O {0} -K {1} -P {2}".format(self.strOmegaRot,
                                                                 self.strKappaRot,
                                                                 self.strPhiRot)
            
            strScriptCommandLine += " -D 0.0,0.0,0.0"
            
            strScriptCommandLine += " -s {0}".format(_strSymmetry)
            
            strScriptCommandLine += " -g \"{0}\"".format(self.strName)

            strScriptCommandLine += " {0}".format(_strMosflmMatFilePath)
            
        return strScriptCommandLine
    
    def parseLogFile(self, _strLogFilePath):
        xsDataResultXOalign = XSDataResultXOalign()
        if os.path.exists(_strLogFilePath):
            strLogText = EDUtilsFile.readFile(_strLogFilePath)
            listLog = strLogText.split("\n")
            iIndex = 0
            bContinue = True
            while bContinue:
                if "Independent Solutions" in listLog[iIndex]:
                    iIndex += 3
                    while listLog[iIndex] != "" and iIndex < len(listLog):
                        xsDataXOalignSolution = XSDataXOalignSolution()
                        # Remove multiple white spaces
                        strTmp = " ".join(listLog[iIndex].split())
                        # Split the string at white spaces
                        listSettings = strTmp.split(" ")
                        fKappa = float(listSettings[1])
                        xsDataXOalignSolution.kappa = XSDataDouble(fKappa)
                        fPhi = float(listSettings[2])
                        xsDataXOalignSolution.phi = XSDataDouble(fPhi)
                        strSettings = "".join(listSettings[3:])
                        xsDataXOalignSolution.settings = XSDataString(strSettings)
                        xsDataResultXOalign.addSolution(xsDataXOalignSolution)
                        iIndex += 1
                iIndex += 1
                if iIndex >= len(listLog):
                    bContinue = False
        return xsDataResultXOalign
        