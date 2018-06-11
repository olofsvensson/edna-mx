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

from XSDataCommon import XSDataInteger

from XSDataISPyBv1_4 import XSDataInputISPyBGroupDataCollections
from XSDataISPyBv1_4 import XSDataResultISPyBGroupDataCollections


class EDPluginISPyBGroupDataCollectionsv1_4(EDPluginISPyBv1_4):
    """
    Plugin to store workflow status in an ISPyB database using web services
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginISPyBv1_4.__init__(self)
        self.setXSDataInputClass(XSDataInputISPyBGroupDataCollections)
        self.strToolsForCollectionWebServiceWsdl = None
        self.iWorkflowId = None


    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginISPyBv1_4.configure(self, _bRequireToolsForCollectionWebServiceWsdl=True)


    def process(self, _edObject=None):
        """
        Uses ToolsForCollectionWebService for storing the workflow status
        """
        EDPluginISPyBv1_4.process(self)
        self.DEBUG("EDPluginISPyBGroupDataCollectionsv1_4.process")
        xsDataInput = self.getDataInput()
        arrayOfFileLocation = []
        arrayOfFileName = []
        for xsDataStringFilePath in xsDataInput.filePath:
            strFilePath = xsDataStringFilePath.value
            arrayOfFileLocation.append(os.path.dirname(strFilePath))
            arrayOfFileName.append(os.path.basename(strFilePath))
        httpAuthenticatedToolsForCollectionWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForCollectionWebService = Client(self.strToolsForCollectionWebServiceWsdl,
                                                    transport=httpAuthenticatedToolsForCollectionWebService,
                                                    cache=None)
        self.listDataCollectionIds = clientToolsForCollectionWebService.service.groupDataCollections(\
                dataCollectionGroupId=self.getXSValue(xsDataInput.dataCollectionGroupId), \
                arrayOfFileLocation=arrayOfFileLocation, \
                arrayOfFileName=arrayOfFileName, \
                )
        self.DEBUG("EDPluginISPyBGroupDataCollectionsv1_4.process: listDataCollectionIds=%r" % self.listDataCollectionIds)





    def finallyProcess(self, _edObject=None):
        EDPluginISPyBv1_4.finallyProcess(self)
        self.DEBUG("EDPluginISPyBGroupDataCollectionsv1_4.finallyProcess")
        xsDataResultISPyBGroupDataCollections = XSDataResultISPyBGroupDataCollections()
        for dataCollectionId in self.listDataCollectionIds:
            xsDataResultISPyBGroupDataCollections.addDataCollectionId(XSDataInteger(dataCollectionId))
        self.setDataOutput(xsDataResultISPyBGroupDataCollections)
