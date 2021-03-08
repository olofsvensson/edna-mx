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
__date__ = "20131129"
__status__ = "beta"

import os
import tempfile

from EDAssert                        import EDAssert
from EDTestCasePluginUnit            import EDTestCasePluginUnit
from EDUtilsFile import EDUtilsFile

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString
from XSDataCommon import XSDataDouble

from XSDataDozorv1_0 import XSDataInputDozor
from XSDataDozorv1_0 import XSDataResultDozor

class EDTestCasePluginUnitDozorv1_0(EDTestCasePluginUnit):


    def __init__(self, _strTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginDozorv1_0")
        self.strDataPath = self.getPluginTestsDataHome()

    def test_generateCommands(self):
        edPlugin = self.getPlugin()
        strInputXML = EDUtilsFile.readFile(os.path.join(self.strDataPath, "XSDataInputDozor_reference.xml"))
        xsDataInput = XSDataInputDozor.parseString(strInputXML)
        strCommandText = edPlugin.generateCommands(xsDataInput)
        print(strCommandText)

    def test_parseOutput(self):
        edPlugin = self.getPlugin()
        edPlugin.startingAngle = 10.0
        edPlugin.firstImageNumber = 1
        edPlugin.oscillationRange = 0.1
        edPlugin.overlap = 0.0
        xsDataResult = edPlugin.parseOutput(os.path.join(self.strDataPath, "Dozor_00002.log"))
        EDAssert.equal(100, len(xsDataResult.imageDozor), "Result from 100 images")
        EDAssert.equal(True, xsDataResult.halfDoseTime is not None, "Half dose time v1.3.8")

    def test_parseDouble(self):
        edPlugin = self.getPlugin()
        EDAssert.strAlmostEqual(1.0, edPlugin.parseDouble("1.0").value, "Parsing '1.0'")
        EDAssert.equal(None, edPlugin.parseDouble("****"), "Parsing '****'")

    def test_generatePngPlots(self):
        edPlugin = self.getPlugin()
        plotmtvFile = os.path.join(self.strDataPath, "dozor_rd.mtv")
        tmpDir = tempfile.mkdtemp(suffix="EDTestCasePluginUnitDozorv1_0_")
        listXSFile = edPlugin.generatePngPlots(plotmtvFile, tmpDir)
        for xsFile in listXSFile:
            print(xsFile.marshal())

    def process(self):
        self.addTestMethod(self.test_generateCommands)
        self.addTestMethod(self.test_parseOutput)
        self.addTestMethod(self.test_parseDouble)
        self.addTestMethod(self.test_generatePngPlots)
