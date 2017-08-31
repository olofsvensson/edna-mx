#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008 EMBL-Grenoble, Grenoble, France
#
#    Principal authors: Sandor Brockhauser (brockhauser@embl-grenoble.fr)
#                       Olof Svensson (svensson@esrf.fr)
#                       Pierre Legrand (pierre.legrand@synchrotron-soleil.fr)
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

__authors__ = [ "Sandor Brockhauser", "Olof Svensson", "Pierre Legrand" ]
__contact__ = "brockhauser@embl-grenoble.fr"
__license__ = "LGPLv3+"
__copyright__ = "EMBL-Grenoble, Grenoble, France"
__date__ = "20120712"
__status__ = "alpha"


import os
import pprint


from EDPluginXDSv1_0 import EDPluginXDSv1_0
from EDUtilsSymmetry import EDUtilsSymmetry

from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataFloat
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

from XSDataXDSv1_0 import XSDataXDSCell
from XSDataXDSv1_0 import XSDataInputXDSIndexing
from XSDataXDSv1_0 import XSDataResultXDSIndexing


class EDPluginXDSIndexingv1_0(EDPluginXDSv1_0):


    def __init__(self):
        EDPluginXDSv1_0.__init__(self)
        self.setXSDataInputClass(XSDataInputXDSIndexing)
        self.dataOutput = XSDataResultXDSIndexing()


    def configure(self):
        EDPluginXDSv1_0.configure(self)
        self.DEBUG("EDPluginXDSIndexingv1_0.configure")
        self.addJob("XYCORR")
        self.addJob("INIT")
        self.addJob("COLSPOT")
        self.addJob("IDXREF")


    def postProcess(self, _edObject=None):
        EDPluginXDSv1_0.postProcess(self)
        self.DEBUG("EDPluginXDSIndexingv1_0.postProcess")
        pathToIdxrefLp = os.path.join(self.getWorkingDirectory(), "IDXREF.LP")
        self.dataOutput = self.readIdxrefLp(pathToIdxrefLp, self.dataOutput)


    def readIdxrefLp(self, _pathToIdxrefLp, _xsDataResultXDSIndexing=None):
        self.DEBUG("EDPluginXDSIndexingv1_0.readIdxrefLp")
        if _xsDataResultXDSIndexing is None:
            xsDataResultXDSIndexing = XSDataResultXDSIndexing()
        else:
            xsDataResultXDSIndexing = _xsDataResultXDSIndexing
        if os.path.exists(_pathToIdxrefLp):
            xsDataResultXDSIndexing.pathToLogFile = XSDataFile(XSDataString(_pathToIdxrefLp))
            with open(_pathToIdxrefLp) as f:
                listLines = f.readlines()
            indexLine = 0
            doParseParameters = False
            doParseLattice = False
            while (indexLine < len(listLines)):
                if "DIFFRACTION PARAMETERS USED AT START OF INTEGRATION" in listLines[indexLine]:
                    doParseParameters = True
                    doParseLattice = False
                elif "DETERMINATION OF LATTICE CHARACTER AND BRAVAIS LATTICE" in listLines[indexLine]:
                    doParseParameters = False
                    doParseLattice = True
                if doParseParameters:
                    if "MOSAICITY" in listLines[indexLine]:
                        mosaicity = float(listLines[indexLine].split()[-1])
                        xsDataResultXDSIndexing.mosaicity = XSDataAngle(mosaicity)
                    elif "DETECTOR COORDINATES (PIXELS) OF DIRECT BEAM" in listLines[indexLine]:
                        xBeam = float(listLines[indexLine].split()[-2])
                        yBeam = float(listLines[indexLine].split()[-1])
                        xsDataResultXDSIndexing.beamCentreX = XSDataFloat(xBeam)
                        xsDataResultXDSIndexing.beamCentreY = XSDataFloat(yBeam)
                    elif "CRYSTAL TO DETECTOR DISTANCE" in listLines[indexLine]:
                        distance = float(listLines[indexLine].split()[-1])
                        xsDataResultXDSIndexing.distance = XSDataLength(distance)
                elif doParseLattice:
                    if listLines[indexLine].startswith(" * ") and not listLines[indexLine + 1].startswith(" * "):
                        listLine = listLines[indexLine].split()
                        xsDataResultXDSIndexing.latticeCharacter = XSDataInteger(int(listLine[1]))
                        bravaisLattice = listLine[2]
                        xsDataResultXDSIndexing.bravaisLattice = XSDataString(bravaisLattice)
                        spaceGroup = EDUtilsSymmetry.getMinimumSymmetrySpaceGroupFromBravaisLattice(bravaisLattice)
                        xsDataResultXDSIndexing.spaceGroup = XSDataString(spaceGroup)
                        spaceGroupNumber = EDUtilsSymmetry.getITNumberFromSpaceGroupName(spaceGroup)
                        xsDataResultXDSIndexing.spaceGroupNumber = XSDataInteger(spaceGroupNumber)
                        xsDataResultXDSIndexing.qualityOfFit = XSDataFloat(float(listLine[3]))
                        xsDataXDSCell = XSDataXDSCell()
                        xsDataXDSCell.length_a = XSDataLength(float(listLine[4]))
                        xsDataXDSCell.length_b = XSDataLength(float(listLine[5]))
                        xsDataXDSCell.length_c = XSDataLength(float(listLine[6]))
                        xsDataXDSCell.angle_alpha = XSDataAngle(float(listLine[7]))
                        xsDataXDSCell.angle_beta = XSDataAngle(float(listLine[8]))
                        xsDataXDSCell.angle_gamma = XSDataAngle(float(listLine[9]))
                        xsDataResultXDSIndexing.unitCell = xsDataXDSCell
                indexLine += 1
        return xsDataResultXDSIndexing


