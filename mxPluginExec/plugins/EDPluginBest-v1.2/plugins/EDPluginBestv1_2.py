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
__date__ = "20151118"
__status__ = "production"

import os
import shutil


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

from XSDataBestv1_2 import XSDataInputBest
from XSDataBestv1_2 import XSDataResultBest

from XSDataBestv1_2 import XSDataBestCollectionPlan
from XSDataBestv1_2 import XSDataBestStatisticalPrediction
from XSDataBestv1_2 import XSDataBestCollectionRun
from XSDataBestv1_2 import XSDataBestStrategySummary
from XSDataBestv1_2 import XSDataBestResolutionBin
from XSDataBestv1_2 import XSDataCrystalScale
from XSDataBestv1_2 import XSDataBestGlePlot

from XSDataDnaTablesBestv1_2 import dna_tables

from EDHandlerXSDataCommon import EDHandlerXSDataCommon


class EDPluginBestv1_2(EDPluginExecProcessScript):

    def __init__(self):
        EDPluginExecProcessScript.__init__(self)
        self.setXSDataInputClass(XSDataInputBest)
        self.setDataOutput(XSDataResultBest())

        # This version of the Best plugin requires the latest
        # version of Best.
        self.addCompatibleVersion("Version 4.1.0 //  02.10.2012")

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

        self.strPathToCorrectLp = None
        self.strPathToBkgpixCbf = None
        self.strListFileXdsAsciiHkl = None

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
        self.DEBUG("EDPluginBestv1_2.configure")
        strScriptExecutable = self.getScriptExecutable()
        self.DEBUG("EDPluginBestv1_2.configure: Script Executable: " + strScriptExecutable)
        strBestScriptHome = EDUtilsPath.getFolderName(strScriptExecutable)
        strBestHome = self.config.get(self.strCONF_BEST_HOME_LABEL, strBestScriptHome)
        self.setBestHome(strBestHome)
        self.DEBUG("EDPluginBestv1_2.configure: Best Home: " + strBestHome)
        self.setCommandBestHome("export besthome=" + self.getBestHome())
        strVersion = self.config.get(self.CONF_EXEC_PROCESS_SCRIPT_VERSION_STRING, "Unknown")
        # Check if version is higher than 4.1:
        try:
            if float(strVersion[8:11]) > 4.0:
                self.bVersionHigherThan4_0 = True
        except Exception as e:
            pass


    def preProcess(self, _edObject=None):
        EDPluginExecProcessScript.preProcess(self)
        self.DEBUG("EDPluginBestv1_2.preProcess")

        self.setScriptLogFileName("best.log")

        if self.dataInput.bestFileContentPar is not None:
            self.setFileBestDat(os.path.join(self.getWorkingDirectory(), "bestfile.dat"))
            self.setFileBestPar(os.path.join(self.getWorkingDirectory(), "bestfile.par"))

            EDUtilsFile.writeFile(self.getFileBestDat(), self.dataInput.bestFileContentDat.value)
            EDUtilsFile.writeFile(self.getFileBestPar(), self.dataInput.bestFileContentPar.value)

            listBestFileContentHKL = self.dataInput.bestFileContentHKL

            iterator = 0
            for bestFileContentHKL in listBestFileContentHKL:
                iterator = iterator + 1
                bestFileHKL = os.path.join(self.getWorkingDirectory(), "bestfile" + str(iterator) + ".hkl")
                self.listFileBestHKL.append(bestFileHKL)
                EDUtilsFile.writeFile(bestFileHKL, bestFileContentHKL.value)

        elif self.dataInput.xdsCorrectLp is not None:
            self.strPathToCorrectLp = os.path.join(self.getWorkingDirectory(), "CORRECT.LP")
            shutil.copyFile(self.dataInput.xdsCorrectLp.path.value, self.strPathToCorrectLp)

            self.strPathToBkgpixCbf = os.path.join(self.getWorkingDirectory(), "BKGPIX.cbf")
            shutil.copyFile(self.dataInput.xdsBkgpixCbf.path.value, self.strPathToBkgpixCbf)

            self.strListFileXdsAsciiHkl = ""
            index = 1
            for xdsAsciiHkl in self.dataInput.xdsAsciiHkl:
                strPathToXdsAsciiHkl = os.path.join(self.getWorkingDirectory(), "XDS_ASCII_{0}.HKL".format(index))
                shutil.copyFile(xdsAsciiHkl.path.value, strPathToXdsAsciiHkl)
                self.strListFileXdsAsciiHkl += " " + strPathToXdsAsciiHkl
                index += 1

        if self.dataInput.complexity is not None:
            self.strComplexity = self.dataInput.complexity.value

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

        # Add output of gle files only if version is 4.1.0 (or higher)
        if self.bVersionHigherThan4_0:
            self.strCommandBest = self.strCommandBest + "-g "

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

        if (self.dataInput.userDefinedRotationStart is not None) and \
           (self.dataInput.userDefinedRotationRange is not None):
            self.strCommandBest += " -phi {0} {1} ".format(self.dataInput.userDefinedRotationStart.value,
                                                          self.dataInput.userDefinedRotationRange.value)
            if self.dataInput.aimedRedundancy is not None:
                self.warning("Aimed redundancy of {0} igored as the oscillation range has been specified.".format(self.dataInput.aimedRedundancy.value))
        elif self.dataInput.aimedRedundancy is not None:
            strAimedRedundancy = str(self.dataInput.aimedRedundancy.value)
            self.strCommandBest = self.strCommandBest + "-R " + strAimedRedundancy + " "

        if self.dataInput.aimedCompleteness is not None:
            strAimedCompleteness = str(self.dataInput.aimedCompleteness.value)
            self.strCommandBest = self.strCommandBest + "-C " + strAimedCompleteness + " "

        if self.dataInput.aimedIOverSigma is not None:
            strAimedIOverSigma = str(self.dataInput.aimedIOverSigma.value)
            self.strCommandBest = self.strCommandBest + "-i2s " + strAimedIOverSigma + " "

        if self.dataInput.crystalAbsorbedDoseRate is not None:
            strCrystalAbsorbedDoseRate = str(self.dataInput.crystalAbsorbedDoseRate.value)
            self.strCommandBest = self.strCommandBest + "-GpS " + strCrystalAbsorbedDoseRate + " "

        if self.dataInput.crystalShape is not None:
            strCrystalShape = str(self.dataInput.crystalShape.value)
            self.strCommandBest = self.strCommandBest + "-sh " + strCrystalShape + " "

        if self.dataInput.crystalSusceptibility is not None:
            strCrystalSusceptibility = str(self.dataInput.crystalSusceptibility.value)
            self.strCommandBest = self.strCommandBest + "-su " + strCrystalSusceptibility + " "

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


        if self.dataInput.anomalousData is not None:
            bAnomalousData = self.dataInput.anomalousData.value
            if bAnomalousData:
                if self.dataInput.numberOfCrystalPositions is not None:
                    self.strCommandBest = self.strCommandBest + "-a -p 0 360 "
                elif self.dataInput.crystalAbsorbedDoseRate is not None:
                    self.strCommandBest = self.strCommandBest + "-asad "
                else:
                    self.strCommandBest = self.strCommandBest + "-a "

        strStrategyOption = self.dataInput.strategyOption
        if strStrategyOption is not None:
            self.strCommandBest = self.strCommandBest + "%s " % strStrategyOption.value

        if self.dataInput.getRadiationDamageModelBeta() is not None:
            fRadiationDamageModelBeta = str(self.dataInput.getRadiationDamageModelBeta().value)
            self.strCommandBest = self.strCommandBest + "-beta " + fRadiationDamageModelBeta + " "

        if self.dataInput.getRadiationDamageModelGamma() is not None:
            fRadiationDamageModelGamma = str(self.dataInput.getRadiationDamageModelGamma().value)
            self.strCommandBest = self.strCommandBest + "-gama " + fRadiationDamageModelGamma + " "

        if self.dataInput.doseLimit is not None:
            self.strCommandBest += " -DMAX {0} ".format(self.dataInput.doseLimit.value)

        if self.dataInput.rFriedel is not None:
            self.strCommandBest += " -Rf {0} ".format(self.dataInput.rFriedel.value)

        self.strCommandBest = self.strCommandBest + "-T " + str(fMaxExposureTime) + " " + \
                                     "-dna " + self.getScriptBaseName() + "_dnaTables.xml" + " " + \
                                     "-o " + os.path.join(self.getWorkingDirectory(), self.getScriptBaseName() + "_plots.mtv ") + \
                                     "-e " + self.strComplexity + " "

        if self.dataInput.xdsBackgroundImage is not None:
            strPathToXdsBackgroundImage = self.dataInput.getXdsBackgroundImage().getPath().value
            self.strCommandBest = self.strCommandBest + "-MXDS " + self.getFileBestPar() + " " + strPathToXdsBackgroundImage + " " + listFileBestHKLCommand
        elif self.dataInput.bestFileContentPar is not None:
            self.strCommandBest = self.strCommandBest + "-mos " + self.getFileBestDat() + " " + self.getFileBestPar() + " " + listFileBestHKLCommand
        elif self.dataInput.xdsCorrectLp is not None:
            self.strCommandBest = self.strCommandBest + "-xds " + self.strPathToCorrectLp + " " + self.strPathToBkgpixCbf + " " + self.strListFileXdsAsciiHkl


        self.setScriptCommandline(self.strCommandBest)


    def finallyProcess(self, _edObject=None):
        EDPluginExecProcessScript.finallyProcess(self)
        self.DEBUG("EDPluginBestv1_2.finallyProcess")
        xsDataResultBest = self.getOutputDataFromDNATableFile(os.path.join(self.getWorkingDirectory(), self.getScriptBaseName() + "_dnaTables.xml"))
        xsDataFilePathToLog = XSDataFile(XSDataString(os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName())))
        xsDataResultBest.setPathToLogFile(xsDataFilePathToLog)
        strError = self.readProcessErrorLogFile()
        if (strError is not None) and (strError != ""):
            strErrorMessage = "Error when executing BEST: {0}".format(strError)
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


    def getOutputDataFromDNATableFile(self, _strFileName):
        xsDataResultBest = XSDataResultBest()
        if os.path.exists(_strFileName):
            strDnaTablesXML = self.readProcessFile(_strFileName)
            # Fix for MXSUP-1751: Error when parsing broken XML
            try:
                strDnaTablesXML = strDnaTablesXML.replace(" > ", " greater than ")
                strDnaTablesXML = strDnaTablesXML.replace(" < ", " lesser than ")
                xsDataDnaTables = dna_tables.parseString(strDnaTablesXML)
            except Exception as e:
                self.setFailure()
                self.error("Parsing of BEST XML file failed: %s" % e)

            # Loop through all the tables and fill in the relevant parts of xsDataResultBest
            if not self.isFailure():
                xsDataStringStrategyOption = self.dataInput.strategyOption
                if xsDataStringStrategyOption is not None:
                    strStrategyOption = xsDataStringStrategyOption.value
                    if strStrategyOption.find("-DamPar") != -1:
                        xsDataResultBest = self.getDamParOutputFromDNATables(xsDataDnaTables)
                    elif strStrategyOption.find("-Bonly") != -1:
                        xsDataResultBest = self.getBonlyOutputFromDNATables(xsDataDnaTables)
                    else:
                        xsDataResultBest = self.getDataCollectionOutputDataFromDNATables(xsDataDnaTables)
                else:
                    xsDataResultBest = self.getDataCollectionOutputDataFromDNATables(xsDataDnaTables)

        return xsDataResultBest


    def getDamParOutputFromDNATables(self, _xsDataDnaTables):
        xsDataResultBest = XSDataResultBest()
        xsTablesCollectionStrategy = EDUtilsTable.getTableListFromTables(_xsDataDnaTables, "dam_par_plan")

        iCollectionPlanNumber = 1
        for xsTableCollectionStrategy in xsTablesCollectionStrategy:

            xsDataBestCollectionPlan = XSDataBestCollectionPlan()
            xsDataStrategySummary = XSDataBestStrategySummary()
            xsGeneralList = EDUtilsTable.getListsFromTable(xsTableCollectionStrategy, "general")[0]
            xsCollectionRunList = EDUtilsTable.getListsFromTable(xsTableCollectionStrategy, "collection_run")

            iCollectionRunNumber = 1
            for xsCollectionRunItemList in xsCollectionRunList:
                xsDataCollectionRun = self.collectionRunItemListToCollectionRun(xsCollectionRunItemList, iCollectionRunNumber)
                xsDataBestCollectionPlan.addCollectionRun(xsDataCollectionRun)
                iCollectionRunNumber = iCollectionRunNumber + 1

            xsDataBestCollectionPlan.setCollectionPlanNumber(XSDataInteger(iCollectionPlanNumber))
            xsDataResultBest.addCollectionPlan(xsDataBestCollectionPlan)
            iCollectionPlanNumber = iCollectionPlanNumber + 1

            xsItemDistance = EDUtilsTable.getItemFromList(xsGeneralList, "distance")
            fDistance = float(xsItemDistance.getValueOf_())
            xsDataStrategySummary.setDistance(XSDataLength(fDistance))

            xsItemResolution = EDUtilsTable.getItemFromList(xsGeneralList, "resolution")
            fResolution = float(xsItemResolution.getValueOf_())
            xsDataStrategySummary.setResolution(XSDataDouble(fResolution))

            xsDataBestCollectionPlan.setStrategySummary(xsDataStrategySummary)

        return xsDataResultBest


    def getBonlyOutputFromDNATables(self, _xsDataDnaTables):
        xsDataResultBest = XSDataResultBest()
        xsTablesGeneralInform = EDUtilsTable.getTableListFromTables(_xsDataDnaTables, "general_inform")

        xsDataBestCollectionPlan = XSDataBestCollectionPlan()
        xsDataCrystalScale = XSDataCrystalScale()


        xsCrystalScaleList = EDUtilsTable.getListsFromTable(xsTablesGeneralInform[0], "crystal_scale")[0]

        xsItemScal = EDUtilsTable.getItemFromList(xsCrystalScaleList, "scal")
        fScal = float(xsItemScal.getValueOf_())
        xsDataCrystalScale.setScale(XSDataDouble(fScal))

        xsItemBfactor = EDUtilsTable.getItemFromList(xsCrystalScaleList, "B_factor")
        fBfactor = float(xsItemBfactor.getValueOf_())
        xsDataCrystalScale.setBFactor(XSDataDouble(fBfactor))

        xsDataBestCollectionPlan.setCrystalScale(xsDataCrystalScale)
        xsDataResultBest.addCollectionPlan(xsDataBestCollectionPlan)

        return xsDataResultBest





    def getDataCollectionOutputDataFromDNATables(self, _xsDataDnaTables):
        xsDataResultBest = XSDataResultBest()
        # SubWedges
        xsTablesCollectionStrategy = EDUtilsTable.getTableListFromTables(_xsDataDnaTables, "data_collection_strategy")

        iCollectionPlanNumber = 1
        for xsTableCollectionStrategy in xsTablesCollectionStrategy:

            xsDataBestCollectionPlan = XSDataBestCollectionPlan()
            xsCollectionRunList = EDUtilsTable.getListsFromTable(xsTableCollectionStrategy, "collection_run")

            iCollectionRunNumber = 1
            for xsCollectionRunItemList in xsCollectionRunList:
                xsDataCollectionRun = self.collectionRunItemListToCollectionRun(xsCollectionRunItemList, iCollectionRunNumber)
                xsDataBestCollectionPlan.addCollectionRun(xsDataCollectionRun)
                iCollectionRunNumber = iCollectionRunNumber + 1


            # Strategy Summary
            xsStrategySummaryItemList = EDUtilsTable.getListsFromTable(xsTableCollectionStrategy, "summary")
            xsDataStrategySummary = self.strategySummaryItemListToStrategySummary(xsStrategySummaryItemList[0])
            # Ranking Resolution
            # Not part of strategySummaryItemListToStrategySummary method since it is in the general_form part
            xsTableGeneralInform = EDUtilsTable.getTableFromTables(_xsDataDnaTables, "general_inform")
            xsRankingResolutionItemList = EDUtilsTable.getListsFromTable(xsTableGeneralInform, "ranking_resolution")
            if len(xsRankingResolutionItemList) > 0:
                xsItemRankingResolution = EDUtilsTable.getItemFromList(xsRankingResolutionItemList[0], "dmin")
                fRankingResolution = float(xsItemRankingResolution.getValueOf_())
                xsDataStrategySummary.setRankingResolution(XSDataDouble(fRankingResolution))

            xsDataBestCollectionPlan.setStrategySummary(xsDataStrategySummary)

            # Satistics
            xsTablesStatisticalPrediction = EDUtilsTable.getTableListFromTables(_xsDataDnaTables, "statistical_prediction")
            for xsTableStatisticalPrediction in xsTablesStatisticalPrediction:
                if xsTableStatisticalPrediction.getIndex() == xsTableCollectionStrategy.getIndex():
                    xsResolutionBinList = EDUtilsTable.getListsFromTable(xsTableStatisticalPrediction, "resolution_bin")
                    xsDataStatisticalPrediction = XSDataBestStatisticalPrediction()
                    for xsResolutionBinItemList in xsResolutionBinList:
                        xsDataResolutionBin = self.resolutionBinItemListToResolutionBin(xsResolutionBinItemList)
                        xsDataStatisticalPrediction.addResolutionBin(xsDataResolutionBin)

                    xsDataBestCollectionPlan.setStatisticalPrediction(xsDataStatisticalPrediction)

            xsDataBestCollectionPlan.setCollectionPlanNumber(XSDataInteger(iCollectionPlanNumber))
            xsDataResultBest.addCollectionPlan(xsDataBestCollectionPlan)
            iCollectionPlanNumber = iCollectionPlanNumber + 1

        # Fix the order of the collection plans - then low resolution pass should be the first one
        listCollectionPlan = xsDataResultBest.getCollectionPlan()
        if len(listCollectionPlan) > 1:
            bIsModified = False
            for xsDataCollectionPlan in listCollectionPlan:
                xsDataStrategySummary = xsDataCollectionPlan.getStrategySummary()
                strReasoning = xsDataStrategySummary.getResolutionReasoning().value
                if (strReasoning.find("Low-resolution") != -1) and xsDataCollectionPlan.getCollectionPlanNumber().value != 1:
                    listCollectionPlan.remove(xsDataCollectionPlan)
                    listCollectionPlan.insert(0, xsDataCollectionPlan)
                    bIsModified = True
            if bIsModified:
                iCollectionPlanNumber = 1
                for xsDataCollectionPlan in listCollectionPlan:
                    xsDataCollectionPlan.setCollectionPlanNumber(XSDataInteger(iCollectionPlanNumber))
                    iCollectionPlanNumber = iCollectionPlanNumber + 1

        return xsDataResultBest


    def collectionRunItemListToCollectionRun(self, _xsCollectionRunItemList, _iCollectionRunNumber):
        xsDataCollectionRun = XSDataBestCollectionRun()

        xsItemWedge = EDUtilsTable.getItemFromList(_xsCollectionRunItemList, "Wedge")
        if xsItemWedge is not None:
            iWedge = int(xsItemWedge.getValueOf_())
        else:
            iWedge = _iCollectionRunNumber
        xsDataCollectionRun.setCollectionRunNumber(XSDataInteger(iWedge))

        xsItemCrystal = EDUtilsTable.getItemFromList(_xsCollectionRunItemList, "Crystal")
        if xsItemCrystal is not None:
            iCrystal = int(xsItemCrystal.getValueOf_())
            xsDataCollectionRun.setCrystalPosition(XSDataInteger(iCrystal))

        xsItemExposureTime = EDUtilsTable.getItemFromList(_xsCollectionRunItemList, "exposure_time")
        fExposureTime = float(xsItemExposureTime.getValueOf_())
        xsDataCollectionRun.setExposureTime(XSDataTime(fExposureTime))

        xsItemAction = EDUtilsTable.getItemFromList(_xsCollectionRunItemList, "action")
        if xsItemAction is not None:
            strAction = xsItemAction.getValueOf_()
            xsDataCollectionRun.setAction(XSDataString(strAction))

        xsItemRotationAxisStart = EDUtilsTable.getItemFromList(_xsCollectionRunItemList, "phi_start")
        fRotationAxisStart = float(xsItemRotationAxisStart.getValueOf_())
        xsDataCollectionRun.setPhiStart(XSDataAngle(fRotationAxisStart))

        xsNumberOfImages = EDUtilsTable.getItemFromList(_xsCollectionRunItemList, "number_of_images")
        iNumberOfImages = int(xsNumberOfImages.getValueOf_())
        xsDataCollectionRun.setNumberOfImages(XSDataInteger(iNumberOfImages))

        xsItemPhiWidth = EDUtilsTable.getItemFromList(_xsCollectionRunItemList, "phi_width")
        fPhiWidth = float(xsItemPhiWidth.getValueOf_())
        xsDataCollectionRun.setPhiWidth(XSDataAngle(fPhiWidth))

        xsItemOverlaps = EDUtilsTable.getItemFromList(_xsCollectionRunItemList, "overlaps")
        if xsItemOverlaps is not None:
            strOverlaps = xsItemOverlaps.getValueOf_()
            xsDataCollectionRun.setOverlaps(XSDataString(strOverlaps))

        xsItemTransmission = EDUtilsTable.getItemFromList(_xsCollectionRunItemList, "transmission")
        if xsItemTransmission is not None:
            fTransmission = float(xsItemTransmission.getValueOf_())
            xsDataCollectionRun.setTransmission(XSDataDouble(fTransmission))

        return xsDataCollectionRun


    def strategySummaryItemListToStrategySummary(self, _xsStrategySummaryItemList):
        xsDataStrategySummary = XSDataBestStrategySummary()

        xsItemDistance = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "distance")
        fDistance = float(xsItemDistance.getValueOf_())
        xsDataStrategySummary.setDistance(XSDataLength(fDistance))

        strItemTransmission = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "transmission")
        fTransmission = float(strItemTransmission.getValueOf_())
        xsDataStrategySummary.setTransmission(XSDataDouble(fTransmission))

        strItemCompleteness = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "completeness")
        # For homegeneity concerns, EDNA data model should store all the completeness value in fraction
        # ( DNA table xml file stores the summary strategy completeness in percentage whereas
        # the resolution bin completeness are in fraction )
        fCompleteness = float(strItemCompleteness.getValueOf_()) / 100
        xsDataStrategySummary.setCompleteness(XSDataDouble(fCompleteness))

        strItemISigma = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "i_sigma")
        fISigma = float(strItemISigma.getValueOf_())
        xsDataStrategySummary.setISigma(XSDataDouble(fISigma))

        strItemRedundancy = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "redundancy")
        fRedundancy = float(strItemRedundancy.getValueOf_())
        xsDataStrategySummary.setRedundancy(XSDataDouble(fRedundancy))

        strItemResolution = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "resolution")
        fResolution = float(strItemResolution.getValueOf_())
        xsDataStrategySummary.setResolution(XSDataDouble(fResolution))

        strItemResolutionReasoning = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "resolution_reasoning")
        strResolutionReasoning = strItemResolutionReasoning.getValueOf_()
        xsDataStrategySummary.setResolutionReasoning(XSDataString(strResolutionReasoning))

        strItemTotalDataCollectionTime = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "total_data_collection_time")
        fTotalDataCollectionTime = float(strItemTotalDataCollectionTime.getValueOf_())
        xsDataStrategySummary.setTotalDataCollectionTime(XSDataTime(fTotalDataCollectionTime))

        strItemTotalExposureTime = EDUtilsTable.getItemFromList(_xsStrategySummaryItemList, "total_exposure_time")
        fTotalExposureTime = float(strItemTotalExposureTime.getValueOf_())
        xsDataStrategySummary.setTotalExposureTime(XSDataTime(fTotalExposureTime))

        return xsDataStrategySummary


    def resolutionBinItemListToResolutionBin(self, _xsResolutionBinItemList):
        xsDataResolutionBin = XSDataBestResolutionBin()

        strItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "min_resolution")
        fItem = float(strItem.getValueOf_())
        xsDataResolutionBin.setMinResolution(XSDataDouble(fItem))

        strItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "max_resolution")
        fItem = float(strItem.getValueOf_())
        xsDataResolutionBin.setMaxResolution(XSDataDouble(fItem))

        strItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "completeness")
        fItem = float(strItem.getValueOf_())
        xsDataResolutionBin.setCompleteness(XSDataDouble(fItem))

        strItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "redundancy")
        fItem = float(strItem.getValueOf_())
        xsDataResolutionBin.setRedundancy(XSDataDouble(fItem))

        strItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "average_intensity")
        fItem = float(strItem.getValueOf_())
        xsDataResolutionBin.setAverageIntensity(XSDataDouble(fItem))

        strItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "average_error")
        fItem = float(strItem.getValueOf_())
        xsDataResolutionBin.setAverageSigma(XSDataDouble(fItem))

        strItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "average_i_over_sigma")
        fItem = float(strItem.getValueOf_())
        xsDataResolutionBin.setIOverSigma(XSDataDouble(fItem))

        strItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "average_i_over_average_sigma")
        if strItem is not None:
            fItem = float(strItem.getValueOf_())
            xsDataResolutionBin.setAverageIntensityOverAverageSigma(XSDataDouble(fItem))

        strItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "R_factor")
        fItem = float(strItem.getValueOf_())
        xsDataResolutionBin.setRFactor(XSDataDouble(fItem))

        strItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "R_friedel")
        if strItem is not None:
            fItem = float(strItem.getValueOf_())
            xsDataResolutionBin.setRFriedel(XSDataDouble(fItem))

#        strItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "average_i_over_sigma_Chi**2")
#        if (strItem is not None:
#            fItem = float(strItem.getValueOf_())
#            xsDataResolutionBin.setIOverSigmaChi(XSDataDouble(fItem))

        strItem = EDUtilsTable.getItemFromList(_xsResolutionBinItemList, "fract_overload")
        fItem = float(strItem.getValueOf_())
        xsDataResolutionBin.setPercentageOverload(XSDataDouble(fItem))

        return xsDataResolutionBin


    def generateExecutiveSummary(self, _edPlugin):
        """
        Generates a summary of the execution of the plugin.
        """
        self.DEBUG("EDPluginBestv1_2.generateExecutiveSummary")
        strBestLog = self.readProcessLogFile()
        listBestLogLines = strBestLog.split("\n")
        for strLine in listBestLogLines:
            self.addExecutiveSummaryLine(strLine)


