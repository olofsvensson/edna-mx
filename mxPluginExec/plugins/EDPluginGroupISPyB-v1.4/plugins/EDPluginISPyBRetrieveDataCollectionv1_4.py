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


__author__ = "Thomas Boeglin"
__contact__ = "thomas.boeglin@esrf.fr"
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

from XSDataISPyBv1_4 import XSDataInputRetrieveDataCollection
from XSDataISPyBv1_4 import XSDataResultRetrieveDataCollection
from XSDataISPyBv1_4 import XSDataISPyBDataCollection

class EDPluginISPyBRetrieveDataCollectionv1_4(EDPluginISPyBv1_4):
    """
    Plugin to retrieve results in an ISPyB database using web services
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginISPyBv1_4.__init__(self)
        self.setXSDataInputClass(XSDataInputRetrieveDataCollection)
        self.collectParameters = None

    def configure(self):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginISPyBv1_4.configure(self, _bRequireToolsForCollectionWebServiceWsdl=True)


    def process(self, _edObject=None):
        """
        Retrieves the contents of the DataCollectionContainer in ISPyB
        """
        EDPluginISPyBv1_4.process(self)
        self.DEBUG("EDPluginISPyBRetrieveDataCollectionv1_4.process")
        infile = self.getDataInput()
        httpAuthenticatedToolsForCollectionWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForCollectionWebService = Client(self.strToolsForCollectionWebServiceWsdl,
                                                    transport=httpAuthenticatedToolsForCollectionWebService,
                                                    cache=None)
        self.collectParameters = None
        if infile.image is not None:
            inpath = infile.image.path.value
            indir = os.path.dirname(inpath)
            infilename = os.path.basename(inpath)
            collect_params = clientToolsForCollectionWebService.service.findDataCollectionFromFileLocationAndFileName(
                             indir,
                             infilename)
        elif infile.dataCollectionId is not None:
            dataCollectionId = infile.dataCollectionId.value
            collect_params = clientToolsForCollectionWebService.service.findDataCollection(dataCollectionId)
        else:
            self.ERROR("Neither image nor data collection id given as input!")
        if collect_params is None:
            self.ERROR("Couldn't find collect for image %s in ISPyB!" % inpath)
            self.setFailure()
        else:
            # the result is a suds.sudsobject.Object, we need to convert it
            res = XSDataISPyBDataCollection()
            try:
                for k, v in collect_params:
                    setattr(res, k, v)
            except:
                self.ERROR('something went wrong converting the result to a XSDataResultRetrieveDataCollection')
                self.setFailure()
            else:
                self.collectParameters = XSDataResultRetrieveDataCollection()
                self.collectParameters.dataCollection = res


    def finallyProcess(self, _edObject=None):
        EDPluginISPyBv1_4.finallyProcess(self)
        self.DEBUG("EDPluginISPyBRetrieveDataCollectionv1_4.finallyProcess")
        if self.collectParameters is None:
            self.collectParameters = XSDataResultRetrieveDataCollection()
        self.setDataOutput(self.collectParameters)


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


