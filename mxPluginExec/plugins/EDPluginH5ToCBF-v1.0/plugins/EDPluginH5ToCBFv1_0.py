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

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

from XSDataH5ToCBFv1_0 import XSDataInputH5ToCBF
from XSDataH5ToCBFv1_0 import XSDataResultH5ToCBF

class EDPluginH5ToCBFv1_0(EDPluginExecProcessScript):
    """
    This plugin runs H5ToXDS to create CBF files from an Eiger HDF5 file. 
    """


    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputH5ToCBF)
        self.setDataOutput(XSDataResultH5ToCBF())
        self.CBFFile = None
        self.tmpCBFFile = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginH5ToCBFv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.hdf5File, "HDF5 file is None")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginH5ToCBFv1_0.preProcess")
        xsDataInputH5ToCBF = self.getDataInput()
        self.setScriptCommandline(self.generateCommands(xsDataInputH5ToCBF))



    def process(self, _edObject=None):
        EDPluginExecProcessScript.process(self)
        self.DEBUG("EDPluginH5ToCBFv1_0.process")

    def postProcess(self, _edObject=None):
        EDPluginExecProcessScript.postProcess(self)
        self.DEBUG("EDPluginH5ToCBFv1_0.postProcess")

        if self.dataInput.dataCollection is None:
            shutil.copy(self.tmpCBFFile, self.CBFFile)
        else:
            # Fill in metadata
            fileTmpCBF = open(self.tmpCBFFile)
            tmpCBF = fileTmpCBF.read()
            fileTmpCBF.close()

            # Replace opening line
            tmpCBF = tmpCBF.replace("CBF: VERSION 1.5, CBFlib v0.7.8 - SLS/DECTRIS PILATUS detectors",
                                    "CBF: VERSION 1.5, CBFlib v0.7.8")


            index1 = tmpCBF.find("# WARNING: FOR XDS PROCESSING ONLY.")
            string2 = "# SOFTWARE VERSION: 1.1.0-RELEASE"
            index2 = tmpCBF.find(string2) + len(string2)

            miniCBFHeader = self.generateMiniCBFHeader(self.dataInput)

            newCBF = tmpCBF[:index1] + miniCBFHeader + tmpCBF[index2:]
            newCBFFile = open(self.CBFFile, "w")
            newCBFFile.write(newCBF)
            newCBFFile.close()



    def finallyProcess(self, _edObject=None):
        EDPluginExecProcessScript.finallyProcess(self)
        self.DEBUG("EDPluginH5ToCBFv1_0.finallyProcess")
        if self.tmpCBFFile is not None:
            if os.path.exists(self.tmpCBFFile):
                os.remove(self.tmpCBFFile)
        if self.CBFFile is not None:
            if os.path.exists(self.CBFFile):
                self.dataOutput.outputCBFFile = XSDataFile(XSDataString(self.CBFFile))


    def generateCommands(self, _xsDataInputH5ToCBF):
        """
        This method creates a list of commands for H5ToXDS
        """
        self.DEBUG("EDPluginH5ToCBFv1_0.generateCommands")

        hdf5File = _xsDataInputH5ToCBF.hdf5File.path.value
        directory = os.path.dirname(hdf5File)
        prefix = EDUtilsImage.getPrefix(hdf5File)

        imageNumber = _xsDataInputH5ToCBF.imageNumber.value

        if _xsDataInputH5ToCBF.hdf5ImageNumber is None:
            hdf5ImageNumber = imageNumber
        else:
            hdf5ImageNumber = _xsDataInputH5ToCBF.hdf5ImageNumber.value

        if "master" in hdf5File:
            masterFile = hdf5File
        else:
            masterFile = os.path.join(directory, prefix + "_{0}_master.h5".format(hdf5ImageNumber))

        CBFFileName = prefix + "_%04d" % imageNumber + ".cbf"
        tmpCBFFileName = "tmp_" + CBFFileName

        if self.dataInput.forcedOutputDirectory is None:
            self.CBFFile = os.path.join(directory, CBFFileName)
        else:
            forcedOutputDirectory = self.dataInput.forcedOutputDirectory.path.value
            if not os.path.exists(forcedOutputDirectory):
                os.makedirs(forcedOutputDirectory, 0o755)
            self.CBFFile = os.path.join(forcedOutputDirectory, CBFFileName)

        self.tmpCBFFile = os.path.join(self.getWorkingDirectory(), tmpCBFFileName)

        scriptCommandLine = "{0} {1} {2}".format(masterFile, imageNumber - hdf5ImageNumber + 1, tmpCBFFileName)

        return scriptCommandLine

    def generateMiniCBFHeader(self, _xsDataInputH5ToCBF):
        dataCollection = _xsDataInputH5ToCBF.dataCollection
        miniCBFHeader = ""
        miniCBFHeader += "# Detector: Dectris Eiger 4M, S/N E-08-0104, ESRF ID30a3\r\n"
        miniCBFHeader += "# {0}\r\n".format(dataCollection.startTime)
        miniCBFHeader += "# Pixel_size 75e-6 m x 75e-6 m\r\n"
        miniCBFHeader += "# Silicon sensor, thickness 0.000320 m\r\n"
        miniCBFHeader += "# Oscillation_axis omega\r\n"
        miniCBFHeader += "# Chi 0.0000 deg\r\n"
        miniCBFHeader += "# Angle_increment {0:.4f} deg.\r\n".format(dataCollection.axisRange)
        miniCBFHeader += "# Polarization 0.99\r\n"
        miniCBFHeader += "# file_comments\r\n"
        miniCBFHeader += "# N_oscillations 1\r\n"
        xbeam = dataCollection.xbeam
        ybeam = dataCollection.ybeam
        miniCBFHeader += "# Beam_xy ({0:.2f}, {1:.2f}) pixels\r\n".format(xbeam / 0.075, ybeam / 0.075)
        miniCBFHeader += "# Exposure_time {0:.6f} s\r\n".format(dataCollection.exposureTime)
        miniCBFHeader += "# Phi 0.0020 deg.\r\n"
        miniCBFHeader += "# Energy_range (0, 0) eV\r\n"
        miniCBFHeader += "# Start_angle {0:.4f} deg.\r\n".format(dataCollection.axisStart)
        miniCBFHeader += "# Detector_distance {0:.6f} m\r\n".format(dataCollection.detectorDistance / 1000.0)
        miniCBFHeader += "# Detector_Voffset 0.0000 m\r\n"
        miniCBFHeader += "# Alpha 0.0000 deg.\r\n"
        miniCBFHeader += "# Flat_field: (nil)\r\n"
        miniCBFHeader += "# Threshold_setting 5980 eV\r\n"
        miniCBFHeader += "# Exposure_period 0.020950 s\r\n"
        miniCBFHeader += "# N_excluded_pixels: = 321\r\n"
        miniCBFHeader += "# Kappa 0.0020 deg.\r\n"
        miniCBFHeader += "# Tau = 0 s\r\n"
        miniCBFHeader += "# Transmission {0:.2f}\r\n".format(dataCollection.transmission)
        miniCBFHeader += "# Detector_2theta 0.0000 deg.\r\n"
        miniCBFHeader += "# Flux {0:.1f}\r\n".format(dataCollection.flux)
        miniCBFHeader += "# Count_cutoff 1048500\r\n"
        miniCBFHeader += "# Trim_directory: (nil)\r\n"
        miniCBFHeader += "# Wavelength {0:.6f} A".format(dataCollection.wavelength)
        return miniCBFHeader

# Detector: PILATUS3 6M, S/N 60-0128, ESRF ID29
# 2015/Mar/04 09:13:22
# Pixel_size 172e-6 m x 172e-6 m
# Silicon sensor, thickness 0.000320 m
# Oscillation_axis omega
# Excluded_pixels:  badpix_mask.tif
# Chi 0.0000 deg.
# Angle_increment 0.1000 deg.
# Polarization 0.99
# file_comments
# N_oscillations 1
# Beam_xy (1227.22, 1255.72) pixels
# Exposure_time 0.020000 s
# Phi 0.0020 deg.
# Energy_range (0, 0) eV
# Start_angle 360.0000 deg.
# Detector_distance 0.473644 m
# Detector_Voffset 0.0000 m
# Alpha 0.0000 deg.
# Flat_field: (nil)
# Threshold_setting 5980 eV
# Exposure_period 0.020950 s
# N_excluded_pixels: = 321
# Kappa 0.0020 deg.
# Tau = 0 s
# Transmission 36.0243526077
# Detector_2theta 0.0000 deg.
# Flux 0.0
# Count_cutoff 1048500
# Trim_directory: (nil)
# Wavelength 1.243944 A

