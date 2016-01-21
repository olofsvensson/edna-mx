#!/usr/bin/env python
#
#    Project: EDNAproc
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
ednaProcPath = os.path.join(autoprocessingPath, "EDNAproc")
if not os.path.exists(ednaProcPath):
    os.makedirs(ednaProcPath, 0755)
xdsInputFile = os.path.join(autoprocessingPath, "XDS.INP")
nres = None
try:
    nres = float(options.get("-residues"))
except Exception:
    pass
spacegroup = options.get("-sg")
cell = options.get("-cell")
dataCollectionId = options["-datacollectionID"]

# parse the input file to find the first image
xdsAppeared = False
waitXdsStart = time.time()
logging.info("EDNAproc launcher: waiting for XDS.INP file")
while not xdsAppeared and (time.time() - waitXdsStart < WAIT_XDS_TIMEOUT):
    time.sleep(1)
    if os.path.exists(xdsInputFile) and os.stat(xdsInputFile).st_size > 0:
        time.sleep(1)
        xdsAppeared = True
        logging.info("EDNAproc launcher: XDS.INP file is there, size={0}".format(os.stat(xdsInputFile).st_size))
if not xdsAppeared:
    logging.error("XDS.INP file ({0}) failed to appear after {1} seconds".format(xdsInputFile, WAIT_XDS_TIMEOUT))
    sys.exit(1)


ednaOutputFileName = "EDNAproc_ispyb.xml"
ednaOutputFilePath = os.path.join(ednaProcPath, ednaOutputFileName)
if os.path.exists(ednaOutputFilePath):
    ednaOutputFile = tempfile.NamedTemporaryFile(suffix=".xml",
                                                 prefix="EDNAproc_ispyb-",
                                                 dir=ednaProcPath,
                                                 delete=False)
    ednaOutputFilePath = os.path.join(ednaProcPath, ednaOutputFile.name)
    ednaOutputFile.close()
else:
    open(ednaOutputFilePath, "w").write("")
os.chmod(ednaOutputFilePath, 0755)

inputTemplate = """<?xml version="1.0"?>
<XSDataAutoprocInput>
  <input_file>
    <path>
      <value>{xdsInputFile}</value>
    </path>
  </input_file>
  <data_collection_id>
    <value>{dataCollectionId}</value>
  </data_collection_id>
  <output_file>
    <path>
      <value>{output_path}</value>
    </path>
  </output_file>
{nresFragment}
{spacegroupFragment}
{cellFragment}
</XSDataAutoprocInput>
"""

# ignore null nres, which might happen for whatever reason
if nres is not None and nres != 0:
    nresFragment = """  <nres>
    <value>{0}</value>
  </nres>""".format(nres)
else:
    nresFragment = ""

if spacegroup is not None:
    spacegroupFragment = """  <spacegroup>
    <value>{0}</value>
  </spacegroup>""".format(spacegroup)
else:
    spacegroupFragment = ""

if cell is not None:
    cellFragment = """  <unit_cell>
    <value>{0}</value>
  </unit_cell>""".format(cell)
else:
    cellFragment = ""

# the other parameters are not used right now
inputXml = inputTemplate.format(xdsInputFile=xdsInputFile,
                                dataCollectionId=dataCollectionId,
                                output_path=ednaOutputFilePath,
                                nresFragment=nresFragment,
                                cellFragment=cellFragment,
                                spacegroupFragment=spacegroupFragment)

# we now need a temp file in the data dir to write the data model to
ednaInputFileName = "EDNAproc_input.xml"
ednaInputFilePath = os.path.join(ednaProcPath, ednaInputFileName)
if os.path.exists(ednaInputFilePath):
    # Create unique file name
    ednaInputFile = tempfile.NamedTemporaryFile(suffix=".xml",
                                                prefix="EDNAproc_input-",
                                                dir=ednaProcPath,
                                                delete=False)
    ednaInputFilePath = os.path.join(ednaProcPath, ednaInputFile.name)
    ednaInputFile.file.write(inputXml)
    ednaInputFile.close()
