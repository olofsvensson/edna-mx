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
import shutil
import traceback
import subprocess

# for the chmod constants
from stat import *

from EDUtilsPath import EDUtilsPath
from EDPluginControl import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataCommon import XSDataStatus, XSDataBoolean, XSDataResult, XSDataString, XSDataDouble
from XSDataEDNAprocv1_0 import XSDataFileConversion, XSDataFileConversionOut

EDFactoryPluginStatic.loadModule("XSDataCCP4v1_0")
from XSDataCCP4v1_0 import XSDataAimless
from XSDataCCP4v1_0 import XSDataPointless
from XSDataCCP4v1_0 import XSDataTruncate
from XSDataCCP4v1_0 import XSDataUniqueify

class EDPluginControlFileConversionv1_0(EDPluginControl):
    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataFileConversion)
        self.setDataOutput(XSDataFileConversionOut())
        self.strAnomSuffix = None

    def configure(self):
        EDPluginControl.configure(self)

    def preProcess(self):
        EDPluginControl.preProcess(self)
        self.DEBUG('FileConversion: preprocess')
        infile = self.dataInput.input_file.value
        outfile = self.dataInput.output_file.value

        self.pointless = self.loadPlugin("EDPluginExecPointlessv1_0")
        self.aimless = self.loadPlugin("EDPluginExecAimlessv1_0")
        self.truncate = self.loadPlugin("EDPluginExecTruncatev1_0")
        self.uniqueify = self.loadPlugin("EDPluginExecUniqueifyv1_0")

        self.strAnomSuffix = "noanom"
        if self.dataInput.anom is not None and self.dataInput.anom.value:
             self.strAnomSuffix = "anom"

        if self.dataInput.image_prefix is not None:
            self.image_prefix = self.dataInput.image_prefix.value + '_'
        else:
            self.image_prefix = ''

        # TODO: change that to a directory in the data model
        self.results_dir = os.path.join(os.path.dirname(self.dataInput.output_file.value))
        self.pointless_out = "ep_{0}unmerged_{1}_pointless_multirecord.mtz".format(self.image_prefix, self.strAnomSuffix)
        self.truncate_out = 'ep_{0}{1}_truncate.mtz'.format(self.image_prefix, self.strAnomSuffix)
        self.aimless_out = 'ep_{0}{1}_aimless.mtz'.format(self.image_prefix, self.strAnomSuffix)
        self.aimless_commands_out = 'ep_{0}{1}_aimless.inp'.format(self.image_prefix, self.strAnomSuffix)


    def checkParameters(self):
        self.DEBUG('FileConversion: checkParameters')
        self.checkMandatoryParameters(self.dataInput.input_file, 'no input file')
        self.checkMandatoryParameters(self.dataInput.output_file, 'no output file')

        # now really check the parameters
        if self.dataInput.input_file is not None:
            path = self.dataInput.input_file.value
            if not os.path.exists(path):
                strErrorMessage = "Input file {0} does not exist".format(path)
                self.ERROR(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
                return

    def process(self):
        self.DEBUG('FileConversion: process')
        EDPluginControl.process(self)
        # first we generate the intermediary file name
        pointless_in = XSDataPointless()
        pointless_in.input_file = self.dataInput.input_file
        pointless_out = os.path.join(os.path.dirname(self.dataInput.output_file.value),
                                     self.pointless_out)
        pointless_in.output_file = XSDataString(pointless_out)
        if self.dataInput.choose_spacegroup is not None:
            pointless_in.choose_spacegroup = self.dataInput.choose_spacegroup
        self.pointless.dataInput = pointless_in
        self.screen("Pointless run " + self.strAnomSuffix)
        self.pointless.executeSynchronous()
        if self.pointless.isFailure():
            strErrorMessage = "Pointless {0} failed".format(self.strAnomSuffix)
            self.ERROR(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
            return

        aimless_in = XSDataAimless()
        aimless_in.input_file = pointless_in.output_file
        aimless_in.output_file = XSDataString(os.path.join(self.results_dir,
                                                           self.aimless_out))
        aimless_in.command_file = XSDataString(os.path.join(self.results_dir,
                                                            self.aimless_commands_out))
        aimless_in.dataCollectionID = self.dataInput.dataCollectionID
        aimless_in.start_image = self.dataInput.start_image
        aimless_in.end_image = self.dataInput.end_image
        aimless_in.res = self.dataInput.res
        aimless_in.anom = self.dataInput.anom

        self.aimless.dataInput = aimless_in
        self.screen("Aimless run " + self.strAnomSuffix)
        self.aimless.executeSynchronous()
        if self.aimless.isFailure():
            strErrorMessage = "Aimless {0} failed".format(self.strAnomSuffix)
            self.ERROR(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
            return

        # copy the aimless log where the results files are
        source_log = os.path.join(self.aimless.getWorkingDirectory(),
                                  self.aimless.getScriptLogFileName())
        self.aimless_log = source_log
        target_log = os.path.join(self.results_dir,
                                  'ep_{0}aimless_{1}.log'.format(self.image_prefix,
                                                              "anom" if self.dataInput.anom.value else "noanom"))
        try:
            shutil.copyfile(source_log, target_log)
        except IOError:
            self.ERROR('Could not copy aimless log file from {0} to {1}'.format(source_log,
                                                                                target_log))

        # now truncate
        truncate_in = XSDataTruncate()
        truncate_in.input_file = self.aimless.dataInput.output_file
        temp_file = tempfile.NamedTemporaryFile(suffix='.mtz',
                                                prefix='tmp2-',
                                                dir=self.aimless.getWorkingDirectory(),
                                                delete=False)
        truncate_out = temp_file.name
        temp_file.close()
        os.chmod(truncate_out, S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH)
        truncate_in.output_file = XSDataString(truncate_out)

        truncate_in.nres = self.dataInput.nres
        truncate_in.anom = self.dataInput.anom
        truncate_in.res = self.dataInput.res

        self.truncate.dataInput = truncate_in
        self.screen("Truncate run " + self.strAnomSuffix)
        self.truncate.executeSynchronous()
        if self.truncate.isFailure():
            strErrorMessage = "Truncate {0} failed".format(self.strAnomSuffix)
            self.ERROR(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
            return

        # copy the truncate log where the results files are
        source_log = os.path.join(self.truncate.getWorkingDirectory(),
                                  self.truncate.getScriptLogFileName())
        target_log = os.path.join(self.results_dir,
                                  'ep_{0}truncate_{1}.log'.format(self.image_prefix,
                                                               "anom" if self.dataInput.anom.value else "noanom"))
        try:
            shutil.copyfile(source_log,
                            target_log)
        except IOError:
            self.ERROR('Could not copy truncate log file from {0} to {1}'.format(source_log,
                                                                                 target_log))

        # and finally uniqueify
        uniqueify_in = XSDataUniqueify()
        uniqueify_in.input_file = truncate_in.output_file
        uniqueify_out = os.path.join(self.results_dir,
                                     self.truncate_out)
        uniqueify_in.output_file = XSDataString(uniqueify_out)

        self.uniqueify.dataInput = uniqueify_in

        if EDUtilsPath.isEMBL() or EDUtilsPath.isALBA():
           # GB: skipping misteriously failing uniqueify run -
           #    which is useless anyway.
           #    copying temp truncate output to results directly
           shutil.copyfile(uniqueify_in.input_file.value, uniqueify_out)
           return

        self.screen("Uniqueify run " + self.strAnomSuffix)
        self.uniqueify.executeSynchronous()
        if self.uniqueify.isFailure():
            strErrorMessage = "Uniqueify {0} failed".format(self.strAnomSuffix)
            self.ERROR(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
            return

    def postProcess(self):
        self.DEBUG('FileConversion: postProcess')
        EDPluginControl.postProcess(self)
        output_file = self.dataInput.output_file.value

        # gzip the aimless unmerged file
        aimless_unmerged_out = 'ep_{0}{1}_aimless_unmerged.mtz'.format(self.image_prefix, self.strAnomSuffix)
        aimless_unmerged_path = os.path.join(os.path.dirname(self.dataInput.output_file.value),
                                             aimless_unmerged_out)
        try:
            self.DEBUG("gzip'ing aimless unmerged file {0}".format(aimless_unmerged_path))
            subprocess.call(['gzip', aimless_unmerged_path])
        except Exception:
            self.DEBUG("gzip'ing the file failed: {0}".format(traceback.format_exc()))

        # gzip the pointless multirecord file
        pointless_out = os.path.join(os.path.dirname(self.dataInput.output_file.value),
                                     self.pointless_out)
        try:
            self.DEBUG("gzip'ing pointless multirecord file {0}".format(pointless_out))
            subprocess.call(['gzip', pointless_out])
        except Exception:
            self.DEBUG("gzip'ing the file failed: {0}".format(traceback.format_exc()))

        res = XSDataFileConversionOut()
        status = XSDataStatus()
        status.isSuccess = XSDataBoolean(os.path.exists(self.uniqueify.dataInput.output_file.value))
        res.status = status
        res.pointless_sgnumber = self.pointless.dataOutput.sgnumber
        res.pointless_sgstring = self.pointless.dataOutput.sgstr
        res.pointless_cell = [XSDataDouble(self.pointless.dataOutput.cell.length_a.value),
                              XSDataDouble(self.pointless.dataOutput.cell.length_b.value),
                              XSDataDouble(self.pointless.dataOutput.cell.length_c.value),
                              XSDataDouble(self.pointless.dataOutput.cell.angle_alpha.value),
                              XSDataDouble(self.pointless.dataOutput.cell.angle_beta.value),
                              XSDataDouble(self.pointless.dataOutput.cell.angle_gamma.value)]
        res.aimless_log = XSDataString(self.aimless_log)
        self.dataOutput = res
