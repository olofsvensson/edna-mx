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

import os, shutil, time

from EDPluginControl import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDVerbose import EDVerbose
from EDUtilsFile import EDUtilsFile

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

EDFactoryPluginStatic.loadModule("markupv1_7")
import markupv1_7


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
                listOfTargetPaths = self.copyResultsToPyarch(self.dataInput.imagePrefix.value,
                                                             self.dataInput.pyarchPath.path.value, 
                                                             xsDataResultControlDimple)
                htmlPath = self.createHtmlPage(self.dataInput.imagePrefix.value,
                                               self.dataInput.pyarchPath.path.value)
                listOfTargetPaths.append(htmlPath)

            
    def copyResultsToPyarch(self, strImagePrefix, strPyarchRootPath, xsDataResultDimple):
        listOfTargetPaths = []
        # Check that pyarch root exists
        if not os.path.exists(strPyarchRootPath):
            self.ERROR("Pyarch root directory does not exists! %s" % strPyarchRootPath)
        else:
            self.DEBUG("Copying results of dimple to : %s" % strPyarchRootPath)
            for xsDataFileBlob in xsDataResultDimple.blob:
                # Copy blob file to pyarch
                strBlobName = os.path.basename(xsDataFileBlob.path.value).split(".")[0]
                strTargetFileName = "%s_%s_dimple.png" % (strImagePrefix, strBlobName)
                strTargetPath = os.path.join(strPyarchRootPath, strTargetFileName)
                shutil.copyfile(xsDataFileBlob.path.value, strTargetPath)
                listOfTargetPaths.append(strTargetPath)
            # Log file
            strTargetLogPath = os.path.join(strPyarchRootPath, "%s_dimple.log" % strImagePrefix)
            shutil.copyfile(xsDataResultDimple.log.path.value, strTargetLogPath)
            listOfTargetPaths.append(strTargetLogPath)
            # Final MTZ file
            strTargetFinalMtzPath = os.path.join(strPyarchRootPath, "%s_dimple.mtz" % strImagePrefix)
            shutil.copyfile(xsDataResultDimple.finalMtz.path.value, strTargetFinalMtzPath)
            listOfTargetPaths.append(strTargetFinalMtzPath)
            # Final PDB file
            strTargetFinalPdbPath = os.path.join(strPyarchRootPath, "%s_dimple.pdb" % strImagePrefix)
            shutil.copyfile(xsDataResultDimple.finalPdb.path.value, strTargetFinalPdbPath)
            listOfTargetPaths.append(strTargetFinalPdbPath)
            # Findblobs log file
            strTargetFindBlobsLogPath = os.path.join(strPyarchRootPath, "%s_findblobs_dimple.log" % strImagePrefix)
            shutil.copyfile(xsDataResultDimple.findBlobsLog.path.value, strTargetFindBlobsLogPath)
            listOfTargetPaths.append(strTargetFindBlobsLogPath)
            # Refmac5_restr log file
            strTargetRefmac5restrLogPath = os.path.join(strPyarchRootPath, "%s_refmac5restr_dimple.log" % strImagePrefix)
            shutil.copyfile(xsDataResultDimple.refmac5restrLog.path.value, strTargetRefmac5restrLogPath)
            listOfTargetPaths.append(strTargetRefmac5restrLogPath)
        return listOfTargetPaths
            
    
    def createHtmlPage(self, strImagePrefix, strPyarchRootPath):
        """Create an HTML page with the results"""
        strHtmlFileName = "%s_index.html" % strImagePrefix
        strPath = os.path.join(strPyarchRootPath, strHtmlFileName)
        page = markupv1_7.page(mode='loose_html')
        # Title and footer
        page.init( title="Dimple Results", 
                   footer="Generated on %s" % time.asctime())
        page.div( align_="LEFT")
        page.h1()
        page.strong( "Dimple Results" )
        page.h1.close()
        page.div.close()
        # Results of REFMAC 5
        page.h3("Final results of Recmac 5:")
        strRefmac5LogPath = os.path.join(strPyarchRootPath, "%s_refmac5restr_dimple.log" % strImagePrefix)
        page.pre(self.extractFinalResultsFromRefmac5RestrLog(strRefmac5LogPath))
        # Results of findblobs
        page.h3("Findblobs log:")
        strFindblobsLogPath = os.path.join(strPyarchRootPath, "%s_findblobs_dimple.log" % strImagePrefix)
        page.pre(open(strFindblobsLogPath).read())
        # Blobs
        page.br()
        for blobName in ["blob1v1", "blob1v2", "blob1v3", "blob2v1", "blob2v2", "blob2v3"]:
            strPageBlobPath = os.path.join(strPyarchRootPath, "%s_%s_dimple.html" % (strImagePrefix, blobName))
            pageBlob = markupv1_7.page()
            pageBlob.init( title=blobName, 
                           footer="Generated on %s" % time.asctime())
            pageBlob.h1(blobName)
            pageBlob.div( align_="LEFT")
            strBlobImage = "%s_%s_dimple.png" % (strImagePrefix, blobName) 
            pageBlob.img(src=strBlobImage, title=blobName)
            pageBlob.div.close()
            pageBlob.br()
            pageBlob.div( align_="LEFT")
            pageBlob.a("Back to previous page", href_=strPath)
            pageBlob.div.close()
            EDUtilsFile.writeFile(strPageBlobPath, str(pageBlob))
            page.a( href=strPageBlobPath)
            page.img( src=strBlobImage, width=300, height=300, title=blobName )
            page.a.close()
            if blobName == "blob1v3":
                page.br()
        page.br()
        # FInalise html page
        strHTML = str(page)
        EDUtilsFile.writeFile(strPath, strHTML)
        return strPath
        
        
        
            
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


    def extractFinalResultsFromRefmac5RestrLog(self, logFilePath):
        fileObject = open(logFilePath)
        listLines = fileObject.readlines()
        fileObject.close()
        iIndex = 0
        for strLine in listLines:
            if "Final results" in strLine:
                break
            else:
                iIndex += 1
        strFinalResults = ""
        for strLine in listLines[iIndex+1:iIndex+7]:
            strFinalResults += strLine
        return strFinalResults
        
