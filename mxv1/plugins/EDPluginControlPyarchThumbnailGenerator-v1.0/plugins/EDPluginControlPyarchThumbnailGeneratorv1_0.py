#
#    Project: MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2010-2014 ESRF
#
#    Principal author:        Olof Svensson
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
from EDFactoryPluginStatic import EDFactoryPluginStatic

__author__ = "Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "Copyrigth (c) 2010 ESRF"

import os, tempfile, Image, time

from EDVerbose import EDVerbose
from EDPluginControl import EDPluginControl
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsPath import EDUtilsPath

EDFactoryPluginStatic.loadModule("EDHandlerESRFPyarchv1_0")

from EDHandlerESRFPyarchv1_0 import EDHandlerESRFPyarchv1_0

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataDoubleWithUnit
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataString
from XSDataPyarchThumbnailGeneratorv1_0 import XSDataInputPyarchThumbnailGenerator
from XSDataPyarchThumbnailGeneratorv1_0 import XSDataResultPyarchThumbnailGenerator

EDFactoryPluginStatic.loadModule("XSDataMXThumbnailv1_1")
from XSDataMXThumbnailv1_1 import XSDataInputMXThumbnail

EDFactoryPluginStatic.loadModule("EDPluginMXWaitFilev1_1")
from EDPluginMXWaitFilev1_1 import EDPluginMXWaitFilev1_1
from XSDataMXWaitFilev1_1 import XSDataInputMXWaitFile


