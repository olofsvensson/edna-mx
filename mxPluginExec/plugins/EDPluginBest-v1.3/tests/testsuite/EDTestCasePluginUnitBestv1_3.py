#
#    Project: mxPluginExec
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Marie-Francoise Incardona (incardon@esrf.fr)
#                            Olof Svensson (svensson@esrf.fr) 
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


__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120712"
__status__ = "production"

import os


from EDUtilsPath                         import EDUtilsPath
from EDAssert                            import EDAssert
from EDUtilsFile                         import EDUtilsFile
from EDTestCasePluginUnit                import EDTestCasePluginUnit
from EDUtilsTest                         import EDUtilsTest
from EDUtilsPath                         import EDUtilsPath
from EDConfiguration                     import EDConfiguration

from XSDataCommon import XSDataString

from XSDataBestv1_3 import XSDataInputBest
from XSDataBestv1_3 import XSDataResultBest

class EDTestCasePluginUnitBestv1_3(EDTestCasePluginUnit):

    def __init__(self, _pyStrTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginBestv1_3")
        self.strDataPath = self.getPluginTestsDataHome()

        self.obtainedInputFile = "XSDataInputBest_test.xml"
        self.referenceInputFile = os.path.join(self.strDataPath, "XSDataInputBest_reference.xml")
        self.referenceResultFile = os.path.join(self.strDataPath, "XSDataResultBest_reference.xml")

        self.referenceScriptLogFileName = os.path.join(self.strDataPath, "EDPluginBestv1_3.log")


    def testConfigureOK(self):
        edPluginBest = self.createPlugin()
        edConfigurationGood01 = EDConfiguration(os.path.join(self.strDataPath, "XSConfiguration.xml"))
        dictItemGood01 = edConfigurationGood01.get(self.getPluginName())
        edPluginBest.setConfig(dictItemGood01, _bLocal = True)
        edPluginBest.setScriptExecutable("cat")
        edPluginBest.configure()
        EDAssert.equal("/bin/bash", edPluginBest.getScriptShell())
        EDAssert.equal("cat", edPluginBest.getScriptExecutable())
        EDAssert.equal("/opt/pxsoft/ccp4-6.0.2/include/ccp4.setup-bash.orig", edPluginBest.getSetupCCP4())
        EDAssert.equal("Version of Best to be tested", edPluginBest.getStringVersion())
        EDAssert.equal(600, edPluginBest.getTimeOut())
        EDAssert.equal("/home/sweet/home", edPluginBest.getBestHome())
        EDAssert.equal("export besthome=/home/sweet/home", edPluginBest.getCommandBestHome())
        self.cleanUp(edPluginBest)


    def testSetDataModelInput(self):
        edPluginBest = self.createPlugin()
        edConfigurationGood01 = EDConfiguration(os.path.join(self.strDataPath, "XSConfiguration.xml"))
        dictItemGood01 = edConfigurationGood01.get(self.getPluginName())
        edPluginBest.setConfig(dictItemGood01, _bLocal = True)
        edPluginBest.setScriptExecutable("cat")
        edPluginBest.configure()

        from XSDataBestv1_3 import XSDataInputBest
        xsDataInputBest = XSDataInputBest()

        from XSDataCommon import XSDataAbsorbedDoseRate
        from XSDataCommon import XSDataDouble
        from XSDataCommon import XSDataString
        from XSDataCommon import XSDataTime
        from XSDataCommon import XSDataFile
        from XSDataCommon import XSDataAngularSpeed
        from XSDataCommon import XSDataString
        from XSDataCommon import XSDataAngle
        from XSDataCommon import XSDataBoolean

        xsDataInputBest.setCrystalAbsorbedDoseRate(XSDataAbsorbedDoseRate(0.22E+06))
        xsDataInputBest.setCrystalShape(XSDataDouble(1))
        xsDataInputBest.setCrystalSusceptibility(XSDataDouble(1.5))
        xsDataInputBest.setDetectorType(XSDataString("q210-2x"))
        xsDataInputBest.setBeamExposureTime(XSDataTime(1))
        xsDataInputBest.setBeamMaxExposureTime(XSDataTime(10000))
        xsDataInputBest.setBeamMinExposureTime(XSDataTime(0.1))
        xsDataInputBest.setGoniostatMinRotationWidth(XSDataAngle(0.1))
        xsDataInputBest.setGoniostatMaxRotationSpeed(XSDataAngularSpeed(10))
        xsDataInputBest.setAimedResolution(XSDataDouble(2))
        xsDataInputBest.setAimedRedundancy(XSDataDouble(6.5))
        xsDataInputBest.setAimedCompleteness(XSDataDouble(0.9))
        xsDataInputBest.setAimedIOverSigma(XSDataDouble(3))
        xsDataInputBest.setComplexity(XSDataString("min"))
        xsDataInputBest.setAnomalousData(XSDataBoolean(False))
        fileDirectory = edPluginBest.getWorkingDirectory()

        bestFileContentDat = EDUtilsFile.readFile(os.path.join(self.strDataPath, "bestfile.dat"))
        xsDataInputBest.setBestFileContentDat(XSDataString(bestFileContentDat))

        bestFileContentPar = EDUtilsFile.readFile(os.path.join(self.strDataPath, "bestfile.par"))
        xsDataInputBest.setBestFileContentPar(XSDataString(bestFileContentPar))

        bestFileContentHKL = EDUtilsFile.readFile(os.path.join(self.strDataPath, "bestfile1.hkl"))
        xsDataInputBest.addBestFileContentHKL(XSDataString(bestFileContentHKL))

        xsDataInputBest.exportToFile(self.obtainedInputFile)

        pyStrExpectedInput = self.readAndParseFile (self.referenceInputFile)
        pyStrObtainedInput = self.readAndParseFile (self.obtainedInputFile)

        xsDataInputExpected = XSDataInputBest.parseString(pyStrExpectedInput)
        xsDataInputObtained = XSDataInputBest.parseString(pyStrObtainedInput)

        EDAssert.equal(xsDataInputExpected.marshal(), xsDataInputObtained.marshal())
        EDUtilsFile.deleteFile(self.obtainedInputFile)

        self.cleanUp(edPluginBest)


    def testGenerateExecutiveSummary(self):
        pyStrInputBest = self.readAndParseFile (self.referenceInputFile)
        pyStrResultBest = self.readAndParseFile (self.referenceResultFile)

        from XSDataBestv1_3 import XSDataInputBest
        from XSDataBestv1_3 import XSDataResultBest

        xsDataInputBest = XSDataInputBest.parseString(pyStrInputBest)
        xsDataResultBest = XSDataResultBest.parseString(pyStrResultBest)
        edPluginBest = self.createPlugin()
        edPluginBest.setDataInput(xsDataInputBest)
        edPluginBest.setDataOutput(xsDataResultBest)
        edPluginBest.generateExecutiveSummary(edPluginBest)


    def testGetXSDataResultBest1(self):
        edPluginBest = self.createPlugin()
        xsDataInputBest = XSDataInputBest()
        edPluginBest.dataInput = xsDataInputBest
        # Test 1
        xsDataResultBest = edPluginBest.getXSDataResultBest(os.path.join(self.strDataPath, "unit_test_1_best.log"))
        xsDataResultBestReference = XSDataResultBest.parseFile(os.path.join(self.strDataPath, "XSDataResultBest_unit_test_1.xml"))
        print xsDataResultBest.marshal()
        EDAssert.equal(xsDataResultBestReference.collectionPlan[0].marshal(), 
                       xsDataResultBest.collectionPlan[0].marshal(), "Collection plan")

    def testGetXSDataResultBest2(self):
        edPluginBest = self.createPlugin()
        xsDataInputBest = XSDataInputBest()
        edPluginBest.dataInput = xsDataInputBest
        # Test 1
        xsDataResultBest = edPluginBest.getXSDataResultBest(os.path.join(self.strDataPath, "unit_test_2_best.log"))
        xsDataResultBestReference = XSDataResultBest.parseFile(os.path.join(self.strDataPath, "XSDataResultBest_unit_test_2.xml"))
#        print xsDataResultBest.marshal()
        for index in range(len(xsDataResultBestReference.collectionPlan)):
            try:
                EDAssert.equal(xsDataResultBestReference.collectionPlan[index].marshal(), 
                           xsDataResultBest.collectionPlan[index].marshal(), "Collection plan {0}".format(index))
            except:
                pass

    def testGetXSDataResultBest3(self):
        edPluginBest = self.createPlugin()
        xsDataInputBest = XSDataInputBest()
        edPluginBest.dataInput = xsDataInputBest
        # Test 1
        xsDataResultBest = edPluginBest.getXSDataResultBest(os.path.join(self.strDataPath, "unit_test_3_best.log"))
        xsDataResultBestReference = XSDataResultBest.parseFile(os.path.join(self.strDataPath, "XSDataResultBest_unit_test_3.xml"))
#        print xsDataResultBest.marshal()
        EDAssert.equal(xsDataResultBestReference.collectionPlan[0].marshal(), 
                       xsDataResultBest.collectionPlan[0].marshal(), "Collection plan")

    def testGetXSDataResultBest4(self):
        edPluginBest = self.createPlugin()
        xsDataInputBest = XSDataInputBest()
        edPluginBest.dataInput = xsDataInputBest
        # Test 1
        xsDataResultBest = edPluginBest.getXSDataResultBest(os.path.join(self.strDataPath, "unit_test_4_best.log"))
        xsDataResultBestReference = XSDataResultBest.parseFile(os.path.join(self.strDataPath, "XSDataResultBest_unit_test_4.xml"))
        print xsDataResultBest.marshal()
        EDAssert.equal(xsDataResultBestReference.collectionPlan[0].marshal(), 
                       xsDataResultBest.collectionPlan[0].marshal(), "Collection plan")

    def testGetXSDataResultBest5(self):
        edPluginBest = self.createPlugin()
        xsDataInputBest = XSDataInputBest()
        xsDataInputBest.strategyOption = XSDataString("-Bonly")
        edPluginBest.dataInput = xsDataInputBest
        # Test 1
        xsDataResultBest = edPluginBest.getXSDataResultBest(os.path.join(self.strDataPath, "unit_test_5_best.log"))
        xsDataResultBestReference = XSDataResultBest.parseFile(os.path.join(self.strDataPath, "XSDataResultBest_unit_test_5.xml"))
        print xsDataResultBest.marshal()
        EDAssert.equal(xsDataResultBestReference.collectionPlan[0].marshal(), 
                       xsDataResultBest.collectionPlan[0].marshal(), "Collection plan")

    def process(self):
#        self.addTestMethod(self.testConfigureOK)
#        self.addTestMethod(self.testSetDataModelInput)
        #self.addTestMethod(self.testGenerateExecutiveSummary)
#        self.addTestMethod(self.testGetXSDataResultBest4)
        self.addTestMethod(self.testGetXSDataResultBest5)


if __name__ == '__main__':

    edTestCasePluginUnitBestv1_3 = EDTestCasePluginUnitBestv1_3("EDTestCasePluginUnitBestv1_3")
    edTestCasePluginUnitBestv1_3.execute()

