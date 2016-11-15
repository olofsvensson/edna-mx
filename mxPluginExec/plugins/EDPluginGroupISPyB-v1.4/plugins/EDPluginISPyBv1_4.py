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
import sys
import datetime

from EDPluginExec import EDPluginExec
from EDFactoryPluginStatic import EDFactoryPluginStatic

if (sys.version_info > (3, 0)):
    EDFactoryPluginStatic.loadModule("EDInstallJurkoSuds94664ddd46a6Python3")
    PYTHON3 = True
else:
    EDFactoryPluginStatic.loadModule("EDInstallJurkoSuds94664ddd46a6")
    PYTHON3 = False


from suds.client import Client
from suds.transport.http import HttpAuthenticated
from suds.sax.date import DateTime


class EDPluginISPyBv1_4(EDPluginExec):
    """
    Abstract plugin for all ISPyBv1_4 plugins
    """

    def __init__(self):
        EDPluginExec.__init__(self)
        self.strUserName = None
        self.strPassWord = None
        self.strToolsForCollectionWebServiceWsdl = None
        self.strToolsForAutoprocessingWebServiceWsdl = None
        self.strToolsForBLSampleWebServiceWsdl = None
        self.strToolsForScreeningEDNAWebServiceWsdl = None


    def configure(self,
                  _bRequireToolsForCollectionWebServiceWsdl=False,
                  _bRequireToolsForAutoprocessingWebServiceWsdl=False,
                  _bRequireToolsForBLSampleWebServiceWsdl=False,
                  _bRequireToolsForScreeningEDNAWebServiceWsdl=False):
        """
        Gets the web servise wdsl parameters from the config file and stores them in class member attributes.
        """
        EDPluginExec.configure(self)
        self.strUserName = str(self.config.get("userName"))
        if self.strUserName is None:
            self.ERROR("{0}.configure: No user name found in configuration!".format(self.getName()))
            self.setFailure()
        self.strPassWord = str(self.config.get("passWord"))
        if self.strPassWord is None:
            self.ERROR("{0}.configure: No pass word found in configuration!")
            self.setFailure()
        self.strToolsForCollectionWebServiceWsdl = self.config.get("toolsForCollectionWebServiceWsdl")
        if _bRequireToolsForCollectionWebServiceWsdl and self.strToolsForCollectionWebServiceWsdl is None:
            self.ERROR("{0}.configure: No toolsForCollectionWebServiceWsdl found in configuration!")
            self.setFailure()
        self.strToolsForAutoprocessingWebServiceWsdl = self.config.get("toolsForAutoprocessingWebServiceWsdl")
        if _bRequireToolsForAutoprocessingWebServiceWsdl and self.strToolsForAutoprocessingWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreImageQualityIndicatorsv1_4.configure: No toolsForAutoprocessingWebServiceWsdl found in configuration!")
            self.setFailure()
        self.strToolsForBLSampleWebServiceWsdl = self.config.get("toolsForBLSampleWebServiceWsdl")
        if _bRequireToolsForBLSampleWebServiceWsdl and self.strToolsForBLSampleWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBGetSampleInformationv1_4.configure: No toolsForBLSampleWebServiceWsdl found in configuration!")
            self.setFailure()
        self.strToolsForScreeningEDNAWebServiceWsdl = self.config.get("toolsForScreeningEDNAWebServiceWsdl")
        if _bRequireToolsForScreeningEDNAWebServiceWsdl and self.strToolsForScreeningEDNAWebServiceWsdl is None:
            self.ERROR("EDPluginISPyBStoreScreeningv1_4.configure: No toolsForScreeningEDNAWebServiceWsdl found in configuration!")
            self.setFailure()

    def getValue(self, _oValue, _oDefaultValue=None):
        if _oValue is None:
            oReturnValue = _oDefaultValue
        else:
            oReturnValue = _oValue
        return oReturnValue

    def getXSValue(self, _xsData, _oDefaultValue=None, _iMaxStringLength=255):
        if _xsData is None:
            oReturnValue = _oDefaultValue
        elif (PYTHON3 and (type(_xsData) == str)) or (not PYTHON3 and ((type(_xsData) == str) or (type(_xsData) == unicode))):
            oReturnValue = _xsData
        elif type(_xsData) in [bool, int, float]:
            oReturnValue = _xsData
        else:
            oReturnValue = _xsData.value
        if type(oReturnValue) == bool:
            if oReturnValue:
                oReturnValue = "1"
            else:
                oReturnValue = "0"
        if (PYTHON3 and (type(oReturnValue) == str)) or (not PYTHON3 and ((type(oReturnValue) == str) or (type(oReturnValue) == unicode))):
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


