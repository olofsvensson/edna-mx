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



__author__ = "Thomas Boeglin"
__license__ = "GPLv3+"
__copyright__ = "ESRF"




import os.path
import shutil

from EDPlugin import EDPlugin
from EDVerbose import EDVerbose
from EDFactoryPlugin import edFactoryPlugin

from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataVectorDouble
from XSDataCommon import XSDataString

edFactoryPlugin.loadModule('XSDataXDSv1_0')

from XSDataXDSv1_0 import XSDataXscaleCompletenessEntry
from XSDataXDSv1_0 import XSDataXscaleParsingInput
from XSDataXDSv1_0 import XSDataXscaleParsedOutput

class EDPluginParseXscaleOutputv1_0(EDPlugin):

    def __init__(self):
        EDPlugin.__init__(self)
        self.setXSDataInputClass(XSDataXscaleParsingInput)
        self.setDataOutput(XSDataXscaleParsedOutput())

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginParseXscaleOutputv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput.lp_file, "No LP file given")

        # now really check it
        path = self.dataInput.lp_file.value
        if not os.path.isfile(path):
            strErrorMessage = "Input file {0} does not exist".format(path)
            self.ERROR(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()

    def preProcess(self, _edObject=None):
        EDPlugin.preProcess(self)
        self.DEBUG("EDPluginParseXscaleOutputv1_0.preProcess")

    def process(self, _edObject=None):
        EDPlugin.process(self)

        output = XSDataXscaleParsedOutput()

        # get all the file's contents, find where the info is and then
        # use helper functions to retrieve stuff and put it in the
        # data model
        try:
            f = open(self.dataInput.lp_file.value, 'r')
            lines = f.readlines()
        except IOError:
            strErrorMessage = "Input file {0} could not be opened".format(self.dataInput.lp_file.value)
            self.ERROR(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
            return

        # look for the stats table
        info_begin = None
        info_end = None
        started = False
        for line_no, line in enumerate(lines):
            if line.find('LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected') != -1:
                # there's an empty line after the header
                info_begin = line_no + 2
            if info_begin is not None and line.find('total') != -1:
                # we're at the last table line
                info_end = line_no
                # stop here as there are some other lines containing
                # "total" later
                break
        if info_begin is None or info_end is None:
            strErrorMessage = "Could not find the completeness table"
            self.ERROR(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
            return

        _extract_completeness_entries(lines[info_begin:info_end + 1], output)

        input_file = self.dataInput.lp_file.value
        output.xds_run_directory = XSDataString(os.path.dirname(input_file))
        self.dataOutput = output

    def postProcess(self, _edObject=None):
        EDPlugin.postProcess(self)
        self.DEBUG("EDPluginParseXscaleOutputv1_0.postProcess")


def _extract_completeness_entries(lines, output):
    for lineno, line in enumerate(lines):
        if line.find('total') != -1:
            # special case for the last table line which contains the
            # totals
            infos = [float(x.replace('%', '').replace('*', '')) for x in line.split()[1:]]
            output.total_completeness = XSDataXscaleCompletenessEntry()
            output.total_completeness.observed = XSDataDouble(infos[0])
            output.total_completeness.unique = XSDataDouble(infos[1])
            output.total_completeness.possible = XSDataDouble(infos[2])

            output.total_completeness.multiplicity = XSDataDouble(infos[0] / infos[2])

            output.total_completeness.complete = XSDataDouble(infos[3])
            output.total_completeness.rfactor = XSDataDouble(infos[4])
            output.total_completeness.isig = XSDataDouble(infos[7])
            output.total_completeness.half_dataset_correlation = XSDataDouble(infos[10])
        else:
            # regular line, do not strip the first elem and bump the
            # indices by 1
            infos = [float(x.replace('%', '').replace('*', '')) for x in line.split()]
            res = XSDataXscaleCompletenessEntry()
            res.res = XSDataDouble(infos[0])
            res.observed = XSDataDouble(infos[1])
            res.unique = XSDataDouble(infos[2])
            res.possible = XSDataDouble(infos[3])

            res.multiplicity = XSDataDouble(infos[1] / infos[3])

            res.complete = XSDataDouble(infos[4])
            res.rfactor = XSDataDouble(infos[5])
            res.isig = XSDataDouble(infos[8])
            res.half_dataset_correlation = XSDataDouble(infos[10])
            output.completeness_entries.append(res)
