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

__author__="Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os

from EDAssert import EDAssert
from EDTestCasePluginUnit import EDTestCasePluginUnit


class EDTestCasePluginUnitExecPointlessv1_0(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA Exec plugin Pointlessv1_0
    """

    def __init__(self, _strTestName = None):
        EDTestCasePluginUnit.__init__(self, "EDPluginExecPointlessv1_0")
              

    def testParsePointlessOutput(self):
        edPlugin = self.createPlugin()
        pathToLogFile = os.path.join(self.getPluginTestsDataHome(), "pointless.log")
        xsDataResult = edPlugin.parsePointlessOutput(pathToLogFile)
#        print xsDataResult.marshal()
        EDAssert.equal("C 2 2 2", xsDataResult.sgstr.value, "Space group name")
        EDAssert.equal(21, xsDataResult.sgnumber.value, "Space group number")
        EDAssert.equal(52.55, xsDataResult.cell.length_a.value, "Cell length a")
        EDAssert.equal(148.80, xsDataResult.cell.length_b.value, "Cell length b")
        EDAssert.equal(79.68, xsDataResult.cell.length_c.value, "Cell length v")
        EDAssert.equal(91.00, xsDataResult.cell.angle_alpha.value, "Cell angle alpha")
        EDAssert.equal(92.00, xsDataResult.cell.angle_beta.value, "Cell angle beta")
        EDAssert.equal(93.00, xsDataResult.cell.angle_gamma.value, "Cell angle gamma")
        pathToLogFile = os.path.join(self.getPluginTestsDataHome(), "pointless2.log")
        xsDataResult = edPlugin.parsePointlessOutput(pathToLogFile)
#        print xsDataResult.marshal()
        EDAssert.equal("P 3 2 1", xsDataResult.sgstr.value, "Space group name")
        EDAssert.equal(150, xsDataResult.sgnumber.value, "Space group number")
        EDAssert.equal(110.9918, xsDataResult.cell.length_a.value, "Cell length a")
        EDAssert.equal(110.9918, xsDataResult.cell.length_b.value, "Cell length b")
        EDAssert.equal(137.0160, xsDataResult.cell.length_c.value, "Cell length v")
        EDAssert.equal(94.00, xsDataResult.cell.angle_alpha.value, "Cell angle alpha")
        EDAssert.equal(95.00, xsDataResult.cell.angle_beta.value, "Cell angle beta")
        EDAssert.equal(120.00, xsDataResult.cell.angle_gamma.value, "Cell angle gamma")
    
    
    def process(self):
        self.addTestMethod(self.testParsePointlessOutput)

