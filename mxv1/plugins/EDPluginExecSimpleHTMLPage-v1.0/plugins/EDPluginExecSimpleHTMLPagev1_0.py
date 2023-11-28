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

EDFactoryPluginStatic.loadModule("markupv1_10")
import markupv1_10

from report import WorkflowStepReport

from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile

from XSDataSimpleHTMLPagev1_0 import XSDataInputSimpleHTMLPage
from XSDataSimpleHTMLPagev1_0 import XSDataResultSimpleHTMLPage

EDFactoryPluginStatic.loadModule("XSDataMXv1")
from XSDataMXv1 import XSDataDiffractionPlan


class EDPluginExecSimpleHTMLPagev1_0(EDPluginExec):
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
        self.page = None
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
        self.DEBUG("EDPluginExecSimpleHTMLPagev1_0.configure")
        self.fMinTransmission = self.config.get("minTransmissionWarning", self.fMinTransmission)

    def preProcess(self, _edPlugin=None):
        EDPluginExec.preProcess(self, _edPlugin)
        self.DEBUG("EDPluginExecSimpleHTMLPagev1_0.preProcess...")
        self.xsDataResultCharacterisation = self.getDataInput().getCharacterisationResult()
        self.strHtmlFileName = "index.html"
        self.strPath = os.path.join(self.getWorkingDirectory(), self.strHtmlFileName)


    def process(self, _edPlugin=None):
        EDPluginExec.process(self, _edPlugin)
        self.DEBUG("EDPluginExecSimpleHTMLPagev1_0.process...")
        if self.xsDataResultCharacterisation is not None:
            # WorkflowStepReport
            self.workflowStepReport = WorkflowStepReport("Characterisation")
            # Create the simple characterisation result page
            self.page = markupv1_10.page(mode='loose_html')
            self.page.init(title="Characterisation Results",
                       footer="Generated on %s" % time.asctime())
            self.page.div(align_="CENTER")
            self.page.h1()
            if self.xsDataResultCharacterisation is not None:
                self.page.strong("Characterisation Results ")
                self.workflowStepReport.setTitle("Characterisation Results")
            else:
                self.page.strong("No Characterisation Results! ")
                self.workflowStepReport.setTitle("No Characterisation Results!")
            # Link to the EDNA log file
            if self.dataInput.logFile is None:
                strPathToLogFile = self.getLogFileName()
            else:
                strPathToLogFile = self.dataInput.logFile.path.value
            if strPathToLogFile is not None:
                self.page.strong("(")
                self.strPageEDNALog = os.path.join(self.getWorkingDirectory(), "edna_log.html")
                pageEDNALog = markupv1_10.page()
                pageEDNALog.h1("EDNA Log")
                pageEDNALog.a("Back to previous page", href_=self.strHtmlFileName)
                pageEDNALog.pre(html.escape(EDUtilsFile.readFile(strPathToLogFile)))
                pageEDNALog.a("Back to previous page", href_=self.strHtmlFileName)
                EDUtilsFile.writeFile(self.strPageEDNALog, str(pageEDNALog))
                self.page.a("EDNA log file", href_="edna_log.html")
                self.page.strong(")")
                self.workflowStepReport.addLogFile("EDNA Log", "EDNA log file", strPathToLogFile)
            self.page.h1.close()
            self.page.div.close()
            self.dataCollectionInfo()
            self.diffractionPlan()
            self.strategyResults()
            self.graphs()
            self.kappaResults()
            self.indexingResults()
            self.integrationResults()
            self.imageQualityIndicatorResults()
            self.createThumbnailRowOfImages()




    def finallyProcess(self, _edPlugin=None):
        EDPluginExec.finallyProcess(self, _edPlugin)
        self.DEBUG("EDPluginExecSimpleHTMLPagev1_0.finallyProcess...")
        # Render the page
        strHTML = str(self.page)
        EDUtilsFile.writeFile(self.strPath, strHTML)
        xsDataResultSimpleHTMLPage = XSDataResultSimpleHTMLPage()
        xsDataResultSimpleHTMLPage.setPathToHTMLFile(XSDataFile(XSDataString(self.strPath)))
        xsDataResultSimpleHTMLPage.setPathToHTMLDirectory(XSDataFile(XSDataString(os.path.dirname(self.strPath))))
        # Store in Pyarch
        if EDUtilsPath.isESRF() or EDUtilsPath.isEMBL() or EDUtilsPath.isMAXIV() or EDUtilsPath.isALBA:
            strPyarchPath = None
            if self.xsDataResultCharacterisation is not None:
                strPyarchPath = EDHandlerESRFPyarchv1_0.createPyarchHtmlDirectoryPath(self.xsDataResultCharacterisation.getDataCollection())
            if strPyarchPath is None:
                # For debugging purposes
                strPyarchPath = EDUtilsPath.getEdnaUserTempFolder()
            EDHandlerESRFPyarchv1_0.copyHTMLDir(_strPathToHTMLDir=os.path.dirname(self.strPath), _strPathToPyarchDirectory=strPyarchPath)
        # Write workflowStepReport HTML page
