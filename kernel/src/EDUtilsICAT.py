# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2023 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Olof Svensson (svensson@esrf.fr)
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

__authors__ = ["Olof Svensson"]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20230906"

import os
import pprint
import shutil
import pathlib

from pyicat_plus.client.main import IcatClient

from EDVerbose import EDVerbose

class EDUtilsICAT:
    """
    This is a static utility class for ICAT.
    """

    @classmethod
    def uploadToICAT(
        self,
        processName,
        xsDataInputStoreAutoProc,
        directory,
        icatProcessDataDir,
        isAnom,
        beamline,
        proposal,
        timeStart,
        timeEnd,
        isStaraniso=False,
    ):
        if directory.endswith("/"):
            directory = directory[:-1]
        if icatProcessDataDir.endswith("/"):
            icatProcessDataDir = icatProcessDataDir[:-1]

        if isAnom:
            anomString = "anom"
        else:
            anomString = "noanom"
        if isStaraniso:
            staranisoString = "_staraniso"
        else:
            staranisoString = ""
        dataset_name = f"{processName}_{anomString}{staranisoString}"
        icat_dir = os.path.join(icatProcessDataDir, dataset_name)
        os.makedirs(icat_dir, mode=0o755, exist_ok=False)
        # Attached files
        autoProcContainer = xsDataInputStoreAutoProc.AutoProcContainer
        autoProcProgramContainer = autoProcContainer.AutoProcProgramContainer
        for (
            autoProcProgramAttachment
        ) in autoProcProgramContainer.AutoProcProgramAttachment:
            file_path = autoProcProgramAttachment.filePath
            file_name = autoProcProgramAttachment.fileName
            shutil.copy(os.path.join(file_path, file_name), icat_dir)
        # Meta-data
        metadata = {}
        autoProc = autoProcContainer.AutoProc
        autoProcScalingContainer = autoProcContainer.AutoProcScalingContainer
        autoProcIntegrationContainer = (
            autoProcScalingContainer.AutoProcIntegrationContainer
        )
        autoProcIntegration = autoProcIntegrationContainer.AutoProcIntegration
        metadata["MXAutoprocIntegration_space_group"] = autoProc.spaceGroup
        if autoProc.refinedCell_a is not None:
            metadata["MXAutoprocIntegration_cell_a"] = autoProc.refinedCell_a
            metadata["MXAutoprocIntegration_cell_b"] = autoProc.refinedCell_b
            metadata["MXAutoprocIntegration_cell_c"] = autoProc.refinedCell_c
            metadata["MXAutoprocIntegration_cell_alpha"] = autoProc.refinedCell_alpha
            metadata["MXAutoprocIntegration_cell_beta"] = autoProc.refinedCell_beta
            metadata["MXAutoprocIntegration_cell_gamma"] = autoProc.refinedCell_gamma
        else:
            metadata["MXAutoprocIntegration_cell_a"] = autoProcIntegration.cell_a
            metadata["MXAutoprocIntegration_cell_b"] = autoProcIntegration.cell_b
            metadata["MXAutoprocIntegration_cell_c"] = autoProcIntegration.cell_c
            metadata["MXAutoprocIntegration_cell_alpha"] = autoProcIntegration.cell_alpha
            metadata["MXAutoprocIntegration_cell_beta"] = autoProcIntegration.cell_beta
            metadata["MXAutoprocIntegration_cell_gamma"] = autoProcIntegration.cell_gamma

        if autoProcIntegration.anomalous:
            metadata["MXAutoprocIntegration_anomalous"] = 1
        else:
            metadata["MXAutoprocIntegration_anomalous"] = 0
        for (
            autoProcScalingStatistics
        ) in autoProcScalingContainer.AutoProcScalingStatistics:
            statistics_type = autoProcScalingStatistics.scalingStatisticsType
            icat_stat_name = statistics_type.replace("Shell", "")
            metadata[
                f"MXAutoprocIntegrationScaling_{icat_stat_name}_completeness"
            ] = autoProcScalingStatistics.completeness
            metadata[
                f"MXAutoprocIntegrationScaling_{icat_stat_name}_resolution_limit_low"
            ] = autoProcScalingStatistics.resolutionLimitLow
            metadata[
                f"MXAutoprocIntegrationScaling_{icat_stat_name}_resolution_limit_high"
            ] = autoProcScalingStatistics.resolutionLimitHigh
            metadata[
                f"MXAutoprocIntegrationScaling_{icat_stat_name}_r_merge"
            ] = autoProcScalingStatistics.rMerge
            metadata[
                f"MXAutoprocIntegrationScaling_{icat_stat_name}_mean_I_over_sigI"
            ] = autoProcScalingStatistics.meanIOverSigI
            metadata[
                f"MXAutoprocIntegrationScaling_{icat_stat_name}_cc_half"
            ] = autoProcScalingStatistics.ccHalf
            metadata[
                f"MXAutoprocIntegrationScaling_{icat_stat_name}_cc_ano"
            ] = autoProcScalingStatistics.ccAno

        # ICAT settings
        icat_beamline = EDUtilsICAT.getIcatBeamline(beamline)
        if icat_beamline is not None:
            if icat_beamline == "ID30A-2":
                metadata_urls = ["bcu-mq-04.esrf.fr:61613"]
            else:
                metadata_urls = ["bcu-mq-01.esrf.fr:61613", "bcu-mq-02.esrf.fr:61613"]
            EDVerbose.screen(metadata_urls)
            if len(metadata_urls) > 0:
                client = IcatClient(metadata_urls=metadata_urls)
                metadata["Sample_name"] = dataset_name
                metadata["scanType"] = "integration"
                metadata["Process_program"] = processName + staranisoString
                raw = [str(pathlib.Path(directory))]
                EDVerbose.screen("Before store")
                EDVerbose.screen(f"icat_beamline {icat_beamline}")
                EDVerbose.screen(f"proposal {proposal}")
                EDVerbose.screen(f"dataset_name {dataset_name}")
                EDVerbose.screen(f"icat_dir {icat_dir}")
                EDVerbose.screen(f"metadata {pprint.pformat(metadata)}")
                EDVerbose.screen(f"raw {raw}")
                client.store_processed_data(
                    beamline=icat_beamline,
                    proposal=proposal,
                    dataset=dataset_name,
                    path=str(icat_dir),
                    metadata=metadata,
                    raw=raw,
                )
                EDVerbose.screen("After store")

    @classmethod
    def getIcatBeamline(cls, beamline):
        dict_beamline = {
            "id23eh1": "ID23-1",
            "id23eh2": "ID23-2",
            "id30a1": "ID30A-1",
            "id30a2": "ID30A-2",
            "id30a3": "ID30A-3",
            "id30b": "ID30b",
            "bm07": "BM07",
        }
        icat_beamline = dict_beamline.get(beamline, None)
        return icat_beamline
