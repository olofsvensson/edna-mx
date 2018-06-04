#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2016 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr)
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


__authors__ = ["Marie-Francoise Incardona", "Olof Svensson"]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os

from EDPluginControlIndexingv10 import EDPluginControlIndexingv10

from XSDataCommon import XSDataBoolean

class EDPluginControlIndexingLabelitv10(EDPluginControlIndexingv10):
    """
    This plugin is derived from EDPluginControlIndexingv10, and implements
    only the specific parts needed for executing the Labelit execution plugin.
    """

    def __init__ (self):
        EDPluginControlIndexingv10.__init__(self)
        self.setPluginIndexingName("EDPluginLabelitIndexingv1_1")
        self.setPluginIndexingExecutiveSummaryName("Labelit")
        self.setGeneratePredictionImage(True)
        self.__listXSDataImageReference = None

    def loadPluginIndexingInputData(self):
        self.verboseDebug("EDPluginControlIndexingLabelitv10.loadPluginIndexingInputData...")
        xsDataIndexingInput = self.getDataInput()
        from EDHandlerXSDataPhenixv1_1 import EDHandlerXSDataPhenixv1_1
        self.getPluginIndexing().dataInput = EDHandlerXSDataPhenixv1_1.generateXSDataInputLabelitIndexing(xsDataIndexingInput)


    def getDataIndexingResult(self, _edPlugin):
        """
        This method retrieves the indexing results from a MOSFLM indexing plugin.
        """
        self.DEBUG("EDPluginControlIndexingLabelitv10.getDataIndexingResultFromMOSFLM")
        xsDataResultLabelitIndexing = _edPlugin.dataOutput
        from EDHandlerXSDataPhenixv1_1 import EDHandlerXSDataPhenixv1_1
        xsDataIndexingResult = EDHandlerXSDataPhenixv1_1.generateXSDataIndexingResult(xsDataResultLabelitIndexing,
                                                                                       self.getExperimentalCondition())
        xsDataIndexingResult.setLabelitIndexing(XSDataBoolean(True))
        return xsDataIndexingResult
