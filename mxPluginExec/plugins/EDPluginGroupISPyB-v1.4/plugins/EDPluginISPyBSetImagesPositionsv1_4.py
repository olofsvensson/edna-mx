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

from EDFactoryPluginStatic import EDFactoryPluginStatic

from EDPluginISPyBv1_4 import EDPluginISPyBv1_4

from suds.client import Client
from suds.transport.http import HttpAuthenticated
from suds.sax.date import DateTime

from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataString
from XSDataCommon import XSDataBoolean

from XSDataISPyBv1_4 import XSDataInputISPyBSetImagesPositions
from XSDataISPyBv1_4 import XSDataResultISPyBSetImagesPositions
from XSDataISPyBv1_4 import XSDataISPyBImageCreation


class EDPluginISPyBSetImagesPositionsv1_4(EDPluginISPyBv1_4):
    """
    Plugin to store sample position (for grid scans)
    """

    def __init__(self):
        """
        Sets default values for dbserver parameters 
        """
        EDPluginISPyBv1_4.__init__(self)
        self.setXSDataInputClass(XSDataInputISPyBSetImagesPositions)
        self.listImageCreation = []


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
        self.DEBUG("EDPluginISPyBSetImagesPositionsv1_4.process")
        httpAuthenticatedToolsForCollectionWebService = HttpAuthenticated(username=self.strUserName, password=self.strPassWord)
        clientToolsForCollectionWebService = Client(self.strToolsForCollectionWebServiceWsdl,
                                                    transport=httpAuthenticatedToolsForCollectionWebService,
                                                    cache=None)
        # Loop over all positions
        listImagePosition = []
        for xsDataImagePosition in self.dataInput.imagePosition:
            imagePosition = clientToolsForCollectionWebService.factory.create('imagePosition')
            # Get the workflow ID and status
            imagePosition.fileName = os.path.basename(xsDataImagePosition.fileName.path.value)
            imagePosition.fileLocation = os.path.dirname(xsDataImagePosition.fileName.path.value)
            if xsDataImagePosition.jpegFileFullPath is not None:
                imagePosition.jpegFileFullPath = xsDataImagePosition.jpegFileFullPath.path.value
            if xsDataImagePosition.jpegThumbnailFileFullPath is not None:
                imagePosition.jpegThumbnailFileFullPath = xsDataImagePosition.jpegThumbnailFileFullPath.path.value
            listImagePosition.append(imagePosition)
        self.listImageCreation = clientToolsForCollectionWebService.service.setImagesPositions(
                                    listImagePosition=listImagePosition)
        self.DEBUG("EDPluginISPyBSetImagesPositionsv1_4.process: listImageCreation=%r" % self.listImageCreation)





    def finallyProcess(self, _edObject=None):
        EDPluginISPyBv1_4.finallyProcess(self)
        self.DEBUG("EDPluginISPyBSetImagesPositionsv1_4.finallyProcess")
        xsDataResultISPyBSetImagesPositions = XSDataResultISPyBSetImagesPositions()
        for imageCreation in self.listImageCreation:
            xsDataISPyBImageCreation = XSDataISPyBImageCreation()
            xsDataISPyBImageCreation.fileLocation = XSDataString(imageCreation.fileLocation)
            xsDataISPyBImageCreation.fileName = XSDataString(imageCreation.fileName)
            try:
                xsDataISPyBImageCreation.imageId = XSDataInteger(imageCreation.imageId)
            except AttributeError:
                self.WARNING("Image %s/%s does not have any image id" %
                             (imageCreation.fileLocation, imageCreation.fileName))
            xsDataISPyBImageCreation.isCreated = XSDataBoolean(imageCreation.isCreated)
            xsDataResultISPyBSetImagesPositions.addImageCreation(xsDataISPyBImageCreation)
        self.setDataOutput(xsDataResultISPyBSetImagesPositions)