else:
    open(ednaInputFilePath, "w").write(inputXml)
os.chmod(ednaInputFilePath, 0755)


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
ednaProcDirectory = "$ednaProcDirectory"
inputFile = "$inputFile"

pluginName = "EDPluginControlAutoprocv1_0"
os.environ["EDNA_SITE"] = "ESRF_ISPyBTest"
os.environ["ISPyB_user"]="user"
os.environ["ISPyB_pass"]="password"

EDVerbose.screen("Executing EDNA plugin %s" % pluginName)
EDVerbose.screen("EDNA_SITE %s" % os.environ["EDNA_SITE"])

hostname = socket.gethostname()
dateString  = time.strftime("%Y%m%d", time.localtime(time.time()))
timeString = time.strftime("%H%M%S", time.localtime(time.time()))
strPluginBaseDir = os.path.join("/tmp", beamline, dateString)
if not os.path.exists(strPluginBaseDir):
    os.makedirs(strPluginBaseDir, 0755)

baseName = "{0}_EDNAproc".format(timeString)
baseDir = os.path.join(strPluginBaseDir, baseName)
if not os.path.exists(baseDir):
    os.makedirs(baseDir, 0755)
EDVerbose.screen("EDNA plugin working directory: %s" % baseDir)

linkName = "{hostname}_{date}-{time}".format(hostname=hostname,
                                             date=dateString,
                                             time=timeString)
os.symlink(baseDir, os.path.join(ednaProcDirectory, linkName))

ednaLogName = "EDNAproc_{0}-{1}.log".format(dateString, timeString)
EDVerbose.setLogFileName(os.path.join(ednaProcDirectory, ednaLogName))
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

template = string.Template(scriptTemplate)
script = template.substitute(beamline=beamline,
                             proposal=proposal,
                             ednaProcDirectory=ednaProcPath,
                             dataCollectionId=options["-datacollectionID"],
                             inputFile=ednaInputFilePath)

# we also need some kind of script to run edna-plugin-launcher
ednaScriptFileName = "EDNAproc_launcher.sh"
ednaScriptFilePath = os.path.join(ednaProcPath, ednaScriptFileName)
if os.path.exists(ednaScriptFilePath):
    # Create unique file name
    ednaScriptFile = tempfile.NamedTemporaryFile(suffix=".sh",
                                                 prefix="EDNAproc_launcher-",
                                                 dir=ednaProcPath,
                                                 delete=False)
    ednaScriptFilePath = os.path.join(ednaProcPath, ednaScriptFile.name)
    ednaScriptFile.file.write(script)
    ednaScriptFile.close()
else:
    open(ednaScriptFilePath, "w").write(script)
os.chmod(ednaScriptFilePath, 0755)


submitSuccess = False
remainingBesHosts = BES_HOSTS

while not submitSuccess and len(remainingBesHosts) > 0:
    besHost = remainingBesHosts.pop()
    besPort = BES_PORT
    log.info("EDNAproc launcher: trying to submit job on {host}:{port}".format(host=besHost, port=besPort))
    try:
        conn = httplib.HTTPConnection(besHost, besPort)
        params = urllib.urlencode({"ednaDpLaunchPath":os.path.join(ednaProcPath, ednaScriptFilePath),
                                   "beamline": beamline,
                                   "proposal": proposal,
                                   "initiator": beamline,
                                   "externalRef": proposal,
                                   "reuseCase": "true" })
        conn.request("POST",
                     "/BES/bridge/rest/processes/EDNA_dp/RUN?%s" % params,
                     headers={"Accept":"text/plain"})
        response = conn.getresponse()
        if response.status != 200:
            log.error("RUN response status = {0}".format(response.status))
        else:
            submitSuccess = True
            log.info("EDNAproc launcher: job successfully submitted on {host}:{port}".format(host=besHost, port=besPort))
    except:
        log.error("EDNAproc launcher: cannot connect to BES server on {host}:{port}!".format(host=besHost, port=besPort))

