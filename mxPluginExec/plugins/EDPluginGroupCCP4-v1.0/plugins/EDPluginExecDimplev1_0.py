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

__author__="Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os, glob

from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile


from XSDataCCP4v1_0 import XSDataInputDimple
from XSDataCCP4v1_0 import XSDataResultDimple

class EDPluginExecDimplev1_0(EDPluginExecProcessScript ):
    """
    This plugin executes the CCP4 program dimple
    """
    

    def __init__(self ):
        EDPluginExecProcessScript.__init__(self )
        self.setXSDataInputClass(XSDataInputDimple)
        self.setDataOutput(XSDataResultDimple())
        self.strDimpleDir = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecDimplev1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput,"Data Input is None")

    
    def preProcess(self, _edObject = None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecDimplev1_0.preProcess")
        xsDataInputDimple = self.getDataInput()
        strMtzFile = xsDataInputDimple.mtz.path.value
        strPdbFile = xsDataInputDimple.pdb.path.value
        self.strDimpleDir = os.path.join(self.getWorkingDirectory(), "dimple")
        self.setScriptCommandline(" " + strMtzFile + " " + strPdbFile + " " + self.strDimpleDir)

    
    def postProcess(self, _edObject = None):
        self.DEBUG("EDPluginExecDimplev1_0.postProcess")
        # Attach log file
        self.dataOutput.log = XSDataFile(XSDataString(os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName())))
        # Check that coot has created the blobs
        for blobName in ["blob1v1.png", "blob1v2.png", "blob1v3.png", "blob2v1.png", "blob2v2.png", "blob2v3.png"]:
            strBlobPath = os.path.join(self.strDimpleDir, blobName)
            if os.path.exists(strBlobPath):
                self.dataOutput.addBlob(XSDataFile(XSDataString(strBlobPath)))
        # Final mtz and pdb
        strFinalMtzPath = os.path.join(self.strDimpleDir, "final.mtz")
        if os.path.exists(strFinalMtzPath):
            self.dataOutput.finalMtz = XSDataFile(XSDataString(strFinalMtzPath))
        strFinalPdbPath = os.path.join(self.strDimpleDir, "final.pdb")
        if os.path.exists(strFinalPdbPath):
            self.dataOutput.finalPdb = XSDataFile(XSDataString(strFinalPdbPath))
        # Findblobs
        for filepath in glob.glob(os.path.join(self.strDimpleDir, "*.log")):
            if filepath.endswith("find-blobs.log"):
                self.dataOutput.findBlobsLog = XSDataFile(XSDataString(filepath))
                break
        # Refmac5restr
        for filepath in glob.glob(os.path.join(self.strDimpleDir, "*.log")):
            if filepath.endswith("refmac5_restr.log"):
                self.dataOutput.refmac5restrLog = XSDataFile(XSDataString(filepath))
                break
        # Results directory
        self.dataOutput.resultsDirectory = XSDataFile(XSDataString(self.strDimpleDir))
                
                
            
                
        