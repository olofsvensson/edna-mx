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
import re

from EDPluginExec import EDPluginExec

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile


from XSDataCCP4v1_0 import XSDataInputAimlessLog2Csv
from XSDataCCP4v1_0 import XSDataResultAimlessLog2Csv

class EDPluginExecAimlessLog2Csvv1_0(EDPluginExec):
    """
    This plugin produces a CSV file from an aimless log file
    """


    def __init__(self):
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputAimlessLog2Csv)
        self.setDataOutput(XSDataResultAimlessLog2Csv())

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecDimplev1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.aimlessLogPath, "Data Input amilessLogPath is None")


    def process(self, _edObject=None):
        EDPluginExec.process(self)
        self.DEBUG("EDPluginExec.process")
        aimlessLogPath = self.dataInput.aimlessLogPath.path.value
        aimlessCsvPath = os.path.join(self.getWorkingDirectory(), "aimless.csv")
        self.createAimlessCsvFile(aimlessLogPath, aimlessCsvPath)
        if os.path.exists(aimlessCsvPath):
            self.dataOutput.csvPath = XSDataFile(XSDataString(aimlessCsvPath))

    def createAimlessCsvFile(self, aimlessLogPath, aimlessCsvPath):
        stats1 = []
        stats2 = []
        stats3 = []

        with open(aimlessLogPath, "r") as f:
            listLines = f.readlines()
        tab1 = re.compile('TABLE:  Analysis against resolution')
        tab1_header = re.compile('N  1\/d\^2    Dmid   Rmrg  Rfull   Rcum  Rmeas   Rpim    Nmeas      AvI  RMSdev    sd  I\/RMS Mn\(I\/sd\)  FrcBias ')
        tab1_end = re.compile('\$\$')
        try:
            for ind in range(len(listLines)):
                item = listLines[ind]
                if tab1.search(item):
                    for ind2 in range(ind + 1, len(listLines)):
                        item2 = listLines[ind2]
                        if tab1_header.search(item2):
                            for ind3 in range(ind2 + 1, len(listLines)):
                                # we are in the body
                                body = listLines[ind3]
                                if tab1_end.search(body):
                                    raise StopIteration
                                fields = body.split()
                                stats1.append(fields)
        #                        print body
        except StopIteration:
            self.DEBUG("Done with Analysis against resolution table")
        ###############
        tab2 = re.compile('TABLE:  Correlations CC')
        tab2_header = re.compile('N  1\/d\^2    Dmid CCanom    Nanom   RCRanom   CC1\/2   NCC1\/2  CC1\/2v   Rsplit     CCfit CCanomfit')
        tab2_end = re.compile('\$\$')
        try:
            for ind in range(len(listLines)):
                item = listLines[ind]
                if tab2.search(item):
                    for ind2 in range(ind + 1, len(listLines)):
                        item2 = listLines[ind2]
                        if tab2_header.search(item2):
                            for ind3 in range(ind2 + 1, len(listLines)):
                                # we are in the body
                                body = listLines[ind3]
                                if tab2_end.search(body):
                                    raise StopIteration
                                fields = body.split()
                                stats2.append(fields)
        #                        print body
        except StopIteration:
            self.DEBUG("Done with CC half table")



        #######################
        tab3 = re.compile('TABLE\:  Completeness \& multiplicity v. resolution')
        tab3_header = re.compile('N  1\/d\^2    Dmid    Nmeas     Nref    Ncent  \%poss C\%poss Mlplct   AnoCmp AnoFrc AnoMlt')
        tab3_end = re.compile('\$\$')
        try:
            for ind in range(len(listLines)):
                item = listLines[ind]
                if tab3.search(item):
                    for ind2 in range(ind + 1, len(listLines)):
                        item2 = listLines[ind2]
                        if tab3_header.search(item2):
                            for ind3 in range(ind2 + 1, len(listLines)):
                                # we are in the body
                                body = listLines[ind3]
                                if tab3_end.search(body):
                                    raise StopIteration
                                fields = body.split()
                                stats3.append(fields)
        #                        print body
        except StopIteration:
            self.DEBUG("Done with Completeness")

        with open(aimlessCsvPath, "w") as out:
            header = "Resolution,Rmeas,Completeness,I/Sig(I),CC1/2,AnomalousCorrelation\n"
            out.write(header)

            for ind in range(len(stats1)):
                highres = stats1[ind][2]
                Rmeas = stats1[ind][6]
                Cpl = stats3[ind][6]
                Isig = stats1[ind][12]
                CChalf = stats2[ind][6]
                CCano = stats2[ind][3]
                s = ","
                joined = s.join([highres, Rmeas, Cpl, Isig, CChalf, CCano])
                out.write(joined + "\n")



