#!/usr/bin/env python
#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author: Olof Svensson (svensson@esrf.fr)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#

# Specific characterisation script for NSLS with Eiger 16M detector



#
# Set up PYTHON path for the EDNA kernel
#
# First locate EDNA_HOME and EDNA_SITE
#

import os
import re
import sys
import glob
import time
import pprint
import tempfile

strProgramPath = sys.argv[0]
strBinPath = os.path.split(strProgramPath)[0]
strMXv1Path = os.path.split(strBinPath)[0]
strEdnaHomePath = os.path.split(strMXv1Path)[0]
os.environ["EDNA_HOME"] = strEdnaHomePath
if (not "EDNA_SITE" in os.environ.keys()):
    print "Cannot start the EDNA MXv1 characterisation application:"
    print "Make sure that $EDNA_SITE is set up before running edna-mxv1-characterisation."
    print "Example:"
    print "$ export EDNA_SITE=<SUFFIX> (should be the configuration file suffix XSConfiguration_<SUFFIX>.xml)"
    print "Please read the INSTALL.txt file under the \"$EDNA_HOME/mxv1\" directory for more details"
    print ""
    sys.exit(1)
strConfigurationFilePath = os.path.join(strEdnaHomePath, "mxv1", "conf", "XSConfiguration_" + os.environ["EDNA_SITE"] + ".xml")
#
# Then add kernel/src and mxv1/src to PYTHONPATH
#
sys.path.append(os.path.join(strEdnaHomePath, "kernel", "src"))
sys.path.append(os.path.join(strEdnaHomePath, "mxv1", "src"))

# Turn on verbose mode by default
sys.argv.append("--verbose")

# Convert the Eiger HDF5 images to CBF

from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsImage import EDUtilsImage

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString
from XSDataCommon import XSDataInteger

EDFactoryPluginStatic.loadModule("XSDataControlH5ToCBFv1_1")
from XSDataControlH5ToCBFv1_1 import XSDataInputControlH5ToCBF


user = os.environ["USER"]
dateString = time.strftime("%Y%m%d", time.localtime(time.time()))
timeString = time.strftime("%H%M%S", time.localtime(time.time()))
pluginBaseDir = os.path.join("/tmp_14_days", user, dateString)
if not os.path.exists(pluginBaseDir):
    try:
        os.makedirs(pluginBaseDir, 0o755)
    except:
        pass
baseDir = tempfile.mkdtemp(prefix="{0}_autoPROC_".format(timeString),
                           dir=pluginBaseDir)
baseName = os.path.basename(baseDir)

listImages = []

# Find which images we should convert
for index in range(len(sys.argv)):
    if sys.argv[index] == "--image":
        index += 1
        while not sys.argv[index].startswith("--"):
            listImages.append(sys.argv[index])
            # Replace the .h5 image file suffix with .cbf
            sys.argv[index] = os.path.splitext(sys.argv[index])[0] + ".cbf"
            index += 1
        break

# Find the series number
firstImagePath = listImages[0]
imagePrefixAndRunNumber = EDUtilsImage.getPrefix(firstImagePath)
imageDirectory = os.path.dirname(firstImagePath)
listFilePath = glob.glob(os.path.join(imageDirectory, imagePrefixAndRunNumber + "*"))
listH5Number = []
listSerialNumber = []
#
# NSLS Eiger HDF 5 naming convention, e.g.:
# ref-XtalSamp_3_4_10_master.h5       ref-XtalSamp_3_4_11_master.h5
# ref-XtalSamp_3_4_10_data_000001.h5  ref-XtalSamp_3_4_11_data_000001.h5
#
p = re.compile('{0}_(?P<serialNumber>\d+)_data_(?P<imageNumber>\d+).h5'.format(imagePrefixAndRunNumber))
firstSerialNumber = None
for filePath in listFilePath:
    # Regular expression, looking for <prefix>_<runnumber>_data_<serialNumber>.h5
    fileName = os.path.basename(filePath)
    m = p.search(fileName)
    if m:
        dictMatch = m.groupdict()
        serialNumber = int(dictMatch["serialNumber"])
        imageNumber = int(dictMatch["imageNumber"])
        listSerialNumber.append((serialNumber, imageNumber))
        if firstSerialNumber is None or firstSerialNumber > serialNumber:
            firstSerialNumber = serialNumber



for serialNumber, imageNumber in listSerialNumber:
    imagePath = "{0}_{1:04d}.h5".format(imagePrefixAndRunNumber, int(imageNumber))
    xsDataInputControlH5ToCBF = XSDataInputControlH5ToCBF()
    xsDataInputControlH5ToCBF.hdf5File = XSDataFile(XSDataString(os.path.join(imageDirectory, imagePath)))
    newImageNumber = serialNumber - firstSerialNumber + 1
    xsDataInputControlH5ToCBF.imageNumber = XSDataInteger(1)
    xsDataInputControlH5ToCBF.hdf5ImageNumber = XSDataInteger(serialNumber)
    xsDataInputControlH5ToCBF.forcedOutputImageNumber = XSDataInteger(newImageNumber)
    edPlugin = EDFactoryPluginStatic.loadPlugin("EDPluginControlH5ToCBFv1_1")
    edPlugin.dataInput = xsDataInputControlH5ToCBF
    edPlugin.setBaseDirectory(pluginBaseDir)
    edPlugin.setBaseName(baseName)
    edPlugin.executeSynchronous()

#
# Now the edApplicationMXv1Characterisation can be imported and started
#
from EDApplicationMXv1Characterisation import EDApplicationMXv1Characterisation
edApplicationMXv1Characterisation = EDApplicationMXv1Characterisation(_strPluginName="EDPluginControlInterfacev1_2", \
                               _strConfigurationFileName=strConfigurationFilePath)
edApplicationMXv1Characterisation.execute()
