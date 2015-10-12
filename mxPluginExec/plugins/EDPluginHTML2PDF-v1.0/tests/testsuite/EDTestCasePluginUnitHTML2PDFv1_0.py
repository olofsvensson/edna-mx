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
__date__ = "20150304"
__status__ = "beta"

import os

from EDAssert                        import EDAssert
from EDTestCasePluginUnit            import EDTestCasePluginUnit

from XSDataHTML2PDFv1_0 import XSDataInputHTML2PDF
from XSDataHTML2PDFv1_0 import XSDataResultHTML2PDF

class EDTestCasePluginUnitHTML2PDFv1_0(EDTestCasePluginUnit):


    def __init__(self, _strTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginHTML2PDFv1_0")
        self.strDataPath = self.getPluginTestsDataHome()
        self.strReferenceInputFile = os.path.join(self.strDataPath, "XSDataInputHTML2PDF_reference.xml")


    def testGenerateCommands(self):
        edPluginHTML2PDF = self.createPlugin()
        xsDataInputHTML2PDF = XSDataInputHTML2PDF.parseFile(self.strReferenceInputFile)
        strCommandLine = edPluginHTML2PDF.generateCommands(xsDataInputHTML2PDF, "/tmp")
        EDAssert.equal("${EDNA_PLUGIN_TESTS_DATA_HOME}/xtal5w1_1_index.html /tmp/xtal5w1_1_index.pdf", strCommandLine)


    def process(self):
        self.addTestMethod(self.testGenerateCommands)
