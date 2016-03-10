# coding: utf8
#
#    Project: <projectName>
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) <copyright>
#
#    Principal author:       <author>
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

__author__ = "<author>"
__license__ = "GPLv3+"
__copyright__ = "<copyright>"

import os

from EDVerbose import EDVerbose
from EDAssert import EDAssert
from EDTestCasePluginExecute import EDTestCasePluginExecute

from XSDataXDSv1_0 import XSDataXdsOutputFile
from XSDataXDSv1_0 import XSDataXdsOutput


class EDTestCasePluginParseXdsOutputv1_0(EDTestCasePluginExecute):
    """
    Those are all execution tests for the EDNA Exec plugin MinimalXds
    """

    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginParseXdsOutputv1_0")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(),
                                           "XSDataXdsOutputFile_reference.xml"))


    def testExecute(self):

        self.run()

        plugin = self.getPlugin()
        output = plugin.dataOutput
        EDAssert.equal(True, output.completeness_entries != [], "completeness_entries")
        EDAssert.equal(True, output.total_completeness is not None, "total_completeness")
        EDAssert.equal(True, output.crystal_mosaicity is not None, "crystal_mosaicity")
        EDAssert.equal(True, output.direct_beam_coordinates is not None, "direct_beam_coordinates")
        EDAssert.equal(True, output.direct_beam_detector_coordinates is not None, "direct_beam_detector_coordinates")
        EDAssert.equal(True, output.detector_origin is not None, "detector_origin")
        EDAssert.equal(True, output.coordinates_of_unit_cell_a_axis is not None, "coordinates_of_unit_cell_a_axis")
        EDAssert.equal(True, output.cell_a is not None, "cell_a")

    def process(self):
        self.addTestMethod(self.testExecute)
