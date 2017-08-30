#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008 EMBL-Grenoble, Grenoble, France
#
#    Principal authors: Sandor Brockhauser (brockhauser@embl-grenoble.fr)
#                       Olof Svensson (svensson@esrf.fr)
#                       Pierre Legrand (pierre.legrand@synchrotron-soleil.fr)
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
__copyright__ = "ESRF"
__date__ = "20170829"
__status__ = "alpha"


import os
import pprint


from EDPluginXDSv1_0 import EDPluginXDSv1_0

from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

from XSDataXDSv1_0 import XSDataCell
from XSDataXDSv1_0 import XSDataInputXDSIntegration
from XSDataXDSv1_0 import XSDataResultXDSIntegration


class EDPluginXDSIntegrationv1_0(EDPluginXDSv1_0):


    def __init__(self):
        EDPluginXDSv1_0.__init__(self)
        self.setXSDataInputClass(XSDataInputXDSIntegration)
        self.dataOutput = XSDataResultXDSIntegration()

    def configure(self):
        EDPluginXDSv1_0.configure(self)
        self.DEBUG("EDPluginXDSIntegrationv1_0.configure")
        self.addJob("DEFPIX")
        self.addJob("INTEGRATE")
        self.addJob("CORRECT")


    def postProcess(self, _edObject=None):
        EDPluginXDSv1_0.postProcess(self)
        self.DEBUG("EDPluginXDSIntegrationv1_0.postProcess")

        correctLp = os.path.join(self.getWorkingDirectory(), "CORRECT.LP")
        if os.path.exists(correctLp):
            self.dataOutput.correctLp = XSDataFile(XSDataString(correctLp))

        bkgpixCbf = os.path.join(self.getWorkingDirectory(), "BKGPIX.cbf")
        if os.path.exists(bkgpixCbf):
            self.dataOutput.bkgpixCbf = XSDataFile(XSDataString(bkgpixCbf))

        xdsAsciiHkl = os.path.join(self.getWorkingDirectory(), "XDS_ASCII.HKL")
        if os.path.exists(xdsAsciiHkl):
            self.dataOutput.xdsAsciiHkl = XSDataFile(XSDataString(xdsAsciiHkl))


