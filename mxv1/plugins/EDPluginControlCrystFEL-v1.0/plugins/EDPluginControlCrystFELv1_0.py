# coding: utf8
#
#    Project: autoPROC
#             http://www.edna-site.org
#
#    Copyright (C) ESRF
#
#    Principal authors: Thomas Boeglin and Olof Svensson
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

__author__ = "Ivars Karpics"
__license__ = "GPLv2+"
__copyright__ = "EMBL Hamburg"

import os
import sys
import time
import socket

from EDPluginControl import EDPluginControl
from EDHandlerESRFPyarchv1_0 import EDHandlerESRFPyarchv1_0
from EDUtilsPath import EDUtilsPath
from EDHandlerXSDataISPyBv1_4 import EDHandlerXSDataISPyBv1_4

from EDFactoryPlugin import edFactoryPlugin
from EDUtilsMessenger import EDUtilsMessenger

from XSDataCommon import XSDataString, XSDataDouble

from XSDataControlCrystFELv1_0 import XSDataInputControlCrystFEL
from XSDataControlCrystFELv1_0 import XSDataResultControlCrystFEL

edFactoryPlugin.loadModule('XSDataCrystFELv1_0')

from XSDataCrystFELv1_0 import XSDataInputCrystFEL
from XSDataCrystFELv1_0 import XSDataResultCrystFEL

edFactoryPlugin.loadModule('XSDataISPyBv1_4')

from XSDataISPyBv1_4 import AutoProcContainer, AutoProc
from XSDataISPyBv1_4 import AutoProcProgram, AutoProcProgramContainer, AutoProcStatus, AutoProcProgramAttachment
from XSDataISPyBv1_4 import AutoProcScaling, AutoProcScalingContainer, AutoProcScalingStatistics
from XSDataISPyBv1_4 import AutoProcIntegrationContainer, AutoProcIntegration
from XSDataISPyBv1_4 import XSDataInputStoreAutoProc, XSDataInputStoreAutoProcStatus
from XSDataISPyBv1_4 import XSDataInputRetrieveDataCollection
from XSDataISPyBv1_4 import XSDataInputISPyBUpdateDataCollectionGroupComment
from XSDataISPyBv1_4 import Image



edFactoryPlugin.loadModule("XSDataMXWaitFilev1_1")
from XSDataMXWaitFilev1_1 import XSDataInputMXWaitFile

