#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20141216"
__status__ = "production"

import os, shutil, gzip

from EDPluginExecProcessScript import EDPluginExecProcessScript
from EDConfiguration import EDConfiguration
from EDUtilsFile import EDUtilsFile


from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataDouble

from XSDataPhenixv1_1 import XSDataTwinLawsStatistics
from XSDataPhenixv1_1 import XSDataInputPhenixXtriage
from XSDataPhenixv1_1 import XSDataResultPhenixXtriage


class EDPluginPhenixXtriagev1_1(EDPluginExecProcessScript):
    """
    This plugin runs the phenix.xtriage command.
    """
    

    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputPhenixXtriage)
        self.setDataOutput(XSDataResultPhenixXtriage())
        self.strPathToLocalMtz = None


    def preProcess(self, _edObject=None):
        """
        Sets up the phenix.xtriage command line, uncompress mtz file if necessary
        """
        EDPluginExecProcessScript.preProcess(self, _edObject)
        self.DEBUG("EDPluginPhenixXtriagev1_1.preProcess...")
        # Check if we have a compressed mtz file...
        strPathMtz = self.dataInput.mtzFile.path.value
        if strPathMtz.endswith(".gz"):
            fIn = gzip.open(strPathMtz, "rb")
            fileContent = fIn.read()
            fIn.close()
            strMtzFileName = os.path.basename(strPathMtz).split(".gz")[0]
            self.strPathToLocalMtz = os.path.join(self.getWorkingDirectory(), strMtzFileName)
            fOut = open(self.strPathToLocalMtz, "wb")
            fOut.write(fileContent)
            fOut.close()
            strPathMtz = self.strPathToLocalMtz
        if self.dataInput.obsLabels is not None:
            strObsLabels = self.dataInput.obsLabels.value
        else:
            strObsLabels = "I,SIGI,merged"
        strCommandPhenixXtriage = "{0} obs={1}".format(strPathMtz, strObsLabels)
        # Necessary for Python 3 environment:
        self.addListCommandPreExecution("unset PYTHONPATH")
        self.setScriptCommandline(strCommandPhenixXtriage)

    def postProcess(self, _edObject=None):
        """
        Parses the phenix.xtriage log fil and the generated MOSFLM script
        """
        strPathLogFile = os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName())
        self.dataOutput = self.parseLogFile(strPathLogFile)

    def finallyProcess(self, _edObject=None):
        EDPluginExecProcessScript.finallyProcess(self, _edObject)
        self.DEBUG("EDPluginPhenixXtriagev1_1.finallyProcess")
        # Remove local mtz file if any
        if self.strPathToLocalMtz is not None and os.path.exists(self.strPathToLocalMtz):
            os.remove(self.strPathToLocalMtz)


    def parseLogFile(self, _strPathToLogFile):
        xsDataResultPhenixXtriage = XSDataResultPhenixXtriage()
        hasTwinning = False
        hasPseudotranslation = False
        if os.path.exists(_strPathToLogFile):
            xsDataResultPhenixXtriage.logFile = XSDataFile(XSDataString(_strPathToLogFile))
            strLog = EDUtilsFile.readFile(_strPathToLogFile)
            iIndex = 0
            listLines = strLog.split("\n")
            bContinue = True
            while bContinue:
                
                if listLines[iIndex].startswith("Statistics depending on twin laws"):
                    #------------------------------------------------------
                    #| Operator | type | R obs. | Britton alpha | H alpha |
                    #------------------------------------------------------
                    #| k,h,-l   |  PM  | 0.025  | 0.458         | 0.478   |
                    #| -h,k,-l  |  PM  | 0.017  | 0.459         | 0.487   |
                    #------------------------------------------------------
                    iIndex +=4
                    while not listLines[iIndex].startswith("---------"):
                        listLine = listLines[iIndex].split("|")
                        xsDataTwinLawsStatistics =XSDataTwinLawsStatistics()
                        xsDataTwinLawsStatistics.operator = XSDataString(listLine[1].replace(" ", ""))
                        xsDataTwinLawsStatistics.twinType = XSDataString(listLine[2].replace(" ", ""))
                        xsDataTwinLawsStatistics.rObs = XSDataDouble(float(listLine[3]))
                        xsDataTwinLawsStatistics.brittonAlpha = XSDataDouble(float(listLine[4]))
                        xsDataTwinLawsStatistics.hAlpha = XSDataDouble(float(listLine[5]))
                        xsDataTwinLawsStatistics.mlAlpha = XSDataDouble(float(listLine[6]))
                        xsDataResultPhenixXtriage.addTwinLawStatistics(xsDataTwinLawsStatistics)
                        iIndex += 1
                                  
                elif listLines[iIndex].startswith("Patterson analyses"):
                    # - Largest peak height   : 6.089
                    iIndex += 1
                    pattersonLargestPeakHeight = float(listLines[iIndex].split(":")[1])
                    xsDataResultPhenixXtriage.pattersonLargestPeakHeight = XSDataDouble(pattersonLargestPeakHeight)
                    # (corresponding p value : 6.921e-01)
                    iIndex += 1
                    pattersonPValue = float(listLines[iIndex].split(":")[1].split(")")[0])
                    xsDataResultPhenixXtriage.pattersonPValue = XSDataDouble(pattersonPValue)
                    
                elif "indicating pseudo translational symmetry" in listLines[iIndex]:
                    #    The analyses of the Patterson function reveals a significant off-origin
                    #    peak that is 66.43 % of the origin peak, indicating pseudo translational symmetry.
                    #    The chance of finding a peak of this or larger height by random in a 
                    #    structure without pseudo translational symmetry is equal to the 6.0553e-06.
                    #    The detected translational NCS is most likely also responsible for the elevated intensity ratio.
                    #    See the relevant section of the logfile for more details.
                    hasPseudotranslation = True
                elif "As there are twin laws possible given the crystal symmetry, twinning could" in listLines[iIndex]:
                    #    The results of the L-test indicate that the intensity statistics
                    #    are significantly different than is expected from good to reasonable,
                    #    untwinned data.
                    #    As there are twin laws possible given the crystal symmetry, twinning could
                    #    be the reason for the departure of the intensity statistics from normality. 
                    hasTwinning = True                   
                iIndex += 1                
                if iIndex == len(listLines):
                    bContinue = False
        xsDataResultPhenixXtriage.twinning = XSDataBoolean(hasTwinning)
        xsDataResultPhenixXtriage.pseudotranslation = XSDataBoolean(hasPseudotranslation)
        return xsDataResultPhenixXtriage
        