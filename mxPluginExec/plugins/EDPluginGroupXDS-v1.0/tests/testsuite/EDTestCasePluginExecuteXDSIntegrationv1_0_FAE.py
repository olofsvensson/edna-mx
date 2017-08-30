#
#    Project: EDNA mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008 EMBL-Grenoble, Grenoble, France
#
#    Principal authors: Sandor Brockhauser (brockhauser@embl-grenoble.fr)
#                       Olof Svensson (svensson@esrf.fr)
#                       Pierre Legrand (pierre.legrand@synchrotron-soleil.fr)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#

__authors__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "EMBL-Grenoble, Grenoble, France"
__date__ = "20170829"
__status__ = "alpha"

import os


from EDAssert                         import EDAssert
from EDUtilsPath                      import EDUtilsPath
from EDTestCasePluginExecute          import EDTestCasePluginExecute
from EDUtilsTest                      import EDUtilsTest




class EDTestCasePluginExecuteXDSIntegrationv1_0_FAE(EDTestCasePluginExecute):


    def __init__(self, _strTestName="EDPluginXDSIntegrationv1_0"):
        EDTestCasePluginExecute.__init__(self, _strTestName)

        self.setConfigurationFile(self.getRefConfigFile())
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), "XSDataInputXDSIntegration_FAE.xml"))

    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)

    def testExecute(self):
        self.run()

    def process(self):
        self.addTestMethod(self.testExecute)

