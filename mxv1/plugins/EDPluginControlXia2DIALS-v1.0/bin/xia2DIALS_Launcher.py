#!/usr/bin/env python
#
#    Project: xia2DIALS
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
# xia2Launcher -path /data/visitor/mx415/id30a2/20160120/PROCESSED_DATA/test4/xds_mx415_run2_1 -mode after -datacollectionID 1640401 -residues 200 -anomalous False -cell "0,0,0,0,0,0"

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

from suds.client import Client
from suds.client import HttpAuthenticated

# XDS.INP creation is now asynchronous in mxcube, so it may not be here yet
# when we're started
WAIT_XDS_TIMEOUT = 300

BES_HOSTS = ["mxhpc2-1704.esrf.fr", "mxhpc2-1705.esrf.fr"]
BES_PORT = 8080
ispybUserName = ""
ispybPassword = ""


# setup the HTTP log handling
logger = logging.getLogger("xia2DIALS_Launcher")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(ch)

# do the arg parsing by hand since neither getopt nor optparse support
# single dash long options.

args = sys.argv[1:]
logger.debug("Input arguments: {0}".format(args))

if (len(args) % 2) != 0:
    logger.error("The argument list is not well formed (odd number of args/options)")
    sys.exit()

options = dict()
for x in range(0, len(args), 2):
    options[args[x]] = args[x + 1]

autoprocessingPath = options["-path"]
dataCollectionId = options["-datacollectionID"]

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



logger.debug("Beamline: {0}".format(beamline))
logger.debug("Proposal: {0}".format(proposal))

# Check if we have less than 8 images
transport = HttpAuthenticated(username=ispybUserName, password=ispybPassword)
if beamline == "id30a2":
    wdslRoot = "https://ispyb-valid.esrf.fr/ispyb/ispyb-ws/ispybWS"
else:
    wdslRoot = "https://ispyb.esrf.fr/ispyb/ispyb-ws/ispybWS"
collectionWdsl = os.path.join(wdslRoot, "ToolsForCollectionWebService?wsdl")
collectionWSClient = Client(collectionWdsl, transport=transport)
collect_params = collectionWSClient.service.findDataCollection(dataCollectionId)
if collect_params.numberOfImages < 8:
    logger.warning("Fewer than eight images, not launching autoPROC")
    sys.exit(0)

xia2DIALSPath = os.path.join(autoprocessingPath, "xia2DIALS")
if not os.path.exists(xia2DIALSPath):
    os.makedirs(xia2DIALSPath, 0o755)
xdsInputFile = os.path.join(autoprocessingPath, "XDS.INP")

# Wait for XDS input file
xdsAppeared = False
waitXdsStart = time.time()
logger.info("xia2DIALS launcher: waiting for XDS.INP file")
while not xdsAppeared and (time.time() - waitXdsStart < WAIT_XDS_TIMEOUT):
    time.sleep(1)
    if os.path.exists(xdsInputFile) and os.stat(xdsInputFile).st_size > 0:
        time.sleep(1)
        xdsAppeared = True
        logger.info("xia2DIALS launcher: XDS.INP file is there, size={0}".format(os.stat(xdsInputFile).st_size))
if not xdsAppeared:
    logger.error("XDS.INP file ({0}) failed to appear after {1} seconds".format(xdsInputFile, WAIT_XDS_TIMEOUT))
    sys.exit(1)

inputTemplate = """<?xml version="1.0"?>
<XSDataInputControlXia2DIALS>
  <dataCollectionId>
    <value>{dataCollectionId}</value>
  </dataCollectionId>
  <processDirectory>
    <path>
      <value>{xia2DIALSPath}</value>
    </path>
  </processDirectory>
</XSDataInputControlXia2DIALS>
"""

# the other parameters are not used right now
inputXml = inputTemplate.format(dataCollectionId=dataCollectionId,
                                xia2DIALSPath=xia2DIALSPath)

# we now need a temp file in the data dir to write the data model to
ednaInputFileName = "xia2DIALS_input.xml"
ednaInputFilePath = os.path.join(xia2DIALSPath, ednaInputFileName)
if os.path.exists(ednaInputFilePath):
    # Create unique file name
    ednaInputFile = tempfile.NamedTemporaryFile(suffix=".xml",
                                                prefix="xia2DIALS_input-",
                                                dir=xia2DIALSPath,
                                                delete=False)
    ednaInputFilePath = os.path.join(xia2DIALSPath, ednaInputFile.name)
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
xia2DIALSDirectory = "$xia2DIALSDirectory"
inputFile = "$inputFile"

