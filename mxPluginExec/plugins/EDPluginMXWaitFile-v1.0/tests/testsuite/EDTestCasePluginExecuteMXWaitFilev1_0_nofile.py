#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) ESRF
#
#    Principal author:       Jerome Kieffer
#
#    Contributing author:    Olof Svensson
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

__author__ = "Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os

from EDVerbose                                  import EDVerbose
from EDAssert                                   import EDAssert
from EDTestCasePluginExecuteMXWaitFilev1_0      import EDTestCasePluginExecuteMXWaitFilev1_0


class EDTestCasePluginExecuteMXWaitFilev1_0_nofile(EDTestCasePluginExecuteMXWaitFilev1_0):
    """
    Those are all execution tests for the EDNA Exec plugin MXWaitFilev1_0
    """

    def __init__(self, _strTestName=None):
        """
        """

        EDTestCasePluginExecuteMXWaitFilev1_0.__init__(self, "EDPluginMXWaitFilev1_0")
        self.setConfigurationFile(os.path.join(self.getPluginTestsDataHome(),
                                               "XSConfiguration_MXWaitFile.xml"))
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputMXWaitFile_nofile.xml"))
        self.setReferenceDataOutputFile(os.path.join(self.getPluginTestsDataHome(), \
                                                     "XSDataResultMXWaitFile_nofile.xml"))
        tmpdir = "/tmp/edna-%s" % os.environ["USER"]
        if not os.path.isdir(tmpdir):
            os.mkdir(tmpdir)
        filename = os.path.join(tmpdir, "noFile")
        if os.path.isfile(filename):
            os.remove(filename)
