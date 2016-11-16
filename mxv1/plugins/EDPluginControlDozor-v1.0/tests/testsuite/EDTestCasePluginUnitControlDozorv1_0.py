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
import pprint

from EDAssert import EDAssert
from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataCommon import XSDataImage

from XSDataControlDozorv1_0 import XSDataInputControlDozor

class EDTestCasePluginUnitControlDozorv1_0(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlDozorv1_0")


    def testCreateDict(self):
        pathToReferenceInput = os.path.join(self.getPluginTestsDataHome(), \
                                            "XSDataInputControlDozor_reference.xml")
        xsDataInputControlDozor = XSDataInputControlDozor.parseFile(pathToReferenceInput)
        edPluginControlDozor = self.createPlugin()
        dictImage = edPluginControlDozor.createImageDict(xsDataInputControlDozor)
        EDAssert.equal(True, type(dictImage) == dict)

    def testCreateListOfBatches(self):
        edPluginControlDozor = self.createPlugin()
        EDAssert.equal([[1], [2], [3], [4], [5]], edPluginControlDozor.createListOfBatches(range(1, 6), 1))
        EDAssert.equal([[1, 2], [3, 4], [5]], edPluginControlDozor.createListOfBatches(range(1, 6), 2))
        EDAssert.equal([[1, 2, 3], [4, 5]], edPluginControlDozor.createListOfBatches(range(1, 6), 3))
        EDAssert.equal([[1, 2, 3, 4], [5]], edPluginControlDozor.createListOfBatches(range(1, 6), 4))
        EDAssert.equal([[1, 2, 3, 4, 5]], edPluginControlDozor.createListOfBatches(range(1, 6), 5))
        EDAssert.equal([[1], [2], [4], [5], [6]], edPluginControlDozor.createListOfBatches(list(range(4, 7)) + list(range(1, 3)), 1))
        EDAssert.equal([[1, 2], [4, 5], [6]], edPluginControlDozor.createListOfBatches(list(range(4, 7)) + list(range(1, 3)), 2))
        EDAssert.equal([[1, 2], [4, 5, 6]], edPluginControlDozor.createListOfBatches(list(range(4, 7)) + list(range(1, 3)), 3))


    def process(self):
        self.addTestMethod(self.testCreateDict)
        self.addTestMethod(self.testCreateListOfBatches)