pluginName = "EDPluginControlXia2DIALSv1_0"
os.environ["EDNA_SITE"] = "ESRF_ISPyB"
os.environ["ISPyB_user"]="$ispybUserName"
os.environ["ISPyB_pass"]="$ispybPassword"

EDVerbose.screen("Executing EDNA plugin %s" % pluginName)
EDVerbose.screen("EDNA_SITE %s" % os.environ["EDNA_SITE"])

hostname = socket.gethostname()
dateString  = time.strftime("%Y%m%d", time.localtime(time.time()))
timeString = time.strftime("%H%M%S", time.localtime(time.time()))
strPluginBaseDir = os.path.join("/tmp", beamline, dateString)
if not os.path.exists(strPluginBaseDir):
    try:
        os.makedirs(strPluginBaseDir, 0o755)
    except:
        pass

baseName = "{0}_xia2DIALS".format(timeString)
baseDir = os.path.join(strPluginBaseDir, baseName)
if not os.path.exists(baseDir):
    try:
        os.makedirs(baseDir, 0o755)
    except:
        pass
        
EDVerbose.screen("EDNA plugin working directory: %s" % baseDir)

linkName = "{hostname}_{date}-{time}".format(hostname=hostname,
                                             date=dateString,
                                             time=timeString)
os.symlink(baseDir, os.path.join(xia2DIALSDirectory, linkName))

ednaLogName = "xia2DIALS_{0}-{1}.log".format(dateString, timeString)
EDVerbose.setLogFileName(os.path.join(xia2DIALSDirectory, ednaLogName))
EDVerbose.setVerboseOn()

edPlugin = EDFactoryPluginStatic.loadPlugin(pluginName)
edPlugin.setDataInput(open(inputFile).read())
edPlugin.setBaseDirectory(strPluginBaseDir)
edPlugin.setBaseName(baseName)

EDVerbose.screen("Start of execution of EDNA plugin %s" % pluginName)
os.chdir(baseDir)
edPlugin.executeSynchronous()

 
"""



template = string.Template(scriptTemplate)
script = template.substitute(beamline=beamline,
                             proposal=proposal,
                             xia2DIALSDirectory=xia2DIALSPath,
                             dataCollectionId=options["-datacollectionID"],
                             inputFile=ednaInputFilePath,
                             ispybUserName=ispybUserName,
                             ispybPassword=ispybPassword)

# we also need some kind of script to run edna-plugin-launcher
ednaScriptFileName = "xia2DIALS_launcher.sh"
ednaScriptFilePath = os.path.join(xia2DIALSPath, ednaScriptFileName)
if os.path.exists(ednaScriptFilePath):
    # Create unique file name
    ednaScriptFile = tempfile.NamedTemporaryFile(suffix=".sh",
                                                 prefix="xia2DIALS_launcher-",
                                                 dir=xia2DIALSPath,
                                                 delete=False)
    ednaScriptFilePath = os.path.join(xia2DIALSPath, ednaScriptFile.name)
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
    logger.info("Trying to submit job on {host}:{port}".format(host=besHost, port=besPort))
    try:
        conn = httplib.HTTPConnection(besHost, besPort)
        params = urllib.urlencode({"ednaDpLaunchPath":os.path.join(xia2DIALSPath, ednaScriptFilePath),
                                   "beamline": beamline,
                                   "proposal": proposal,
                                   "initiator": beamline,
                                   "externalRef": proposal,
                                   "reuseCase": "true" })
        conn.request("POST",
                     "/BES/bridge/rest/processes/xia2DIALS/RUN?%s" % params,
                     headers={"Accept":"text/plain"})
        response = conn.getresponse()
        if response.status != 200:
            logger.error("RUN response status = {0}".format(response.status))
        else:
            submitSuccess = True
            logger.info("Job successfully submitted on {host}:{port}".format(host=besHost, port=besPort))
    except:
        logger.error("Cannot connect to BES server on {host}:{port}!".format(host=besHost, port=besPort))

