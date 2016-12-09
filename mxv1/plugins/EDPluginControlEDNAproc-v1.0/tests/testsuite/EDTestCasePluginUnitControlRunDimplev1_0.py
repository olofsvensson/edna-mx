# coding: utf8
#
#    Project: EDNA dp
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

import os, tempfile, shutil

from EDTestCasePluginUnit import EDTestCasePluginUnit
from EDAssert import EDAssert
from EDFactoryPluginStatic import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("XSDataCCP4v1_0")
from XSDataCCP4v1_0 import XSDataResultDimple

class EDTestCasePluginUnitControlRunDimplev1_0(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA control plugin EDNAprocv1_0
    """

    def __init__(self, _strTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlRunDimplev1_0")
        self.strDataPath = self.getPluginTestsDataHome()

    def preProcess(self, _edObject=None):
        EDTestCasePluginUnit.preProcess(self)
        self.loadTestImage(["final.mtz", "final.pdb", "blob1v1.png", "blob1v2.png", "blob1v3.png",
                            "blob2v1.png", "blob2v2.png", "blob2v3.png"])

    def test_copyResults(self):
        strDimpleOutput = os.path.join(self.strDataPath, "dimple", "Dimplev1_0_dataOutput.xml")
        strResultDimple = self.readAndParseFile(strDimpleOutput)
        xsDataResultDimple = XSDataResultDimple.parseString(strResultDimple)
        edPlugin = self.getPlugin()
        strResultDir = tempfile.mkdtemp(prefix="EDTestCasePluginUnitControlRunDimplev1_0_")
        strPrefix = "xtal5w1_1"
        strPdfPath = os.path.join(xsDataResultDimple.resultsDirectory.path.value, "DIMPLE.pdf")
        listPath = edPlugin.copyResults(strPrefix, strResultDir, xsDataResultDimple, strPdfPath)
        EDAssert.equal(True, os.path.exists(os.path.join(strResultDir, "ep_xtal5w1_1_blob1v1_dimple.png")), "blob1v1.png")
        EDAssert.equal(True, os.path.exists(os.path.join(strResultDir, "ep_xtal5w1_1_blob1v2_dimple.png")), "blob1v2.png")
        EDAssert.equal(True, os.path.exists(os.path.join(strResultDir, "ep_xtal5w1_1_blob1v3_dimple.png")), "blob1v3.png")
        EDAssert.equal(True, os.path.exists(os.path.join(strResultDir, "ep_xtal5w1_1_blob2v1_dimple.png")), "blob2v1.png")
        EDAssert.equal(True, os.path.exists(os.path.join(strResultDir, "ep_xtal5w1_1_blob2v2_dimple.png")), "blob2v2.png")
        EDAssert.equal(True, os.path.exists(os.path.join(strResultDir, "ep_xtal5w1_1_blob2v3_dimple.png")), "blob2v3.png")
        EDAssert.equal(True, os.path.exists(os.path.join(strResultDir, "ep_xtal5w1_1_dimple.log")), "dimple.log")
        EDAssert.equal(True, os.path.exists(os.path.join(strResultDir, "ep_xtal5w1_1_dimple.mtz")), "dimple.mtz")
        EDAssert.equal(True, os.path.exists(os.path.join(strResultDir, "ep_xtal5w1_1_dimple.pdb")), "dimple.pdb")
        EDAssert.equal(True, os.path.exists(os.path.join(strResultDir, "ep_xtal5w1_1_findblobs_dimple.log")), "findblobs.log")
        EDAssert.equal(True, os.path.exists(os.path.join(strResultDir, "ep_xtal5w1_1_refmac5restr_dimple.log")), "refmac5restr.log")
        EDAssert.equal(True, os.path.exists(os.path.join(strResultDir, "ep_xtal5w1_1_results_dimple.pdf")), "dimple.pdf")
        shutil.rmtree(strResultDir)

    def test_createHtmlPage(self):
        strDimpleOutput = os.path.join(self.strDataPath, "dimple", "Dimplev1_0_dataOutput.xml")
        strResultDimple = self.readAndParseFile(strDimpleOutput)
        xsDataResultDimple = XSDataResultDimple.parseString(strResultDimple)
        strPdfPath = os.path.join(xsDataResultDimple.resultsDirectory.path.value, "DIMPLE.pdf")
        edPlugin = self.getPlugin()
        strPyarchRootDir = tempfile.mkdtemp(prefix="html_", dir=os.path.join(self.strDataPath, "dimple"))
        strPrefix = "xtal5w1_1"
        strProposal = "mx415"
        strSessionDate = "2015-02-23"
        strBeamline = "id29"
        strResultsDirectory = strPyarchRootDir
        listPath = edPlugin.copyResults(strPrefix, strPyarchRootDir, xsDataResultDimple, strPdfPath)
        listPathHtml = edPlugin.createHtmlPage(strPrefix, xsDataResultDimple, strResultsDirectory, strPyarchRootDir, strProposal, strSessionDate, strBeamline)
        for pathHtml in listPathHtml:
            EDAssert.equal(True, os.path.exists(pathHtml), "HTML page generated")
        shutil.rmtree(strPyarchRootDir)



    def test_extractFinalResultsFromRefmac5RestrLog(self):
        strRefmacLogFilePath = os.path.join(self.strDataPath, "dimple", "08-refmac5_restr.log")
        edPlugin = self.getPlugin()
        strResults = edPlugin.extractFinalResultsFromRefmac5RestrLog(strRefmacLogFilePath)
        EDAssert.equal(True, strResults != "", "Read Refmac5restr log")


    def process(self):
        self.addTestMethod(self.test_extractFinalResultsFromRefmac5RestrLog)
        self.addTestMethod(self.test_copyResults)
        self.addTestMethod(self.test_createHtmlPage)




