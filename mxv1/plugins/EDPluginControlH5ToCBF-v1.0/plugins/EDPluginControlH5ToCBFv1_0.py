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
EDFactoryPluginStatic.loadModule("XSDataH5ToCBFv1_0")

from XSDataH5ToCBFv1_0 import XSDataISPyBDataCollection
from XSDataH5ToCBFv1_0 import XSDataInputH5ToCBF

EDFactoryPluginStatic.loadModule("XSDataISPyBv1_4")
from XSDataISPyBv1_4 import XSDataInputRetrieveDataCollection

from XSDataControlH5ToCBFv1_0 import XSDataInputControlH5ToCBF
from XSDataControlH5ToCBFv1_0 import XSDataResultControlH5ToCBF
from XSDataControlH5ToCBFv1_0 import XSDataISPyBDataCollection


class EDPluginControlH5ToCBFv1_0(EDPluginControl):
    """
    This plugin runs the ControlH5ToCBF program written by Sasha Popov
    """


    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputControlH5ToCBF)
        self.setDataOutput(XSDataResultControlH5ToCBF())
        self.strEDPluginH5ToCBF = "EDPluginH5ToCBFv1_0"
        self.edPluginEDPluginH5ToCBF = None
        self.strPluginISPyBRetrieveDataCollection = "EDPluginISPyBRetrieveDataCollectionv1_4"
        self.edPluginISPyBRetrieveDataCollection = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlH5ToCBFv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlH5ToCBFv1_0.preProcess")
        self.edPluginEDPluginH5ToCBF = self.loadPlugin(self.strEDPluginH5ToCBF, "H5ToCBF")
        self.edPluginISPyBRetrieveDataCollection = self.loadPlugin(self.strPluginISPyBRetrieveDataCollection, "ISPyBRetrieveDataCollection")



    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlH5ToCBFv1_0.process")
        imageNumber = self.dataInput.imageNumber.value
        if self.dataInput.hdf5ImageNumber is None:
            hdf5ImageNumber = imageNumber
        else:
            hdf5ImageNumber = self.dataInput.hdf5ImageNumber.value

        if self.dataInput.ispybDataCollection is None:
            xsDataInputRetrieveDataCollection = XSDataInputRetrieveDataCollection()
            xsDataImage = XSDataImage(self.dataInput.hdf5File.path)
            xsDataInputRetrieveDataCollection.image = xsDataImage
            self.edPluginISPyBRetrieveDataCollection.dataInput = xsDataInputRetrieveDataCollection
            self.edPluginISPyBRetrieveDataCollection.executeSynchronous()
            xsDataResultRetrieveDataCollection = self.edPluginISPyBRetrieveDataCollection.dataOutput
            dataCollection = xsDataResultRetrieveDataCollection.dataCollection
        else:
            dataCollection = self.dataInput.ispybDataCollection
        if dataCollection is not None:
            if dataCollection.overlap is None:
                overlap = 0.0
            else:
                overlap = dataCollection.overlap
            axisStart = dataCollection.axisStart
            oscillationRange = dataCollection.axisRange
            axisStartNew = axisStart - (overlap + oscillationRange) * (imageNumber - 1)
            dataCollection.axisStart = axisStartNew
            xsDataISPyBDataCollection = XSDataISPyBDataCollection.parseString(dataCollection.marshal())
        else:
            xsDataISPyBDataCollection = None
        xsDataInputH5ToCBF = XSDataInputH5ToCBF()
        xsDataInputH5ToCBF.hdf5File = self.dataInput.hdf5File
        xsDataInputH5ToCBF.imageNumber = self.dataInput.imageNumber
        xsDataInputH5ToCBF.hdf5ImageNumber = XSDataInteger(hdf5ImageNumber)
        xsDataInputH5ToCBF.dataCollection = xsDataISPyBDataCollection
        xsDataInputH5ToCBF.forcedOutputDirectory = self.dataInput.forcedOutputDirectory
        self.edPluginEDPluginH5ToCBF.dataInput = xsDataInputH5ToCBF
        self.edPluginEDPluginH5ToCBF.executeSynchronous()
        if self.edPluginEDPluginH5ToCBF.dataOutput is not None:
            self.dataOutput.outputCBFFile = self.edPluginEDPluginH5ToCBF.dataOutput.outputCBFFile
            if dataCollection is not None:
                self.dataOutput.ispybDataCollection = XSDataISPyBDataCollection.parseString(dataCollection.marshal())
