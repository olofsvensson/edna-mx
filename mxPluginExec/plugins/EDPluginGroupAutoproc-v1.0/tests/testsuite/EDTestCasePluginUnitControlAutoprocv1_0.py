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

__author__="Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os

from EDTestCasePluginUnit import EDTestCasePluginUnit
from EDAssert import EDAssert

class EDTestCasePluginUnitControlAutoprocv1_0(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA control plugin Autoprocv1_0
    """

    def __init__(self, _strTestName = None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlAutoprocv1_0")
              

    def test_getBeamlinePrefixFromPath(self):
        edPlugin = self.getPlugin()
        (strBeamline, strProposal, strPrefix) = edPlugin.getBeamlinePrefixFromPath("/data/visitor/mx1638/id30a1/20140925/PROCESSED_DATA/PIRIN/PIRIN-CCT250879_50mM_2_24h/xds_PIRIN-CCT250879_50mM_2_24h_run1_1/XDS.INP")
        EDAssert.equal("id30a1", strBeamline, "Visitor beamline")
        EDAssert.equal("mx1638", strProposal, "Visitor proposal")
        EDAssert.equal("PIRIN-CCT250879_50mM_2_24h_run1_1", strPrefix, "Visitor prefix")
        (strBeamline, strProposal, strPrefix) = edPlugin.getBeamlinePrefixFromPath("/data/id23eh1/inhouse/opid231/20140925/PROCESSED_DATA/xds_opid231_run3_1/XDS.INP")
        EDAssert.equal("id23eh1", strBeamline, "Inhouse beamline")
        EDAssert.equal("opid231", strProposal, "Inhouse proposal")
        EDAssert.equal("opid231_run3_1", strPrefix, "Inhouse prefix")
        
    
    
    def process(self):
        self.addTestMethod(self.test_getBeamlinePrefixFromPath)

    

