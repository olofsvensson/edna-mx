#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Olof Svensson (svensson@esrf.fr) 
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

from EDTestCasePluginExecuteControlInterfaceToMXCuBEv1_4             import EDTestCasePluginExecuteControlInterfaceToMXCuBEv1_4
from EDAssert import EDAssert

class EDTestCasePluginExecuteControlInterfaceToMXCuBEv1_4_eiger4m_1(EDTestCasePluginExecuteControlInterfaceToMXCuBEv1_4):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecuteControlInterfaceToMXCuBEv1_4.__init__(self, "EDPluginControlInterfaceToMXCuBEv1_4")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputMXCuBE_eiger4m_1.xml"))


    def preProcess(self):
        EDTestCasePluginExecuteControlInterfaceToMXCuBEv1_4.preProcess(self)


    def testExecute(self):
        self.run()




    def process(self):
        self.addTestMethod(self.testExecute)




if __name__ == '__main__':

    EDTestCasePluginExecuteControlInterfaceToMXCuBEv1_4_bestBFactorFailed = EDTestCasePluginExecuteControlInterfaceToMXCuBEv1_4("EDTestCasePluginExecuteControlInterfaceToMXCuBEv1_4_bestBFactorFailed")
    EDTestCasePluginExecuteControlInterfaceToMXCuBEv1_4_bestBFactorFailed.execute()
