#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2012 European Synchrotron Radiation Facility
#                       Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#


__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
import time
import pprint
import shutil
import tempfile

from EDUtilsFile import EDUtilsFile
from EDAssert                        import EDAssert
from EDTestCasePluginUnit            import EDTestCasePluginUnit

from EDFactoryPlugin import edFactoryPlugin

edFactoryPlugin.loadModule('XSDataXDSAPPv1_0')
from XSDataXDSAPPv1_0 import XSDataResultXDSAPP

class EDTestCasePluginUnitControlXDSAPPv1_0(EDTestCasePluginUnit):


    def __init__(self, _strTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlXDSAPPv1_0")
        self.strDataPath = self.getPluginTestsDataHome()

    def test_parseLogFile(self):
        # Not forced space group
        edPlugin = self.getPlugin()
        logFile = os.path.join(self.strDataPath, "results_xtal5w1_1.txt")
        dictLog = edPlugin.parseLogFile(logFile)
        # pprint.pprint(dictLog)
        for item in ["spaceGroup", "spaceGroupNumber",
                     "cellA", "cellB", "cellC",
                     "cellAlpha", "cellBeta", "cellGamma"]:
            EDAssert.equal(True, item in dictLog, item)
        # Forced space group
        edPlugin = self.getPlugin()
        logFile = os.path.join(self.strDataPath, "results_t1_1.txt")
        dictLog = edPlugin.parseLogFile(logFile)
        # pprint.pprint(dictLog)
        for item in ["spaceGroup", "spaceGroupNumber",
                     "cellA", "cellB", "cellC",
                     "cellAlpha", "cellBeta", "cellGamma"]:
            EDAssert.equal(True, item in dictLog, item)


    def test_runXscale(self):
        workingDirectory = tempfile.mkdtemp(prefix="XDSAPP_XSCALE_")
        pathToXdsAsciiHkl = "/data/scisoft/pxsoft/data/AUTO_PROCESSING/XDSAPP/XDSAPPv1_0/XDS_ASCII.HKL"
        shutil.copy(pathToXdsAsciiHkl, workingDirectory)
        # self.screen(workingDirectory)
        edPlugin = self.getPlugin()
        edPlugin.runXscale(workingDirectory, merged=True)
        for fileName in ["XSCALE.LP", "merged_noanom_XSCALE.hkl", "XSCALE.INP", "xscale.log"]:
            EDAssert.equal(True, os.path.exists(os.path.join(workingDirectory, fileName)), fileName)
        shutil.rmtree(workingDirectory)

    def test_createXSDataInputStoreAutoProc(self):
        edPlugin = self.getPlugin()
        strPath = os.path.join(self.strDataPath, "XDSAPPv1_0_dataOutput.xml")
        xsDataResultXDSAPP = XSDataResultXDSAPP.parseFile(strPath)
        proposal = "mx415"
        isAnom = True
        timeStart = time.localtime()
        timeEnd = time.localtime()
        processDirectory = "/data/visitor/mx415/id30a2/20161206/PROCESSED_DATA/t3/autoprocessing_t3_run3_1/XDSAPP"
        template = "t3_3_####.cbf"
        strPathXscaleLp = "/data/scisoft/pxsoft/data/AUTO_PROCESSING/XDSAPP/XDSAPPv1_0/XSCALE.LP"
        dataCollectionId = 123456
        edPlugin.createXSDataInputStoreAutoProc(xsDataResultXDSAPP, processDirectory, template,
                                                strPathXscaleLp, isAnom, proposal, timeStart, timeEnd, dataCollectionId)

    def test_parseXscaleLp(self):
        strPathXscaleLp = "/data/scisoft/pxsoft/data/AUTO_PROCESSING/XDSAPP/XDSAPPv1_0/XSCALE.LP"
        edPlugin = self.getPlugin()
        dictXscale = edPlugin.parseXscaleLp(strPathXscaleLp)
        # pprint.pprint(dictXscale)
        for resolutionShell in ["innerShell", "outerShell", "overall"]:
            for item in ["CCHalf", "ccAno", "completeness", "meanIOverSigI",
                         "multiplicity", "nTotalObservations", "ntotalUniqueObservations",
                         "rMerge", "resolutionLimitHigh", "resolutionLimitLow"]:
                EDAssert.equal(True, dictXscale[resolutionShell][item] is not None, resolutionShell + "." + item)

    def test_parseCorrectLp(self):
        strPathCorrectLp = "/data/scisoft/pxsoft/data/AUTO_PROCESSING/XDSAPP/XDSAPPv1_0/CORRECT.LP"
        edPlugin = self.getPlugin()
        isa = edPlugin.parseCorrectLp(strPathCorrectLp)
        EDAssert.equal(24.62, isa, "ISa value")



    def process(self):
        self.addTestMethod(self.test_parseLogFile)
        self.addTestMethod(self.test_runXscale)
        self.addTestMethod(self.test_createXSDataInputStoreAutoProc)
        self.addTestMethod(self.test_parseXscaleLp)
        self.addTestMethod(self.test_parseCorrectLp)
