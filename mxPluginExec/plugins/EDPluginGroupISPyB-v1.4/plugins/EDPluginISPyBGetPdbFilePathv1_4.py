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
__date__ = "20161109"
__status__ = "production"

import os

from EDFactoryPluginStatic import EDFactoryPluginStatic

from EDPluginISPyBv1_4 import EDPluginISPyBv1_4

from suds.client import Client
from suds.transport.http import HttpAuthenticated
from suds.sax.date import DateTime

from XSDataCommon import XSDataString

from XSDataISPyBv1_4 import XSDataInputISPyBGetPdbFilePath
from XSDataISPyBv1_4 import XSDataResultISPyBGetPdbFilePath


class EDPluginISPyBGetPdbFilePathv1_4(EDPluginISPyBv1_4):
    """
    Plugin for rertrieving path to pdb file
    """

    def __init__(self):
        EDPluginISPyBv1_4.__init__(self)
        self.setXSDataInputClass(XSDataInputISPyBGetPdbFilePath)
        self.dataCollectionId = None
        self.strPathToPdbFile = None


    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginISPyBv1_4.configure(self, _bRequireToolsForCollectionWebServiceWsdl=True)




    def process(self, _edObject=None):
        """
        Uses ToolsForCollectionWebService 
        """
        EDPluginISPyBv1_4.process(self)
        self.DEBUG("EDPluginISPyBGetPdbFilePathv1_4.process")
        httpAuthenticatedToolsForCollectionWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForCollectionWebService = Client(self.strToolsForCollectionWebServiceWsdl, transport=httpAuthenticatedToolsForCollectionWebService)
        # Loop over all positions
        xsDataInputISPyBGetPdbFilePath = self.getDataInput()
        iDataCollectionId = self.getXSValue(xsDataInputISPyBGetPdbFilePath.dataCollectionId)
        self.strPathToPdbFile = clientToolsForCollectionWebService.service.getPdbFilePath(
                                    iDataCollectionId, \
                                    )
        self.DEBUG("EDPluginISPyBGetPdbFilePathv1_4.process: path to pdb file=%r" % self.strPathToPdbFile)





    def finallyProcess(self, _edObject=None):
        EDPluginISPyBv1_4.finallyProcess(self)
        self.DEBUG("EDPluginISPyBGetPdbFilePathv1_4.finallyProcess")
        xsDataResultISPyBGetPdbFilePath = XSDataResultISPyBGetPdbFilePath()
        if self.strPathToPdbFile is not None:
            xsDataResultISPyBGetPdbFilePath.pdbFilePath = XSDataString(self.strPathToPdbFile)
        self.setDataOutput(xsDataResultISPyBGetPdbFilePath)

