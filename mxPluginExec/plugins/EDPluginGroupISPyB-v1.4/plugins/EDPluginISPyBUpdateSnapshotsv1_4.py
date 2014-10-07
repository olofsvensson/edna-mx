#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2011-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
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
__date__ = "20141006"
__status__ = "production"

import os, datetime

from EDPluginExec import EDPluginExec
from EDFactoryPluginStatic import EDFactoryPluginStatic

EDFactoryPluginStatic.loadModule("EDInstallSudsv0_4")
from suds.client import Client
from suds.transport.http import HttpAuthenticated
from suds.sax.date import DateTime

from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataFile

from XSDataISPyBv1_4 import XSDataInputUpdateSnapshots
from XSDataISPyBv1_4 import XSDataResultUpdateSnapshots
from XSDataISPyBv1_4 import XSDataISPyBDataCollection

class EDPluginISPyBUpdateSnapshotsv1_4(EDPluginExec):
    """
    Plugin to update a data collection entry in the ISPyB data base
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputUpdateSnapshots)
        self.setDataOutput(XSDataResultUpdateSnapshots())
        self.strUserName = None
        self.strPassWord = None
        self.strToolsForCollectionWebServiceWsdl = None
        self.dataCollectionId = None

    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginExec.configure(self)
        self.strUserName = str(self.config.get("userName"))
        if self.strUserName is None:
            self.ERROR("EDPluginISPyBRetrieveDataCollectionv1_4.configure: No user name found in configuration!")
            self.setFailure()
        self.strPassWord = str(self.config.get("passWord"))
        if self.strPassWord is None:
            self.ERROR("EDPluginISPyBRetrieveDataCollectionv1_4.configure: No pass word found in configuration!")
            self.setFailure()
        self.strToolsForCollectionWebServiceWsdl = self.config.get("toolsForCollectionWebServiceWsdl")
        if self.strToolsForCollectionWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBRetrieveDataCollectionv1_4.configure: No toolsForCollectionWebService found in configuration!")
            self.setFailure()


    def process(self, _edObject=None):
        """
        Upload the new content of data collection into ISPyB
        """
        EDPluginExec.process(self)
        self.DEBUG("EDPluginISPyBUpdateSnapshotsv1_4.process")

        httpAuthenticatedToolsForCollectionWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForCollectionWebService = Client(self.strToolsForCollectionWebServiceWsdl, transport=httpAuthenticatedToolsForCollectionWebService)
        self.collectParameters = None

        xsDataInput = self.getDataInput()
        
        strImagePath = xsDataInput.image.path.value
        fileLocation = os.path.dirname(strImagePath)
        fileName = os.path.basename(strImagePath)
        
        dataCollection = clientToolsForCollectionWebService.service.findDataCollectionFromFileLocationAndFileName(
                         fileLocation=fileLocation,
                         fileName=fileName)

        if dataCollection is not None:

            if xsDataInput.xtalSnapshotFullPath1 is not None:
                dataCollection.xtalSnapshotFullPath1 = xsDataInput.xtalSnapshotFullPath1.path.value      
            if xsDataInput.xtalSnapshotFullPath2 is not None:
                dataCollection.xtalSnapshotFullPath2 = xsDataInput.xtalSnapshotFullPath2.path.value        
            if xsDataInput.xtalSnapshotFullPath3 is not None:
                dataCollection.xtalSnapshotFullPath3 = xsDataInput.xtalSnapshotFullPath3.path.value
            if xsDataInput.xtalSnapshotFullPath4 is not None:
                dataCollection.xtalSnapshotFullPath4 = xsDataInput.xtalSnapshotFullPath4.path.value       
            
            self.dataCollectionId = clientToolsForCollectionWebService.service.storeOrUpdateDataCollection(
                             dataCollection=dataCollection)

        self.DEBUG("EDPluginISPyBUpdateSnapshotsv1_4.process: data collection id = %r" % self.dataCollectionId)


    def finallyProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginISPyBUpdateSnapshotsv1_4.finallyProcess")
        if self.dataCollectionId is not None:
            self.dataOutput.dataCollectionId = XSDataInteger(self.dataCollectionId)            


    def getValue(self, _oValue, _oDefaultValue=None):
        if _oValue is None:
            oReturnValue = _oDefaultValue
        else:
            oReturnValue = _oValue
        return oReturnValue


    def getDateValue(self, _strValue, _strFormat, _oDefaultValue):
        if _strValue is None:
            oReturnValue = _oDefaultValue
        else:
            try:
                oReturnValue = DateTime(datetime.datetime.strptime(_strValue, _strFormat))
            except:
                oReturnValue = DateTime(datetime.datetime.strptime(_strValue, _strFormat))
        return oReturnValue


