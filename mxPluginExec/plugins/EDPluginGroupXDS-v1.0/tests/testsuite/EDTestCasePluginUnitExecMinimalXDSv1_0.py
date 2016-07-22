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

__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "EMBL-Grenoble, Grenoble, France"
__date__ = "20160722"
__status__ = "production"

import os


from EDAssert import EDAssert
from EDUtilsPath import EDUtilsPath

from EDTestCasePluginUnit import EDTestCasePluginUnit
from EDUtilsTest import EDUtilsTest


class EDTestCasePluginUnitExecMinimalXDSv1_0(EDTestCasePluginUnit):


    def __init__(self, _strTestName="EDPluginExecMinimalXdsv1_0"):
        EDTestCasePluginUnit.__init__(self, _strTestName)


    def testCheckSpotRanges(self):
        edPlugin = self.getPlugin()
        listSpotRanges = [[1, 100], [200, 300], [400, 500]]
        EDAssert.equal(['1 100', '200 300', '400 500'], edPlugin.checkSpotRanges(listSpotRanges, 1, 500))
        EDAssert.equal(['1 100'], edPlugin.checkSpotRanges(listSpotRanges, 1, 100))
        EDAssert.equal(['200 300', '400 450'], edPlugin.checkSpotRanges(listSpotRanges, 150, 450))
        EDAssert.equal(['250 300', '400 500'], edPlugin.checkSpotRanges(listSpotRanges, 250, 500))

    def process(self):
        self.addTestMethod(self.testCheckSpotRanges)


