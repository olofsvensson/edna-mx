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
__date__ = "20160909"
__status__ = "production"

import os
import json
import datetime

from EDPluginExec import EDPluginExec
from EDFactoryPluginStatic import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallJurkoSuds94664ddd46a6")
from suds.client import Client
from suds.transport.http import HttpAuthenticated
from suds.sax.date import DateTime

from XSDataCommon import XSDataInteger

from XSDataISPyBv1_4 import XSDataInputISPyBStoreWorkflowStep
from XSDataISPyBv1_4 import XSDataResultISPyBStoreWorkflowStep


class EDPluginISPyBStoreWorkflowStepv1_4(EDPluginExec):
    """
    Plugin to store workflow step in an ISPyB database using web services
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputISPyBStoreWorkflowStep)
        self.strUserName = None
        self.strPassWord = None
        self.strToolsForCollectionWebServiceWsdl = None
        self.iWorkflowStepId = None


    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginExec.configure(self)
        self.strUserName = str(self.config.get("userName"))
        if self.strUserName is None:
            self.ERROR("EDPluginISPyBStoreWorkflowStepv1_4.configure: No user name found in configuration!")
            self.setFailure()
        self.strPassWord = str(self.config.get("passWord"))
        if self.strPassWord is None:
            self.ERROR("EDPluginISPyBStoreWorkflowStepv1_4.configure: No pass word found in configuration!")
            self.setFailure()
        self.strToolsForCollectionWebServiceWsdl = self.config.get("toolsForCollectionWebServiceWsdl")
        if self.strToolsForCollectionWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreWorkflowStepv1_4.configure: No toolsForCollectionWebServiceWsdl found in configuration!")
            self.setFailure()

    def getXSValue(self, _xsData, _oDefaultValue=None, _iMaxStringLength=255):
        if _xsData is None:
            oReturnValue = _oDefaultValue
        else:
            oReturnValue = _xsData.value
        if type(oReturnValue) == bool:
            if oReturnValue:
                oReturnValue = "1"
            else:
                oReturnValue = "0"
        elif (type(oReturnValue) == str) or (type(oReturnValue) == unicode):
            if len(oReturnValue) > _iMaxStringLength:
                strOldString = oReturnValue
                oReturnValue = oReturnValue[0:_iMaxStringLength - 3] + "..."
                self.warning("String truncated to %d characters for ISPyB! Original string: %s" % (_iMaxStringLength, strOldString))
                self.warning("Truncated string: %s" % oReturnValue)
        return oReturnValue


    def getDateValue(self, _strValue, _strFormat, _oDefaultValue):
        if _strValue is None or _strValue == "None":
            oReturnValue = _oDefaultValue
        else:
            oReturnValue = DateTime(datetime.datetime.strptime(_strValue, _strFormat))
        return oReturnValue

    def process(self, _edObject=None):
        """
        Uses ToolsForCollectionWebService for storing the workflow status
        """
        EDPluginExec.process(self)
        self.DEBUG("EDPluginISPyBStoreWorkflowStepv1_4.process")
        # First get the image ID
        httpAuthenticatedToolsForCollectionWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForCollectionWebService = Client(self.strToolsForCollectionWebServiceWsdl, transport=httpAuthenticatedToolsForCollectionWebService)
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
        EDPluginExec.finallyProcess(self)
        self.DEBUG("EDPluginISPyBStoreWorkflowStepv1_4.finallyProcess")
        xsDataResultISPyBStoreWorkflowStep = XSDataResultISPyBStoreWorkflowStep()
        if self.iWorkflowStepId is not None:
            xsDataResultISPyBStoreWorkflowStep.workflowStepId = XSDataInteger(self.iWorkflowStepId)
        self.setDataOutput(xsDataResultISPyBStoreWorkflowStep)
