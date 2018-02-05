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
        strInputXML = EDUtilsFile.readFile(os.path.join(self.strDataPath, "XSDataInputAutoPROC_reference.xml"))
        xsDataInput = XSDataInputAutoPROC.parseString(strInputXML)
        strCommandLine = edPlugin.generateCommandLine(xsDataInput)
        # print(strCommandLine)
        EDAssert.equal("-B -xml -nthreads 12 autoPROC_ScaleWithXscale='yes' -Id 1088454A,/scisoft/pxsoft/data/AUTO_PROCESSING/id29/20130301/RAW_DATA/GaelleB/xtal5,xtal5w1_1_####.cbf,1,50 -R 5.0 2.0", strCommandLine, "Reference data input")
        # Symmetry input
        strInputXML = EDUtilsFile.readFile(os.path.join(self.strDataPath, "XSDataInputAutoPROC_symm.xml"))
        xsDataInput = XSDataInputAutoPROC.parseString(strInputXML)
        strCommandLine = edPlugin.generateCommandLine(xsDataInput)
        EDAssert.equal("-B -xml -nthreads 12 autoPROC_ScaleWithXscale='yes' -Id 1088454A,/scisoft/pxsoft/data/AUTO_PROCESSING/id29/20130301/RAW_DATA/GaelleB/xtal5,xtal5w1_1_####.cbf,1,50 -R 5.0 2.0 symm=\"P1\" cell=\"52.4 78.7 79.4 90.0 89.8 109.4\"", strCommandLine, "Reference data input")



    def process(self):
        self.addTestMethod(self.test_generateCommandLine)
