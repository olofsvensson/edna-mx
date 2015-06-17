#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
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


__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20150610"
__status__ = "production"

import os
import re

from EDUtilsPath                     import EDUtilsPath
from EDMessage                       import EDMessage
from EDUtilsFile                     import EDUtilsFile
from EDUtilsTable                    import EDUtilsTable
from EDConfiguration                 import EDConfiguration
from EDPluginExecProcessScript       import EDPluginExecProcessScript

from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataString
from XSDataCommon import XSDataTime

from XSDataBestv1_3 import XSDataInputBest
from XSDataBestv1_3 import XSDataResultBest

from XSDataBestv1_3 import XSDataBestCollectionPlan
from XSDataBestv1_3 import XSDataBestStatisticalPrediction
from XSDataBestv1_3 import XSDataBestCollectionRun
from XSDataBestv1_3 import XSDataBestStrategySummary
from XSDataBestv1_3 import XSDataBestResolutionBin
from XSDataBestv1_3 import XSDataCrystalScale
from XSDataBestv1_3 import XSDataBestGlePlot

from EDHandlerXSDataCommon import EDHandlerXSDataCommon


class EDPluginBestv1_3(EDPluginExecProcessScript):

    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputBest)
        self.setDataOutput(XSDataResultBest())

        # This version of the Best plugin requires the latest
        # version of Best. 
        self.addCompatibleVersion("Version 5.1.0 //  28.05.2015")
