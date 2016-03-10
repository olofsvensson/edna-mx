# coding: utf8
#
#    Project: EDNAproc
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author: Thomas Boeglin
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

__authors__=["Thomas Boeglin", "Olof Svensson"]
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os, tempfile, shutil

from EDVerbose import EDVerbose
from EDAssert import EDAssert
from EDUtilsPath import EDUtilsPath
from EDTestCasePluginExecute import EDTestCasePluginExecute


class EDTestCasePluginControlFileConversionv1_0(EDTestCasePluginExecute):

    def __init__(self, _strTestName = None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlFileConversionv1_0")

        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataFileConversionInput_reference.xml"))
        self.strTmpDir = tempfile.mkdtemp(prefix="EDPluginControlFileConversionv1_0", dir=EDUtilsPath.getEdnaTestDataImagesPath())
        if "EDNA_TMP_DIR" in os.environ.keys():
            self.strTmpDirOrig = os.environ["EDNA_TMP_DIR"]
        else:
            self.strTmpDirOrig = None
        os.environ["EDNA_TMP_DIR"] = self.strTmpDir


    def testExecute(self):
        self.run()
        edPlugin = self.getPlugin()
        xsDataFileConversionOut = edPlugin.dataOutput
        EDAssert.equal(True, xsDataFileConversionOut.status.isSuccess.value, "Is success")
        EDAssert.equal(19, xsDataFileConversionOut.pointless_sgnumber.value, "pointless_sgnumber")
        EDAssert.equal("P 21 21 21", xsDataFileConversionOut.pointless_sgstring.value, "pointless_sgstring")
        EDAssert.equal(True, os.path.exists(xsDataFileConversionOut.aimless_log.value), "Aimless log exists")
        shutil.rmtree(self.strTmpDir)
        if self.strTmpDirOrig is not None:
            os.environ["EDNA_TMP_DIR"] = self.strTmpDirOrig
        

    def process(self):
        self.addTestMethod(self.testExecute)
