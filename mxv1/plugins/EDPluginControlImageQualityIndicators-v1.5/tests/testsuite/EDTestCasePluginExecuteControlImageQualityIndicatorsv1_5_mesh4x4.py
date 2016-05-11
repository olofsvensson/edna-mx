#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2013 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr)
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

__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os

from EDTestCasePluginExecute import EDTestCasePluginExecute


class EDTestCasePluginExecuteControlImageQualityIndicatorsv1_5_mesh4x4(EDTestCasePluginExecute):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlImageQualityIndicatorsv1_5")
        self.setRequiredPluginConfiguration("EDPluginDistlSignalStrengthv1_1")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputControlImageQualityIndicators_mesh4x4.xml"))
#        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataResultControlImageQualityIndicators_mesh4x4.xml"))


    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "mesh-test_1_0001.cbf",
                            "mesh-test_1_0002.cbf",
                            "mesh-test_1_0003.cbf",
                            "mesh-test_1_0004.cbf",
                            "mesh-test_1_0005.cbf",
                            "mesh-test_1_0006.cbf",
                            "mesh-test_1_0007.cbf",
                            "mesh-test_1_0008.cbf",
                            "mesh-test_1_0009.cbf",
                            "mesh-test_1_0010.cbf",
                            "mesh-test_1_0011.cbf",
                            "mesh-test_1_0012.cbf",
                            "mesh-test_1_0013.cbf",
                            "mesh-test_1_0014.cbf",
                            "mesh-test_1_0015.cbf",
                            "mesh-test_1_0016.cbf",
                             ])


    def testExecute(self):
        self.run()


    def process(self):
        self.addTestMethod(self.testExecute)


