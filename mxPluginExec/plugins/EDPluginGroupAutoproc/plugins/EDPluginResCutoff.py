from __future__ import with_statement

# coding: utf8
#
#    Project: Autoproc
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




import os.path
import shutil
import math

from EDPlugin import EDPlugin
from EDVerbose import EDVerbose
from XSDataCommon import XSDataBoolean, XSDataFloat, XSDataVectorDouble
from XSDataAutoproc import XSDataResCutoff, XSDataResCutoffResult
from XSDataAutoproc import XSData2DCoordinates, XSDataXdsCompletenessEntry


class EDPluginResCutoff(EDPlugin):
    """
    """


    def __init__(self ):
        """
        """
        EDPlugin.__init__(self )
        self.setXSDataInputClass(XSDataResCutoff)

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginParseXdsOutput.checkParameters")

        data_input = self.dataInput
        self.checkMandatoryParameters(data_input.completeness_entries,
                                      "no completeness entries in input")

    def preProcess(self, _edObject = None):
        EDPlugin.preProcess(self)
        self.DEBUG("EDPluginResCutoff.preProcess")

    def process(self, _edObject = None):
        EDPlugin.process(self)
        detector_max_res = self.dataInput.detector_max_res
        if detector_max_res is not None:
            detector_max_res = detector_max_res.value

        completeness_cutoff_param = self.dataInput.completeness_cutoff
        if completeness_cutoff_param is None:
            completeness_cutoff = 80
        else:
            completeness_cutoff = completeness_cutoff_param.value

        isig_cutoff_param = self.dataInput.isig_cutoff
        if isig_cutoff_param is None:
            isig_cutoff = 3
        else:
            isig_cutoff = isig_cutoff_param.value

        cc_half_cutoff_param = self.dataInput.cc_half_cutoff
        if cc_half_cutoff_param is not None:
            cc_half_cutoff = cc_half_cutoff_param.value
        else:
            cc_half_cutoff = 30

        res_override = self.dataInput.res_override

        bins = list()

        # for the first iteration
        # comment from max's code: "less stringent at low res"
        local_completeness_cutoff = 70
        # declared but not initialized in the perl code
        prev_isig = prev_res = 0

        # XXX: if res is still not defined at the end it is set to
        # detector_max_res, which we should somehow defined (in the
        # data model?) and used as the default value before we start
        # the processing
        res = detector_max_res

        for entry in self.dataInput.completeness_entries:
            current_res = entry.res.value
            complete = entry.complete.value
            rfactor = entry.rfactor.value
            isig = entry.isig.value
            cc_half = entry.half_dataset_correlation.value

            #isig < isig_cutoff or \
            if cc_half < cc_half_cutoff or \
               (res_override is not None and current_res < res_override.value):
                continue
            else:
                bins.append(current_res)

        # Now the implementation of what max does when he encouters
        # the total values, which are conveniently already parsed in
        # our case
        if len(bins) < 2:
            EDVerbose.DEBUG("No bins with CC1/2 greater than %s" % cc_half_cutoff)
            EDVerbose.DEBUG("""something could be wrong, or the completeness could be too low!
bravais lattice/SG could be incorrect or something more insidious like
incorrect parameters in XDS.INP like distance, X beam, Y beam, etc.
Stopping""")
            self.setFailure()
            return
        if res is None:
            res = sorted(bins)[0]
        if res_override is not None:
            res = res_override.value

        retbins = [XSDataFloat(x) for x in bins]


        data_output = XSDataResCutoffResult()
        data_output.res = XSDataFloat(res)
        data_output.bins = retbins
        totals = self.dataInput.total_completeness
        data_output.total_complete = totals.complete
        data_output.total_rfactor = totals.rfactor
        data_output.total_isig = totals.isig

        self.dataOutput = data_output

    def postProcess(self, _edObject = None):
        EDPlugin.postProcess(self)
        self.DEBUG("EDPluginParseXdsOutput.postProcess")


# straight port of max's code, reusing the same var names (pythonized)
def _calculate_res_from_bins(prev_isig, prev_res, isig, res, isig_cutoff):
    diff_i = prev_isig - isig
    diff_d = prev_res - res

    hyp = math.sqrt((diff_i ** 2) + (diff_d ** 2))
    alpha = diff_i / diff_d

    res_id = isig_cutoff - isig
    res_offset = res_id / alpha

    return res_offset + res
