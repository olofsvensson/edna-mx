#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
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
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20141217"
__status__ = "production"

import os

from EDAssert    import EDAssert
from EDUtilsTest import EDUtilsTest
from EDUtilsFile import EDUtilsFile

from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataPhenixv1_1 import XSDataResultPhenixXtriage

class EDTestCasePluginUnitPhenixXtriagev1_1(EDTestCasePluginUnit):


    def __init__(self, _pyStrTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginPhenixXtriagev1_1")


    def testParseLogFile(self):
        edPluginPhenixXtriagev1_1 = self.createPlugin()
        logFile = os.path.join(self.getPluginTestsDataHome(), "PhenixXtriage_noTwinning_noPseudotranslation.log")
        xsDataResultPhenixXtriage = edPluginPhenixXtriagev1_1.parseLogFile(logFile)
        # Check log file
        EDAssert.equal(True, os.path.exists(xsDataResultPhenixXtriage.logFile.path.value), "Log file")
        # Reference data
        xmlFile = os.path.join(self.getPluginTestsDataHome(), "XSDataResultPhenixXtriage_reference.xml")
        xml = self.readAndParseFile(xmlFile)        
        xsDataResultPhenixXtriageReference = XSDataResultPhenixXtriage.parseString(xml)
        # Remove the paths to the log file before comparison
        xsDataResultPhenixXtriage.logFile = None
        xsDataResultPhenixXtriageReference.logFile = None
        EDAssert.equal(xsDataResultPhenixXtriageReference.marshal(),
                       xsDataResultPhenixXtriage.marshal(), "Output values")

    def testParsePseudotranslationLogFile(self):        
        edPluginPhenixXtriagev1_1 = self.createPlugin()
        logFilePseudotranslation = os.path.join(self.getPluginTestsDataHome(), "PhenixXtriage_pseudotranslation.log")
        xsDataResultPhenixXtriage = edPluginPhenixXtriagev1_1.parseLogFile(logFilePseudotranslation)
        # Check log file
        EDAssert.equal(True, os.path.exists(xsDataResultPhenixXtriage.logFile.path.value), "Log file")
        # Reference data
        xmlFile = os.path.join(self.getPluginTestsDataHome(), "XSDataResultPhenixXtriage_pseudotranslation.xml")
        xml = self.readAndParseFile(xmlFile)        
        xsDataResultPhenixXtriageReference = XSDataResultPhenixXtriage.parseString(xml)
        # Remove the paths to the log file before comparison
        xsDataResultPhenixXtriage.logFile = None
        xsDataResultPhenixXtriageReference.logFile = None
        EDAssert.equal(xsDataResultPhenixXtriageReference.marshal(),
                       xsDataResultPhenixXtriage.marshal(), "Output values")


    def process(self):
        self.addTestMethod(self.testParseLogFile)
        self.addTestMethod(self.testParsePseudotranslationLogFile)


