#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2011-2012 European Synchrotron Radiation Facility
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
__date__ = "20120712"
__status__ = "production"

import os, datetime

from EDPluginExec import EDPluginExec
from EDFactoryPluginStatic import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallSudsv0_4")
from suds.client import Client
from suds.transport.http import HttpAuthenticated
from suds.sax.date import DateTime

from XSDataCommon import XSDataInteger

from XSDataISPyBv1_4 import XSDataInputStoreAutoProcProgramAttachment
from XSDataISPyBv1_4 import XSDataResultStoreAutoProcProgramAttachment


class EDPluginISPyBStoreAutoProcProgramAttachmentv1_4(EDPluginExec):
    """
    Plugin to store results in an ISPyB database using web services
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputStoreAutoProcProgramAttachment)
        self.setDataOutput(XSDataResultStoreAutoProcProgramAttachment())
        self.strUserName = None
        self.strPassWord = None
        self.strToolsForAutoprocessingWebServiceWsdl = None
        
    
    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginExec.configure(self)
        self.strUserName = str(self.config.get("userName"))
        if self.strUserName is None:
            self.ERROR("EDPluginISPyBStoreAutoProcProgramAttachmentv1_4.configure: No user name found in configuration!")
            self.setFailure()
        self.strPassWord = str(self.config.get("passWord"))
        if self.strPassWord is None:
            self.ERROR("EDPluginISPyBStoreAutoProcProgramAttachmentv1_4.configure: No pass word found in configuration!")
            self.setFailure()
        self.strToolsForAutoprocessingWebServiceWsdl = self.config.get("toolsForAutoprocessingWebServiceWsdl")
        if self.strToolsForAutoprocessingWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreAutoProcProgramAttachmentv1_4.configure: No toolsForAutoprocessingWebServiceWsdl found in configuration!")
            self.setFailure()
                

    def process(self, _edObject=None):
        """
        Stores the contents of the AutoProcContainer in ISPyB.
        """
        EDPluginExec.process(self)
        self.DEBUG("EDPluginISPyBStoreAutoProcProgramAttachmentv1_4.process")
        xsDataInputStoreAutoProcProgramAttachment = self.getDataInput()
        httpAuthenticatedToolsForAutoprocessingWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForAutoprocessingWebService = Client(self.strToolsForAutoprocessingWebServiceWsdl, transport=httpAuthenticatedToolsForAutoprocessingWebService)
        # AutoProcProgramAttachment
        listAutoProcProgramAttachment = xsDataInputStoreAutoProcProgramAttachment.getAutoProcProgramAttachment()
        for xsDataAutoProcProgramAttachment in listAutoProcProgramAttachment:
            iAutoProcProgramAttachmentId = self.storeOrUpdateAutoProcProgramAttachment(clientToolsForAutoprocessingWebService, xsDataAutoProcProgramAttachment)
            self.dataOutput.addAutoProcProgramAttachmentId(XSDataInteger(iAutoProcProgramAttachmentId))


    def finallyProcess(self, _edObject=None):
        EDPluginExec.finallyProcess(self)
        self.DEBUG("EDPluginISPyBStoreAutoProcProgramAttachmentv1_4.finallyProcess")


    def getXSValue(self, _xsData, _oDefaultValue=None, _iMaxStringLength=255):
        if _xsData is None:
            oReturnValue = _oDefaultValue
        else:
            oReturnValue = _xsData
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
    


    def storeOrUpdateAutoProcProgramAttachment(self, _clientToolsForAutoprocessingWebService, _xsDataAutoProcProgramAttachment):
        """Creates an entry in the ISPyB AutoProcProgramAttachment table"""
        iAutoProcProgramAttachmentId = self.getXSValue(_xsDataAutoProcProgramAttachment.getAutoProcProgramAttachmentId())
        iAutoProcProgramId = self.getXSValue(_xsDataAutoProcProgramAttachment.getAutoProcProgramId())
        strFileType = self.getXSValue(_xsDataAutoProcProgramAttachment.getFileType())
        strFileName = self.getXSValue(_xsDataAutoProcProgramAttachment.getFileName())
        strFilePath = self.getXSValue(_xsDataAutoProcProgramAttachment.getFilePath())
        recordTimeStamp = DateTime(datetime.datetime.now())
        iAutoProcProgramAttachmentId = _clientToolsForAutoprocessingWebService.service.storeOrUpdateAutoProcProgramAttachment(
                arg0=iAutoProcProgramAttachmentId, \
                fileType=strFileType, \
                fileName=strFileName, \
                filePath=strFilePath, \
                recordTimeStamp=recordTimeStamp, \
                autoProcProgramId=iAutoProcProgramId
                )
        self.DEBUG("AutoProcProgramAttachmentId: %r" % iAutoProcProgramAttachmentId)
        return iAutoProcProgramAttachmentId


