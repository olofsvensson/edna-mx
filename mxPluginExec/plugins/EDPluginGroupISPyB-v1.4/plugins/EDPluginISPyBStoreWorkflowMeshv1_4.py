#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2011-2014 European Synchrotron Radiation Facility
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

from XSDataISPyBv1_4 import XSDataInputISPyBStoreWorkflowMesh
from XSDataISPyBv1_4 import XSDataResultISPyBStoreWorkflowMesh


class EDPluginISPyBStoreWorkflowMeshv1_4(EDPluginISPyBv1_4):
    """
    Plugin to store workflow status in an ISPyB database using web services
    """

    def __init__(self):
        """
        Init plugin
        """
        EDPluginISPyBv1_4.__init__(self)
        self.setXSDataInputClass(XSDataInputISPyBStoreWorkflowMesh)
        self.iWorkflowMeshId = None


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
        self.DEBUG("EDPluginISPyBStoreWorkflowMeshv1_4.process")
        # First get the image ID
        xsDataInputWorkflowMesh = self.getDataInput()

        httpAuthenticatedToolsForCollectionWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForCollectionWebService = Client(self.strToolsForCollectionWebServiceWsdl,
                                                    transport=httpAuthenticatedToolsForCollectionWebService,
                                                    cache=None)
        workflowMeshWS3VO = clientToolsForCollectionWebService.factory.create('workflowMeshWS3VO')
        workflowMeshWS3VO.workflowId = self.getXSValue(xsDataInputWorkflowMesh.workflowId)
        workflowMeshWS3VO.bestPositionId = self.getXSValue(xsDataInputWorkflowMesh.bestPositionId)
        workflowMeshWS3VO.bestImageId = self.getXSValue(xsDataInputWorkflowMesh.bestImageId)
        workflowMeshWS3VO.value1 = self.getXSValue(xsDataInputWorkflowMesh.value1)
        workflowMeshWS3VO.value2 = self.getXSValue(xsDataInputWorkflowMesh.value2)
        workflowMeshWS3VO.value3 = self.getXSValue(xsDataInputWorkflowMesh.value3)
        workflowMeshWS3VO.value4 = self.getXSValue(xsDataInputWorkflowMesh.value4)
        workflowMeshWS3VO.cartographyPath = self.getXSValue(xsDataInputWorkflowMesh.cartographyPath)
#        print workflowMeshWS3VO
        self.iWorkflowMeshId = clientToolsForCollectionWebService.service.storeOrUpdateWorkflowMesh(workflowMeshWS3VO)
        self.DEBUG("EDPluginISPyBStoreWorkflowMeshv1_4.process: WorkflowId=%d" % self.iWorkflowMeshId)





    def finallyProcess(self, _edObject=None):
        EDPluginISPyBv1_4.finallyProcess(self)
        self.DEBUG("EDPluginISPyBStoreWorkflowMeshv1_4.finallyProcess")
        xsDataResultISPyBStoreWorkflowMesh = XSDataResultISPyBStoreWorkflowMesh()
        if self.iWorkflowMeshId is not None:
            xsDataResultISPyBStoreWorkflowMesh.workflowMeshId = XSDataInteger(self.iWorkflowMeshId)
        self.setDataOutput(xsDataResultISPyBStoreWorkflowMesh)
