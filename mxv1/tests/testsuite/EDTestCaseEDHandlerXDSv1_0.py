#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Karl Levik (karl.levik@diamond.ac.uk)
#                            Olof Svensson (svensson@esrf.fr)
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

import os

from EDTestCase import EDTestCase
from EDUtilsTest import EDUtilsTest
from EDUtilsPath import EDUtilsPath
from EDAssert import EDAssert

class EDTestCaseEDHandlerXDSv1_0(EDTestCase):

    def __init__(self, _testName=None):
        EDTestCase.__init__(self, _testName)
        dataHome = EDUtilsTest.getPluginTestDataDirectory(self.getClassName())
        dataDir = "EDHandlerXDSv1_0"
        self.dataPath = os.path.join(dataHome, dataDir)


    def testGenerateXSDataInputXDSIndexing(self):
        filename = "XSDataIndexingInput_reference.xml"
        path = os.path.join(self.dataPath, filename)
        xmlIndexingInput = EDUtilsTest.readAndParseFile(path)
        from XSDataMXv1 import XSDataIndexingInput
        xsDataIndexingInput = XSDataIndexingInput.parseString(xmlIndexingInput)

        from EDHandlerXSDataXDSv1_0 import EDHandlerXSDataXDSv1_0
        xsDataInputXDSIndexing = EDHandlerXSDataXDSv1_0.generateXSDataInputXDSIndexing(xsDataIndexingInput)

        referenceFilename = "XSDataInputXDSIndexing_reference.xml"
        referencePath = os.path.join(self.dataPath, referenceFilename)
        xmlInputXDSIndexingReference = EDUtilsTest.readAndParseFile(referencePath)
        EDAssert.equal(xmlInputXDSIndexingReference, xsDataInputXDSIndexing.marshal())


    def process(self):
        self.addTestMethod(self.testGenerateXSDataInputXDSIndexing)


