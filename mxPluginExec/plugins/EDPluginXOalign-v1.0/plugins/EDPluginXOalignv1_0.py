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
        self.fMaxKappaAngle = 200
        self.fMinKappaAngle = -200
        self.fOmega = 0.0
        self.fKappa = 0.0
        self.fPhi = 0.0

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginXOalignv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.symmetry, "Symmetry is None")
        self.checkMandatoryParameters(self.dataInput.cell, "Cell is None")
        self.checkMandatoryParameters(self.dataInput.orientation, "Orientation is None")

    def configure(self):
        EDPluginExecProcessScript.configure(self)
        self.DEBUG("EDPluginXOalignv1_0.configure")
        self.strOmegaRot = self.config.get("OmegaRot")
        self.strKappaRot = self.config.get("KappaRot")
        self.strPhiRot   = self.config.get("PhiRot")
        self.strName     = self.config.get("Name")
        self.fMaxKappaAngle = self.config.get("maxKappaAngle", self.fMaxKappaAngle)
        self.fMinKappaAngle = self.config.get("minKappaAngle", self.fMinKappaAngle)

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginXOalignv1_0.preProcess")
        xsDataInputXOalign = self.dataInput
        if xsDataInputXOalign.omega is not None:
            self.fOmega = xsDataInputXOalign.omega.value
        if xsDataInputXOalign.kappa is not None:
            self.fKappa = xsDataInputXOalign.kappa.value
        if xsDataInputXOalign.phi is not None:
            self.fPhi = xsDataInputXOalign.phi.value
        # Create the MOSFLM mat file
        strMosflmMatFilePath = os.path.join(self.getWorkingDirectory(), "mosflm.mat")
        self.writeDataMOSFLMNewmat(self.dataInput.orientation, 
                                   self.dataInput.cell, 
                                   strMosflmMatFilePath)
        # Construct the command line
        self.setScriptCommandline(self.generateCommands(self.dataInput.symmetry.value, strMosflmMatFilePath))
        
        
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

    def generateCommands(self, _strSymmetry, _strMosflmMatFilePath):
        """
        This method creates a list of commands for mtz2various
        """
        self.DEBUG("EDPluginXOalignv1_0.generateCommands")
        strScriptCommandLine = ""
            
        strScriptCommandLine += "-O {0} -K {1} -P {2}".format(self.strOmegaRot,
                                                             self.strKappaRot,
                                                             self.strPhiRot)
        
        strScriptCommandLine += " -D {0},{1},{2}".format(self.fOmega, self.fKappa, self.fPhi)
        
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
                        if fKappa >= self.fMinKappaAngle and fKappa <= self.fMaxKappaAngle: 
                            xsDataXOalignSolution.kappa = XSDataDouble(fKappa)
                            fPhi = float(listSettings[2])
                            # Offset phi with omega value
                            fNewPhi = (fPhi-self.fOmega) % 360
                            xsDataXOalignSolution.phi = XSDataDouble(fNewPhi)
                            strSettings = "".join(listSettings[3:])
                            xsDataXOalignSolution.settings = XSDataString(strSettings)
                            xsDataResultXOalign.addSolution(xsDataXOalignSolution)
                        iIndex += 1
                iIndex += 1
                if iIndex >= len(listLog):
                    bContinue = False
        return xsDataResultXOalign
    
    def writeDataMOSFLMNewmat(self, _orientation, _cell, _strMatFileName):
        self.DEBUG("EDPluginXOalignv1_0.writeDataMOSFLMNewmat")
        matrixA = _orientation.matrixA
        strNewmat =  " %11.8f %11.8f %11.8f\n" % (matrixA.m11, matrixA.m12, matrixA.m13)
        strNewmat += " %11.8f %11.8f %11.8f\n" % (matrixA.m21, matrixA.m22, matrixA.m23)
        strNewmat += " %11.8f %11.8f %11.8f\n" % (matrixA.m31, matrixA.m32, matrixA.m33)
        strNewmat += " %11.3f %11.3f %11.3f\n" % (0.0, 0.0, 0.0)
        matrixU = _orientation.matrixU
        strNewmat += " %11.7f %11.7f %11.7f\n" % (matrixU.m11, matrixU.m12, matrixU.m13)
        strNewmat += " %11.7f %11.7f %11.7f\n" % (matrixU.m21, matrixU.m22, matrixU.m23)
        strNewmat += " %11.7f %11.7f %11.7f\n" % (matrixU.m31, matrixU.m32, matrixU.m33)

        strNewmat += " %11.4f %11.4f %11.4f" % (_cell.length_a.value, 
                                                _cell.length_b.value, 
                                                _cell.length_c.value)
        strNewmat += " %11.4f %11.4f %11.4f\n" % (_cell.angle_alpha.value,
                                                  _cell.angle_beta.value,
                                                  _cell.angle_gamma.value)
        strNewmat += " %11.3f %11.3f %11.3f\n" % (0.0, 0.0, 0.0)

        self.writeProcessFile(_strMatFileName, strNewmat)
    