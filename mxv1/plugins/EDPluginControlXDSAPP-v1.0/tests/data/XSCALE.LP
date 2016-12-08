
 ***** XSCALE ***** (VERSION Nov 1, 2016  BUILT=20161101)   6-Dec-2016
 Author: Wolfgang Kabsch
 Copy licensed until 30-Apr-2017 to
  academic users for non-commercial applications   
 No redistribution.


 ******************************************************************************
                              CONTROL CARDS
 ******************************************************************************

 OUTPUT_FILE= merged_anom_XSCALE.hkl
 INPUT_FILE= XDS_ASCII.HKL
 MERGE= TRUE
 FRIEDEL'S_LAW= FALSE

 THE DATA COLLECTION STATISTICS REPORTED BELOW ASSUMES:
 SPACE_GROUP_NUMBER=  179
 UNIT_CELL_CONSTANTS=    92.47    92.47   128.02  90.000  90.000 120.000

 ***** 12 EQUIVALENT POSITIONS IN SPACE GROUP #179 *****

    If x',y',z' is an equivalent position to x,y,z, then
        x'=x*ML(1)+y*ML( 2)+z*ML( 3)+ML( 4)/12.0
        y'=x*ML(5)+y*ML( 6)+z*ML( 7)+ML( 8)/12.0
        z'=x*ML(9)+y*ML(10)+z*ML(11)+ML(12)/12.0

    #    1  2  3  4    5  6  7  8    9 10 11 12 
    1    1  0  0  0    0  1  0  0    0  0  1  0
    2    0 -1  0  0    1 -1  0  0    0  0  1  8
    3   -1  1  0  0   -1  0  0  0    0  0  1  4
    4   -1  0  0  0    0 -1  0  0    0  0  1  6
    5    0  1  0  0   -1  1  0  0    0  0  1  2
    6    1 -1  0  0    1  0  0  0    0  0  1 10
    7    0  1  0  0    1  0  0  0    0  0 -1  8
    8   -1  0  0  0   -1  1  0  0    0  0 -1  4
    9    1 -1  0  0    0 -1  0  0    0  0 -1  0
   10    0 -1  0  0   -1  0  0  0    0  0 -1  2
   11    1  0  0  0    1 -1  0  0    0  0 -1 10
   12   -1  1  0  0    0  1  0  0    0  0 -1  6
 

 ALL DATA SETS WILL BE SCALED TO XDS_ASCII.HKL                                                                                                           


 ******************************************************************************
                    READING INPUT REFLECTION DATA FILES
 ******************************************************************************

 NUMBER OF UNIQUE REFLECTIONS IN FILE "REMOVE.HKL"       1


 DATA    MEAN       REFLECTIONS        INPUT FILE NAME
 SET# INTENSITY  ACCEPTED REJECTED
   1  0.1407E+03   176254      0  XDS_ASCII.HKL

 ******************************************************************************
           CORRECTION FACTORS AS FUNCTION OF IMAGE NUMBER & RESOLUTION
 ******************************************************************************

 RECIPROCAL CORRECTION FACTORS FOR INPUT DATA SETS MERGED TO
 OUTPUT FILE: merged_anom_XSCALE.hkl                            

 THE CALCULATIONS ASSUME         FRIEDEL'S_LAW= TRUE
 TOTAL NUMBER OF CORRECTION FACTORS DEFINED      260
 DEGREES OF FREEDOM OF CHI^2 FIT             55350.0
 CHI^2-VALUE OF FIT OF CORRECTION FACTORS      0.890
 NUMBER OF CYCLES CARRIED OUT                      3

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_001.cbf       
 XMIN=     0.7 XMAX=   639.2 NXBIN=   13
 YMIN= 0.00053 YMAX= 0.27757 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS      67283


 ******************************************************************************
  CORRECTION FACTORS AS FUNCTION OF X (fast) & Y(slow) IN THE DETECTOR PLANE
 ******************************************************************************

 RECIPROCAL CORRECTION FACTORS FOR INPUT DATA SETS MERGED TO
 OUTPUT FILE: merged_anom_XSCALE.hkl                            

 THE CALCULATIONS ASSUME         FRIEDEL'S_LAW= TRUE
 TOTAL NUMBER OF CORRECTION FACTORS DEFINED     1332
 DEGREES OF FREEDOM OF CHI^2 FIT             55260.8
 CHI^2-VALUE OF FIT OF CORRECTION FACTORS      0.885
 NUMBER OF CYCLES CARRIED OUT                      3

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_001.cbf      
 XMIN=    11.9 XMAX=  1470.4 NXBIN=   36
 YMIN=   108.5 YMAX=  1595.6 NYBIN=   37
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS      67283


 ******************************************************************************
   CORRECTION FACTORS AS FUNCTION OF IMAGE NUMBER & DETECTOR SURFACE POSITION
 ******************************************************************************

 RECIPROCAL CORRECTION FACTORS FOR INPUT DATA SETS MERGED TO
 OUTPUT FILE: merged_anom_XSCALE.hkl                            

 THE CALCULATIONS ASSUME         FRIEDEL'S_LAW= TRUE
 TOTAL NUMBER OF CORRECTION FACTORS DEFINED      169
 DEGREES OF FREEDOM OF CHI^2 FIT             55348.0
 CHI^2-VALUE OF FIT OF CORRECTION FACTORS      0.882
 NUMBER OF CYCLES CARRIED OUT                      3

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_001.cbf      
 XMIN=     0.7 XMAX=   639.2 NXBIN=   13
 DETECTOR_SURFACE_POSITION=     741     852
 DETECTOR_SURFACE_POSITION=     989    1105
 DETECTOR_SURFACE_POSITION=     493    1105
 DETECTOR_SURFACE_POSITION=     493     599
 DETECTOR_SURFACE_POSITION=     989     599
 DETECTOR_SURFACE_POSITION=    1302    1089
 DETECTOR_SURFACE_POSITION=     973    1424
 DETECTOR_SURFACE_POSITION=     509    1424
 DETECTOR_SURFACE_POSITION=     181    1089
 DETECTOR_SURFACE_POSITION=     181     615
 DETECTOR_SURFACE_POSITION=     509     280
 DETECTOR_SURFACE_POSITION=     973     280
 DETECTOR_SURFACE_POSITION=    1302     615
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS      67283


 ******************************************************************************
    CORRECTION PARAMETERS FOR THE STANDARD ERROR OF REFLECTION INTENSITIES
 ******************************************************************************

 The variance v0(I) of the intensity I obtained from counting statistics is
 replaced by v(I)=a*(v0(I)+b*I^2). The model parameters a, b are chosen to
 minimize the discrepancies between v(I) and the variance estimated from
 sample statistics of symmetry related reflections. This model implicates
 an asymptotic limit ISa=1/SQRT(a*b) for the highest I/Sigma(I) that the
 experimental setup can produce (Diederichs (2010) Acta Cryst D66, 733-740).
 Often the value of ISa is reduced from the initial value ISa0 due to systematic
 errors showing up by comparison with other data sets in the scaling procedure.
 (ISa=ISa0=-1 if v0 is unknown for a data set.)

     a        b          ISa    ISa0   INPUT DATA SET
 1.063E+00  6.797E-03   11.76   12.36 XDS_ASCII.HKL
 

 FACTOR TO PLACE ALL DATA SETS TO AN APPROXIMATE ABSOLUTE SCALE 0.114318E+04
 (ASSUMING A PROTEIN WITH 50% SOLVENT)



 ******************************************************************************
  STATISTICS OF SCALED OUTPUT DATA SET : merged_anom_XSCALE.hkl
  FILE TYPE:         XDS_ASCII      MERGE=TRUE           FRIEDEL'S_LAW=FALSE

        17 OUT OF    176254 REFLECTIONS REJECTED
     48260 REFLECTIONS ON OUTPUT FILE 

 ******************************************************************************
 DEFINITIONS:
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

     8.49        1980     541       547       98.9%       6.9%      5.9%     1975   20.10      8.1%    99.2*   -13    0.857     174
     6.00        3708     989       992       99.7%       6.1%      6.3%     3697   17.27      7.1%    99.3*   -13    0.783     389
     4.90        4320    1277      1279       99.8%       6.0%      6.6%     4306   15.27      7.2%    99.3*     3    0.834     531
     4.24        5602    1520      1523       99.8%       5.8%      6.5%     5582   16.66      6.8%    99.5*    -6    0.759     644
     3.80        6549    1722      1724       99.9%       6.6%      6.8%     6539   16.15      7.6%    99.4*    -8    0.740     751
     3.47        7321    1906      1907       99.9%       7.0%      7.3%     7315   15.07      8.1%    99.4*    -6    0.748     845
     3.21        7887    2055      2055      100.0%       8.0%      8.4%     7879   12.60      9.2%    99.3*     1    0.809     924
     3.00        7613    2226      2228       99.9%       9.4%     10.2%     7597   10.04     11.2%    98.6*    -1    0.752     999
     2.83        8355    2384      2385      100.0%      12.0%     12.7%     8321    8.49     14.2%    98.0*    -6    0.746    1060
     2.68        9335    2504      2505      100.0%      15.1%     15.8%     9301    7.38     17.6%    97.2*    -5    0.716    1118
     2.56        9906    2614      2616       99.9%      18.3%     19.1%     9871    6.21     21.3%    96.6*    -3    0.761    1174
     2.45       10666    2766      2769       99.9%      23.6%     25.3%    10640    5.00     27.4%    93.6*    -3    0.733    1260
     2.35       11126    2868      2874       99.8%      27.3%     29.1%    11092    4.38     31.6%    93.1*    -4    0.734    1302
     2.27       11503    2955      2964       99.7%      31.9%     33.2%    11466    3.90     36.9%    90.0*    -2    0.757    1342
     2.19       10727    3053      3074       99.3%      46.5%     40.4%    10647    3.03     54.9%    80.3*    -2    0.847    1352
     2.12       11086    3218      3223       99.8%      46.4%     47.9%    11018    2.59     55.1%    76.1*    -3    0.746    1455
     2.06       11100    3271      3283       99.6%      50.8%     48.7%    11029    2.45     60.5%    69.6*    -2    0.784    1476
     2.00       12374    3384      3392       99.8%      62.5%     62.2%    12329    2.03     73.2%    63.2*     0    0.783    1553
     1.95       13064    3518      3524       99.8%      67.3%     68.4%    13015    1.90     78.6%    51.6*    -4    0.750    1617
     1.90       12015    3489      3570       97.7%      96.3%     88.3%    11810    1.36    113.5%    40.5*    -7    0.739    1475
    total      176237   48260     48434       99.6%      12.9%     13.1%   175429    6.51     15.1%    99.3*    -3    0.763   21441


 ========== STATISTICS OF INPUT DATA SET ==========


  R-FACTORS FOR INTENSITIES OF DATA SET XDS_ASCII.HKL

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.49         6.9%       5.9%      1975
     6.00         6.1%       6.3%      3697
     4.90         6.0%       6.6%      4306
     4.24         5.8%       6.5%      5582
     3.80         6.6%       6.8%      6539
     3.47         7.0%       7.3%      7315
     3.21         8.0%       8.4%      7879
     3.00         9.4%      10.2%      7597
     2.83        12.0%      12.7%      8321
     2.68        15.1%      15.8%      9301
     2.56        18.3%      19.1%      9871
     2.45        23.6%      25.3%     10640
     2.35        27.3%      29.1%     11092
     2.27        31.9%      33.2%     11466
     2.19        46.5%      40.4%     10647
     2.12        46.4%      47.9%     11018
     2.06        50.8%      48.7%     11029
     2.00        62.5%      62.2%     12329
     1.95        67.3%      68.4%     13015
     1.90        96.3%      88.3%     11810
    total        12.9%      13.1%    175429


 ******************************************************************************
    WILSON STATISTICS OF SCALED DATA SET: merged_anom_XSCALE.hkl                            
 ******************************************************************************

 Data is divided into resolution shells and a straight line 
 A - 2*B*SS is fitted to log<I>, where
   RES    = mean resolution (Angstrom) in shell
   SS     = mean of (sin(THETA)/LAMBDA)**2 in shell
   <I>    = mean reflection intensity in shell
   BO     = (A - log<I>)/(2*SS)
    #     = number of reflections in resolution shell

   WILSON LINE (using all data) : A=  13.850 B=  31.036 CORRELATION=  0.98
      #      RES      SS        <I>       log(<I>)       BO
     408    10.663   0.002  1.1474E+06      13.953     -23.4
     641     6.633   0.006  4.9289E+05      13.108      65.3
     802     5.185   0.009  4.9144E+05      13.105      40.1
     924     4.396   0.013  6.2980E+05      13.353      19.2
    1028     3.886   0.017  5.2168E+05      13.165      20.7
    1142     3.518   0.020  4.0661E+05      12.916      23.1
    1223     3.237   0.024  2.5358E+05      12.443      29.5
    1300     3.016   0.027  1.7123E+05      12.051      32.7
    1394     2.833   0.031  1.2648E+05      11.748      33.7
    1445     2.681   0.035  9.9473E+04      11.508      33.7
    1525     2.551   0.038  7.1092E+04      11.172      34.8
    1590     2.438   0.042  5.8341E+04      10.974      34.2
    1654     2.339   0.046  5.1983E+04      10.859      32.7
    1703     2.251   0.049  4.7177E+04      10.762      31.3
    1770     2.172   0.053  3.4002E+04      10.434      32.2
    1839     2.101   0.057  3.2653E+04      10.394      30.5
    1862     2.036   0.060  2.8349E+04      10.252      29.8
    1928     1.978   0.064  2.4050E+04      10.088      29.4
    1973     1.924   0.068  1.8604E+04       9.831      29.7


 HIGHER ORDER MOMENTS OF WILSON DISTRIBUTION OF  CENTRIC DATA
    AS COMPARED WITH THEORETICAL VALUES. (EXPECTED: 1.00)    
      #      RES        <I**2>/      <I**3>/      <I**4>/  
                         3<I>**2     15<I>**3    105<I>**4 

     201    10.663        0.924        0.736        0.491
     203     6.633        1.021        0.993        0.867
     209     5.185        0.834        0.776        0.677
     212     4.396        1.147        1.126        0.977
     204     3.886        1.033        0.872        0.656
     211     3.518        1.033        1.005        0.916
     214     3.237        1.113        1.135        1.020
     206     3.016        1.069        0.847        0.574
     214     2.833        0.955        0.791        0.568
     206     2.681        1.287        1.505        1.592
     217     2.551        1.117        1.096        0.987
     210     2.438        1.410        1.614        1.624
     206     2.339        0.843        0.855        0.917
     207     2.251        0.835        0.678        0.486
     211     2.172        1.064        0.991        0.850
     212     2.101        0.786        0.609        0.456
     201     2.036        0.822        0.512        0.273
     213     1.978        0.648        0.356        0.182
     207     1.924        0.928        0.906        1.006
    3964   overall        0.994        0.917        0.797


 HIGHER ORDER MOMENTS OF WILSON DISTRIBUTION OF ACENTRIC DATA
    AS COMPARED WITH THEORETICAL VALUES. (EXPECTED: 1.00)    
      #      RES        <I**2>/      <I**3>/      <I**4>/  
                         2<I>**2      6<I>**3     24<I>**4 

     207    10.663        0.971        0.944        0.946
     438     6.633        0.995        0.935        0.826
     593     5.185        1.080        1.176        1.347
     712     4.396        0.953        0.945        0.990
     824     3.886        0.973        0.951        0.896
     931     3.518        1.033        1.125        1.289
    1009     3.237        1.067        1.197        1.378
    1094     3.016        0.963        0.950        0.907
    1180     2.833        0.999        1.039        1.141
    1239     2.681        0.993        0.990        0.961
    1308     2.551        1.020        1.155        1.449
    1380     2.438        0.916        0.819        0.696
    1448     2.339        1.066        1.195        1.384
    1496     2.251        1.129        1.250        1.368
    1559     2.172        1.035        1.050        1.071
    1627     2.101        1.001        0.992        1.024
    1661     2.036        0.979        0.981        1.025
    1715     1.978        0.879        0.723        0.610
    1766     1.924        1.132        1.025        0.880
   22187   overall        1.012        1.022        1.058

   ======= CUMULATIVE INTENSITY DISTRIBUTION =======
 DEFINITIONS:
   <I>    = mean reflection intensity
 Na(Z)exp = expected number of acentric reflections with I <= Z*<I>
 Na(Z)obs = observed number of acentric reflections with I <= Z*<I>
 Nc(Z)exp = expected number of  centric reflections with I <= Z*<I>
 Nc(Z)obs = observed number of  centric reflections with I <= Z*<I>



 Nc(Z)obs/Nc(Z)exp versus resolution and Z (0.1-1.0)
      #      RES     0.1   0.2   0.3   0.4   0.5   0.6   0.7   0.8   0.9   1.0

     201    10.663  1.10  1.04  1.00  1.00  1.00  1.01  1.02  1.02  1.05  1.04
     203     6.633  0.89  1.03  1.09  1.02  1.05  1.01  1.01  1.05  1.05  1.07
     209     5.185  0.87  0.86  0.88  0.94  0.96  0.96  1.03  1.00  1.03  1.04
     212     4.396  1.04  1.06  1.00  1.01  1.01  1.02  0.99  0.99  0.96  0.95
     204     3.886  0.77  1.02  1.00  0.96  0.94  0.97  0.95  0.98  1.01  0.98
     211     3.518  1.11  1.03  1.04  0.99  0.98  0.96  0.98  0.97  0.95  0.96
     214     3.237  1.02  1.12  1.01  1.02  1.01  1.01  1.06  1.03  1.02  1.03
     206     3.016  0.57  0.80  0.87  0.91  0.91  0.97  0.95  0.93  0.90  0.91
     214     2.833  0.92  0.99  0.96  1.03  1.00  1.01  1.01  1.00  0.98  0.99
     206     2.681  0.82  0.86  0.92  1.02  1.03  1.05  1.07  1.04  1.03  1.02
     217     2.551  0.58  0.71  0.86  0.90  0.96  0.99  0.96  0.99  0.98  0.97
     210     2.438  0.92  0.91  1.01  0.98  0.97  0.97  0.98  0.98  0.96  0.96
     206     2.339  0.86  0.79  0.89  0.96  0.99  1.02  1.02  1.01  1.01  1.02
     207     2.251  0.99  0.95  0.96  0.97  0.97  0.96  1.00  1.01  1.04  1.03
     211     2.172  0.76  0.78  0.80  0.85  0.86  0.89  0.92  0.94  0.98  0.99
     212     2.101  0.72  0.72  0.84  0.91  0.93  0.96  0.96  1.00  1.01  1.02
     201     2.036  0.82  0.71  0.69  0.67  0.75  0.81  0.86  0.84  0.87  0.90
     213     1.978  0.76  0.68  0.66  0.66  0.78  0.83  0.86  0.85  0.91  0.93
     207     1.924  1.05  0.91  0.86  0.90  0.85  0.85  0.89  0.91  0.93  0.96
    3964   overall  0.87  0.89  0.91  0.93  0.94  0.96  0.97  0.98  0.98  0.99


 Na(Z)obs/Na(Z)exp versus resolution and Z (0.1-1.0)
      #      RES     0.1   0.2   0.3   0.4   0.5   0.6   0.7   0.8   0.9   1.0

     207    10.663  0.91  0.85  0.89  0.82  0.93  0.95  0.95  0.96  0.99  0.99
     438     6.633  1.01  1.10  1.03  1.05  1.06  1.03  0.99  1.00  1.00  1.00
     593     5.185  1.12  1.06  1.05  1.00  1.00  1.02  1.01  0.99  0.98  0.95
     712     4.396  1.08  1.02  1.01  1.01  1.00  1.02  1.01  1.02  1.01  1.00
     824     3.886  0.93  1.03  0.98  1.03  1.01  1.03  1.04  1.05  1.03  1.02
     931     3.518  0.99  1.04  1.02  1.03  1.01  1.03  1.03  1.03  1.03  1.02
    1009     3.237  1.04  1.12  1.09  1.08  1.06  1.05  1.04  1.03  1.01  1.03
    1094     3.016  0.85  1.05  1.03  1.03  1.07  1.06  1.05  1.04  1.03  1.02
    1180     2.833  0.80  0.90  0.97  0.97  1.00  1.01  1.03  1.02  1.00  1.02
    1239     2.681  0.96  0.98  1.05  1.04  1.04  1.04  1.03  1.03  1.03  1.02
    1308     2.551  0.89  0.87  0.96  1.00  1.03  1.04  1.04  1.05  1.05  1.04
    1380     2.438  0.94  0.86  0.91  0.93  0.98  0.98  0.99  1.00  1.00  1.00
    1448     2.339  0.78  0.81  0.94  0.96  0.97  0.99  0.98  0.97  0.99  1.01
    1496     2.251  1.58  1.12  1.02  0.98  0.99  0.97  0.97  0.98  0.99  0.99
    1559     2.172  1.35  1.03  0.90  0.91  0.93  0.97  0.97  0.97  0.98  0.99
    1627     2.101  1.16  0.87  0.82  0.85  0.87  0.90  0.91  0.93  0.95  0.96
    1661     2.036  1.09  0.81  0.79  0.83  0.88  0.90  0.93  0.95  0.97  0.97
    1715     1.978  0.86  0.65  0.61  0.65  0.73  0.77  0.81  0.85  0.89  0.93
    1766     1.924  2.10  1.28  1.05  0.94  0.89  0.86  0.87  0.89  0.90  0.90
   22187   overall  1.12  0.96  0.94  0.94  0.95  0.96  0.97  0.98  0.98  0.99


 List of      1 reflections *NOT* obeying Wilson distribution (Z> 10.0)

   h    k    l     RES      Z     Intensity    Sigma

   32  -14   22    2.58   10.57  0.7515E+06  0.2372E+05 "alien"


 List of      1 reflections *NOT* obeying Wilson distribution (sorted by resolution)
 Ice rings could occur at (Angstrom):
 3.897,3.669,3.441, 2.671,2.249,2.072, 1.948,1.918,1.883,1.721

   h    k    l     RES      Z     Intensity    Sigma

   32  -14   22    2.58   10.57  0.7515E+06  0.2372E+05

 cpu time used by XSCALE        2.7 sec
 elapsed wall-clock time        2.8 sec
