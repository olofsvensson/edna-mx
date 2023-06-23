# coding: utf8
#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Olof Svensson (svensson@esrf.fr)
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

import os
import html
import json
import time
import shutil

from PIL import Image

from EDPluginExec import EDPluginExec
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsFile import EDUtilsFile
from EDHandlerESRFPyarchv1_0 import EDHandlerESRFPyarchv1_0
from EDUtilsPath import EDUtilsPath
from EDUtilsImage import EDUtilsImage

from EDUtilsReport import EDUtilsReport

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

from XSDataSimpleHTMLPagev1_1 import XSDataInputSimpleHTMLPage
from XSDataSimpleHTMLPagev1_1 import XSDataResultSimpleHTMLPage

EDFactoryPluginStatic.loadModule("XSDataMXv1")
from XSDataMXv1 import XSDataDiffractionPlan


class EDPluginExecSimpleHTMLPagev1_1(EDPluginExec):
    """
    This plugin launches the EDPluginExecOutputHTMLv1_0 for creating web pages for ISPyB
    """

    def __init__ (self):
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputSimpleHTMLPage)
        self.strPluginExecOutputHTMLName = "EDPluginExecOutputHTMLv1_0"
        self.edPluginExecOutputHTML = None
        self.strHTML = None
        self.xsDataResultCharacterisation = None
        self.strPath = None
        self.strTableColourTitle1 = "#F5F5FF"
        self.strTableColourTitle2 = "#F0F0FF"
        self.strTableColourRows = "#FFFFA0"
        self.strPageEDNALog = None
        self.fMinTransmission = 10  # %
        self.bIsHelical = False
        self.bIsMultiPositional = False
        self.workflowStepReport = None


    def configure(self):
        """
        Gets the configuration parameters (if any).
        """
        EDPluginExec.configure(self)
        self.DEBUG("EDPluginExecSimpleHTMLPagev1_1.configure")
        self.fMinTransmission = self.config.get("minTransmissionWarning", self.fMinTransmission)

    def preProcess(self, _edPlugin=None):
        EDPluginExec.preProcess(self, _edPlugin)
        self.DEBUG("EDPluginExecSimpleHTMLPagev1_1.preProcess...")
        self.xsDataResultCharacterisation = self.getDataInput().getCharacterisationResult()
        self.strHtmlFileName = "index.html"
        self.strPath = os.path.join(self.getWorkingDirectory(), self.strHtmlFileName)


    def process(self, _edPlugin=None):
        EDPluginExec.process(self, _edPlugin)
        self.DEBUG("EDPluginExecSimpleHTMLPagev1_1.process...")
        if self.xsDataResultCharacterisation is not None:
            # EDutilsReport
            self.workflowStepReport = EDUtilsReport("Characterisation")
            if self.xsDataResultCharacterisation is not None:
                self.workflowStepReport.setTitle("Characterisation Results")
            else:
                self.workflowStepReport.setTitle("No Characterisation Results!")
            self.transmissionWarning()
            self.indexingResults()
            self.strategyResults()
            self.graphs()
            self.diffractionPlan()
            self.imageQualityIndicatorResults()
            self.createPredictionRowOfImages()
            self.createThumbnailRowOfImages()
            self.kappaResults()
            self.dataCollectionInfo()
            self.indexingLogFile()
            self.integrationLogFiles()
            self.bestAndRaddoseLogFiles()
            # Link to the EDNA log file
            if self.dataInput.logFile is None:
                strPathToLogFile = self.getLogFileName()
            else:
                strPathToLogFile = self.dataInput.logFile.path.value
            if strPathToLogFile is not None:
                self.workflowStepReport.addLogFile("edna_log", "EDNA log file", strPathToLogFile)




    def finallyProcess(self, _edPlugin=None):
        EDPluginExec.finallyProcess(self, _edPlugin)
        self.DEBUG("EDPluginExecSimpleHTMLPagev1_1.finallyProcess...")
        xsDataResultSimpleHTMLPage = XSDataResultSimpleHTMLPage()
        xsDataResultSimpleHTMLPage.setPathToHTMLFile(XSDataFile(XSDataString(os.path.join(self.getWorkingDirectory(), self.strHtmlFileName))))
        xsDataResultSimpleHTMLPage.setPathToHTMLDirectory(XSDataFile(XSDataString(self.getWorkingDirectory())))
        # Write workflowStepReport HTML page
        pathToIndexFile = self.workflowStepReport.renderHtml(self.getWorkingDirectory(), nameOfIndexFile=self.strHtmlFileName)
        pathToJsonFile = self.workflowStepReport.renderJson(self.getWorkingDirectory())
        # Store in Pyarch
        if EDUtilsPath.isESRF() or EDUtilsPath.isEMBL() or EDUtilsPath.isMAXIV() or EDUtilsPath.isALBA:
            strPyarchPath = None
            if self.xsDataResultCharacterisation is not None:
                strPyarchPath = EDHandlerESRFPyarchv1_0.createPyarchHtmlDirectoryPath(self.xsDataResultCharacterisation.getDataCollection())
            if strPyarchPath is None:
                # For debugging purposes
                strPyarchPath = EDUtilsPath.getEdnaUserTempFolder()
            EDHandlerESRFPyarchv1_0.copyHTMLDir(_strPathToHTMLDir=os.path.dirname(self.strPath), _strPathToPyarchDirectory=strPyarchPath)
            xsDataResultSimpleHTMLPage.setPathToHTMLDirectory(XSDataFile(XSDataString(strPyarchPath)))
            if not os.path.exists(strPyarchPath):
                os.makedirs(strPyarchPath, 0o755)
            EDUtilsPath.systemCopyFile(pathToJsonFile, strPyarchPath)
            pathToJsonFile = os.path.join(strPyarchPath, os.path.basename(pathToJsonFile))
        # Write json file
        xsDataResultSimpleHTMLPage.pathToJsonFile = XSDataFile(XSDataString(pathToJsonFile))
        self.setDataOutput(xsDataResultSimpleHTMLPage)




    def indexingResults(self):
        # Was the indexing successful?
        xsDataResultIndexing = self.xsDataResultCharacterisation.getIndexingResult()
        strForcedSpaceGroup = None
        # Check for forced space group!
        if self.xsDataResultCharacterisation.dataCollection.diffractionPlan is not None:
            if self.xsDataResultCharacterisation.dataCollection.diffractionPlan.forcedSpaceGroup is not None:
                strForcedSpaceGroup = self.xsDataResultCharacterisation.dataCollection.diffractionPlan.forcedSpaceGroup.value
                if strForcedSpaceGroup == "":
                    strForcedSpaceGroup = None
        if xsDataResultIndexing:
            # Table with indexing results
            self.createTableWithIndexResults(xsDataResultIndexing, strForcedSpaceGroup)



    def integrationLogFiles(self):
        # Was the integration successful?
        xsDataResultIntegration = self.xsDataResultCharacterisation.getIntegrationResult()
        if xsDataResultIntegration:
            iIntegration = 1
            for xsDataIntegrationSubWedgeResult in xsDataResultIntegration.getIntegrationSubWedgeResult():
                if xsDataIntegrationSubWedgeResult.getIntegrationLogFile() is not None:
                    strPathToIntegrationLogFile = xsDataIntegrationSubWedgeResult.getIntegrationLogFile().getPath().getValue()
                    self.workflowStepReport.addLogFile("integration_%d_log" % iIntegration,
                                                       "Integration Log No %d" % iIntegration,
                                                       strPathToIntegrationLogFile)
                    iIntegration += 1





    def strategyResults(self):
        # Was the strategy successful?
        xsDataResultStrategy = self.xsDataResultCharacterisation.getStrategyResult()
        if xsDataResultStrategy is None:
            # Check if indexing and integration results
            xsDataResultIntegration = self.xsDataResultCharacterisation.getIntegrationResult()
            xsDataResultIndexing = self.xsDataResultCharacterisation.getIndexingResult()
            if xsDataResultIndexing is None:
                self.workflowStepReport.addWarning("Strategy calculation not performed due to indexing failure, see the EDNA log file for more details")
            elif xsDataResultIntegration is None:
                self.workflowStepReport.addWarning("Strategy calculation not performed due to integration failure, see the EDNA log file for more details")
            else:
                self.workflowStepReport.addWarning("Strategy calculation failed, see the EDNA log file for more details")
        else:
            listXSDataCollectionPlan = xsDataResultStrategy.getCollectionPlan()
            if listXSDataCollectionPlan == []:
                self.workflowStepReport.addWarning("Strategy calculation failed, see the BEST log file for more details")
            else:
                iNoSubWedges = len(listXSDataCollectionPlan)
                if self.bIsHelical:
                    tabTitle = "Helical collection plan strategy"
                elif self.bIsMultiPositional:
                    tabTitle = "Multi-positional collection plan strategy"
                elif iNoSubWedges != 1:
                    tabTitle = "Multi-wedge collection plan strategy"
                else:
                    tabTitle = "Collection plan strategy"
                # Check if ranking resolution is higher than the suggested strategy resolution(s)
                bHigherResolutionDetected = False
                fRankingResolution = None
                fResolutionMax = None
                fDistanceMin = None
                for xsDataCollectionPlan in listXSDataCollectionPlan:
                    xsDataSummaryStrategy = xsDataCollectionPlan.getStrategySummary()
                    xsDataCollectionStrategy = xsDataCollectionPlan.getCollectionStrategy()
                    if xsDataSummaryStrategy.getRankingResolution():
                        # Retrieve the resolution...
                        fResolution = xsDataSummaryStrategy.getResolution().getValue()
                        # Retrieve the detector distance...
                        fDistance = xsDataCollectionStrategy.getSubWedge()[0].getExperimentalCondition().getDetector().getDistance().getValue()
                        if fResolutionMax is None:
                            fResolutionMax = fResolution
                            fDistanceMin = fDistance
                        elif (fResolution < fResolutionMax) and (abs(fResolution - fResolutionMax) > 0.1):
                            fResolutionMax = fResolution
                            fDistanceMin = fDistance
                        fRankingResolution = xsDataSummaryStrategy.getRankingResolution().getValue()

                if fRankingResolution != None and fResolutionMax != None:
                    if fRankingResolution < fResolutionMax:
                        if not bHigherResolutionDetected:
                            self.workflowStepReport.addWarning("Best has detected that the sample can diffract to {0:.2f} Å!".format(fRankingResolution))
                            self.workflowStepReport.addWarning("Move the detector to collect {0:.2f} Å data and re-launch the EDNA characterisation.".format(fRankingResolution))
                        bHigherResolutionDetected = True


                for xsDataCollectionPlan in listXSDataCollectionPlan:
                    xsDataSummaryStrategy = xsDataCollectionPlan.getStrategySummary()
                    fResolutionMax = xsDataSummaryStrategy.getResolution().getValue()
                    tableColumns = ["Wedge", "Subwedge", "Start (°)", "Width (°)", "No images",
                                    "Exp time (s)", "Max res (Å)", "Rel trans (%)", "Distance (mm)"]
                    xsDataCollectionStrategy = xsDataCollectionPlan.getCollectionStrategy()
                    tableData = []
                    for xsDataSubWegde in xsDataCollectionStrategy.getSubWedge():
                        xsDataExperimentalCondition = xsDataSubWegde.getExperimentalCondition()
                        iWedge = xsDataCollectionPlan.getCollectionPlanNumber().getValue()
                        iRunNumber = xsDataSubWegde.getSubWedgeNumber().getValue()
                        fRotationAxisStart = xsDataExperimentalCondition.getGoniostat().getRotationAxisStart().getValue()
                        fRotationAxisEnd = xsDataExperimentalCondition.getGoniostat().getRotationAxisEnd().getValue()
                        fOscillationWidth = xsDataExperimentalCondition.getGoniostat().getOscillationWidth().getValue()
                        iNumberOfImages = int((fRotationAxisEnd - fRotationAxisStart) / fOscillationWidth)
                        fExposureTime = xsDataExperimentalCondition.getBeam().getExposureTime().getValue()
                        fTransmission = xsDataExperimentalCondition.getBeam().getTransmission().getValue()
                        fDistance = xsDataExperimentalCondition.getDetector().getDistance().getValue()
                        listRow = []
                        listRow.append(iWedge)
                        listRow.append(iRunNumber)
                        listRow.append("%.2f" % fRotationAxisStart)
                        listRow.append("%.2f" % fOscillationWidth)
                        listRow.append(iNumberOfImages)
                        listRow.append("%.3f" % fExposureTime)
                        listRow.append("%.2f" % fResolutionMax)
                        listRow.append("%.2f" % fTransmission)
                        listRow.append("%.2f" % fDistance)
                        tableData.append(listRow)
                    if xsDataSummaryStrategy.getResolutionReasoning():
                        strResolutionReasoning = xsDataSummaryStrategy.getResolutionReasoning().getValue()
                        strResolutionReasoningFirstLower = strResolutionReasoning[0].lower() + strResolutionReasoning[1:]
                        self.workflowStepReport.addTable(tabTitle + ": " + strResolutionReasoningFirstLower, tableColumns, tableData)
                    else:
                        self.workflowStepReport.addTable(tabTitle, tableColumns, tableData)

    def bestAndRaddoseLogFiles(self):
        xsDataResultStrategy = self.xsDataResultCharacterisation.getStrategyResult()
        if xsDataResultStrategy is not None:
            if xsDataResultStrategy.bestLogFile:
                strPathToBestLogFile = xsDataResultStrategy.bestLogFile.path.value
