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


from EDUtilsFile import EDUtilsFile
from EDAssert                        import EDAssert
from EDTestCasePluginUnit            import EDTestCasePluginUnit

from XSDataXDSAPPv1_0 import XSDataInputXDSAPP

class EDTestCasePluginUnitXDSAPPv1_0(EDTestCasePluginUnit):


    def __init__(self, _strTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginExecXDSAPPv1_0")
        self.strDataPath = self.getPluginTestsDataHome()

    def test_generateCommandLine(self):
        edPlugin = self.getPlugin()
        strInputXML = EDUtilsFile.readFile(os.path.join(self.strDataPath, "XSDataInputXDSAPP_reference.xml"))
        xsDataInput = XSDataInputXDSAPP.parseString(strInputXML)
        strCommandLine = edPlugin.generateCommandLine(xsDataInput)
        print(strCommandLine)
#        EDAssert.equal("--cmd --image /data/scisoft/pxsoft/data/AUTO_PROCESSING/id29/20130301/RAW_DATA/GaelleB/xtal5/xtal5w1_1_0001.cbf --fried=true", strCommandLine, "Reference data input")

    def test_parseOutputDirectory(self):
        testXDSAPPDir = "/data/scisoft/pxsoft/data/AUTO_PROCESSING/XDSAPP/XDSAPPv1_0"
        edPlugin = self.getPlugin()
        xsDataResultXDSAPP = edPlugin.parseOutputDirectory(testXDSAPPDir, "xtal5w1_1")
        print(xsDataResultXDSAPP.marshal())
        # EDAssert.equal(os.path.exists(xsDataResultXDSAPP.logFile.path.value), True, "Xia2 log file")


    def process(self):
        self.addTestMethod(self.test_generateCommandLine)
        self.addTestMethod(self.test_parseOutputDirectory)
