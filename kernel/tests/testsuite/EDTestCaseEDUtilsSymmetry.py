#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr)
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

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDTestCase      import EDTestCase
from EDUtilsSymmetry import EDUtilsSymmetry
from EDAssert        import EDAssert


class EDTestCaseEDUtilsSymmetry(EDTestCase):


    def testGetMinimumSymmetrySpaceGroupFromBravaisLattice(self):
        """
        Testing retrieving the lowest symmetry space group from all Bravais Lattices
        """
        listBravaisLattice = [ "aP", "mP", "mC", "mI", "oP", "oA", "oB", "oC", "oS", "oF", "oI", "tP", "tC", "tI", "tF", "hP", "hR", "cP", "cF", "cI" ]
        listSpaceGroup = [ "P1", "P2", "C2", "C2", "P222", "C222", "C222", "C222", "C222", "F222", "I222", "P4", "P4", "I4", "I4", "P3", "H3", "P23", "F23", "I23" ]
        for iIndex in range(len(listBravaisLattice)):
            EDAssert.equal(listSpaceGroup[ iIndex ], EDUtilsSymmetry.getMinimumSymmetrySpaceGroupFromBravaisLattice(listBravaisLattice[ iIndex]))

    def testGetITNumberFromSpaceGroupName(self):
        EDAssert.equal(1, EDUtilsSymmetry.getITNumberFromSpaceGroupName("P1"), "ITNumber from space group P1")
        EDAssert.equal(3, EDUtilsSymmetry.getITNumberFromSpaceGroupName("P2"), "ITNumber from space group P2")
        EDAssert.equal(5, EDUtilsSymmetry.getITNumberFromSpaceGroupName("C2"), "ITNumber from space group C2")
        EDAssert.equal(16, EDUtilsSymmetry.getITNumberFromSpaceGroupName("P222"), "ITNumber from space group P222")
        EDAssert.equal(21, EDUtilsSymmetry.getITNumberFromSpaceGroupName("C222"), "ITNumber from space group C222")
        EDAssert.equal(22, EDUtilsSymmetry.getITNumberFromSpaceGroupName("F222"), "ITNumber from space group F222")
        EDAssert.equal(75, EDUtilsSymmetry.getITNumberFromSpaceGroupName("P4"), "ITNumber from space group P4")
        EDAssert.equal(79, EDUtilsSymmetry.getITNumberFromSpaceGroupName("I4"), "ITNumber from space group I4")
        EDAssert.equal(143, EDUtilsSymmetry.getITNumberFromSpaceGroupName("P3"), "ITNumber from space group P3")
        EDAssert.equal(146, EDUtilsSymmetry.getITNumberFromSpaceGroupName("H3"), "ITNumber from space group H3")
        EDAssert.equal(195, EDUtilsSymmetry.getITNumberFromSpaceGroupName("P23"), "ITNumber from space group P23")
        EDAssert.equal(196, EDUtilsSymmetry.getITNumberFromSpaceGroupName("F23"), "ITNumber from space group F23")

    def testGetSpaceGroupNameFromITNumber(self):
        EDAssert.equal("P1", EDUtilsSymmetry.getSpaceGroupNameFromITNumber(1), "Space group from from it number 1")
        EDAssert.equal("P2", EDUtilsSymmetry.getSpaceGroupNameFromITNumber(3), "Space group from from it number 3")
        EDAssert.equal("C2", EDUtilsSymmetry.getSpaceGroupNameFromITNumber(5), "Space group from from it number 5")
        EDAssert.equal("P222", EDUtilsSymmetry.getSpaceGroupNameFromITNumber(16), "Space group from from it number 16")
        EDAssert.equal("C222", EDUtilsSymmetry.getSpaceGroupNameFromITNumber(21), "Space group from from it number 21")
        EDAssert.equal("F222", EDUtilsSymmetry.getSpaceGroupNameFromITNumber(22), "Space group from from it number 22")
        EDAssert.equal("P4", EDUtilsSymmetry.getSpaceGroupNameFromITNumber(75), "Space group from from it number 75")
        EDAssert.equal("I4", EDUtilsSymmetry.getSpaceGroupNameFromITNumber(79), "Space group from from it number 79")
        EDAssert.equal("P3", EDUtilsSymmetry.getSpaceGroupNameFromITNumber(143), "Space group from from it number 143")
        EDAssert.equal("H3", EDUtilsSymmetry.getSpaceGroupNameFromITNumber(146), "Space group from from it number 146")
        EDAssert.equal("P23", EDUtilsSymmetry.getSpaceGroupNameFromITNumber(195), "Space group from from it number 195")
        EDAssert.equal("F23", EDUtilsSymmetry.getSpaceGroupNameFromITNumber(196), "Space group from from it number 196")


    def process(self):
        self.addTestMethod(self.testGetMinimumSymmetrySpaceGroupFromBravaisLattice)
        self.addTestMethod(self.testGetITNumberFromSpaceGroupName)
        self.addTestMethod(self.testGetSpaceGroupNameFromITNumber)


if __name__ == '__main__':

    edTestCaseEDUtilsSymmetry = EDTestCaseEDUtilsSymmetry("TestCase EDTestCaseEDUtilsSymmetry")
    edTestCaseEDUtilsSymmetry.execute()
