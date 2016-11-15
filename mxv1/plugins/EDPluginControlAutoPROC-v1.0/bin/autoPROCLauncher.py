#!/usr/bin/env python
#
#    Project: autoPROC
#             http://www.edna-site.org
#
#    Copyright (C) ESRF
#
#    Principal authors: Olof Svensson and Thomas Boeglin
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

__authors__ = ["Olof Svensson", "Thomas Boeglin"]
__license__ = "GPLv3+"
__copyright__ = "ESRF"

# called this way
# autoproc-launcher.py -path /data/visitor/mx415/id30a2/20160120/PROCESSED_DATA/test4/xds_mx415_run2_1 -mode after -datacollectionID 1640401 -residues 200 -anomalous False -cell "0,0,0,0,0,0"

import os
import sys
import time
import string
import urllib
import logging
import httplib
import logging
import tempfile
import subprocess

# XDS.INP creation is now asynchronous in mxcube, so it may not be here yet
# when we're started
WAIT_XDS_TIMEOUT = 300

BES_HOSTS = ["mxhpc2-1705.esrf.fr", "mxhpc2-1704.esrf.fr"]
BES_PORT = 8080


# setup the HTTP log handling
log = logging.getLogger()
log.setLevel(logging.DEBUG)


# do the arg parsing by hand since neither getopt nor optparse support
# single dash long options.

args = sys.argv[1:]

if (len(args) % 2) != 0:
    logging.error("the argument list is not well formed (odd number of args/options)")
    sys.exit()

options = dict()
for x in range(0, len(args), 2):
    options[args[x]] = args[x + 1]

autoprocessingPath = options["-path"]
autoPROCPath = os.path.join(autoprocessingPath, "autoPROC")
if not os.path.exists(autoPROCPath):
    os.makedirs(autoPROCPath, 0o755)
dataCollectionId = options["-datacollectionID"]


inputTemplate = """<?xml version="1.0"?>
<XSDataInputControlAutoPROC>
  <dataCollectionId>
    <value>{dataCollectionId}</value>
  </dataCollectionId>
  <processDirectory>
    <path>
      <value>{autoPROCPath}</value>
    </path>
  </processDirectory>
</XSDataInputControlAutoPROC>
"""

# the other parameters are not used right now
inputXml = inputTemplate.format(dataCollectionId=dataCollectionId,
                                autoPROCPath=autoPROCPath)

# we now need a temp file in the data dir to write the data model to
ednaInputFileName = "autoPROC_input.xml"
ednaInputFilePath = os.path.join(autoPROCPath, ednaInputFileName)
if os.path.exists(ednaInputFilePath):
    # Create unique file name
    ednaInputFile = tempfile.NamedTemporaryFile(suffix=".xml",
                                                prefix="autoPROC_input-",
                                                dir=autoPROCPath,
                                                delete=False)
    ednaInputFilePath = os.path.join(autoPROCPath, ednaInputFile.name)
    ednaInputFile.file.write(inputXml)
    ednaInputFile.close()
else:
    open(ednaInputFilePath, "w").write(inputXml)
os.chmod(ednaInputFilePath, 0o755)


