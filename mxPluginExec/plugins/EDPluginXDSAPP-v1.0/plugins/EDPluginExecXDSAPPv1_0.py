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

__author__ = "Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os
import glob

from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDUtilsImage import EDUtilsImage

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString

from XSDataXDSAPPv1_0 import XSDataInputXDSAPP
from XSDataXDSAPPv1_0 import XSDataResultXDSAPP


class EDPluginExecXDSAPPv1_0(EDPluginExecProcessScript):
    """
    This plugin runs the XDSAPP program 'process' written by Global Phasing
    """


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputXDSAPP)
        self.setDataOutput(XSDataResultXDSAPP())
        self.maxNoProcessors = None
        self.raxis = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecXDSAPPv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.prefixRunNumber = None


    def configure(self):
        EDPluginExecProcessScript.configure(self)
        self.DEBUG("EDPluginExecXDSAPPv1_0.configure")
        self.maxNoProcessors = self.config.get("maxNoProcessors", self.maxNoProcessors)
        self.raxis = self.config.get("raxis", self.raxis)

    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginExecXDSAPPv1_0.preProcess")
        strCommandLine = self.generateCommandLine(self.dataInput)
        self.setScriptCommandline(strCommandLine)
        self.addListCommandPreExecution("export PATH=/opt/pxsoft/bin:$PATH")


    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginExecXDSAPPv1_0.postProcess")
        # Populate the results
        prefixRunNumber = EDUtilsImage.getPrefix(self.dataInput.image.path.value)
        xsDataResultXDSAPP = self.parseOutputDirectory(self.getWorkingDirectory(), prefixRunNumber)
        self.dataOutput = xsDataResultXDSAPP


    def generateCommandLine(self, _xsDataInputXDSAPP):
        """
        This method creates the input command line for XDSAPP
        """
        self.DEBUG("EDPluginExecXDSAPPv1_0.generateCommands")
        strCommandText = ""

        # Image
        strCommandText += " --image {0}".format(_xsDataInputXDSAPP.image.path.value)

        anomalous = True
        if _xsDataInputXDSAPP.anomalous is not None:
            if not _xsDataInputXDSAPP.anomalous.value:
                anomalous = False

        if anomalous:
            strCommandText += " --fried=false"
        else:
            strCommandText += " --fried=true"

        if self.raxis is not None:
            strCommandText += " --raxis=\"{0}\"".format(self.raxis)

        strCommandText += " --dir={0}".format(self.getWorkingDirectory())

        if self.maxNoProcessors is not None:
            strCommandText += " --cpu={0} --jobs=1".format(self.maxNoProcessors)

        if _xsDataInputXDSAPP.startImageNumber is not None and \
           _xsDataInputXDSAPP.endImageNumber is not None:
            strCommandText += " --range=\"{0} {1}\"".format(_xsDataInputXDSAPP.startImageNumber.value,
                                                            _xsDataInputXDSAPP.endImageNumber.value)

        if _xsDataInputXDSAPP.spacegroup is not None:
            strCommandText += " --spacegroup=\"{0}\"".format(_xsDataInputXDSAPP.spacegroup.value)

        return strCommandText


    def parseOutputDirectory(self, _workingDirectory, _prefixRunNumber):
        xsDataResultXDSAPP = XSDataResultXDSAPP()
        # Log file
        logFile = os.path.join(_workingDirectory, "results_{0}.txt").format(_prefixRunNumber)
        if os.path.exists(logFile):
            xsDataResultXDSAPP.logFile = XSDataFile(XSDataString(logFile))
        # Pointless log
        if os.path.exists(os.path.join(_workingDirectory, "pointless.log")):
            xsDataResultXDSAPP.pointlessLog = XSDataFile(XSDataString(os.path.join(_workingDirectory, "pointless.log")))
        # Phenix Xtriage log
        if os.path.exists(os.path.join(_workingDirectory, "phenix_xtriage.log")):
            xsDataResultXDSAPP.phenixXtriageLog = XSDataFile(XSDataString(os.path.join(_workingDirectory, "phenix_xtriage.log")))
        # CORRECT.LP
        if os.path.exists(os.path.join(_workingDirectory, "CORRECT.LP")):
            xsDataResultXDSAPP.correctLP = XSDataFile(XSDataString(os.path.join(_workingDirectory, "CORRECT.LP")))
        # XDS_ASCII.HKL
        if os.path.exists(os.path.join(_workingDirectory, "XDS_ASCII.HKL")):
            xsDataResultXDSAPP.XDS_ASCII_HKL = XSDataFile(XSDataString(os.path.join(_workingDirectory, "XDS_ASCII.HKL")))
        if os.path.exists(os.path.join(_workingDirectory, "XDS_ASCII.HKL_1")):
            xsDataResultXDSAPP.XDS_ASCII_HKL_1 = XSDataFile(XSDataString(os.path.join(_workingDirectory, "XDS_ASCII.HKL_1")))
        # XSCALE.LP
        if os.path.exists(os.path.join(_workingDirectory, "XSCALE.LP")):
            xsDataResultXDSAPP.XSCALE_LP = XSDataFile(XSDataString(os.path.join(_workingDirectory, "XSCALE.LP")))
        # XDS.INP
        if os.path.exists(os.path.join(_workingDirectory, "XDS.INP")):
            xsDataResultXDSAPP.XDS_INP = XSDataFile(XSDataString(os.path.join(_workingDirectory, "XDS.INP")))
        # Result files
        for mtz_F in glob.glob(os.path.join(_workingDirectory, "{0}*_F.mtz".format(_prefixRunNumber))):
            xsDataResultXDSAPP.addMtz_F(XSDataFile(XSDataString(mtz_F)))
        for mtz_I in glob.glob(os.path.join(_workingDirectory, "{0}*_I.mtz".format(_prefixRunNumber))):
            xsDataResultXDSAPP.addMtz_I(XSDataFile(XSDataString(mtz_I)))
        for mtz_F_plus_F_minus in glob.glob(os.path.join(_workingDirectory, "{0}*_F_plus_F_minus.mtz".format(_prefixRunNumber))):
            xsDataResultXDSAPP.addMtz_F_plus_F_minus(XSDataFile(XSDataString(mtz_F_plus_F_minus)))
        for hkl in glob.glob(os.path.join(_workingDirectory, "{0}*.hkl".format(_prefixRunNumber))):
            xsDataResultXDSAPP.addHkl(XSDataFile(XSDataString(hkl)))
        for cv in glob.glob(os.path.join(_workingDirectory, "{0}*.cv".format(_prefixRunNumber))):
            xsDataResultXDSAPP.addCv(XSDataFile(XSDataString(mtz_F)))
        return xsDataResultXDSAPP
