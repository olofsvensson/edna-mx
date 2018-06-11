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

import os
import datetime

from EDFactoryPluginStatic import EDFactoryPluginStatic

from EDPluginISPyBv1_4 import EDPluginISPyBv1_4

from suds.client import Client
from suds.transport.https import HttpAuthenticated
from suds.sax.date import DateTime

from XSDataISPyBv1_4 import XSDataInputStoreAutoProcStatus
from XSDataISPyBv1_4 import XSDataResultStoreAutoProcStatus


class EDPluginISPyBStoreAutoProcStatusv1_4(EDPluginISPyBv1_4):
    """
    Plugin to store results in an ISPyB database using web services
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginISPyBv1_4.__init__(self)
        self.setXSDataInputClass(XSDataInputStoreAutoProcStatus)
        self.iAutoProcIntegrationId = None
        self.iAutoProcStatusId = None
        self.iAutoProcProgramId = None
        self.bAnomalous = False


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
        iDataCollectionId = None
        self.DEBUG("EDPluginISPyBStoreAutoProcStatusv1_4.process")
        httpAuthenticatedToolsForAutoprocessingWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForAutoprocessingWebService = Client(self.strToolsForAutoprocessingWebServiceWsdl,
                                                        transport=httpAuthenticatedToolsForAutoprocessingWebService,
                                                        cache=None)
        xsDataInputStoreAutoProcStatus = self.getDataInput()
        if xsDataInputStoreAutoProcStatus.dataCollectionId is not None:
            iDataCollectionId = xsDataInputStoreAutoProcStatus.dataCollectionId
        if xsDataInputStoreAutoProcStatus.autoProcIntegrationId is not None:
            self.iAutoProcIntegrationId = xsDataInputStoreAutoProcStatus.autoProcIntegrationId
        if xsDataInputStoreAutoProcStatus.autoProcStatusId is not None:
            self.iAutoProcStatusId = xsDataInputStoreAutoProcStatus.autoProcStatusId
        if xsDataInputStoreAutoProcStatus.anomalous is not None:
            self.bAnomalous = xsDataInputStoreAutoProcStatus.anomalous
        # If autoProcIntegrationId is not given a dataCollectionId must be present:
        if (self.iAutoProcIntegrationId is None) and (iDataCollectionId is None):
            strErrorMessage = "Either data collection id or auto proc integration id must be given as input!"
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
        else:
            if self.iAutoProcIntegrationId is None:
                # Check if we have AutoProcProgram
                xsDataAutoProcProgram = xsDataInputStoreAutoProcStatus.AutoProcProgram
                if xsDataAutoProcProgram is not None:
                    iAutoProcProgramId = self.getXSValue(xsDataAutoProcProgram.getAutoProcProgramId())
                    strProcessingCommandLine = self.getXSValue(xsDataAutoProcProgram.getProcessingCommandLine())
                    strProcessingPrograms = self.getXSValue(xsDataAutoProcProgram.getProcessingPrograms())
                    strProcessingStatus = self.getXSValue(xsDataAutoProcProgram.getProcessingStatus(), "SUCCESS")
                    if strProcessingStatus == "true" or strProcessingStatus == "1":
                        strProcessingStatus = "SUCCESS"
                    elif strProcessingStatus == "false" or strProcessingStatus == "0":
                        strProcessingStatus = "FAILED"
                    strProcessingMessage = self.getXSValue(xsDataAutoProcProgram.getProcessingMessage())
                    processingStartTime = self.getDateValue(xsDataAutoProcProgram.getProcessingStartTime(), "%a %b %d %H:%M:%S %Y", DateTime(datetime.datetime.now()))
                    processingEndTime = self.getDateValue(xsDataAutoProcProgram.getProcessingEndTime(), "%a %b %d %H:%M:%S %Y", DateTime(datetime.datetime.now()))
                    strProcessingEnvironment = self.getXSValue(xsDataAutoProcProgram.getProcessingEnvironment())
                    recordTimeStamp = self.getDateValue(None, "%a %b %d %H:%M:%S %Y", DateTime(datetime.datetime.now()))
                    self.iAutoProcProgramId = clientToolsForAutoprocessingWebService.service.storeOrUpdateAutoProcProgram(
                        arg0=iAutoProcProgramId, \
                        processingCommandLine=strProcessingCommandLine, \
                        processingPrograms=strProcessingPrograms, \
                        processingStatus=strProcessingStatus, \
                        processingMessage=strProcessingMessage, \
                        processingStartTime=processingStartTime, \
                        processingEndTime=processingEndTime, \
                        processingEnvironment=strProcessingEnvironment, \
                        recordTimeStamp=recordTimeStamp
                        )
                else:
                    self.iAutoProcProgramId = None
                self.DEBUG("iAutoProcProgramId: {0}".format(self.iAutoProcProgramId))
                # If no autoProcessingId is given create a dummy entry in the integration table
                self.iAutoProcIntegrationId = self.storeOrUpdateAutoProcIntegration(clientToolsForAutoprocessingWebService,
                                                                               _iDataCollectionId=iDataCollectionId,
                                                                               _iAutoProcProgramId=self.iAutoProcProgramId, \
                                                                               _bAnomalous=self.bAnomalous)
            # Store the AutoProcStatus
            self.iAutoProcStatusId = self.storeOrUpdateAutoProcStatus(clientToolsForAutoprocessingWebService, \
                                                                 _xsDataAutoProcStatus=xsDataInputStoreAutoProcStatus.getAutoProcStatus(), \
                                                                 _iAutoProcIntegrationId=self.iAutoProcIntegrationId, \
                                                                 _iAutoProcStatusId=self.iAutoProcStatusId)

    def finallyProcess(self, _edObject=None):
        EDPluginISPyBv1_4.finallyProcess(self)
        self.DEBUG("EDPluginISPyBStoreAutoProcStatusv1_4.finallyProcess")
        xsDataResultStoreAutoProcStatus = XSDataResultStoreAutoProcStatus()
        xsDataResultStoreAutoProcStatus.setAutoProcIntegrationId(self.iAutoProcIntegrationId)
        xsDataResultStoreAutoProcStatus.setAutoProcProgramId(self.iAutoProcProgramId)
        xsDataResultStoreAutoProcStatus.setAutoProcStatusId(self.iAutoProcStatusId)
        self.setDataOutput(xsDataResultStoreAutoProcStatus)



    def storeOrUpdateAutoProcIntegration(self, _clientToolsForAutoprocessingWebService, \
                                         _iAutoProcIntegrationId=None, _iDataCollectionId=None,
                                         _iAutoProcProgramId=None, _bAnomalous=False):
        """Creates or updates an entry in the ISPyB AutoProcIntegration table"""
        recordTimeStamp = DateTime(datetime.datetime.now())
        iAutoProcIntegrationId = _clientToolsForAutoprocessingWebService.service.storeOrUpdateAutoProcIntegration(
                arg0=_iAutoProcIntegrationId, \
                recordTimeStamp=recordTimeStamp, \
                dataCollectionId=_iDataCollectionId, \
                autoProcProgramId=_iAutoProcProgramId, \
                anomalous=_bAnomalous, \
                )
        self.DEBUG("AutoProcProgramIntegrationId: %r" % iAutoProcIntegrationId)
        return iAutoProcIntegrationId


    def storeOrUpdateAutoProcStatus(self, _clientToolsForAutoprocessingWebService, \
                                    _xsDataAutoProcStatus, _iAutoProcIntegrationId, _iAutoProcStatusId=None):
        """Creates or updates an entry in the ISPyB AutoProcIntegration table"""
        strStep = self.getXSValue(_xsDataAutoProcStatus.getStep())
        strStatus = self.getXSValue(_xsDataAutoProcStatus.getStatus())
        strComments = self.getXSValue(_xsDataAutoProcStatus.getComments(), _iMaxStringLength=1024)
        strBltimeStamp = DateTime(datetime.datetime.now())
        iAutoProcIntegrationId = _clientToolsForAutoprocessingWebService.service.storeOrUpdateAutoProcStatus(
                arg0=_iAutoProcStatusId, \
                autoProcIntegrationId=_iAutoProcIntegrationId, \
                step=strStep, \
                status=strStatus, \
                comments=strComments, \
                bltimeStamp=strBltimeStamp, \
                )
        self.DEBUG("AutoProcProgramStatusId: %r" % iAutoProcIntegrationId)
        return iAutoProcIntegrationId

