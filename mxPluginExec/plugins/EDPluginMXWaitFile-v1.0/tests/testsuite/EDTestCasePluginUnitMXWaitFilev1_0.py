#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) ESRF
#
#    Principal author:       Jerome Kieffer
#
#    Contributing author:    Olof Svensson
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

__author__ = "Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataMXWaitFilev1_0 import XSDataInputMXWaitFile
from XSDataCommon import  XSDataFile, XSDataString, XSDataInteger

class EDTestCasePluginUnitMXWaitFilev1_0(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin MXWaitFilev1_0
    """

    def __init__(self, _strTestName=None):
        """
        """
        EDTestCasePluginUnit.__init__(self, "EDPluginMXWaitFilev1_0")


    def testCheckParameters(self):
        xsDataInput = XSDataInputMXWaitFile()
        xsDataInput.setExpectedFile(XSDataFile(XSDataString("toto")))
        xsDataInput.setExpectedSize(XSDataInteger(10))
        edPluginMXWaitFile = self.createPlugin()
        edPluginMXWaitFile.setDataInput(xsDataInput)
        edPluginMXWaitFile.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)
