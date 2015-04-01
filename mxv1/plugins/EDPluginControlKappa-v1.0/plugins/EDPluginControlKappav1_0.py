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

from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataXOalignv1_0")
from XSDataXOalignv1_0 import XSDataInputXOalign
from XSDataXOalignv1_0 import XSDataXOalignCell
from XSDataXOalignv1_0 import XSDataXOalignOrientation

from XSDataMXv1 import XSDataKappaSolution
from XSDataMXv1 import XSDataInputControlKappa
from XSDataMXv1 import XSDataResultControlKappa


class EDPluginControlKappav1_0(EDPluginControl):
    """
    This plugin runs the XOalign program written by Sasha Popov
    """
    

    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputControlKappa)
        self.setDataOutput(XSDataResultControlKappa())
        self.strEDPluginXOalignName = "EDPluginXOalignv1_0"
        self.edPluginXOalign = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlKappav1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")

    
    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlKappav1_0.preProcess")
        self.edPluginXOalign = self.loadPlugin(self.strEDPluginXOalignName, "XOalign")
        xsDataInputXOalign = XSDataInputXOalign()
        orientation = self.dataInput.selectedSolution.orientation
        cell = self.dataInput.selectedSolution.crystal.cell
        xsDataXOalignOrientation = XSDataXOalignOrientation.parseString(orientation.marshal())
        xsDataXOalignCell = XSDataXOalignCell.parseString(cell.marshal())
        xsDataInputXOalign.symmetry = self.dataInput.selectedSolution.crystal.spaceGroup.name
        xsDataInputXOalign.orientation = xsDataXOalignOrientation
        xsDataInputXOalign.cell = xsDataXOalignCell
        self.edPluginXOalign.dataInput = xsDataInputXOalign

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlKappav1_0.process")
        self.executePluginSynchronous(self.edPluginXOalign)
        
    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self, _edObject)
        self.DEBUG("EDPluginControlKappav1_0.postProcess")
        self.dataOutput.logFile = self.edPluginXOalign.dataOutput.logFile
        for solution in self.edPluginXOalign.dataOutput.solution:
            xsDataKappaSolution = XSDataKappaSolution.parseString(solution.marshal())
            self.dataOutput.addSolution(xsDataKappaSolution)
