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
__date__ = "20120712"
__status__ = "production"

from EDTestSuite  import EDTestSuite

class EDTestSuitePluginPlotGlev1_1(EDTestSuite):
    """
    This is the test suite for EDNA plugin PlotGle 
    It will run subsequently all unit tests and execution tests.     
    """        

    def process(self):
        self.addTestCaseFromName("EDTestCasePluginUnitPlotGlev1_1")
        self.addTestCaseFromName("EDTestCasePluginExecutePlotGlev1_1")
        self.addTestCaseFromName("EDTestCasePluginExecutePlotGlev1_1_glePlotInput")
        


if __name__ == '__main__':

    edTestSuitePluginExecPlotGlev1_1 = EDTestSuitePluginExecPlotGlev1_1("EDTestSuitePluginExecPlotGlev1_1")
    edTestSuitePluginExecPlotGlev1_1.execute()

