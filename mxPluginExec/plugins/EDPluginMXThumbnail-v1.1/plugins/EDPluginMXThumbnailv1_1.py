# coding: utf8
#
#    Project: <projectName>
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
__date__ = "20120712"
__status__ = "production"

import os
import numpy
import fabio
import scipy.ndimage
try:
    import Image
    import ImageFile
    import ImageOps
except:
    from PIL import Image
    from PIL import ImageFile
    from PIL import ImageOps
    
from EDPluginExec import EDPluginExec
from EDUtilsFile import EDUtilsFile
from EDUtilsPlatform import EDUtilsPlatform

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

from XSDataMXThumbnailv1_1 import XSDataInputMXThumbnail
from XSDataMXThumbnailv1_1 import XSDataResultMXThumbnail

class EDPluginMXThumbnailv1_1(EDPluginExec):
    

    def __init__(self):
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputMXThumbnail)
        self.setDataOutput(XSDataResultMXThumbnail())
        self.minLevel = 0
        self.maxLevel = 99.95 # %
        self.dilatation = 4
        self.format = "jpg"
        self.width = 512
        self.height = 512
        self.output = None


    def checkParameters(self):
        self.DEBUG("EDPluginExecPlotGlev1_1.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.image, "Input image is None")

    
    def process(self, _edObject=None):
        EDPluginExec.process(self)
        imageFileName = os.path.basename(self.dataInput.image.path.value)
        # Default format
        strSuffix = "jpg"
        strPILFormat = "JPEG"
        # Check if format is provided
        if self.dataInput.format is not None:
            strFormat = self.dataInput.format.value
            if strFormat.lower() == "png":
                strSuffix = "png"
                strPILFormat = "PNG"
        # The following code has been adapted from EDPluginExecThumbnail written by J.Kieffer
        fabioImage = fabio.openimage.openimage(self.dataInput.image.path.value)
        numpyImage = fabioImage.data
        dtype = numpyImage.dtype
        sortedArray = numpyImage.flatten()
        sortedArray.sort()
        numpyImage = numpy.maximum(numpyImage, int(self.minLevel) * numpy.ones_like(numpyImage))
        maxLevel = sortedArray[int(round(float(self.maxLevel) * sortedArray.size / 100.0))]
        numpyImage = numpy.minimum(numpyImage, maxLevel * numpy.ones_like(numpyImage))
        numpyImage = scipy.ndimage.morphology.grey_dilation(numpyImage, (self.dilatation, self.dilatation))
        mumpyImageFloat = (numpyImage.astype(numpy.float32)) / float(maxLevel)
        numpyImageInt = ( mumpyImageFloat * 255.0 ).astype(numpy.uint8)
        pilOutputImage = ImageOps.invert(Image.fromarray(numpyImageInt, 'L'))
        if self.dataInput.height is not None and self.dataInput.width is not None:
            pilOutputImage = pilOutputImage.resize((self.dataInput.width.value, self.dataInput.height.value), Image.ANTIALIAS)
        if self.dataInput.outputPath is None:
            outputPath = os.path.join(self.getWorkingDirectory(), os.path.splitext(imageFileName)[0] + "." + strSuffix)
        else:
            outputPath = self.dataInput.outputPath.path.value
        self.DEBUG("Output thumbnail path: %s" % outputPath)
        self.width, self.height = pilOutputImage.size
        if self.width * self.height > ImageFile.MAXBLOCK:
            ImageFile.MAXBLOCK = self.width * self.height
        pilOutputImage.save(outputPath, strPILFormat, quality=85, optimize=True)
        self.dataOutput.thumbnail = XSDataFile(XSDataString(outputPath))
        
        