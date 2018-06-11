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
__date__ = "20161109"
__status__ = "production"

import os

from EDFactoryPluginStatic import EDFactoryPluginStatic

from EDPluginISPyBv1_4 import EDPluginISPyBv1_4

from suds.client import Client
from suds.transport.http import HttpAuthenticated
from suds.sax.date import DateTime

from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataFile

from XSDataISPyBv1_4 import XSDataInputUpdateSnapshots
from XSDataISPyBv1_4 import XSDataResultUpdateSnapshots
from XSDataISPyBv1_4 import XSDataISPyBDataCollection

class EDPluginISPyBUpdateSnapshotsv1_4(EDPluginISPyBv1_4):
    """
    Plugin to update a data collection entry in the ISPyB data base
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginISPyBv1_4.__init__(self)
        self.setXSDataInputClass(XSDataInputUpdateSnapshots)
        self.setDataOutput(XSDataResultUpdateSnapshots())
        self.dataCollectionId = None

    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginISPyBv1_4.configure(self, _bRequireToolsForCollectionWebServiceWsdl=True)


    def process(self, _edObject=None):
        """
        Upload the new content of data collection into ISPyB
        """
        EDPluginISPyBv1_4.process(self)
        self.DEBUG("EDPluginISPyBUpdateSnapshotsv1_4.process")

        httpAuthenticatedToolsForCollectionWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForCollectionWebService = Client(self.strToolsForCollectionWebServiceWsdl,
                                                    transport=httpAuthenticatedToolsForCollectionWebService,
                                                    cache=None)
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
        EDPluginISPyBv1_4.finallyProcess(self)
        self.DEBUG("EDPluginISPyBUpdateSnapshotsv1_4.finallyProcess")
        if self.dataCollectionId is not None:
            self.dataOutput.dataCollectionId = XSDataInteger(self.dataCollectionId)




