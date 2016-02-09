#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:        Olof Svensson
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

from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit
from EDAssert import EDAssert

class EDTestCasePluginUnitControlImageQualityIndicatorsv1_4(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlImageQualityIndicatorsv1_4")


    def testGetH5FilePath(self):
        edPlugin = self.getPlugin()
        filePath1 = "/data/id30a3/inhouse/opid30a3/20160204/RAW_DATA/meshtest/XrayCentering_01/mesh-meshtest_1_0001.cbf"
        h5FilePath1 = edPlugin.getH5FilePath(filePath1, 9)
        h5FilePath1Reference = "/data/id30a3/inhouse/opid30a3/20160204/RAW_DATA/meshtest/XrayCentering_01/mesh-meshtest_1_1_master.h5"
        EDAssert.equal(h5FilePath1, h5FilePath1Reference, "path1")
        filePath2 = "/data/id30a3/inhouse/opid30a3/20160204/RAW_DATA/meshtest/XrayCentering_01/mesh-meshtest_1_00012.cbf"
        h5FilePath2 = edPlugin.getH5FilePath(filePath2, 9)
        h5FilePath2Reference = "/data/id30a3/inhouse/opid30a3/20160204/RAW_DATA/meshtest/XrayCentering_01/mesh-meshtest_1_10_master.h5"
        EDAssert.equal(h5FilePath2, h5FilePath2Reference, "path2")



    def process(self):
        self.addTestMethod(self.testGetH5FilePath)


