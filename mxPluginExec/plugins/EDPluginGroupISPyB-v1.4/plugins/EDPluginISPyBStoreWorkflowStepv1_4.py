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
import json
import datetime

from EDFactoryPluginStatic import EDFactoryPluginStatic

from EDPluginISPyBv1_4 import EDPluginISPyBv1_4

from suds.client import Client
from suds.transport.http import HttpAuthenticated
from suds.sax.date import DateTime

from XSDataCommon import XSDataInteger

from XSDataISPyBv1_4 import XSDataInputISPyBStoreWorkflowStep
from XSDataISPyBv1_4 import XSDataResultISPyBStoreWorkflowStep


class EDPluginISPyBStoreWorkflowStepv1_4(EDPluginISPyBv1_4):
    """
    Plugin to store workflow step in an ISPyB database using web services
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginISPyBv1_4.__init__(self)
        self.setXSDataInputClass(XSDataInputISPyBStoreWorkflowStep)
        self.iWorkflowStepId = None


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
        self.DEBUG("EDPluginISPyBStoreWorkflowStepv1_4.process")
        # First get the image ID
        httpAuthenticatedToolsForCollectionWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForCollectionWebService = Client(self.strToolsForCollectionWebServiceWsdl,
                                                    transport=httpAuthenticatedToolsForCollectionWebService,
                                                    cache=None)
        dictWorkflowStep = {
            "workflowId"                  : self.getXSValue(self.dataInput.workflowId),
            "workflowStepType"            : self.getXSValue(self.dataInput.workflowStepType),
            "status"                      : self.getXSValue(self.dataInput.status),
            "folderPath"                  : self.getXSValue(self.dataInput.folderPath),
            "imageResultFilePath"         : self.getXSValue(self.dataInput.imageResultFilePath),
            "htmlResultFilePath"          : self.getXSValue(self.dataInput.htmlResultFilePath),
            "resultFilePath"              : self.getXSValue(self.dataInput.resultFilePath),
            "comments"                    : self.getXSValue(self.dataInput.comments),
            "crystalSizeX"                : self.getXSValue(self.dataInput.crystalSizeX),
            "crystalSizeY"                : self.getXSValue(self.dataInput.crystalSizeY),
            "crystalSizeZ"                : self.getXSValue(self.dataInput.crystalSizeZ),
            "maxDozorScore"               : self.getXSValue(self.dataInput.maxDozorScore),
         }
        strDictWorkflowStep = json.dumps(dictWorkflowStep)
        self.iWorkflowStepId = clientToolsForCollectionWebService.service.storeWorkflowStep(strDictWorkflowStep)
        self.DEBUG("EDPluginISPyBStoreWorkflowStepv1_4.process: WorkflowStepId = {0}".format(self.iWorkflowStepId))





    def finallyProcess(self, _edObject=None):
        EDPluginISPyBv1_4.finallyProcess(self)
        self.DEBUG("EDPluginISPyBStoreWorkflowStepv1_4.finallyProcess")
        xsDataResultISPyBStoreWorkflowStep = XSDataResultISPyBStoreWorkflowStep()
        if self.iWorkflowStepId is not None:
            xsDataResultISPyBStoreWorkflowStep.workflowStepId = XSDataInteger(self.iWorkflowStepId)
        self.setDataOutput(xsDataResultISPyBStoreWorkflowStep)
