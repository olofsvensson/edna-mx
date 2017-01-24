
 ***** CORRECT ***** (VERSION Nov 1, 2016  BUILT=20161101)   2-Dec-2016

 INPUT PARAMETER VALUES
 ----------------------
 SPACE_GROUP_NUMBER=   21 as used in the INTEGRATE step
 UNIT_CELL_CONSTANTS=    52.713   148.997    79.725  90.000  90.000  90.000 as used by INTEGRATE
 FRIEDEL'S_LAW=TRUE 
 PROFILE_FITTING= TRUE 
 OVERLOAD=   1048576     MINPK=  75.00000    WFAC1=   1.0
 INCLUDE_RESOLUTION_RANGE=    50.000     1.900
 NAME_TEMPLATE_OF_DATA_FRAMES=images/xtal5w1_1_????.cbf CBF
 DATA_RANGE=       1    1120
 ROTATION_AXIS=  0.999998  0.000078  0.002188
 OSCILLATION_RANGE=  0.100000
 STARTING_ANGLE=     0.000     STARTING_FRAME=       1
 X-RAY_WAVELENGTH=  0.972386
 INCIDENT_BEAM_DIRECTION= -0.007174  0.004865  1.028362
 FRACTION_OF_POLARIZATION=   0.990
 POLARIZATION_PLANE_NORMAL=  0.000000  1.000000  0.000000
 AIR=   0.00100
 DETECTOR=PILATUS
 SILICON=  3.627217 SENSOR_THICKNESS=  0.000000
 NUMBER OF DETECTOR SEGMENTS   1
 NX=  2463  NY=  2527    QX=  0.172000  QY=  0.172000
 ORGX=   1240.46  ORGY=   1247.17
 DETECTOR_DISTANCE=   304.052
 DIRECTION_OF_DETECTOR_X-AXIS=   1.00000   0.00000   0.00000
 DIRECTION_OF_DETECTOR_Y-AXIS=   0.00000   1.00000   0.00000
 BEAM_DIVERGENCE_E.S.D.=   0.029
 REFLECTING_RANGE_E.S.D.=   0.089
 MINIMUM_ZETA=     0.050
 MAXIMUM_ERROR_OF_SPOT_POSITION=   3.0
 MAXIMUM_ERROR_OF_SPINDLE_POSITION=   2.0
 MINIMUM_I/SIGMA=   3.0
 REFLECTIONS/CORRECTION_FACTOR=      50
 STRICT_ABSORPTION_CORRECTION=FALSE 
 CORRECTIONS= DECAY MODULATION ABSORPTION                      
 REFERENCE_DATA_SET=                                                  
 FIT_B-FACTOR_TO_REFERENCE_DATA_SET=FALSE 

  183779 REFLECTIONS ON FILE "INTEGRATE.HKL"
       0 CORRUPTED REFLECTION RECORDS (IGNORED)
       0 MATCHING REFLECTIONS SPECIFIED IN FILE "FILTER.HKL"
      17 REFLECTIONS INCOMPLETE OR OUTSIDE IMAGE RANGE       1 ...    1120
       0 OVERLOADED REFLECTIONS (IGNORED)
   79307 REFLECTIONS OUTSIDE ACCEPTED RESOLUTION RANGES
                OR TOO CLOSE TO ROTATION AXIS (IGNORED)
  104455 REFLECTIONS ACCEPTED


 NUMBER OF UNIQUE REFLECTIONS IN FILE "REMOVE.HKL"       6



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
 SPACE_GROUP_NUMBER=   20 (0: unknown symmetry and unit cell)
 UNIT_CELL_CONSTANTS=    52.72   149.00    79.73  90.000  90.000  90.000
 UNIT_CELL_A-AXIS=     0.000     0.000     0.000 (0 0 0 : unknown)
 UNIT_CELL_B-AXIS=     0.000     0.000     0.000 (0 0 0 : unknown)
 UNIT_CELL_C-AXIS=     0.000     0.000     0.000 (0 0 0 : unknown)
 REIDX=  0  0  0  0  0  0  0  0  0  0  0  0 (all 0 : not specified)
 TEST_RESOLUTION_RANGE=   10.00    5.00 (Angstrom) for space group determination
 NUMBER OF ACCEPTED REFLECTIONS FOR CALCULATING Rmeas             5086
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

 *  31        aP          0.0      52.7   79.0   79.7  90.0  90.0  70.5   -2  0  0  0 -1 -1  0  0  0  0  2  0
 *  44        aP          0.0      52.7   79.0   79.7  90.0  90.0 109.5    2  0  0  0 -1 -1  0  0  0  0 -2  0
 *  34        mP          0.0      52.7   79.7   79.0  90.0 109.5  90.0   -2  0  0  0  0  0  2  0  1  1  0  0
 *  39        mC          0.0     149.0   52.7   79.7  90.0  90.0  90.0    0 -2  0  0 -2  0  0  0  0  0 -2  0
 *  29        mC          0.0      52.7  149.0   79.7  90.0  90.0  90.0   -2  0  0  0  0  2  0  0  0  0 -2  0
 *  38        oC          0.0      52.7  149.0   79.7  90.0  90.0  90.0   -2  0  0  0  0 -2  0  0  0  0  2  0
 *  37        mC         19.8     149.0   52.7   79.7  90.0  90.0  90.0    0 -2  0  0 -2  0  0  0  0  0 -2  0
 *  33        mP         19.8      52.7   79.7   79.0  90.0 109.5  90.0   -2  0  0  0  0  0 -2  0  1 -1  0  0
 *  28        mC         19.8      52.7  149.0   79.7  90.0  90.0  90.0   -2  0  0  0  0 -2  0  0  0  0  2  0
 *  36        oC         19.8      52.7  149.0   79.7  90.0  90.0  90.0   -2  0  0  0  0  2  0  0  0  0 -2  0
    35        mP        250.0      79.0   52.7   79.7  90.0  90.0 109.5    1  1  0  0 -2  0  0  0  0  0  2  0
    32        oP        250.0      52.7   79.0   79.7  90.0  90.0 109.5    2  0  0  0 -1 -1  0  0  0  0 -2  0
    20        mC        269.8     112.3  112.3   52.7 103.6 103.6  90.5   -1  1 -2  0 -1  1  2  0  2  0  0  0
    23        oC        269.8     112.3  112.3   52.7  76.4 103.6  89.5   -1  1  2  0  1 -1  2  0  2  0  0  0
    25        mC        269.8     112.3  112.3   52.7  76.4 103.6  89.5   -1  1  2  0  1 -1  2  0  2  0  0  0
    27        mC        269.8     167.9   52.7  112.3 103.6 138.4  71.7   -2  0  4  0 -2  0  0  0  1 -1 -2  0
    21        tP        269.8      79.0   79.7   52.7  90.0 109.5  90.0   -1  1  0  0  0  0  2  0  2  0  0  0
    19        oI        289.7      52.7  112.3  112.3  96.8  76.4 103.6   -2  0  0  0  1 -1 -2  0 -1 -1  2  0
    26        oF        394.8      52.7  167.9  149.0  90.0  90.0 108.3    2  0  0  0 -2  0  4  0  0 -2  0  0
    18        tI        414.7     112.3  112.3   52.7  76.4  76.4  83.2    1 -1 -2  0  1  1 -2  0  2  0  0  0
    42        oI        591.6      52.7   79.7  169.0 118.1  90.0  90.0    2  0  0  0  0  0  2  0  0 -2 -2  0
    41        mC        591.6     177.0   79.7   52.7  90.0 107.3  63.2   -2  2  2  0  0  0  2  0  2  0  0  0
    10        mC        623.7     108.6   79.0   79.7  90.0  90.0 113.8   -3 -1  0  0 -1  1  0  0  0  0 -2  0
    12        hP        623.7      52.7   79.0   79.7  90.0  90.0 109.5    2  0  0  0 -1 -1  0  0  0  0 -2  0
    13        oC        623.7      79.0  108.6   79.7  90.0  90.0  66.2    1 -1  0  0 -3 -1  0  0  0  0 -2  0
    14        mC        623.7      79.0  108.6   79.7  90.0  90.0  66.2    1 -1  0  0 -3 -1  0  0  0  0 -2  0
    30        mC        686.8      79.0  178.0   52.7  98.5 109.5  63.6   -1 -1  0  0 -1 -1 -4  0  2  0  0  0
    40        oC        811.8      79.0  178.0   52.7  81.5 109.5 116.4    1  1  0  0 -1 -1 -4  0 -2  0  0  0
    22        hP        831.7      79.0   79.7   52.7  90.0 109.5  90.0   -1  1  0  0  0  0  2  0  2  0  0  0
    11        tP        873.7      52.7   79.0   79.7  90.0  90.0 109.5    2  0  0  0 -1 -1  0  0  0  0 -2  0
     2        hR        893.5      79.0   95.6  134.8  99.8  71.0 100.6   -1  1  0  0  2  0  2  0  3  1 -2  0
     4        hR        893.5     108.6   95.6  112.3 117.6  73.5 113.7   -3 -1  0  0  2  0 -2  0  1 -1  2  0
     3        cP        893.5      52.7   79.0   79.7  90.0  90.0 109.5   -2  0  0  0  1  1  0  0  0  0 -2  0
    15        tI        913.4      52.7   79.7  169.0  61.9  90.0  90.0   -2  0  0  0  0  0 -2  0  0 -2 -2  0
     1        cF        999.0     112.3  134.8  112.3 101.0  89.5 130.5   -1  1  2  0 -3 -1 -2  0  1 -1  2  0
     5        cI        999.0      95.6   79.0  112.3  56.8  62.4  79.4    2  0 -2  0  1 -1  0  0 -1 -1 -2  0
     6        tI        999.0     112.3   95.6   79.0  79.4  56.8  62.4   -1 -1 -2  0  2  0 -2  0  1 -1  0  0
     7        tI        999.0      95.6   79.0  112.3  56.8  62.4  79.4    2  0 -2  0  1 -1  0  0 -1 -1 -2  0
     8        oI        999.0      79.0   95.6  112.3  62.4  56.8  79.4   -1  1  0  0 -2  0  2  0  1  1  2  0
     9        hR        999.0      52.7   95.6  238.8 109.8  83.7 123.5    2  0  0  0 -2  0  2  0  1 -3 -2  0
    16        oF        999.0      79.0  108.6  178.0 100.3 116.4  66.2   -1  1  0  0  3  1  0  0  1 -1 -4  0
    17        mC        999.0      95.6   95.6   79.0  79.4 100.6  66.9   -2  0  2  0  2  0  2  0  1  1  0  0
    24        hR        999.0     178.0  112.3   52.7 103.6  81.5 113.2   -1 -1 -4  0  1 -1  2  0 -2  0  0  0
    43        mI        999.0      79.0  178.0   79.0 110.2 141.0  63.6    1  1  0  0  1  1  4  0  1 -1  0  0

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


 Several solutions exist for the given space group that explain the data. The
 selected solution (marked "*") correlates best with the given reference data set.
 The independent settings of the cell can be obtained by application of the
 REINDEXING TRANSFORMATION to the original indices H,K,L from file INTEGRATE.HKL

 CORRELATION = correlation factor with the reference data set
 NPAIR       = number of unique reflection pairs correlated 
 Rmeas=Rrim  = redundancy independent R-factor (intensities)
               For definition see:
               Rmeas : Diederichs & Karplus,
                       Nature Struct. Biol. 4, 269-275 (1997);
               Rrim  : Weiss & Hilgenfeld,
                       J.Appl.Cryst. 30,203-205 (1997).
 COMPARED    = number of reflections used for calculating Rmeas
 ESD         = Agreement with given unit cell geometry

 CORRELATION  NPAIR  Rmeas  COMPARED  ESD       REINDEX TRANSFORMATION

  *   0.00        0   18.9    3798    0.00  2  0  0  0  0  2  0  0  0  0  2  0

 ************ SELECTED SPACE GROUP AND UNIT CELL FOR THIS DATA SET ************

 SPACE_GROUP_NUMBER=   20
 UNIT_CELL_CONSTANTS=    52.72   149.00    79.73  90.000  90.000  90.000
 UNIT_CELL_A-AXIS=    14.800    23.820    44.637
 UNIT_CELL_B-AXIS=   -94.884   111.421   -27.999
 UNIT_CELL_C-AXIS=   -57.247   -38.781    39.676
 REFLECTIONS H,K,L FROM "INTEGRATE.HKL" WILL BE REINDEXED BY
 H' = (  2*H +  0*K +  0*L)/ 2 +  0
 K' = (  0*H +  2*K +  0*L)/ 2 +  0
 L' = (  0*H +  0*K +  2*L)/ 2 +  0

 *****  8 EQUIVALENT POSITIONS IN SPACE GROUP # 20 *****

    If x',y',z' is an equivalent position to x,y,z, then
        x'=x*ML(1)+y*ML( 2)+z*ML( 3)+ML( 4)/12.0
        y'=x*ML(5)+y*ML( 6)+z*ML( 7)+ML( 8)/12.0
        z'=x*ML(9)+y*ML(10)+z*ML(11)+ML(12)/12.0

    #    1  2  3  4    5  6  7  8    9 10 11 12 
    1    1  0  0  0    0  1  0  0    0  0  1  0
    2    1  0  0  0    0 -1  0  0    0  0 -1  0
    3   -1  0  0  0    0 -1  0  0    0  0  1  6
    4   -1  0  0  0    0  1  0  0    0  0 -1  6
    5    1  0  0  6    0  1  0  6    0  0  1  0
    6    1  0  0  6    0 -1  0  6    0  0 -1  0
    7   -1  0  0  6    0 -1  0  6    0  0  1  6
    8   -1  0  0  6    0  1  0  6    0  0 -1  6

 ******************************************************************************
      MEAN DISCREPANCIES BETWEEN OBSERVED AND CALCULATED SPOT LOCATIONS
 ******************************************************************************

 The discrepancies in X- and Y-coordinates of the spots are depicted in the
 two images DX-CORRECTIONS.cbf and DY-CORRECTIONS.cbf for inspection with
 the XDS-Viewer.



 ******************************************************************************
  REFINEMENT OF DIFFRACTION PARAMETERS USING ALL IMAGES
 ******************************************************************************


 REFINED VALUES OF DIFFRACTION PARAMETERS DERIVED FROM     22421 INDEXED SPOTS
 REFINED PARAMETERS:   AXIS BEAM ORIENTATION CELL POSITION
 STANDARD DEVIATION OF SPOT    POSITION (PIXELS)     0.44
 STANDARD DEVIATION OF SPINDLE POSITION (DEGREES)    0.03
 SPACE GROUP NUMBER     20
 UNIT CELL PARAMETERS     52.715   149.002    79.727  90.000  90.000  90.000
 E.S.D. OF CELL PARAMETERS  3.1E-02 6.9E-02 3.6E-02 0.0E+00 0.0E+00 0.0E+00
 REC. CELL PARAMETERS   0.018970  0.006711  0.012543  90.000  90.000  90.000
 COORDINATES OF UNIT CELL A-AXIS    14.793    23.813    44.643
 COORDINATES OF UNIT CELL B-AXIS   -94.909   111.406   -27.975
 COORDINATES OF UNIT CELL C-AXIS   -57.244   -38.806    39.668
 CRYSTAL MOSAICITY (DEGREES)     0.089
 LAB COORDINATES OF ROTATION AXIS  0.999998  0.000088  0.002166
 DIRECT BEAM COORDINATES (REC. ANGSTROEM)  -0.007172  0.004853  1.028362
 DETECTOR COORDINATES (PIXELS) OF DIRECT BEAM    1228.13   1255.53
 DETECTOR ORIGIN (PIXELS) AT                     1240.46   1247.19
 CRYSTAL TO DETECTOR DISTANCE (mm)       304.06
 LAB COORDINATES OF DETECTOR X-AXIS  1.000000  0.000000  0.000000
 LAB COORDINATES OF DETECTOR Y-AXIS  0.000000  1.000000  0.000000


 THE DATA COLLECTION STATISTICS REPORTED BELOW ASSUMES:
 SPACE_GROUP_NUMBER=   20
 UNIT_CELL_CONSTANTS=    52.71   149.00    79.73  90.000  90.000  90.000


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
 -0.05  0.05     10354         24.903       1.073
  0.05  0.15     10551         24.950       1.071
  0.15  0.25     10620         25.304       1.056
  0.25  0.35     10352         43.021       0.621
  0.35  0.45     10529         24.401       1.095
  0.45  0.55     10380         24.619       1.085
  0.55  0.65     10422         25.112       1.064
  0.65  0.75     10497         24.676       1.082
  0.75  0.85     10321         24.539       1.088
  0.85  0.95     10404         25.726       1.038
 
 -0.05  0.95    104430         26.710       1.000
 

 ******************************************************************************
           CORRECTION FACTORS AS FUNCTION OF IMAGE NUMBER & RESOLUTION
 ******************************************************************************

 RECIPROCAL CORRECTION FACTORS FOR INPUT DATA SETS MERGED TO
 OUTPUT FILE: XDS_ASCII.HKL                                     

 THE CALCULATIONS ASSUME         FRIEDEL'S_LAW= TRUE
 TOTAL NUMBER OF CORRECTION FACTORS DEFINED      440
 DEGREES OF FREEDOM OF CHI^2 FIT             16368.2
 CHI^2-VALUE OF FIT OF CORRECTION FACTORS      0.954
 NUMBER OF CYCLES CARRIED OUT                      5

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY.cbf           
 XMIN=     0.0 XMAX=  1119.4 NXBIN=   22
 YMIN= 0.00056 YMAX= 0.27746 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS      22521


 ******************************************************************************
  CORRECTION FACTORS AS FUNCTION OF X (fast) & Y(slow) IN THE DETECTOR PLANE
 ******************************************************************************

 RECIPROCAL CORRECTION FACTORS FOR INPUT DATA SETS MERGED TO
 OUTPUT FILE: XDS_ASCII.HKL                                     

 THE CALCULATIONS ASSUME         FRIEDEL'S_LAW= TRUE
 TOTAL NUMBER OF CORRECTION FACTORS DEFINED      441
 DEGREES OF FREEDOM OF CHI^2 FIT             16382.3
 CHI^2-VALUE OF FIT OF CORRECTION FACTORS      0.936
 NUMBER OF CYCLES CARRIED OUT                      4

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX.cbf          
 XMIN=   224.9 XMAX=  2223.7 NXBIN=   21
 YMIN=   252.4 YMAX=  2264.4 NYBIN=   21
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS      22521


 ******************************************************************************
   CORRECTION FACTORS AS FUNCTION OF IMAGE NUMBER & DETECTOR SURFACE POSITION
 ******************************************************************************

 RECIPROCAL CORRECTION FACTORS FOR INPUT DATA SETS MERGED TO
 OUTPUT FILE: XDS_ASCII.HKL                                     

 THE CALCULATIONS ASSUME         FRIEDEL'S_LAW= TRUE
 TOTAL NUMBER OF CORRECTION FACTORS DEFINED      286
 DEGREES OF FREEDOM OF CHI^2 FIT             16421.0
 CHI^2-VALUE OF FIT OF CORRECTION FACTORS      0.919
 NUMBER OF CYCLES CARRIED OUT                      3

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP.cbf          
 XMIN=     0.0 XMAX=  1119.4 NXBIN=   22
 DETECTOR_SURFACE_POSITION=    1224    1258
 DETECTOR_SURFACE_POSITION=    1564    1600
 DETECTOR_SURFACE_POSITION=     885    1600
 DETECTOR_SURFACE_POSITION=     885     917
 DETECTOR_SURFACE_POSITION=    1564     917
 DETECTOR_SURFACE_POSITION=    1993    1579
 DETECTOR_SURFACE_POSITION=    1543    2032
 DETECTOR_SURFACE_POSITION=     906    2032
 DETECTOR_SURFACE_POSITION=     456    1579
 DETECTOR_SURFACE_POSITION=     456     938
 DETECTOR_SURFACE_POSITION=     906     485
 DETECTOR_SURFACE_POSITION=    1543     485
 DETECTOR_SURFACE_POSITION=    1993     938
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS      22521


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
 7.512E-01  2.195E-03   24.62


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

   42.174  17.326    18.20   1.45      4.27      3.09     135     139       8
   17.326  12.804    15.92   1.16      4.02      3.53     207     208      10
   12.804  10.618    15.55   1.25      3.76      3.24     276     276      10
   10.618   9.270    15.94   1.13      3.48      3.49     323     325       9
    9.270   8.331    15.27   1.08      3.99      3.75     357     361       7
    8.331   7.630    13.55   0.99      3.78      4.01     289     302      11
    7.630   7.081    12.70   1.02      4.78      4.60     341     346       7
    7.081   6.635    11.03   0.95      4.84      5.07     420     423       8
    6.635   6.264    11.13   1.00      5.34      5.29     450     460       5
    6.264   5.949    10.25   1.03      4.94      5.12     494     499       7
    5.949   5.678    11.41   0.98      4.46      4.79     500     505      11
    5.678   5.440    11.89   0.97      4.66      4.76     567     570       7
    5.440   5.230    11.25   0.99      5.04      5.04     523     525      13
    5.230   5.043    12.03   1.02      4.64      4.73     626     631      13
    5.043   4.874    12.27   1.10      4.87      4.61     615     618      13
    4.874   4.721    12.14   0.99      4.40      4.65     647     652      11
    4.721   4.582    12.90   0.92      3.94      4.22     664     667      16
    4.582   4.454    12.52   0.94      4.33      4.66     687     688       9
    4.454   4.337    12.73   0.90      4.06      4.48     666     671      11
    4.337   4.228    12.79   0.91      4.09      4.54     711     718       8
    4.228   4.127    12.08   0.91      4.29      4.57     661     668      11
    4.127   4.033    11.68   1.06      5.02      4.90     612     624      10
    4.033   3.945    11.12   1.04      5.17      5.01     611     623      21
    3.945   3.863    11.58   0.99      4.69      4.92     686     695      10
    3.863   3.785    10.97   1.15      5.60      5.25     743     743      19
    3.785   3.712    10.33   1.05      5.69      5.53     797     804       9
    3.712   3.644    10.27   1.04      5.58      5.59     787     795       9
    3.644   3.578     9.35   1.08      6.25      6.04     827     829       6
    3.578   3.517     8.97   1.04      6.62      6.54     849     853      12
    3.517   3.458     8.54   1.03      6.85      6.76     836     842      11
    3.458   3.402     8.60   1.13      7.18      6.81     884     888      11
    3.402   3.349     8.73   1.00      6.82      6.70     954     956      10
    3.349   3.298     8.53   0.91      6.38      6.87     792     792       6
    3.298   3.249     8.27   1.10      7.52      7.20    1066    1074      15
    3.249   3.203     6.98   1.03      8.37      8.26     894     898       7
    3.203   3.158     7.31   1.00      8.14      8.14     961     967      13
    3.158   3.116     6.95   1.07      8.60      8.45     981     984       9
    3.116   3.075     6.77   0.92      8.82      9.04     994    1001       7
    3.075   3.035     6.17   1.02      9.94      9.88     990     993       4
    3.035   2.997     6.03   1.04     10.10      9.98    1077    1081      11
    2.997   2.961     5.36   1.03     11.35     11.21    1002    1005       7
    2.961   2.925     5.20   1.02     12.22     11.90    1099    1102       6
    2.925   2.891     5.22   0.95     11.67     11.72    1055    1060      12
    2.891   2.858     4.95   0.96     11.69     11.96     986     990      10
    2.858   2.827     4.71   0.97     13.02     13.04     952     963      16
    2.827   2.796     4.77   0.96     12.67     12.56     939     951       7
    2.796   2.766     4.22   1.03     15.45     14.75     933     938      13
    2.766   2.737     4.54   0.97     13.49     13.68     931     945       8
    2.737   2.709     4.12   1.01     15.77     15.31    1099    1110       7
    2.709   2.682     4.21   1.03     14.88     14.80    1040    1046       7
    2.682   2.656     4.00   0.97     15.68     15.81    1050    1056       4
    2.656   2.630     4.39   1.04     15.12     14.58    1142    1147       8
    2.630   2.605     3.66   1.01     17.87     17.47    1115    1126       5
    2.605   2.581     3.68   1.05     17.69     16.81    1159    1164       5
    2.581   2.558     3.80   1.03     17.27     16.88    1194    1199      10
    2.558   2.535     3.48   1.13     19.39     17.91    1179    1183       8
    2.535   2.513     3.40   0.99     18.92     18.88    1219    1222       4
    2.513   2.491     3.38   1.03     18.08     17.81    1113    1115      10
    2.491   2.470     3.37   1.00     19.60     18.99    1257    1261       5
    2.470   2.449     3.02   1.05     21.40     20.70    1192    1195       6
    2.449   2.429     2.75   1.02     23.71     23.26    1327    1328       3
    2.429   2.410     2.80   1.01     22.37     21.98    1152    1157       8
    2.410   2.390     2.61   0.96     24.37     24.97    1276    1286       2
    2.390   2.372     2.87   0.98     22.31     22.11    1326    1328      10
    2.372   2.353     2.66   0.95     23.55     24.09    1305    1311       4
    2.353   2.336     2.73   0.99     23.52     23.43    1226    1232       4
    2.336   2.318     2.62   1.05     24.77     24.10    1321    1325       5
    2.318   2.301     2.59   1.01     24.98     24.52    1387    1392       8
    2.301   2.284     2.38   1.12     29.62     27.56    1217    1220       4
    2.284   2.268     2.40   1.02     26.42     26.14    1365    1367       6
    2.268   2.252     2.33   1.02     28.11     27.44    1349    1354       3
    2.252   2.236     2.24   1.08     31.12     29.09    1418    1420      10
    2.236   2.221     2.28   1.02     29.77     28.85    1270    1274       7
    2.221   2.206     2.06   0.96     30.62     30.87    1247    1255      12
    2.206   2.191     2.11   1.01     31.51     30.71    1292    1301      11
    2.191   2.177     2.04   1.12     34.89     32.69    1192    1213       8
    2.177   2.163     1.93   1.00     33.02     33.17    1178    1195      12
    2.163   2.149     1.90   0.97     34.64     34.60    1233    1248       9
    2.149   2.135     1.79   1.02     37.28     36.38    1221    1227       7
    2.135   2.122     1.68   0.99     40.46     39.72    1346    1357      13
    2.122   2.109     1.63   0.97     41.28     41.27    1423    1430       7
    2.109   2.096     1.78   1.04     39.08     37.43    1333    1344       4
    2.096   2.083     1.65   1.01     41.29     40.78    1364    1369       9
    2.083   2.071     1.69   1.02     40.06     39.24    1357    1368       7
    2.071   2.059     1.41   0.96     47.04     47.30    1484    1493       7
    2.059   2.047     1.53   0.93     42.61     44.23    1412    1417       3
    2.047   2.035     1.49   0.95     43.79     44.65    1328    1333       5
    2.035   2.023     1.30   1.03     52.78     51.22    1514    1522       6
    2.023   2.012     1.41   0.95     46.77     47.75    1448    1455       5
    2.012   2.001     1.33   0.93     48.20     50.10    1523    1529       4
    2.001   1.990     1.22   0.98     54.85     54.92    1413    1419       2
    1.990   1.979     1.19   1.00     56.61     55.73    1472    1481       6
    1.979   1.968     1.07   0.96     62.64     63.19    1498    1504       5
    1.968   1.958     1.20   0.93     52.93     55.77    1611    1618      11
    1.958   1.948     1.25   0.97     54.50     54.46    1423    1431       5
    1.948   1.938     1.17   0.89     54.46     57.38    1605    1614       7
    1.938   1.928     1.01   0.91     64.63     67.18    1529    1534       6
    1.928   1.918     1.00   0.89     63.63     66.72    1564    1569       2
    1.918   1.908     0.89   0.89     70.91     75.38    1548    1556       5
    1.908   1.898     0.91   0.91     70.33     72.53    1307    1327       4
   --------------------------------------------------------------------------
   42.174   1.898     4.42   1.00     12.81     12.76  102960  103575     819
 


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
  SUMMARY OF DATA SET STATISTICS FOR IMAGE   DATA_RANGE=       1     125
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


 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  CC(1/2)  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     5.65         406     296      1051       28.2%       3.9%      3.8%      204   14.30      5.3%    99.3*     0    0.000       1
     4.01         750     599      1775       33.7%       3.5%      3.5%      295   13.44      4.9%    99.6*     0    0.000       0
     3.28         991     795      2247       35.4%       5.2%      4.8%      379   10.30      7.3%    99.2*     0    0.000       0
     2.84        1247    1019      2640       38.6%       8.3%      7.5%      449    6.74     11.7%    97.8*     0    0.000       0
     2.54        1296    1030      2959       34.8%      12.2%     12.4%      532    4.46     17.2%    94.7*     0    0.000       0
     2.32        1517    1241      3259       38.1%      18.0%     17.1%      552    3.21     25.4%    91.1*     0    0.000       0
     2.15        1611    1292      3554       36.4%      24.6%     25.6%      638    2.39     34.8%    83.5*     0    0.000       0
     2.01        1736    1403      3763       37.3%      30.0%     31.2%      666    1.75     42.5%    79.8*     0    0.000       0
     1.90        1885    1503      4017       37.4%      48.3%     46.8%      764    1.24     68.3%    55.4*     0    0.000       0
    total       11439    9178     25265       36.3%      10.4%     10.3%     4479    4.72     14.7%    98.9*     0    0.000       1


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES     11607
 NUMBER OF REJECTED MISFITS                               166
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                    0
 NUMBER OF ACCEPTED OBSERVATIONS                        11441
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                   9180



 ******************************************************************************
  SUMMARY OF DATA SET STATISTICS FOR IMAGE   DATA_RANGE=       1     250
 ******************************************************************************


 AVERAGE INTENSITY FOR       1 REFLECTIONS WHICH SHOULD
 BE SYSTEMATICALLY ABSENT IS     0.1% OF MEAN INTENSITY


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


 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  CC(1/2)  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     5.65         838     427      1051       40.6%       3.9%      3.8%      672   17.38      5.0%    99.7*    21    0.951      21
     4.01        1511     831      1775       46.8%       3.9%      3.9%     1146   16.50      5.1%    99.5*     9    0.908      35
     3.28        1974    1146      2247       51.0%       5.2%      4.8%     1450   12.66      6.9%    99.3*    -5    1.025      45
     2.84        2459    1464      2640       55.5%       8.3%      8.0%     1725    8.02     11.0%    98.6*     3    0.947      77
     2.54        2605    1566      2959       52.9%      13.2%     13.1%     1804    5.28     17.4%    96.0*    -1    0.850      82
     2.32        3050    1889      3259       58.0%      19.6%     19.7%     2007    3.61     25.8%    91.6*     3    0.818      76
     2.15        3236    1959      3554       55.1%      26.4%     27.2%     2194    2.79     34.6%    88.7*     4    0.845      87
     2.01        3448    2111      3763       56.1%      36.2%     36.5%     2330    2.00     47.8%    75.8*    -2    0.726      88
     1.90        3716    2242      4017       55.8%      53.5%     56.4%     2558    1.39     70.7%    56.9*     6    0.695      86
    total       22837   13635     25265       54.0%      10.8%     10.7%    15886    5.52     14.2%    99.1*     4    0.837     597


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES     23134
 NUMBER OF REJECTED MISFITS                               295
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                    1
 NUMBER OF ACCEPTED OBSERVATIONS                        22838
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                  13636



 ******************************************************************************
  SUMMARY OF DATA SET STATISTICS FOR IMAGE   DATA_RANGE=       1     374
 ******************************************************************************


 AVERAGE INTENSITY FOR      13 REFLECTIONS WHICH SHOULD
 BE SYSTEMATICALLY ABSENT IS     0.6% OF MEAN INTENSITY


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


 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  CC(1/2)  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     5.65        1264     521      1051       49.6%       3.9%      3.9%     1138   19.75      4.9%    99.7*     4    0.813      75
     4.01        2318     943      1775       53.1%       4.1%      4.1%     2070   19.62      5.0%    99.6*     3    0.866     115
     3.28        2981    1262      2247       56.2%       5.4%      5.2%     2648   15.10      6.7%    99.5*     5    0.964     116
     2.84        3687    1556      2640       58.9%       8.5%      8.3%     3272    9.71     10.5%    99.0*     9    0.952     133
     2.54        3903    1725      2959       58.3%      13.4%     13.3%     3443    6.39     16.9%    96.3*    -3    0.824     145
     2.32        4595    2029      3259       62.3%      19.3%     19.8%     4032    4.43     24.2%    93.9*     0    0.782     178
     2.15        4807    2186      3554       61.5%      27.5%     27.6%     4142    3.25     34.6%    89.2*     0    0.798     206
     2.01        5174    2397      3763       63.7%      37.4%     38.8%     4449    2.33     47.4%    76.4*     5    0.813     210
     1.90        5575    2556      4017       63.6%      53.2%     56.8%     4849    1.62     67.5%    64.0*    -2    0.703     264
    total       34304   15175     25265       60.1%      11.5%     11.6%    30043    6.58     14.5%    99.1*     3    0.817    1442


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES     34692
 NUMBER OF REJECTED MISFITS                               371
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                   13
 NUMBER OF ACCEPTED OBSERVATIONS                        34308
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                  15177



 ******************************************************************************
  SUMMARY OF DATA SET STATISTICS FOR IMAGE   DATA_RANGE=       1     498
 ******************************************************************************


 AVERAGE INTENSITY FOR      22 REFLECTIONS WHICH SHOULD
 BE SYSTEMATICALLY ABSENT IS     0.7% OF MEAN INTENSITY


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


 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  CC(1/2)  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     5.65        1701     573      1051       54.5%       4.0%      3.9%     1616   22.28      4.8%    99.7*     2    0.874     184
     4.01        3108    1016      1775       57.2%       4.0%      4.1%     2938   22.09      4.8%    99.7*    -4    0.770     314
     3.28        4007    1333      2247       59.3%       5.5%      5.3%     3812   17.23      6.6%    99.6*    -1    0.858     390
     2.84        4951    1640      2640       62.1%       8.6%      8.5%     4709   11.04     10.3%    99.2*     5    0.863     446
     2.54        5225    1847      2959       62.4%      13.9%     13.7%     4943    7.17     16.8%    96.7*    -5    0.796     409
     2.32        6141    2123      3259       65.1%      19.6%     20.1%     5857    5.05     23.8%    94.5*    -3    0.757     494
     2.15        6368    2319      3554       65.3%      27.6%     27.8%     5989    3.65     33.8%    90.5*    -8    0.759     482
     2.01        6877    2544      3763       67.6%      37.9%     39.4%     6472    2.61     46.5%    79.4*     1    0.771     500
     1.90        7415    2704      4017       67.3%      53.7%     57.2%     7063    1.83     66.2%    66.2*     0    0.730     557
    total       45793   16099     25265       63.7%      11.7%     11.9%    43399    7.47     14.2%    99.3*    -2    0.789    3776


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES     46240
 NUMBER OF REJECTED MISFITS                               421
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                   22
 NUMBER OF ACCEPTED OBSERVATIONS                        45797
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                  16101



 ******************************************************************************
  SUMMARY OF DATA SET STATISTICS FOR IMAGE   DATA_RANGE=       1     623
 ******************************************************************************


 AVERAGE INTENSITY FOR      32 REFLECTIONS WHICH SHOULD
 BE SYSTEMATICALLY ABSENT IS     1.9% OF MEAN INTENSITY


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


 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  CC(1/2)  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     5.65        2136     644      1051       61.3%       4.1%      4.0%     2056   23.70      4.9%    99.7*    -2    0.827     265
     4.01        3897    1139      1775       64.2%       4.2%      4.2%     3738   23.30      4.9%    99.7*    -3    0.754     521
     3.28        5018    1492      2247       66.4%       5.7%      5.5%     4827   18.11      6.7%    99.6*     2    0.862     643
     2.84        6222    1823      2640       69.1%       8.8%      8.6%     6014   11.71     10.3%    99.2*     2    0.839     802
     2.54        6567    2059      2959       69.6%      14.1%     13.8%     6285    7.62     16.7%    97.1*    -4    0.800     709
     2.32        7700    2329      3259       71.5%      19.9%     20.2%     7467    5.42     23.6%    94.9*    -3    0.779     890
     2.15        8014    2565      3554       72.2%      27.6%     27.7%     7668    3.90     32.9%    91.1*    -6    0.758     842
     2.01        8618    2783      3763       74.0%      38.5%     39.7%     8278    2.80     45.9%    81.1*     2    0.797     875
     1.90        9297    2961      4017       73.7%      53.9%     57.6%     8994    1.97     64.6%    69.7*     1    0.727     955
    total       57469   17795     25265       70.4%      12.0%     12.1%    55327    7.99     14.2%    99.3*    -1    0.789    6502


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES     57987
 NUMBER OF REJECTED MISFITS                               486
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                   32
 NUMBER OF ACCEPTED OBSERVATIONS                        57469
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                  17795



 ******************************************************************************
  SUMMARY OF DATA SET STATISTICS FOR IMAGE   DATA_RANGE=       1     747
 ******************************************************************************


 AVERAGE INTENSITY FOR      36 REFLECTIONS WHICH SHOULD
 BE SYSTEMATICALLY ABSENT IS     1.0% OF MEAN INTENSITY


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


 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  CC(1/2)  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     5.65        2585     766      1051       72.9%       4.1%      4.0%     2481   23.87      4.8%    99.7*    -3    0.810     299
     4.01        4709    1336      1775       75.3%       4.2%      4.3%     4494   23.25      4.9%    99.7*    -4    0.758     599
     3.28        6051    1741      2247       77.5%       5.7%      5.6%     5762   18.05      6.6%    99.6*    -1    0.843     787
     2.84        7472    2104      2640       79.7%       8.9%      8.8%     7145   11.71     10.3%    99.2*     3    0.840    1017
     2.54        7881    2343      2959       79.2%      14.4%     14.1%     7507    7.67     16.9%    97.0*    -7    0.783     937
     2.32        9253    2692      3259       82.6%      20.4%     20.4%     8824    5.47     23.7%    95.5*    -4    0.785    1247
     2.15        9612    2920      3554       82.2%      28.0%     28.0%     9118    4.03     32.9%    90.9*     0    0.785    1194
     2.01       10326    3144      3763       83.6%      39.6%     40.2%     9854    2.87     46.5%    81.3*     1    0.805    1220
     1.90       11150    3364      4017       83.7%      54.5%     58.0%    10640    2.03     64.0%    71.0*     0    0.731    1350
    total       69039   20410     25265       80.8%      12.1%     12.2%    65825    8.12     14.1%    99.4*    -1    0.790    8650


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES     69630
 NUMBER OF REJECTED MISFITS                               555
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                   36
 NUMBER OF ACCEPTED OBSERVATIONS                        69039
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                  20410



 ******************************************************************************
  SUMMARY OF DATA SET STATISTICS FOR IMAGE   DATA_RANGE=       1     871
 ******************************************************************************


 AVERAGE INTENSITY FOR      36 REFLECTIONS WHICH SHOULD
 BE SYSTEMATICALLY ABSENT IS     1.0% OF MEAN INTENSITY


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


 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  CC(1/2)  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     5.65        3020     892      1051       84.9%       4.1%      4.0%     2907   23.69      4.8%    99.7*    -5    0.812     331
     4.01        5514    1549      1775       87.3%       4.2%      4.4%     5286   22.90      4.9%    99.7*     0    0.782     674
     3.28        7079    2000      2247       89.0%       5.8%      5.7%     6789   17.92      6.8%    99.6*    -1    0.838     879
     2.84        8704    2392      2640       90.6%       9.1%      9.0%     8328   11.65     10.5%    99.1*     1    0.832    1155
     2.54        9207    2642      2959       89.3%      14.6%     14.4%     8801    7.69     17.0%    96.9*    -4    0.794    1097
     2.32       10804    3026      3259       92.9%      20.7%     20.7%    10330    5.52     24.0%    95.3*    -3    0.788    1423
     2.15       11225    3250      3554       91.4%      28.3%     28.1%    10716    4.14     33.0%    90.8*     0    0.796    1415
     2.01       12042    3496      3763       92.9%      40.5%     40.8%    11485    2.91     47.1%    80.9*     0    0.793    1505
     1.90       13006    3742      4017       93.2%      55.9%     58.5%    12430    2.06     65.1%    70.8*     0    0.750    1677
    total       80601   22989     25265       91.0%      12.2%     12.3%    77072    8.21     14.2%    99.4*    -1    0.794   10156


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES     81267
 NUMBER OF REJECTED MISFITS                               630
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                   36
 NUMBER OF ACCEPTED OBSERVATIONS                        80601
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                  22989



 ******************************************************************************
  SUMMARY OF DATA SET STATISTICS FOR IMAGE   DATA_RANGE=       1     996
 ******************************************************************************


 AVERAGE INTENSITY FOR      36 REFLECTIONS WHICH SHOULD
 BE SYSTEMATICALLY ABSENT IS     1.0% OF MEAN INTENSITY


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


 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  CC(1/2)  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     5.65        3463     983      1051       93.5%       4.1%      4.1%     3378   23.86      4.9%    99.7*    -3    0.813     385
     4.01        6319    1700      1775       95.8%       4.2%      4.5%     6156   23.06      4.9%    99.7*    -3    0.763     773
     3.28        8103    2170      2247       96.6%       5.9%      5.8%     7926   18.27      6.8%    99.6*    -2    0.825    1004
     2.84        9962    2578      2640       97.7%       9.3%      9.3%     9745   11.86     10.8%    99.0*     3    0.841    1344
     2.54       10530    2855      2959       96.5%      14.9%     14.7%    10273    7.79     17.3%    96.8*    -1    0.806    1281
     2.32       12349    3217      3259       98.7%      21.0%     21.0%    12116    5.70     24.3%    95.0*    -2    0.789    1614
     2.15       12844    3464      3554       97.5%      28.5%     28.2%    12565    4.29     33.2%    90.5*    -1    0.786    1603
     2.01       13737    3699      3763       98.3%      41.4%     41.5%    13447    3.00     48.0%    81.1*    -1    0.801    1736
     1.90       14892    3951      4017       98.4%      56.3%     58.5%    14633    2.13     65.3%    72.3*     1    0.747    1981
    total       92199   24617     25265       97.4%      12.4%     12.5%    90239    8.44     14.4%    99.4*    -1    0.793   11721


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES     92949
 NUMBER OF REJECTED MISFITS                               714
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                   36
 NUMBER OF ACCEPTED OBSERVATIONS                        92199
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                  24617



 ******************************************************************************
  STATISTICS OF SAVED DATA SET "XDS_ASCII.HKL" (DATA_RANGE=       1    1120)
 FILE TYPE:         XDS_ASCII      MERGE=FALSE          FRIEDEL'S_LAW=TRUE 
 ******************************************************************************

   REFLECTIONS OF TYPE H,0,0  0,K,0  0,0,L OR EXPECTED TO BE ABSENT (*)
   --------------------------------------------------------------------

   H    K    L  RESOLUTION  INTENSITY     SIGMA    INTENSITY/SIGMA  #OBSERVED

    0    0    2    39.863   0.1528E+03  0.4498E+01        33.98           2 
    0    0    3    26.576   0.1021E+00  0.1979E+00         0.52           2*
    0    0    4    19.932   0.2942E+01  0.3401E+00         8.65           2 
    0    0    5    15.945   0.1924E+00  0.3186E+00         0.60           2*
    0    0    6    13.288   0.3246E+03  0.9641E+01        33.66           2 
    0    0    7    11.390   0.2589E+00  0.4507E+00         0.57           2*
    0    0    8     9.966   0.5214E+03  0.1540E+02        33.86           2 
    0    0    9     8.859   0.2806E+00  0.5750E+00         0.49           2*
    0    0   10     7.973   0.3705E+02  0.1727E+01        21.45           2 
    0    0   11     7.248  -0.3129E-01  0.7155E+00        -0.04           2*
    0    0   12     6.644   0.7475E+01  0.9970E+00         7.50           2 
    0    0   13     6.133   0.1203E+01  0.1255E+01         0.96           1*
    0    0   15     5.315  -0.1267E+00  0.1524E+01        -0.08           1*
    0    0   16     4.983   0.2052E+03  0.9832E+01        20.88           1 
    0    0   17     4.690   0.5128E+00  0.1241E+01         0.41           2*
    0    0   18     4.429   0.3935E+02  0.2371E+01        16.59           2 
    0    0   19     4.196   0.2098E+01  0.1522E+01         1.38           2*
    0    0   20     3.986   0.1428E+02  0.1951E+01         7.32           2 
    0    0   21     3.797   0.7078E+00  0.1616E+01         0.44           2*
    0    0   22     3.624   0.2547E+03  0.8731E+01        29.17           2 
    0    0   23     3.466  -0.4271E+00  0.1735E+01        -0.25           2*
    0    0   24     3.322   0.4291E+02  0.3006E+01        14.28           2 
    0    0   25     3.189   0.3727E+01  0.1918E+01         1.94           2*
    0    0   26     3.066   0.1289E+00  0.1836E+01         0.07           2 
    0    0   27     2.953  -0.1350E+01  0.2521E+01        -0.54           1*
    0    0   28     2.847   0.4046E+02  0.4595E+01         8.81           1 
    0    0   29     2.749   0.6439E+00  0.1778E+01         0.36           2*
    0    0   30     2.658   0.8728E+01  0.2107E+01         4.14           2 
    0    0   31     2.572  -0.3739E+00  0.1831E+01        -0.20           2*
    0    0   32     2.491   0.2085E+03  0.8261E+01        25.24           2 
    0    0   33     2.416   0.1411E+00  0.1869E+01         0.08           2*
    0    0   34     2.345   0.5979E+02  0.4089E+01        14.62           2 
    0    0   35     2.278   0.2453E+01  0.2331E+01         1.05           2*
    0    0   36     2.215   0.2290E+02  0.3281E+01         6.98           2 
    0    0   37     2.155  -0.3090E+01  0.2335E+01        -1.32           2*
    0    0   39     2.044  -0.1943E+01  0.3839E+01        -0.51           1*
    0    0   40     1.993   0.2086E+00  0.3401E+01         0.06           1 
    0    0   41     1.945  -0.1568E+01  0.2542E+01        -0.62           2*
    0    4    0    37.250   0.1709E+03  0.7142E+01        23.92           1 
    0    6    0    24.834   0.4788E+02  0.1594E+01        30.03           2 
    0   10    0    14.900   0.1472E+03  0.4566E+01        32.24           2 
    0   12    0    12.417   0.1382E+03  0.4380E+01        31.55           2 
    0   14    0    10.643   0.9653E+03  0.2821E+02        34.21           2 
    0   16    0     9.313   0.2288E+02  0.1232E+01        18.58           2 
    0   18    0     8.278   0.2743E+03  0.8500E+01        32.27           2 
    0   20    0     7.450   0.1525E+03  0.5117E+01        29.80           2 
    0   22    0     6.773   0.3577E+01  0.1340E+01         2.67           1 
    0   24    0     6.208   0.6898E+01  0.1460E+01         4.72           1 
    0   26    0     5.731   0.3021E+02  0.1829E+01        16.51           2 
    0   28    0     5.321   0.2774E+02  0.1869E+01        14.84           2 
    0   32    0     4.656   0.4652E+03  0.2027E+02        22.95           1 
    0   34    0     4.382   0.1013E+03  0.4368E+01        23.20           2 
    0   36    0     4.139   0.5957E+02  0.3211E+01        18.55           2 
    0   38    0     3.921   0.8378E+02  0.4018E+01        20.85           2 
    0   40    0     3.725   0.4472E+03  0.1438E+02        31.10           2 
    0   44    0     3.386   0.1394E+03  0.5948E+01        23.43           2 
    0   46    0     3.239   0.2083E+03  0.1179E+02        17.67           1 
    0   48    0     3.104   0.3309E+02  0.4076E+01         8.12           1 
    0   50    0     2.980   0.1373E+02  0.2523E+01         5.44           2 
    0   52    0     2.865   0.1212E+02  0.2447E+01         4.95           2 
    0   54    0     2.759   0.4495E+02  0.3476E+01        12.93           2 
    0   56    0     2.661   0.1442E+03  0.8895E+01        16.21           1 
    0   58    0     2.569   0.9822E+01  0.3280E+01         2.99           1 
    0   60    0     2.483   0.1411E+03  0.9073E+01        15.56           1 
    0   62    0     2.403   0.2867E+01  0.3348E+01         0.86           1 
    0   64    0     2.328   0.5794E+01  0.3569E+01         1.62           1 
    0   68    0     2.191   0.5885E+01  0.4251E+01         1.38           1 
    0   70    0     2.129   0.2635E+01  0.4980E+01         0.53           1 
    0   72    0     2.069   0.3582E+02  0.6908E+01         5.18           1 
    0   74    0     2.014  -0.4664E+01  0.4956E+01        -0.94           1 
    0   76    0     1.961   0.1616E+02  0.5684E+01         2.84           1 
    0   78    0     1.910   0.9010E+01  0.5145E+01         1.75           1 
   12    0    0     4.393   0.6099E+03  0.2887E+02        21.12           1 
   14    0    0     3.765   0.3848E+03  0.2048E+02        18.79           1 
   16    0    0     3.295   0.1872E+02  0.6139E+01         3.05           1 
   18    0    0     2.929   0.5363E+02  0.7211E+01         7.44           1 
   20    0    0     2.636   0.2129E+03  0.1378E+02        15.44           1 
   22    0    0     2.396   0.4943E+02  0.6776E+01         7.30           1 
   26    0    0     2.027   0.1465E+02  0.4900E+01         2.99           1 

 AVERAGE INTENSITY FOR      36 REFLECTIONS WHICH SHOULD
 BE SYSTEMATICALLY ABSENT IS     1.0% OF MEAN INTENSITY


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


 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  CC(1/2)  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     5.65        3886    1037      1051       98.7%       4.3%      4.2%     3834   24.38      5.0%    99.7*    -2    0.837     474
     4.01        7107    1761      1775       99.2%       4.4%      4.6%     7050   23.81      5.1%    99.7*    -3    0.743     936
     3.28        9089    2228      2247       99.2%       6.1%      6.0%     9035   18.94      7.0%    99.5*     0    0.841    1193
     2.84       11210    2628      2640       99.5%       9.7%      9.7%    11159   12.36     11.2%    99.1*    -1    0.826    1557
     2.54       11811    2932      2959       99.1%      15.5%     15.2%    11722    8.06     18.0%    96.6*    -2    0.812    1468
     2.32       13884    3250      3259       99.7%      21.8%     21.5%    13838    5.97     25.0%    95.2*    -2    0.806    1882
     2.15       14437    3530      3554       99.3%      29.6%     28.8%    14347    4.46     34.1%    90.8*    -3    0.799    1870
     2.01       15432    3750      3763       99.7%      42.5%     42.2%    15346    3.14     48.9%    81.2*    -1    0.799    2036
     1.90       16719    3969      4017       98.8%      58.2%     60.0%    16629    2.23     66.7%    71.9*     1    0.758    2246
    total      103575   25085     25265       99.3%      12.8%     12.8%   102960    8.82     14.7%    99.4*    -1    0.799   13662


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES    104430
 NUMBER OF REJECTED MISFITS                               819
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                   36
 NUMBER OF ACCEPTED OBSERVATIONS                       103575
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                  25085



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

   WILSON LINE (using all data) : A=   4.025 B=  23.633 CORRELATION=  0.96
      #      RES      SS        <I>       log(<I>)       BO
     371    10.577   0.002  3.9705E+01       3.681      76.9
     597     6.616   0.006  2.2421E+01       3.110      80.1
     748     5.183   0.009  3.2800E+01       3.490      28.7
     879     4.397   0.013  4.7775E+01       3.867       6.1
     981     3.882   0.017  4.0657E+01       3.705       9.7
    1082     3.516   0.020  3.2259E+01       3.474      13.6
    1158     3.237   0.024  2.4983E+01       3.218      16.9
    1245     3.016   0.027  1.5592E+01       2.747      23.3
    1319     2.835   0.031  1.1280E+01       2.423      25.8
    1400     2.682   0.035  9.0992E+00       2.208      26.1
    1455     2.552   0.038  7.7804E+00       2.052      25.7
    1535     2.439   0.042  6.3320E+00       1.846      25.9
    1602     2.340   0.046  6.0749E+00       1.804      24.3
    1657     2.251   0.049  5.4631E+00       1.698      23.6
    1702     2.172   0.053  4.5322E+00       1.511      23.7
    1776     2.101   0.057  3.8591E+00       1.350      23.6
    1819     2.037   0.060  3.3363E+00       1.205      23.4
    1869     1.978   0.064  2.7770E+00       1.021      23.5
    1890     1.924   0.068  2.3005E+00       0.833      23.6


 HIGHER ORDER MOMENTS OF WILSON DISTRIBUTION OF  CENTRIC DATA
    AS COMPARED WITH THEORETICAL VALUES. (EXPECTED: 1.00)    
      #      RES        <I**2>/      <I**3>/      <I**4>/  
                         3<I>**2     15<I>**3    105<I>**4 

     130    10.577        1.003        1.100        1.154
     131     6.616        1.086        1.032        0.832
     130     5.183        1.394        1.694        1.714
     138     4.397        1.210        1.066        0.803
     128     3.882        1.552        1.715        1.734
     129     3.516        1.208        1.251        1.183
     128     3.237        1.922        2.926        3.979
     137     3.016        1.432        2.650        4.610
     130     2.835        0.972        0.914        0.791
     135     2.682        0.830        0.643        0.450
     125     2.552        0.805        0.724        0.585
     138     2.439        0.767        0.627        0.508
     133     2.340        1.219        1.216        1.083
     132     2.251        1.238        1.510        1.683
     132     2.172        1.308        1.985        3.349
     138     2.101        0.782        0.686        0.594
     136     2.037        1.202        1.317        1.344
     129     1.978        1.048        1.198        1.308
     131     1.924        1.017        0.781        0.558
    2510   overall        1.156        1.315        1.486


 HIGHER ORDER MOMENTS OF WILSON DISTRIBUTION OF ACENTRIC DATA
    AS COMPARED WITH THEORETICAL VALUES. (EXPECTED: 1.00)    
      #      RES        <I**2>/      <I**3>/      <I**4>/  
                         2<I>**2      6<I>**3     24<I>**4 

     241    10.577        1.150        1.357        1.574
     466     6.616        0.878        0.747        0.612
     618     5.183        0.944        0.917        0.949
     741     4.397        0.923        0.864        0.779
     853     3.882        0.872        0.804        0.723
     953     3.516        0.957        0.941        0.903
    1030     3.237        0.909        0.825        0.721
    1108     3.016        1.004        1.070        1.210
    1189     2.835        1.004        1.026        1.053
    1265     2.682        0.941        0.834        0.688
    1330     2.552        1.010        0.983        0.904
    1397     2.439        1.050        1.254        1.729
    1469     2.340        0.980        0.962        0.909
    1525     2.251        0.998        1.040        1.146
    1570     2.172        0.993        1.012        1.048
    1638     2.101        1.019        1.005        0.987
    1683     2.037        1.000        0.977        0.956
    1740     1.978        1.040        1.079        1.170
    1759     1.924        1.021        0.956        0.865
   22575   overall        0.989        0.987        1.003

   ======= CUMULATIVE INTENSITY DISTRIBUTION =======
 DEFINITIONS:
   <I>    = mean reflection intensity
 Na(Z)exp = expected number of acentric reflections with I <= Z*<I>
 Na(Z)obs = observed number of acentric reflections with I <= Z*<I>
 Nc(Z)exp = expected number of  centric reflections with I <= Z*<I>
 Nc(Z)obs = observed number of  centric reflections with I <= Z*<I>



 Nc(Z)obs/Nc(Z)exp versus resolution and Z (0.1-1.0)
      #      RES     0.1   0.2   0.3   0.4   0.5   0.6   0.7   0.8   0.9   1.0

     130    10.577  0.84  1.07  1.09  1.06  1.06  1.06  1.08  1.06  1.04  1.04
     131     6.616  0.74  0.77  0.82  0.94  0.95  0.92  0.95  0.97  0.98  0.97
     130     5.183  0.68  0.67  0.83  0.93  0.98  1.01  1.06  1.04  1.05  1.06
     138     4.397  0.88  0.99  0.94  1.00  1.00  0.97  0.96  0.96  0.96  0.96
     128     3.882  0.50  0.61  0.69  0.79  0.75  0.84  0.84  0.82  0.86  0.84
     129     3.516  0.69  0.78  0.76  0.88  0.89  0.98  0.97  0.99  0.98  0.98
     128     3.237  0.91  1.04  1.07  1.12  1.16  1.13  1.11  1.08  1.08  1.09
     137     3.016  0.53  0.72  0.88  0.89  0.90  0.92  0.94  0.93  0.97  0.96
     130     2.835  0.81  0.98  1.03  1.01  0.96  0.95  0.97  0.95  0.96  0.99
     135     2.682  0.63  0.77  0.94  0.92  0.92  0.95  0.96  0.97  1.00  1.01
     125     2.552  0.61  0.86  0.96  1.05  1.04  1.03  1.03  1.08  1.06  1.07
     138     2.439  0.82  0.80  0.92  0.93  0.99  0.96  0.91  0.92  0.94  0.96
     133     2.340  0.82  0.83  0.99  1.05  1.00  0.96  0.97  0.98  0.97  0.98
     132     2.251  0.73  0.79  0.96  0.93  0.97  1.09  1.09  1.05  1.04  1.05
     132     2.172  0.58  0.61  0.65  0.72  0.80  0.82  0.90  0.93  0.92  0.90
     138     2.101  1.02  0.88  0.87  0.90  0.88  0.90  0.93  0.95  0.99  1.03
     136     2.037  1.01  0.79  0.76  0.79  0.83  0.93  0.91  0.91  0.95  0.95
     129     1.978  1.19  1.01  0.97  0.93  0.95  0.94  0.91  0.91  0.96  0.93
     131     1.924  0.61  0.57  0.55  0.58  0.62  0.63  0.72  0.78  0.81  0.85
    2510   overall  0.77  0.82  0.88  0.92  0.93  0.95  0.96  0.96  0.97  0.98


 Na(Z)obs/Na(Z)exp versus resolution and Z (0.1-1.0)
      #      RES     0.1   0.2   0.3   0.4   0.5   0.6   0.7   0.8   0.9   1.0

     241    10.577  0.78  0.82  0.93  1.01  1.10  1.09  1.06  1.05  1.05  1.04
     466     6.616  0.72  0.84  0.84  0.89  0.93  0.96  0.98  0.99  0.99  1.01
     618     5.183  0.87  0.87  0.94  1.03  1.04  1.04  1.04  1.04  1.03  1.02
     741     4.397  0.88  0.96  0.94  1.02  1.01  1.00  1.04  1.04  1.03  1.02
     853     3.882  0.62  0.89  1.02  1.02  1.02  1.04  1.02  1.02  1.01  1.02
     953     3.516  0.72  0.91  0.97  0.98  0.99  1.00  1.02  1.02  1.02  1.02
    1030     3.237  0.69  0.86  0.96  1.00  0.97  1.01  1.03  1.03  1.03  1.01
    1108     3.016  0.87  0.94  0.95  0.98  0.99  1.02  1.03  1.01  1.03  1.02
    1189     2.835  0.81  0.87  0.99  0.95  0.98  1.02  1.02  1.00  1.01  1.01
    1265     2.682  0.79  0.81  0.87  0.92  0.94  0.98  0.99  0.98  0.99  0.99
    1330     2.552  0.85  0.89  0.91  0.94  0.98  1.01  1.01  1.00  1.00  1.00
    1397     2.439  0.85  0.77  0.88  0.90  0.96  0.96  0.98  0.99  0.99  1.01
    1469     2.340  0.98  0.97  0.95  0.95  0.95  0.96  0.97  1.02  1.03  1.02
    1525     2.251  0.90  0.86  0.90  0.93  0.97  0.98  1.00  1.00  1.00  0.99
    1570     2.172  1.15  0.90  0.87  0.90  0.94  0.97  0.98  0.98  0.99  1.00
    1638     2.101  1.06  0.84  0.82  0.90  0.93  0.94  0.97  0.97  0.99  0.99
    1683     2.037  1.35  0.99  0.91  0.89  0.90  0.90  0.93  0.95  0.95  0.98
    1740     1.978  1.35  0.94  0.85  0.89  0.88  0.91  0.93  0.94  0.95  0.95
    1759     1.924  1.58  1.11  0.97  0.92  0.91  0.91  0.90  0.92  0.94  0.96
   22575   overall  1.00  0.91  0.91  0.94  0.95  0.97  0.98  0.99  0.99  1.00


 List of      1 reflections *NOT* obeying Wilson distribution (Z> 10.0)

   h    k    l     RES      Z     Intensity    Sigma

    1    1   33    2.41   11.41  0.1444E+03  0.3226E+01 "alien"


 List of      1 reflections *NOT* obeying Wilson distribution (sorted by resolution)
 Ice rings could occur at (Angstrom):
 3.897,3.669,3.441, 2.671,2.249,2.072, 1.948,1.918,1.883,1.721

   h    k    l     RES      Z     Intensity    Sigma

    1    1   33    2.41   11.41  0.1444E+03  0.3226E+01

 NUMBER OF UNIQUE ALIEN REFLECTIONS WITH A Z-SCORE ABOVE LIMIT         0
 (ALIENS ABOVE LIMIT (REJECT_ALIEN=      20.0) ARE MARKED INVALID)

 NUMBER OF REFLECTION RECORDS ON OUTPUT FILE "XDS_ASCII.HKL"      104430
 NUMBER OF ACCEPTED OBSERVATIONS (INCLUDING SYSTEMATIC ABSENCES)  103611
 NUMBER OF REJECTED MISFITS & ALIENS (marked by -1*SIGMA(IOBS))      819


 cpu time used                  9.5 sec
 elapsed wall-clock time        2.7 sec
