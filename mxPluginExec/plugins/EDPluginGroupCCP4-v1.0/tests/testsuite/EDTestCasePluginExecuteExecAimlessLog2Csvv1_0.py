# coding: utf8
#
#    Project: <projectName>
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

import os


from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute


class EDTestCasePluginExecuteExecAimlessLog2Csvv1_0(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin dimple
    """

    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginExecAimlessLog2Csvv1_0")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputAimlessLog2Csv_reference.xml"))



    def testExecute(self):
        self.run()

        edPlugin = self.getPlugin()
        csvPath = edPlugin.dataOutput.csvPath.path.value
        EDAssert.equal(True, os.path.exists(csvPath), "Path to csv file exists")
        referenceCsvFile = os.path.join(self.getPluginTestsDataHome(), "aimless.csv")
        with open(referenceCsvFile) as f1:
            referenceOutput = f1.read()
        with open(csvPath) as f2:
            output = f2.read()
        EDAssert.equal(referenceOutput, output, "Content is equal to reference")




    def process(self):
        self.addTestMethod(self.testExecute)


