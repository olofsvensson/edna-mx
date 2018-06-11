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
__date__ = "20161109"
__status__ = "production"

import os
import datetime

from EDFactoryPluginStatic import EDFactoryPluginStatic

from EDPluginISPyBv1_4 import EDPluginISPyBv1_4

from suds.client import Client
from suds.transport.http import HttpAuthenticated
from suds.sax.date import DateTime

from XSDataCommon import XSDataInteger

from XSDataISPyBv1_4 import XSDataInputStoreAutoProcProgramAttachment
from XSDataISPyBv1_4 import XSDataResultStoreAutoProcProgramAttachment


class EDPluginISPyBStoreAutoProcProgramAttachmentv1_4(EDPluginISPyBv1_4):
    """
    Plugin to store results in an ISPyB database using web services
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginISPyBv1_4.__init__(self)
        self.setXSDataInputClass(XSDataInputStoreAutoProcProgramAttachment)
        self.setDataOutput(XSDataResultStoreAutoProcProgramAttachment())


    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginISPyBv1_4.configure(self, _bRequireToolsForAutoprocessingWebServiceWsdl=True)


    def process(self, _edObject=None):
        """
        Stores the contents of the AutoProcContainer in ISPyB.
        """
        EDPluginISPyBv1_4.process(self)
        self.DEBUG("EDPluginISPyBStoreAutoProcProgramAttachmentv1_4.process")
        xsDataInputStoreAutoProcProgramAttachment = self.getDataInput()
        httpAuthenticatedToolsForAutoprocessingWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForAutoprocessingWebService = Client(self.strToolsForAutoprocessingWebServiceWsdl,
                                                        transport=httpAuthenticatedToolsForAutoprocessingWebService,
                                                        cache=None)
        # AutoProcProgramAttachment
        listAutoProcProgramAttachment = xsDataInputStoreAutoProcProgramAttachment.getAutoProcProgramAttachment()
        for xsDataAutoProcProgramAttachment in listAutoProcProgramAttachment:
            iAutoProcProgramAttachmentId = self.storeOrUpdateAutoProcProgramAttachment(clientToolsForAutoprocessingWebService, xsDataAutoProcProgramAttachment)
            self.dataOutput.addAutoProcProgramAttachmentId(XSDataInteger(iAutoProcProgramAttachmentId))


    def finallyProcess(self, _edObject=None):
        EDPluginISPyBv1_4.finallyProcess(self)
        self.DEBUG("EDPluginISPyBStoreAutoProcProgramAttachmentv1_4.finallyProcess")



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


