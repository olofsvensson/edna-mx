
 ***** CORRECT ***** (VERSION Jun 1, 2017  BUILT=20170615)  31-Aug-2017

 INPUT PARAMETER VALUES
 ----------------------
 SPACE_GROUP_NUMBER=    1 as used in the INTEGRATE step
 UNIT_CELL_CONSTANTS=    65.869   111.487   111.635  89.852  90.017  90.039 as used by INTEGRATE
 FRIEDEL'S_LAW=TRUE 
 PROFILE_FITTING= TRUE 
 OVERLOAD=   1048500     MINPK=  75.00000    WFAC1=   1.0
 INCLUDE_RESOLUTION_RANGE=    20.000     0.000
 NAME_TEMPLATE_OF_DATA_FRAMES=img/ref-FAE-x09_4_xdslink_?????.cbf CBF
 DATA_RANGE=       1       1
 ROTATION_AXIS=  1.000000  0.000000  0.000000
 OSCILLATION_RANGE=  1.000000
 STARTING_ANGLE=   359.500     STARTING_FRAME=       1
 X-RAY_WAVELENGTH=  0.966000
 INCIDENT_BEAM_DIRECTION=  0.002014 -0.001661  1.035193
 FRACTION_OF_POLARIZATION=   0.500
 POLARIZATION_PLANE_NORMAL=  0.000000  1.000000  0.000000
 AIR=   0.00030
 DETECTOR=PILATUS
 SILICON=  3.556632 SENSOR_THICKNESS=  0.320000
 NUMBER OF DETECTOR SEGMENTS   1
 NX=  1475  NY=  1679    QX=  0.172000  QY=  0.172000
 ORGX=    748.21  ORGY=    855.81
 DETECTOR_DISTANCE=   234.474
 DIRECTION_OF_DETECTOR_X-AXIS=   1.00000   0.00000   0.00000
 DIRECTION_OF_DETECTOR_Y-AXIS=   0.00000   1.00000   0.00000
 BEAM_DIVERGENCE_E.S.D.=   0.068
 REFLECTING_RANGE_E.S.D.=   0.515
 MINIMUM_ZETA=     0.050
 MAXIMUM_ERROR_OF_SPOT_POSITION=   3.0
 MAXIMUM_ERROR_OF_SPINDLE_POSITION=   2.0
 MINIMUM_I/SIGMA=   3.0
 REFLECTIONS/CORRECTION_FACTOR=      50
 STRICT_ABSORPTION_CORRECTION=FALSE 
 CORRECTIONS= DECAY MODULATION ABSORPTION                      
 REFERENCE_DATA_SET=                                                  
 FIT_B-FACTOR_TO_REFERENCE_DATA_SET=FALSE 

       7 REFLECTIONS ON FILE "INTEGRATE.HKL"
       0 CORRUPTED REFLECTION RECORDS (IGNORED)
       0 MATCHING REFLECTIONS SPECIFIED IN FILE "FILTER.HKL"
       0 REFLECTIONS INCOMPLETE OR OUTSIDE IMAGE RANGE       1 ...       1
       0 OVERLOADED REFLECTIONS (IGNORED)
       0 REFLECTIONS OUTSIDE ACCEPTED RESOLUTION RANGES
                OR TOO CLOSE TO ROTATION AXIS (IGNORED)
       7 REFLECTIONS ACCEPTED



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
 SPACE_GROUP_NUMBER=   75 (0: unknown symmetry and unit cell)
 UNIT_CELL_CONSTANTS=   111.55   111.55    65.90  90.000  90.000  90.000
 UNIT_CELL_A-AXIS=     0.000     0.000     0.000 (0 0 0 : unknown)
 UNIT_CELL_B-AXIS=     0.000     0.000     0.000 (0 0 0 : unknown)
 UNIT_CELL_C-AXIS=     0.000     0.000     0.000 (0 0 0 : unknown)
 REIDX=  0  0  0  0  0  0  0  0  0  0  0  0 (all 0 : not specified)
 TEST_RESOLUTION_RANGE=   10.00    5.00 (Angstrom) for space group determination
 NUMBER OF ACCEPTED REFLECTIONS FOR CALCULATING Rmeas                0
 NUMBER OF ACCEPTED UNIQUE REFLECTIONS FROM REFERENCE DATA SET       0


 !!! WARNING !!! NO REFLECTIONS TO COMPUTE Rmeas.
                 INCORRECT CHOICE OF TEST_RESOLUTION_RANGE= ?


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

 *  31        aP          0.0      65.9  111.5  111.6  89.9  90.0  90.0    1  0  0  0  0 -1  0  0  0  0 -1  0
 *  44        aP          0.2      65.9  111.5  111.6  90.1  90.0  90.0   -1  0  0  0  0 -1  0  0  0  0  1  0
 *  35        mP          1.0     111.5   65.9  111.6  90.0  90.1  90.0    0  1  0  0  1  0  0  0  0  0 -1  0
 *  20        mC          4.1     158.0  157.6   65.9  90.0  90.0  90.1    0 -1 -1  0  0 -1  1  0 -1  0  0  0
 *  34        mP          4.2      65.9  111.6  111.5  90.1  90.0  90.0    1  0  0  0  0  0 -1  0  0  1  0  0
 *  33        mP          4.5      65.9  111.5  111.6  90.1  90.0  90.0   -1  0  0  0  0 -1  0  0  0  0  1  0
 *  32        oP          4.8      65.9  111.5  111.6  90.1  90.0  90.0   -1  0  0  0  0 -1  0  0  0  0  1  0
 *  23        oC          4.9     157.6  158.0   65.9  90.0  90.0  89.9    0 -1  1  0  0  1  1  0 -1  0  0  0
 *  25        mC          4.9     157.6  158.0   65.9  90.0  90.0  89.9    0 -1  1  0  0  1  1  0 -1  0  0  0
 *  21        tP          8.6     111.5  111.6   65.9  90.0  90.0  90.1    0 -1  0  0  0  0  1  0 -1  0  0  0
    39        mC        249.9     232.5   65.9  111.6  90.0  90.1  73.6    1  2  0  0  1  0  0  0  0  0 -1  0
    37        mC        250.9     232.8   65.9  111.5  90.0  90.1  73.6   -1  0 -2  0 -1  0  0  0  0  1  0  0
    29        mC        253.0      65.9  232.5  111.6  89.9  90.0  73.6    1  0  0  0  1  2  0  0  0  0  1  0
    28        mC        253.2      65.9  232.8  111.5  89.9  90.0  73.6   -1  0  0  0 -1  0 -2  0  0 -1  0  0
    38        oC        253.6      65.9  232.5  111.6  89.9  90.0 106.4    1  0  0  0 -1 -2  0  0  0  0 -1  0
    36        oC        254.6      65.9  232.8  111.5  89.9  90.0 106.4   -1  0  0  0  1  0  2  0  0  1  0  0
    27        mC        499.2     232.5   65.9  157.6  90.0 132.6  73.6   -1 -2  0  0 -1  0  0  0  0  1 -1  0
    19        oI        503.0      65.9  157.6  171.1  89.9  67.4  90.0   -1  0  0  0  0  1 -1  0 -1 -1 -1  0
    26        oF        620.5      65.9  232.5  232.8  85.3 106.4 106.4    1  0  0  0 -1 -2  0  0 -1  0 -2  0
    18        tI        624.3     157.6  171.1   65.9  67.4  90.0  90.1    0  1 -1  0  1  1  1  0  1  0  0  0
    30        mC        712.5     111.5  249.3   65.9  90.0  90.0  63.6    0 -1  0  0  0 -1  2  0 -1  0  0  0
    41        mC        713.3     249.3  111.5   65.9  90.0  90.0  63.6    0  1 -2  0  0  1  0  0  1  0  0  0
    40        oC        713.5     111.5  249.3   65.9  90.0  90.0 116.4    0  1  0  0  0 -1  2  0  1  0  0  0
    22        hP        717.3     111.5  111.6   65.9  90.0  90.0  90.1    0 -1  0  0  0  0  1  0 -1  0  0  0
    10        mC        935.8     129.5  129.5  111.6  89.9  90.1 118.8    1 -1  0  0  1  1  0  0  0  0  1  0
    14        mC        936.4     129.5  129.5  111.6  90.1  90.1  61.2   -1  1  0  0  1  1  0  0  0  0 -1  0
    13        oC        936.6     129.5  129.5  111.6  90.1  90.1  61.2   -1 -1  0  0  1 -1  0  0  0  0  1  0
    11        tP        937.1      65.9  111.5  111.6  90.1  90.0  90.0   -1  0  0  0  0 -1  0  0  0  0  1  0
     2        hR        940.0     129.5  129.6  171.2 111.6  68.5 105.1    1  1  0  0 -1  0 -1  0 -1  1  1  0
     4        hR        941.0     129.5  129.6  170.8 111.4  68.6 104.9   -1 -1  0  0  1  0 -1  0  1 -1  1  0
     3        cP        944.7      65.9  111.5  111.6  90.1  90.0  90.0   -1  0  0  0  0  1  0  0  0  0 -1  0
    42        oI        963.4      65.9  111.5  257.9 115.5 104.8  90.0    1  0  0  0  0 -1  0  0 -1  1 -2  0
     1        cF        999.0     170.8  170.8  171.1  98.6  98.5 134.6    1  1 -1  0  1 -1  1  0 -1 -1 -1  0
     5        cI        999.0     129.6  129.5  157.6  52.6  52.5  75.1   -1  0 -1  0 -1  1  0  0  0  1 -1  0
     6        tI        999.0     157.6  129.6  129.5  75.1  52.6  52.5    0 -1  1  0 -1  0  1  0 -1 -1  0  0
     7        tI        999.0     129.6  129.5  157.6  52.6  52.5  75.1   -1  0  1  0 -1 -1  0  0  0 -1  1  0
     8        oI        999.0     129.5  129.6  157.6  52.5  52.6  75.1    1  1  0  0  1  0 -1  0  0  1 -1  0
     9        hR        999.0      65.9  129.5  358.8  99.9 100.6 120.5    1  0  0  0 -1 -1  0  0 -1  1 -3  0
    12        hP        999.0      65.9  111.5  111.6  90.1  90.0  90.0   -1  0  0  0  0 -1  0  0  0  0  1  0
    15        tI        999.0      65.9  111.5  257.9  64.5  75.2  90.0   -1  0  0  0  0  1  0  0 -1  1 -2  0
    16        oF        999.0     129.5  129.5  257.8 103.9 120.0  61.2    1  1  0  0 -1  1  0  0 -1 -1  2  0
    17        mC        999.0     129.5  129.5  129.6  75.1 105.1  61.2   -1  1  0  0  1  1  0  0  1  0 -1  0
    24        hR        999.0     257.6  158.0   65.9  90.0  75.2 107.8   -1 -2  1  0  0  1  1  0 -1  0  0  0
    43        mI        999.0     129.5  257.8  111.5 115.5 149.4  60.0   -1 -1  0  0 -1 -1  2  0  0  1  0  0

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

  *   0.00        0    0.0       0    0.00  0  0  1  0  0 -1  0  0  1  0  0  0
      0.00        0    0.0       0    0.00  0  1  0  0  0  0 -1  0 -1  0  0  0

 ************ SELECTED SPACE GROUP AND UNIT CELL FOR THIS DATA SET ************

 SPACE_GROUP_NUMBER=   75
 UNIT_CELL_CONSTANTS=   111.55   111.55    65.90  90.000  90.000  90.000
 UNIT_CELL_A-AXIS=    26.886   -90.478    59.608
 UNIT_CELL_B-AXIS=   -18.265    56.924    94.102
 UNIT_CELL_C-AXIS=   -63.031   -19.115    -0.619
 REFLECTIONS H,K,L FROM "INTEGRATE.HKL" WILL BE REINDEXED BY
 H' = (  0*H +  0*K +  1*L)/ 1 +  0
 K' = (  0*H + -1*K +  0*L)/ 1 +  0
 L' = (  1*H +  0*K +  0*L)/ 1 +  0

 *****  4 EQUIVALENT POSITIONS IN SPACE GROUP # 75 *****

    If x',y',z' is an equivalent position to x,y,z, then
        x'=x*ML(1)+y*ML( 2)+z*ML( 3)+ML( 4)/12.0
        y'=x*ML(5)+y*ML( 6)+z*ML( 7)+ML( 8)/12.0
        z'=x*ML(9)+y*ML(10)+z*ML(11)+ML(12)/12.0

    #    1  2  3  4    5  6  7  8    9 10 11 12 
    1    1  0  0  0    0  1  0  0    0  0  1  0
    2   -1  0  0  0    0 -1  0  0    0  0  1  0
    3    0  1  0  0   -1  0  0  0    0  0  1  0
    4    0 -1  0  0    1  0  0  0    0  0  1  0

 ******************************************************************************
      MEAN DISCREPANCIES BETWEEN OBSERVED AND CALCULATED SPOT LOCATIONS
 ******************************************************************************

 The discrepancies in X- and Y-coordinates of the spots are depicted in the
 two images DX-CORRECTIONS.cbf and DY-CORRECTIONS.cbf for inspection with
 the XDS-Viewer.



 ******************************************************************************
  REFINEMENT OF DIFFRACTION PARAMETERS USING ALL IMAGES
 ******************************************************************************


 !!! WARNING !!! REFINEMENT RESULTS NOT ACCEPTED BECAUSE OF INSUFFICIENT
 NUMBER OF REFLECTIONS.


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
  0.45  0.55         5         13.335       1.283
  0.55  0.65         1         74.963       0.228
 
 -0.05  0.95         7         17.113       1.000
 

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
 4.000E+00  1.000E-04   50.00


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

    3.623   0.964     0.17   0.00    -99.90    -99.90       0       7       0
   --------------------------------------------------------------------------
    3.623   2.821     0.17   0.00    -99.90    -99.90       0       7       0
 


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
  STATISTICS OF SAVED DATA SET "XDS_ASCII.HKL" (DATA_RANGE=       1       1)
 FILE TYPE:         XDS_ASCII      MERGE=FALSE          FRIEDEL'S_LAW=TRUE 
 ******************************************************************************

   REFLECTIONS OF TYPE H,0,0  0,K,0  0,0,L OR EXPECTED TO BE ABSENT (*)
   --------------------------------------------------------------------

   H    K    L  RESOLUTION  INTENSITY     SIGMA    INTENSITY/SIGMA  #OBSERVED


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

     3.50           1       1     10428        0.0%     -99.9%    -99.9%        0    0.00    -99.9%     0.0      0    0.000       0
     3.39           1       1      1059        0.1%     -99.9%    -99.9%        0    0.00    -99.9%     0.0      0    0.000       0
     3.28           1       1      1078        0.1%     -99.9%    -99.9%        0    0.00    -99.9%     0.0      0    0.000       0
     3.19           1       1      1139        0.1%     -99.9%    -99.9%        0    0.00    -99.9%     0.0      0    0.000       0
     3.11           0       0      1138        0.0%     -99.9%    -99.9%        0    0.00    -99.9%     0.0      0    0.000       0
     3.03           0       0      1185        0.0%     -99.9%    -99.9%        0    0.00    -99.9%     0.0      0    0.000       0
     2.95           0       0      1219        0.0%     -99.9%    -99.9%        0    0.00    -99.9%     0.0      0    0.000       0
     2.89           2       2      1252        0.2%     -99.9%    -99.9%        0    0.00    -99.9%     0.0      0    0.000       0
     2.82           1       1      1252        0.1%     -99.9%    -99.9%        0    0.00    -99.9%     0.0      0    0.000       0
    total           7       7     19750        0.0%     -99.9%    -99.9%        0    0.00    -99.9%     0.0      0    0.000       0


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES         7
 NUMBER OF REJECTED MISFITS                                 0
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                    0
 NUMBER OF ACCEPTED OBSERVATIONS                            7
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                      7



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

   WILSON LINE (using all data) : A=   3.421 B=   7.475 CORRELATION=  0.06
      #      RES      SS        <I>       log(<I>)       BO
       1     3.472   0.021  7.4963E+01       4.317     -21.6
       1     3.381   0.022  7.0687E+00       1.956      33.5
       1     3.283   0.023  1.8273E+01       2.905      11.1
       1     2.944   0.029  1.0304E+01       2.332      18.9
       1     2.886   0.030  4.1619E+01       3.729      -5.1
       1     2.821   0.031 -1.0592E+01    -999.999   -1000.0


 HIGHER ORDER MOMENTS OF WILSON DISTRIBUTION OF  CENTRIC DATA
    AS COMPARED WITH THEORETICAL VALUES. (EXPECTED: 1.00)    
      #      RES        <I**2>/      <I**3>/      <I**4>/  
                         3<I>**2     15<I>**3    105<I>**4 

       0   overall        0.000        0.000        0.000


 HIGHER ORDER MOMENTS OF WILSON DISTRIBUTION OF ACENTRIC DATA
    AS COMPARED WITH THEORETICAL VALUES. (EXPECTED: 1.00)    
      #      RES        <I**2>/      <I**3>/      <I**4>/  
                         2<I>**2      6<I>**3     24<I>**4 

       1     3.472        0.500        0.167        0.042
       1     3.381        0.500        0.167        0.042
       1     3.283        0.500        0.167        0.042
       1     2.944        0.500        0.167        0.042
       1     2.886        0.500        0.167        0.042
       6   overall        0.417        0.139        0.035

   ======= CUMULATIVE INTENSITY DISTRIBUTION =======
 DEFINITIONS:
   <I>    = mean reflection intensity
 Na(Z)exp = expected number of acentric reflections with I <= Z*<I>
 Na(Z)obs = observed number of acentric reflections with I <= Z*<I>
 Nc(Z)exp = expected number of  centric reflections with I <= Z*<I>
 Nc(Z)obs = observed number of  centric reflections with I <= Z*<I>



 Nc(Z)obs/Nc(Z)exp versus resolution and Z (0.1-1.0)
      #      RES     0.1   0.2   0.3   0.4   0.5   0.6   0.7   0.8   0.9   1.0

       0   overall  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00


 Na(Z)obs/Na(Z)exp versus resolution and Z (0.1-1.0)
      #      RES     0.1   0.2   0.3   0.4   0.5   0.6   0.7   0.8   0.9   1.0

       1     3.472  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  1.58
       1     3.381  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  1.58
       1     3.283  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  1.58
       1     2.944  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  1.58
       1     2.886  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  1.58
       6   overall  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  1.32

 NUMBER OF UNIQUE ALIEN REFLECTIONS WITH A Z-SCORE ABOVE LIMIT         0
 (ALIENS ABOVE LIMIT (REJECT_ALIEN=      20.0) ARE MARKED INVALID)

 NUMBER OF REFLECTION RECORDS ON OUTPUT FILE "XDS_ASCII.HKL"           7
 NUMBER OF ACCEPTED OBSERVATIONS (INCLUDING SYSTEMATIC ABSENCES)       7
 NUMBER OF REJECTED MISFITS & ALIENS (marked by -1*SIGMA(IOBS))        0


 cpu time used                  0.0 sec
 elapsed wall-clock time        0.0 sec
