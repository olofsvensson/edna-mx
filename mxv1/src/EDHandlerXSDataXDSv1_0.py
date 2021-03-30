#
#    Project: The EDNA Prototype
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008 EMBL-Grenoble, Grenoble, France
#
#    Principal authors: Sandor Brockhauser (brockhauser@embl-grenoble.fr)
#                       Pierre Legrand (pierre.legrand@synchrotron-soleil.fr)
#
#    Contributors:      Olof Svensson (svensson@esrf.fr)


__authors__ = [ "Sandor Brockhauser", "Olof Svensson", "Pierre Legrand" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


from EDUtilsImage import EDUtilsImage
from EDUtilsPath import EDUtilsPath
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsFile import EDUtilsFile
from EDUtilsSymmetry import EDUtilsSymmetry

from XSDataCommon import XSDataLength
from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataWavelength
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataVectorDouble

from XSDataMXv1 import XSDataCell
from XSDataMXv1 import XSDataCrystal
from XSDataMXv1 import XSDataSpaceGroup
from XSDataMXv1 import XSDataDetector
from XSDataMXv1 import XSDataIndexingResult
from XSDataMXv1 import XSDataResultControlXDSGenerateBackgroundImage
from XSDataMXv1 import XSDataIndexingSolutionSelected
from XSDataMXv1 import XSDataStatisticsIndexing
from XSDataMXv1 import XSDataExperimentalCondition
from XSDataMXv1 import XSDataOrientation

EDFactoryPluginStatic.loadModule("XSDataXDSv1_0")
from XSDataXDSv1_0 import XSDataInputXDSIndexing
from XSDataXDSv1_0 import XSDataInputXDSIntegration
from XSDataXDSv1_0 import XSDataInputXDSGenerateBackgroundImage
from XSDataXDSv1_0 import XSDataXDSDetector
from XSDataXDSv1_0 import XSDataVectorDouble
from XSDataXDSv1_0 import XSDataXDSBeam
from XSDataXDSv1_0 import XSDataXDSImage
from XSDataXDSv1_0 import XSDataXDSGoniostat
from XSDataXDSv1_0 import XSDataXDSIntegerRange
from XSDataXDSv1_0 import XSDataXDSDoubleRange
from XSDataXDSv1_0 import XSDataXDSCrystal
from XSDataXDSv1_0 import XSDataXDSImageLink
from XSDataXDSv1_0 import XSDataXDSRectangle



class EDHandlerXSDataXDSv1_0:


    @staticmethod
    def generateXSDataInputXDS(_xsDataInputXDS, _xsDataCollection):

        xsDataCollection = _xsDataCollection
        xsDataExperimentalCondition = _xsDataCollection.getSubWedge()[0].getExperimentalCondition()
        xsDataSubWedgeList = xsDataCollection.getSubWedge()

        xsDataBeam = xsDataExperimentalCondition.getBeam()
        xsDataDetector = xsDataExperimentalCondition.getDetector()
        xsDataGoniostat = xsDataExperimentalCondition.getGoniostat()

        dWavelength = xsDataBeam.getWavelength().getValue()
        dDistance = xsDataDetector.getDistance().getValue()
        dBeamPositionX = xsDataDetector.getBeamPositionX().getValue()
        dBeamPositionY = xsDataDetector.getBeamPositionY().getValue()

        # Start with the detector

        xsDataXDSDetector = EDHandlerXSDataXDSv1_0.getXSDataXDSDetector(xsDataDetector)
        _xsDataInputXDS.setDetector(xsDataXDSDetector)

        # Then the beam

        xsDataXDSBeam = XSDataXDSBeam()

        xsDataVectorDoubleIncidentBeam = XSDataVectorDouble()
        xsDataVectorDoubleIncidentBeam.setV1(0.0)
        xsDataVectorDoubleIncidentBeam.setV2(0.0)
        xsDataVectorDoubleIncidentBeam.setV3(1.0)
        xsDataXDSBeam.setIncident_beam_direction(xsDataVectorDoubleIncidentBeam)

        xsDataVectorDoublePolarizationPlaneNormal = XSDataVectorDouble()
        xsDataVectorDoublePolarizationPlaneNormal.setV1(0.0)
        xsDataVectorDoublePolarizationPlaneNormal.setV2(1.0)
        xsDataVectorDoublePolarizationPlaneNormal.setV3(0.0)
        xsDataXDSBeam.setPolarization_plane_normal(xsDataVectorDoublePolarizationPlaneNormal)

        xsDataXDSBeam.setX_ray_wavelength(XSDataWavelength(dWavelength))

        _xsDataInputXDS.setBeam(xsDataXDSBeam)

        # Then the goniostat

        xsDataXDSGoniostat = XSDataXDSGoniostat()

        xsDataVectorDoubleRotationAxis = XSDataVectorDouble()
        xsDataVectorDoubleRotationAxis.setV1(1.0)
        xsDataVectorDoubleRotationAxis.setV2(0.0)
        xsDataVectorDoubleRotationAxis.setV3(0.0)
        xsDataXDSGoniostat.setRotation_axis(xsDataVectorDoubleRotationAxis)

        xsDataXDSGoniostat.setOscillation_range(xsDataGoniostat.getOscillationWidth())

        xsDataXDSGoniostat.setStarting_angle(xsDataGoniostat.getRotationAxisStart())

        _xsDataInputXDS.setGoniostat(xsDataXDSGoniostat)

        # Then the Crystal

        xsDataXDSCrystal = XSDataXDSCrystal()

        xsDataXDSCrystal.setFriedels_law(XSDataString("FALSE"))
#
# #        if ( xsDataCrystal is not None ):
# #            xsDataSpaceGroup = xsDataCrystal.getSpaceGroup()
# #            if ( xsDataSpaceGroup is not None ):
# #                xsDataStringName = xsDataSpaceGroup.getName()
# #                if ( xsDataStringName is not None ):
# #                    xsDataInputXDS.setSymmetry( XSDataString( xsDataStringName.getValue() ) )
#        xsDataXDSCrystal.setSpace_group_number(XSDataInteger(0))
#
#        xsDataXDSCrystal.setStrong_pixel(XSDataInteger(8))
#
#        xsDataCell = XSDataCell()
#        xsDataCell.setLength_a(XSDataLength(0.0))
#        xsDataCell.setLength_b(XSDataLength(0.0))
#        xsDataCell.setLength_c(XSDataLength(0.0))
#        xsDataCell.setAngle_alpha(XSDataAngle(0.0))
#        xsDataCell.setAngle_beta(XSDataAngle(0.0))
#        xsDataCell.setAngle_gamma(XSDataAngle(0.0))
#        xsDataXDSCrystal.setUnit_cell_constants(xsDataCell)
#
        xsDataXDSCrystal.minimum_number_of_pixels_in_a_spot = XSDataInteger(2)

        _xsDataInputXDS.setCrystal(xsDataXDSCrystal)

        # Finaly the images

        xsDataXDSImage = XSDataXDSImage()

        xsDataSubWedgeFirst = xsDataSubWedgeList[0]
        xsDataImageFirst = xsDataSubWedgeFirst.getImage()[0]
        pyStrPath = xsDataImageFirst.getPath().getValue()
        pyStrFileName = EDUtilsFile.getBaseName(pyStrPath)
        pyStrDirectory = EDUtilsPath.getFolderName(pyStrPath)

        pyStrPrefix = EDUtilsImage.getPrefix(pyStrFileName)
        pyStrSuffix = EDUtilsImage.getSuffix(pyStrFileName)
        pyStrXDSTemplate = "%s_xdslink_?????.%s" % (pyStrPrefix, pyStrSuffix)

        xsDataXDSImage.setName_template_of_data_frames(XSDataString(pyStrXDSTemplate))

        iXDSLowestImageNumberGlobal = 1
        xsDataXDSImage.setStarting_frame(XSDataInteger(iXDSLowestImageNumberGlobal))

        # First we have to find the smallest goniostat rotation axis start:
        fGonioStatOscillationStartMin = None
        for xsDataSubWedge in xsDataSubWedgeList:
            xsDataGoniostat = xsDataSubWedge.getExperimentalCondition().getGoniostat()
            fGonioStatOscillationStart = xsDataGoniostat.getRotationAxisStart().getValue()
            if (fGonioStatOscillationStartMin is None):
                fGonioStatOscillationStartMin = fGonioStatOscillationStart
            elif (fGonioStatOscillationStartMin > fGonioStatOscillationStart):
                fGonioStatOscillationStartMin = fGonioStatOscillationStart

        # Loop through the list of sub wedges

        for xsDataSubWedge in xsDataSubWedgeList:

            xsDataImageList = xsDataSubWedge.getImage()
            xsDataGoniostat = xsDataSubWedge.getExperimentalCondition().getGoniostat()
            fGonioStatOscillationStart = xsDataGoniostat.getRotationAxisStart().getValue()
            fGonioStatOscillationRange = xsDataGoniostat.getOscillationWidth().getValue()

            # First find the lowest and highest image numbers
            iLowestImageNumber = None
            for xsDataImage in xsDataImageList:
                iImageNumber = xsDataImage.getNumber().getValue()
                if (iLowestImageNumber is None):
                    iLowestImageNumber = iImageNumber
                elif (iImageNumber < iLowestImageNumber):
                    iLowestImageNumber = iImageNumber

            # Loop through the list of images
            iLowestXDSImageNumber = None
            iHighestXDSImageNumber = None
            for xsDataImage in xsDataImageList:
                iImageNumber = xsDataImage.getNumber().getValue()
                fImageOscillationStart = fGonioStatOscillationStart + (iImageNumber - iLowestImageNumber) * fGonioStatOscillationRange
                iXDSImageNumber = iXDSLowestImageNumberGlobal + int((fImageOscillationStart - fGonioStatOscillationStartMin) / fGonioStatOscillationRange)
                # print iXDSImageNumber, fImageOscillationStart, fGonioStatOscillationStartMin, fGonioStatOscillationRange
                pyStrSourcePath = xsDataImage.getPath()
                pyStrTarget = "%s_xdslink_%05d.%s" % (pyStrPrefix, iXDSImageNumber, pyStrSuffix)
                xsDataXDSImageLink = XSDataXDSImageLink()
                xsDataFileSource = XSDataFile()
                xsDataFileSource.setPath(pyStrSourcePath)
                xsDataXDSImageLink.setSource(xsDataFileSource)
                xsDataXDSImageLink.setTarget(XSDataString(pyStrTarget))
                _xsDataInputXDS.addImage_link(xsDataXDSImageLink)
                if (iLowestXDSImageNumber is None):
                    iLowestXDSImageNumber = iXDSImageNumber
                elif (iLowestXDSImageNumber > iXDSImageNumber):
                    iLowestXDSImageNumber = iXDSImageNumber
                if (iHighestXDSImageNumber is None):
                    iHighestXDSImageNumber = iXDSImageNumber
                elif (iHighestXDSImageNumber < iXDSImageNumber):
                    iHighestXDSImageNumber = iXDSImageNumber
            xsDataXDSIntegerRange = XSDataXDSIntegerRange()
            xsDataXDSIntegerRange.setLower(XSDataInteger(iLowestXDSImageNumber))
            xsDataXDSIntegerRange.setUpper(XSDataInteger(iHighestXDSImageNumber))

            xsDataXDSImage.addBackground_range(xsDataXDSIntegerRange)
            xsDataXDSImage.addData_range(xsDataXDSIntegerRange)
            xsDataXDSImage.addSpot_range(xsDataXDSIntegerRange)

        _xsDataInputXDS.setImage(xsDataXDSImage)

        return _xsDataInputXDS


    @staticmethod
    def generateXSDataResultXDSGenerateBackgroundImage(_xsDataResultXDSGeneratePredictionImage):
        xsDataResultControlXDSGenerateBackgroundImage = XSDataResultControlXDSGenerateBackgroundImage()
        xsDataResultControlXDSGenerateBackgroundImage.setXdsBackgroundImage(_xsDataResultXDSGeneratePredictionImage.getXdsBackgroundImage())
        return xsDataResultControlXDSGenerateBackgroundImage




    @staticmethod
    def getXSDataXDSDetector(_xsDataDetector):
        EDFactoryPluginStatic.loadModule("XSDataXDSv1_0")
        from XSDataXDSv1_0 import XSDataXDSDetector
        from XSDataXDSv1_0 import XSDataXDSIntegerRange
        xsDataXDSDetector = XSDataXDSDetector()
        strDetectorType = _xsDataDetector.getType().getValue()
        if ((strDetectorType == "q4")      or \
             (strDetectorType == "q4-2x")   or \
             (strDetectorType == "q210")    or \
             (strDetectorType == "q210-2x") or \
             (strDetectorType == "q315")    or \
             (strDetectorType == "q315-2x")):
            xsDataXDSDetector.setDetector_name(XSDataString("ADSC"))
            xsDataXDSDetector.setMinimum_valid_pixel_value(XSDataInteger(1))
            xsDataXDSDetector.setOverload(XSDataInteger(65535))

            xsDataXDSIntegerRangeTrustedPixel = XSDataXDSIntegerRange()
            xsDataXDSIntegerRangeTrustedPixel.setLower(XSDataInteger(6000))
            xsDataXDSIntegerRangeTrustedPixel.setUpper(XSDataInteger(30000))
            xsDataXDSDetector.setValue_range_for_trusted_detector_pixels(xsDataXDSIntegerRangeTrustedPixel)
#        elif ( strDetectorType == "mar165") or \
#               strDetectorType == "mar225") ):
#            xsDataXDSDetector.setType( XSDataString( "MARCCD" ) )
        elif strDetectorType == "pilatus6m":
            xsDataXDSDetector.setDetector_name(XSDataString("PILATUS"))
            listUntrustedRectangle = \
               [[ 487, 495, 0, 2528], \
                [ 981, 989, 0, 2528], \
                [1475, 1483, 0, 2528], \
                [1969, 1977, 0, 2528], \
                [   0, 2464, 195, 213], \
                [   0, 2464, 407, 425], \
                [   0, 2464, 619, 637], \
                [   0, 2464, 831, 849], \
                [   0, 2464, 1043, 1061], \
                [   0, 2464, 1255, 1273], \
                [   0, 2464, 1467, 1485], \
                [   0, 2464, 1679, 1697], \
                [   0, 2464, 1891, 1909], \
                [   0, 2464, 2103, 2121], \
                [   0, 2464, 2315, 2333]]
            for listRectangle in listUntrustedRectangle:
                xsDataXDSRectangle = XSDataXDSRectangle()
                xsDataXDSRectangle.setX1(XSDataInteger(listRectangle[0]))
                xsDataXDSRectangle.setX2(XSDataInteger(listRectangle[1]))
                xsDataXDSRectangle.setY1(XSDataInteger(listRectangle[2]))
                xsDataXDSRectangle.setY2(XSDataInteger(listRectangle[3]))
                xsDataXDSDetector.addUntrusted_rectangle(xsDataXDSRectangle)
            xsDataXDSDetector.setMinimum_valid_pixel_value(XSDataInteger(0))
            xsDataXDSDetector.setOverload(XSDataInteger(1048500))

            xsDataXDSIntegerRangeTrustedPixel = XSDataXDSIntegerRange()
            xsDataXDSIntegerRangeTrustedPixel.setLower(XSDataInteger(7000))
            xsDataXDSIntegerRangeTrustedPixel.setUpper(XSDataInteger(30000))
            xsDataXDSDetector.setValue_range_for_trusted_detector_pixels(xsDataXDSIntegerRangeTrustedPixel)

            xsDataXDSDoubleRangeTrustedRegion = XSDataXDSDoubleRange()
            xsDataXDSDoubleRangeTrustedRegion.setLower(XSDataDouble(0.0))
            xsDataXDSDoubleRangeTrustedRegion.setUpper(XSDataDouble(1.41))
            xsDataXDSDetector.setTrusted_region(xsDataXDSDoubleRangeTrustedRegion)

            xsDataXDSDetector.setSensor_thickness(XSDataDouble(0.32))
        elif strDetectorType == "pilatus2m":
            xsDataXDSDetector.setDetector_name(XSDataString("PILATUS"))
            listUntrustedRectangle = \
               [[ 487, 495, 0, 1680], \
                [ 981, 989, 0, 1680], \
                [   0, 1476, 195, 213], \
                [   0, 1476, 407, 425], \
                [   0, 1476, 619, 637], \
                [   0, 1476, 831, 849], \
                [   0, 1476, 1043, 1061], \
                [   0, 1476, 1255, 1273], \
                [   0, 1476, 1467, 1485]]
            for listRectangle in listUntrustedRectangle:
                xsDataXDSRectangle = XSDataXDSRectangle()
                xsDataXDSRectangle.setX1(XSDataInteger(listRectangle[0]))
                xsDataXDSRectangle.setX2(XSDataInteger(listRectangle[1]))
                xsDataXDSRectangle.setY1(XSDataInteger(listRectangle[2]))
                xsDataXDSRectangle.setY2(XSDataInteger(listRectangle[3]))
                xsDataXDSDetector.addUntrusted_rectangle(xsDataXDSRectangle)
            xsDataXDSDetector.setMinimum_valid_pixel_value(XSDataInteger(0))
            xsDataXDSDetector.setOverload(XSDataInteger(1048500))

            xsDataXDSIntegerRangeTrustedPixel = XSDataXDSIntegerRange()
            xsDataXDSIntegerRangeTrustedPixel.setLower(XSDataInteger(7000))
            xsDataXDSIntegerRangeTrustedPixel.setUpper(XSDataInteger(30000))
            xsDataXDSDetector.setValue_range_for_trusted_detector_pixels(xsDataXDSIntegerRangeTrustedPixel)

            xsDataXDSDoubleRangeTrustedRegion = XSDataXDSDoubleRange()
            xsDataXDSDoubleRangeTrustedRegion.setLower(XSDataDouble(0.0))
            xsDataXDSDoubleRangeTrustedRegion.setUpper(XSDataDouble(1.41))
            xsDataXDSDetector.setTrusted_region(xsDataXDSDoubleRangeTrustedRegion)

            xsDataXDSDetector.setSensor_thickness(XSDataDouble(0.32))
        elif strDetectorType == "eiger4m":
            xsDataXDSDetector.setDetector_name(XSDataString("PILATUS"))
            listUntrustedRectangle = \
               [[ 1029, 1040, 0, 2167], \
                [ 0, 2070, 512, 550], \
                [ 0, 2070, 1063, 1103], \
                [ 0, 2070, 1614, 1654],
                ]
            for listRectangle in listUntrustedRectangle:
                xsDataXDSRectangle = XSDataXDSRectangle()
                xsDataXDSRectangle.setX1(XSDataInteger(listRectangle[0]))
                xsDataXDSRectangle.setX2(XSDataInteger(listRectangle[1]))
                xsDataXDSRectangle.setY1(XSDataInteger(listRectangle[2]))
                xsDataXDSRectangle.setY2(XSDataInteger(listRectangle[3]))
                xsDataXDSDetector.addUntrusted_rectangle(xsDataXDSRectangle)
            xsDataXDSDetector.setMinimum_valid_pixel_value(XSDataInteger(0))
            xsDataXDSDetector.setOverload(XSDataInteger(1048500))

            xsDataXDSIntegerRangeTrustedPixel = XSDataXDSIntegerRange()
            xsDataXDSIntegerRangeTrustedPixel.setLower(XSDataInteger(7000))
            xsDataXDSIntegerRangeTrustedPixel.setUpper(XSDataInteger(30000))
            xsDataXDSDetector.setValue_range_for_trusted_detector_pixels(xsDataXDSIntegerRangeTrustedPixel)

            xsDataXDSDoubleRangeTrustedRegion = XSDataXDSDoubleRange()
            xsDataXDSDoubleRangeTrustedRegion.setLower(XSDataDouble(0.0))
            xsDataXDSDoubleRangeTrustedRegion.setUpper(XSDataDouble(1.41))
            xsDataXDSDetector.setTrusted_region(xsDataXDSDoubleRangeTrustedRegion)

            xsDataXDSDetector.setSensor_thickness(XSDataDouble(0.32))
        elif strDetectorType == "eiger9m":
            xsDataXDSDetector.setDetector_name(XSDataString("PILATUS"))
            listUntrustedRectangle = \
               [[ 1029, 1040, 0, 3269], \
                [ 2069, 2082, 0, 3269], \
                [ 0, 3110, 513, 553], \
                [ 0, 3110, 1064, 1104], \
                [ 0, 3110, 1615, 1655], \
                [ 0, 3110, 2166, 2206], \
                [ 0, 3110, 2717, 2757], \
                ]
            for listRectangle in listUntrustedRectangle:
                xsDataXDSRectangle = XSDataXDSRectangle()
                xsDataXDSRectangle.setX1(XSDataInteger(listRectangle[0]))
                xsDataXDSRectangle.setX2(XSDataInteger(listRectangle[1]))
                xsDataXDSRectangle.setY1(XSDataInteger(listRectangle[2]))
                xsDataXDSRectangle.setY2(XSDataInteger(listRectangle[3]))
                xsDataXDSDetector.addUntrusted_rectangle(xsDataXDSRectangle)
            xsDataXDSDetector.setMinimum_valid_pixel_value(XSDataInteger(0))
            xsDataXDSDetector.setOverload(XSDataInteger(1048500))

            xsDataXDSIntegerRangeTrustedPixel = XSDataXDSIntegerRange()
            xsDataXDSIntegerRangeTrustedPixel.setLower(XSDataInteger(7000))
            xsDataXDSIntegerRangeTrustedPixel.setUpper(XSDataInteger(30000))
            xsDataXDSDetector.setValue_range_for_trusted_detector_pixels(xsDataXDSIntegerRangeTrustedPixel)

            xsDataXDSDoubleRangeTrustedRegion = XSDataXDSDoubleRange()
            xsDataXDSDoubleRangeTrustedRegion.setLower(XSDataDouble(0.0))
            xsDataXDSDoubleRangeTrustedRegion.setUpper(XSDataDouble(1.41))
            xsDataXDSDetector.setTrusted_region(xsDataXDSDoubleRangeTrustedRegion)

            xsDataXDSDetector.setSensor_thickness(XSDataDouble(0.45))
        elif strDetectorType == "eiger16m":
            xsDataXDSDetector.setDetector_name(XSDataString("PILATUS"))
            # From https://www.psi.ch/sls/pxi/ComputingEN/XDS.INP.E16M.X06SA_2016.txt
            # !EXCLUSION OF HORIZONTAL DEAD AREAS OF THE EIGER 16M DETECTOR + ONE PIXEL ON EACH SIDE
            # UNTRUSTED_RECTANGLE=    0 4151    513  553
            # UNTRUSTED_RECTANGLE=    0 4151   1064 1104
            # UNTRUSTED_RECTANGLE=    0 4151   1615 1655
            # UNTRUSTED_RECTANGLE=    0 4151   2166 2206
            # UNTRUSTED_RECTANGLE=    0 4151   2717 2757
            # UNTRUSTED_RECTANGLE=    0 4151   3268 3308
            # UNTRUSTED_RECTANGLE=    0 4151   3819 3859
            # !EXCLUSION OF VERTICAL DEAD AREAS OF THE EIGER 16M DETECTOR + ONE PIXEL ON EACH SIDE
            # UNTRUSTED_RECTANGLE= 1029 1042      0 4372
            # UNTRUSTED_RECTANGLE= 2069 2082      0 4372
            # UNTRUSTED_RECTANGLE= 3109 3122      0 4372
            listUntrustedRectangle = \
                [
                    [    0, 4151, 513, 553],
                    [    0, 4151, 1064, 1104],
                    [    0, 4151, 1615, 1655],
                    [    0, 4151, 2166, 2206],
                    [    0, 4151, 2717, 2757],
                    [    0, 4151, 3268, 3308],
                    [    0, 4151, 3819, 3859],
                    [ 1029, 1042, 0, 4372],
                    [ 2069, 2082, 0, 4372],
                    [ 3109, 3122, 0, 4372],
                ]
            for listRectangle in listUntrustedRectangle:
                xsDataXDSRectangle = XSDataXDSRectangle()
                xsDataXDSRectangle.setX1(XSDataInteger(listRectangle[0]))
                xsDataXDSRectangle.setX2(XSDataInteger(listRectangle[1]))
                xsDataXDSRectangle.setY1(XSDataInteger(listRectangle[2]))
                xsDataXDSRectangle.setY2(XSDataInteger(listRectangle[3]))
                xsDataXDSDetector.addUntrusted_rectangle(xsDataXDSRectangle)
            xsDataXDSDetector.setMinimum_valid_pixel_value(XSDataInteger(0))
            xsDataXDSDetector.setOverload(XSDataInteger(1048500))

            xsDataXDSIntegerRangeTrustedPixel = XSDataXDSIntegerRange()
            xsDataXDSIntegerRangeTrustedPixel.setLower(XSDataInteger(4000))
            xsDataXDSIntegerRangeTrustedPixel.setUpper(XSDataInteger(30000))
            xsDataXDSDetector.setValue_range_for_trusted_detector_pixels(xsDataXDSIntegerRangeTrustedPixel)

            xsDataXDSDoubleRangeTrustedRegion = XSDataXDSDoubleRange()
            xsDataXDSDoubleRangeTrustedRegion.setLower(XSDataDouble(0.0))
            xsDataXDSDoubleRangeTrustedRegion.setUpper(XSDataDouble(1.21))
            xsDataXDSDetector.setTrusted_region(xsDataXDSDoubleRangeTrustedRegion)

            xsDataXDSDetector.setSensor_thickness(XSDataDouble(0.32))

        elif strDetectorType == "eiger2_16m":
            xsDataXDSDetector.setDetector_name(XSDataString("PILATUS"))

            listUntrustedRectangle = \
                [
                    [0, 4149, 512, 549],
                    [0, 4149, 1062, 1099],
                    [0, 4149, 1612, 1649],
                    [0, 4149, 2162, 2199],
                    [0, 4149, 2712, 2749],
                    [0, 4149, 3262, 3299],
                    [0, 4149, 3812, 3849],
                    [513, 514, 0, 4362],
                    [1028, 1039, 0, 4362],
                    [1553, 1554, 0, 4362],
                    [2068, 2079, 0, 4362],
                    [2593, 2594, 0, 4362],
                    [3108, 3119, 0, 4362],
                    [3633, 3634, 0, 4362]
                ]

            for listRectangle in listUntrustedRectangle:
                xsDataXDSRectangle = XSDataXDSRectangle()
                xsDataXDSRectangle.setX1(XSDataInteger(listRectangle[0]))
                xsDataXDSRectangle.setX2(XSDataInteger(listRectangle[1]))
                xsDataXDSRectangle.setY1(XSDataInteger(listRectangle[2]))
                xsDataXDSRectangle.setY2(XSDataInteger(listRectangle[3]))
                xsDataXDSDetector.addUntrusted_rectangle(xsDataXDSRectangle)

            xsDataXDSDetector.setMinimum_valid_pixel_value(XSDataInteger(0))
            xsDataXDSDetector.setOverload(XSDataInteger(1048500))

            xsDataXDSIntegerRangeTrustedPixel = XSDataXDSIntegerRange()
            xsDataXDSIntegerRangeTrustedPixel.setLower(XSDataInteger(4000))
            xsDataXDSIntegerRangeTrustedPixel.setUpper(XSDataInteger(30000))
            xsDataXDSDetector.setValue_range_for_trusted_detector_pixels(xsDataXDSIntegerRangeTrustedPixel)

            xsDataXDSDoubleRangeTrustedRegion = XSDataXDSDoubleRange()
            xsDataXDSDoubleRangeTrustedRegion.setLower(XSDataDouble(0.0))
            xsDataXDSDoubleRangeTrustedRegion.setUpper(XSDataDouble(1.21))
            xsDataXDSDetector.setTrusted_region(xsDataXDSDoubleRangeTrustedRegion)

            xsDataXDSDetector.setSensor_thickness(XSDataDouble(0.75))

        elif strDetectorType == "mar225":
            xsDataXDSDetector.setDetector_name(XSDataString("CCDCHESS"))
            xsDataXDSDetector.setMinimum_valid_pixel_value(XSDataInteger(0))
            xsDataXDSDetector.setOverload(XSDataInteger(65000))

            xsDataXDSIntegerRangeTrustedPixel = XSDataXDSIntegerRange()
            xsDataXDSIntegerRangeTrustedPixel.setLower(XSDataInteger(7000))
            xsDataXDSIntegerRangeTrustedPixel.setUpper(XSDataInteger(30000))
            xsDataXDSDetector.setValue_range_for_trusted_detector_pixels(xsDataXDSIntegerRangeTrustedPixel)

            xsDataXDSDoubleRangeTrustedRegion = XSDataXDSDoubleRange()
            xsDataXDSDoubleRangeTrustedRegion.setLower(XSDataDouble(0.0))
            xsDataXDSDoubleRangeTrustedRegion.setUpper(XSDataDouble(1.4))
            xsDataXDSDetector.setTrusted_region(xsDataXDSDoubleRangeTrustedRegion)
        else:
            # This is a temporary solution for the exception problem pointed out in bug #43.
            # Instead of raising an exception with a known type we send the error message as a string.
            pyStrErrorMessage = "EDHandlerXSDataXDSv1_0.getXSDataXDSDetector: Unknown detector type : " + strDetectorType
            raise BaseException(pyStrErrorMessage)

        xsDataXDSDetector.setNx(_xsDataDetector.getNumberPixelX())
        xsDataXDSDetector.setNy(_xsDataDetector.getNumberPixelY())
        xsDataXDSDetector.setQx(_xsDataDetector.getPixelSizeX())
        xsDataXDSDetector.setQy(_xsDataDetector.getPixelSizeY())
        xsDataXDSDetector.setDetector_distance(_xsDataDetector.getDistance())

        fOrgx = _xsDataDetector.getBeamPositionY().getValue() / _xsDataDetector.getPixelSizeY().getValue()
        fOrgy = _xsDataDetector.getBeamPositionX().getValue() / _xsDataDetector.getPixelSizeX().getValue()
        xsDataXDSDetector.setOrgx(XSDataDouble(fOrgx))
        xsDataXDSDetector.setOrgy(XSDataDouble(fOrgy))
        xsDataVectorDoubleXAxis = XSDataVectorDouble()

        xsDataVectorDoubleXAxis.setV1(1.0)
        xsDataVectorDoubleXAxis.setV2(0.0)
        xsDataVectorDoubleXAxis.setV3(0.0)
        xsDataXDSDetector.setDirection_of_detector_x_axis(xsDataVectorDoubleXAxis)

        xsDataVectorDoubleYAxis = XSDataVectorDouble()
        xsDataVectorDoubleYAxis.setV1(0.0)
        xsDataVectorDoubleYAxis.setV2(1.0)
        xsDataVectorDoubleYAxis.setV3(0.0)
        xsDataXDSDetector.setDirection_of_detector_y_axis(xsDataVectorDoubleYAxis)


        return xsDataXDSDetector


    @staticmethod
    def generateXSDataInputXDSIndexing(_xsDataIndexingInput):
        xsDataInputXDSIndexing = XSDataInputXDSIndexing()
        xsDataCollection = _xsDataIndexingInput.dataCollection
        xsDataInputXDSIndexing = EDHandlerXSDataXDSv1_0.generateXSDataInputXDS(xsDataInputXDSIndexing, xsDataCollection)
        return xsDataInputXDSIndexing

    @staticmethod
    def generateXSDataIndexingResult(_xsDataResultXDSIndexing, _xsDataExperimentalCondition=None):

        xsDataIndexingResult = XSDataIndexingResult()
        xsDataIndexingSolutionSelected = XSDataIndexingSolutionSelected()
        xsDataCrystalSelected = XSDataCrystal()
#        xsDataIndexingSolutionSelected.setNumber(XSDataInteger(iIndex))
#        xsDataCellSelected = xsDataLabelitSolution.getUnitCell()
        spaceGroupName = EDUtilsSymmetry.getMinimumSymmetrySpaceGroupFromBravaisLattice(_xsDataResultXDSIndexing.bravaisLattice.value)
        xsDataCrystalSelected = XSDataCrystal()
        xsDataSpaceGroupSelected = XSDataSpaceGroup()
        xsDataSpaceGroupSelected.setName(XSDataString(spaceGroupName))
        xsDataCrystalSelected.setSpaceGroup(xsDataSpaceGroupSelected)
#        xsDataCrystalSelected.setCell(xsDataCellSelected)
        xsDataCrystalSelected.setMosaicity(XSDataDouble(_xsDataResultXDSIndexing.mosaicity.value))
        xsDataCrystalSelected.setCell(XSDataCell.parseString(_xsDataResultXDSIndexing.unitCell.marshal()))

        xsDataIndexingSolutionSelected.setCrystal(xsDataCrystalSelected)

        xsDataOrientation = XSDataOrientation()
        xsDataOrientation.setMatrixA(_xsDataResultXDSIndexing.getAMatrix())
        xsDataOrientation.setMatrixU(_xsDataResultXDSIndexing.getUMatrix())
        xsDataIndexingSolutionSelected.setOrientation(xsDataOrientation)


        xsDataStatisticsIndexing = XSDataStatisticsIndexing()

        if (_xsDataExperimentalCondition is not None):
            fBeamPositionXOrig = _xsDataExperimentalCondition.getDetector().getBeamPositionX().getValue()
            fBeamPositionYOrig = _xsDataExperimentalCondition.getDetector().getBeamPositionY().getValue()
            fBeamPositionXNew = _xsDataResultXDSIndexing.getBeamCentreX().getValue()
            fBeamPositionYNew = _xsDataResultXDSIndexing.getBeamCentreY().getValue()
            xsDataStatisticsIndexing.setBeamPositionShiftX(XSDataLength(fBeamPositionXOrig - fBeamPositionXNew))
            xsDataStatisticsIndexing.setBeamPositionShiftY(XSDataLength(fBeamPositionYOrig - fBeamPositionYNew))

        xsDataExperimentalConditionRefined = None
        if (_xsDataExperimentalCondition is None):
            xsDataExperimentalConditionRefined = XSDataExperimentalCondition()
        else:
            # Copy the incoming experimental condition
            xmlExperimentalCondition = _xsDataExperimentalCondition.marshal()
            xsDataExperimentalConditionRefined = XSDataExperimentalCondition.parseString(xmlExperimentalCondition)

        xsDataDetector = xsDataExperimentalConditionRefined.getDetector()
        if (xsDataDetector is None):
            xsDataDetector = XSDataDetector()

        xsDataDetector.setBeamPositionX(XSDataLength(_xsDataResultXDSIndexing.getBeamCentreX().value))
        xsDataDetector.setBeamPositionY(XSDataLength(_xsDataResultXDSIndexing.getBeamCentreY().value))
        xsDataDetector.setDistance(_xsDataResultXDSIndexing.getDistance())

        xsDataExperimentalConditionRefined.setDetector(xsDataDetector)
        xsDataIndexingSolutionSelected.setExperimentalConditionRefined(xsDataExperimentalConditionRefined)

        xsDataIndexingResult.setSelectedSolution(xsDataIndexingSolutionSelected)

        return xsDataIndexingResult
#
#        xsDataLabelitScreenOutput = _xsDataResultLabelit.getLabelitScreenOutput()
#        xsDataLabelitMosflmScriptsOutput = _xsDataResultLabelit.getLabelitMosflmScriptsOutput()
#
#        iSelectedSolutionNumber = xsDataLabelitScreenOutput.getSelectedSolutionNumber().getValue()
#
#        xsDataIndexingResult = XSDataIndexingResult()
#        xsDataIndexingSolutionSelected = None
#
#        for xsDataLabelitSolution in xsDataLabelitScreenOutput.getLabelitScreenSolution():
#            xsDataCrystal = XSDataCrystal()
#            xsDataSpaceGroup = XSDataSpaceGroup()
#            edStringSpaceGroupName = EDUtilsSymmetry.getMinimumSymmetrySpaceGroupFromBravaisLattice(xsDataLabelitSolution.getBravaisLattice().getValue())
#            xsDataSpaceGroup.setName(XSDataString(edStringSpaceGroupName))
#            xsDataCrystal.setSpaceGroup(xsDataSpaceGroup)
#            xsDataCrystal.setCell(xsDataLabelitSolution.getUnitCell())
#            xsDataIndexingSolution = XSDataIndexingSolution()
#            xsDataIndexingSolution.setCrystal(xsDataCrystal)
#            iIndex = xsDataLabelitSolution.getSolutionNumber().getValue()
#            xsDataIndexingSolution.setNumber(XSDataInteger(iIndex))
#            xsDataIndexingResult.addSolution(xsDataIndexingSolution)
#            if (iIndex == iSelectedSolutionNumber):
#                xsDataIndexingSolutionSelected = XSDataIndexingSolutionSelected()
#                xsDataIndexingSolutionSelected.setNumber(XSDataInteger(iIndex))
#                edStringSelectedSpaceGroupName = edStringSpaceGroupName
#                xsDataCellSelected = xsDataLabelitSolution.getUnitCell()
#                fRmsdSelected = xsDataLabelitSolution.getRmsd().getValue()
#                iNumberOfSpotsSelected = xsDataLabelitSolution.getNumberOfSpots().getValue()
#
#        xsDataCrystalSelected = XSDataCrystal()
#        xsDataSpaceGroupSelected = XSDataSpaceGroup()
#        xsDataSpaceGroupSelected.setName(XSDataString(edStringSelectedSpaceGroupName))
#        # xsDataSpaceGroupSelected.setITNumber( XSDataInteger( iSelectedSpaceGroupNumber ) )
#        xsDataCrystalSelected.setSpaceGroup(xsDataSpaceGroupSelected)
#        xsDataCrystalSelected.setCell(xsDataCellSelected)
#        xsDataCrystalSelected.setMosaicity(XSDataDouble(xsDataLabelitScreenOutput.getMosaicity().getValue()))
#        xsDataIndexingSolutionSelected.setCrystal(xsDataCrystalSelected)
#
#        xsDataOrientation = XSDataOrientation()
#        xsDataOrientation.setMatrixA(xsDataLabelitMosflmScriptsOutput.getAMatrix())
#        xsDataOrientation.setMatrixU(xsDataLabelitMosflmScriptsOutput.getUMatrix())
#        xsDataIndexingSolutionSelected.setOrientation(xsDataOrientation)
#
#        xsDataStatisticsIndexing = XSDataStatisticsIndexing()
#
#        if (_xsDataExperimentalCondition is not None):
#            fBeamPositionXOrig = _xsDataExperimentalCondition.getDetector().getBeamPositionX().getValue()
#            fBeamPositionYOrig = _xsDataExperimentalCondition.getDetector().getBeamPositionY().getValue()
#            fBeamPositionXNew = xsDataLabelitScreenOutput.getBeamCentreX().getValue()
#            fBeamPositionYNew = xsDataLabelitScreenOutput.getBeamCentreY().getValue()
#            xsDataStatisticsIndexing.setBeamPositionShiftX(XSDataLength(fBeamPositionXOrig - fBeamPositionXNew))
#            xsDataStatisticsIndexing.setBeamPositionShiftY(XSDataLength(fBeamPositionYOrig - fBeamPositionYNew))
#
#        # xsDataStatisticsIndexing.setSpotDeviXSDataLength( dDistanceRefinedationAngular( XSDataAngle( dDeviationAngular ) )
#        xsDataStatisticsIndexing.setSpotDeviationPositional(XSDataLength(fRmsdSelected))
#        xsDataStatisticsIndexing.setSpotsUsed(XSDataInteger(iNumberOfSpotsSelected))
#        xsDataStatisticsIndexing.setSpotsTotal(XSDataInteger(iNumberOfSpotsSelected))
#        xsDataIndexingSolutionSelected.setStatistics(xsDataStatisticsIndexing)
#
#        xsDataExperimentalConditionRefined = None
#        if (_xsDataExperimentalCondition is None):
#            xsDataExperimentalConditionRefined = XSDataExperimentalCondition()
#        else:
#            # Copy the incoming experimental condition
#            xmlExperimentalCondition = _xsDataExperimentalCondition.marshal()
#            xsDataExperimentalConditionRefined = XSDataExperimentalCondition.parseString(xmlExperimentalCondition)
#
#        xsDataDetector = xsDataExperimentalConditionRefined.getDetector()
#        if (xsDataDetector is None):
#            xsDataDetector = XSDataDetector()
#
#        xsDataDetector.setBeamPositionX(xsDataLabelitScreenOutput.getBeamCentreX())
#        xsDataDetector.setBeamPositionY(xsDataLabelitScreenOutput.getBeamCentreY())
#        xsDataDetector.setDistance(xsDataLabelitScreenOutput.getDistance())
#
#        xsDataExperimentalConditionRefined.setDetector(xsDataDetector)
#        xsDataIndexingSolutionSelected.setExperimentalConditionRefined(xsDataExperimentalConditionRefined)

    @staticmethod
    def generateXSDataInputXDSIntegration(_xsDataIndexingInput, _spaceGroupNumber, _unitCell, _filePaths):
        xsDataInputXDSIntegration = XSDataInputXDSIntegration()
        xsDataCollection = _xsDataIndexingInput.dataCollection
        xsDataInputXDSIntegration = EDHandlerXSDataXDSv1_0.generateXSDataInputXDS(xsDataInputXDSIntegration, xsDataCollection)
        xsDataInputXDSIntegration.crystal.space_group_number = XSDataInteger(_spaceGroupNumber)
        xsDataInputXDSIntegration.crystal.unit_cell_constants = _unitCell
        xsDataInputXDSIntegration.filePaths = _filePaths
        return xsDataInputXDSIntegration
