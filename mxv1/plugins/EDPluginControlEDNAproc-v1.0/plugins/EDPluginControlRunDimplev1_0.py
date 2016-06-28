# coding: utf8
#
#    Project: EDNAproc
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

__author__ = "Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os, shutil, time

from EDPluginControl import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDVerbose import EDVerbose
from EDUtilsFile import EDUtilsFile
from EDUtilsPath import EDUtilsPath

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString
from XSDataCommon import XSDataBoolean

from XSDataEDNAprocv1_0  import XSDataInputControlDimple
from XSDataEDNAprocv1_0  import XSDataResultControlDimple

# pdb file retrieval
EDFactoryPluginStatic.loadModule('XSDataISPyBv1_4')
from XSDataISPyBv1_4 import XSDataInputISPyBGetPdbFilePath
from XSDataISPyBv1_4 import XSDataInputStoreAutoProcProgramAttachment
from XSDataISPyBv1_4 import AutoProcProgramAttachment

EDFactoryPluginStatic.loadModule("XSDataCCP4v1_0")
from XSDataCCP4v1_0 import XSDataInputDimple

EDFactoryPluginStatic.loadModule("markupv1_10")
import markupv1_10

EDFactoryPluginStatic.loadModule("XSDataHTML2PDFv1_0")
from XSDataHTML2PDFv1_0 import XSDataInputHTML2PDF