#        pathToIndexFile = self.workflowStepReport.renderHtml(self.getWorkingDirectory(), nameOfIndexFile="index_step.html")
        pathToJsonFile = self.workflowStepReport.renderJson(self.getWorkingDirectory())
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
            # Table containg indexing results and thumbnail images
            self.page.table(class_='indexResultsAndThumbnails', border_="0", cellpadding_="0")
            self.page.tr(align_="CENTER")
            self.page.td()
            # Table with indexing results
            self.createTableWithIndexResults(xsDataResultIndexing, strForcedSpaceGroup)
            self.page.td.close()
            # Thumbnail images
            self.page.td()
            self.createPredictionRowOfImages()
            self.page.td.close()
            self.page.tr.close()
            self.page.table.close()


    def integrationResults(self):
        # Was the integration successful?
        xsDataResultIntegration = self.xsDataResultCharacterisation.getIntegrationResult()
        if xsDataResultIntegration:
            iIntegration = 1
            for xsDataIntegrationSubWedgeResult in xsDataResultIntegration.getIntegrationSubWedgeResult():
                if xsDataIntegrationSubWedgeResult.getIntegrationLogFile() is not None:
                    strPathToIntegrationLogFile = xsDataIntegrationSubWedgeResult.getIntegrationLogFile().getPath().getValue()
                    strIntegrationHtmlPageName = "integration_%d_log.html" % iIntegration
                    strPageIntegrationLog = os.path.join(self.getWorkingDirectory(), strIntegrationHtmlPageName)
                    pageIntegrationLog = markupv1_10.page()
                    pageIntegrationLog.h1("Integration Log No %d" % iIntegration)
                    pageIntegrationLog.a("Back to previous page", href_=self.strHtmlFileName)
                    pageIntegrationLog.pre(html.escape(EDUtilsFile.readFile(strPathToIntegrationLogFile)))
                    pageIntegrationLog.a("Back to previous page", href_=self.strHtmlFileName)
                    EDUtilsFile.writeFile(strPageIntegrationLog, str(pageIntegrationLog))
                    self.page.a("Integration log file %d" % iIntegration, href=strIntegrationHtmlPageName)
                    self.page.br()
                    self.workflowStepReport.addLogFile("Integration Log No %d" % iIntegration,
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
                self.page.font(_color="red", size="+2")
                self.page.h2()
                self.page.strong("Strategy calculation not performed due to indexing failure, see the ")
                self.page.a("EDNA log file", href=os.path.basename(self.strPageEDNALog))
                self.page.strong(" for more details")
                self.page.h2.close()
                self.page.font.close()
                self.workflowStepReport.addWarning("Strategy calculation not performed due to indexing failure, see the EDNA log file for more details")
            elif xsDataResultIntegration is None:
                self.page.font(_color="red", size="+2")
                self.page.h2()
                self.page.strong("Strategy calculation not performed due to integration failure, see the ")
                self.page.a("EDNA log file", href=os.path.basename(self.strPageEDNALog))
                self.page.strong(" for more details")
                self.page.h2.close()
                self.page.font.close()
                self.workflowStepReport.addWarning("Strategy calculation not performed due to integration failure, see the EDNA log file for more details")
            else:
                self.page.font(_color="red", size="+2")
                self.page.h2()
                self.page.strong("Strategy calculation failed, see the ")
                self.page.a("EDNA log file", href=os.path.basename(self.strPageEDNALog))
                self.page.strong(" for more details")
                self.page.h2.close()
                self.page.font.close()
                self.workflowStepReport.addWarning("Strategy calculation failed, see the EDNA log file for more details")
        else:
            # Add link to BEST log file:
            if xsDataResultStrategy.getBestLogFile():
                strPathToBestLogFile = xsDataResultStrategy.getBestLogFile().getPath().getValue()
                if os.path.exists(strPathToBestLogFile):
                    strPageBestLog = os.path.join(self.getWorkingDirectory(), "best_log.html")
                    pageBestLog = markupv1_10.page()
                    pageBestLog.h1("BEST Log")
                    pageBestLog.a("Back to previous page", href_=self.strHtmlFileName)
                    pageBestLog.pre(html.escape(EDUtilsFile.readFile(strPathToBestLogFile)))
                    pageBestLog.a("Back to previous page", href_=self.strHtmlFileName)
                    EDUtilsFile.writeFile(strPageBestLog, str(pageBestLog))
            # Add link to RADDOSE log file:
            strPageRaddoseLog = None
            if xsDataResultStrategy.getRaddoseLogFile():
                strPathToRaddoseLogFile = xsDataResultStrategy.getRaddoseLogFile().getPath().getValue()
                strPageRaddoseLog = os.path.join(self.getWorkingDirectory(), "raddose_log.html")
                if os.path.exists(strPathToRaddoseLogFile):
                    pageRaddoseLog = markupv1_10.page()
                    pageRaddoseLog.h1("RADDOSE Log")
                    pageRaddoseLog.a("Back to previous page", href_=self.strHtmlFileName)
                    pageRaddoseLog.pre(html.escape(EDUtilsFile.readFile(strPathToRaddoseLogFile)))
                    pageRaddoseLog.a("Back to previous page", href_=self.strHtmlFileName)
                    EDUtilsFile.writeFile(strPageRaddoseLog, str(pageRaddoseLog))
            listXSDataCollectionPlan = xsDataResultStrategy.getCollectionPlan()
            if listXSDataCollectionPlan == []:
                self.page.font(_color="red", size="+2")
                self.page.h2()
                self.page.strong("Strategy calculation failed, see the ")
                self.page.a("BEST log file", href="best_log.html")
                self.page.strong(" for more details")
                if strPageRaddoseLog is not None:
                    self.page.a(" (RADDOSE log file)", href="raddose_log.html")
                self.page.h2.close()
                self.page.font.close()
                self.workflowStepReport.addWarning("Strategy calculation failed, see the BEST log file for more details")
            else:
                iNoSubWedges = len(listXSDataCollectionPlan)
                self.page.h2()
                if self.bIsHelical:
                    self.page.strong("Helical collection plan strategy (")
                    tabTitle = "Helical collection plan strategy"
                elif self.bIsMultiPositional:
                    self.page.strong("Multi-positional collection plan strategy (")
                    tabTitle = "Multi-positional collection plan strategy"
                elif iNoSubWedges != 1:
                    self.page.strong("Multi-wedge collection plan strategy (")
                    tabTitle = "Multi-wedge collection plan strategy"
                else:
                    self.page.strong("Collection plan strategy (")
                    tabTitle = "Collection plan strategy"
                if strPageRaddoseLog is not None:
                    self.page.a("RADDOSE log file", href="raddose_log.html")
                    self.page.strong(", ")
                self.page.a("BEST log file", href="best_log.html")
                self.page.strong(")")
                self.page.h2.close()
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
                            self.page.font(_color="red", size="+2")
                            self.page.i()
                            self.page.h2("Best has detected that the sample can diffract to %.2f &Aring;!" % fRankingResolution)
                            self.page.i.close()
                            self.page.font.close()
                            self.page.font(_color="red", size="+1")
                            self.page.strong("The current strategy is calculated to %.2f &Aring;." % fResolutionMax)
                            # self.page.strong("In order to calculate a strategy to %.2f &Aring; set the detector distance to %.2f mm (%.2f &Aring;) and re-launch the EDNA characterisation." % (fRankingResolution,fDistanceMin,fRankingResolution))
                            self.page.strong("In order to calculate a strategy to %.2f &Aring; move the detector to collect %.2f &Aring; data and re-launch the EDNA characterisation." % (fRankingResolution, fRankingResolution))
                            self.page.font.close()
                            self.workflowStepReport.addWarning("Best has detected that the sample can diffract to {0:.2f} &Aring;!".format(fRankingResolution))
                            self.workflowStepReport.addWarning("Move the detector to collect {0:.2f} &Aring; data and re-launch the EDNA characterisation.".format(fRankingResolution))
                        bHigherResolutionDetected = True


                for xsDataCollectionPlan in listXSDataCollectionPlan:
                    xsDataSummaryStrategy = xsDataCollectionPlan.getStrategySummary()
                    fResolutionMax = xsDataSummaryStrategy.getResolution().getValue()
                    strResolutionReasoning = ""
                    if xsDataSummaryStrategy.getResolutionReasoning():
                        strResolutionReasoning = xsDataSummaryStrategy.getResolutionReasoning().getValue()
                    self.page.table(class_='indexResults', border_="1", cellpadding_="0")
                    self.page.tr(align_="CENTER")
                    self.page.th(strResolutionReasoning, colspan_="9", bgcolor_=self.strTableColourTitle1)
                    self.page.tr.close()
                    self.page.tr(align_="CENTER", bgcolor_=self.strTableColourTitle2)
                    tableColumns = ["Wedge", "Subwedge", "Start (&deg;)", "Width (&deg;)", "No images",
                                    "Exp time (s)", "Max res (&Aring;)", "Rel trans (%)", "Distance (mm)"]
                    self.page.th("Wedge")
                    self.page.th("Subwedge")
                    self.page.th("Start (&deg;)")
                    self.page.th("Width (&deg;)")
                    self.page.th("No images")
                    self.page.th("Exp time (s)")
                    self.page.th("Max res (&Aring;)")
                    self.page.th("Rel trans (%)")
                    self.page.th("Distance (mm)")
                    self.page.tr.close()
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
                        self.page.tr(align_="CENTER", bgcolor_=self.strTableColourRows)
                        listRow = []
                        self.page.th(iWedge)
                        listRow.append(iWedge)
                        self.page.th(iRunNumber)
                        listRow.append(iRunNumber)
                        self.page.th("%.2f" % fRotationAxisStart)
                        listRow.append("%.2f" % fRotationAxisStart)
                        self.page.th("%.2f" % fOscillationWidth)
                        listRow.append("%.2f" % fOscillationWidth)
                        self.page.th(iNumberOfImages)
                        listRow.append(iNumberOfImages)
                        self.page.th("%.3f" % fExposureTime)
                        listRow.append("%.3f" % fExposureTime)
                        self.page.th("%.2f" % fResolutionMax)
                        listRow.append("%.2f" % fResolutionMax)
                        self.page.th("%.2f" % fTransmission)
                        listRow.append("%.2f" % fTransmission)
                        self.page.th("%.2f" % fDistance)
                        listRow.append("%.2f" % fDistance)
                        self.page.tr.close()
                        tableData.append(listRow)
                    self.page.table.close()
                    strResolutionReasoningFirstLower = strResolutionReasoning[0].lower() + strResolutionReasoning[1:]
                    self.workflowStepReport.addTable(tabTitle + ": " + strResolutionReasoningFirstLower, tableColumns, tableData)
        # Add log files
        if strPathToBestLogFile is not None:
            self.workflowStepReport.addLogFile("BEST Log", "Best log file", strPathToBestLogFile)
        if strPathToRaddoseLogFile is not None:
            self.workflowStepReport.addLogFile("RADDOSE Log", "RADDOSE log file", strPathToRaddoseLogFile)


    def dataCollectionInfo(self):
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
                    self.page.font(_color="red", size="+2")
                    self.page.i()
                    self.page.h2(strWarningMessage1 + "<br>" + strWarningMessage2)
                    self.page.i.close()
                    self.page.font.close()
                    self.workflowStepReport.addWarning(strWarningMessage1)
                    self.workflowStepReport.addWarning(strWarningMessage2)
            self.page.h2("Data collection info")
            firstImage = firstSubWedge.image[0]
            if firstImage.date is not None:
                strDate = firstImage.date.value
            else:
                strDate = "-----"
            strPrefix = EDUtilsImage.getPrefix(firstImage.path.value)
            strDirName = os.path.dirname(firstImage.path.value)
            self.page.table(class_='dataCollectionInfo', border_="1", cellpadding_="0")
            dictTable = {"type": "table",
                         "title": "Data collection info",
                         "columns": [],
                         "data": []}
            listRow = []
            self.page.tr(align_="CENTER")
            self.page.th("Data collection date", bgcolor_=self.strTableColourTitle2)
            dictTable["columns"].append("Data collection date")
            self.page.th(strDate, bgcolor_=self.strTableColourRows)
            listRow.append(strDate)
            self.page.tr.close()
            self.page.tr(align_="CENTER", bgcolor_=self.strTableColourTitle2)
            self.page.th("Image prefix", bgcolor_=self.strTableColourTitle2)
            dictTable["columns"].append("Image prefix")
            self.page.th(strPrefix, bgcolor_=self.strTableColourRows)
            listRow.append(strPrefix)
            self.page.tr.close()
            self.page.tr(align_="CENTER", bgcolor_=self.strTableColourTitle2)
            self.page.th("Directory", bgcolor_=self.strTableColourTitle2)
            dictTable["columns"].append("Directory")
            self.page.th(strDirName, bgcolor_=self.strTableColourRows)
            listRow.append(strDirName)
            self.page.tr.close()
            self.page.table.close()
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
                strExtraColumnTitle = "Helical<br>distance (mm)"
                if self.dataInput.helicalDistance is not None:
                    fHelicalDistance = self.dataInput.helicalDistance.value
                    strExtraColumnValue = "%.3f" % fHelicalDistance
                else:
                    strExtraColumnValue = "Unknown"
            elif strStrategyOption.find("-Npos") != -1:
                strTitle = "Multi-positional Diffraction Plan"
                self.bIsMultiPositional = True
        self.page.h2(strTitle)
        self.page.table(class_='diffractionPlan', border_="1", cellpadding_="0")
        dictTable = {"type": "table",
                     "title": "Diffraction Plan",
                     "columns": [],
                     "data": []}
        self.page.tr(align_="CENTER", bgcolor_=self.strTableColourTitle2)
        self.page.th("Forced<br>space group")
        dictTable["columns"].append("Forced\nspace group")
        self.page.th("Anomalous<br>data")
        dictTable["columns"].append("Anomalous\ndata")
        self.page.th("Aimed<br>multiplicity")
        dictTable["columns"].append("Aimed\nmultiplicity")
        self.page.th("Aimed<br>completeness")
        dictTable["columns"].append("Aimed\ncompleteness")
        self.page.th("Aimed I/sigma<br>at highest res.")
        dictTable["columns"].append("Aimed I/sigma\nat highest res.")
        self.page.th("Aimed<br>resolution (&Aring;)")
        dictTable["columns"].append("Aimed\nresolution (&Aring;)")
        self.page.th("Min osc.<br>width")
        dictTable["columns"].append("Min osc.\nwidth")
        if strExtraColumnTitle is not None:
            self.page.th(strExtraColumnTitle)
            dictTable["columns"].append(strExtraColumnTitle)
        self.page.tr.close()
        self.page.tr(align_="CENTER", bgcolor_=self.strTableColourRows)
        listRow = []
        # Forced space group
        if xsDataDiffractionPlan.getForcedSpaceGroup() is None:
            strForcedSpaceGroup = "None"
        else:
            strForcedSpaceGroup = xsDataDiffractionPlan.getForcedSpaceGroup().getValue()
        self.page.th(strForcedSpaceGroup)
        listRow.append(strForcedSpaceGroup)
        # Anomalous data
        if xsDataDiffractionPlan.getAnomalousData() is None or xsDataDiffractionPlan.getAnomalousData().getValue() == False:
            strAnomalousData = "False"
        else:
            strAnomalousData = "True"
        self.page.th(strAnomalousData)
        listRow.append(strAnomalousData)
        # Aimed multiplicity
        if xsDataDiffractionPlan.getAimedMultiplicity() is None:
            strAimedMultiplicity = "Default<br>(optimized)"
        else:
            strAimedMultiplicity = "%.2f" % xsDataDiffractionPlan.getAimedMultiplicity().getValue()
        self.page.th(strAimedMultiplicity)
        listRow.append(strAimedMultiplicity)
        # Aimed completeness
        if xsDataDiffractionPlan.getAimedCompleteness() is None:
            strAimedCompleteness = "Default<br>(>= 0.99)"
        else:
            strAimedCompleteness = "%.2f" % xsDataDiffractionPlan.getAimedCompleteness().getValue()
        self.page.th(strAimedCompleteness)
        listRow.append(strAimedCompleteness)
        # Aimed aimedIOverSigmaAtHighestResolution
        if xsDataDiffractionPlan.getAimedIOverSigmaAtHighestResolution() is None:
            strAimedIOverSigmaAtHighestResolution = "BEST Default"
        else:
            strAimedIOverSigmaAtHighestResolution = "%.2f" % xsDataDiffractionPlan.getAimedIOverSigmaAtHighestResolution().getValue()
        self.page.th(strAimedIOverSigmaAtHighestResolution)
        listRow.append(strAimedIOverSigmaAtHighestResolution)
        # Aimed resolution
        if xsDataDiffractionPlan.getAimedResolution() is None:
            strAimedResolution = "Default<br>(highest possible)"
        else:
            strAimedResolution = "%0.2f" % xsDataDiffractionPlan.getAimedResolution().getValue()
        self.page.th(strAimedResolution)
        listRow.append(strAimedResolution)
        # Min osc width
        if xsDataDiffractionPlan.goniostatMinOscillationWidth is None:
            strMinOscWidth = "Default"
        else:
            strMinOscWidth = "%0.2f" % xsDataDiffractionPlan.goniostatMinOscillationWidth.value
        self.page.th(strMinOscWidth)
        listRow.append(strMinOscWidth)
        if strExtraColumnValue is not None:
            self.page.th(strExtraColumnValue)
            listRow.append(strExtraColumnValue)
        # Close the table
        self.page.tr.close()
        self.page.table.close()
        dictTable["data"].append(listRow)
        #
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
        self.page.div(align_="left")
        self.page.table(class_='imageRow')
        self.page.tr(align_="CENTER")
        self.workflowStepReport.startImageList()
        for xsDataSubWedge in self.xsDataResultCharacterisation.dataCollection.subWedge:
            for xsDataImage in xsDataSubWedge.image:
                strReferenceImageName = os.path.basename(xsDataImage.path.value)
                listJpegImage = self.xsDataResultCharacterisation.jpegImage
                for xsDataImageJpeg in listJpegImage:
                    if xsDataImageJpeg.number.value == xsDataImage.number.value:
                        strPathToJpegImage = xsDataImageJpeg.path.value
                        strJpegFileName = os.path.basename(strPathToJpegImage)
                        shutil.copyfile(strPathToJpegImage, os.path.join(self.getWorkingDirectory(), strJpegFileName))
                        os.chmod(strPathToJpegImage, 0o644)
                for xsDataThumbnailImage in listThumbnailImage:
                    if xsDataThumbnailImage.number.value == xsDataImage.number.value:
                        strPathToThumbnailImage = xsDataThumbnailImage.path.value
                        strThumbnailFileName = os.path.basename(strPathToThumbnailImage)
                        shutil.copyfile(strPathToThumbnailImage, os.path.join(self.getWorkingDirectory(), strThumbnailFileName))
                        os.chmod(strPathToThumbnailImage, 0o644)
                        break
                self.workflowStepReport.addImage(strPathToJpegImage, imageTitle=os.path.splitext(strJpegFileName)[0], pathToThumbnailImage=strPathToThumbnailImage)
                self.page.td()
                self.page.table(class_='image')
                self.page.tr(align_="CENTER")
                self.page.td()
                strPageReferenceImage = os.path.splitext(strReferenceImageName)[0] + ".html"
                pageReferenceImage = markupv1_10.page()
                pageReferenceImage.init(title=strReferenceImageName,
                       footer="Generated on %s" % time.asctime())
                pageReferenceImage.h1(strReferenceImageName)
                pageReferenceImage.a("Back to previous page", href_=self.strHtmlFileName)
                pageReferenceImage.img(src=strJpegFileName, title=strJpegFileName)
                pageReferenceImage.a("Back to previous page", href_=self.strHtmlFileName)
                EDUtilsFile.writeFile(os.path.join(self.getWorkingDirectory(), strPageReferenceImage), str(pageReferenceImage))
                self.page.a(href=strPageReferenceImage)
                self.page.img(src=strThumbnailFileName, width=256, height=256, title=strReferenceImageName)
                self.page.a.close()
                self.page.td.close()
                self.page.tr.close()
                self.page.tr(align_="CENTER")
                self.page.td(strReferenceImageName, class_="caption")
                self.page.td.close()
                self.page.tr.close()
                self.page.table.close()
                self.page.td.close()
        self.workflowStepReport.endImageList()


    def createPredictionRowOfImages(self):
        listPaths = []
        xsDataResultIndexing = self.xsDataResultCharacterisation.indexingResult
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
                strLocalPath = os.path.join(self.getWorkingDirectory(), strFileName)
                self.page.td()
                if os.path.exists(strPathToPredictionImage):
                    shutil.copyfile(strPathToPredictionImage, strLocalPath)
                    listPaths.append(strLocalPath)
                    self.page.table(class_='image')
                    self.page.tr(align_="CENTER")
                    self.page.td()
                    strPageReferenceImage = os.path.splitext(strFileName)[0] + ".html"
                    pageReferenceImage = markupv1_10.page()
                    pageReferenceImage.init(title=strReferenceFileName,
                           footer="Generated on %s" % time.asctime())
                    pageReferenceImage.h1(strReferenceFileName)
                    pageReferenceImage.a("Back to previous page", href_=self.strHtmlFileName)
                    pageReferenceImage.img(src=strFileName, title=strReferenceFileName)
                    pageReferenceImage.a("Back to previous page", href_=self.strHtmlFileName)
                    EDUtilsFile.writeFile(os.path.join(self.getWorkingDirectory(), strPageReferenceImage), str(pageReferenceImage))
                    outfile = os.path.join(self.getWorkingDirectory(),
                                           os.path.splitext(os.path.basename(strPathToPredictionImage))[0] + ".thumbnail.jpg")
                    size = [256, 256]
                    im = Image.open(strPathToPredictionImage)
                    im.thumbnail(size, Image.LANCZOS)
                    im.save(outfile, "JPEG")
                    os.chmod(outfile, 0o644)
                    self.page.a(href=strPageReferenceImage)
                    self.page.img(src=os.path.basename(outfile), width=256, height=256, title=strFileName)
                    self.page.a.close()
                    self.page.td.close()
                    self.page.tr.close()
                    self.page.tr(align_="CENTER")
                    self.page.td(strReferenceFileName, class_="caption")
                    self.page.td.close()
                    self.page.tr.close()
                    self.page.table.close()
                    self.page.td.close()
                    self.workflowStepReport.addImage(strLocalPath, os.path.splitext(strFileName)[0],
                                                     pathToThumbnailImage=outfile)
        self.workflowStepReport.endImageList()
        self.page.table.close()
        self.page.div.close()


    def createTableWithIndexResults(self, _xsDataResultIndexing, _strForcedSpaceGroup):
        xsDataSolutionSelected = _xsDataResultIndexing.getSelectedSolution()
        xsDataCrystal = xsDataSolutionSelected.getCrystal()
        xsDataCell = xsDataCrystal.getCell()
        strSpaceGroup = xsDataCrystal.spaceGroup.name.value
        if _strForcedSpaceGroup is None:
            self.page.h3("Indexing summary: Selected spacegroup: %s" % strSpaceGroup)
        else:
            if strSpaceGroup.upper() == _strForcedSpaceGroup.upper():
                self.page.h3("Indexing summary: Forced spacegroup: %s" % strSpaceGroup)
            else:
                self.page.h3("Indexing summary: Selected spacegroup: %s, forced space group: %s" % (strSpaceGroup, _strForcedSpaceGroup))
        self.page.table(class_='indexResults', border_="1", cellpadding_="0")
        self.page.tr(align_="CENTER", bgcolor_=self.strTableColourTitle1)
        self.page.th("Refined unit cell parameters (&Aring;/degrees)", colspan_="6")
        self.page.tr.close()
        self.page.tr(align_="CENTER", bgcolor_=self.strTableColourTitle2)
        self.page.th("a (&Aring;)")
        self.page.th("b (&Aring;)")
        self.page.th("c (&Aring;)")
        self.page.th("alpha (&deg;)")
        self.page.th("beta (&deg;)")
        self.page.th("gamma (&deg;)")
        self.page.tr.close()
        tableColumns = ["a (&Aring;)", "b (&Aring;)", "c (&Aring;)", "alpha (&deg;)", "beta (&deg;)", "gamma (&deg;)"]
        self.page.tr(align_="CENTER", bgcolor_=self.strTableColourRows)
        listRow = []
        tableData = []
        self.page.td("%.3f" % xsDataCell.getLength_a().getValue())
        listRow.append("%.3f" % xsDataCell.getLength_a().getValue())
        self.page.td("%.3f" % xsDataCell.getLength_b().getValue())
        listRow.append("%.3f" % xsDataCell.getLength_b().getValue())
        self.page.td("%.3f" % xsDataCell.getLength_c().getValue())
        listRow.append("%.3f" % xsDataCell.getLength_c().getValue())
        self.page.td("%.3f" % xsDataCell.getAngle_alpha().getValue())
        listRow.append("%.3f" % xsDataCell.getAngle_alpha().getValue())
        self.page.td("%.3f" % xsDataCell.getAngle_beta().getValue())
        listRow.append("%.3f" % xsDataCell.getAngle_beta().getValue())
        self.page.td("%.3f" % xsDataCell.getAngle_gamma().getValue())
        listRow.append("%.3f" % xsDataCell.getAngle_gamma().getValue())
        self.page.td.close()
        self.page.tr.close()
        self.page.table.close()
        tableData.append(listRow)
        self.workflowStepReport.addTable("Indexing results", tableColumns, tableData)
        if _xsDataResultIndexing.getIndexingLogFile():
            strPathToIndexingLogFile = _xsDataResultIndexing.getIndexingLogFile().getPath().getValue()
            strPageIndexingLog = os.path.join(self.getWorkingDirectory(), "indexing_log.html")
            pageIndexingLog = markupv1_10.page()
            pageIndexingLog.h1("Indexing Log")
            pageIndexingLog.a("Back to previous page", href_=self.strHtmlFileName)
            pageIndexingLog.pre(html.escape(EDUtilsFile.readFile(strPathToIndexingLogFile)))
            pageIndexingLog.a("Back to previous page", href_=self.strHtmlFileName)
            EDUtilsFile.writeFile(strPageIndexingLog, str(pageIndexingLog))
            self.page.a("Indexing log file", href="indexing_log.html")
            self.workflowStepReport.addLogFile("Indexing Log", "Indexing log file", strPathToIndexingLogFile)



    def imageQualityIndicatorResults(self):
        listXSDataResultImageQualityIndicators = self.xsDataResultCharacterisation.imageQualityIndicators
        bDozor = False
        for xsDataResultImageQualityIndicators in listXSDataResultImageQualityIndicators:
            if xsDataResultImageQualityIndicators.dozor_score is not None:
                bDozor = True
        self.page.h3("Image quality indicators")
        self.page.table(class_='imageQualityIndicatorResults', border_="1", cellpadding_="0")
        self.page.tr(align_="CENTER", bgcolor_=self.strTableColourTitle2)
        tableColumns = []
        self.page.th("File")
        tableColumns.append("File")
        if bDozor:
            self.page.th("Dozor score (1)")
            tableColumns.append("Dozor score (1)")
            self.page.th("Tot integr signal (2)")
            tableColumns.append("Tot integr signal (2)")
        else:
            self.page.th("Tot integr signal (1)")
            tableColumns.append("Tot integr signal (1)")
        self.page.th("Spot total")
        tableColumns.append("Spot total")
        self.page.th("In-Res Total")
        tableColumns.append("In-Res Total")
        self.page.th("Good Bragg")
        tableColumns.append("Good Bragg")
        self.page.th("Ice Rings")
        tableColumns.append("Ice Rings")
        self.page.th("Meth 1 Res")
        tableColumns.append("Meth 1 Res")
        self.page.th("Meth 2 Res")
        tableColumns.append("Meth 2 Res")
        self.page.th("Max unit cell")
        tableColumns.append("Max unit cell")
        self.page.tr.close()
        tableData = []
        for xsDataResultImageQualityIndicators in listXSDataResultImageQualityIndicators:
            listRow = []
            self.page.tr(align_="CENTER", bgcolor_=self.strTableColourRows)
            self.page.td("%s" % os.path.basename(xsDataResultImageQualityIndicators.image.path.value))
            listRow.append("%s" % os.path.basename(xsDataResultImageQualityIndicators.image.path.value))
            if bDozor:
                if xsDataResultImageQualityIndicators.dozor_score:
                    fDozor_score = xsDataResultImageQualityIndicators.dozor_score.value
                    if fDozor_score > 1.0:
                        self.page.td("%.1f" % fDozor_score)
                        listRow.append("%.1f" % fDozor_score)
                    else:
                        self.page.td("%.3f" % fDozor_score)
                        listRow.append("%.3f" % fDozor_score)
                else:
                    self.page.td("NA")
                    listRow.append("NA")
            if xsDataResultImageQualityIndicators.totalIntegratedSignal:
                self.page.td("%.0f" % xsDataResultImageQualityIndicators.totalIntegratedSignal.value)
                listRow.append("%.0f" % xsDataResultImageQualityIndicators.totalIntegratedSignal.value)
            else:
                self.page.td("NA")
                listRow.append("NA")
            self.page.td("%d" % xsDataResultImageQualityIndicators.spotTotal.value)
            listRow.append("%d" % xsDataResultImageQualityIndicators.spotTotal.value)
            self.page.td("%d" % xsDataResultImageQualityIndicators.inResTotal.value)
            listRow.append("%d" % xsDataResultImageQualityIndicators.inResTotal.value)
            self.page.td("%d" % xsDataResultImageQualityIndicators.goodBraggCandidates.value)
            listRow.append("%d" % xsDataResultImageQualityIndicators.goodBraggCandidates.value)
            self.page.td("%d" % xsDataResultImageQualityIndicators.iceRings.value)
            listRow.append("%d" % xsDataResultImageQualityIndicators.iceRings.value)
            self.page.td("%.2f" % xsDataResultImageQualityIndicators.method1Res.value)
            listRow.append("%.2f" % xsDataResultImageQualityIndicators.method1Res.value)
            if xsDataResultImageQualityIndicators.method2Res:
                self.page.td("%.2f" % xsDataResultImageQualityIndicators.method2Res.value)
                listRow.append("%.2f" % xsDataResultImageQualityIndicators.method2Res.value)
            else:
                self.page.td("NA")
                listRow.append("NA")
            if xsDataResultImageQualityIndicators.maxUnitCell:
                self.page.td("%.1f" % xsDataResultImageQualityIndicators.maxUnitCell.value)
                listRow.append("%.1f" % xsDataResultImageQualityIndicators.maxUnitCell.value)
            else:
                self.page.td("NA")
                listRow.append("NA")
            self.page.td.close()
            self.page.tr.close()
            tableData.append(listRow)
        self.page.table.close()
        self.workflowStepReport.addTable("Image quality indicators", tableColumns, tableData)
        # Some info about Dozor and Labelit
        if bDozor:
            self.page.strong("1. Dozor score: criteria of diffraction signal strength that uses intensities over background vs resolution. Popov 2014, to be published.")
            self.workflowStepReport.addInfo("1. Dozor score: criteria of diffraction signal strength that uses intensities over background vs resolution. Popov 2014, to be published.")
            self.page.br()
            self.page.strong("2. Total integrated signal, spot total etc: results from ")
            self.workflowStepReport.addInfo("2. Total integrated signal, spot total etc: results from cctbx Spotfinder")
            self.page.a("cctbx Spotfinder", href="http://cci.lbl.gov/publications/download/ccn_jul2010_page18.pdf")
            self.page.br()
        else:
            self.page.strong("1. Total integrated signal, spot total etc: results from ")
            self.page.a("cctbx Spotfinder", href="http://cci.lbl.gov/publications/download/ccn_jul2010_page18.pdf")
            self.workflowStepReport.addInfo("1. Total integrated signal, spot total etc: results from cctbx Spotfinder")
            self.page.br()


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
        self.page.table(class_='bestGraphs', border_="0", cellpadding_="0")
        if self.getDataInput().characterisationResult.strategyResult is None:
            return
        if self.getDataInput().characterisationResult.strategyResult.bestGraphFile == []:
            return
        listXSDataFile = self.getDataInput().characterisationResult.strategyResult.bestGraphFile
        if listXSDataFile != []:
            self.page.tr(align_="CENTER")
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
                strFileName = os.path.basename(xsDataFile.path.value)
                # print strFileName
                shutil.copy(xsDataFile.path.value, os.path.join(self.getWorkingDirectory(), strFileName))
                self.page.td()
                strPageGraphFileName = os.path.splitext(strFileName)[0] + ".html"
                strPageGraphPath = os.path.join(self.getWorkingDirectory(), strPageGraphFileName)
                pageGraph = markupv1_10.page()
                pageGraph.init(title=strFileName,
                       footer="Generated on %s" % time.asctime())
                pageGraph.img(src=strFileName, title=strFileName)
                pageGraph.br()
                pageGraph.a("Back to previous page", href_=self.strHtmlFileName)
                EDUtilsFile.writeFile(strPageGraphPath, str(pageGraph))
                outfile = os.path.join(self.getWorkingDirectory(),
                                       os.path.splitext(strFileName)[0] + ".thumbnail.jpg")
                size = [300, 200]
                im = Image.open(xsDataFile.path.value)
                im.thumbnail(size, Image.LANCZOS)
                im.save(outfile, "JPEG")
                self.page.a(href=strPageGraphFileName)
                self.page.img(src=os.path.basename(outfile), title=strFileName)
                self.workflowStepReport.addImage(xsDataFile.path.value, "", pathToThumbnailImage=outfile)
                self.page.a.close()
                self.page.td.close()
                iIndex += 1
                if iIndex > 4:
                    iIndex = 1
                    self.page.tr.close()
                    self.page.tr(align_="CENTER")
            self.workflowStepReport.endImageList()
            self.page.tr.close()
            self.page.table.close()


    def kappaResults(self):

        if self.xsDataResultCharacterisation.kappaReorientation is not None and len(self.xsDataResultCharacterisation.kappaReorientation.solution) > 0:
            strPathToKappaLogFile = None
            if self.xsDataResultCharacterisation.kappaReorientation.logFile:
                strPathToKappaLogFile = self.xsDataResultCharacterisation.kappaReorientation.logFile.path.value
                strPageKappaLog = os.path.join(self.getWorkingDirectory(), "kappa_log.html")
                pageKappaLog = markupv1_10.page()
                pageKappaLog.h1("Kappa re-orientation Log")
                pageKappaLog.a("Back to previous page", href_=self.strHtmlFileName)
                pageKappaLog.pre(html.escape(EDUtilsFile.readFile(strPathToKappaLogFile)))
                pageKappaLog.a("Back to previous page", href_=self.strHtmlFileName)
                EDUtilsFile.writeFile(strPageKappaLog, str(pageKappaLog))
            self.page.h3()
            self.page.strong("Suggested kappa goniostat reorientation ( XOalign*, ")
            self.page.a("log file", href="kappa_log.html")
            self.page.strong("):")
            self.page.h3.close()
            self.page.table(class_='kappaSuggestedResult', border_="1", cellpadding_="1")
            self.page.tr(align_="CENTER", bgcolor_=self.strTableColourTitle2)
            self.page.th("Kappa")
            self.page.th("Phi")
            self.page.th("Settings")
            self.page.tr.close()
            tableColumns = ["Kappa", "Phi", "Settings"]
            listRow = []
            for solution in self.xsDataResultCharacterisation.kappaReorientation.solution:
                self.page.tr(align_="CENTER", bgcolor_=self.strTableColourRows)
                self.page.th(" %.2f " % float(solution.kappa.value))
                listRow.append(" %.2f " % float(solution.kappa.value))
                self.page.th(" %.2f " % float(solution.phi.value))
                listRow.append(" %.2f " % float(solution.phi.value))
                self.page.th(" %s " % html.escape(solution.settings.value))
                listRow.append(" %s " % html.escape(solution.settings.value))
                self.page.tr.close()
            self.page.table.close()
            self.page.br()
            self.page.strong("*) XOalign is a part of XDSme written by Pierre Legrand (https://code.google.com/p/xdsme)")
            self.page.br()
            self.page.br()
            self.page.br()
            tableData = []
            tableData.append(listRow)
            self.workflowStepReport.addTable("Suggested kappa goniostat reorientation (XOAlign*)",
                                             tableColumns, tableData)
            if strPathToKappaLogFile is not None:
                self.workflowStepReport.addLogFile("Kappa re-orientation Log",
                                                   "Kappa re-orientation Log",
                                                   strPathToKappaLogFile)
            self.workflowStepReport.addInfo("*) XOalign is a part of XDSme written by Pierre Legrand (https://code.google.com/p/xdsme)")