class EDPluginControlCrystFELv1_0(EDPluginControl):
    """
    Control plugin for 
    """


    def __init__(self):
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputControlCrystFEL)
        self.dataOutput = XSDataResultControlCrystFEL()
        self.pyarchPrefix = None
        self.resultsDirectory = None
        self.pyarchDirectory = None
        self.processingCommandLine = None
        self.processingPrograms = None
        self.hasUploadedResultsToISPyB = False

        self.baseName = None
        self.timeEnd = None

    def configure(self):
        EDPluginControl.configure(self)
        self.messenger = EDUtilsMessenger(self.config.get('mxCuBE_URI'))


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginControlCrystFELv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.dataCollectionId, "No data collection id")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginControlCrystFELv1_0.preProcess")
        self.screen("CrystFEL processing started")

        self.processingCommandLine = ' '.join(sys.argv)
        self.processingPrograms = "CrystFEL"

        self.strHost = socket.gethostname()
        self.screen("Running on {0}".format(self.strHost))
        try:
            strLoad = os.getloadavg()
            self.screen("System load avg: {0}".format(strLoad))
        except OSError:
            pass

        self.ispyb_retrieve_dc_plugin = self.loadPlugin("EDPluginISPyBRetrieveDataCollectionv1_4", "ispyb_retrieve_dc")
        self.index_plugin = self.loadPlugin("EDPluginExecCrystFELIndexv1_0", "indexamajig")

        self.process_hkl_plugin = self.loadPlugin("EDPluginExecCrystFELProcesshklv1_0", "process_hkl")
        self.process_hkl_plugin_odd = self.loadPlugin("EDPluginExecCrystFELProcesshklv1_0", "process_hkl_odd")
        self.process_hkl_plugin_even = self.loadPlugin("EDPluginExecCrystFELProcesshklv1_0", "process_hkl_even")
        self.partialator_plugin = self.loadPlugin("EDPluginExecCrystFELPartialatorv1_0", "partialator")

        self.post_process_plugin = self.loadPlugin("EDPluginExecCrystFELPostprocessv1_0", "post_process")

        self.store_autoproc_plugin = self.loadPlugin('EDPluginISPyBStoreAutoProcv1_4', "ispyb_store_autoproc")
        self.store_dc_comment_plugin = self.loadPlugin("EDPluginISPyBUpdateDataCollectionGroupCommentv1_4", "ispyb_store_dc_comment")

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG('EDPluginControlCrystFELv1_0.process starting')

        directory = None
        template = None
        imageNoStart = None
        imageNoEnd = None
        userName = os.environ["USER"]

        if self.dataInput.dataCollectionId is not None:
            # Recover the data collection from ISPyB
            #self.messenger.sendProcessingStatus(self.dataInput.dataCollectionId.value,
            #                                    "CrystFEL",
            #                                    "started")
            xsDataInputRetrieveDataCollection = XSDataInputRetrieveDataCollection()
            xsDataInputRetrieveDataCollection.dataCollectionId = self.dataInput.dataCollectionId
            self.ispyb_retrieve_dc_plugin.dataInput = xsDataInputRetrieveDataCollection
            self.ispyb_retrieve_dc_plugin.executeSynchronous()
            ispybDataCollection = self.ispyb_retrieve_dc_plugin.dataOutput.dataCollection

            directory = ispybDataCollection.imageDirectory
            if EDUtilsPath.isEMBL():
                #TODO PE2 has 7 digits others 5
                template = ispybDataCollection.fileTemplate.replace("%07d", "####")
            else:
                template = ispybDataCollection.fileTemplate.replace("%04d", "####")
            imageNoStart = ispybDataCollection.startImageNumber
            imageNoEnd = imageNoStart + ispybDataCollection.numberOfImages - 1

        # Process directory
        if self.dataInput.processDirectory is not None:
            processDirectory = self.dataInput.processDirectory.path.value
        else:
            processDirectory = directory.replace("RAW_DATA", "PROCESSED_DATA")

        dir_parts = processDirectory.split("/")
        processDirectory = "/data/users/%s" % os.path.join(*dir_parts[5:])

        # Make results directory
        self.resultsDirectory = os.path.join(processDirectory, "crystfel_results")
        try:
            if not os.path.exists(self.resultsDirectory):
                os.makedirs(self.resultsDirectory) 
        except Exception as ex:
            print ex 

        self.pyarchDirectory = EDHandlerESRFPyarchv1_0.createPyarchFilePath(directory)

        #TODO: enable when ready
        """
        if self.pyarchDirectory is not None:
            self.pyarchDirectory = self.pyarchDirectory.replace('PROCESSED_DATA', 'RAW_DATA')
            if not os.path.exists(self.pyarchDirectory):
                os.makedirs(self.pyarchDirectory)
        """

        self.baseFileName = "%s/crystfel_xgandalf_%d" % (
            self.resultsDirectory,
            self.dataInput.dataCollectionId.value
        )

        xsDataInputCrystFEL = XSDataInputCrystFEL()
        

        # Check if imagesFullPath exists. If not then generate one
        if self.dataInput.imagesFullPath is None:
            imagesFullPath = "%s_images_fullpath.lst" % self.baseName
            imagesFullFile = open(imagesFullPath, "w")
            for index in range(imageNoEnd - imageNoStart + 1):
                imagePath = os.path.join(directory, ispybDataCollection.fileTemplate % (index + 1))
                imagesFullFile.write("%s\n" % imagePath)
            imagesFullFile.close()
            xsDataInputCrystFEL.imagesFullPath = XSDataString(imagesFullPath)
        else:
            xsDataInputCrystFEL.imagesFullPath = self.dataInput.imagesFullPath

        xsDataInputCrystFEL.geomFile = self.dataInput.geomFile
        xsDataInputCrystFEL.cellFile = self.dataInput.cellFile
        xsDataInputCrystFEL.pointGroup = self.dataInput.pointGroup
        xsDataInputCrystFEL.spaceGroup = self.dataInput.spaceGroup
        xsDataInputCrystFEL.resCutOff= self.dataInput.resCutOff
        xsDataInputCrystFEL.baseFileName = XSDataString(self.baseFileName)

        
        self.timeStart = time.localtime()

        self.integration_id, self.program_id = self.create_integration_id(
            self.dataInput.dataCollectionId.value,
            "Creating integration ID")

        self.index_plugin.dataInput = xsDataInputCrystFEL
        self.process_hkl_plugin.dataInput = xsDataInputCrystFEL
        self.process_hkl_plugin_odd.dataInput = xsDataInputCrystFEL
        self.process_hkl_plugin_even.dataInput = xsDataInputCrystFEL
        self.partialator_plugin.dataInput = xsDataInputCrystFEL
        self.post_process_plugin.dataInput = xsDataInputCrystFEL
        self.post_process_plugin.dataOutput = XSDataResultCrystFEL

        self.process_hkl_plugin_odd.process_hkl_options += " --odd-only"
        self.process_hkl_plugin_odd.process_hkl_type = "o"
        self.process_hkl_plugin_even.process_hkl_options += " --even-only"
        self.process_hkl_plugin_even.process_hkl_type = "e"


        self.index_plugin.executeSynchronous()
        if self.index_plugin.isFailure():
            self.ERROR('indexamajig: Failed')
            self.setFailure()
            return
        else:
            self.screen('indexamajig: Finished')

        self.process_hkl_plugin.executeSynchronous()
        if self.process_hkl_plugin.isFailure():
            self.ERROR('process_hkl: Failed')
            self.setFailure()
            return
        else:
            self.screen('process_hkl: Finished') 

        self.process_hkl_plugin_odd.executeSynchronous()
        if self.process_hkl_plugin_odd.isFailure():
            self.ERROR('process_hkl_odd: Failed')
            self.setFailure()
            return
        else:
            self.screen('process_hkl_odd: Finished')

        self.process_hkl_plugin_even.executeSynchronous()
        if self.process_hkl_plugin_even.isFailure():
            self.ERROR('process_hkl_even: Failed')
            self.setFailure()
            return
        else:
            self.screen('process_hkl_even: Finished') 

        self.partialator_plugin.executeSynchronous()
        if self.partialator_plugin.isFailure():
            self.ERROR('partialator: Failed')
            self.setFailure()
            return
        else:
            self.screen('partialator: Finished')

        self.post_process_plugin.executeSynchronous()
        if self.post_process_plugin.isFailure():
            self.ERROR('post_process: Failed')
            self.setFailure()
            return
        else:
            self.screen('post_process: Finished')
 
        self.timeEnd = time.localtime()

    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginControlCrystFELv1_0.postProcess")

        """
        autoProcScalingStatisticsId : integer optional
        scalingStatisticsType : string
        comments : string
        resolutionLimitLow : float
        resolutionLimitHigh : float
        rMerge : float
        rMeasWithinIPlusIMinus : float
        rMeasAllIPlusIMinus : float
        rPimWithinIPlusIMinus : float
        rPimAllIPlusIMinus : float
        fractionalPartialBias : float
        nTotalObservations : integer
        ntotalUniqueObservations : integer
        meanIOverSigI : float
        completeness : float
        multiplicity : float
        anomalousCompleteness : float
        anomalousMultiplicity : float
        recordTimeStamp : string
        anomalous : boolean
        autoProcScalingId : integer
        ccHalf : float
        ccAno : float
        sigAno : float
        isa : float
        completenessSpherical : float
        anomalousCompletenessSpherical : float
        completenessEllipsoidal : float
        anomalousCompletenessEllipsoidal : float
        """

        """
        overallCompl : XSDataDouble
        overallRed : XSDataDouble
        overallSnr : XSDataDouble
        overallRsplit : XSDataDouble
        overallCC
        """

        output = AutoProcContainer()
        autoproc = AutoProc()
        autoproc.spaceGroup = str(self.dataInput.spaceGroup.value)
        output.AutoProc = autoproc

        scaling_container = AutoProcScalingContainer()
        scaling = AutoProcScaling()
        scaling.recordTimeStamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        scaling_container.AutoProcScaling = scaling

        #Open the cell file and get the cell parameters

        cell_file = open(self.dataInput.cellFile.value, "r")
        cell_params = {}
        for line in cell_file.readlines():
            if line.startswith("a ="):
                cell_params["a"] = float(line[4:9])
            elif line.startswith("b ="):
                cell_params["b"] = float(line[4:9])
            elif line.startswith("c ="):
                cell_params["c"] = float(line[4:9])
            elif line.startswith("al ="):
                cell_params["alpha"] = float(line[4:9])
            elif line.startswith("be ="):
                cell_params["beta"] = float(line[4:9])
            elif line.startswith("ga ="):
                cell_params["gamma"] = float(line[4:9])
        cell_file.close()

        autoproc.refinedCell_a = cell_params["a"]
        autoproc.refinedCell_b = cell_params["b"]
        autoproc.refinedCell_c = cell_params["c"]
        autoproc.refinedCell_alpha = cell_params["alpha"]
        autoproc.refinedCell_beta = cell_params["beta"]
        autoproc.refinedCell_gamma = cell_params["gamma"]

        overall_stats = AutoProcScalingStatistics()
        overall_stats.scalingStatisticsType = "innerShell"
        overall_stats.ccHalf = float(self.post_process_plugin.dataOutput.overallCC.value)
        overall_stats.resolutionLimitLow = float(self.post_process_plugin.dataOutput.resolutionLimitLow.value)
        overall_stats.resolutionLimitHigh = float(self.post_process_plugin.dataOutput.resolutionLimitHigh.value)
        overall_stats.completeness = float(self.post_process_plugin.dataOutput.overallCompl.value)
        #TODO get rMerge: otherwise results are not displayed in EXI
        overall_stats.rMerge = 0

        scaling_container.AutoProcScalingStatistics.append(overall_stats)

        integration_container = AutoProcIntegrationContainer()
        image = Image()
        image.dataCollectionId = self.dataInput.dataCollectionId.value
        integration_container.Image = image
 
        integration = AutoProcIntegration()
        if self.integration_id is not None:
            integration.autoProcIntegrationId = self.integration_id
            integration.cell_a = cell_params["a"]
            integration.cell_b = cell_params["b"]
            integration.cell_c = cell_params["c"]
            integration.cell_alpha = cell_params["alpha"]
            integration.cell_beta = cell_params["beta"]
            integration.cell_gamma = cell_params["gamma"]
            integration.anomalous = 0

        # done with the integration
        integration_container.AutoProcIntegration = integration
        scaling_container.AutoProcIntegrationContainer = integration_container

        program_container = AutoProcProgramContainer()
        program_container.AutoProcProgram = EDHandlerXSDataISPyBv1_4.createAutoProcProgram(
             programId=self.program_id, status="SUCCESS", timeStart=self.timeStart, timeEnd=self.timeEnd,
             processingCommandLine=self.processingCommandLine, processingPrograms=self.processingPrograms)

        output.AutoProcProgramContainer = program_container
        output.AutoProcScalingContainer = scaling_container

        for log_file in self.post_process_plugin.dataOutput.logFiles:
            pathToLogFile = log_file.path.value
            pyarchFileName = os.path.join(self.pyarchDirectory, os.path.basename(pathToLogFile))
            #shutil.copy(pathToLogFile, os.path.join(self.resultsDirectory, pyarchFileName))

            autoproc_program_attachment = AutoProcProgramAttachment()
            autoproc_program_attachment.fileName = os.path.basename(pyarchFileName)
            autoproc_program_attachment.filePath = os.path.dirname(pyarchFileName)
            autoproc_program_attachment.fileType = "Log"
            program_container.addAutoProcProgramAttachment(autoproc_program_attachment)
            self.screen("Result file %s uploaded to ISPyB" % os.path.basename(pyarchFileName))

        for data_file in self.post_process_plugin.dataOutput.dataFiles:
            pathToDataFile = data_file.path.value
            pyarchFileName = os.path.join(self.pyarchDirectory, os.path.basename(pathToDataFile))
            #shutil.copy(pathToLogFile, os.path.join(self.resultsDirectory, pyarchFileName))

            autoproc_program_attachment = AutoProcProgramAttachment()
            autoproc_program_attachment.fileName = os.path.basename(pyarchFileName)
            autoproc_program_attachment.filePath = os.path.dirname(pyarchFileName)
            autoproc_program_attachment.fileType = "Result"
            program_container.addAutoProcProgramAttachment(autoproc_program_attachment)
            self.screen("Result file %s uploaded to ISPyB" % os.path.basename(pyarchFileName))

        ispyb_input = XSDataInputStoreAutoProc()
        ispyb_input.AutoProcContainer = output

        self.store_autoproc_plugin.dataInput = ispyb_input
        self.store_autoproc_plugin.executeSynchronous()


        if self.store_autoproc_plugin.isFailure():
            self.ERROR("Could not upload results to ispyb!")
        else:
            self.hasUploadedAnomResultsToISPyB = True
            self.screen("Results uploaded to ISPyB")

        xsDataInput = XSDataInputISPyBUpdateDataCollectionGroupComment()
        xsDataInput.newComment = XSDataString(self.post_process_plugin.dataOutput.comment.value)
        xsDataInput.dataCollectionId = self.dataInput.dataCollectionId
        self.store_dc_comment_plugin.dataInput = xsDataInput
        self.executePluginSynchronous(self.store_dc_comment_plugin)

    def create_integration_id(self, datacollect_id, comments):
        autoproc_status = edFactoryPlugin.loadPlugin('EDPluginISPyBStoreAutoProcStatusv1_4')
        status_input = XSDataInputStoreAutoProcStatus()
        status_input.dataCollectionId = datacollect_id
        status_input.anomalous = True

        # needed even if we only want to get an integration ID?
        status_data = AutoProcStatus()
        status_data.step = "Indexing"
        status_data.status = "Launched"
        status_data.comments = comments

        # Program
        autoProcProgram = EDHandlerXSDataISPyBv1_4.createAutoProcProgram(
                    programId=None, status="RUNNING", timeStart=self.timeStart, timeEnd=self.timeEnd,
                    processingCommandLine=self.processingCommandLine, processingPrograms=self.processingPrograms)

        status_input.AutoProcProgram = autoProcProgram
        status_input.AutoProcStatus = status_data

        autoproc_status.dataInput = status_input
        # get our EDNAproc status id
        autoproc_status.executeSynchronous()
        return (autoproc_status.dataOutput.autoProcIntegrationId, autoproc_status.dataOutput.autoProcProgramId)