scriptTemplate = """#!/usr/bin/env python

import os
import sys
import time
import socket
import traceback

sys.path.insert(0, "/opt/pxsoft/EDNA/vMX/edna/kernel/src")

from EDVerbose import EDVerbose
from EDFactoryPluginStatic import EDFactoryPluginStatic

beamline = "$beamline"
proposal = "$proposal"
dataCollectionId = $dataCollectionId
autoPROCDirectory = "$autoPROCDirectory"
inputFile = "$inputFile"

pluginName = "EDPluginControlAutoPROCv1_0"
os.environ["EDNA_SITE"] = "ESRF_ISPyBTest"
os.environ["ISPyB_user"]=""
os.environ["ISPyB_pass"]=""

EDVerbose.screen("Executing EDNA plugin %s" % pluginName)
EDVerbose.screen("EDNA_SITE %s" % os.environ["EDNA_SITE"])

hostname = socket.gethostname()
dateString  = time.strftime("%Y%m%d", time.localtime(time.time()))
timeString = time.strftime("%H%M%S", time.localtime(time.time()))
strPluginBaseDir = os.path.join("/tmp", beamline, dateString)
if not os.path.exists(strPluginBaseDir):
    os.makedirs(strPluginBaseDir, 0o755)

baseName = "{0}_autoPROC".format(timeString)
baseDir = os.path.join(strPluginBaseDir, baseName)
if not os.path.exists(baseDir):
    os.makedirs(baseDir, 0o755)
EDVerbose.screen("EDNA plugin working directory: %s" % baseDir)

linkName = "{hostname}_{date}-{time}".format(hostname=hostname,
                                             date=dateString,
                                             time=timeString)
os.symlink(baseDir, os.path.join(autoPROCDirectory, linkName))

ednaLogName = "autoPROC_{0}-{1}.log".format(dateString, timeString)
EDVerbose.setLogFileName(os.path.join(autoPROCDirectory, ednaLogName))
EDVerbose.setVerboseOn()

edPlugin = EDFactoryPluginStatic.loadPlugin(pluginName)
edPlugin.setDataInput(open(inputFile).read())
edPlugin.setBaseDirectory(strPluginBaseDir)
edPlugin.setBaseName(baseName)

EDVerbose.screen("Start of execution of EDNA plugin %s" % pluginName)
os.chdir(baseDir)
edPlugin.executeSynchronous()

 
"""

directories = autoprocessingPath.split(os.path.sep)
try:
    if directories[2] == "visitor":
        beamline = directories[4]
        proposal = directories[3]
    else:
        beamline = directories[2]
        proposal = directories[4]
except:
    beamline = "unknown"
    proposal = "unknown"

# For the time being we launch autoPROC only for opidXX, mxihrX and mx415
if not proposal.startswith("opid") or proposal.startswith("mxihr") or proposal != "mx415":
    # Proposal is not opidXX, mxihrX or mx415, not running autoPROC.
    sys.exit(0)


template = string.Template(scriptTemplate)
script = template.substitute(beamline=beamline,
                             proposal=proposal,
                             autoPROCDirectory=autoPROCPath,
                             dataCollectionId=options["-datacollectionID"],
                             inputFile=ednaInputFilePath)

# we also need some kind of script to run edna-plugin-launcher
ednaScriptFileName = "autoPROC_launcher.sh"
ednaScriptFilePath = os.path.join(autoPROCPath, ednaScriptFileName)
if os.path.exists(ednaScriptFilePath):
    # Create unique file name
    ednaScriptFile = tempfile.NamedTemporaryFile(suffix=".sh",
                                                 prefix="autoPROC_launcher-",
                                                 dir=autoPROCPath,
                                                 delete=False)
    ednaScriptFilePath = os.path.join(autoPROCPath, ednaScriptFile.name)
    ednaScriptFile.file.write(script)
    ednaScriptFile.close()
else:
    open(ednaScriptFilePath, "w").write(script)
os.chmod(ednaScriptFilePath, 0o755)


submitSuccess = False
remainingBesHosts = BES_HOSTS

while not submitSuccess and len(remainingBesHosts) > 0:
    besHost = remainingBesHosts.pop()
    besPort = BES_PORT
    log.info("autoPROC launcher: trying to submit job on {host}:{port}".format(host=besHost, port=besPort))
    try:
        conn = httplib.HTTPConnection(besHost, besPort)
        params = urllib.urlencode({"ednaDpLaunchPath":os.path.join(autoPROCPath, ednaScriptFilePath),
                                   "beamline": beamline,
                                   "proposal": proposal,
                                   "initiator": beamline,
                                   "externalRef": proposal,
                                   "reuseCase": "true" })
        conn.request("POST",
                     "/BES/bridge/rest/processes/autoPROC/RUN?%s" % params,
                     headers={"Accept":"text/plain"})
        response = conn.getresponse()
        if response.status != 200:
            log.error("RUN response status = {0}".format(response.status))
        else:
            submitSuccess = True
            log.info("autoPROC launcher: job successfully submitted on {host}:{port}".format(host=besHost, port=besPort))
    except:
        log.error("autoPROC launcher: cannot connect to BES server on {host}:{port}!".format(host=besHost, port=besPort))

