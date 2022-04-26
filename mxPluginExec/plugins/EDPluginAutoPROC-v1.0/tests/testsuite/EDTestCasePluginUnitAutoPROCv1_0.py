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

from XSDataAutoPROCv1_0 import XSDataInputAutoPROC

class EDTestCasePluginUnitAutoPROCv1_0(EDTestCasePluginUnit):


    def __init__(self, _strTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginExecAutoPROCv1_0")
        self.strDataPath = self.getPluginTestsDataHome()

    def test_generateCommandLine(self):
        edPlugin = self.getPlugin()
        strInputXML1 = EDUtilsFile.readFile(os.path.join(self.strDataPath, "XSDataInputAutoPROC_reference.xml"))
        xsDataInput1 = XSDataInputAutoPROC.parseString(strInputXML1)
        strCommandLine1 = edPlugin.generateCommandLine(xsDataInput1)
        referenceCommandLine1 = "-B -xml -nthreads 12 -M ReportingInlined autoPROC_HIGHLIGHT=\"no\" -Id 1088454A,/data/scisoft/pxsoft/data/AUTO_PROCESSING/id29/20130301/RAW_DATA/GaelleB/xtal5,xtal5w1_1_####.cbf,1,50 -R 5.0 2.0"
        # print(strCommandLine1)
        EDAssert.equal(referenceCommandLine1, strCommandLine1, "Reference data input")
        # Symmetry input
        strInputXML2 = EDUtilsFile.readFile(os.path.join(self.strDataPath, "XSDataInputAutoPROC_symm.xml"))
        xsDataInput2 = XSDataInputAutoPROC.parseString(strInputXML2)
        strCommandLine2 = edPlugin.generateCommandLine(xsDataInput2)
        # print(strCommandLine2)
        referenceCommandLine2 = "-B -xml -nthreads 12 -M ReportingInlined autoPROC_HIGHLIGHT=\"no\" -Id 1088454A,/data/scisoft/pxsoft/data/AUTO_PROCESSING/id29/20130301/RAW_DATA/GaelleB/xtal5,xtal5w1_1_####.cbf,1,50 -R 5.0 2.0 symm=\"P1\" cell=\"52.4 78.7 79.4 90.0 89.8 109.4\""
        # print(referenceCommandLine)
        EDAssert.equal(referenceCommandLine2, strCommandLine2, "Reference data input")



    def process(self):
        self.addTestMethod(self.test_generateCommandLine)