class EDPluginControlPyarchThumbnailGeneratorv1_0(EDPluginControl):
    """
    This control plugin uses EDPluginMXThumbnailv1_1 for creating two JPEG images from
    a diffraction image: one 1024x1024 (imagename.jpeg) and one 256x256 (imagename.thumb.jpeg).    
    """


    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputPyarchThumbnailGenerator)
        self.setDataOutput(XSDataResultPyarchThumbnailGenerator())
        self.strExecThumbnailPluginName = "EDPluginMXThumbnailv1_1"
        self.edPluginExecThumbnail = None
        self.strMXWaitFilePluginName = "EDPluginMXWaitFilev1_1"
        self.edPluginMXWaitFile = None
        self.strOutputPath = None
        self.strOutputPathWithoutExtension = None
        self.xsDataFilePathToThumbnail = None
        self.xsDataFilePathToThumbnail2 = None
        self.minImageSize = 1000000
        self.strSuffix = "jpeg"
        self.strImageFormat = "JPEG"


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlPyarchThumbnailGeneratorv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getDiffractionImage(), "No diffraction image file path")

    def configure(self):
        EDPluginControl.configure(self)
        self.minImageSize = self.config.get("minImageSize", self.minImageSize)
        

    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlPyarchThumbnailGeneratorv1_0.preProcess")
        # Check that the input image exists and is of the expected type
        strPathToDiffractionImage = self.dataInput.diffractionImage.path.value
        strImageFileNameExtension = os.path.splitext(strPathToDiffractionImage)[1]
        if not strImageFileNameExtension in [".img", ".marccd", ".mccd", ".cbf"]:
            self.error("Unknown image file name extension for pyarch thumbnail generator: %s" % strPathToDiffractionImage)
            self.setFailure()
        else:
            # Load the MXWaitFile plugin
            xsDataInputMXWaitFile = XSDataInputMXWaitFile()
            # Quite ugly hack to avoid lag problems at the ESRF:
            if EDUtilsPath.isESRF():
                if any( beamline in strPathToDiffractionImage for beamline in ["id23eh1", "id29"]):
                    # Pilatus 6M
                    self.minImageSize = 6000000
                elif any( beamline in strPathToDiffractionImage for beamline in ["id23eh2", "id30a1"]):
                    # Pilatus3 2M
                    self.minImageSize = 2000000
            elif EDUtilsPath.isEMBL():
                    self.minImageSize = 10000
            xsDataInputMXWaitFile.setSize(XSDataInteger(self.minImageSize))
            xsDataInputMXWaitFile.setFile(self.getDataInput().getDiffractionImage())
            if self.getDataInput().getWaitForFileTimeOut():
                xsDataInputMXWaitFile.setTimeOut(self.getDataInput().getWaitForFileTimeOut())
            self.edPluginMXWaitFile = EDPluginMXWaitFilev1_1()
            self.edPluginMXWaitFile.setDataInput(xsDataInputMXWaitFile)
            # Load the execution plugin
            self.edPluginExecThumbnail = self.loadPlugin(self.strExecThumbnailPluginName)
            xsDataInputMXThumbnail = XSDataInputMXThumbnail()
            xsDataInputMXThumbnail.image = self.getDataInput().getDiffractionImage()
            xsDataInputMXThumbnail.height = XSDataInteger(1024)
            xsDataInputMXThumbnail.width = XSDataInteger(1024)
            xsDataInputMXThumbnail.format = self.dataInput.format
            # Output path
            strImageNameWithoutExt = os.path.basename(os.path.splitext(strPathToDiffractionImage)[0])
            strImageDirname = os.path.dirname(strPathToDiffractionImage)
            if self.getDataInput().getForcedOutputDirectory():
                strForcedOutputDirectory = self.getDataInput().getForcedOutputDirectory().getPath().getValue()
                if not os.access(strForcedOutputDirectory, os.W_OK):
                    self.error("Cannot write to forced output directory : %s" % strForcedOutputDirectory)
                    self.setFailure()
                else:
                    self.strOutputPathWithoutExtension = os.path.join(strForcedOutputDirectory, strImageNameWithoutExt)
            else:
                # Try to store in the ESRF pyarch directory
                strOutputDirname = EDHandlerESRFPyarchv1_0.createPyarchFilePath(strImageDirname)
                # Check that output pyarch path exists and is writeable:
                bIsOk = False
                if strOutputDirname:
                    if not os.path.exists(strOutputDirname):
                        # Try to create the directory
                        try:
                            os.makedirs(strOutputDirname)
                            bIsOk = True
                        except Exception as e:
                            self.WARNING("Couldn't create the directory %s" % strOutputDirname)
                    elif os.access(strOutputDirname, os.W_OK):
                        bIsOk = True
                if not bIsOk:
                    self.warning("Cannot write to pyarch directory: %s" % strOutputDirname)
                    strTmpUser = os.path.join("/tmp", os.environ["USER"])
                    if not os.path.exists(strTmpUser):
                        os.mkdir(strTmpUser, 0755)
                    strOutputDirname = tempfile.mkdtemp(prefix="EDPluginPyarchThumbnailv10_", dir=strTmpUser)
                    os.chmod(strOutputDirname, 0755)
                    self.warning("Writing thumbnail images to: %s" % strOutputDirname)
                self.strOutputPathWithoutExtension = os.path.join(strOutputDirname, strImageNameWithoutExt)
            if self.dataInput.format is not None:
                self.strSuffix = self.dataInput.format.value.lower()
                self.strImageFormat = self.dataInput.format.value.upper()
            self.strOutputPath = os.path.join(self.strOutputPathWithoutExtension + "."+self.strSuffix)
            xsDataInputMXThumbnail.setOutputPath(XSDataFile(XSDataString(self.strOutputPath)))
            self.edPluginExecThumbnail.setDataInput(xsDataInputMXThumbnail)


    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginControlPyarchThumbnailGeneratorv1_0.process")
        if self.edPluginExecThumbnail and self.edPluginMXWaitFile:
            self.edPluginMXWaitFile.connectSUCCESS(self.doSuccessMXWaitFile)
            self.edPluginMXWaitFile.connectFAILURE(self.doFailureMXWaitFile)
            self.edPluginMXWaitFile.executeSynchronous()



    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlPyarchThumbnailGeneratorv1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultPyarchThumbnailGenerator()
        if self.xsDataFilePathToThumbnail:
            xsDataResult.setPathToJPEGImage(self.xsDataFilePathToThumbnail)
        if self.xsDataFilePathToThumbnail2:
            xsDataResult.setPathToThumbImage(self.xsDataFilePathToThumbnail2)
        self.setDataOutput(xsDataResult)


    def doSuccessMXWaitFile(self, _edPlugin=None):
        self.DEBUG("EDPluginControlID29CreateThumbnailv1_0.doSuccessMXWaitFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlID29CreateThumbnailv1_0.doSuccessMXWaitFile")
        # Check that the image is really there
        if not self.edPluginMXWaitFile.getDataOutput().getTimedOut().getValue():
            # Workaround for ESRF lag problem
            if EDUtilsPath.isESRF():
                time.sleep(2)
            # The image is here - make the first thumbnail
            self.edPluginExecThumbnail.connectSUCCESS(self.doSuccessExecThumbnail)
            self.edPluginExecThumbnail.connectFAILURE(self.doFailureExecThumbnail)
            self.edPluginExecThumbnail.executeSynchronous()
        else:
            self.error("Time-out while waiting for image!")
            self.setFailure()


    def doFailureMXWaitFile(self, _edPlugin=None):
        self.DEBUG("EDPluginControlID29CreateThumbnailv1_0.doFailureMXWaitFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlID29CreateThumbnailv1_0.doFailureMXWaitFile")
        # To be removed if failure of the exec plugin shouldn't make the control plugin to fail:
        self.setFailure()


    def doSuccessExecThumbnail(self, _edPlugin=None):
        self.DEBUG("EDPluginControlPyarchThumbnailGeneratorv1_0.doSuccessExecThumbnail")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginControlPyarchThumbnailGeneratorv1_0.doSuccessExecThumbnail")
        self.xsDataFilePathToThumbnail = self.edPluginExecThumbnail.dataOutput.thumbnail
        # Retrieve the output path
        pathToThumbnail = self.xsDataFilePathToThumbnail.path.value
        outfile = os.path.splitext(pathToThumbnail)[0] + ".thumb." + self.strSuffix
        size = [256, 256]
        im = Image.open(pathToThumbnail)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(outfile, self.strImageFormat)
        self.xsDataFilePathToThumbnail2 = XSDataFile(XSDataString(outfile))


    def doFailureExecThumbnail(self, _edPlugin=None):
        self.DEBUG("EDPluginControlPyarchThumbnailGeneratorv1_0.doFailureExecThumbnail")
        self.retrieveFailureMessages(_edPlugin, "EDPluginControlPyarchThumbnailGeneratorv1_0.doFailureExecThumbnail")
        # To be removed if failure of the exec plugin shouldn't make the control plugin to fail:
        self.setFailure()


