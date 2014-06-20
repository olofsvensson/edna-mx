#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
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

from EDVerbose                           import EDVerbose
from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute

class EDTestCasePluginExecuteControlIndexingIndicatorsv1_1(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlIndexingIndicatorsv1_1")
        self.setRequiredPluginConfiguration("EDPluginMOSFLMIndexingv10")
        self.setRequiredPluginConfiguration("EDPluginLabelitDistlv1_1")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataCollection_reference.xml"), "dataCollection")

    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "ref-2m_RNASE_1_0002.cbf", "ref-2m_RNASE_1_0001.cbf" ])


    def testExecute(self):
        self.run()



    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    edTestCasePluginExecuteControlIndexingIndicatorsv11 = EDTestCasePluginExecuteControlIndexingIndicatorsv11("EDTestCasePluginExecuteControlIndexingIndicatorsv11")
    edTestCasePluginExecuteControlIndexingIndicatorsv11.execute()