class EDPluginControlRunDimplev1_0(EDPluginControl):
    """
    Checks if there's a PDB file available either in ISPyB or on disk.
    If there's a PDB file:
    - Runs dimple
    - Copies blob png files to pyarch
    - Upload file locations to ISPyB
    """


    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputControlDimple)
        self.dataOutput = XSDataResultControlDimple()
        self.strPdbPath = None
        self.strPathNoanomAimlessMtz = None
        self.strPathToResults = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlRunDimplev1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.mtzFile, "No MTZ file")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlRunDimplev1_0.preProcess")
        self.strPathNoanomAimlessMtz = self.dataInput.mtzFile.path.value
        # Use the directory oof the mtzFile for storing the DIMPLE result files
        self.strPathToResults = os.path.dirname(self.strPathNoanomAimlessMtz)
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


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlRunDimplev1_0.process")
        if self.strPdbPath is None:
            self.screen('No pdb file found, not running dimple')
            return
        # Run dimple
        xsDataResultDimple = self.runDimple(self.strPdbPath, self.strPathNoanomAimlessMtz)
        if xsDataResultDimple is not None:
            # Create HTML page
            listHtmlPath = self.createHtmlPage(self.dataInput.imagePrefix.value,
                                               xsDataResultDimple,
                                               os.path.join(self.getWorkingDirectory(), "html"),
                                               self.dataInput.proposal.value,
                                               self.dataInput.sessionDate.value,
                                               self.dataInput.beamline.value)
            xsDataInputHTML2PDF = XSDataInputHTML2PDF()
            for strHtmlPath in listHtmlPath:
                xsDataInputHTML2PDF.addHtmlFile(XSDataFile(XSDataString(strHtmlPath)))
            xsDataInputHTML2PDF.resultDirectory = xsDataResultDimple.resultsDirectory
            edPluginHTML2PDF = self.loadPlugin("EDPluginHTML2PDFv1_0")
            edPluginHTML2PDF.dataInput = xsDataInputHTML2PDF
            edPluginHTML2PDF.executeSynchronous()
            strPdfFile = edPluginHTML2PDF.dataOutput.pdfFile.path.value
            # Copy result files
            listOfTargetPaths = self.copyResults(self.dataInput.imagePrefix.value,
                                                 self.strPathToResults,
                                                 xsDataResultDimple,
                                                 strPdfFile)
            # Upload files to ISPyB
            if self.dataInput.autoProcProgramId is not None and self.dataInput.pyarchPath is not None:
                strPyarchRootPath = self.dataInput.pyarchPath.path.value
                xsDataInputStoreAutoProcProgramAttachment = XSDataInputStoreAutoProcProgramAttachment()
                for targetPath in listOfTargetPaths:
                    shutil.copy(targetPath, strPyarchRootPath)
                    autoProcProgramAttachment = AutoProcProgramAttachment()
                    autoProcProgramAttachment.fileType = "Result"
                    autoProcProgramAttachment.fileName = os.path.basename(targetPath)
                    autoProcProgramAttachment.filePath = strPyarchRootPath
                    autoProcProgramAttachment.autoProcProgramId = self.dataInput.autoProcProgramId.value
                    xsDataInputStoreAutoProcProgramAttachment.addAutoProcProgramAttachment(autoProcProgramAttachment)
                edPluginStoreAutoProcProgramAttachment = self.loadPlugin("EDPluginISPyBStoreAutoProcProgramAttachmentv1_4")
                edPluginStoreAutoProcProgramAttachment.dataInput = xsDataInputStoreAutoProcProgramAttachment
                edPluginStoreAutoProcProgramAttachment.executeSynchronous()



    def copyResults(self, strImagePrefix, strResultDir, xsDataResultDimple, strPdfFile):
        listOfTargetPaths = []
        # Check that pyarch root exists
        if not os.path.exists(strResultDir):
            self.ERROR("Result directory does not exists! %s" % strResultDir)
        else:
            self.DEBUG("Copying results of dimple to : %s" % strResultDir)
            for xsDataFileBlob in xsDataResultDimple.blob:
                # Copy blob file to pyarch
                strBlobName = os.path.basename(xsDataFileBlob.path.value).split(".")[0]
                strTargetFileName = "ep_%s_%s_dimple.png" % (strImagePrefix, strBlobName)
                strTargetPath = os.path.join(strResultDir, strTargetFileName)
                shutil.copyfile(xsDataFileBlob.path.value, strTargetPath)
                listOfTargetPaths.append(strTargetPath)
            # Log file
            strTargetLogPath = os.path.join(strResultDir, "ep_%s_dimple.log" % strImagePrefix)
            shutil.copyfile(xsDataResultDimple.log.path.value, strTargetLogPath)
            listOfTargetPaths.append(strTargetLogPath)
            # Final MTZ file
            strTargetFinalMtzPath = os.path.join(strResultDir, "ep_%s_dimple.mtz" % strImagePrefix)
            shutil.copyfile(xsDataResultDimple.finalMtz.path.value, strTargetFinalMtzPath)
            listOfTargetPaths.append(strTargetFinalMtzPath)
            # Final PDB file
            strTargetFinalPdbPath = os.path.join(strResultDir, "ep_%s_dimple.pdb" % strImagePrefix)
            shutil.copyfile(xsDataResultDimple.finalPdb.path.value, strTargetFinalPdbPath)
            listOfTargetPaths.append(strTargetFinalPdbPath)
            # Findblobs log file
            strTargetFindBlobsLogPath = os.path.join(strResultDir, "ep_%s_findblobs_dimple.log" % strImagePrefix)
            shutil.copyfile(xsDataResultDimple.findBlobsLog.path.value, strTargetFindBlobsLogPath)
            listOfTargetPaths.append(strTargetFindBlobsLogPath)
            # Refmac5_restr log file
            strTargetRefmac5restrLogPath = os.path.join(strResultDir, "ep_%s_refmac5restr_dimple.log" % strImagePrefix)
            shutil.copyfile(xsDataResultDimple.refmac5restrLog.path.value, strTargetRefmac5restrLogPath)
            listOfTargetPaths.append(strTargetRefmac5restrLogPath)
            # Result PDF file
            strTargetPdfPath = os.path.join(strResultDir, "ep_%s_results_dimple.pdf" % strImagePrefix)
            shutil.copyfile(strPdfFile, strTargetPdfPath)
            listOfTargetPaths.append(strTargetPdfPath)
        return listOfTargetPaths


    def createHtmlPage(self, strImagePrefix, xsDataResultDimple, strHtmlPath, strProposal, strSessionDate, strBeamline):
        """Create an HTML page with the results"""
        if not os.path.exists(strHtmlPath):
            os.makedirs(strHtmlPath, 0755)
        strSample = "_".join(strImagePrefix.split("_")[0:-1])
        strHtmlFileName = "ep_%s_index.html" % strImagePrefix
        strPath = os.path.join(strHtmlPath, strHtmlFileName)
        strResultsDirectory = xsDataResultDimple.resultsDirectory.path.value
        page = markupv1_10.page(mode='loose_html')
        # Title and footer
        page.init(title="Dimple Results",
                   footer="Generated on %s" % time.asctime())
        page.div(align_="LEFT")
        page.h1()
        page.strong("Dimple Results for sample {0} from proposal {1}".format(strSample, strProposal))
        page.h1.close()
        page.h3("Session date: {0}-{1}-{2}".format(strSessionDate[0:4], strSessionDate[4:6], strSessionDate[6:]))
        page.h3("Beamline: {0}".format(strBeamline))
        page.h3("Dimple output files can be found in :")
        page.strong(strResultsDirectory)
        page.div.close()
        # Results of REFMAC 5
        page.h3("Final results of Recmac 5:")
        page.pre(self.extractFinalResultsFromRefmac5RestrLog(xsDataResultDimple.refmac5restrLog.path.value))
        # Results of findblobs
        page.h3("Findblobs log:")
        page.pre(open(xsDataResultDimple.findBlobsLog.path.value).read())
        # Blobs
        page.br()
        listImageHTML = []
        for xsDataFileBlob in xsDataResultDimple.blob:
            # Copy blob file to html directory
            strBlobName = os.path.basename(xsDataFileBlob.path.value).split(".")[0]
            strBlobImage = "ep_%s_%s_dimple.png" % (strImagePrefix, strBlobName)
            strTargetPath = os.path.join(strHtmlPath, strBlobImage)
            shutil.copyfile(xsDataFileBlob.path.value, strTargetPath)
            strPageBlobPath = os.path.join(strHtmlPath, "ep_%s_%s_dimple.html" % (strImagePrefix, strBlobName))
            pageBlob = markupv1_10.page()
            pageBlob.init(title=strBlobName,
                           footer="Generated on %s" % time.asctime())
            pageBlob.h1(strBlobName)
            pageBlob.div(align_="LEFT")
            pageBlob.img(src=strBlobImage, title=strBlobName)
            pageBlob.div.close()
            pageBlob.br()
            pageBlob.div(align_="LEFT")
            pageBlob.a("Back to previous page", href_=os.path.basename(strPath))
            pageBlob.div.close()
            EDUtilsFile.writeFile(strPageBlobPath, str(pageBlob))
            listImageHTML.append(strPageBlobPath)
            page.a(href=os.path.basename(strPageBlobPath))
            page.img(src=strBlobImage, width=200, height=200, title=strBlobName)
            page.a.close()
            if strBlobName == "blob1v3":
                page.br()
        page.br()
        # FInalise html page
        strHTML = str(page)
        EDUtilsFile.writeFile(strPath, strHTML)
        listHTML = [strPath] + listImageHTML
        return listHTML




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

    def postProcess(self, _edObject=None):
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
        for strLine in listLines[iIndex + 1:iIndex + 7]:
            strFinalResults += strLine
        return strFinalResults

