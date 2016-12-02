# coding: utf8
#
#    Project: MXv1
#             http://www.edna-site.org
#
#    Copyright (C) ESRF
#
#    Principal author:       Olof Svensson
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
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os

from EDPluginControl import EDPluginControl
from EDUtilsImage import EDUtilsImage

from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataImage

from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataH5ToCBFv1_1")

from XSDataH5ToCBFv1_1 import XSDataInputH5ToCBF

from XSDataControlH5ToCBFv1_1 import XSDataInputControlH5ToCBF
from XSDataControlH5ToCBFv1_1 import XSDataResultControlH5ToCBF
from XSDataControlH5ToCBFv1_1 import XSDataISPyBDataCollection


class EDPluginControlH5ToCBFv1_1(EDPluginControl):
    """
    This plugin runs the ControlH5ToCBF program written by Sasha Popov
    """


    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputControlH5ToCBF)
        self.setDataOutput(XSDataResultControlH5ToCBF())
        self.strEDPluginH5ToCBF = "EDPluginH5ToCBFv1_1"
        self.edPluginEDPluginH5ToCBF = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlH5ToCBFv1_1.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlH5ToCBFv1_1.preProcess")
        self.edPluginEDPluginH5ToCBF = self.loadPlugin(self.strEDPluginH5ToCBF)



    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlH5ToCBFv1_1.process")
        imageNumber = self.dataInput.imageNumber.value
        if self.dataInput.hdf5ImageNumber is None:
            hdf5ImageNumber = imageNumber
        else:
            hdf5ImageNumber = self.dataInput.hdf5ImageNumber.value

        xsDataInputH5ToCBF = XSDataInputH5ToCBF()
        xsDataInputH5ToCBF.hdf5File = self.dataInput.hdf5File
        xsDataInputH5ToCBF.imageNumber = self.dataInput.imageNumber
        xsDataInputH5ToCBF.hdf5ImageNumber = XSDataInteger(hdf5ImageNumber)
        xsDataInputH5ToCBF.forcedOutputDirectory = self.dataInput.forcedOutputDirectory
        xsDataInputH5ToCBF.forcedOutputImageNumber = self.dataInput.forcedOutputImageNumber
        self.edPluginEDPluginH5ToCBF.dataInput = xsDataInputH5ToCBF
        self.edPluginEDPluginH5ToCBF.executeSynchronous()
        if self.edPluginEDPluginH5ToCBF.dataOutput is not None:
            self.dataOutput.outputCBFFile = self.edPluginEDPluginH5ToCBF.dataOutput.outputCBFFile
