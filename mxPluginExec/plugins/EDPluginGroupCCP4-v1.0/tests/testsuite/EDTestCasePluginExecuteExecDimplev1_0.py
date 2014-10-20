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


from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute


class EDTestCasePluginExecuteExecDimplev1_0(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin dimple
    """
    
    def __init__(self, _strTestName = None):
        EDTestCasePluginExecute.__init__(self, "EDPluginExecDimplev1_0")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputDimple_reference.xml"))
                 
                 
    def preProcess(self, _edObject = None):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage(["dimple_noanom_aimless.mtz", "dimple_model.pdb"])
        
    def testExecute(self):
        self.run()
        
        # Check that blob images have been generated
        edPlugin = self.getPlugin()
        EDAssert.equal(True, edPlugin.dataOutput.blob!=[], "Blobfiles in result")
        for xsDataBlobFile in edPlugin.dataOutput.blob:
            strPath = xsDataBlobFile.path.value
            EDAssert.equal(True, os.path.exists(strPath), "Path to %s exists" % os.path.basename(strPath))
        EDAssert.equal(True, os.path.exists(edPlugin.dataOutput.log.path.value), "Path to log file exists")
        EDAssert.equal(True, os.path.exists(edPlugin.dataOutput.finalMtz.path.value), "Path to final mtz file exists")
        EDAssert.equal(True, os.path.exists(edPlugin.dataOutput.finalPdb.path.value), "Path to final pdb file exists")
        EDAssert.equal(True, os.path.exists(edPlugin.dataOutput.findBlobsLog.path.value), "Path to find-blobs.log file exists")
        

    def process(self):
        self.addTestMethod(self.testExecute)

        
