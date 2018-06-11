#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2011-2016 European Synchrotron Radiation Facility
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

from XSDataISPyBv1_4 import XSDataInputISPyBSetImageQualityIndicatorsPlot
from XSDataISPyBv1_4 import XSDataResultISPyBSetImageQualityIndicatorsPlot


class EDPluginISPyBSetImageQualityIndicatorsPlotv1_4(EDPluginISPyBv1_4):
    """
    Plugin to store motor positions (for grid scans)
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginISPyBv1_4.__init__(self)
        self.setXSDataInputClass(XSDataInputISPyBSetImageQualityIndicatorsPlot)
        self.dataCollectionId = None


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
        self.DEBUG("EDPluginISPyBSetImageQualityIndicatorsPlotv1_4.process")
        httpAuthenticatedToolsForCollectionWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForCollectionWebService = Client(self.strToolsForCollectionWebServiceWsdl,
                                                    transport=httpAuthenticatedToolsForCollectionWebService,
                                                    cache=None)
        # Loop over all positions
        xsDataInputISPyBSetImageQualityIndicatorsPlot = self.getDataInput()
        iDataCollectionId = self.getXSValue(xsDataInputISPyBSetImageQualityIndicatorsPlot.dataCollectionId)
        imageQualityIndicatorsPlotPath = self.getXSValue(xsDataInputISPyBSetImageQualityIndicatorsPlot.imageQualityIndicatorsPlotPath)
        imageQualityIndicatorsCSVPath = self.getXSValue(xsDataInputISPyBSetImageQualityIndicatorsPlot.imageQualityIndicatorsCSVPath)
        self.dataCollectionId = clientToolsForCollectionWebService.service.setImageQualityIndicatorsPlot(
                                    arg0=iDataCollectionId, \
                                    imageQualityIndicatorsPlotPath=imageQualityIndicatorsPlotPath, \
                                    imageQualityIndicatorsCSVPath=imageQualityIndicatorsCSVPath, \
                                    )
        self.DEBUG("EDPluginISPyBSetImageQualityIndicatorsPlotv1_4.process: dataCollectionId=%r" % self.dataCollectionId)





    def finallyProcess(self, _edObject=None):
        EDPluginISPyBv1_4.finallyProcess(self)
        self.DEBUG("EDPluginISPyBSetImageQualityIndicatorsPlotv1_4.finallyProcess")
        xsDataResultISPyBSetImageQualityIndicatorsPlot = XSDataResultISPyBSetImageQualityIndicatorsPlot()
        xsDataResultISPyBSetImageQualityIndicatorsPlot.dataCollectionId = XSDataInteger(self.dataCollectionId)
        self.setDataOutput(xsDataResultISPyBSetImageQualityIndicatorsPlot)


