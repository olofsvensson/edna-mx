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
import time
import shutil

from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDUtilsImage import EDUtilsImage
from EDUtilsPath import EDUtilsPath

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

from XSDataH5ToCBFv1_1 import XSDataInputH5ToCBF
from XSDataH5ToCBFv1_1 import XSDataResultH5ToCBF

class EDPluginH5ToCBFv1_1(EDPluginExecProcessScript):
    """
    This plugin runs the 'MOSFLM' converter (eiger2cbf or minicbf) 
    to create CBF files from Eiger HDF5 images. 
    """


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputH5ToCBF)
        self.setDataOutput(XSDataResultH5ToCBF())
        self.CBFFile = None
        self.CBFFileTemplate = None
        self.tmpCBFFile = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginH5ToCBFv1_1.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.hdf5File, "HDF5 file is None")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginH5ToCBFv1_1.preProcess")
        xsDataInputH5ToCBF = self.getDataInput()
        self.setScriptCommandline(self.generateCommands(xsDataInputH5ToCBF))



    def process(self, _edObject=None):
        EDPluginExecProcessScript.process(self)
        self.DEBUG("EDPluginH5ToCBFv1_1.process")

    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginH5ToCBFv1_1.postProcess")



    def finallyProcess(self, _edObject=None):
        EDPluginExecProcessScript.finallyProcess(self)
        self.DEBUG("EDPluginH5ToCBFv1_1.finallyProcess")
        if self.CBFFile is not None:
            if os.path.exists(self.CBFFile):
                self.dataOutput.outputCBFFile = XSDataFile(XSDataString(self.CBFFile))
        elif self.CBFFileTemplate is not None:
            self.dataOutput.outputCBFFileTemplate = XSDataFile(XSDataString(self.CBFFileTemplate))


    def generateCommands(self, _xsDataInputH5ToCBF):
        """
        This method creates a list of commands for the converter
        """
        self.DEBUG("EDPluginH5ToCBFv1_1.generateCommands")

        hdf5File = _xsDataInputH5ToCBF.hdf5File.path.value
        directory = os.path.dirname(hdf5File)
        prefix = EDUtilsImage.getPrefix(hdf5File)

        if _xsDataInputH5ToCBF.imageNumber is not None:
            imageNumber = _xsDataInputH5ToCBF.imageNumber.value

            if _xsDataInputH5ToCBF.hdf5ImageNumber is None:
                hdf5ImageNumber = imageNumber
            else:
                hdf5ImageNumber = _xsDataInputH5ToCBF.hdf5ImageNumber.value

            if "master" in hdf5File:
                masterFile = hdf5File
            else:
                if EDUtilsPath.isESRF():
                    masterFile = os.path.join(directory, prefix + "_{0}_master.h5".format(hdf5ImageNumber))
                else:
                    masterFile = os.path.join(directory, prefix + "_master.h5".format(hdf5ImageNumber))

            if _xsDataInputH5ToCBF.forcedOutputImageNumber is not None:
                CBFFileName = prefix + "_%04d" % _xsDataInputH5ToCBF.forcedOutputImageNumber.value + ".cbf"
                imageNumberInHdf5File = imageNumber
            else:
                CBFFileName = prefix + "_%04d" % imageNumber + ".cbf"
                imageNumberInHdf5File = imageNumber - hdf5ImageNumber + 1

            tmpCBFFileName = "tmp_" + CBFFileName

            if _xsDataInputH5ToCBF.forcedOutputDirectory is None:
                self.CBFFile = os.path.join(directory, CBFFileName)
            else:
                forcedOutputDirectory = self.dataInput.forcedOutputDirectory.path.value
                if not os.path.exists(forcedOutputDirectory):
                    os.makedirs(forcedOutputDirectory, 0o755)
                self.CBFFile = os.path.join(forcedOutputDirectory, CBFFileName)

            scriptCommandLine = "{0} {1} {2}".format(masterFile, imageNumberInHdf5File, self.CBFFile)

        elif _xsDataInputH5ToCBF.startImageNumber is not None and _xsDataInputH5ToCBF.endImageNumber is not None:

            startImageNumber = _xsDataInputH5ToCBF.startImageNumber.value
            endImageNumber = _xsDataInputH5ToCBF.endImageNumber.value

            if _xsDataInputH5ToCBF.hdf5ImageNumber is None:
                hdf5ImageNumber = startImageNumber
            else:
                hdf5ImageNumber = _xsDataInputH5ToCBF.hdf5ImageNumber.value

            if "master" in hdf5File:
                masterFile = hdf5File
            else:
                masterFile = os.path.join(directory, prefix + "_{0}_master.h5".format(hdf5ImageNumber))

            CBFFileNamePrefix = prefix + "_"

            if _xsDataInputH5ToCBF.forcedOutputDirectory is None:
                CBFFilePath = os.path.join(directory, CBFFileNamePrefix)
            else:
                forcedOutputDirectory = self.dataInput.forcedOutputDirectory.path.value
                if not os.path.exists(forcedOutputDirectory):
                    os.makedirs(forcedOutputDirectory, 0o755)
                CBFFilePath = os.path.join(forcedOutputDirectory, CBFFileNamePrefix)

            scriptCommandLine = "{0} {1}:{2} {3}".format(masterFile, startImageNumber, endImageNumber, CBFFilePath)

            self.CBFFileTemplate = CBFFilePath + "######.cbf"

        return scriptCommandLine