#                self.workflowStepReport.addLogFile("BEST Log", "Best log file", strPathToBestLogFile)
                self.workflowStepReport.addLogFile("best_log", "Best log file", strPathToBestLogFile)
            if xsDataResultStrategy.fbestLogFile:
                strPathToFBestLogFile = xsDataResultStrategy.fbestLogFile.path.value
                #                self.workflowStepReport.addLogFile("BEST Log", "Best log file", strPathToBestLogFile)
                self.workflowStepReport.addLogFile("fbest_log", "FBest log file", strPathToFBestLogFile)
            if xsDataResultStrategy.raddoseLogFile:
                strPathToRaddoseLogFile = xsDataResultStrategy.raddoseLogFile.path.value
#                self.workflowStepReport.addLogFile("RADDOSE Log", "RADDOSE log file", strPathToRaddoseLogFile)
                self.workflowStepReport.addLogFile("raddose_log", "RADDOSE log file", strPathToRaddoseLogFile)


    def transmissionWarning(self):
        xsDataCollection = self.xsDataResultCharacterisation.getDataCollection()
        if xsDataCollection is not None:
            firstSubWedge = xsDataCollection.subWedge[0]
            # MXSUP-1445: Check if transmission is less than 10% and warn if it's the case
            xsDataBeam = firstSubWedge.getExperimentalCondition().getBeam()
            if xsDataBeam.getTransmission() is not None:
                fTransmission = xsDataBeam.getTransmission().getValue()
                if fTransmission < self.fMinTransmission:
                    strWarningMessage1 = "WARNING! Transmission for characterisation set to %.1f %%" % fTransmission
                    strWarningMessage2 = "If this transmission setting is not intentional, please consider re-characterising with transmission set to 100 %"
                    self.workflowStepReport.addWarning(strWarningMessage1)
                    self.workflowStepReport.addWarning(strWarningMessage2)

    def dataCollectionInfo(self):
        xsDataCollection = self.xsDataResultCharacterisation.getDataCollection()
        if xsDataCollection is not None:
            firstSubWedge = xsDataCollection.subWedge[0]
            firstImage = firstSubWedge.image[0]
            if firstImage.date is not None:
                strDate = firstImage.date.value
            else:
                strDate = "-----"
            strPrefix = EDUtilsImage.getPrefix(firstImage.path.value)
            strDirName = os.path.dirname(firstImage.path.value)
            dictTable = {"type": "table",
                         "title": "Data collection info",
                         "columns": [],
                         "data": []}
            listRow = []
            dictTable["columns"].append("Data collection date")
            listRow.append(strDate)
            dictTable["columns"].append("Image prefix")
            listRow.append(strPrefix)
            dictTable["columns"].append("Directory")
            listRow.append(strDirName)
            dictTable["data"].append(listRow)
            #
            self.workflowStepReport.addTable("Data collection info",
                                             dictTable["columns"],
                                             dictTable["data"],
                                             orientation="vertical")


    def diffractionPlan(self):
        # Do we have a diffracionPlan?
        xsDataDiffractionPlan = self.xsDataResultCharacterisation.getDataCollection().getDiffractionPlan()
        if xsDataDiffractionPlan is None:
            xsDataDiffractionPlan = XSDataDiffractionPlan()
        strTitle = "Diffraction Plan"
        strExtraColumnTitle = None
        strExtraColumnValue = None
        if xsDataDiffractionPlan.strategyOption is not None:
            strStrategyOption = xsDataDiffractionPlan.strategyOption.value
            if strStrategyOption.find("-helic") != -1:
                strTitle = "Helical Diffraction Plan"
                self.bIsHelical = True
                strExtraColumnTitle = "Helical\ndistance (mm)"
                if self.dataInput.helicalDistance is not None:
                    fHelicalDistance = self.dataInput.helicalDistance.value
                    strExtraColumnValue = "%.3f" % fHelicalDistance
                else:
                    strExtraColumnValue = "Unknown"
            elif strStrategyOption.find("-Npos") != -1:
                strTitle = "Multi-positional Diffraction Plan"
                self.bIsMultiPositional = True
        dictTable = {"type": "table",
                     "title": "Diffraction Plan",
                     "columns": [],
                     "data": []}
        dictTable["columns"].append("Forced\nspace group")
        dictTable["columns"].append("Anomalous\ndata")
        dictTable["columns"].append("Aimed\nmultiplicity")
        dictTable["columns"].append("Aimed\ncompleteness")
        dictTable["columns"].append("Aimed I/sigma\nat highest res.")
        dictTable["columns"].append("Aimed\nresolution (Å)")
        dictTable["columns"].append("Min osc.\nwidth")
        if strExtraColumnTitle is not None:
            dictTable["columns"].append(strExtraColumnTitle)
        listRow = []
        # Forced space group
        if xsDataDiffractionPlan.getForcedSpaceGroup() is None:
            strForcedSpaceGroup = "None"
        else:
            strForcedSpaceGroup = xsDataDiffractionPlan.getForcedSpaceGroup().getValue()
        listRow.append(strForcedSpaceGroup)
        # Anomalous data
        if xsDataDiffractionPlan.getAnomalousData() is None or xsDataDiffractionPlan.getAnomalousData().getValue() == False:
            strAnomalousData = "False"
        else:
            strAnomalousData = "True"
        listRow.append(strAnomalousData)
        # Aimed multiplicity
        if xsDataDiffractionPlan.getAimedMultiplicity() is None:
            strAimedMultiplicity = "Default\n(optimized)"
        else:
            strAimedMultiplicity = "%.2f" % xsDataDiffractionPlan.getAimedMultiplicity().getValue()
        listRow.append(strAimedMultiplicity)
        # Aimed completeness
        if xsDataDiffractionPlan.getAimedCompleteness() is None:
            strAimedCompleteness = "Default\n(>= 0.99)"
        else:
            strAimedCompleteness = "%.2f" % xsDataDiffractionPlan.getAimedCompleteness().getValue()
        listRow.append(strAimedCompleteness)
        # Aimed aimedIOverSigmaAtHighestResolution
        if xsDataDiffractionPlan.getAimedIOverSigmaAtHighestResolution() is None:
            strAimedIOverSigmaAtHighestResolution = "BEST Default"
        else:
            strAimedIOverSigmaAtHighestResolution = "%.2f" % xsDataDiffractionPlan.getAimedIOverSigmaAtHighestResolution().getValue()
        listRow.append(strAimedIOverSigmaAtHighestResolution)
        # Aimed resolution
        if xsDataDiffractionPlan.getAimedResolution() is None:
            strAimedResolution = "Default\n(highest possible)"
        else:
            strAimedResolution = "%0.2f" % xsDataDiffractionPlan.getAimedResolution().getValue()
        listRow.append(strAimedResolution)
        # Min osc width
        if xsDataDiffractionPlan.goniostatMinOscillationWidth is None:
            strMinOscWidth = "Default"
        else:
            strMinOscWidth = "%0.2f" % xsDataDiffractionPlan.goniostatMinOscillationWidth.value
        listRow.append(strMinOscWidth)
        if strExtraColumnValue is not None:
            listRow.append(strExtraColumnValue)
        #
        dictTable["data"].append(listRow)
        self.workflowStepReport.addTable(strTitle,
                                         dictTable["columns"],
                                         dictTable["data"])


    def createLinkToBestLogFile(self):
        xsDataResultStrategy = self.xsDataResultCharacterisation.getStrategyResult()


    def createThumbnailRowOfImages(self):
        # Thumbnail images of the predictions
        xsDataResultIndexing = self.xsDataResultCharacterisation.indexingResult
        listThumbnailImage = self.xsDataResultCharacterisation.thumbnailImage
        if len(listThumbnailImage) == 0:
            return
        self.workflowStepReport.startImageList()
        for xsDataSubWedge in self.xsDataResultCharacterisation.dataCollection.subWedge:
            for xsDataImage in xsDataSubWedge.image:
                strReferenceImageName = os.path.basename(xsDataImage.path.value)
                listJpegImage = self.xsDataResultCharacterisation.jpegImage
                for xsDataImageJpeg in listJpegImage:
                    if xsDataImageJpeg.number.value == xsDataImage.number.value:
                        strPathToJpegImage = xsDataImageJpeg.path.value
                for xsDataThumbnailImage in listThumbnailImage:
                    if xsDataThumbnailImage.number.value == xsDataImage.number.value:
                        strPathToThumbnailImage = xsDataThumbnailImage.path.value
                        break
                self.workflowStepReport.addImage(strPathToJpegImage,
                                                 imageTitle=os.path.basename(os.path.splitext(strPathToJpegImage)[0]),
                                                 pathToThumbnailImage=strPathToThumbnailImage)
        self.workflowStepReport.endImageList()


    def createPredictionRowOfImages(self):
        listPaths = []
        xsDataResultIndexing = self.xsDataResultCharacterisation.indexingResult
        if xsDataResultIndexing is not None:
            self.workflowStepReport.startImageList()
            for xsDataSubWedge in self.xsDataResultCharacterisation.dataCollection.subWedge:
                for xsDataImage in xsDataSubWedge.image:
                    xsDataResultPrediction = xsDataResultIndexing.predictionResult
                    listXSDataReferenceImage = xsDataResultIndexing.image
                    for xsDataImagePrediction in xsDataResultPrediction.predictionImage:
                        if xsDataImagePrediction.number.value == xsDataImage.number.value:
                            strPathToPredictionImage = xsDataImagePrediction.path.value
                            strFileName = os.path.basename(strPathToPredictionImage)
                            break
                    strReferenceFileName = None
                    if strReferenceFileName is None:
                        strReferenceFileName = strFileName
                    if os.path.exists(strPathToPredictionImage):
                        outfile = os.path.join(self.getWorkingDirectory(),
                                               os.path.splitext(os.path.basename(strPathToPredictionImage))[0] + ".thumbnail.jpg")
                        size = [256, 256]
                        im = Image.open(strPathToPredictionImage)
                        im.thumbnail(size, Image.ANTIALIAS)
                        im.save(outfile, "JPEG")
                        os.chmod(outfile, 0o644)
                        self.workflowStepReport.addImage(strPathToPredictionImage, os.path.basename(os.path.splitext(strFileName)[0]),
                                                         pathToThumbnailImage=outfile)
                        os.remove(outfile)
            self.workflowStepReport.endImageList()


    def createTableWithIndexResults(self, _xsDataResultIndexing, _strForcedSpaceGroup):
        xsDataSolutionSelected = _xsDataResultIndexing.getSelectedSolution()
        xsDataCrystal = xsDataSolutionSelected.getCrystal()
        xsDataCell = xsDataCrystal.getCell()
        strSpaceGroup = xsDataCrystal.spaceGroup.name.value
        tableTitle = "Indexing summary"
        if _strForcedSpaceGroup is None:
            spaceGroupTitle = "Selected spacegroup"
        else:
            if strSpaceGroup.upper() == _strForcedSpaceGroup.upper():
                spaceGroupTitle = "Forced spacegroup"
            else:
                spaceGroupTitle = "Selected spacegroup\n(Forced space group: %s)" % (_strForcedSpaceGroup)
        tableColumns = [spaceGroupTitle, "a [Å]", "b [Å]", "c [Å]", "alpha [°]", "beta [°]", "gamma [°]"]
        listRow = []
        tableData = []
        listRow.append(strSpaceGroup)
        listRow.append("%.3f" % xsDataCell.getLength_a().getValue())
        listRow.append("%.3f" % xsDataCell.getLength_b().getValue())
        listRow.append("%.3f" % xsDataCell.getLength_c().getValue())
        listRow.append("%.3f" % xsDataCell.getAngle_alpha().getValue())
        listRow.append("%.3f" % xsDataCell.getAngle_beta().getValue())
        listRow.append("%.3f" % xsDataCell.getAngle_gamma().getValue())
        tableData.append(listRow)
        self.workflowStepReport.addTable(tableTitle, tableColumns, tableData)

    def indexingLogFile(self):
        xsDataResultIndexing = self.xsDataResultCharacterisation.getIndexingResult()
        if xsDataResultIndexing is not None and xsDataResultIndexing.getIndexingLogFile():
            strPathToIndexingLogFile = xsDataResultIndexing.getIndexingLogFile().getPath().getValue()
