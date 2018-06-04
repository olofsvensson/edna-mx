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
        h5MasterFilePath1, h5DataFilePath1, h5FileNumber = edPlugin.getH5FilePath(filePath1, 9)
        h5MasterFilePath1Reference = "/data/id30a3/inhouse/opid30a3/20160204/RAW_DATA/meshtest/XrayCentering_01/mesh-meshtest_1_1_master.h5"
        h5DataFilePath1Reference = "/data/id30a3/inhouse/opid30a3/20160204/RAW_DATA/meshtest/XrayCentering_01/mesh-meshtest_1_1_data_000001.h5"
        print h5MasterFilePath1
        print h5MasterFilePath1Reference
        print h5DataFilePath1
        print h5DataFilePath1Reference
        EDAssert.equal(h5MasterFilePath1, h5MasterFilePath1Reference, "masterPath1")
        EDAssert.equal(h5DataFilePath1, h5DataFilePath1Reference, "dataPath1")
        # fast mesh
        filePath2 = "/data/id30a3/inhouse/opid30a3/20171017/RAW_DATA/mesh2/MeshScan_02/mesh-opid30a3_2_0021.cbf"
        h5MasterFilePath2, h5DataFilePath2, h5FileNumber2 = edPlugin.getH5FilePath(filePath2, batchSize=20, isFastMesh=True)
        print(h5MasterFilePath2, h5DataFilePath2, h5FileNumber2)
        h5MasterFilePath2Reference = "/data/id30a3/inhouse/opid30a3/20171017/RAW_DATA/mesh2/MeshScan_02/mesh-opid30a3_2_1_master.h5"
        EDAssert.equal(h5MasterFilePath2, h5MasterFilePath2Reference, "master path2")
        h5DataFilePath2Reference = "/data/id30a3/inhouse/opid30a3/20171017/RAW_DATA/mesh2/MeshScan_02/mesh-opid30a3_2_1_data_000001.h5"
        EDAssert.equal(h5DataFilePath2, h5DataFilePath2Reference, "data path2")
        # fast mesh 2
        filePath2 = "/data/id30a3/inhouse/opid30a3/20171017/RAW_DATA/mesh2/MeshScan_02/mesh-opid30a3_2_0321.cbf"
        h5MasterFilePath2, h5DataFilePath2, h5FileNumber2 = edPlugin.getH5FilePath(filePath2, batchSize=20, isFastMesh=True)
        print(h5MasterFilePath2, h5DataFilePath2, h5FileNumber2)
        h5MasterFilePath2Reference = "/data/id30a3/inhouse/opid30a3/20171017/RAW_DATA/mesh2/MeshScan_02/mesh-opid30a3_2_1_master.h5"
        EDAssert.equal(h5MasterFilePath2, h5MasterFilePath2Reference, "master path2")
        h5DataFilePath2Reference = "/data/id30a3/inhouse/opid30a3/20171017/RAW_DATA/mesh2/MeshScan_02/mesh-opid30a3_2_1_data_000004.h5"
        EDAssert.equal(h5DataFilePath2, h5DataFilePath2Reference, "data path2")



    def process(self):
        self.addTestMethod(self.testGetH5FilePath)


