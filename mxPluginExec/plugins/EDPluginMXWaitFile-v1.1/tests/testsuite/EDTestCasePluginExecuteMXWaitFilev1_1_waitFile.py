#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2011-2013 European Synchrotron Radiation Facility
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


__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20140623"

import os, tempfile, shutil, time

from threading import Timer

from EDAssert import EDAssert
from EDTestCasePluginExecute import EDTestCasePluginExecute
from EDUtilsPath import EDUtilsPath


class EDTestCasePluginExecuteMXWaitFilev1_1_waitFile(EDTestCasePluginExecute):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginMXWaitFilev1_1")
        self.strTmpDir = tempfile.mkdtemp(prefix="EDPluginMXWaitFilev1_1", dir=EDUtilsPath.getEdnaTestDataImagesPath())
        os.chmod(self.strTmpDir, 0o755)
        if "EDNA_TMP_DIR" in os.environ:
            self.strTmpDirOrig = os.environ["EDNA_TMP_DIR"]
        else:
            self.strTmpDirOrig = None
        os.environ["EDNA_TMP_DIR"] = self.strTmpDir
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputMXWaitFile_waitFile.xml"))
        self.strInputDataFile1 = os.path.join(self.getTestsDataImagesHome(), "ref-testscale_1_001.img")
        self.strInputDataFileNew1 = None


    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "ref-testscale_1_001.img" ])
        self.strInputDataFileNew1 = os.path.join(self.strTmpDir, "ref-testscale_1_001.img")


    def copyFile(self):
        self.screen("Copying file %s to %s" % (self.strInputDataFile1, self.strInputDataFileNew1))
        shutil.copyfile(self.strInputDataFile1, self.strInputDataFileNew1)


    def testExecute(self):
        # Start a timer for copying the file
        pyTimer = Timer(5, self.copyFile)
        pyTimer.start()
        self.run()
        pyTimer.cancel()
        # Check timeout
        edPlugin = self.getPlugin()
        EDAssert.equal(False, edPlugin.dataOutput.timedOut.value, "TimedOut should be False")
        time.sleep(1)
        shutil.rmtree(self.strTmpDir)
        if self.strTmpDirOrig is not None:
            os.environ["EDNA_TMP_DIR"] = self.strTmpDirOrig


    def process(self):
        self.addTestMethod(self.testExecute)


