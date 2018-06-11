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

from XSDataISPyBv1_4 import XSDataInputStoreListOfImageQualityIndicators
from XSDataISPyBv1_4 import XSDataResultStoreListOfImageQualityIndicators


class EDPluginISPyBStoreListOfImageQualityIndicatorsv1_4(EDPluginISPyBv1_4):
    """
    Plugin to store results in an ISPyB database using web services
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginISPyBv1_4.__init__(self)
        self.setXSDataInputClass(XSDataInputStoreListOfImageQualityIndicators)
        self.listImageQualityIndicatorsId = []
        self.iAutoProcProgramId = None


    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginISPyBv1_4.configure(self,
                                    _bRequireToolsForCollectionWebServiceWsdl=True,
                                    _bRequireToolsForAutoprocessingWebServiceWsdl=True)




    def process(self, _edObject=None):
        """
        First uses the ImageService to find the imageId.
        Then uses ToolsForCollectionWebService for storing the image quality indicators.
        """
        EDPluginISPyBv1_4.process(self)
        self.DEBUG("EDPluginISPyBStoreListOfImageQualityIndicatorsv1_4.process")
        httpAuthenticatedToolsForAutoprocessingWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForAutoprocessingWebService = Client(self.strToolsForAutoprocessingWebServiceWsdl,
                                                        transport=httpAuthenticatedToolsForAutoprocessingWebService,
                                                        cache=None)
        # Loop over all input image quality indicators:
        listImageQualityIndicatorsForWS = []
        for xsDataImageQualityIndicators in self.dataInput.imageQualityIndicators:
            # print xsDataImageQualityIndicators.marshal()
            imageQualityIndicatorsWS3VO = clientToolsForAutoprocessingWebService.factory.create('imageQualityIndicatorsWS3VO')
            strPathToImage = xsDataImageQualityIndicators.getImage().getPath().getValue()
            imageQualityIndicatorsWS3VO.fileName = os.path.basename(strPathToImage)
            imageQualityIndicatorsWS3VO.fileLocation = os.path.dirname(strPathToImage)
#            imageQualityIndicatorsWS3VO.imageId                       = 0
            imageQualityIndicatorsWS3VO.autoProcProgramId = self.iAutoProcProgramId
            imageQualityIndicatorsWS3VO.spotTotal = self.getXSValue(xsDataImageQualityIndicators.spotTotal)
            imageQualityIndicatorsWS3VO.inResTotal = self.getXSValue(xsDataImageQualityIndicators.inResTotal)
            imageQualityIndicatorsWS3VO.goodBraggCandidates = self.getXSValue(xsDataImageQualityIndicators.goodBraggCandidates)
            imageQualityIndicatorsWS3VO.iceRings = self.getXSValue(xsDataImageQualityIndicators.iceRings)
            imageQualityIndicatorsWS3VO.method1Res = self.getXSValue(xsDataImageQualityIndicators.method1Res)
            imageQualityIndicatorsWS3VO.method2Res = self.getXSValue(xsDataImageQualityIndicators.method2Res)
            imageQualityIndicatorsWS3VO.maxUnitCell = self.getXSValue(xsDataImageQualityIndicators.maxUnitCell)
            imageQualityIndicatorsWS3VO.pctSaturationTop50Peaks = self.getXSValue(xsDataImageQualityIndicators.pctSaturationTop50Peaks)
            imageQualityIndicatorsWS3VO.inResolutionOvrlSpots = self.getXSValue(xsDataImageQualityIndicators.inResolutionOvrlSpots)
            imageQualityIndicatorsWS3VO.binPopCutOffMethod2Res = self.getXSValue(xsDataImageQualityIndicators.binPopCutOffMethod2Res)
            imageQualityIndicatorsWS3VO.totalIntegratedSignal = self.getXSValue(xsDataImageQualityIndicators.totalIntegratedSignal)
            imageQualityIndicatorsWS3VO.dozor_score = self.getXSValue(xsDataImageQualityIndicators.dozor_score)
            imageQualityIndicatorsWS3VO.recordTimeStamp = DateTime(datetime.datetime.now())
            listImageQualityIndicatorsForWS.append(imageQualityIndicatorsWS3VO)
        self.listImageQualityIndicatorsId = clientToolsForAutoprocessingWebService.service.storeOrUpdateImageQualityIndicatorsForFileNames(
            listImageQualityIndicatorsForWS=listImageQualityIndicatorsForWS)
        self.DEBUG("EDPluginISPyBStoreListOfImageQualityIndicatorsv1_4.process: listImageQualityIndicatorsId=%r" % self.listImageQualityIndicatorsId)





    def finallyProcess(self, _edObject=None):
        EDPluginISPyBv1_4.finallyProcess(self)
        self.DEBUG("EDPluginISPyBStoreListOfImageQualityIndicatorsv1_4.finallyProcess")
        xsDataResultStoreListOfImageQualityIndicators = XSDataResultStoreListOfImageQualityIndicators()
        for iImageQualityIndicatorsId in self.listImageQualityIndicatorsId:
            xsDataResultStoreListOfImageQualityIndicators.addImageQualityIndicatorsId(XSDataInteger(iImageQualityIndicatorsId))
        self.setDataOutput(xsDataResultStoreListOfImageQualityIndicators)
