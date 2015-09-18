#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
#                       Jerome Kieffer
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
from __future__ import with_statement
__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson", "Jerome Kieffer" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys, time
from EDThreading            import Semaphore
from EDCommandLine          import EDCommandLine
from EDVerbose              import EDVerbose
from EDConfigurationStatic  import EDConfigurationStatic
from EDMessage              import EDMessage
from EDUtilsPath            import EDUtilsPath
from EDUtilsFile            import EDUtilsFile
from EDFactoryPluginStatic  import EDFactoryPluginStatic


class EDApplication(object):
    """
    This is the main EDNA application class. This class can be sub-classed for any specific application need.
    An EDNA application is able to launch an entry point plugin. It accepts the following parameter:
    --execute    : name of the plugin to be executed 
    --inputFile  : related plugin data (xml input data file name)
    --outputFile : related plugin result (xml output data file name)
    --conf       : configuration file name
    --basedir    : where the application working directory should go 
    --DEBUG or --debug : turns on debugging   
    -v or --version : Displays the application name and version
    --verbose    : Turns on verbose mode
    --no-log     : Turns off logging
    -h or --help : Prints out an usage message
    """

    CONFIGURATION_PARAM_LABEL = "--conf"
    PLUGIN_PARAM_LABEL = "--execute"
    DATASET_PARAM_LABEL = "--inputFile"
    OUTPUT_PARAM_LABEL = "--outputFile"
    DATASET_BASE_DIRECTORY = "--basedir"
    DEBUG_PARAM_LABEL_1 = "--DEBUG"
    DEBUG_PARAM_LABEL_2 = "--debug"
    VERSION_PARAM_LABEL_1 = "-v"
    VERSION_PARAM_LABEL_2 = "--version"
    VERBOSE_MODE_LABEL = "--verbose"
    NO_LOG_LABEL = "--no-log"
    HELP_LABEL_1 = "-h"
    HELP_LABEL_2 = "--help"

    __edConfiguration = None
    __edFactoryPlugin = None
    __semaphore = Semaphore()


    def __init__(self, _strName="EDApplication", \
                  _strVersion="1.0.1", \
                  _strPluginName=None, \
                  _strConfigurationFileName=None, \
                  _strDataInputFilePath=None, \
                  _edLogFile=None, \
                  _strBaseDir=None, \
                  _strWorkingDir=None, \
                  _strDataOutputFilePath=None):
        self._strName = _strName
        self._strVersion = _strVersion
        self._strPluginName = _strPluginName
        self._strConfigurationFileName = _strConfigurationFileName
        self._strDataInputFilePath = _strDataInputFilePath
        self._strDataOutputFilePath = _strDataOutputFilePath
        self._edLogFile = _edLogFile
        self._strBaseDir = _strBaseDir
        self._strWorkingDir = _strWorkingDir
        self._strFullApplicationWorkingDirectory = None
        self._strXMLData = None
        self._listErrorMessages = []
        self._listWarningMessages = []
        self._xsDataOutput = None
        self._edObtainedOutputDataFile = None
        self._strDataOutputFilePath = None
        self._edPlugin = None
        self._edCommandLine = EDCommandLine(sys.argv)
        self._strApplicationInstanceName = self._strName + "_" + time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        self._strLogFileName = self._strApplicationInstanceName + ".log"
        self._bIsFailure = False
        self._strCurrentWorkingDirectory = os.getcwd()
        self._strConfigurationHome = None
        self._strPathToLogFile = None


    def execute(self):
        """
        This is the main execute method which executes preProcess, process and postProcess.
        """
        self.preProcess()
        self.process()
        self.postProcess()


    def preProcess(self):
        """
        Creates the application working directory (log dir)
        Initializes the configuration
        retrieves the plugin xml data to be passed to the plugin
        """
        EDVerbose.DEBUG("EDApplication.preProcess")
        self.processCommandline()
        if (not self._bIsFailure):
            # Check that the plugin can be located
            strPluginLocation = EDFactoryPluginStatic.getFactoryPlugin().getModuleLocation(self._strPluginName)
            if (strPluginLocation is None):
                EDVerbose.error("Plugin  %s cannot be loaded!" % self._strPluginName)
                self._bIsFailure = True
            # Check that the input file can be read
            if (self.getDataInputFilePath() is not None) and (not os.path.exists(self._strDataInputFilePath)):
                EDVerbose.error("Input XML file not found : %s" % self._strDataInputFilePath)
                self._bIsFailure = True
            # Check that the output file can be created
            if (self._strDataOutputFilePath is not None):
                strOutputDirectory = os.path.dirname(self._strDataOutputFilePath)
                if (strOutputDirectory is None or strOutputDirectory == ""):
                    strOutputDirectory = os.getcwd()
                    self._strDataOutputFilePath = os.path.join(strOutputDirectory, self._strDataOutputFilePath)
                if (not os.access(strOutputDirectory, os.W_OK)):
                    EDVerbose.error("Output directory not writable: %s" % strOutputDirectory)
                    self._bIsFailure = True
                elif (os.path.exists(self._strDataOutputFilePath)):
                    if (not os.access(self._strDataOutputFilePath, os.W_OK)):
                        EDVerbose.error("Output file not writable: %s" % self._strDataOutputFilePath)
                        self._bIsFailure = True
        if (not self._bIsFailure):
            EDVerbose.DEBUG("EDApplication.PLUGIN_PARAM_LABEL: " + EDApplication.PLUGIN_PARAM_LABEL)

            if self._strConfigurationFileName is not None:
                # Load the configuration file
                if (os.path.exists(self._strConfigurationFileName)):
                    EDVerbose.screen("Loading Configuration file: %s" % self._strConfigurationFileName)
                    EDConfigurationStatic.addConfigurationFile(self._strConfigurationFileName, _bReplace=True)
                else:
                    EDVerbose.warning("Cannot find configuration file: %s" % self._strConfigurationFileName)
            pyDictionary = {}
            pyDictionary[ "${EDNA_HOME}" ] = EDUtilsPath.getEdnaHome()
            if self.getDataInputFilePath() is not None:
                self._strXMLData = EDUtilsFile.readFileAndParseVariables(self.getDataInputFilePath(), pyDictionary)
            # Create the application working directory    
            if(self._strWorkingDir is None):
                self._strWorkingDir = self._strApplicationInstanceName
            self.createApplicationWorkingDirectory()


    def process(self):
        """
        Calls the Plugin to be executed
        """
        if (not self._bIsFailure):
            self._edPlugin = EDFactoryPluginStatic.loadPlugin(self._strPluginName)
            if(self._edPlugin is not None):
                self._edPlugin.setBaseDirectory(self._strFullApplicationWorkingDirectory)
                self._edPlugin.setBaseName(self._strPluginName)
                self._edPlugin.setDataInput(self._strXMLData)
                self._edPlugin.connectSUCCESS(self.doSuccessActionPlugin)
                self._edPlugin.connectFAILURE(self.doFailureActionPlugin)
                EDVerbose.DEBUG("EDApplication.process: Executing " + self._strPluginName)
                self._edPlugin.execute()
                self._edPlugin.synchronize()
            else:
                EDVerbose.error(EDMessage.ERROR_PLUGIN_NOT_LOADED_02 % ('EDApplication.process', self._strPluginName))
                self._bIsFailure = True




    def processCommandline(self):
        """
        This method is intended to be overridden by applications who
        would like to implement their own command line handling.
        
        This default method implements the following workflow:
            - Check for debug, verbose and log file command line options
        
        """
        EDVerbose.DEBUG("EDApplication.execute")
        EDVerbose.log(self._edCommandLine.getCommandLine())
        self.processCommandLineDebugVerboseLogFile()
        # Determine the base directory
        if(self._strBaseDir is None):
            self.processCommandLineBaseDirectory()
        # Set the name of the log file
        self._strPathToLogFile = os.path.abspath(os.path.join(self._strBaseDir, self._strLogFileName))
        EDVerbose.setLogFileName(self._strPathToLogFile)
        self.processCommandLineHelp()
        if (not self._bIsFailure):
            self.processCommandLineVersion()
        if (not self._bIsFailure):
            # Name of the plugin to be executed        
            if (self._strPluginName is None):
                self.processCommandLinePluginName()
            # Path to the input XML file
            if (self._strDataInputFilePath is None):
                self.processCommandLineInputFilePath()
            # Path to the output XML file
            if(self._strDataOutputFilePath is None):
                self.processCommandLineOutputFilePath()
            if (self._bIsFailure):
                self.usage()
        if (not self._bIsFailure):
            # If strConfigurationFileName is None, this means that it has not been given to the constructor\
            # It has been given by the command line\
            if(self._strConfigurationFileName is None):
                self._strConfigurationFileName = self.getCommandLineArgument(EDApplication.CONFIGURATION_PARAM_LABEL)



    def processCommandLineDebugVerboseLogFile(self):
        EDVerbose.DEBUG("EDApplication.processCommandLineDebugVerboseLogFile")
        EDVerbose.setVerboseOff()
        # Check if no log file
        if (self._edCommandLine.existCommand(EDApplication.NO_LOG_LABEL)):
            EDVerbose.setLogFileOff()
            EDVerbose.DEBUG("Log file output switched off")
        # Check if debug mode
        if (self._edCommandLine.existCommand(EDApplication.DEBUG_PARAM_LABEL_1) or
            self._edCommandLine.existCommand(EDApplication.DEBUG_PARAM_LABEL_2)):
            EDVerbose.setVerboseDebugOn()
            EDVerbose.DEBUG("Debug Mode [ON]")
        # Check if verbose
        if (self._edCommandLine.existCommand(EDApplication.VERBOSE_MODE_LABEL)):
            EDVerbose.setVerboseOn()


    def processCommandLineHelp(self):
        EDVerbose.DEBUG("EDApplication.processCommandLineHelp")
        if (self._edCommandLine.existCommand(EDApplication.HELP_LABEL_1)
            or self._edCommandLine.existCommand(EDApplication.HELP_LABEL_2)):
            EDVerbose.setVerboseOn()
            self.usage()
            self._bIsFailure = True


    def processCommandLineVersion(self):
        EDVerbose.DEBUG("EDApplication.processCommandLineVersion")
        if (self._edCommandLine.existCommand(EDApplication.VERSION_PARAM_LABEL_1) or
            self._edCommandLine.existCommand(EDApplication.VERSION_PARAM_LABEL_2)):
            EDVerbose.setVerboseOn()
            EDVerbose.screen("%s version %s" % (self._strName, self._strVersion))
            self._bIsFailure = True



    def processCommandLinePluginName(self):
        """
        """
        EDVerbose.DEBUG("EDApplication.processCommandLinePluginName")
        if (not self._edCommandLine.existCommand(EDApplication.PLUGIN_PARAM_LABEL)):
            EDVerbose.error("No %s command line argument found!" % EDApplication.PLUGIN_PARAM_LABEL)
            self._bIsFailure = True
        else:
            self._strPluginName = self.getCommandLineArgument(EDApplication.PLUGIN_PARAM_LABEL)
            EDVerbose.DEBUG("EDApplication.processCommandLinePluginName : %s = %s" % (EDApplication.PLUGIN_PARAM_LABEL, self._strPluginName))


    def processCommandLineInputFilePath(self):
        """
        """
        EDVerbose.DEBUG("EDApplication.processCommandLineInputFilePath")
        if (not self._edCommandLine.existCommand(EDApplication.DATASET_PARAM_LABEL)):
            EDVerbose.error("No %s command line argument found!" % EDApplication.DATASET_PARAM_LABEL)
            self._bIsFailure = True
        else:
            self._strDataInputFilePath = self.getCommandLineArgument(EDApplication.DATASET_PARAM_LABEL)
            EDVerbose.DEBUG("EDApplication.initApplication : %s = %s" % (EDApplication.DATASET_PARAM_LABEL, self._strDataInputFilePath))


    def processCommandLineOutputFilePath(self):
        """
        """
        EDVerbose.DEBUG("EDApplication.processCommandLineOutputFilePath")
        if (not self._edCommandLine.existCommand(EDApplication.OUTPUT_PARAM_LABEL)):
            EDVerbose.DEBUG("No %s command line argument found" % EDApplication.OUTPUT_PARAM_LABEL)
        else:
            self._strDataOutputFilePath = self.getCommandLineArgument(EDApplication.OUTPUT_PARAM_LABEL)
            EDVerbose.DEBUG("EDApplication.initApplication : %s = %s" % (EDApplication.OUTPUT_PARAM_LABEL, self._strDataOutputFilePath))


    def processCommandLineBaseDirectory(self):
        """
        """
        EDVerbose.DEBUG("EDApplication.processCommandLineBaseDirectory")
        self._strBaseDir = self.getCommandLineArgument(EDApplication.DATASET_BASE_DIRECTORY)
        if(self._strBaseDir is None):
            self._strBaseDir = os.getcwd()
            EDVerbose.DEBUG("Base directory set to current working directory = %s" % (self._strBaseDir))
        else:
            EDVerbose.DEBUG("%s = %s" % (EDApplication.DATASET_BASE_DIRECTORY, self._strBaseDir))





    def postProcess(self):
        """
        """
        # Restore the current working directory 
        os.chdir(self._strCurrentWorkingDirectory)


    @classmethod
    def usage(cls):
        """
        Print usage...
        """
        EDVerbose.screen("")
        EDVerbose.screen("Usage: ")
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Name of the plugin to be executed" % (cls.PLUGIN_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Path to the XML input file" % (cls.DATASET_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("-----------------------------------------------------------------------------------------------------------")
        EDVerbose.screen("")
        EDVerbose.screen(" Additional options available:")
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Path to the file wich will contain the XML output" % (cls.OUTPUT_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Base directory, i.e. working directory for the application" % (cls.DATASET_BASE_DIRECTORY))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Verbose mode" % (cls.VERBOSE_MODE_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : XSConfiguration file" % (cls.CONFIGURATION_PARAM_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : Executable version info" % (cls.VERSION_PARAM_LABEL_1 + " or " + cls.VERSION_PARAM_LABEL_2))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : DEBUG log traces" % (cls.DEBUG_PARAM_LABEL_1 + " or " + cls.DEBUG_PARAM_LABEL_2))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : No log file" % (cls.NO_LOG_LABEL))
        EDVerbose.screen("")
        EDVerbose.screen("%35s : This help message" % (cls.HELP_LABEL_1 + " or " + cls.HELP_LABEL_2))
        EDVerbose.screen("")


    @classmethod
    def getFactoryPlugin(cls):
        EDVerbose.WARNING("the use of EDclsetFactoryPlugin is deprecated. Please use EDFactoryPluginStatic.getFactoryPlugin instead.")
        return EDFactoryPluginStatic.getFactoryPlugin


    @classmethod
    def loadPlugin(cls, _strPluginName):
        EDVerbose.WARNING("The use of EDApplication.loadPlugin is deprecated. Please use EDFactoryPluginStatic.getFactoryPlugin instead.")
        return EDFactoryPluginStatic.loadPlugin(_strPluginName)


    @classmethod
    def loadModule(cls, _strModuleName):
        EDVerbose.WARNING("The use of EDApplication.loadModule is deprecated. Please use EDFactoryPluginStatic.getFactoryPlugin instead.")
        EDFactoryPluginStatic.loadModule(_strModuleName)


    def getDataInputFilePath(self):
        return self._strDataInputFilePath


    def getBaseDir(self):
        """
        Getter for base directory
        @return: path of the base directory
        @rtype: string
        """
        return self._strBaseDir


    def createApplicationWorkingDirectory(self):
        """
        Created the working directory of the application (<date>-<application name>)
        First tries to retrieve the base dir from --basedir option or related parameter from constructor
        Otherwise tries to retrieve it from EDNA_BASE_DIRECTORY environment variable
        Otherwise put the base dir as the current directory
        """
        EDVerbose.DEBUG("EDApplication.createApplicationWorkingDirectory")
        strBaseDirectory = self.getBaseDir()
        strDateTime = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        self._strFullApplicationWorkingDirectory = os.path.join(strBaseDirectory, self._strWorkingDir)
        # Check that a folder / file with the same name already exists
        if(os.path.exists(self._strFullApplicationWorkingDirectory) or \
            os.path.exists(self._strFullApplicationWorkingDirectory)):
            # It does exist so we have to modify the name of the working directory
            iIndex = 1
            bContinueFlag = True
            while (bContinueFlag):
                self._strFullApplicationWorkingDirectory = os.path.join(strBaseDirectory,
                                                                                        "%s_%d" % \
                                                                                        (strDateTime, \
                                                                                          iIndex))
                if(os.path.isdir(self._strFullApplicationWorkingDirectory) or \
                    os.path.exists(self._strFullApplicationWorkingDirectory)):
                    iIndex += 1
                else:
                    bContinueFlag = False
        # Add _nobackup suffix if run at the ESRF
        strEdnSite = EDUtilsPath.getEdnaSite()
        if EDUtilsPath.isESRF():
            self._strFullApplicationWorkingDirectory += "_nobackup"
        # Make the directory
        os.mkdir(self._strFullApplicationWorkingDirectory)
        # Change it to be the current working directory
        os.chdir(self._strFullApplicationWorkingDirectory)


    def getFullApplicationWorkingDirectory(self):
        return self._strFullApplicationWorkingDirectory

    def getCurrentWorkingDirectory(self):
        return self._strCurrentWorkingDirectory


    def doSuccessActionPlugin(self, _edPlugin):
        """
        """
        EDVerbose.DEBUG("EDApplication.doSuccessActionPlugin")
        # Print the potential Warnings and Errors
        self._listWarningMessages = _edPlugin.getListOfWarningMessages()
        EDVerbose.DEBUG("EDApplication.doSuccessActionPlugin: Plugin %s Successful with : %i Warnings " % (_edPlugin.getPluginName(), len(self._listWarningMessages)))
        for warningMessage in self._listWarningMessages:
            EDVerbose.screen(warningMessage)
        self._listErrorMessages = _edPlugin.getListOfErrorMessages()
        EDVerbose.DEBUG("EDApplication.doSuccessActionPlugin: Plugin %s Successful with : %i Errors" % (_edPlugin.getPluginName(), len(self._listErrorMessages)))
        for errorMessage in self._listErrorMessages:
            EDVerbose.error(errorMessage)
        if (_edPlugin.hasDataOutput()):
            xsDataOutput = _edPlugin.getDataOutput()
            if (xsDataOutput is not None and self._strDataOutputFilePath is not None):
                xsDataOutput.exportToFile(self._strDataOutputFilePath)
            if (xsDataOutput is not None and self._edObtainedOutputDataFile is not None):
                xsDataOutput.exportToFile(self._edObtainedOutputDataFile)


    def doFailureActionPlugin(self, _edPlugin):
        EDVerbose.DEBUG("EDApplication.doFailureActionPlugin")

        # Print the potential Warnings and Errors
        EDVerbose.DEBUG("EDApplication.doFailureActionPlugin: Plugin %s failed" % _edPlugin.getClassName())
        self._listWarningMessages = _edPlugin.getListOfWarningMessages()
        for warningMessage in self._listWarningMessages:
            EDVerbose.screen(warningMessage)

        self._listErrorMessages = _edPlugin.getListOfErrorMessages()
        for errorMessage in self._listErrorMessages:
            EDVerbose.screen(errorMessage)
        if (_edPlugin.hasDataOutput()):
            xsDataOutput = _edPlugin.getDataOutput()
            if (xsDataOutput is not None and self._strDataOutputFilePath is not None):
                xsDataOutput.exportToFile(self._strDataOutputFilePath)
            if (xsDataOutput is not None and self._edObtainedOutputDataFile is not None):
                xsDataOutput.exportToFile(self._edObtainedOutputDataFile)


    def getPlugin(self):
        return self._edPlugin


    def getPluginOutputData(self):
        return self._xsDataOutput


    def getWarningMessages(self):
        return self._listWarningMessages


    def getErrorMessages(self):
        return self._listErrorMessages


    def getEdCommandLine(self):
        return self._edCommandLine


    def getCommandLine(self):
        return self._edCommandLine.getCommandLine()


    def getCommandLineArguments(self):
        with self.__class__.__semaphore:
            edCommandLine = self._edCommandLine.getCommandLine()
        return edCommandLine

    def getCommandLineArgument(self, _strKey):
        with self.__class__.__semaphore:
            strCommandLineArgument = self._edCommandLine.getArgument(_strKey)
        return strCommandLineArgument

    @classmethod
    def synchronizeOn(cls):
        """
        Lock the whole class
        """
        cls.__semaphore.acquire()


    @classmethod
    def synchronizeOff(cls):
        """
        Unlock the whole class
        """
        cls.__semaphore.release()


    def getApplicationName(self):
        return self._strName + "-" + self._strVersion


    def getWorkingDir(self):
        """
        Getter for working dir
        @rtype: string
        @return working dir 
        """
        return self._strWorkingDir


    def setWorkingDir(self, _strDir):
        """
        Setter for working dir
        @type _strDir: string
        @param _strDir: working dir 
        """
        self._strWorkingDir = _strDir


    def isFailure(self):
        return self._bIsFailure


    def setFailure(self, _bFailure):
        self._bIsFailure = _bFailure


    def getPluginName(self):
        return self._strPluginName
