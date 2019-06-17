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

from EDPluginExecProcessScript import EDPluginExecProcessScript

from XSDataCrystFELv1_0 import XSDataInputCrystFEL
from XSDataCrystFELv1_0 import XSDataResultCrystFEL


class EDPluginExecCrystFELPartialatorv1_0(EDPluginExecProcessScript):
    """
    This plugin runs the CrystFEL program
    """


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputCrystFEL)
        self.setDataOutput(XSDataResultCrystFEL())

        #TODO move to input file
        self.partialator_options = "--max-adu=65000 --iterations=1 --model=unity -j 60"

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecCrystFELPartialatorv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")


    def configure(self):
        EDPluginExecProcessScript.configure(self)
        self.DEBUG("EDPluginExecCrystFELPartialatorv1_0.configure")

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecCrystFELPartialatorv1_0.preProcess")
        strCommandLine = self.generateCommandLine(self.dataInput)
        self.setScriptCommandline(strCommandLine)


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecCrystFELPartialatorv1_0.postProcess")
        # Populate the results
        xsDataResultCrystFEL = self.parseOutputDirectory(self.getWorkingDirectory())
        self.dataOutput = xsDataResultCrystFEL


    def generateCommandLine(self, _xsDataInputCrystFEL):
        """
        This method creates the input command line for CrystFEL
        """
        self.DEBUG("EDPluginExecCrystFELPartialatorv1_0.generateCommands")
     
        strCommandText = "-i %s.stream -o %s_partialator_%s.hkl -y %s %s" % (
            _xsDataInputCrystFEL.baseFileName.value,
            _xsDataInputCrystFEL.baseFileName.value,
            _xsDataInputCrystFEL.pointGroup.value,
            _xsDataInputCrystFEL.pointGroup.value,
            self.partialator_options
        )
        return  strCommandText

    def parseOutputDirectory(self, _workingDirectory):
        xsDataResultCrystFEL = XSDataResultCrystFEL()
        return xsDataResultCrystFEL
