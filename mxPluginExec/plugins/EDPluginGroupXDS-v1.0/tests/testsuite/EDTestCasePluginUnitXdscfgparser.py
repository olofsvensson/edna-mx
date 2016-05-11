# coding: utf8
#
#    Project: EDNA dp
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

__author__ = "Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os

from EDTestCasePluginUnit import EDTestCasePluginUnit
from EDAssert import EDAssert

import xdscfgparser


class EDTestCasePluginUnitXdscfgparser(EDTestCasePluginUnit):
    """
    Test of xdscfgparser
    """

    def __init__(self, _strTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginExecMinimalXdsv1_0")


    def testParse_xds_file(self):
        xdsInpPath = os.path.join(self.getPluginTestsDataHome(), "XDS_xdscfgparser.INP")
        parserDict = xdscfgparser.parse_xds_file(xdsInpPath)
#        import pprint
#        pprint.pprint(parserDict)
        EDAssert.equal([1, 4], parserDict["BACKGROUND_RANGE="], "BACKGROUND_RANGE")
        EDAssert.equal(['/data/id29/inhouse/opid291/x_geo_corr.cbf'], parserDict["X-GEO_CORR="], "X-GEO_CORR")
        EDAssert.strAlmostEqual(305.04, parserDict['DETECTOR_DISTANCE='], 'DETECTOR_DISTANCE')


    def process(self):
        self.addTestMethod(self.testParse_xds_file)



