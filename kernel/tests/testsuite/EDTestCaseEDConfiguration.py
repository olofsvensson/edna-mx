#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
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


"""
This is the test case for the EDConfiguration class.
"""

import os

from EDAssert                import EDAssert
from EDConfiguration         import EDConfiguration
from EDConfigurationStatic   import EDConfigurationStatic
from EDUtilsTest             import EDUtilsTest
from EDUtilsPath             import EDUtilsPath
from EDTestCase              import EDTestCase

from XSDataCommon import XSPluginItem

class EDTestCaseEDConfiguration(EDTestCase):


    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, "EDTestCaseEDConfiguration")
        strKernelDataHome = EDUtilsTest.getPluginTestDataDirectory(self.getClassName())
        strDataDir = "EDConfiguration"
        self.strDataPath = EDUtilsPath.mergePath(strKernelDataHome, strDataDir)
        self.strEdnaSiteOrig = EDUtilsPath.getEdnaSite()


    def preProcess(self):
        """Set EDNA_SITE to TestSite for these tests"""
        EDUtilsPath.setEdnaSite("TestSite")


    def testAddConfigFile(self):
        # Tests adding a config file
        strPath = os.path.join(self.strDataPath, "XSConfiguration.xml")
        edConfiguration = EDConfiguration()
        edConfiguration.addConfigurationFile(strPath)
        # Load the config file again, this time the cache should be used
        edConfiguration.addConfigurationFile(strPath)


    def testGetPathToProjectConfigurationFile(self):
        edConfiguration = EDConfiguration()
        strPathToConfigurationFile1 = edConfiguration.getPathToProjectConfigurationFile("EDPluginTestPluginFactory")
        strPathToConfigurationFileReference1 = EDUtilsPath.appendListOfPaths(EDUtilsPath.getEdnaHome(),
                                                                                  [ "kernel", "tests", "data", "EDFactoryPlugin", \
                                                                                   "testProject", "conf", "XSConfiguration_TestSite.xml" ])
        EDAssert.equal(strPathToConfigurationFileReference1, strPathToConfigurationFile1)
        EDUtilsPath.setEdnaSite("NonexistingTestSite")
        strPathToConfigurationFile2 = edConfiguration.getPathToProjectConfigurationFile("EDPluginTestPluginFactory")
        strPathToConfigurationFileReference2 = None
        EDAssert.equal(strPathToConfigurationFileReference2, strPathToConfigurationFile2)


    def finallyProcess(self):
        """Restores EDNA_SITE"""
        EDUtilsPath.setEdnaSite(self.strEdnaSiteOrig)



    def testGetPluginListSize(self):
        """
        Testing the retrieved XSPluginList size from configuration
        """
        strPath = os.path.join(self.strDataPath, "XSConfiguration.xml")
        edConfiguration = EDConfiguration()
        edConfiguration.addConfigurationFile(strPath)
        iPluginListSize = edConfiguration.getPluginListSize()
        EDAssert.equal(1, iPluginListSize)


    def process(self):
        self.addTestMethod(self.testAddConfigFile)
        self.addTestMethod(self.testGetPathToProjectConfigurationFile)
        self.addTestMethod(self.testGetPluginListSize)


if __name__ == '__main__':

    edTestCaseEDConfiguration = EDTestCaseEDConfiguration("EDTestCaseEDConfiguration")
    edTestCaseEDConfiguration.execute()
