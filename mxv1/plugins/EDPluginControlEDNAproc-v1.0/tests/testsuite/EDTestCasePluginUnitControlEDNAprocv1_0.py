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
import tempfile

from EDTestCasePluginUnit import EDTestCasePluginUnit
from EDAssert import EDAssert

class EDTestCasePluginUnitControlEDNAprocv1_0(EDTestCasePluginUnit):
    """
    Those are all units tests for the EDNA control plugin EDNAprocv1_0
    """

    def __init__(self, _strTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlEDNAprocv1_0")


    def test_getBeamlinePrefixFromPath(self):
        edPlugin = self.getPlugin()
        (strBeamline, strProposal, strSessionDate, strPrefix) = edPlugin.getBeamlinePrefixFromPath("/data/visitor/mx1638/id30a1/20140925/PROCESSED_DATA/PIRIN/PIRIN-CCT250879_50mM_2_24h/xds_PIRIN-CCT250879_50mM_2_24h_run1_1/XDS.INP")
        EDAssert.equal("id30a1", strBeamline, "Visitor beamline")
        EDAssert.equal("mx1638", strProposal, "Visitor proposal")
        EDAssert.equal("20140925", strSessionDate, "Visitor session date")
        EDAssert.equal("PIRIN-CCT250879_50mM_2_24h_run1_1", strPrefix, "Visitor prefix")
        (strBeamline, strProposal, strSessionDate, strPrefix) = edPlugin.getBeamlinePrefixFromPath("/data/id23eh1/inhouse/opid231/20140925/PROCESSED_DATA/xds_opid231_run3_1/XDS.INP")
        EDAssert.equal("id23eh1", strBeamline, "Inhouse beamline")
        EDAssert.equal("opid231", strProposal, "Inhouse proposal")
        EDAssert.equal("20140925", strSessionDate, "Inhouse session date")
        EDAssert.equal("opid231_run3_1", strPrefix, "Inhouse prefix")
        (strBeamline, strProposal, strSessionDate, strPrefix) = edPlugin.getBeamlinePrefixFromPath("/data/gz/visitor/mx1650/id30a3/20150728/PROCESSED_DATA/shoeb/dm_9/xds_dm_9_w1_run1_1/XDS.INP")
        EDAssert.equal("id30a3", strBeamline, "Visitor gz beamline")
        EDAssert.equal("mx1650", strProposal, "Visitor gz proposal")
        EDAssert.equal("20150728", strSessionDate, "Visitor gz session date")
        EDAssert.equal("dm_9_w1_run1_1", strPrefix, "Visitor gz prefix")
        (strBeamline, strProposal, strSessionDate, strPrefix) = edPlugin.getBeamlinePrefixFromPath("/data/gz/id30a3/inhouse/opid30a3/20150831/RAW_DATA/thaumatin/xds_thaumatin_run3_1/XDS.INP")
        EDAssert.equal("id30a3", strBeamline, "Inhouse gz beamline")
        EDAssert.equal("opid30a3", strProposal, "Inhouse gz proposal")
        EDAssert.equal("20150831", strSessionDate, "Inhouse gz session date")
        EDAssert.equal("thaumatin_run3_1", strPrefix, "Inhouse gz prefix")


    def test_eiger_template_to_image(self):
        edPlugin = self.getPlugin()
        print(edPlugin.eiger_template_to_image("eigertest_1_1_??????.h5", 1))
        print(edPlugin.eiger_template_to_image("eigertest_1_1_??????.h5", 1000))


    def test_createInputFile(self):
        edPlugin = self.getPlugin()
        testDir = tempfile.mkdtemp(prefix="EDTestCasePluginUnitControlEDNAprocv1_0_")
        dataCollectionId = 1756293
        filePath = edPlugin.createInputFile(dataCollectionId, testDir)
        print(filePath)


    def process(self):
#        self.addTestMethod(self.test_getBeamlinePrefixFromPath)
#        self.addTestMethod(self.test_eiger_template_to_image)
        self.addTestMethod(self.test_createInputFile)



