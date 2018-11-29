# coding: utf8
#
#    Project: MX Plugin Exec
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

__author__ = "Ivars Karpics"
__license__ = "GPLv3+"
__copyright__ = "EMBL Hamburg"

import os
import glob
import subprocess
import multiprocessing

from EDUtilsPath import EDUtilsPath

from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString

from XSDataCrystFELv1_0 import XSDataInputCrystFEL
from XSDataCrystFELv1_0 import XSDataResultCrystFEL


class EDPluginExecCrystFELIndexv1_0(EDPluginExecProcessScript):
    """
    This plugin runs the CrystFEL program
    """


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputCrystFEL)
        self.setDataOutput(XSDataResultCrystFEL())

    def checkParameters(self):
        self.DEBUG("EDPluginExecCrystFELIndexv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")


    def configure(self):
        EDPluginExecProcessScript.configure(self)
        self.DEBUG("EDPluginExecCrystFELIndexv1_0.configure")

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecCrystFELIndexv1_0.preProcess")
        strCommandLine = self.generateCommandLine(self.dataInput)
        self.setScriptCommandline(strCommandLine)


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecCrystFELIndexv1_0.postProcess")
        # Populate the results
        xsDataResultCrystFEL = self.parseOutputDirectory(self.getWorkingDirectory())
        self.dataOutput = xsDataResultCrystFEL


    def generateCommandLine(self, _xsDataInputCrystFEL):
        self.DEBUG("EDPluginExecCrystFELIndexv1_0.generateCommands")

        strCommandText = "-i %s -g %s " %(_xsDataInputCrystFEL.indexFile.value,
                                          _xsDataInputCrystFEL.geomFile.value)
        strCommandText += "--peaks=zaef --threshold=20 --min-gradient=100 --min-snr=5 "
        strCommandText += "--no-cell-combinations --indexing=mosflm,xds --int-radius=3,4,5 "
        strCommandText += "-o %s -p %s -j 72" % (_xsDataInputCrystFEL.indexResultFile.value,
                                                 _xsDataInputCrystFEL.cellFile.value)

        return  strCommandText

    def parseOutputDirectory(self, _workingDirectory):
        xsDataResultCrystFEL = XSDataResultCrystFEL()
        return xsDataResultCrystFEL