#        self.addCompatibleVersion("Version 4.1.0 //  02.10.2012")

        self.strCONF_BEST_HOME_LABEL = "besthome"

        # Default value of strategy complexity
        self.strComplexity = "none"

        self.strBestHome = None
        self.strCommandBestHome = None
        self.strCommandBest = None

        self.strExposureTime = None
        self.strDoseRate = None
        self.strDetectorType = None

        self.strPathToBestDatFile = None
        self.strPathToBestParFile = None
        self.listFileBestHKL = []

        self.bVersionHigherThan4_0 = False


    def checkParameters(self):
        """
        Checks the data input object
        """
        # Checks the mandatory parameters:
        self.checkMandatoryParameters(self.dataInput.beamExposureTime, "beamExposureTime")
        self.checkMandatoryParameters(self.dataInput.beamMaxExposureTime, "beamMaxExposureTime")
        self.checkMandatoryParameters(self.dataInput.detectorType, "detectorType")

        self.checkImportantParameters(self.dataInput.crystalAbsorbedDoseRate, "crystalDoseRate - radiation damage will not be estimated")
        self.checkImportantParameters(self.dataInput.crystalShape, "crystalShape")


    def getComplexity(self):
        return self.strComplexity


    def setComplexity(self, _strComplexity):
        self.strComplexity = _strComplexity


    def getBestHome(self):
        return self.strBestHome


    def setBestHome(self, strBestHome):
        self.strBestHome = strBestHome


    def getCommandBestHome(self):
        return self.strCommandBestHome


    def setCommandBestHome(self, _strCommandBestHome):
        self.strCommandBestHome = _strCommandBestHome


    def getCommandBest(self):
        return self.strCommandBest


    def setCommandBest(self, _strCommandBest):
        self.strCommandBest = _strCommandBest


    def getFileBestDat(self):
        return self.strPathToBestDatFile


    def setFileBestDat(self, _edFileBestDat):
        self.strPathToBestDatFile = _edFileBestDat


    def getFileBestPar(self):
        return self.strPathToBestParFile


    def setFileBestPar(self, _edFileBestPar):
        self.strPathToBestParFile = _edFileBestPar


    def getListFileBestHKL(self):
        return self.listFileBestHKL


    def setListFileBestHKL(self, _pyListFileBestHKL):
        self.listFileBestHKL = _pyListFileBestHKL


    def configure(self):
        EDPluginExecProcessScript.configure(self)
        self.DEBUG("EDPluginBestv1_3.configure")
        self.setRequireCCP4(True)
        strScriptExecutable = self.getScriptExecutable()
        self.DEBUG("EDPluginBestv1_3.configure: Script Executable: " + strScriptExecutable)
        strBestScriptHome = EDUtilsPath.getFolderName(strScriptExecutable)
        strBestHome = self.config.get(self.strCONF_BEST_HOME_LABEL, strBestScriptHome)
        self.setBestHome(strBestHome)
        self.DEBUG("EDPluginBestv1_3.configure: Best Home: " + strBestHome)
        self.setCommandBestHome("export besthome=" + self.getBestHome())
        strVersion = self.config.get(self.CONF_EXEC_PROCESS_SCRIPT_VERSION_STRING, "Unknown")


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginBestv1_3.preProcess")

        self.setScriptLogFileName("best.log")

        self.setFileBestDat(os.path.join(self.getWorkingDirectory(), "bestfile.dat"))
        self.setFileBestPar(os.path.join(self.getWorkingDirectory(), "bestfile.par"))

        EDUtilsFile.writeFile(self.getFileBestDat(), self.dataInput.bestFileContentDat.value)
        EDUtilsFile.writeFile(self.getFileBestPar(), self.dataInput.bestFileContentPar.value)

        listBestFileContentHKL = self.dataInput.getBestFileContentHKL()

        iterator = 0
        for bestFileContentHKL in listBestFileContentHKL:
            iterator = iterator + 1
            bestFileHKL = os.path.join(self.getWorkingDirectory(), "bestfile" + str(iterator) + ".hkl")
            self.listFileBestHKL.append(bestFileHKL)
            EDUtilsFile.writeFile(bestFileHKL, bestFileContentHKL.value)


        if self.dataInput.complexity is not None:
            self.setComplexity(self.dataInput.complexity.value)

        self.initializeCommands()


    def initializeCommands(self):
        self.addListCommandPreExecution(self.strCommandBestHome)

        listFileBestHKL = self.getListFileBestHKL()
        listFileBestHKLCommand = ""

        for fileBestHKL in listFileBestHKL:
            listFileBestHKLCommand = listFileBestHKLCommand + fileBestHKL + " "

        strDetectorName = self.dataInput.detectorType.value
        fExposureTime = self.dataInput.beamExposureTime.value
        fMaxExposureTime = self.dataInput.beamMaxExposureTime.value

        self.strCommandBest = "-f " + strDetectorName + " " + "-t " + str(fExposureTime) + " "

        # Add output of gle files
        self.strCommandBest = self.strCommandBest + "-g "

        if self.dataInput.crystalAbsorbedDoseRate is not None:
            strCrystalAbsorbedDoseRate = str(self.dataInput.crystalAbsorbedDoseRate.value)
            self.strCommandBest = self.strCommandBest + "-GpS " + strCrystalAbsorbedDoseRate + " "

        if self.dataInput.crystalShape is not None:
            strCrystalShape = str(self.dataInput.crystalShape.value)
            self.strCommandBest = self.strCommandBest + "-sh " + strCrystalShape + " "

        if self.dataInput.crystalSusceptibility is not None:
            strCrystalSusceptibility = str(self.dataInput.crystalSusceptibility.value)
            self.strCommandBest = self.strCommandBest + "-su " + strCrystalSusceptibility + " "

        if self.dataInput.anomalousData is not None:
            bAnomalousData = self.dataInput.anomalousData.value
            if (bAnomalousData):
                if self.dataInput.crystalAbsorbedDoseRate is not None:
                    self.strCommandBest = self.strCommandBest + "-asad "
                else:
                    self.strCommandBest = self.strCommandBest + "-a "

        if self.dataInput.beamMinExposureTime is not None:
            strBeamMinExposureTime = str(self.dataInput.beamMinExposureTime.value)
            self.strCommandBest = self.strCommandBest + "-M " + strBeamMinExposureTime + " "

        if self.dataInput.goniostatMaxRotationSpeed is not None:
            strGoniostatMaxRotationSpeed = str(self.dataInput.goniostatMaxRotationSpeed.value)
            self.strCommandBest = self.strCommandBest + "-S " + strGoniostatMaxRotationSpeed + " "

        if self.dataInput.goniostatMinRotationWidth is not None:
            strGoniostatMinRotationWidth = str(self.dataInput.goniostatMinRotationWidth.value)
            self.strCommandBest = self.strCommandBest + "-w " + strGoniostatMinRotationWidth + " "

        if self.dataInput.aimedResolution is not None:
            strAimedResolution = str(self.dataInput.aimedResolution.value)
            self.strCommandBest = self.strCommandBest + "-r " + strAimedResolution + " "

        if self.dataInput.aimedRedundancy is not None:
            strAimedRedundancy = str(self.dataInput.aimedRedundancy.value)
            self.strCommandBest = self.strCommandBest + "-R " + strAimedRedundancy + " "

        if self.dataInput.aimedCompleteness is not None:
            strAimedCompleteness = str(self.dataInput.aimedCompleteness.value)
            self.strCommandBest = self.strCommandBest + "-C " + strAimedCompleteness + " "

        if self.dataInput.aimedIOverSigma is not None:
            strAimedIOverSigma = str(self.dataInput.aimedIOverSigma.value)
            self.strCommandBest = self.strCommandBest + "-i2s " + strAimedIOverSigma + " "

        if self.dataInput.transmission is not None:
            strTransmission = str(self.dataInput.transmission.value)
            self.strCommandBest = self.strCommandBest + "-Trans " + strTransmission + " "

        if self.dataInput.minTransmission is not None:
            strMinTransmission = str(self.dataInput.minTransmission.value)
            self.strCommandBest = self.strCommandBest + "-TRmin " + strMinTransmission + " "

        if self.dataInput.numberOfCrystalPositions is not None:
            iNumberOfCrystalPositions = str(self.dataInput.numberOfCrystalPositions.value)
            self.strCommandBest = self.strCommandBest + "-Npos " + iNumberOfCrystalPositions + " "

        
        if self.dataInput.detectorDistanceMin is not None:
            fDetectorDistanceMin = str(self.dataInput.detectorDistanceMin.value)
            self.strCommandBest = self.strCommandBest + "-DIS_MIN " + fDetectorDistanceMin + " "

        
        if self.dataInput.detectorDistanceMax is not None:
            fDetectorDistanceMax = str(self.dataInput.detectorDistanceMax.value)
            self.strCommandBest = self.strCommandBest + "-DIS_MAX " + fDetectorDistanceMax + " "

        
        xsDataStrategyOption = self.dataInput.strategyOption
        if xsDataStrategyOption is not None:
            self.strCommandBest = self.strCommandBest + "%s " % xsDataStrategyOption.value

        xsDataAngleUserDefinedRotationStart = self.dataInput.userDefinedRotationStart
        xsDataAngleUserDefinedRotationRange = self.dataInput.userDefinedRotationRange
        if xsDataAngleUserDefinedRotationStart is not None:
            self.strCommandBest = self.strCommandBest + "-phi %f %f " % \
              (xsDataAngleUserDefinedRotationStart.value, xsDataAngleUserDefinedRotationRange.value)

        if self.dataInput.radiationDamageModelBeta is not None:
            fRadiationDamageModelBeta = str(self.dataInput.radiationDamageModelBeta.value)
            self.strCommandBest = self.strCommandBest + "-beta " + fRadiationDamageModelBeta + " "

        if self.dataInput.radiationDamageModelGamma is not None:
            fRadiationDamageModelGamma = str(self.dataInput.radiationDamageModelGamma.value)
            self.strCommandBest = self.strCommandBest + "-gama " + fRadiationDamageModelGamma + " "

        self.strCommandBest = self.strCommandBest + "-T " + str(fMaxExposureTime) + " " + \
                                     "-o " + os.path.join(self.getWorkingDirectory(), self.getScriptBaseName() + "_plots.mtv ") + \
                                     "-e " + self.getComplexity() + " "
                                     
        if self.dataInput.xdsBackgroundImage:
            strPathToXdsBackgroundImage = self.dataInput.xdsBackgroundImage.path.value
            self.strCommandBest = self.strCommandBest + "-MXDS " + self.getFileBestPar() + " " + strPathToXdsBackgroundImage + " " + listFileBestHKLCommand            
        else:
            self.strCommandBest = self.strCommandBest + "-mos " + self.getFileBestDat() + " " + self.getFileBestPar() + " " + listFileBestHKLCommand

        self.setScriptCommandline(self.strCommandBest)


    def finallyProcess(self, _edObject=None):
        EDPluginExecProcessScript.finallyProcess(self)
        self.DEBUG("EDPluginBestv1_3.finallyProcess")
        xsDataResultBest = self.getXSDataResultBest(os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName()))
        xsDataFilePathToLog = XSDataFile(XSDataString(os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName())))
        xsDataResultBest.setPathToLogFile(xsDataFilePathToLog)
        strError = self.readProcessErrorLogFile()
        if((strError is not None) and (strError != "")):
            strErrorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginBestv1_3.finallyProcess', 'EDPluginBestv1_3', strError)
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            # Append error message to best log
            strLog = self.readProcessLogFile()
            strLog += "\n" + strError
            EDUtilsFile.writeFile(os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName()), strLog)
            self.setDataOutput(xsDataResultBest)
            self.setFailure()
        else:
            strPathToPlotMtv = os.path.join(self.getWorkingDirectory(), self.getScriptBaseName() + "_plots.mtv")
            if os.path.exists(strPathToPlotMtv):
                xsDataFilePathToPlotMtv = XSDataFile(XSDataString(strPathToPlotMtv))
                xsDataResultBest.setPathToPlotMtvFile(xsDataFilePathToPlotMtv)
            # Check for .gle files
            for strPath in os.listdir(self.getWorkingDirectory()):
                if strPath.endswith(".gle"):
                    xsDataBestGlePlot = XSDataBestGlePlot()
                    xsDataBestGlePlot.script = XSDataFile(XSDataString(os.path.join(self.getWorkingDirectory(), strPath)))
                    strDataPath = strPath[:-4] + ".dat"
                    if os.path.exists(os.path.join(self.getWorkingDirectory(), strDataPath)):
                        xsDataBestGlePlot.data = XSDataFile(XSDataString(os.path.join(self.getWorkingDirectory(), strDataPath)))
                    else:
                        strDataPath = strPath[:-4] + ".data"
                        if os.path.exists(os.path.join(self.getWorkingDirectory(), strDataPath)):
                            xsDataBestGlePlot.data = XSDataFile(XSDataString(os.path.join(self.getWorkingDirectory(), strDataPath)))
                    xsDataResultBest.addGlePlot(xsDataBestGlePlot)
            self.setDataOutput(xsDataResultBest)


    def getXSDataResultBest(self, _strPathToLogFile):
        """Parse the BEST log file"""
        xsDataResultBest = None
        if os.path.exists(_strPathToLogFile):
            strBestLog = EDUtilsFile.readFile(_strPathToLogFile)
            xsDataStringStrategyOption = self.dataInput.strategyOption
            # Check if -DamPar or -Bonly strategy options have been used
            if xsDataStringStrategyOption is not None:
                strStrategyOption = xsDataStringStrategyOption.value
                if strStrategyOption.find("-Bonly") != -1:
                    xsDataResultBest = self.getBonlyOutputFromLog(strBestLog)
            if xsDataResultBest is None:
                # Neither the -DamPar nor the -Bonly strategy option has been used
                xsDataResultBest = self.getDataCollectionOutputDataFromLog(strBestLog)
        return xsDataResultBest


    def getBonlyOutputFromLog(self, _strBestLog):
        listLog = _strBestLog.split("\n")
        indexLine = 0
        xsDataResultBest = XSDataResultBest()
        xsDataBestCollectionPlan  = XSDataBestCollectionPlan()
        xsDataCrystalScale = XSDataCrystalScale()
        #
        while not "Relative scale" in listLog[indexLine]:
            indexLine += 1
        xsDataCrystalScale.scale = XSDataDouble(listLog[indexLine].split()[-1])
        #
        while not "Overall B-factor" in listLog[indexLine]:
            indexLine += 1
        xsDataCrystalScale.bFactor = XSDataDouble(listLog[indexLine].split()[-2])
        xsDataBestCollectionPlan.crystalScale = xsDataCrystalScale
        xsDataResultBest.addCollectionPlan(xsDataBestCollectionPlan)
        return xsDataResultBest


    def getDataCollectionOutputDataFromLog(self, _strBestLog):
        xsDataResultBest = XSDataResultBest()
        # loop through the lines of the log file
        isScanningWedge = False
        indexLine = 0
        listLog = _strBestLog.split("\n")
        iCollectionPlanNumber = 1
        while indexLine < len(listLog):
            if "Plan of data collection for radiation damage characterisation" in listLog[indexLine]:
                xsDataBestCollectionPlan  = XSDataBestCollectionPlan()
                xsDataBestStrategySummary = XSDataBestStrategySummary()
                indexLine += 2
                regEx= re.compile(""" Resolution limit =\s*(\d+\.\d+) Angstrom\s*Distance =\s*(\d+\.\d+)mm""")
                matchObj = regEx.search(listLog[indexLine])
                if matchObj == None:
                    raise BaseException("Cannot parse best log file!")
                resultMatch = matchObj.groups()
                resultion = float(resultMatch[0])
                distance = float(resultMatch[1])
                xsDataBestStrategySummary.resolution = XSDataDouble(resultion)
                xsDataBestStrategySummary.distance = XSDataLength(distance)
                xsDataBestCollectionPlan.strategySummary = xsDataBestStrategySummary
                # Burn strategy
                indexLine += 7
                collectionRunNumber = 1
                while not listLog[indexLine].startswith("-------------------------------"):
                    listLine = listLog[indexLine].split()
                    if listLine[0].startswith("exposure") or listLine[0].startswith("burn"):
                        xsDataBestCollectionRun = XSDataBestCollectionRun()
                        xsDataBestCollectionRun.collectionRunNumber = XSDataInteger(collectionRunNumber)
                        xsDataBestCollectionRun.action = XSDataString(listLine[0])
                        xsDataBestCollectionRun.phiStart = XSDataAngle(listLine[1])
                        xsDataBestCollectionRun.phiWidth = XSDataAngle(listLine[2])
                        xsDataBestCollectionRun.exposureTime = XSDataTime(listLine[3])
                        xsDataBestCollectionRun.numberOfImages = XSDataInteger(listLine[4].split("|")[0])
                        xsDataBestCollectionRun.transmission = XSDataDouble(listLine[5])
                        xsDataBestCollectionPlan.addCollectionRun(xsDataBestCollectionRun)
                        collectionRunNumber += 1
                    indexLine += 1
                xsDataBestCollectionPlan.collectionPlanNumber = XSDataInteger(iCollectionPlanNumber)
                xsDataResultBest.addCollectionPlan(xsDataBestCollectionPlan)                
            if "Main Wedge" in listLog[indexLine] or "Low resolution Wedge" in listLog[indexLine] \
                or "Strategy for SAD data collection" in listLog[indexLine]:
                isScanningWedge = True
                xsDataBestCollectionPlan  = XSDataBestCollectionPlan()
                xsDataBestStrategySummary = XSDataBestStrategySummary()
                if "Main Wedge" in listLog[indexLine]:
                    indexLine += 2
                    # ResolutionReasoning
                    xsDataBestStrategySummary.resolutionReasoning = XSDataString(listLog[indexLine].strip())
                elif "Strategy for SAD data collection" in listLog[indexLine]:
                    indexLine += 2
                    xsDataBestStrategySummary.resolutionReasoning = XSDataString(listLog[indexLine].strip())
                else:
                    xsDataBestStrategySummary.resolutionReasoning = XSDataString("Low-resolution pass, no overloads and full completeness")
                # Resolution, transmission, distance
                indexLine += 1
                while not "Resolution limit" in listLog[indexLine]:
                    indexLine += 1
                regEx= re.compile(""" Resolution limit =\s*(\d+\.\d+) Angstrom   Transmission =\s*(\d+\.\d+)%  Distance =\s*(\d+\.\d+)mm""")
                matchObj = regEx.search(listLog[indexLine])
                if matchObj == None:
                    raise BaseException("Cannot parse best log file!")
                resultMatch = matchObj.groups()
                resultion = float(resultMatch[0])
                transmission = float(resultMatch[1])
                distance = float(resultMatch[2])
                xsDataBestStrategySummary.resolution = XSDataDouble(resultion)
                xsDataBestStrategySummary.transmission = XSDataDouble(transmission)
                xsDataBestStrategySummary.distance = XSDataLength(distance)
                # Resolution, transmission, distance
                indexLine += 8
                while not listLog[indexLine].startswith("-------------------------------"):
                    listLine = listLog[indexLine].split()
                    xsDataBestCollectionRun = XSDataBestCollectionRun()
                    xsDataBestCollectionRun.collectionRunNumber = XSDataInteger(listLine[0])
                    xsDataBestCollectionRun.phiStart = XSDataAngle(listLine[1])
                    xsDataBestCollectionRun.phiWidth = XSDataAngle(listLine[2])
                    xsDataBestCollectionRun.exposureTime = XSDataTime(listLine[3])
                    xsDataBestCollectionRun.numberOfImages = XSDataInteger(listLine[4].split("|")[0])
                    xsDataBestCollectionRun.overlaps = XSDataString(listLine[5])
                    xsDataBestCollectionPlan.addCollectionRun(xsDataBestCollectionRun)
                    indexLine += 1
                #
                xsDataBestStrategySummary.completeness = XSDataDouble(listLine[11])
                #
                while not "Redundancy" in listLog[indexLine]:
                    indexLine += 1
                xsDataBestStrategySummary.redundancy = XSDataDouble(listLog[indexLine].split()[-1])
                #
                while not "I/Sigma (outer shell)" in listLog[indexLine]:
                    indexLine += 1
                xsDataBestStrategySummary.iSigma = XSDataDouble(listLog[indexLine].split()[6].replace(")",""))
                #
                while not "Total Exposure time" in listLog[indexLine]:
                    indexLine += 1
                xsDataBestStrategySummary.totalExposureTime = XSDataTime(listLog[indexLine].split()[4])
                #
                while not "Total Data Collection time" in listLog[indexLine]:
                    indexLine += 1
                xsDataBestStrategySummary.totalDataCollectionTime = XSDataTime(listLog[indexLine].split()[5])
                #
                while not "Wedge Data Collection Statistics according to the Strategy" in listLog[indexLine]:
                    indexLine += 1
                (xsDataBestStatisticalPrediction, indexLine) = self.getXSDataBestStatisticalPrediction(listLog, indexLine)
                
                xsDataBestCollectionPlan.strategySummary = xsDataBestStrategySummary
                xsDataBestCollectionPlan.statisticalPrediction = xsDataBestStatisticalPrediction
                xsDataBestCollectionPlan.collectionPlanNumber = XSDataInteger(iCollectionPlanNumber)
                iCollectionPlanNumber += 1
                xsDataResultBest.addCollectionPlan(xsDataBestCollectionPlan)
            if "Additional information" in listLog[indexLine]:
                #
                while not "Relative scale" in listLog[indexLine]:
                    indexLine += 1
                scale = float(listLog[indexLine].split()[-1])
                #
                while not "Overall B-factor" in listLog[indexLine]:
                    indexLine += 1
                #
                bFactor = float(listLog[indexLine].split()[-2])
                while not "Estimated limit of resolution" in listLog[indexLine]:
                    indexLine += 1
                rankingResolution = float(listLog[indexLine].split()[5])
                for collectionPlan in xsDataResultBest.collectionPlan:
                    xsDataCrystalScale = XSDataCrystalScale()
                    xsDataCrystalScale.scale = XSDataDouble(scale)
                    xsDataCrystalScale.bFactor = XSDataDouble(bFactor)
                    collectionPlan.crystalScale = xsDataCrystalScale
                    collectionPlan.strategySummary.rankingResolution = XSDataDouble(rankingResolution)
            indexLine += 1
        return xsDataResultBest
                
                
    def getXSDataBestStatisticalPrediction(self, _listLog, _indexLine):
        minResolution = None
        maxResolution = None
        indexLine = _indexLine
        xsDataBestStatisticalPrediction = XSDataBestStatisticalPrediction()
        if "Wedge Data Collection Statistics according to the Strategy" in _listLog[indexLine]:
            indexLine += 2
            if "Rfriedel" in _listLog[indexLine]:
                hasRfriedel = True
            else:
                hasRfriedel = False
            indexLine += 3
            continueToReadLog = True
            while continueToReadLog:
                listLine = _listLog[indexLine].split()
                xsDataBestResolutionBin = XSDataBestResolutionBin()
                if "All data" in _listLog[indexLine]:
                    xsDataBestResolutionBin.minResolution = XSDataDouble(minResolution)
                    xsDataBestResolutionBin.maxResolution = XSDataDouble(maxResolution)
                    continueToReadLog = False
                else:
                    if minResolution is None or minResolution < float(listLine[0]):
                        minResolution = listLine[0]
                    if maxResolution is None or maxResolution > float(listLine[1]):
                        maxResolution = listLine[1]
                    xsDataBestResolutionBin.minResolution = XSDataDouble(listLine[0])
                    xsDataBestResolutionBin.maxResolution = XSDataDouble(listLine[1])
                xsDataBestResolutionBin.completeness = XSDataDouble(float(listLine[2])/100.0)
                xsDataBestResolutionBin.averageIntensity = XSDataDouble(listLine[3])
                xsDataBestResolutionBin.averageSigma = XSDataDouble(listLine[4])
                xsDataBestResolutionBin.averageIntensityOverAverageSigma = XSDataDouble(listLine[5])
                xsDataBestResolutionBin.IOverSigma = XSDataDouble(listLine[6])
                xsDataBestResolutionBin.rFactor = XSDataDouble(listLine[7])
                if hasRfriedel:
                    xsDataBestResolutionBin.rFriedel = XSDataDouble(listLine[8])
                    xsDataBestResolutionBin.percentageOverload = XSDataDouble(listLine[9])
                else:
                    xsDataBestResolutionBin.percentageOverload = XSDataDouble(listLine[8])
                xsDataBestStatisticalPrediction.addResolutionBin(xsDataBestResolutionBin)
                indexLine += 1
        return (xsDataBestStatisticalPrediction, indexLine)




    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        self.DEBUG("EDPluginBestv1_3.generateExecutiveSummary")
        strBestLog = self.readProcessLogFile()
        listBestLogLines = strBestLog.split("\n")
        for strLine in listBestLogLines:
            self.addExecutiveSummaryLine(strLine)


