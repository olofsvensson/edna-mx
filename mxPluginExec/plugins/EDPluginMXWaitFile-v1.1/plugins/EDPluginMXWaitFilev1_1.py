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
        self.defaultTimeOut = 120 #s
        self.configTimeOut = None
    
    def configure(self):
        EDPluginExec.configure(self)
        configTimeOut = self.config.get(EDPlugin.CONF_TIME_OUT)
        if configTimeOut is not None:
            self.configTimeOut = float(configTimeOut)
            # Set plugin timout to 5 s more in order to avoid EDPlugin timeout
            self.setTimeOut(configTimeOut + 5.0)
            

    def process(self, _edPlugin=None):
        EDPluginExec.process(self)
        xsDataInputMXWaitFile = self.getDataInput()
        if xsDataInputMXWaitFile.file is None:
            strError = "No expected file path in input!"
            self.ERROR(strError)
            self.setFailure(true)
        else:
            strFilePath = xsDataInputMXWaitFile.file.path.value
            # Wait for file if it's not already on disk'
            if os.path.exists(strFilePath):
                self.dataOutput.timedOut = XSDataBoolean(False)
            else:
                self.screen("Waiting for file %s" % strFilePath)
                if xsDataInputMXWaitFile.size is None:
                    size = None
                else:
                    size = xsDataInputMXWaitFile.size.value
                    self.DEBUG("Expected size: %d (bytes)" % size)
                if xsDataInputMXWaitFile.timeOut is None:
                    if self.configTimeOut is None:
                        timeOut = self.defaultTimeOut
                        self.DEBUG("Using default timeout = %.1f s" % timeOut)
                    else:
                        timeOut = self.configTimeOut
                        self.DEBUG("Using configured timeout = %.1f s" % timeOut)
                else:
                    timeOut = xsDataInputMXWaitFile.timeOut.value
                    self.DEBUG("Using timeout = %.1f s from input" % timeOut)
                #
                hasTimedOut = False
                shouldContinue = True
                timeElapsed = 0
                while shouldContinue and not hasTimedOut:
                    # Sleep 1 s 
                    time.sleep(1)
                    timeElapsed += 1
                    # Check if time out
                    if timeElapsed > timeOut:
                        hasTimedOut = True
                        strWarning = "Timeout while waiting for file %s" % strFilePath
                        self.WARNING(strWarning)
                        self.addWarningMessage(strWarning)
                    else:
                        # Check if file is there
                        if os.path.exists(strFilePath):
                            if size is not None:
                                # Check that it has right size
                                if os.path.getsize(strFilePath) > size:
                                    shouldContinue = False
                            else:
                                shouldContinue = False
                self.dataOutput.timedOut = XSDataBoolean(hasTimedOut)
                    
                