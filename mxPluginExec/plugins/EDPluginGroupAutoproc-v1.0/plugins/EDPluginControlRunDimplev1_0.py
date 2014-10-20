# coding: utf8
#
#    Project: Autoproc
#             http://www.edna-site.org
#
#    Copyright (C) ESRF
#
#    Principal author: Olof Svensson
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

import os, shutil

from EDPluginControl import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDVerbose import EDVerbose

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString
from XSDataCommon import XSDataBoolean

from XSDataAutoprocv1_0  import XSDataInputControlDimple
from XSDataAutoprocv1_0  import XSDataResultControlDimple

# pdb file retrieval
EDFactoryPluginStatic.loadModule('XSDataISPyBv1_4')
from XSDataISPyBv1_4 import XSDataInputISPyBGetPdbFilePath

EDFactoryPluginStatic.loadModule("XSDataCCP4v1_0")
from XSDataCCP4v1_0 import XSDataInputDimple


class EDPluginControlRunDimplev1_0( EDPluginControl ):
    """
    Checks if there's a PDB file available either in ISPyB or on disk.
    If there's a PDB file:
    - Runs dimple
    - Copies blob png files to pyarch
    - Upload file locations to ISPyB
    """


    def __init__( self ):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputControlDimple)
        self.dataOutput = XSDataResultControlDimple()
        self.strPdbPath = None
        self.strPathNoanomAimlessMtz = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlRunDimplev1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.mtzFile, "No MTZ file")


    def preProcess(self, _edObject = None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlRunDimplev1_0.preProcess")
        self.strPathNoanomAimlessMtz = self.dataInput.mtzFile.path.value
        # we need a PDB file either in ispyb or in the image directory
        edPluginGetPdbFile = self.loadPlugin("EDPluginISPyBGetPdbFilePathv1_4")
        xsDataInputGetPdbFilePath = XSDataInputISPyBGetPdbFilePath()
        xsDataInputGetPdbFilePath.dataCollectionId = self.dataInput.dataCollectionId
        edPluginGetPdbFile.dataInput = xsDataInputGetPdbFilePath
        edPluginGetPdbFile.executeSynchronous()
        xsDataFilePdb = edPluginGetPdbFile.dataOutput.pdbFilePath
        if xsDataFilePdb is None:
            xsDataFilePdbDirectory = self.dataInput.pdbDirectory
            if xsDataFilePdbDirectory is None:
                self.screen('No pdb file in ispyb')
            else:
                strPdbDirectory = xsDataFilePdbDirectory.path.value
                self.screen('No pdb file in ispyb, trying the directory {0}'.format(strPdbDirectory))
                for f in os.listdir(strPdbDirectory):
                    if f.endswith('.pdb'):
                        self.strPdbPath = os.path.join(strPdbDirectory, f)
                        break
        else:
            self.strPdbPath = xsDataFilePdb.value


    def process(self, _edObject = None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlRunDimplev1_0.process")
        if self.strPdbPath is None:
            self.screen('No pdb file found, not running dimple')
            return
        # Run dimple
        xsDataResultControlDimple = self.runDimple(self.strPdbPath, self.strPathNoanomAimlessMtz)
        if xsDataResultControlDimple is not None:
            # Copy result files to pyarch
            if self.dataInput.pyarchPath is not None:
                self.copyResultsToPyarch(self.dataInput.imagePrefix.value,
                                         self.dataInput.pyarchPath.path.value, 
                                         xsDataResultDimple)

            
    def copyResultsToPyarch(self, strImagePrefix, strPyarchRootPath, xsDataResultDimple):
        listOfTargetPaths = []
        # Check that pyarch root exists
        if not os.path.exists(strPyarchRootPath):
            self.ERROR("Pyarch root directory does not exists! %s" % strPyarchRootPath)
        else:
            # Create "dimple" sub directory
            strDimplePath = os.path.join(strPyarchRootPath, "dimple")
            os.makedirs(strDimplePath, 0755)
            for xsDataFileBlob in xsDataResultDimple.blob:
                # Copy blob file to pyarch
                strBlobName = os.path.basename(xsDataFileBlob.path.value).split(".")[0]
                strTargetFileName = "%s_%s_dimple.png" % (strImagePrefix, strBlobName)
                strTargetPath = os.path.join(strDimplePath, strTargetFileName)
                shutil.copyfile(xsDataFileBlob.path.value, strTargetPath)
                listOfTargetPaths.append(strTargetPath)
            # Log file
            strTargetLogPath = os.path.join(strDimplePath, "%s_dimple.log" % strImagePrefix)
            shutil.copyfile(xsDataResultDimple.log.path.value, strTargetLogPath)
            listOfTargetPaths.append(strTargetLogPath)
            # Final MTZ file
            strTargetFinalMtzPath = os.path.join(strDimplePath, "%s_dimple.mtz" % strImagePrefix)
            shutil.copyfile(xsDataResultDimple.finalMtz.path.value, strTargetFinalMtzPath)
            listOfTargetPaths.append(strTargetFinalMtzPath)
            # Final PDB file
            strTargetFinalPdbPath = os.path.join(strDimplePath, "%s_dimple.pdb" % strImagePrefix)
            shutil.copyfile(xsDataResultDimple.finalPdb.path.value, strTargetFinalPdbPath)
            listOfTargetPaths.append(strTargetFinalPdbPath)
            # Findblobs log file
            strTargetFindBlobsLogPath = os.path.join(strDimplePath, "%s_findblobs_dimple.log" % strImagePrefix)
            shutil.copyfile(xsDataResultDimple.findBlobsLog.path.value, strTargetFindBlobsLogPath)
            listOfTargetPaths.append(strTargetFindBlobsLogPath)
        return listOfTargetPaths
            
            
    def runDimple(self, strPdbPath, strPathNoanomAimlessMtz):
        self.screen('Running dimple with pdb file {0}'.format(strPdbPath))
        xsDataResultControlDimple = None
        edPluginDimple = self.loadPlugin("EDPluginExecDimplev1_0")
        xsDataInputDimple = XSDataInputDimple()
        strPathNoanomAimlessMtz = self.dataInput.mtzFile.path.value
        if not os.path.exists(strPathNoanomAimlessMtz):
            strErrorMessage = "Cannot find expected result mtz file {0}, execution of dimple abandoned".format(strPathNoanomAimlessMtz)
            self.ERROR(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
        elif not os.path.exists(strPdbPath):
            strErrorMessage = "Cannot find expected pdb file {0}, execution of dimple abandoned".format(strPdbPath)
            self.ERROR(strErrorMessage)
            if os.path.exists("/data/pyapdb"):
                self.addErrorMessage(strErrorMessage)
        else:
            xsDataInputDimple.mtz = XSDataFile(XSDataString(strPathNoanomAimlessMtz))
            xsDataInputDimple.pdb = XSDataFile(XSDataString(strPdbPath))
            edPluginDimple.dataInput = xsDataInputDimple
            edPluginDimple.executeSynchronous()
            if not edPluginDimple.isFailure():
                self.dataOutput.dimpleExecutedSuccessfully = XSDataBoolean(True)
                xsDataResultControlDimple = edPluginDimple.dataOutput
        return xsDataResultControlDimple

    def postProcess(self, _edObject = None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlRunDimplev1_0.postProcess")
