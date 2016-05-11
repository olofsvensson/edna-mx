
 ***** CORRECT ***** (VERSION January 10, 2014)   3-Jul-2014

 INPUT PARAMETER VALUES
 ----------------------
 SPACE_GROUP_NUMBER=    1 as used in the INTEGRATE step
 UNIT_CELL_CONSTANTS=    50.942    61.956    68.435  89.797  89.749  89.885 as used by INTEGRATE
 FRIEDEL'S_LAW=FALSE
 PROFILE_FITTING= TRUE 
 OVERLOAD=   1048500     MINPK=  75.00000    WFAC1=   1.0
 INCLUDE_RESOLUTION_RANGE=    60.000     1.900
 NAME_TEMPLATE_OF_DATA_FRAMES=i/CER-sampA08_1_????.cbf CBF
 DATA_RANGE=       1      90
 ROTATION_AXIS=  1.000000  0.000000  0.000000
 OSCILLATION_RANGE=  0.200000
 STARTING_ANGLE=    92.013     STARTING_FRAME=       1
 X-RAY_WAVELENGTH=  0.976250
 INCIDENT_BEAM_DIRECTION= -0.003700  0.004649  1.024311
 FRACTION_OF_POLARIZATION=   0.990
 POLARIZATION_PLANE_NORMAL=  0.000000  1.000000  0.000000
 AIR=   0.00031
 DETECTOR=PILATUS
 SILICON=  3.670364 SENSOR_THICKNESS=  0.320000
 NUMBER OF DETECTOR SEGMENTS   1
 NX=  2463  NY=  2527    QX=  0.172000  QY=  0.172000
 ORGX=   1238.56  ORGY=   1247.03
 DETECTOR_DISTANCE=   390.075
 DIRECTION_OF_DETECTOR_X-AXIS=   1.00000   0.00000   0.00000
 DIRECTION_OF_DETECTOR_Y-AXIS=   0.00000   1.00000   0.00000
 BEAM_DIVERGENCE_E.S.D.=   0.100
 REFLECTING_RANGE_E.S.D.=   0.860
 MINIMUM_ZETA=     0.050
 MAXIMUM_ERROR_OF_SPOT_POSITION=   3.0
 MAXIMUM_ERROR_OF_SPINDLE_POSITION=   2.0
 MINIMUM_I/SIGMA=   3.0
 REFLECTIONS/CORRECTION_FACTOR=      50
 STRICT_ABSORPTION_CORRECTION=FALSE 
 CORRECTIONS= DECAY MODULATION ABSORPTION                      
 REFERENCE_DATA_SET=                                                  


    7458 REFLECTIONS ON FILE "INTEGRATE.HKL"
       0 CORRUPTED REFLECTION RECORDS (IGNORED)
       0 MATCHING REFLECTIONS SPECIFIED IN FILE "FILTER.HKL"
       0 REFLECTIONS INCOMPLETE OR OUTSIDE IMAGE RANGE       1 ...      90
       0 OVERLOADED REFLECTIONS (IGNORED)
     249 REFLECTIONS OUTSIDE ACCEPTED RESOLUTION RANGES
                OR TOO CLOSE TO ROTATION AXIS (IGNORED)
    7209 REFLECTIONS ACCEPTED



 ******************************************************************************
                      AUTOMATIC SPACE GROUP ASSIGNMENT
 ******************************************************************************

 XDS adopts the following approach.
 (1) it looks for possible symmetries of the crystal lattice
 (2) it computes a redundancy independent R-factor for all enantiomorphous
     point groups compatible with the observed lattice symmetry.
 (3) it selects the group which explains the intensity data at an acceptable,
     redundancy-independent R-factor (Rmeas, Rrim) using a minimum number of
     unique reflections.

 This approach does not test for the presence of screw axes. Consequently,
 orthorhombic cell axes will be specified in increasing length (following
 conventions), despite the possibility that different assignments for the
 cell axes could become necessary for space groups P222(1) and P2(1)2(1)2
 containing one or two screw axes, respectively.

 The user can always override the automatic decisions by specifying the
 correct space group number and unit cell constants in XDS.INP and repeating
 the CORRECT step of XDS. This provides a simple way to rename orthorhombic
 cell constants if screw axes are present.

 In addition, the user has the option to specify in XDS.INP
 (a) a reference data set or
 (b) a reindexing transformation or
 (c) the three basis vectors (if known from processing a previous data set
 taken at the same crystal orientation in a multi-wavelength experiment).
 These features of XDS are useful for resolving the issue of alternative
 settings of polar or rhombohedral cells (like P4, P6, R3).

 =====> Specifications provided by the user in XDS.INP:
 SPACE_GROUP_NUMBER=    0 (0: unknown symmetry and unit cell)
 UNIT_CELL_CONSTANTS=     0.00     0.00     0.00   0.000   0.000   0.000
 UNIT_CELL_A-AXIS=     0.000     0.000     0.000 (0 0 0 : unknown)
 UNIT_CELL_B-AXIS=     0.000     0.000     0.000 (0 0 0 : unknown)
 UNIT_CELL_C-AXIS=     0.000     0.000     0.000 (0 0 0 : unknown)
 REIDX=  0  0  0  0  0  0  0  0  0  0  0  0 (all 0 : not specified)
 TEST_RESOLUTION_RANGE=   10.00    5.00 (Angstrom) for space group determination
 NUMBER OF ACCEPTED REFLECTIONS FOR CALCULATING Rmeas              454
 NUMBER OF ACCEPTED UNIQUE REFLECTIONS FROM REFERENCE DATA SET       0


 *********** DETERMINATION OF LATTICE CHARACTER AND BRAVAIS LATTICE ***********

 The CHARACTER OF A LATTICE is defined by the metrical parameters of its
 reduced cell as described in the INTERNATIONAL TABLES FOR CRYSTALLOGRAPHY
 Volume A, p. 746 (KLUWER ACADEMIC PUBLISHERS, DORDRECHT/BOSTON/LONDON, 1989).
 Note that more than one lattice character may have the same BRAVAIS LATTICE.

 A lattice character is marked "*" to indicate a lattice consistent with the
 observed locations of the diffraction spots. These marked lattices must have
 low values for the QUALITY OF FIT and their implicated UNIT CELL CONSTANTS
 should not violate the ideal values by more than
 MAX_CELL_AXIS_ERROR=  0.03
 MAX_CELL_ANGLE_ERROR=           3.0 (Degrees)

 The REINDEXING TRANSFORMATION REIDX() consists of 12 integers that relate
 the original indices H,K,L from file INTEGRATE.HKL to the indices H',K',L'
 with respect to the new cell.
    H'=(REIDX(1)*H+REIDX( 2)*K+REIDX( 3)*L)/IDXV+REIDX( 4)
    K'=(REIDX(5)*H+REIDX( 6)*K+REIDX( 7)*L)/IDXV+REIDX( 8)
    L'=(REIDX(9)*H+REIDX(10)*K+REIDX(11)*L)/IDXV+REIDX(12)
 The value of the integer IDXV depends on the lattice type used for
 specifying reflections on file INTEGRATE.HKL; IDXV is
 1 for a primitive,
 2 for a face or body centred,
 3 for a rhombohedral,
 4 for a lattice centred on all faces.
 IDXV is set by XDS and cannot be input by the user.

  LATTICE-  BRAVAIS-   QUALITY  UNIT CELL CONSTANTS (ANGSTROEM & DEGREES)    REINDEXING TRANSFORMATION
 CHARACTER  LATTICE     OF FIT      a      b      c   alpha  beta gamma

 *  31        aP          0.0      51.0   61.9   68.3  89.9  89.8  89.9    1  0  0  0  0  1  0  0  0  0  1  0
 *  44        aP          1.6      51.0   61.9   68.3  90.1  90.2  89.9   -1  0  0  0  0 -1  0  0  0  0  1  0
 *  33        mP          5.0      51.0   61.9   68.3  90.1  90.2  89.9   -1  0  0  0  0 -1  0  0  0  0  1  0
 *  35        mP          5.9      61.9   51.0   68.3  90.2  90.1  89.9    0  1  0  0  1  0  0  0  0  0 -1  0
 *  34        mP          6.2      51.0   68.3   61.9  90.1  89.9  90.2    1  0  0  0  0  0 -1  0  0  1  0  0
 *  32        oP          7.8      51.0   61.9   68.3  90.1  90.2  89.9   -1  0  0  0  0 -1  0  0  0  0  1  0
    20        mC        161.5      92.3   92.1   51.0  89.9  90.3  95.6    0  1  1  0  0  1 -1  0 -1  0  0  0
    25        mC        163.4      92.3   92.1   51.0  90.1  90.3  84.4    0 -1 -1  0  0  1 -1  0  1  0  0  0
    23        oC        166.2      92.1   92.3   51.0  90.3  90.1  84.4    0 -1  1  0  0  1  1  0 -1  0  0  0
    21        tP        168.1      61.9   68.3   51.0  90.2  89.9  90.1    0 -1  0  0  0  0  1  0 -1  0  0  0
    10        mC        239.2      80.3   80.1   68.3  90.0  90.2 101.1    1  1  0  0  1 -1  0  0  0  0 -1  0
    14        mC        240.8      80.3   80.1   68.3  90.0  90.2  78.9   -1 -1  0  0  1 -1  0  0  0  0  1  0
    13        oC        244.5      80.3   80.1   68.3  90.0  90.2  78.9   -1 -1  0  0  1 -1  0  0  0  0  1  0
    11        tP        246.1      51.0   61.9   68.3  90.1  90.2  89.9   -1  0  0  0  0 -1  0  0  0  0  1  0
    28        mC        248.4      51.0  145.6   61.9  89.9  90.1  69.8   -1  0  0  0 -1  0  2  0  0  1  0  0
    29        mC        248.9      51.0  133.8   68.3  90.0  90.2  67.8    1  0  0  0  1 -2  0  0  0  0 -1  0
    37        mC        250.4     145.6   51.0   61.9  89.9  90.1  69.8   -1  0  2  0 -1  0  0  0  0 -1  0  0
    36        oC        252.3      51.0  145.6   61.9  89.9  89.9 110.2   -1  0  0  0  1  0 -2  0  0 -1  0  0
    39        mC        253.0     133.8   51.0   68.3  90.2  90.0  67.8   -1  2  0  0 -1  0  0  0  0  0  1  0
    38        oC        254.9      51.0  133.8   68.3  90.0  90.2 112.2   -1  0  0  0  1 -2  0  0  0  0  1  0
    30        mC        369.2      61.9  149.9   51.0  89.8  90.1  65.7    0  1  0  0  0  1 -2  0 -1  0  0  0
    41        mC        370.4     149.9   61.9   51.0  89.9  90.2  65.7    0  1 -2  0  0  1  0  0  1  0  0  0
    40        oC        373.2      61.9  149.9   51.0  89.8  89.9 114.3    0  1  0  0  0 -1  2  0  1  0  0  0
     2        hR        400.7      80.1   85.1  105.7 103.3  81.6 112.3    1 -1  0  0 -1  0  1  0 -1 -1 -1  0
     4        hR        405.4      80.1   85.4  105.2 103.2  81.5 112.3   -1  1  0  0  1  0  1  0  1  1 -1  0
     3        cP        407.3      51.0   61.9   68.3  90.1  90.2  89.9   -1  0  0  0  0 -1  0  0  0  0  1  0
    12        hP        493.3      51.0   61.9   68.3  89.9  90.2  90.1    1  0  0  0  0 -1  0  0  0  0 -1  0
    27        mC        495.7     133.8   51.0   92.1  90.1 128.4  67.8   -1  2  0  0 -1  0  0  0  0 -1  1  0
    22        hP        533.5      61.9   68.3   51.0  90.2  89.9  90.1    0 -1  0  0  0  0  1  0 -1  0  0  0
     5        cI        570.2      85.1   80.3   92.1  58.9  53.6  67.8   -1  0  1  0 -1 -1  0  0  0 -1  1  0
    42        oI        617.7      51.0   61.9  158.2 113.0 108.6  89.9    1  0  0  0  0  1  0  0 -1 -1  2  0
    26        oF        618.8      51.0  133.8  145.6  82.4 110.2 112.2    1  0  0  0 -1  2  0  0 -1  0  2  0
     1        cF        648.8     105.3  105.2  105.2 107.9  99.1 122.1    1 -1  1  0  1  1 -1  0 -1  1  1  0
    19        oI        656.0      51.0   92.1  105.2  85.1  61.3  90.1   -1  0  0  0  0 -1  1  0 -1  1  1  0
    15        tI        736.9      51.0   61.9  158.2  67.0  71.4  89.9   -1  0  0  0  0 -1  0  0 -1 -1  2  0
    18        tI        779.2      92.1  105.2   51.0  61.3  89.9  94.9    0 -1  1  0  1 -1 -1  0  1  0  0  0
     9        hR        982.2      51.0   80.1  219.8  94.1 103.2 129.4    1  0  0  0 -1  1  0  0 -1 -1  3  0
     6        tI        999.0      92.3   85.4   80.3  67.5  58.6  53.4    0  1  1  0  1  0  1  0  1  1  0  0
     7        tI        999.0      85.4   80.3   92.3  58.6  53.4  67.5    1  0  1  0  1  1  0  0  0  1  1  0
     8        oI        999.0      80.3   85.4   92.3  53.4  58.6  67.5   -1 -1  0  0 -1  0 -1  0  0 -1 -1  0
    16        oF        999.0      80.3   80.1  158.8  95.5 120.6  78.9   -1 -1  0  0  1 -1  0  0  1  1  2  0
    17        mC        999.0      80.1   80.3   85.4  67.5 112.3  78.9    1 -1  0  0 -1 -1  0  0 -1  0 -1  0
    24        hR        999.0     150.3   92.1   51.0  90.1  70.4 102.5    1 -2 -1  0  0  1 -1  0  1  0  0  0
    43        mI        999.0      80.3  158.8   61.9 113.1 140.6  59.4    1  1  0  0  1  1  2  0  0 -1  0  0

 ****** LATTICE SYMMETRY IMPLICATED BY SPACE GROUP SYMMETRY ******

