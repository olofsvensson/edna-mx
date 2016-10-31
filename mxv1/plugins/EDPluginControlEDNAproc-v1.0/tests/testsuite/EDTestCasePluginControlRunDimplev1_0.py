# coding: utf8
#
#    Project: EDNAproc
#             http://www.edna-site.org
#
#    Copyright (C) ESRF
#
#    Principal author: Olof Svensson
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

import os, tempfile, shutil

from EDVerbose import EDVerbose
from EDAssert import EDAssert
from EDUtilsPath import EDUtilsPath
from EDTestCasePluginExecute import EDTestCasePluginExecute

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

class EDTestCasePluginControlRunDimplev1_0(EDTestCasePluginExecute):

    def __init__(self, _strTestName = None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlRunDimplev1_0")

        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputControlDimple_reference.xml"))

    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "dimple_noanom_aimless.mtz" ])

    def testExecute(self):
        pyarchPath = tempfile.mkdtemp(prefix="EDTestCasePluginControlRunDimplev1_0_")
        xsDataPyarchPath = XSDataFile(XSDataString(pyarchPath))
        self._edPlugin.dataInput.pyarchPath = xsDataPyarchPath
        self.run()

    def process(self):
        self.addTestMethod(self.testExecute)
