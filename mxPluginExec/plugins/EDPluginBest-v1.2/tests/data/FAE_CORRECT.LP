
 ***** CORRECT ***** (VERSION Jun 1, 2017  BUILT=20170615)   1-Sep-2017

 INPUT PARAMETER VALUES
 ----------------------
 SPACE_GROUP_NUMBER=    1 as used in the INTEGRATE step
 UNIT_CELL_CONSTANTS=    65.499   110.683   110.981  90.045  89.970  89.952 as used by INTEGRATE
 FRIEDEL'S_LAW=TRUE 
 PROFILE_FITTING= TRUE 
 OVERLOAD=   1048500     MINPK=  75.00000    WFAC1=   1.0
 INCLUDE_RESOLUTION_RANGE=    20.000     0.000
 NAME_TEMPLATE_OF_DATA_FRAMES=img/ref-FAE-x09_4_xdslink_?????.img CBF
 DATA_RANGE=       1       1
 ROTATION_AXIS=  1.000000  0.000000  0.000000
 OSCILLATION_RANGE=  1.000000
 STARTING_ANGLE=   359.500     STARTING_FRAME=       1
 X-RAY_WAVELENGTH=  0.966000
 INCIDENT_BEAM_DIRECTION=  0.003212 -0.001436  1.035191
 FRACTION_OF_POLARIZATION=   0.500
 POLARIZATION_PLANE_NORMAL=  0.000000  1.000000  0.000000
 AIR=   0.00030
 DETECTOR=PILATUS
 SILICON=  3.556632 SENSOR_THICKNESS=  0.000000
 NUMBER OF DETECTOR SEGMENTS   1
 NX=  1475  NY=  1679    QX=  0.172000  QY=  0.172000
 ORGX=    746.80  ORGY=    855.57
 DETECTOR_DISTANCE=   233.035
 DIRECTION_OF_DETECTOR_X-AXIS=   1.00000   0.00000   0.00000
 DIRECTION_OF_DETECTOR_Y-AXIS=   0.00000   1.00000   0.00000
 BEAM_DIVERGENCE_E.S.D.=   0.026
 REFLECTING_RANGE_E.S.D.=   0.148
 MINIMUM_ZETA=     0.050
 MAXIMUM_ERROR_OF_SPOT_POSITION=   3.0
 MAXIMUM_ERROR_OF_SPINDLE_POSITION=   2.0
 MINIMUM_I/SIGMA=   3.0
 REFLECTIONS/CORRECTION_FACTOR=      50
 STRICT_ABSORPTION_CORRECTION=FALSE 
 CORRECTIONS= DECAY MODULATION ABSORPTION                      
 REFERENCE_DATA_SET=                                                  
 FIT_B-FACTOR_TO_REFERENCE_DATA_SET=FALSE 

    2012 REFLECTIONS ON FILE "INTEGRATE.HKL"
       0 CORRUPTED REFLECTION RECORDS (IGNORED)
       0 MATCHING REFLECTIONS SPECIFIED IN FILE "FILTER.HKL"
       0 REFLECTIONS INCOMPLETE OR OUTSIDE IMAGE RANGE       1 ...       1
       0 OVERLOADED REFLECTIONS (IGNORED)
       0 REFLECTIONS OUTSIDE ACCEPTED RESOLUTION RANGES
                OR TOO CLOSE TO ROTATION AXIS (IGNORED)
    2012 REFLECTIONS ACCEPTED



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
 UNIT_CELL_CONSTANTS=   110.85   110.85    65.50  90.000  90.000  90.000
 UNIT_CELL_A-AXIS=     0.000     0.000     0.000 (0 0 0 : unknown)
 UNIT_CELL_B-AXIS=     0.000     0.000     0.000 (0 0 0 : unknown)
 UNIT_CELL_C-AXIS=     0.000     0.000     0.000 (0 0 0 : unknown)
 REIDX=  0  0  0  0  0  0  0  0  0  0  0  0 (all 0 : not specified)
 TEST_RESOLUTION_RANGE=   10.00    5.00 (Angstrom) for space group determination
 NUMBER OF ACCEPTED REFLECTIONS FOR CALCULATING Rmeas               80
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

 *  44        aP          0.0      65.4  110.3  110.7  90.3  90.0  90.0    1  0  0  0  0  1  0  0  0  0  1  0
 *  31        aP          0.5      65.4  110.3  110.7  89.7  90.0  90.0   -1  0  0  0  0  1  0  0  0  0 -1  0
 *  35        mP          1.1     110.3   65.4  110.7  90.0  90.3  90.0    0 -1  0  0 -1  0  0  0  0  0 -1  0
 *  34        mP          7.8      65.4  110.7  110.3  90.3  90.0  90.0   -1  0  0  0  0  0 -1  0  0 -1  0  0
 *  33        mP          7.9      65.4  110.3  110.7  90.3  90.0  90.0    1  0  0  0  0  1  0  0  0  0  1  0
 *  32        oP          8.4      65.4  110.3  110.7  90.3  90.0  90.0    1  0  0  0  0  1  0  0  0  0  1  0
 *  25        mC         11.8     155.9  156.7   65.4  90.0  90.1  89.8    0  1  1  0  0 -1  1  0  1  0  0  0
 *  23        oC         12.8     155.9  156.7   65.4  90.0  90.1  89.8    0  1  1  0  0 -1  1  0  1  0  0  0
 *  20        mC         13.3     156.7  155.9   65.4  90.1  90.0  90.2    0  1 -1  0  0  1  1  0  1  0  0  0
 *  21        tP         20.1     110.3  110.7   65.4  90.0  90.0  90.3    0  1  0  0  0  0  1  0  1  0  0  0
    39        mC        249.9     230.0   65.4  110.7  90.0  90.3  73.5   -1 -2  0  0 -1  0  0  0  0  0 -1  0
    37        mC        250.1     230.9   65.4  110.3  90.0  90.3  73.6    1  0  2  0  1  0  0  0  0  1  0  0
    38        oC        257.2      65.4  230.0  110.7  89.7  90.0 106.5   -1  0  0  0  1  2  0  0  0  0 -1  0
    36        oC        257.4      65.4  230.9  110.3  89.7  90.0 106.4    1  0  0  0 -1  0 -2  0  0  1  0  0
    29        mC        257.4      65.4  230.0  110.7  89.7  90.0  73.5   -1  0  0  0 -1 -2  0  0  0  0  1  0
    28        mC        257.7      65.4  230.9  110.3  89.7  90.0  73.6    1  0  0  0  1  0  2  0  0 -1  0  0
    27        mC        500.4     230.0   65.4  155.9  89.9 132.4  73.5    1  2  0  0  1  0  0  0  0 -1 -1  0
    19        oI        512.1      65.4  155.9  169.8  89.8  67.3  89.9    1  0  0  0  0 -1 -1  0  1  1 -1  0
    26        oF        618.2      65.4  230.0  231.0  85.1 106.5 106.5   -1  0  0  0  1  2  0  0  1  0 -2  0
    18        tI        629.8     155.9  169.8   65.4  67.3  90.1  90.2    0 -1 -1  0 -1 -1  1  0 -1  0  0  0
    41        mC        703.5     246.9  110.3   65.4  90.0  90.1  63.8    0 -1 -2  0  0 -1  0  0 -1  0  0  0
    40        oC        704.1     110.3  246.9   65.4  89.9  90.0 116.2    0 -1  0  0  0  1  2  0 -1  0  0  0
    30        mC        704.3     110.3  246.9   65.4  90.1  90.0  63.8    0  1  0  0  0  1  2  0  1  0  0  0
    22        hP        715.7     110.3  110.7   65.4  90.0  90.0  90.3    0  1  0  0  0  0  1  0  1  0  0  0
    14        mC        927.1     128.2  128.3  110.7  90.2  90.3  61.4    1  1  0  0 -1  1  0  0  0  0  1  0
    10        mC        927.7     128.2  128.3  110.7  89.8  90.3 118.6   -1 -1  0  0 -1  1  0  0  0  0 -1  0
    13        oC        928.2     128.2  128.3  110.7  90.2  90.3  61.4    1  1  0  0 -1  1  0  0  0  0  1  0
    11        tP        928.8      65.4  110.3  110.7  90.3  90.0  90.0    1  0  0  0  0  1  0  0  0  0  1  0
     4        hR        938.9     128.3  128.7  169.0 111.4  68.8 104.8    1 -1  0  0 -1  0  1  0 -1 -1 -1  0
     2        hR        940.6     128.3  128.6  169.8 111.6  68.6 105.3   -1  1  0  0  1  0  1  0  1  1 -1  0
     3        cP        946.1      65.4  110.3  110.7  90.3  90.0  90.0    1  0  0  0  0  1  0  0  0  0  1  0
    42        oI        953.0      65.4  110.3  255.4 115.3 104.8  90.0   -1  0  0  0  0 -1  0  0  1  1  2  0
     1        cF        999.0     169.1  169.0  169.8  98.8  98.4 134.5   -1  1  1  0 -1 -1 -1  0  1 -1  1  0
     5        cI        999.0     128.6  128.2  155.9  52.8  52.5  75.2    1  0  1  0  1  1  0  0  0  1  1  0
     6        tI        999.0     155.9  128.6  128.2  75.2  52.8  52.5    0  1  1  0  1  0  1  0  1  1  0  0
     7        tI        999.0     128.6  128.2  155.9  52.8  52.5  75.2    1  0  1  0  1  1  0  0  0  1  1  0
     8        oI        999.0     128.2  128.6  155.9  52.5  52.8  75.2   -1 -1  0  0 -1  0 -1  0  0 -1 -1  0
     9        hR        999.0      65.4  128.2  355.6  99.7 100.6 120.7   -1  0  0  0  1  1  0  0  1 -1 -3  0
    12        hP        999.0      65.4  110.3  110.7  90.3  90.0  90.0    1  0  0  0  0  1  0  0  0  0  1  0
    15        tI        999.0      65.4  110.3  255.4  64.7  75.2  90.0    1  0  0  0  0  1  0  0  1  1  2  0
    16        oF        999.0     128.2  128.3  255.4 103.7 119.9  61.4   -1 -1  0  0  1 -1  0  0  1  1  2  0
    17        mC        999.0     128.3  128.2  128.6  75.2 105.3  61.4    1 -1  0  0 -1 -1  0  0 -1  0 -1  0
    24        hR        999.0     254.8  156.7   65.4  90.0  75.2 107.7    1  2  1  0  0 -1  1  0  1  0  0  0
    43        mI        999.0     128.2  255.4  110.3 115.3 149.3  60.1    1  1  0  0  1  1  2  0  0 -1  0  0

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

  *   0.00        0    0.0       0    0.00  0 -1  0  0  0  0 -1  0  1  0  0  0
      0.00        0    0.0       0    0.00  0  1  0  0  0  0 -1  0 -1  0  0  0

 ************ SELECTED SPACE GROUP AND UNIT CELL FOR THIS DATA SET ************

 SPACE_GROUP_NUMBER=   75
 UNIT_CELL_CONSTANTS=   110.85   110.85    65.50  90.000  90.000  90.000
 UNIT_CELL_A-AXIS=    18.592   -56.619   -92.794
 UNIT_CELL_B-AXIS=    -4.985    94.285   -57.857
 UNIT_CELL_C-AXIS=    64.436     8.253     7.818
 REFLECTIONS H,K,L FROM "INTEGRATE.HKL" WILL BE REINDEXED BY
 H' = (  0*H + -1*K +  0*L)/ 1 +  0
 K' = (  0*H +  0*K + -1*L)/ 1 +  0
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


 REFINED VALUES OF DIFFRACTION PARAMETERS DERIVED FROM       404 INDEXED SPOTS
 REFINED PARAMETERS:   POSITION BEAM  ORIENTATION CELL
 STANDARD DEVIATION OF SPOT    POSITION (PIXELS)     0.29
 STANDARD DEVIATION OF SPINDLE POSITION (DEGREES)    0.10
 SPACE GROUP NUMBER     75
 UNIT CELL PARAMETERS    111.253   111.253    65.678  90.000  90.000  90.000
 E.S.D. OF CELL PARAMETERS  3.5E-01 3.5E-01 2.3E-01 0.0E+00 0.0E+00 0.0E+00
 REC. CELL PARAMETERS   0.008989  0.008989  0.015226  90.000  90.000  90.000
 COORDINATES OF UNIT CELL A-AXIS    18.684   -56.869   -93.776
 COORDINATES OF UNIT CELL B-AXIS    -5.026    94.584   -58.360
 COORDINATES OF UNIT CELL C-AXIS    64.677     8.287     7.861
 CRYSTAL MOSAICITY (DEGREES)     0.148
 LAB COORDINATES OF ROTATION AXIS  1.000000  0.000000  0.000000
 DIRECT BEAM COORDINATES (REC. ANGSTROEM)   0.003534 -0.001459  1.035190
 DETECTOR COORDINATES (PIXELS) OF DIRECT BEAM     751.04    853.59
 DETECTOR ORIGIN (PIXELS) AT                      746.40    855.51
 CRYSTAL TO DETECTOR DISTANCE (mm)       233.76
 LAB COORDINATES OF DETECTOR X-AXIS  1.000000  0.000000  0.000000
 LAB COORDINATES OF DETECTOR Y-AXIS  0.000000  1.000000  0.000000


 THE DATA COLLECTION STATISTICS REPORTED BELOW ASSUMES:
 SPACE_GROUP_NUMBER=   75
 UNIT_CELL_CONSTANTS=   111.25   111.25    65.68  90.000  90.000  90.000


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
  0.05  0.15        59         94.490       0.768
  0.15  0.25       219         79.293       0.915
  0.25  0.35       298         81.089       0.895
  0.35  0.45       264         78.061       0.929
  0.45  0.55       287         57.338       1.265
  0.55  0.65       277         78.026       0.930
  0.65  0.75       287         83.917       0.864
  0.75  0.85       231         47.596       1.524
  0.85  0.95        90         56.491       1.284
 
 -0.05  0.95      2012         72.537       1.000
 

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

   16.435   5.137    20.30   1.38      3.18      2.17       2      89       0
    5.137   3.724    13.08   0.00    -99.90    -99.90       0     149       0
    3.724   3.067     6.06   0.02     26.23    148.20       2     187       0
    3.067   2.668     2.39   0.17     29.70     57.09       2     185       0
    2.668   2.393     1.05   0.28     39.99     59.95       4     236       0
    2.393   2.188     0.56   0.18     55.27    103.16       2     259       0
    2.188   2.028     0.29   0.11    156.62    473.10       4     236       0
    2.028   1.899     0.14   0.11    -99.90    -99.90       4     271       0
    1.899   1.792     0.07   0.00    -99.90    -99.90       0     300       0
    1.792   1.701    -0.05   0.00    -99.90    -99.90       0     100       0
   --------------------------------------------------------------------------
   16.435   1.701     2.91   0.27     18.85     40.73      20    2012       0
 


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

     4.90         107     106      3836        2.8%       3.2%      2.2%        2   19.39      4.5%     0.0      0    0.000       0
     3.54         177     177      6152        2.9%     -99.9%    -99.9%        0    0.00    -99.9%     0.0      0    0.000       0
     2.91         200     199      7794        2.6%      26.2%    148.2%        2    4.83     37.1%     0.0      0    0.000       0
     2.53         242     240      9122        2.6%      23.6%     38.5%        4    1.63     33.3%     0.0      0    0.000       0
     2.27         261     259     10308        2.5%     139.2%    241.1%        4    0.74    196.9%     0.0      0    0.000       0
     2.08         268     268     11404        2.4%     -99.9%    -99.9%        0    0.00    -99.9%     0.0      0    0.000       0
     1.93         294     290     12305        2.4%     -99.9%    -99.9%        8    0.00    -99.9%     3.9      0    0.000       0
     1.80         325     325     13257        2.5%     -99.9%    -99.9%        0    0.00    -99.9%     0.0      0    0.000       0
     1.70         138     138     14029        1.0%     -99.9%    -99.9%        0    0.00    -99.9%     0.0      0    0.000       0
    total        2012    2002     88207        2.3%      18.8%     40.7%       20    2.91     26.7%    98.7*     0    0.000       0


 NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES      2012
 NUMBER OF REJECTED MISFITS                                 0
 NUMBER OF SYSTEMATIC ABSENT REFLECTIONS                    0
 NUMBER OF ACCEPTED OBSERVATIONS                         2012
 NUMBER OF UNIQUE ACCEPTED REFLECTIONS                   2002



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

   WILSON LINE (using all data) : A=   7.129 B=  49.137 CORRELATION=  0.93
      #      RES      SS        <I>       log(<I>)       BO
      43     8.754   0.003  4.8238E+02       6.179     145.7
      51     5.677   0.008  3.6345E+02       5.896      79.5
      81     4.562   0.012  3.3633E+02       5.818      54.6
      78     3.877   0.017  3.4068E+02       5.831      39.0
      97     3.451   0.021  1.9728E+02       5.285      43.9
      93     3.135   0.025  1.2063E+02       4.793      45.9
     109     2.881   0.030  6.1414E+01       4.118      50.0
     107     2.678   0.035  4.1005E+01       3.714      49.0
     125     2.529   0.039  2.2465E+01       3.112      51.4
     125     2.390   0.044  1.6351E+01       2.794      49.5
     132     2.279   0.048  1.6333E+01       2.793      45.0
     136     2.181   0.053  8.2735E+00       2.113      47.7
     116     2.089   0.057  7.5841E+00       2.026      44.5
     136     2.013   0.062  4.2973E+00       1.458      46.0
     139     1.944   0.066  4.3703E+00       1.475      42.8
     169     1.881   0.071  4.1359E+00       1.420      40.4
     148     1.824   0.075  1.1305E+00       0.123      46.6
      91     1.775   0.079  2.1962E-02      -3.818      69.0
      26     1.731   0.083 -3.3415E+00    -999.999   -1000.0


 HIGHER ORDER MOMENTS OF WILSON DISTRIBUTION OF  CENTRIC DATA
    AS COMPARED WITH THEORETICAL VALUES. (EXPECTED: 1.00)    
      #      RES        <I**2>/      <I**3>/      <I**4>/  
                         3<I>**2     15<I>**3    105<I>**4 

       6     8.754        0.256        0.103        0.031
       3     5.677        0.646        0.296        0.100
       5     4.562        0.547        0.266        0.099
       4     3.877        0.326        0.092        0.019
       4     3.451        3.987        4.922        4.533
       3     3.135        0.803        0.381        0.135
       2     2.678        0.047        0.005        0.000
       3     2.529        1.117        0.689        0.309
       3     2.390        1.604        0.772        0.390
       2     2.279        0.490        0.144        0.032
       1     2.181       17.558       25.485       26.423
       4     2.089        2.357        1.629        1.031
       4     1.944        2.814        0.933        1.167
       4     1.824       53.722      144.047      535.287
       2     1.775     2422.970     5143.664   506678.294
      60   overall       85.949      182.052    16926.128


 HIGHER ORDER MOMENTS OF WILSON DISTRIBUTION OF ACENTRIC DATA
    AS COMPARED WITH THEORETICAL VALUES. (EXPECTED: 1.00)    
      #      RES        <I**2>/      <I**3>/      <I**4>/  
                         2<I>**2      6<I>**3     24<I>**4 

      37     8.754        1.069        0.865        0.579
      48     5.677        0.817        0.570        0.343
      76     4.562        1.031        1.066        1.064
      74     3.877        1.016        0.959        0.827
      93     3.451        0.800        0.600        0.398
      90     3.135        0.969        0.907        0.780
     106     2.881        1.146        1.305        1.448
     105     2.678        1.093        1.226        1.481
     122     2.529        0.947        0.698        0.456
     122     2.390        1.094        0.921        0.716
     130     2.279        1.191        1.209        1.231
     135     2.181        1.856        1.723        1.805
     112     2.089        2.515        2.654        4.348
     132     2.013        5.613        4.659       14.302
     135     1.944        6.984        6.455       21.327
     166     1.881        7.827       11.293       37.773
     144     1.824       73.783      124.840     2865.790
      89     1.775   158063.998 -3862889.818*************
    1942   overall     7251.735  -177020.780572156432.588

   ======= CUMULATIVE INTENSITY DISTRIBUTION =======
 DEFINITIONS:
   <I>    = mean reflection intensity
 Na(Z)exp = expected number of acentric reflections with I <= Z*<I>
 Na(Z)obs = observed number of acentric reflections with I <= Z*<I>
 Nc(Z)exp = expected number of  centric reflections with I <= Z*<I>
 Nc(Z)obs = observed number of  centric reflections with I <= Z*<I>



 Nc(Z)obs/Nc(Z)exp versus resolution and Z (0.1-1.0)
      #      RES     0.1   0.2   0.3   0.4   0.5   0.6   0.7   0.8   0.9   1.0

       6     8.754  1.34  1.45  1.20  1.76  1.60  1.48  1.40  1.33  1.27  1.22
       3     5.677  0.00  0.00  0.80  1.41  1.28  1.19  1.12  1.06  1.01  0.98
       5     4.562  0.81  0.58  0.96  0.85  1.15  1.07  1.00  0.95  0.91  1.17
       4     3.877  1.01  0.72  0.60  1.06  0.96  0.89  0.84  0.80  0.76  0.73
       4     3.451  2.01  1.45  1.20  1.06  0.96  0.89  0.84  0.80  0.76  0.73
       3     3.135  0.00  0.96  0.80  0.70  0.64  0.59  0.56  0.53  1.01  0.98
       2     2.678  2.01  1.45  1.20  1.06  0.96  1.78  1.67  1.59  1.52  1.47
       3     2.529  1.34  0.96  0.80  1.41  1.28  1.19  1.12  1.06  1.01  0.98
       3     2.390  1.34  0.96  0.80  0.70  0.64  0.59  0.56  0.53  0.51  0.49
       2     2.279  0.00  0.00  0.00  0.00  0.00  0.00  0.84  0.80  0.76  0.73
       1     2.181  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00
       4     2.089  1.01  0.72  0.60  0.53  0.48  0.45  0.42  0.40  0.38  0.37
       4     1.944  1.01  0.72  0.60  0.53  0.48  0.45  0.42  0.40  0.38  0.37
       4     1.824  2.01  1.45  1.20  1.06  0.96  0.89  0.84  0.80  0.76  0.73
       2     1.775  2.01  1.45  1.20  1.06  0.96  0.89  0.84  0.80  0.76  0.73
      60   overall  0.94  0.77  0.72  0.81  0.77  0.74  0.73  0.69  0.69  0.68


 Na(Z)obs/Na(Z)exp versus resolution and Z (0.1-1.0)
      #      RES     0.1   0.2   0.3   0.4   0.5   0.6   0.7   0.8   0.9   1.0

      37     8.754  1.14  0.89  0.94  0.98  1.03  1.08  1.13  1.08  1.00  0.94
      48     5.677  0.66  0.92  0.72  0.76  0.79  0.92  0.87  0.98  0.95  0.89
      76     4.562  0.83  0.94  0.96  0.96  0.94  0.93  0.97  0.98  1.04  1.06
      74     3.877  0.99  1.04  1.04  1.02  1.10  1.02  1.02  0.98  0.91  0.96
      93     3.451  0.56  0.89  0.87  0.98  0.98  1.05  1.03  1.00  1.00  0.95
      90     3.135  0.93  0.98  0.99  0.84  0.96  0.89  0.93  1.05  1.01  1.00
     106     2.881  1.09  1.09  0.91  1.00  0.96  0.94  0.97  0.99  0.99  0.99
     105     2.678  1.60  1.21  1.18  1.10  1.02  1.10  1.00  0.99  0.98  0.95
     122     2.529  1.98  1.18  0.95  0.87  0.81  0.82  0.88  0.85  0.84  0.87
     122     2.390  1.81  1.04  1.08  0.97  0.90  0.85  0.88  0.85  0.84  0.88
     130     2.279  1.94  1.27  1.01  0.98  0.96  0.92  0.90  0.88  0.91  0.92
     135     2.181  3.19  2.00  1.49  1.21  1.11  1.00  0.99  0.90  0.87  0.87
     112     2.089  3.38  1.87  1.41  1.14  0.98  0.91  0.85  0.79  0.80  0.79
     132     2.013  4.22  2.30  1.70  1.36  1.17  1.04  1.01  0.95  0.88  0.83
     135     1.944  4.20  2.21  1.60  1.30  1.09  0.95  0.87  0.81  0.75  0.76
     166     1.881  4.62  2.46  1.77  1.39  1.18  1.05  0.99  0.94  0.88  0.84
     144     1.824  5.25  2.76  1.93  1.52  1.27  1.14  1.02  0.93  0.90  0.87
      89     1.775  5.55  2.91  2.04  1.60  1.34  1.17  1.05  0.96  0.89  0.84
    1942   overall  2.73  1.66  1.31  1.13  1.03  0.97  0.95  0.91  0.89  0.88


 List of     81 reflections *NOT* obeying Wilson distribution (Z> 10.0)

   h    k    l     RES      Z     Intensity    Sigma

   45  -42    5    1.79 1490.71  0.3274E+02  0.3135E+02 "alien"
   45  -42    6    1.78 1091.65  0.2397E+02  0.3046E+02 "alien"
   54   10   17    1.79  986.71  0.2167E+02  0.3020E+02 "alien"
   56   12   14    1.79  979.77  0.2152E+02  0.3617E+02 "alien"
   58   18   10    1.76  928.52  0.2039E+02  0.2970E+02 "alien"
   46  -38   10    1.79  866.59  0.1903E+02  0.2667E+02 "alien"
   44  -42    9    1.77  843.75  0.1853E+02  0.3174E+02 "alien"
   47  -41    5    1.77  815.76  0.1792E+02  0.2943E+02 "alien"
   38  -37   19    1.79  801.04  0.1759E+02  0.2819E+02 "alien"
   39  -38   18    1.78  683.63  0.1501E+02  0.3119E+02 "alien"
   36  -34   23    1.77  677.35  0.1488E+02  0.2516E+02 "alien"
   55   10   17    1.77  611.35  0.1343E+02  0.3009E+02 "alien"
   44  -42    7    1.80  601.03  0.1320E+02  0.3050E+02 "alien"
   60   18    5    1.76  534.84  0.1175E+02  0.3380E+02 "alien"
   42  -40   14    1.78  514.52  0.1130E+02  0.3165E+02 "alien"
   56   11   15    1.78  416.01  0.9136E+01  0.2862E+02 "alien"
   34  -32   25    1.76  401.61  0.8820E+01  0.2670E+02 "alien"
   57   12   14    1.77  401.48  0.8817E+01  0.3439E+02 "alien"
   27  -23   30    1.80  398.17  0.8744E+01  0.2339E+02 "alien"
   47  -40    7    1.77  391.04  0.8588E+01  0.2743E+02 "alien"
   44  -42    8    1.79  380.26  0.8351E+01  0.3153E+02 "alien"
   55   18   13    1.80  375.40  0.8244E+01  0.2886E+02 "alien"
   47  -37   12    1.76  366.75  0.8054E+01  0.3078E+02 "alien"
   59   18    7    1.77  361.23  0.7933E+01  0.3207E+02 "alien"
   34  -32   24    1.80  340.89  0.7487E+01  0.2614E+02 "alien"
   46  -36   13    1.78  297.42  0.6532E+01  0.2642E+02 "alien"
   45  -42    8    1.77  294.48  0.6467E+01  0.3007E+02 "alien"
   45  -42    7    1.77  293.79  0.6452E+01  0.3055E+02 "alien"
   38  -36   20    1.78  271.28  0.5958E+01  0.3387E+02 "alien"
   44  -42   10    1.76  262.86  0.5773E+01  0.3069E+02 "alien"
   57   18   11    1.78  258.45  0.5676E+01  0.2884E+02 "alien"
   47  -41    4    1.77  258.17  0.5670E+01  0.2977E+02 "alien"
   47  -40    6    1.78  235.28  0.5167E+01  0.3175E+02 "alien"
   50   16   20    1.78  233.26  0.5123E+01  0.2397E+02 "alien"
   46  -42    2    1.78  181.78  0.3992E+01  0.2981E+02 "alien"
   52   17   18    1.78  178.80  0.3927E+01  0.2775E+02 "alien"
   42  -40   15    1.76  170.91  0.3754E+01  0.2911E+02 "alien"
   53   17   17    1.78  161.42  0.3545E+01  0.2435E+02 "alien"
   39  -37   20    1.75  126.97  0.2789E+01  0.2652E+02 "alien"
   41  -39   16    1.77  120.43  0.2645E+01  0.3045E+02 "alien"
   41  -39   17    1.75   68.44  0.1503E+01  0.2808E+02 "alien"
   57   14    9    1.83   37.19  0.4205E+02  0.4291E+02 "alien"
   57   18    5    1.84   35.39  0.4001E+02  0.3168E+02 "alien"
   45  -40    4    1.84   27.86  0.3149E+02  0.3004E+02 "alien"
   56   18    9    1.83   21.65  0.2448E+02  0.3117E+02 "alien"
   58   18    5    1.81   21.37  0.2416E+02  0.3186E+02 "alien"
   58   16    4    1.84   20.54  0.2322E+02  0.3649E+02 "alien"
   47  -42    0    1.77   20.47  0.1949E+01  0.3001E+02 "alien"
   58   17    1    1.84   20.44  0.2311E+02  0.3340E+02 "alien"
   58   18    2    1.83   20.27  0.2292E+02  0.3697E+02 "alien"
   35  -34   21    1.84   19.53  0.2208E+02  0.2797E+02 "alien"
   38  -37   18    1.82   19.45  0.2199E+02  0.2873E+02 "alien"
   35  -34   22    1.81   19.43  0.2197E+02  0.2784E+02 "alien"
   58   16    5    1.83   19.00  0.2148E+02  0.3331E+02 "alien"
   56   14   10    1.85   18.34  0.2073E+02  0.3882E+02 "alien"
   22  -17   32    1.83   17.08  0.1931E+02  0.2030E+02 "alien"
   39  -38   16    1.83   16.59  0.1876E+02  0.2957E+02 "alien"
   34  -33   23    1.81   16.16  0.1826E+02  0.2970E+02 "alien"
   58   18    3    1.83   16.11  0.1821E+02  0.3385E+02 "alien"
   44  -41    3    1.84   15.67  0.1771E+02  0.3395E+02 "alien"
   53    9   18    1.80   15.52  0.1755E+02  0.2639E+02 "alien"
   59   16    4    1.81   15.04  0.1700E+02  0.3697E+02 "alien"
   40   40    9    1.90   14.51  0.6002E+02  0.4434E+02 "alien"
   41  -40   11    1.85   14.11  0.1595E+02  0.3280E+02 "alien"
   59   18    3    1.80   14.09  0.1593E+02  0.3149E+02 "alien"
   45  -41    2    1.82   14.07  0.1591E+02  0.3008E+02 "alien"
   44   14   24    1.81   13.68  0.1547E+02  0.2084E+02 "alien"
   39  -38   17    1.81   13.27  0.1500E+02  0.2782E+02 "alien"
   45  -39    6    1.84   13.23  0.1496E+02  0.3269E+02 "alien"
   50    7   20    1.83   12.99  0.1469E+02  0.2894E+02 "alien"
   23  -18   32    1.81   12.39  0.1400E+02  0.1863E+02 "alien"
   58   17    2    1.84   11.96  0.1352E+02  0.3698E+02 "alien"
   40  -38   19    1.74   11.65 -0.3893E+02  0.2673E+02 "alien"
   57   15    7    1.85   11.57  0.1308E+02  0.3381E+02 "alien"
   52   17   16    1.82   11.55  0.1306E+02  0.2761E+02 "alien"
   43  -30   19    1.81   10.77  0.1218E+02  0.2173E+02 "alien"
   44  -41    1    1.85   10.72  0.1212E+02  0.3073E+02 "alien"
   52   10   16    1.87   10.55  0.4361E+02  0.3471E+02 "alien"
   59   17    0    1.81   10.38  0.2425E+02  0.4032E+02 "alien"
   58   15    7    1.82   10.36  0.1171E+02  0.3350E+02 "alien"
   51    7   20    1.81   10.15  0.1148E+02  0.3228E+02 "alien"


 List of     81 reflections *NOT* obeying Wilson distribution (sorted by resolution)
 Ice rings could occur at (Angstrom):
 3.897,3.669,3.441, 2.671,2.249,2.072, 1.948,1.918,1.883,1.721

   h    k    l     RES      Z     Intensity    Sigma

   40  -38   19    1.74   11.65 -0.3893E+02  0.2673E+02
   39  -37   20    1.75  126.97  0.2789E+01  0.2652E+02
   41  -39   17    1.75   68.44  0.1503E+01  0.2808E+02
   42  -40   15    1.76  170.91  0.3754E+01  0.2911E+02
   60   18    5    1.76  534.84  0.1175E+02  0.3380E+02
   47  -37   12    1.76  366.75  0.8054E+01  0.3078E+02
   44  -42   10    1.76  262.86  0.5773E+01  0.3069E+02
   58   18   10    1.76  928.52  0.2039E+02  0.2970E+02
   34  -32   25    1.76  401.61  0.8820E+01  0.2670E+02
   47  -42    0    1.77   20.47  0.1949E+01  0.3001E+02
   45  -42    8    1.77  294.48  0.6467E+01  0.3007E+02
   36  -34   23    1.77  677.35  0.1488E+02  0.2516E+02
   47  -41    5    1.77  815.76  0.1792E+02  0.2943E+02
   57   12   14    1.77  401.48  0.8817E+01  0.3439E+02
   55   10   17    1.77  611.35  0.1343E+02  0.3009E+02
   47  -40    7    1.77  391.04  0.8588E+01  0.2743E+02
   59   18    7    1.77  361.23  0.7933E+01  0.3207E+02
   41  -39   16    1.77  120.43  0.2645E+01  0.3045E+02
   47  -41    4    1.77  258.17  0.5670E+01  0.2977E+02
   44  -42    9    1.77  843.75  0.1853E+02  0.3174E+02
   45  -42    7    1.77  293.79  0.6452E+01  0.3055E+02
   53   17   17    1.78  161.42  0.3545E+01  0.2435E+02
   42  -40   14    1.78  514.52  0.1130E+02  0.3165E+02
   52   17   18    1.78  178.80  0.3927E+01  0.2775E+02
   57   18   11    1.78  258.45  0.5676E+01  0.2884E+02
   47  -40    6    1.78  235.28  0.5167E+01  0.3175E+02
   50   16   20    1.78  233.26  0.5123E+01  0.2397E+02
   56   11   15    1.78  416.01  0.9136E+01  0.2862E+02
   46  -36   13    1.78  297.42  0.6532E+01  0.2642E+02
   39  -38   18    1.78  683.63  0.1501E+02  0.3119E+02
   45  -42    6    1.78 1091.65  0.2397E+02  0.3046E+02
   46  -42    2    1.78  181.78  0.3992E+01  0.2981E+02
   38  -36   20    1.78  271.28  0.5958E+01  0.3387E+02
   44  -42    8    1.79  380.26  0.8351E+01  0.3153E+02
   45  -42    5    1.79 1490.71  0.3274E+02  0.3135E+02
   38  -37   19    1.79  801.04  0.1759E+02  0.2819E+02
   46  -38   10    1.79  866.59  0.1903E+02  0.2667E+02
   54   10   17    1.79  986.71  0.2167E+02  0.3020E+02
   56   12   14    1.79  979.77  0.2152E+02  0.3617E+02
   44  -42    7    1.80  601.03  0.1320E+02  0.3050E+02
   27  -23   30    1.80  398.17  0.8744E+01  0.2339E+02
   55   18   13    1.80  375.40  0.8244E+01  0.2886E+02
   34  -32   24    1.80  340.89  0.7487E+01  0.2614E+02
   59   18    3    1.80   14.09  0.1593E+02  0.3149E+02
   53    9   18    1.80   15.52  0.1755E+02  0.2639E+02
   51    7   20    1.81   10.15  0.1148E+02  0.3228E+02
   39  -38   17    1.81   13.27  0.1500E+02  0.2782E+02
   23  -18   32    1.81   12.39  0.1400E+02  0.1863E+02
   43  -30   19    1.81   10.77  0.1218E+02  0.2173E+02
   44   14   24    1.81   13.68  0.1547E+02  0.2084E+02
   59   16    4    1.81   15.04  0.1700E+02  0.3697E+02
   59   17    0    1.81   10.38  0.2425E+02  0.4032E+02
   35  -34   22    1.81   19.43  0.2197E+02  0.2784E+02
   34  -33   23    1.81   16.16  0.1826E+02  0.2970E+02
   58   18    5    1.81   21.37  0.2416E+02  0.3186E+02
   38  -37   18    1.82   19.45  0.2199E+02  0.2873E+02
   58   15    7    1.82   10.36  0.1171E+02  0.3350E+02
   52   17   16    1.82   11.55  0.1306E+02  0.2761E+02
   45  -41    2    1.82   14.07  0.1591E+02  0.3008E+02
   58   18    3    1.83   16.11  0.1821E+02  0.3385E+02
   22  -17   32    1.83   17.08  0.1931E+02  0.2030E+02
   39  -38   16    1.83   16.59  0.1876E+02  0.2957E+02
   58   18    2    1.83   20.27  0.2292E+02  0.3697E+02
   50    7   20    1.83   12.99  0.1469E+02  0.2894E+02
   56   18    9    1.83   21.65  0.2448E+02  0.3117E+02
   58   16    5    1.83   19.00  0.2148E+02  0.3331E+02
   57   14    9    1.83   37.19  0.4205E+02  0.4291E+02
   45  -40    4    1.84   27.86  0.3149E+02  0.3004E+02
   58   16    4    1.84   20.54  0.2322E+02  0.3649E+02
   58   17    2    1.84   11.96  0.1352E+02  0.3698E+02
   58   17    1    1.84   20.44  0.2311E+02  0.3340E+02
   45  -39    6    1.84   13.23  0.1496E+02  0.3269E+02
   35  -34   21    1.84   19.53  0.2208E+02  0.2797E+02
   57   18    5    1.84   35.39  0.4001E+02  0.3168E+02
   44  -41    3    1.84   15.67  0.1771E+02  0.3395E+02
   41  -40   11    1.85   14.11  0.1595E+02  0.3280E+02
   44  -41    1    1.85   10.72  0.1212E+02  0.3073E+02
   56   14   10    1.85   18.34  0.2073E+02  0.3882E+02
   57   15    7    1.85   11.57  0.1308E+02  0.3381E+02
   52   10   16    1.87   10.55  0.4361E+02  0.3471E+02
   40   40    9    1.90   14.51  0.6002E+02  0.4434E+02

 NUMBER OF UNIQUE ALIEN REFLECTIONS WITH A Z-SCORE ABOVE LIMIT        50
 (ALIENS ABOVE LIMIT (REJECT_ALIEN=      20.0) ARE MARKED INVALID)

 NUMBER OF REFLECTION RECORDS ON OUTPUT FILE "XDS_ASCII.HKL"        2012
 NUMBER OF ACCEPTED OBSERVATIONS (INCLUDING SYSTEMATIC ABSENCES)    1962
 NUMBER OF REJECTED MISFITS & ALIENS (marked by -1*SIGMA(IOBS))       50


 cpu time used                  0.1 sec
 elapsed wall-clock time        0.2 sec