BRAVAIS-            POSSIBLE SPACE-GROUPS FOR PROTEIN CRYSTALS
  TYPE                     [SPACE GROUP NUMBER,SYMBOL]
  aP      [1,P1]
  mP      [3,P2] [4,P2(1)]
 mC,mI    [5,C2]
  oP      [16,P222] [17,P222(1)] [18,P2(1)2(1)2] [19,P2(1)2(1)2(1)]
  oC      [21,C222] [20,C222(1)]
  oF      [22,F222]
  oI      [23,I222] [24,I2(1)2(1)2(1)]
  tP      [75,P4] [76,P4(1)] [77,P4(2)] [78,P4(3)] [89,P422] [90,P42(1)2]
          [91,P4(1)22] [92,P4(1)2(1)2] [93,P4(2)22] [94,P4(2)2(1)2]
          [95,P4(3)22] [96,P4(3)2(1)2]
  tI      [79,I4] [80,I4(1)] [97,I422] [98,I4(1)22]
  hP      [143,P3] [144,P3(1)] [145,P3(2)] [149,P312] [150,P321] [151,P3(1)12]
          [152,P3(1)21] [153,P3(2)12] [154,P3(2)21] [168,P6] [169,P6(1)]
          [170,P6(5)] [171,P6(2)] [172,P6(4)] [173,P6(3)] [177,P622]
          [178,P6(1)22] [179,P6(5)22] [180,P6(2)22] [181,P6(4)22] [182,P6(3)22]
  hR      [146,R3] [155,R32]
  cP      [195,P23] [198,P2(1)3] [207,P432] [208,P4(2)32] [212,P4(3)32]
          [213,P4(1)32]
  cF      [196,F23] [209,F432] [210,F4(1)32]
  cI      [197,I23] [199,I2(1)3] [211,I432] [214,I4(1)32]


 ********************* SYMMETRY OF REFLECTION INTENSITIES *********************

 Analysis of symmetry related reflections is based on strong data within a
 TEST_RESOLUTION_RANGE=   10.00    5.00 Angstrom (defined in XDS.INP).

 The symmetry test is carried out for the enantiomorphous space groups above
 (omitting those with screw axes) that conform with the observed lattice
 symmetry. The test is quantified by the redundancy independent R-factor,
 Rmeas, defined by Diederichs & Karplus, Nature Struct. Biol. 4, 269-275 (1997).

 For computation of Rmeas a minimum number of symmetry-related reflections is
 required and set by the user (in XDS.INP) as the parameter
                      MIN_RFL_Rmeas=   50

 Low values for Rmeas should be obtained if the crystal possesses the symmetry
 elements of the tested space group. The decision whether the crystal's data
 satisfy the requirements of the tested space group is based on a constant set
 by the user (in XDS.INP) as the parameter
                      MAX_FAC_Rmeas=      2.
 which provides an upper limit for acceptable Rmeas as a multiple of the
 lowest Rmeas found for all tested space groups. If Rmeas is larger than this
 upper limit, the corresponding space group symmetry is considered violated
 by the observed data.

 XDS will select (*) that space group that requires a minimum number of unique
 reflections to account for the observed intensities at an acceptable Rmeas.

 UNIQUE   = number of unique reflections
 Rmeas    = redundancy independent R-factor (intensities)
 COMPARED = number of reflections used for calculating Rmeas

 SPACE-GROUP         UNIT CELL CONSTANTS            UNIQUE   Rmeas  COMPARED  LATTICE-
   NUMBER      a      b      c   alpha beta gamma                            CHARACTER

       1      51.0   61.9   68.3  89.9  89.8  89.9     388     4.3       66    31 aP
   *  16      51.0   61.9   68.3  90.0  90.0  90.0     277     4.3      177    32 oP
       3      61.9   51.0   68.3  90.0  90.1  90.0     290     4.3      164    35 mP
       3      51.0   61.9   68.3  90.0  90.2  90.0     371     4.3       83    33 mP
       3      51.0   68.3   61.9  90.0  89.9  90.0     375     4.2       79    34 mP
       1      51.0   61.9   68.3  90.1  90.2  89.9     388     4.3       66    44 aP
 

 ************ SELECTED SPACE GROUP AND UNIT CELL FOR THIS DATA SET ************

 SPACE_GROUP_NUMBER=   16
 UNIT_CELL_CONSTANTS=    50.96    61.92    68.32  90.000  90.000  90.000
 UNIT_CELL_A-AXIS=   -50.033    -4.024     8.793
 UNIT_CELL_B-AXIS=   -10.904     0.362   -60.956
 UNIT_CELL_C-AXIS=     5.542   -68.082    -1.236
 REFLECTIONS H,K,L FROM "INTEGRATE.HKL" WILL BE REINDEXED BY
 H' = ( -1*H +  0*K +  0*L)/ 1 +  0
 K' = (  0*H + -1*K +  0*L)/ 1 +  0
 L' = (  0*H +  0*K +  1*L)/ 1 +  0

 *****  4 EQUIVALENT POSITIONS IN SPACE GROUP # 16 *****

    If x',y',z' is an equivalent position to x,y,z, then
        x'=x*ML(1)+y*ML( 2)+z*ML( 3)+ML( 4)/12.0
        y'=x*ML(5)+y*ML( 6)+z*ML( 7)+ML( 8)/12.0
        z'=x*ML(9)+y*ML(10)+z*ML(11)+ML(12)/12.0

    #    1  2  3  4    5  6  7  8    9 10 11 12 
    1    1  0  0  0    0  1  0  0    0  0  1  0
    2   -1  0  0  0    0 -1  0  0    0  0  1  0
    3    1  0  0  0    0 -1  0  0    0  0 -1  0
    4   -1  0  0  0    0  1  0  0    0  0 -1  0

 ******************************************************************************
      MEAN DISCREPANCIES BETWEEN OBSERVED AND CALCULATED SPOT LOCATIONS
 ******************************************************************************

 The discrepancies in X- and Y-coordinates of the spots are depicted in the
 two images DX-CORRECTIONS.cbf and DY-CORRECTIONS.cbf for inspection with
 the XDS-Viewer.



 ******************************************************************************
  REFINEMENT OF DIFFRACTION PARAMETERS USING ALL IMAGES
 ******************************************************************************


 REFINED VALUES OF DIFFRACTION PARAMETERS DERIVED FROM   2929 INDEXED SPOTS
 REFINED PARAMETERS:   DISTANCE BEAM ORIENTATION CELL
 STANDARD DEVIATION OF SPOT    POSITION (PIXELS)     1.35
 STANDARD DEVIATION OF SPINDLE POSITION (DEGREES)    0.14
 SPACE GROUP NUMBER     16
 UNIT CELL PARAMETERS     50.850    61.730    67.903  90.000  90.000  90.000
 E.S.D. OF CELL PARAMETERS  8.2E-02 9.5E-02 2.0E-01 0.0E+00 0.0E+00 0.0E+00
 REC. CELL PARAMETERS   0.019666  0.016200  0.014727  90.000  90.000  90.000
 COORDINATES OF UNIT CELL A-AXIS   -49.888    -4.278     8.870
 COORDINATES OF UNIT CELL B-AXIS   -10.827     0.253   -60.772
 COORDINATES OF UNIT CELL C-AXIS     5.575   -67.661    -1.275
 CRYSTAL MOSAICITY (DEGREES)     0.860
 LAB COORDINATES OF ROTATION AXIS  1.000000  0.000000  0.000000
 DIRECT BEAM COORDINATES (REC. ANGSTROEM)  -0.004887  0.004921  1.024305
 DETECTOR COORDINATES (PIXELS) OF DIRECT BEAM    1229.73   1257.47
 DETECTOR ORIGIN (PIXELS) AT                     1240.52   1246.60
 CRYSTAL TO DETECTOR DISTANCE (mm)       389.04
 LAB COORDINATES OF DETECTOR X-AXIS  1.000000  0.000000  0.000000
 LAB COORDINATES OF DETECTOR Y-AXIS  0.000000  1.000000  0.000000


 THE DATA COLLECTION STATISTICS REPORTED BELOW ASSUMES:
 SPACE_GROUP_NUMBER=   16
 UNIT_CELL_CONSTANTS=    50.85    61.73    67.90  90.000  90.000  90.000


 ******************************************************************************
        MEAN INTENSITY AS FUNCTION OF SPINDLE POSITION WITHIN DATA IMAGE
 ******************************************************************************

 This statistics could serve as a diagnostic tool for detecting
 shutter problems (suggested by Kay Diederichs).
 Data are corrected for this effect if PATCH_SHUTTER_PROBLEM=TRUE in XDS.INP.
 ===> Selected : PATCH_SHUTTER_PROBLEM=FALSE

 INTERVAL = Angular interval in units of the oscillation range
            covered by a data image.
 NUMBER   = Number of reflections in each interval
 INTENSITY= Mean intensity of the reflections in each interval
 FACTOR   = Correction factor applied to intensities;
            INTENSITY(overall)/INTENSITY(interval)

   INTERVAL     NUMBER      INTENSITY      FACTOR
 -0.05  0.05       686       4151.793       0.847
  0.05  0.15       723       3386.479       1.038
  0.15  0.25       710       3123.899       1.125
  0.25  0.35       727       3398.906       1.034
  0.35  0.45       710       3767.008       0.933
  0.45  0.55       732       3635.973       0.967
  0.55  0.65       742       3878.241       0.906
  0.65  0.75       755       3255.993       1.080
  0.75  0.85       686       3197.642       1.099
  0.85  0.95       738       3375.260       1.042
 
 -0.05  0.95      7209       3515.340       1.000
 

 ******************************************************************************
           CORRECTION FACTORS AS FUNCTION OF IMAGE NUMBER & RESOLUTION
 ******************************************************************************

 RECIPROCAL CORRECTION FACTORS FOR INPUT DATA SETS MERGED TO
 OUTPUT FILE: XDS_ASCII.HKL                                     

 THE CALCULATIONS ASSUME         FRIEDEL'S_LAW= TRUE
 TOTAL NUMBER OF CORRECTION FACTORS DEFINED       40
 DEGREES OF FREEDOM OF CHI^2 FIT              1127.3
 CHI^2-VALUE OF FIT OF CORRECTION FACTORS      2.041
 NUMBER OF CYCLES CARRIED OUT                      3

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY.cbf           
 XMIN=     3.4 XMAX=    87.2 NXBIN=    2
 YMIN= 0.00065 YMAX= 0.27874 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS       2247


 ******************************************************************************
  CORRECTION FACTORS AS FUNCTION OF X (fast) & Y(slow) IN THE DETECTOR PLANE
 ******************************************************************************

 RECIPROCAL CORRECTION FACTORS FOR INPUT DATA SETS MERGED TO
 OUTPUT FILE: XDS_ASCII.HKL                                     

 THE CALCULATIONS ASSUME         FRIEDEL'S_LAW= TRUE
 TOTAL NUMBER OF CORRECTION FACTORS DEFINED       49
 DEGREES OF FREEDOM OF CHI^2 FIT              1120.2
 CHI^2-VALUE OF FIT OF CORRECTION FACTORS      1.983
 NUMBER OF CYCLES CARRIED OUT                      3

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX.cbf          
 XMIN=    24.9 XMAX=  2430.4 NXBIN=    7
 YMIN=    27.1 YMAX=  2501.9 NYBIN=    7
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS       2247


 ******************************************************************************
   CORRECTION FACTORS AS FUNCTION OF IMAGE NUMBER & DETECTOR SURFACE POSITION
 ******************************************************************************

 RECIPROCAL CORRECTION FACTORS FOR INPUT DATA SETS MERGED TO
 OUTPUT FILE: XDS_ASCII.HKL                                     

 THE CALCULATIONS ASSUME         FRIEDEL'S_LAW= TRUE
 TOTAL NUMBER OF CORRECTION FACTORS DEFINED       26
 DEGREES OF FREEDOM OF CHI^2 FIT              1127.0
 CHI^2-VALUE OF FIT OF CORRECTION FACTORS      1.958
 NUMBER OF CYCLES CARRIED OUT                      3

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP.cbf          
 XMIN=     3.4 XMAX=    87.2 NXBIN=    2
 DETECTOR_SURFACE_POSITION=    1228    1265
 DETECTOR_SURFACE_POSITION=    1636    1685
 DETECTOR_SURFACE_POSITION=     819    1685
 DETECTOR_SURFACE_POSITION=     819     844
 DETECTOR_SURFACE_POSITION=    1636     844
 DETECTOR_SURFACE_POSITION=    2152    1659
 DETECTOR_SURFACE_POSITION=    1611    2216
 DETECTOR_SURFACE_POSITION=     845    2216
 DETECTOR_SURFACE_POSITION=     303    1659
 DETECTOR_SURFACE_POSITION=     303     870
 DETECTOR_SURFACE_POSITION=     845     313
 DETECTOR_SURFACE_POSITION=    1611     313
 DETECTOR_SURFACE_POSITION=    2152     870
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS       2247


 ******************************************************************************
    CORRECTION PARAMETERS FOR THE STANDARD ERROR OF REFLECTION INTENSITIES
 ******************************************************************************

 The variance v0(I) of the intensity I obtained from counting statistics is
 replaced by v(I)=a*(v0(I)+b*I^2). The model parameters a, b are chosen to
 minimize the discrepancies between v(I) and the variance estimated from
 sample statistics of symmetry related reflections. This model implicates
 an asymptotic limit ISa=1/SQRT(a*b) for the highest I/Sigma(I) that the
 experimental setup can produce (Diederichs (2010) Acta Cryst D66, 733-740).

     a        b          ISa
 5.977E-02  1.400E-01   10.93


 ******************************************************************************
      STANDARD ERROR OF REFLECTION INTENSITIES AS FUNCTION OF RESOLUTION
      FOR DATA SET  XDS_ASCII.HKL                                     
 ******************************************************************************

  I/Sigma  = mean intensity/Sigma of a reflection in shell
  Chi^2    = goodness of fit between sample variances of
             symmetry-related intensities and their errors
             (Chi^2 = 1 for perfect agreement)
  R-FACTOR
  observed = (SUM(ABS(I(h,i)-I(h))))/(SUM(I(h,i)))
  expected = expected R-FACTOR derived from Sigma(I)

   NUMBER  = number of reflections in resolution shell
             used for calculation of R-FACTOR
  ACCEPTED = number of accepted reflections
  REJECTED = number of rejected reflections (MISFITS),
             recognized by comparison with symmetry-related
             reflections.

 RESOLUTION RANGE  I/Sigma  Chi^2  R-FACTOR  R-FACTOR  NUMBER ACCEPTED REJECTED
                                   observed  expected

   39.248  10.497    10.76   0.51      3.16      5.17      20      57       4
   10.497   7.559    10.88   0.28      2.20      5.17      30      78       2
    7.559   6.210    10.78   0.53      2.42      5.58      53     124       4
    6.210   5.395    10.74   0.52      3.23      5.29      64     150       2
    5.395   4.835    10.68   0.62      4.33      5.23      52     141       6
    4.835   4.419    10.61   0.55      3.63      5.20      67     175       8
    4.419   4.095    10.55   0.66      3.68      5.28      75     199      14
    4.095   3.833     9.73   1.21      7.23      5.22      65     197      32
    3.833   3.616     8.84   1.84      6.13      5.32      65     217      34
    3.616   3.432     8.89   2.08      6.35      5.21      55     194      25
    3.432   3.273     9.24   1.97      9.85      5.29      71     238       7
    3.273   3.135     9.95   0.93      3.35      5.23      79     260      10
    3.135   3.012    10.14   1.26      5.65      5.29      90     280      19
    3.012   2.903     9.76   1.28      4.43      5.28      86     264      14
    2.903   2.805     9.06   1.24      5.24      5.33      64     273      27
    2.805   2.717     7.74   2.18      7.60      5.67      38     241      42
    2.717   2.636     6.70   2.41     10.28      5.21      26     231      50
    2.636   2.562     4.02   1.84     10.13      7.65      44     243      44
    2.562   2.494     8.11   1.57      6.44      5.73      80     281      34
    2.494   2.431     7.76   1.87      7.37      5.90      60     293      32
    2.431   2.373     7.52   1.90      6.43      5.68      64     304      16
    2.373   2.318     7.38   1.80      8.92      5.92      70     310      32
    2.318   2.268     1.81   2.51     10.46      7.19      36     289      20
    2.268   2.220     6.42   0.00    -99.90    -99.90       0     220       4
    2.220   2.175     1.20   1.45      5.94      8.97       6     227       6
    2.175   2.133     5.56   0.00    -99.90    -99.90       0     227       4
    2.133   2.093     2.32   2.75     10.97      5.28       2     233       0
    2.093   2.056     3.43   0.00    -99.90    -99.90       0     191       0
    2.056   2.020    -2.45   0.00    -99.90    -99.90       0     160       0
    2.020   1.986     3.47   0.00    -99.90    -99.90       0     157       0
    1.986   1.954    -2.25   0.00    -99.90    -99.90       0     116       0
    1.954   1.923     4.02   0.00    -99.90    -99.90       0      85       0
    1.923   1.894     4.74   0.00    -99.90    -99.90       0      62       0
   --------------------------------------------------------------------------
   39.248   1.894     6.97   1.35      6.39      5.29    1362    6717     492
 


 ******************************************************************************
  SUMMARY OF DATA SET STATISTICS FOR VARIOUS SUBSETS OF INCLUDED DATA IMAGES
 ******************************************************************************

 Data set statistics is reported below several times, each with a different
 upper limit on the number of images included. This provides the user with
 the information for deciding which data images should be excluded from the
 final data set because of radiation damage or other defects. If the user
 decides for a subset of "good" images that differs from the specification
 as given by the input parameter (see DATA_RANGE= in XDS.INP) the CORRECT-
 step of XDS must be repeated with the new parameter values for DATA_RANGE=.


 ******************************************************************************
  SUMMARY OF DATA SET STATISTICS FOR IMAGE   DATA_RANGE=       1      46
 ******************************************************************************


          COMPLETENESS AND QUALITY OF DATA SET
          ------------------------------------

 R-FACTOR
 observed = (SUM(ABS(I(h,i)-I(h))))/(SUM(I(h,i)))
 expected = expected R-FACTOR derived from Sigma(I)

 COMPARED = number of reflections used for calculating R-FACTOR
 I/SIGMA  = mean of intensity/Sigma(I) of unique reflections
            (after merging symmetry-related observations)
 Sigma(I) = standard deviation of reflection intensity I
            estimated from sample statistics

 R-meas   = redundancy independent R-factor (intensities)
            Diederichs & Karplus (1997), Nature Struct. Biol. 4, 269-275.

 CC(1/2)  = percentage of correlation between intensities from
            random half-datasets. Correlation significant at
            the 0.1% level is marked by an asterisk.
            Karplus & Diederichs (2012), Science 336, 1030-33
 Anomal   = percentage of correlation between random half-sets
  Corr      of anomalous intensity differences. Correlation
            significant at the 0.1% level is marked.
 SigAno   = mean anomalous difference in units of its estimated
            standard deviation (|F(+)-F(-)|/Sigma). F(+), F(-)
            are structure factor estimates obtained from the
            merged intensity observations in each parity class.
  Nano    = Number of unique reflections used to calculate
            Anomal_Corr & SigAno. At least two observations
            for each (+ and -) parity are required.

       NOTE:      Friedel pairs are treated as different reflections.

 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  CC(1/2)  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     5.63         180     154      1257       12.3%       2.1%      5.3%       49   11.50      2.9%    99.8*     0    0.000       0
     4.00         308     259      2238       11.6%       4.0%      5.2%       95   11.54      5.6%    98.7*     0    0.000       0
     3.27         359     323      2885       11.2%       7.0%      5.2%       72   10.99      9.9%    97.3*     0    0.000       1
     2.84         497     460      3403       13.5%       3.5%      5.2%       74   10.40      5.0%    99.4*     0    0.000       0
     2.54         425     421      3884       10.8%      11.0%      5.8%        8    8.82     15.6%    99.5*     0    0.000       0
     2.32         537     531      4285       12.4%       6.3%      5.3%       12    8.27      9.0%    97.4*     0    0.000       0
     2.15         350     349      4655        7.5%       4.5%      5.2%        2    7.57      6.4%     0.0      0    0.000       0
     2.01         251     251      4993        5.0%     -99.9%    -99.9%        0  -99.00    -99.9%     0.0      0    0.000       0
     1.89          91      91      5310        1.7%     -99.9%    -99.9%        0  -99.00    -99.9%     0.0      0    0.000       0
    total        2998    2839     32910        8.6%       5.6%      5.2%      312    9.25      7.9%    98.3*     0    0.000       1


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES    3606
 NUMBER OF REJECTED MISFITS                             253
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                  0
 NUMBER OF ACCEPTED OBSERVATIONS                       3353
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                 3193



 ******************************************************************************
  STATISTICS OF SAVED DATA SET "XDS_ASCII.HKL" (DATA_RANGE=       1      90)
 FILE TYPE:         XDS_ASCII      MERGE=FALSE          FRIEDEL'S_LAW=FALSE
 ******************************************************************************

   REFLECTIONS OF TYPE H,0,0  0,K,0  0,0,L OR EXPECTED TO BE ABSENT (*)
   --------------------------------------------------------------------

   H    K    L  RESOLUTION  INTENSITY     SIGMA    INTENSITY/SIGMA  #OBSERVED

    0    8    0     7.716   0.4385E+04  0.4013E+03        10.93           1 
    0    9    0     6.859   0.8176E+01  0.5788E+01         1.41           1 
    0   10    0     6.173   0.1675E+04  0.1535E+03        10.92           1 
    0   11    0     5.612   0.1879E+02  0.7277E+01         2.58           1 
    0   12    0     5.144   0.4652E+04  0.4258E+03        10.93           1 
    0   13    0     4.748  -0.4775E+02  0.1003E+02        -4.76           1 
    0   14    0     4.409   0.3415E+05  0.3125E+04        10.93           1 
    0   15    0     4.115  -0.1709E+03  0.2050E+02        -8.34           1 
    0   16    0     3.858   0.4622E+05  0.4228E+04        10.93           1 
    0   17    0     3.631   0.1443E+05  0.1320E+04        10.93           1 
    0   18    0     3.429   0.4658E+05  0.4261E+04        10.93           1 
    0   19    0     3.249   0.1308E+04  0.1208E+03        10.83           1 
    0   20    0     3.086   0.1220E+04  0.1127E+03        10.83           1 
    0   21    0     2.940   0.9567E+03  0.8884E+02        10.77           1 
    0   22    0     2.806   0.1633E+01  0.1484E+02         0.11           1 
    0   24    0     2.572   0.2912E+03  0.3123E+02         9.32           1 
    0   25    0     2.469   0.2898E+00  0.1554E+02         0.02           1 
    0   26    0     2.374   0.1336E+04  0.1237E+03        10.81           1 
    0   27    0     2.286  -0.2507E+03  0.2936E+02        -8.54           1 
    0   29    0     2.129   0.3073E+03  0.3433E+02         8.95           1 
   11    0    0     4.623  -0.6725E+01  0.3449E+01        -1.95           1 
   12    0    0     4.238   0.3130E+04  0.2864E+03        10.93           1 
   13    0    0     3.912   0.2931E+05  0.2682E+04        10.93           1 

          COMPLETENESS AND QUALITY OF DATA SET
          ------------------------------------

 R-FACTOR
 observed = (SUM(ABS(I(h,i)-I(h))))/(SUM(I(h,i)))
 expected = expected R-FACTOR derived from Sigma(I)

 COMPARED = number of reflections used for calculating R-FACTOR
 I/SIGMA  = mean of intensity/Sigma(I) of unique reflections
            (after merging symmetry-related observations)
 Sigma(I) = standard deviation of reflection intensity I
            estimated from sample statistics

 R-meas   = redundancy independent R-factor (intensities)
            Diederichs & Karplus (1997), Nature Struct. Biol. 4, 269-275.

 CC(1/2)  = percentage of correlation between intensities from
            random half-datasets. Correlation significant at
            the 0.1% level is marked by an asterisk.
            Karplus & Diederichs (2012), Science 336, 1030-33
 Anomal   = percentage of correlation between random half-sets
  Corr      of anomalous intensity differences. Correlation
            significant at the 0.1% level is marked.
 SigAno   = mean anomalous difference in units of its estimated
            standard deviation (|F(+)-F(-)|/Sigma). F(+), F(-)
            are structure factor estimates obtained from the
            merged intensity observations in each parity class.
  Nano    = Number of unique reflections used to calculate
            Anomal_Corr & SigAno. At least two observations
            for each (+ and -) parity are required.

       NOTE:      Friedel pairs are treated as different reflections.

 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  CC(1/2)  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     5.63         353     277      1257       22.0%       2.7%      5.3%      146   12.00      3.8%    99.8*   -55    0.674       8
     4.00         636     509      2238       22.7%       3.7%      5.2%      241   11.83      5.2%    99.3*    63    0.860       4
     3.27         719     606      2885       21.0%       7.8%      5.2%      220   11.19     10.9%    97.3*    18    3.604       4
     2.84         969     817      3403       24.0%       4.4%      5.3%      299   10.63      6.2%    98.8*   -26    0.552      16
     2.54         805     732      3884       18.8%       9.6%      5.3%      146    9.06     13.6%    97.2*   -19    1.214       8
     2.32        1051     930      4285       21.7%       7.3%      5.7%      242    8.43     10.3%    97.4*    18    1.477      15
     2.15         661     644      4655       13.8%       7.4%      5.7%       34    7.58     10.5%    96.3*    26    0.804       2
     2.01         479     478      4993        9.6%      11.0%      5.3%        2    6.87     15.5%     0.0      0    0.000       0
     1.89         248     248      5310        4.7%     -99.9%    -99.9%        0  -99.00    -99.9%     0.0      0    0.000       0
    total        5921    5241     32910       15.9%       6.4%      5.3%     1330    9.38      8.9%    98.2*    22    1.150      57


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES    7209
 NUMBER OF REJECTED MISFITS                             492
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                  0
 NUMBER OF ACCEPTED OBSERVATIONS                       6717
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                 6021



 ******************************************************************************
    WILSON STATISTICS OF DATA SET  "XDS_ASCII.HKL"
 ******************************************************************************

 Data is divided into resolution shells and a straight line 
 A - 2*B*SS is fitted to log<I>, where
   RES    = mean resolution (Angstrom) in shell
   SS     = mean of (sin(THETA)/LAMBDA)**2 in shell
   <I>    = mean reflection intensity in shell
   BO     = (A - log<I>)/(2*SS)
    #     = number of reflections in resolution shell

   WILSON LINE (using all data) : A=   8.106 B=   4.889 CORRELATION=  0.14
      #      RES      SS        <I>       log(<I>)       BO
      70    10.484   0.002  4.3695E+03       8.382     -60.7
     126     6.590   0.006  2.4411E+03       7.800      26.6
     165     5.181   0.009  4.0730E+03       8.312     -11.1
     211     4.390   0.013  3.7989E+03       8.242      -5.3
     211     3.880   0.017  1.3310E+04       9.496     -41.8
     228     3.505   0.020  1.1023E+04       9.308     -29.5
     291     3.228   0.024  1.5287E+03       7.332      16.1
     314     3.009   0.028  1.0179E+03       6.926      21.4
     314     2.827   0.031  6.5833E+02       6.490      25.8
     234     2.676   0.035  4.5622E+03       8.426      -4.6
     316     2.543   0.039  4.6751E+02       6.147      25.3
     348     2.432   0.042  3.7793E+02       5.935      25.7
     336     2.337   0.046  3.5423E+02       5.870      24.4
     202     2.249   0.049  2.4790E+04      10.118     -20.4
     292     2.166   0.053  2.5379E+02       5.537      24.1
     200     2.099   0.057  6.7263E+03       8.814      -6.2
     147     2.030   0.061  5.8638E+03       8.677      -4.7
     131     1.978   0.064  6.5141E+02       6.479      12.7
      77     1.924   0.068  1.0325E+04       9.242      -8.4


 HIGHER ORDER MOMENTS OF WILSON DISTRIBUTION OF  CENTRIC DATA
    AS COMPARED WITH THEORETICAL VALUES. (EXPECTED: 1.00)    
      #      RES        <I**2>/      <I**3>/      <I**4>/  
                         3<I>**2     15<I>**3    105<I>**4 

      28    10.484        0.647        0.484        0.308
      32     6.590        0.632        0.420        0.263
      29     5.181        2.078        4.076        6.658
      42     4.390        0.374        0.207        0.108
      36     3.880        0.724        0.437        0.208
      37     3.505        0.786        0.423        0.180
      43     3.228        1.084        0.940        0.694
      47     3.009        0.943        0.688        0.453
      34     2.827        1.075        0.967        0.824
      25     2.676        1.086        0.586        0.237
      32     2.543        2.684        3.331        3.419
      36     2.432        1.134        1.130        1.012
      29     2.337        1.947        3.107        4.471
      13     2.249        0.481        0.207        0.067
      30     2.166        1.755        1.571        1.128
      19     2.099        1.143        1.130        0.819
       9     2.030        1.133        0.858        0.499
       9     1.978        2.060        2.507        2.294
       3     1.924        0.528        0.191        0.053
     533   overall        1.160        1.210        1.248


 HIGHER ORDER MOMENTS OF WILSON DISTRIBUTION OF ACENTRIC DATA
    AS COMPARED WITH THEORETICAL VALUES. (EXPECTED: 1.00)    
      #      RES        <I**2>/      <I**3>/      <I**4>/  
                         2<I>**2      6<I>**3     24<I>**4 

      42    10.484        1.009        0.882        0.747
      94     6.590        1.124        1.339        1.629
     136     5.181        0.971        1.030        1.058
     169     4.390        1.112        1.244        1.448
     175     3.880        1.789        2.731        3.398
     191     3.505        1.011        0.827        0.550
     248     3.228        0.942        1.067        1.371
     267     3.009        0.832        0.661        0.477
     280     2.827        0.976        1.025        1.085
     209     2.676        1.168        1.105        0.834
     284     2.543        0.841        0.846        0.953
     312     2.432        0.981        1.019        1.066
     307     2.337        0.895        0.778        0.628
     189     2.249        0.948        0.669        0.387
     262     2.166        0.921        0.893        0.816
     181     2.099        1.943        2.736        3.054
     138     2.030        2.179        3.714        5.165
     122     1.978        2.653        6.513       13.616
      74     1.924        0.906        0.703        0.456
    3680   overall        1.150        1.391        1.701

   ======= CUMULATIVE INTENSITY DISTRIBUTION =======
 DEFINITIONS:
   <I>    = mean reflection intensity
 Na(Z)exp = expected number of acentric reflections with I <= Z*<I>
 Na(Z)obs = observed number of acentric reflections with I <= Z*<I>
 Nc(Z)exp = expected number of  centric reflections with I <= Z*<I>
 Nc(Z)obs = observed number of  centric reflections with I <= Z*<I>



 Nc(Z)obs/Nc(Z)exp versus resolution and Z (0.1-1.0)
      #      RES     0.1   0.2   0.3   0.4   0.5   0.6   0.7   0.8   0.9   1.0

      28    10.484  1.29  1.03  0.86  0.83  0.82  0.83  0.90  1.02  1.09  1.20
      32     6.590  0.13  0.54  0.53  0.73  0.84  0.89  0.89  0.94  1.00  0.96
      29     5.181  0.97  1.10  1.16  1.17  1.06  1.04  0.98  0.93  0.89  0.96
      42     4.390  0.38  0.62  0.91  1.01  1.05  1.15  1.12  1.17  1.16  1.19
      36     3.880  0.67  1.29  1.20  1.12  1.07  1.04  0.98  0.97  0.97  0.98
      37     3.505  0.54  0.70  0.91  0.80  0.83  0.77  0.91  0.86  0.82  0.87
      43     3.228  0.09  0.40  0.84  0.84  0.80  0.95  0.90  0.92  0.96  0.99
      47     3.009  0.26  0.43  0.41  0.63  0.78  0.80  0.86  0.85  0.87  0.84
      34     2.827  0.71  0.85  0.71  0.68  0.79  0.84  0.84  0.84  0.81  0.82
      25     2.676  0.64  0.81  0.77  0.76  0.85  0.78  0.80  0.83  0.79  0.76
      32     2.543  0.25  0.45  0.53  0.66  0.60  0.56  0.63  0.60  0.71  0.73
      36     2.432  0.34  0.56  0.53  0.59  0.53  0.54  0.74  0.80  0.76  0.86
      29     2.337  0.42  0.30  0.41  0.51  0.46  0.43  0.58  0.66  0.63  0.66
      13     2.249  2.48  1.78  1.48  1.30  1.18  1.10  1.03  0.98  0.94  0.90
      30     2.166  0.13  0.39  0.56  0.63  0.64  0.71  0.78  0.80  0.76  0.83
      19     2.099  2.97  2.13  2.02  1.78  1.62  1.50  1.41  1.34  1.28  1.23
       9     2.030  2.24  1.61  1.33  1.17  1.07  1.19  1.12  1.06  1.01  0.98
       9     1.978  2.24  1.93  1.87  1.64  1.49  1.39  1.30  1.24  1.18  1.14
       3     1.924  0.00  0.00  0.00  0.00  0.64  0.59  0.56  1.06  1.01  0.98
     533   overall  0.66  0.78  0.82  0.85  0.85  0.87  0.89  0.91  0.91  0.93


 Na(Z)obs/Na(Z)exp versus resolution and Z (0.1-1.0)
      #      RES     0.1   0.2   0.3   0.4   0.5   0.6   0.7   0.8   0.9   1.0

      42    10.484  0.25  0.39  0.46  0.51  0.48  0.69  0.71  0.95  0.92  0.87
      94     6.590  0.45  1.00  1.19  1.19  1.16  1.11  1.06  0.99  0.99  0.99
     136     5.181  0.70  0.69  0.91  0.89  1.07  1.01  1.02  1.07  1.08  1.08
     169     4.390  0.50  0.78  0.75  0.75  0.78  0.80  0.83  0.88  0.92  0.94
     175     3.880  2.64  2.46  2.14  1.85  1.57  1.52  1.44  1.36  1.26  1.20
     191     3.505  2.37  1.79  1.74  1.49  1.30  1.21  1.11  1.06  1.00  0.96
     248     3.228  0.64  0.76  0.82  0.86  0.90  0.93  0.94  0.97  0.99  1.00
     267     3.009  0.59  0.83  0.87  0.82  0.80  0.84  0.94  1.05  1.02  1.02
     280     2.827  1.05  0.85  0.90  0.91  0.96  0.92  0.94  0.99  1.01  1.03
     209     2.676  3.77  2.77  2.10  1.73  1.46  1.31  1.22  1.18  1.11  1.06
     284     2.543  1.11  0.99  1.17  1.11  1.06  1.05  1.04  1.05  1.07  1.06
     312     2.432  1.08  0.99  1.01  0.98  0.99  0.96  0.98  0.99  1.01  1.03
     307     2.337  1.30  1.08  1.02  0.97  1.03  1.01  1.00  1.01  1.04  1.04
     189     2.249  3.34  1.90  1.37  1.16  1.00  0.90  0.90  0.85  0.81  0.83
     262     2.166  1.32  1.09  1.03  1.07  1.05  1.02  1.02  1.03  1.02  1.02
     181     2.099  6.68  3.69  2.69  2.11  1.80  1.57  1.42  1.31  1.22  1.15
     138     2.030  7.01  3.88  2.77  2.20  1.86  1.62  1.45  1.36  1.26  1.19
     122     1.978  3.27  2.71  2.40  2.14  1.90  1.74  1.63  1.52  1.42  1.34
      74     1.924  0.99  0.75  0.78  0.74  0.96  1.14  1.18  1.10  1.07  1.05
    3680   overall  1.96  1.49  1.34  1.21  1.15  1.10  1.08  1.07  1.06  1.04


 List of      1 reflections *NOT* obeying Wilson distribution (Z> 10.0)

   h    k    l     RES      Z     Intensity    Sigma

   18   17   17    1.95   11.47  0.7471E+04  0.6841E+03 "alien"


 List of      1 reflections *NOT* obeying Wilson distribution (sorted by resolution)
 Ice rings could occur at (Angstrom):
 3.897,3.669,3.441, 2.671,2.249,2.072, 1.948,1.918,1.883,1.721

   h    k    l     RES      Z     Intensity    Sigma

   18   17   17    1.95   11.47  0.7471E+04  0.6841E+03

 NUMBER OF UNIQUE ALIEN REFLECTIONS WITH A Z-SCORE ABOVE LIMIT         1
 (ALIENS ABOVE LIMIT (REJECT_ALIEN=      20.0) ARE MARKED INVALID)

 NUMBER OF REFLECTION RECORDS ON OUTPUT FILE "XDS_ASCII.HKL"        7209
 NUMBER OF ACCEPTED OBSERVATIONS (INCLUDING SYSTEMATIC ABSENCES)    6716
 NUMBER OF REJECTED MISFITS & ALIENS (marked by -1*SIGMA(IOBS))      493


 cpu time used                  4.7 sec
 elapsed wall-clock time        0.5 sec
