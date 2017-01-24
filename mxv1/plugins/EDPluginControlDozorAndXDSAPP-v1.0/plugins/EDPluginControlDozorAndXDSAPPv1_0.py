# coding: utf8
#
#    Project: MXv1
#             http://www.edna-site.org
#
#    Copyright (C) ESRF
#
#    Principal author: Olof Svensson
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

__author__ = "Olof Svensson"
__license__ = "GPLv2+"
__copyright__ = "ESRF"

import os
import sys
import gzip
import time
import shutil
import socket
import subprocess

from EDPluginControl import EDPluginControl
from EDHandlerESRFPyarchv1_0 import EDHandlerESRFPyarchv1_0
from EDUtilsPath import EDUtilsPath
from EDUtilsFile import EDUtilsFile

from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataString
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataDouble

from XSDataControlDozorAndXDSAPPv1_0 import XSDataInputControlDozorAndXDSAPP
from XSDataControlDozorAndXDSAPPv1_0 import XSDataResultControlDozorAndXDSAPP

EDFactoryPluginStatic.loadModule("XSDataControlDozorv1_0")
from XSDataControlDozorv1_0 import XSDataInputControlDozor

EDFactoryPluginStatic.loadModule("XSDataControlXDSAPPv1_0")
from XSDataControlXDSAPPv1_0 import XSDataInputControlXDSAPP

class EDPluginControlDozorAndXDSAPPv1_0(EDPluginControl):
    """
    Control plugin for running both Dozor and XDSAPP. This plugin is intended
    to be used for Eiger HDF5 images.
    
    The control Dozor plugin will generate CBF images for the whole data collection
    in a temporary directory and then these images are used by XDSAPP. When the XDSAPP
    processing is finished the temporary directory containing the CBF images is deleted.
    """


    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputControlDozorAndXDSAPP)
        self.dataOutput = XSDataResultControlDozorAndXDSAPP()


    def configure(self):
        EDPluginControl.configure(self)

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlDozorAndXDSAPPv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.dataCollectionId, "No data collection id")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlDozorAndXDSAPPv1_0.preProcess")


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG('EDPluginControlDozorAndXDSAPPv1_0.process starting')

        # Run the Dozor control plugin keeping the CBF file directory
        xsDataInputControlDozor = XSDataInputControlDozor()
        xsDataInputControlDozor.dataCollectionId = self.dataInput.dataCollectionId
        xsDataInputControlDozor.processDirectory = self.dataInput.dozorProcessDirectory
        xsDataInputControlDozor.keepCbfTmpDirectory = XSDataBoolean(True)
        edPluginControlDozor = self.loadPlugin("EDPluginControlDozorv1_0")
        edPluginControlDozor.dataInput = xsDataInputControlDozor
        edPluginControlDozor.executeSynchronous()

        # Run the XDSAPP control plugin
        xsDataInputControlXDSAPP = XSDataInputControlXDSAPP()
        xsDataInputControlXDSAPP.dataCollectionId = self.dataInput.dataCollectionId
        xsDataInputControlXDSAPP.doAnomAndNonanom = self.dataInput.doAnomAndNonanom
        xsDataInputControlXDSAPP.hdf5ToCbfDirectory = edPluginControlDozor.dataOutput.pathToCbfDirectory
        xsDataInputControlXDSAPP.processDirectory = self.dataInput.xdsappProcessDirectory
        edPluginControlXDSAPP = self.loadPlugin("EDPluginControlXDSAPPv1_0")
        edPluginControlXDSAPP.dataInput = xsDataInputControlXDSAPP
        edPluginControlXDSAPP.executeSynchronous()

        # Delete the temporary directory containing the CBF images
        shutil.rmtree(edPluginControlDozor.dataOutput.pathToCbfDirectory.path.value)

