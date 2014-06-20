# coding: utf8
#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) ESRF
#
#    Principal author:       Jerome Kieffer
#
#    Contributing author:    Olof Svensson
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

from __future__ import with_statement
__authors__ = ["Jerome Kieffer", "Olof Svensson"]
__contact__ = "kieffer@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "ESRF"
__date__ = "2014-06-20"
__status__ = "production"

import time, os
from EDPlugin             import EDPlugin
from EDConfiguration      import EDConfiguration
from EDApplication        import EDApplication
from XSDataMXWaitFilev1_0 import XSDataInputMXWaitFile, XSDataResultMXWaitFile
from XSDataCommon         import XSDataString, XSDataInteger, XSDataFile, XSPluginItem, XSDataBoolean
from EDThreading          import Semaphore


class EDPluginMXWaitFilev1_0(EDPlugin):
    """
    Plugins that waits for a file to be written and reach a certain size
    """
    #offers some extra seconds between officiel timeout and allows the plugin to finish gracefully.
    EXTRA_TIME = 5
    DELTA_TIME = 1
    DEFAULT_TIMEOUT = 2
    config_timeout = None
    writeXmlInOut = True
    writeDataXMLOutput = True
    writeDataXMLInput = True
    sem = Semaphore()

    def __init__(self):
        EDPlugin.__init__(self)
        self.setXSDataInputClass(XSDataInputMXWaitFile)
        self.filename = None
        self.exists = None
        self.filesize = None
        self.expectedSize = None
        self.timeout = self.DEFAULT_TIMEOUT



    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginMXWaitFilev1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getExpectedFile(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getExpectedSize(), "Data Input is None")

    def configure(self):
        """

        Configuration step of the plugin: mainly extend the timeout by 5 seconds to let the plugin finish.

        """
        if self.__class__.config_timeout is None:
            with self.__class__.sem:
                if self.__class__.config_timeout is None:
                    iTimeOut = self.config.get(EDPlugin.CONF_TIME_OUT, None)
                    if iTimeOut is not None:
                        self.DEBUG("EDPlugin.configure: Setting time out to %d s from plugin configuration." % iTimeOut)
                        self.__class__.config_timeout = iTimeOut
                    else:
                        self.__class__.config_timeout = self.getDefaultTimeOut()
                    self.__class__.writeXmlInOut = bool(self.config.get(self.CONF_WRITE_XML_INPUT_OUTPUT, True))
                    self.__class__.writeDataXMLOutput = bool(self.config.get(self.CONF_WRITE_XML_OUTPUT, True))
                    self.__class__.writeDataXMLInput = bool(self.config.get(self.CONF_WRITE_XML_INPUT, True))
        self.timeout = self.__class__.config_timeout
        self.setTimeOut(self.__class__.config_timeout + EDPluginMXWaitFilev1_0.EXTRA_TIME)
        self.setWriteXMLInputOutput(self.writeXmlInOut)
        self.setWriteXMLOutput(self.writeDataXMLOutput)
        self.setWriteXMLInput(self.writeDataXMLInput)

    def preProcess(self, _edObject=None):
        EDPlugin.preProcess(self)
        self.DEBUG("EDPluginMXWaitFilev1_0.preProcess")
        self.filename = self.getDataInput().getExpectedFile().getPath().getValue()
        self.expectedSize = self.getDataInput().getExpectedSize().getValue()
        if self.getDataInput().getTimeOut():
            self.timeout = self.getDataInput().getTimeOut().getValue()
            self.setTimeOut(self.getDataInput().getTimeOut().getValue() + EDPluginMXWaitFilev1_0.EXTRA_TIME)


    def process(self, _edObject=None):
        EDPlugin.process(self)
        self.DEBUG("EDPluginMXWaitFilev1_0.process")
        self.DEBUG("EDPluginMXWaitFilev1_0 Plugin TimeOut is set to: %s, internal TimeOut is %s" % (self.getTimeOut(), self.timeout))
        self.setTimeInit()
        dirname = os.path.dirname(self.filename)
        while self.getRunTime() < self.timeout:
            if os.path.isdir(dirname):
                fd = os.open(dirname, os.O_RDONLY)
                os.fstat(fd)
                os.close(fd)
                if os.path.exists(self.filename):
                    self.filesize = os.path.getsize(self.filename)
                    if self.filesize >= self.expectedSize:
                        break
            time.sleep(EDPluginMXWaitFilev1_0.DELTA_TIME)
        self.setTimeEnd()


    def postProcess(self, _edObject=None):
        EDPlugin.postProcess(self)
        self.DEBUG("EDPluginMXWaitFilev1_0.postProcess: Waited for %.3f s" % self.getRunTime())
        xsDataResult = XSDataResultMXWaitFile()
        if os.path.exists(self.filename):
            xsDataFile = XSDataFile()
            xsDataFile.setPath(XSDataString(self.filename))
            xsDataResult.setActualFile(xsDataFile)
            xsDataResult.setActualSize(XSDataInteger(os.path.getsize(self.filename)))
        xsDataResult.setTimedOut(XSDataBoolean(self.getRunTime() >= self.timeout))
        # Create some output data
        self.setDataOutput(xsDataResult)