#            self.workflowStepReport.addLogFile("Indexing Log", "Indexing log file", strPathToIndexingLogFile)
            self.workflowStepReport.addLogFile("indexing_log", "Indexing log file", strPathToIndexingLogFile)



    def imageQualityIndicatorResults(self):
        listXSDataResultImageQualityIndicators = self.xsDataResultCharacterisation.imageQualityIndicators
        bDozor = False
        for xsDataResultImageQualityIndicators in listXSDataResultImageQualityIndicators:
            if xsDataResultImageQualityIndicators.dozor_score is not None:
                bDozor = True
        tableColumns = []
        tableColumns.append("File")
        if bDozor:
            tableColumns.append("Dozor score (1)")
            tableColumns.append("Dozor visible res. [Å]")
            tableColumns.append("Tot integr signal (2)")
        else:
            tableColumns.append("Tot integr signal (1)")
        tableColumns.append("Spot total")
        tableColumns.append("In-Res Total")
        tableColumns.append("Good Bragg")
        tableColumns.append("Ice Rings")
        tableColumns.append("Meth 1 Res")
        tableColumns.append("Meth 2 Res")
        tableColumns.append("Max unit cell")
        tableData = []
        for xsDataResultImageQualityIndicators in listXSDataResultImageQualityIndicators:
            listRow = []
            listRow.append("%s" % os.path.basename(xsDataResultImageQualityIndicators.image.path.value))
            if bDozor:
                if xsDataResultImageQualityIndicators.dozor_score:
                    fDozor_score = xsDataResultImageQualityIndicators.dozor_score.value
                    if fDozor_score > 1.0:
                        listRow.append("%.1f" % fDozor_score)
                    else:
                        listRow.append("%.3f" % fDozor_score)
                else:
                    listRow.append("NA")
                if xsDataResultImageQualityIndicators.dozorVisibleResolution:
                    listRow.append("%.1f" % xsDataResultImageQualityIndicators.dozorVisibleResolution.value)
                else:
                    listRow.append("NA")
            if xsDataResultImageQualityIndicators.totalIntegratedSignal:
                listRow.append("%.0f" % xsDataResultImageQualityIndicators.totalIntegratedSignal.value)
            else:
                listRow.append("NA")
            listRow.append("%d" % xsDataResultImageQualityIndicators.spotTotal.value)
            listRow.append("%d" % xsDataResultImageQualityIndicators.inResTotal.value)
            listRow.append("%d" % xsDataResultImageQualityIndicators.goodBraggCandidates.value)
            listRow.append("%d" % xsDataResultImageQualityIndicators.iceRings.value)
            listRow.append("%.2f" % xsDataResultImageQualityIndicators.method1Res.value)
            if xsDataResultImageQualityIndicators.method2Res:
                listRow.append("%.2f" % xsDataResultImageQualityIndicators.method2Res.value)
            else:
                listRow.append("NA")
            if xsDataResultImageQualityIndicators.maxUnitCell:
                listRow.append("%.1f" % xsDataResultImageQualityIndicators.maxUnitCell.value)
            else:
                listRow.append("NA")
            tableData.append(listRow)
        self.workflowStepReport.addTable("Image quality indicators", tableColumns, tableData)
        # Some info about Dozor and Labelit
        if bDozor:
            self.workflowStepReport.addInfo("1. Dozor score: criteria of diffraction signal strength that uses intensities over background vs resolution. Popov 2014, to be published.")
            self.workflowStepReport.addInfo("2. Total integrated signal, spot total etc: results from cctbx Spotfinder")
        else:
            self.workflowStepReport.addInfo("1. Total integrated signal, spot total etc: results from cctbx Spotfinder")


    def findEDNALogFile(self):
        """Trying to locate the EDNA plugin launcher log file..."""
        strWorkingDir = self.getWorkingDirectory()
        strBaseDir = strWorkingDir
        strPathToLogFile = None
        for iLevels in range(4):
            strBaseDir = os.path.dirname(strBaseDir)
            self.DEBUG("Searching in strBaseDir: " + strBaseDir)
            # Now search for a ED*.log file...
            for strFileName in os.listdir(strBaseDir):
                if strFileName.startswith("ED") and strFileName.endswith(".log") and not os.path.isdir(os.path.join(strBaseDir, strFileName)):
                    # Check that the corresponding directory exists...
                    strStrippedFileName = strFileName.replace("EDPlugin", "")
                    strStrippedFileName = strStrippedFileName.replace(".log", "")
                    for strDirName in os.listdir(strBaseDir):
                        if os.path.isdir(os.path.join(strBaseDir, strDirName)):
                            if strDirName.find(strStrippedFileName) != -1:
                                # Final check - is the directory name in the working dir
                                if strWorkingDir.find(strDirName) != -1:
                                    # Ok, we found it!
                                    strPathToLogFile = os.path.join(strBaseDir, strFileName)
        return strPathToLogFile


    def graphs(self):
        if self.getDataInput().characterisationResult.strategyResult is None:
            return
        if self.getDataInput().characterisationResult.strategyResult.bestGraphFile == []:
            return
        listXSDataFile = self.getDataInput().characterisationResult.strategyResult.bestGraphFile
        if listXSDataFile != []:
            iIndex = 1
            # If -damPar is used only three plots are available:
            if len(listXSDataFile) >= 7:
                listPlotsToDisplay = [0, 1, 3, 6]
            elif len(listXSDataFile) >= 4:
                listPlotsToDisplay = [0, 1, 2, 3]
            else:
                listPlotsToDisplay = range(len(listXSDataFile))
            self.workflowStepReport.startImageList()
            for iIndexPlot in listPlotsToDisplay:
                xsDataFile = listXSDataFile[iIndexPlot]
                plotPath = xsDataFile.path.value
                plotFileName = os.path.basename(plotPath)
                plotTitle = os.path.splitext(plotFileName)[0]
                tmpOutfile = os.path.join(self.getWorkingDirectory(),
                                          plotTitle + ".thumbnail.jpg")
                size = [300, 200]
                im = Image.open(plotPath)
                im.thumbnail(size, Image.ANTIALIAS)
                im.save(tmpOutfile, "JPEG")
                self.workflowStepReport.addImage(plotPath, plotTitle, tmpOutfile)
                os.remove(tmpOutfile)
                iIndex += 1
                if iIndex > 4:
                    iIndex = 1
            self.workflowStepReport.endImageList()


    def kappaResults(self):

        if self.xsDataResultCharacterisation.kappaReorientation is not None and len(self.xsDataResultCharacterisation.kappaReorientation.solution) > 0:
            strPathToKappaLogFile = None
            if self.xsDataResultCharacterisation.kappaReorientation.logFile:
                strPathToKappaLogFile = self.xsDataResultCharacterisation.kappaReorientation.logFile.path.value
            tableColumns = ["Kappa", "Phi", "Settings"]
            listRow = []
            for solution in self.xsDataResultCharacterisation.kappaReorientation.solution:
                listRow.append(" %.2f " % float(solution.kappa.value))
                listRow.append(" %.2f " % float(solution.phi.value))
                listRow.append(" %s " % html.escape(solution.settings.value))
            tableData = []
            tableData.append(listRow)
            self.workflowStepReport.addTable("Suggested kappa goniostat reorientation (XOAlign*)",
                                             tableColumns, tableData)
            if strPathToKappaLogFile is not None:
#                self.workflowStepReport.addLogFile("Kappa re-orientation Log",
#                                                   "Kappa re-orientation Log",
#                                                   strPathToKappaLogFile)
                self.workflowStepReport.addLogFile("kappa_log",
                                                   "Kappa re-orientation Log",
                                                   strPathToKappaLogFile)
            self.workflowStepReport.addInfo("*) XOalign is a part of XDSme written by Pierre Legrand (https://code.google.com/p/xdsme)")
