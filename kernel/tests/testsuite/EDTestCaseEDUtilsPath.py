# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Olof Svensson (svensson@esrf.fr)
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

"""
This is the test case for the EDUtilsFile static class.
"""


import os
import tempfile

from EDTestCase     import EDTestCase
from EDVerbose      import EDVerbose
from EDAssert       import EDAssert
from EDUtilsFile    import EDUtilsFile
from EDUtilsPath    import EDUtilsPath

class EDTestCaseEDUtilsPath(EDTestCase):


    def __init__(self, _strTestName=None):
        EDTestCase.__init__(self, "EDTestCaseEDUtilsPath")


    def testGetEdnaUserTempFolder(self):
        # Test that we can access the user temp folder
        strUserTempFolder = EDUtilsPath.getEdnaUserTempFolder()
        EDAssert.equal(True, os.path.exists(strUserTempFolder), "Checking that user temp folder exists")
        # Test if we can write to the temp folder
        strTest = "This is a test string."
        strPathTestFile = os.path.join(strUserTempFolder, "EDTestCaseEDUtilsPath_testFile.txt")
        EDUtilsFile.writeFile(strPathTestFile, strTest)
        EDAssert.equal(True, os.path.exists(strPathTestFile), "Checking that new temp file exists")
        # Delete the test file
        os.remove(strPathTestFile)
        
    def testSystemCopyFile(self):
        testText = "Test text"
        file1 = tempfile.NamedTemporaryFile(prefix="file1_")
        fileName1 = file1.name
        file1.close()
        with open(fileName1, "w") as f1:
            f1.write(testText)
        file2 = tempfile.NamedTemporaryFile(prefix="file2_")
        file2.close()
        fileName2 = file2.name
        EDUtilsPath.systemCopyFile(fileName1, fileName2)
        with open(fileName2) as f:
            file2Content = f.read()
        EDAssert.equal(testText, file2Content)

    def testSystemCopyTree(self):
        testText = "Test text"
        dir1 = tempfile.mkdtemp(prefix= "dir1_")
        testFileName = "test_file.txt"
        testFilePath1 = os.path.join(dir1, testFileName)
        with open(testFilePath1, "w") as f1:
            f1.write(testText)
        dir2 = tempfile.mkdtemp(prefix= "dir2_")
        EDUtilsPath.systemCopyTree(dir1, dir2, dirs_exists_ok=True)
        testFilePath2 = os.path.join(dir2, testFileName)
        with open(testFilePath2) as f:
            file2Content = f.read()
        EDAssert.equal(testText, file2Content)

    def testSystemRmTreeWithoutErrors(self):
        testText = "Test text"
        dir1 = tempfile.mkdtemp(prefix= "dir1_")
        testFileName = "test_file.txt"
        testFilePath1 = os.path.join(dir1, testFileName)
        with open(testFilePath1, "w") as f1:
            f1.write(testText)
        EDUtilsPath.systemRmTree(dir1, ignore_errors=False)

    def testSystemRmTreeWithErrors(self):
        # try with ignore_errors=False
        dir1 = "/a/path/which/does/not/exists"
        try:
            EDUtilsPath.systemRmTree(dir1, ignore_errors=False)
            exception_caught = False
        except Exception as e:
            exception_caught = True
        EDAssert.equal(True, exception_caught)
        # try with ignore_errors=True
        try:
            EDUtilsPath.systemRmTree(dir1, ignore_errors=True)
            exception_caught = False
        except Exception as e:
            exception_caught = True
        EDAssert.equal(False, exception_caught)



    def process(self):
        self.addTestMethod(self.testGetEdnaUserTempFolder)
        self.addTestMethod(self.testSystemCopyFile)
        self.addTestMethod(self.testSystemCopyTree)
        self.addTestMethod(self.testSystemRmTreeWithoutErrors)
        self.addTestMethod(self.testSystemRmTreeWithErrors)


if __name__ == '__main__':

    edTestCaseEDUtilsPath = EDTestCaseEDUtilsPath("EDTestCaseEDUtilsPath")
    edTestCaseEDUtilsPath.execute()
