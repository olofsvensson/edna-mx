# coding: utf8
#
#    Project: <projectName>
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

__author__="Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"
__date__ = "20120712"
__status__ = "production"

import os


from EDAssert                            import EDAssert
from EDTestCasePluginExecute             import EDTestCasePluginExecute


class EDTestCasePluginExecuteMXThumbnailv1_1(EDTestCasePluginExecute):
    
    def __init__(self, _strTestName = None):
        EDTestCasePluginExecute.__init__(self, "EDPluginMXThumbnailv1_1")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputMXThumbnail_reference.xml"))
                 
    def preProcess(self):
        EDTestCasePluginExecute.preProcess(self)
        self.loadTestImage([ "ref-testscale_1_001.img" ])
        
    def testExecute(self):
        self.run()
        # Check that thumbnail image has been generated
        edPlugin = self.getPlugin()
        thumbnailPath = edPlugin.dataOutput.thumbnail.path.value
        EDAssert.equal(True, os.path.exists(thumbnailPath), "Thumbnail path exists")
        

    def process(self):
        self.addTestMethod(self.testExecute)

        
