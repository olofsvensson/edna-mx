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

import re
import os.path
import tempfile

from EDPluginControl import EDPluginControl

from XSDataCommon import XSDataStatus, XSDataBoolean, XSDataResult, XSDataString
from XSDataEDNAprocv1_0 import XSDataEDNAprocImport, XSDataEDNAprocImportOut
from XSDataEDNAprocv1_0 import XSDataFileConversion

OUTFILE_TEMPLATE = 'unmerged_{0}.mtz'

class EDPluginControlEDNAprocImportv1_0(EDPluginControl):
    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataEDNAprocImport)
        self.setDataOutput(XSDataEDNAprocImportOut())
        self.anom = None
        self.noanom = None

    def configure(self):
        EDPluginControl.configure(self)

    def preProcess(self):
        EDPluginControl.preProcess(self)
        self.DEBUG('Import : preprocess')
        tocopy = ['dataCollectionID', 'start_image', 'end_image',
                  'res', 'nres', 'image_prefix']

        if self.dataInput.input_anom:
            self.anom = self.loadPlugin('EDPluginControlFileConversionv1_0')
            anom_in = XSDataFileConversion()
            for a in tocopy:
                setattr(anom_in, a, getattr(self.dataInput, a))
            anom_in.anom = XSDataBoolean(True)
            anom_in.input_file = self.dataInput.input_anom
            anom_in.output_file = XSDataString(os.path.join(self.outdir, OUTFILE_TEMPLATE.format('anom')))
            anom_in.choose_spacegroup = self.dataInput.choose_spacegroup
            self.anom.dataInput = anom_in

        if self.dataInput.input_noanom:
            self.noanom = self.loadPlugin('EDPluginControlFileConversionv1_0')
            noanom_in = XSDataFileConversion()
            for a in tocopy:
                setattr(noanom_in, a, getattr(self.dataInput, a))
            noanom_in.anom = XSDataBoolean(False)
            noanom_in.input_file = self.dataInput.input_noanom
            noanom_in.output_file = XSDataString(os.path.join(self.outdir, OUTFILE_TEMPLATE.format('noanom')))
            noanom_in.choose_spacegroup = self.dataInput.choose_spacegroup
            self.noanom.dataInput = noanom_in


    def checkParameters(self):
        # NB. we'll only check for the output directory existence for
        # now
        self.DEBUG('Import: checkParameters')
        outdir = self.dataInput.output_directory
        if outdir is None:
            strErrorMessage = "File Import: output directory not specified: aborting"
            self.ERROR(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
            return

        self.outdir = outdir.value
        if not os.path.exists(self.outdir) and not os.path.isdir(self.outdir):
            strErrorMessage = "File Import: output directory is not a directory"
            self.ERROR(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
            return


    def process(self):
        self.DEBUG('Import: process')
        EDPluginControl.process(self)

        # start all plugins
        for p in self.getListOfLoadedPlugin():
            p.execute()

        self.synchronizePlugins()

    def postProcess(self):
        self.DEBUG('Import: postProcess')
        EDPluginControl.postProcess(self)

        res = XSDataEDNAprocImportOut()
        status = XSDataStatus()
        res.status = status
        if self.dataInput.input_anom and self.dataInput.input_noanom:
            all_good = not self.anom.isFailure() and not self.noanom.isFailure()
        elif self.dataInput.input_anom:
            all_good = not self.anom.isFailure()
        else:
            all_good = not self.noanom.isFailure()
        status.isSuccess = XSDataBoolean(all_good)
        files = list()
        if self.dataInput.input_anom and not self.anom.isFailure():
            files.append(self.anom.dataInput.output_file)
        if self.dataInput.input_noanom and not self.noanom.isFailure():
            files.append(self.noanom.dataInput.output_file)
        res.files = files

        if self.noanom:
            res.pointless_sgnumber = self.noanom.dataOutput.pointless_sgnumber
            res.pointless_sgstring = self.noanom.dataOutput.pointless_sgstring
            res.pointless_cell = self.noanom.dataOutput.pointless_cell
        else:
            res.pointless_sgnumber = self.anom.dataOutput.pointless_sgnumber
            res.pointless_sgstring = self.anom.dataOutput.pointless_sgstring
            res.pointless_cell = self.anom.dataOutput.pointless_cell

        if self.dataInput.input_anom:
            res.aimless_log_anom = self.anom.dataOutput.aimless_log

        if self.dataInput.input_noanom:
            res.aimless_log_noanom = self.noanom.dataOutput.aimless_log

        self.dataOutput = res
