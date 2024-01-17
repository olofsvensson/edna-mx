#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2017 European Synchrotron Radiation Facility
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
__date__ = "20171016"
__status__ = "beta"

import os

from EDAssert import EDAssert
from EDUtilsFile import EDUtilsFile
from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString
from XSDataCommon import XSDataDouble

from XSDataFbestv1_0 import XSDataInputFbest
from XSDataFbestv1_0 import XSDataResultFbest

class EDTestCasePluginUnitFbestv1_0(EDTestCasePluginUnit):


    def __init__(self, _strTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginFbestv1_0")
        self.strDataPath = self.getPluginTestsDataHome()

    def test_generateCommands(self):
        edPlugin = self.getPlugin()
        strInputXML = EDUtilsFile.readFile(os.path.join(self.strDataPath, "XSDataInputFbest_reference.xml"))
        xsDataInput = XSDataInputFbest.parseString(strInputXML)
        strCommandText = edPlugin.generateCommands(xsDataInput)
        # print strCommandText
        strExpected = " -f 1.23e+12 -res 2.00 -bh 0.100 -bv 0.200 -w 0.987 -a 0.150 -sx 0.300 -sy 0.400 -rot 190.000 -rst 0.200 -tlim 0.020 -Dmax 40.0 -dose 10.0 -sen 25.0 -cs 0.500"
        EDAssert.equal(strExpected, strCommandText, "generateCommands")


    def test_parseOutput(self):
        edPlugin = self.getPlugin()
        strLogPath = os.path.join(self.strDataPath, "fbest.log")
        xsDataResult = edPlugin.parseOutput(strLogPath)
        xsDataResult.fbestLogFile = None
        strResultReferenceXML = EDUtilsFile.readFile(os.path.join(self.strDataPath, "XSDataResultFbest_reference.xml"))
        EDAssert.equal(strResultReferenceXML, xsDataResult.marshal(), "parseOutput")

    def process(self):
        self.addTestMethod(self.test_generateCommands)
        self.addTestMethod(self.test_parseOutput)

