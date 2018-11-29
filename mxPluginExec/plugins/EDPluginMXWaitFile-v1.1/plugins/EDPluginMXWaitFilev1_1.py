#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2011-2013 European Synchrotron Radiation Facility
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


__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20140623"

import os, time

from EDPlugin import EDPlugin
from EDPluginExec import EDPluginExec

from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataInteger

from XSDataMXWaitFilev1_1 import XSDataInputMXWaitFile
from XSDataMXWaitFilev1_1 import XSDataResultMXWaitFile


class EDPluginMXWaitFilev1_1(EDPluginExec):
    """
    This plugin waits for a file to appear on disk
    """

    def __init__(self):
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputMXWaitFile)
        self.setDataOutput(XSDataResultMXWaitFile())
        self.expectedSize = None
        self.timeOut = 120  # s Default timeout
        self.strFilePath = None


    def configure(self, _edPlugin=None):
        EDPluginExec.configure(self)
        xsDataInputMXWaitFile = self.dataInput
        if xsDataInputMXWaitFile.file is None:
            strError = "No expected file path in input!"
            self.ERROR(strError)
            self.setFailure(true)
        else:
            self.strFilePath = xsDataInputMXWaitFile.file.path.value
            if xsDataInputMXWaitFile.size is not None:
                self.expectedSize = xsDataInputMXWaitFile.size.value
                self.DEBUG("Expected size: %d (bytes)" % self.expectedSize)
            if xsDataInputMXWaitFile.timeOut is None:
                configTimeOut = self.config.get(EDPlugin.CONF_TIME_OUT)
                if configTimeOut is not None:
                    self.timeOut = float(configTimeOut)
                    self.DEBUG("Using configured timeout = %.1f s" % self.timeOut)
                else:
                    self.DEBUG("Using default timeout = %.1f s" % self.timeOut)
            else:
                self.timeOut = xsDataInputMXWaitFile.timeOut.value
                self.DEBUG("Using timeout = %.1f s from input" % self.timeOut)
            # Set plugin timout to 60 s more in order to avoid EDPlugin timeout
            self.setTimeOut(self.timeOut + 60.0)


    def process(self, _edPlugin=None):
        EDPluginExec.process(self)
        # Wait for file if it's not already on disk'
        finalSize = None
        hasTimedOut = False
        shouldContinue = True
        fileDir = os.path.dirname(self.strFilePath)
        if os.path.exists(fileDir):
            # Patch provided by Sebastien 2018/02/09 for forcing NFS cache:
            self.DEBUG("NFS cache clear, doing os.fstat on directory {0}".format(fileDir))
            d = os.open(fileDir, os.O_DIRECTORY)
            statResult = os.fstat(d)
            self.DEBUG("Results of os.fstat: {0}".format(statResult))
        # Check if file is there
        if os.path.exists(self.strFilePath):
            fileSize = os.path.getsize(self.strFilePath)
            if self.expectedSize is not None:
                # Check size
                if fileSize > self.expectedSize:
                    shouldContinue = False
            finalSize = fileSize
        if shouldContinue:
            self.screen("Waiting %d seconds for file %s" % (self.timeOut, self.strFilePath))
            #
            timeStart = time.time()
            while shouldContinue and not hasTimedOut:
                # Sleep 1 s
                time.sleep(1)
                if os.path.exists(fileDir):
                    # Patch provided by Sebastien 2018/02/09 for forcing NFS cache:
                    self.DEBUG("NFS cache clear, doing os.fstat on directory {0}".format(fileDir))
                    d = os.open(fileDir, os.O_DIRECTORY)
                    statResult = os.fstat(d)
                    self.DEBUG("Results of os.fstat: {0}".format(statResult))
                # Try to execute a "ls" on the file directory - this sometimes speed up NFS
                #if os.path.exists(fileDir):
                #    os.system("ls %s > /dev/null" % fileDir)
                timeElapsed = time.time() - timeStart
                # Check if time out
                if timeElapsed > self.timeOut:
                    hasTimedOut = True
                    strWarning = "Timeout while waiting for file %s" % self.strFilePath
                    self.WARNING(strWarning)
                    self.addWarningMessage(strWarning)
                else:
                    # Check if file is there
                    if os.path.exists(self.strFilePath):
                        fileSize = os.path.getsize(self.strFilePath)
                        if self.expectedSize is not None:
                            # Check that it has right size
                            if fileSize > self.expectedSize:
                                shouldContinue = False
                        else:
                            shouldContinue = False
                        finalSize = fileSize
        self.dataOutput.timedOut = XSDataBoolean(hasTimedOut)
        if finalSize is not None:
            self.dataOutput.finalSize = XSDataInteger(finalSize)

