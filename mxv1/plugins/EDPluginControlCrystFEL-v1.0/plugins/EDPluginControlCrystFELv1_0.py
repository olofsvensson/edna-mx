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
import shutil

from EDPluginControl import EDPluginControl
from EDHandlerESRFPyarchv1_0 import EDHandlerESRFPyarchv1_0
from EDUtilsPath import EDUtilsPath
from EDHandlerXSDataISPyBv1_4 import EDHandlerXSDataISPyBv1_4

from EDFactoryPlugin import edFactoryPlugin
from EDUtilsMessenger import EDUtilsMessenger

from XSDataCommon import XSDataFile
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataString
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataTime

from XSDataControlCrystFELv1_0 import XSDataInputControlCrystFEL
from XSDataControlCrystFELv1_0 import XSDataResultControlCrystFEL

edFactoryPlugin.loadModule('XSDataCrystFELv1_0')

from XSDataCrystFELv1_0 import XSDataInputCrystFEL

edFactoryPlugin.loadModule('XSDataISPyBv1_4')
# plugin input/output
from XSDataISPyBv1_4 import AutoProcContainer
from XSDataISPyBv1_4 import AutoProcProgramAttachment
from XSDataISPyBv1_4 import XSDataInputRetrieveDataCollection
from XSDataISPyBv1_4 import XSDataInputStoreAutoProc


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
        self.hasUploadedNoanomResultsToISPyB = False

        self.baseName = None
        self.streamFilename = None

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
        self.processingPrograms = ""

        self.strHost = socket.gethostname()
        self.screen("Running on {0}".format(self.strHost))
        try:
            strLoad = os.getloadavg()
            self.screen("System load avg: {0}".format(strLoad))
        except OSError:
            pass

        self.wait_first_image_plugin = self.loadPlugin("EDPluginMXWaitFilev1_1", "wait_first")
        self.ispyb_retrieve_dc_plugin = self.loadPlugin("EDPluginISPyBRetrieveDataCollectionv1_4", "ispyb_retrieve_dc")
        self.index_plugin = self.loadPlugin("EDPluginExecCrystFELIndexv1_0", "indexamajig")

        self.process_hkl_plugin = self.loadPlugin("EDPluginExecCrystFELProcesshklv1_0", "process_hkl")
        self.process_hkl_plugin_odd = self.loadPlugin("EDPluginExecCrystFELProcesshklv1_0", "process_hkl_odd")
        self.process_hkl_plugin_even = self.loadPlugin("EDPluginExecCrystFELProcesshklv1_0", "process_hkl_even")
        self.partialator_plugin = self.loadPlugin("EDPluginExecCrystFELPartialatorv1_0", "partialator")

        self.post_process_plugin = self.loadPlugin("EDPluginExecCrystFELPostprocessv1_0", "post_process")

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG('EDPluginControlCrystFELv1_0.process starting')

        directory = None
        template = None
        imageNoStart = None
        imageNoEnd = None
        pathToStartImage = None
        pathToEndImage = None
        userName = os.environ["USER"]
        beamline = "unknown"
        proposal = "unknown"

        # If we have a data collection id, use it
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

            pathToStartImage = os.path.join(directory, ispybDataCollection.fileTemplate % imageNoStart)
            pathToEndImage = os.path.join(directory, ispybDataCollection.fileTemplate % imageNoEnd)

        # Process directory
        if self.dataInput.processDirectory is not None:
            processDirectory = self.dataInput.processDirectory.path.value
        else:
            processDirectory = directory.replace("RAW_DATA", "PROCESSED_DATA")

        # Make results directory
        self.resultsDirectory = os.path.join(processDirectory, "results")
        try:
            if not os.path.exists(self.resultsDirectory):
                os.makedirs(self.resultsDirectory, 755) 
        except Exception as ex:
            print ex 

        # Create path to pyarch
        self.pyarchDirectory = EDHandlerESRFPyarchv1_0.createPyarchFilePath(self.resultsDirectory)

        #TODO: enable when ready
        """
        if self.pyarchDirectory is not None:
            self.pyarchDirectory = self.pyarchDirectory.replace('PROCESSED_DATA', 'RAW_DATA')
            if not os.path.exists(self.pyarchDirectory):
                os.makedirs(self.pyarchDirectory, 755)
        """

        # Determine pyarch prefix
        listPrefix = template.split("_")
        self.pyarchPrefix = "di_{0}_run{1}".format(listPrefix[-3], listPrefix[-2])

        isH5 = False

        minSizeFirst = 1000000
        minSizeLast = 1000000
        fWaitFileTimeout = 60

        xsDataInputMXWaitFileFirst = XSDataInputMXWaitFile()
        xsDataInputMXWaitFileFirst.file = XSDataFile(XSDataString(pathToStartImage))
        xsDataInputMXWaitFileFirst.timeOut = XSDataTime(fWaitFileTimeout)
        self.wait_first_image_plugin.size = XSDataInteger(minSizeFirst)
        self.wait_first_image_plugin.dataInput = xsDataInputMXWaitFileFirst
        self.wait_first_image_plugin.executeSynchronous()
        if self.wait_first_image_plugin.dataOutput.timedOut.value:
            strWarningMessage = "Timeout after %d seconds waiting for the first image %s!" % (fWaitFileTimeout, pathToStartImage)
            self.addWarningMessage(strWarningMessage)
            self.WARNING(strWarningMessage)

        self.baseName = "%s/crystfel_xgandalf" % self.resultsDirectory

        self.streamFilename = "%s_%d.stream" % (
            self.baseName,
            self.dataInput.dataCollectionId.value
        )
        self.hklFilename = "%s_%d.hkl" % (
            self.baseName,
            self.dataInput.dataCollectionId.value
        )
        self.mtzFilename = "%s_%d.mtz" % (
            self.baseName,
            self.dataInput.dataCollectionId.value
        )

        # Prepare input to execution plugin
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

        #TODO EDNA can generate the imagesFull path if id do not exist
        xsDataInputCrystFEL.imagesFullPath = self.dataInput.imagesFullPath
        xsDataInputCrystFEL.streamFile = XSDataString(self.streamFilename)
        xsDataInputCrystFEL.hklFile = XSDataString(self.hklFilename)
        xsDataInputCrystFEL.mtzFile = XSDataString(self.mtzFilename)

        self.timeStart = time.localtime()

        """
        if self.dataInput.dataCollectionId is not None:
            # Set ISPyB to running
            self.autoProcIntegrationId, self.autoProcProgramId = \
              EDHandlerXSDataISPyBv1_4.setIspybToRunning(self, dataCollectionId=self.dataInput.dataCollectionId.value,
                                                         processingCommandLine=self.processingCommandLine,
                                                         processingPrograms=self.processingPrograms,
                                                         isAnom=True,
                                                         timeStart=self.timeStart)
        """
        self.index_plugin.dataInput = xsDataInputCrystFEL
        self.index_plugin.executeSynchronous()

        if self.index_plugin.isFailure():
            self.ERROR('indexamajig: Failed')
            self.setFailure()
            return
        else:
            self.screen('indexamajig: Finished')

        self.process_hkl_plugin.dataInput = xsDataInputCrystFEL
        self.process_hkl_plugin_odd.dataInput = xsDataInputCrystFEL
        self.process_hkl_plugin_even.dataInput = xsDataInputCrystFEL
        self.partialator_plugin.dataInput = xsDataInputCrystFEL
        self.post_process_plugin.dataInput = xsDataInputCrystFEL

        self.process_hkl_plugin_odd.process_hkl_options += " --odd-only"
        self.process_hkl_plugin_even.process_hkl_options += " --even-only"


        self.process_hkl_plugin.executeSynchronous()
        if self.process_hkl_plugin.isFailure():
            self.ERROR('process_hkl: Failed')
            self.setFailure()
            return
        else:
            self.screen('process_hkl: Finished') 


        self.process_hkl_plugin_odd.dataInput.hklFile = XSDataString(self.hklFilename + "_o")
        self.process_hkl_plugin_odd.executeSynchronous()
        if self.process_hkl_plugin_odd.isFailure():
            self.ERROR('process_hkl_odd: Failed')
            self.setFailure()
            return
        else:
            self.screen('process_hkl_odd: Finished')


        self.process_hkl_plugin_even.dataInput.hklFile = XSDataString(self.hklFilename + "_e")
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
 
        """ 
        self.edPluginExecCrystFELScale.dataInput = xsDataInputCrystFEL
        self.edPluginExecCrystFELScale.executeSynchronous()

        if self.edPluginExecCrystFELScale.isFailure():
            self.ERROR('CrystFELScalev1_0: Failed')
            self.setFailure()
            return
        else:
            self.screen('CrystFELScalev1_0: Finished')

        self.timeEnd = time.localtime()
        """

        # Upload to ISPyB
        """
        self.hasUploadedResultsToISPyB = self.uploadToISPyB(self.index_plugin, True, proposal,
                           self.autoProcProgramId, self.autoProcIntegrationId)
        if self.hasUploadedResultsToISPyB:
            self.screen("results uploaded to ISPyB")
        else:
            self.messenger.sendProcessingStatus(self.dataInput.dataCollectionId.value,
                                                "",
                                                "failed")

            EDHandlerXSDataISPyBv1_4.setIspybToFailed(self,
                         dataCollectionId=self.dataInput.dataCollectionId.value,
                         autoProcIntegrationId=self.autoProcIntegrationId,
                         autoProcProgramId=self.autoProcProgramId,
                         processingCommandLine=self.processingCommandLine,
                         processingPrograms=self.processingPrograms,
                         isAnom=True,
                         timeStart=self.timeStart,
                         timeEnd=self.timeEnd)
            self.ERROR("Could not upload results to ISPyB!")
        """

    def finallyProcess(self, _edObject=None):
        EDPluginControl.finallyProcess(self)
        self.index_plugin.synchronize()
        strMessage = ""
        if self.getListOfWarningMessages() != []:
            strMessage += "Warning messages: \n\n"
            for strWarningMessage in self.getListOfWarningMessages():
                strMessage += strWarningMessage + "\n\n"
        if self.getListOfErrorMessages() != []:
            strMessage += "Error messages: \n\n"
            for strErrorMessage in self.getListOfErrorMessages():
                strMessage += strErrorMessage + "\n\n"
        if self.isFailure():
            self.screen(" processing ended with errors!")
            #self.messenger.sendProcessingStatus(self.dataInput.dataCollectionId.value,
            #                                    "",
            #                                    "failed")

            if strMessage != "":
                self.screen("Warning and/or error messages: \n{0}.".format(strMessage))
            self.timeEnd = time.localtime()
            if self.dataInput.dataCollectionId is not None:
                # Upload program failure status to ISPyB
                # anom
                pass 
                #self.screen("Setting program status to failed in ISPyB.")
                """
                if not self.hasUploadedResultsToISPyB:
                    self.screen("Setting program status to failed in ISPyB.")
                    EDHandlerXSDataISPyBv1_4.setIspybToFailed(self,
                         dataCollectionId=self.dataInput.dataCollectionId.value,
                         autoProcIntegrationId=self.autoProcIntegrationId,
                         autoProcProgramId=self.autoProcProgramId,
                         processingCommandLine=self.processingCommandLine,
                         processingPrograms=self.processingPrograms,
                         isAnom=True,
                         timeStart=self.timeStart,
                         timeEnd=self.timeEnd)
                 """

        #else:
        #   self.messenger.sendProcessingStatus(self.dataInput.dataCollectionId.value,
        #                                       "cysFEL",
        #                                       "success")

    def uploadToISPyB(self, edPluginExecCrystFEL, isAnom, proposal, programId, integrationId):
        successUpload = False
        return successUpload

    def eiger_template_to_image(self, fmt, num):
        fileNumber = int(num / 100)
        if fileNumber == 0:
            fileNumber = 1
        fmt_string = fmt.replace("####", "1_data_%06d" % fileNumber)
        return fmt_string.format(num)

    def eiger_template_to_master(self, fmt):
        fmt_string = fmt.replace("####", "1_master")
        return fmt_string
