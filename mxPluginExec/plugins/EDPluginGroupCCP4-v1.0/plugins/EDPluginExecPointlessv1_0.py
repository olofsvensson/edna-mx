from __future__ import with_statement

# coding: utf8
#
#    Project: EDNAproc
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author: Thomas Boeglin
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

__author__="Thomas Boeglin"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import re
import os.path

from EDVerbose import EDVerbose
from EDUtilsPath import EDUtilsPath
from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDUtilsFile import EDUtilsFile

from XSDataCommon import XSDataStatus, XSDataBoolean, XSDataResult
from XSDataCommon import XSDataInteger, XSDataString, XSDataLength, XSDataAngle
from XSDataCCP4v1_0 import XSDataPointless, XSDataPointlessOut, XSDataCCP4Cell

class EDPluginExecPointlessv1_0(EDPluginExecProcessScript):
    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setRequiredToHaveConfiguration(True)
        self.setXSDataInputClass(XSDataPointless)


    def configure(self):
        EDPluginExecProcessScript.configure(self)

    def preProcess(self):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG('Pointless: preprocess')
        if self.output_file is not None and self.input_file is not None:
            if EDUtilsPath.isEMBL() or EDUtilsPath.isALBA():
                options = '''-c xdsin {0} hklout {1}'''.format(self.input_file,
                                                               self.output_file)
            else:
                options = '''xdsin {0} hklout {1}'''.format(self.input_file,
                                                            self.output_file)
            self.setScriptCommandline(options)
            self.DEBUG('command line options set to {0}'.format(options))
        self.addListCommandExecution('setting symmetry-based')
        if self.dataInput.choose_spacegroup is not None:
            self.addListCommandExecution('choose spacegroup {0}'.format(self.dataInput.choose_spacegroup.value))

    def checkParameters(self):
        self.DEBUG('Pointless: checkParameters')
        data_input = self.getDataInput()
        self.checkMandatoryParameters(data_input.input_file, 'no input file')
        self.checkMandatoryParameters(data_input.output_file, 'no output file')

        self.input_file = self.dataInput.input_file.value
        self.output_file = self.dataInput.output_file.value

        # now really check the parameters
        if data_input.input_file is not None:
            path = data_input.input_file.value
            if not os.path.exists(path):
                self.ERROR('input file {0} does not exist'.format(path))
                self.setFailure()
                return

    def process(self):
        self.DEBUG('Pointless: process')
        EDPluginExecProcessScript.process(self)

    def postProcess(self):
        self.DEBUG('Pointless: postProcess')
        EDPluginExecProcessScript.postProcess(self)
        outputFile = self.dataInput.output_file.value
        self.dataOutput = self.parsePointlessOutput(os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName()))

    def parsePointlessOutput(self, _outputFile):
        
        sgre = re.compile(""" \* Space group = '(?P<sgstr>.*)' \(number\s+(?P<sgnumber>\d+)\)""")

        sgnumber = sgstr = None

        res = XSDataPointlessOut()
        status = XSDataStatus()
        status.isSuccess = XSDataBoolean(False)
        if os.path.exists(_outputFile):
            res.status = status

            strLog = EDUtilsFile.readFile(_outputFile)
            if strLog is not None:
                # we'll apply the regexp to the whole file contents which
                # hopefully won't be that long.
                m = sgre.search(strLog)
                if m is not None:
                    d = m.groupdict()
                    sgnumber = d['sgnumber']
                    sgstr = d['sgstr']

                    res.sgnumber = XSDataInteger(sgnumber)
                    res.sgstr = XSDataString(sgstr)
                    status.isSuccess = XSDataBoolean(True)
                    # Search first for unit cell after the Laue group...
                    unitCellRe = re.compile("""  Laue group confidence.+\\n\\n\s+Unit cell:(.+)""")
                    m2 = unitCellRe.search(strLog)
                    if m2 is None:
                        # Then search it from the end...
                        unitCellRe = re.compile(""" \* Cell Dimensions : \(obsolete \- refer to dataset cell dimensions above\)\\n\\n(.+)""")
                        m2 = unitCellRe.search(strLog)
                    if m2 is not None:
                        listCell = m2.groups()[0].split()
                        xsDataCCP4Cell = XSDataCCP4Cell()
                        xsDataCCP4Cell.length_a = XSDataLength(listCell[0])
                        xsDataCCP4Cell.length_b = XSDataLength(listCell[1])
                        xsDataCCP4Cell.length_c = XSDataLength(listCell[2])
                        xsDataCCP4Cell.angle_alpha = XSDataAngle(listCell[3])
                        xsDataCCP4Cell.angle_beta = XSDataAngle(listCell[4])
                        xsDataCCP4Cell.angle_gamma = XSDataAngle(listCell[5])
                        res.cell = xsDataCCP4Cell
        return res
