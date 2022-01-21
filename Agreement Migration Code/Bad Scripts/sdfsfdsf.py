import os



downloadingcheck = [
    172979,
    186808,
    146210,
    146204,
    143126,
    143127,
    172981,
    150984,
    187545,
    187543,
    141318,
    150994,
    113859,
    170242,
    170241,
    141316,
    187819,
    160554,
    160555,
    158815,
    186806,
    187365,
    187137,
    197067,
    197065,
    165641,
    175028,
    165640,
    176276,
    168181,
    183092,
    168182,
    187595,
    183091,
    187593,
    186595,
    186596,
    167793,
    175026,
    176278,
    185065,
    185064,
    177408,
    177409,
    169300,
    180710,
    164563,
    164565,
    180711,
    152170,
    165725,
    165726,
    178330,
    178331,
    152169,
    191846,
    191845,
    158913,
    178138,
    158915,
    158914,
    158921,
    163821,
    170690,
    158918,
    170692,
    158920,
    147721,
    150303,
    158901,
    163822,
    158906,
    187590,
    161453,
    184777,
    195362,
    158905,
    158900,
    184775,
    195361,
    158912,
    158911,
    158904,
    161454,
    158908,
    158898,
    158897,
    147759,
    158907,
    158917,
    158910,
    159034,
    158919,
    158916,
    187588,
    150286,
    158909,
    147787,
    158902,
    158903,
    178137,
    182358,
    194651,
    145888,
    169817,
    111841,
    149038,
    169824,
    169823,
    145869,
    168147,
    158434,
    194649,
    182357,
    158433,
    174747,
    174746,
    192387,
    192386,
    165370,
    165369,
    174165,
    174166,
    182850,
    182849,
    168532,
    179926,
    156050,
    166368,
    166369,
    158040,
    143397,
    153785,
    188808,
    188809,
    153786,
    151949,
    151950,
    141699,
    144204,
    178773,
    144206,
    178772,
    147191,
    158039,
    147192,
    171734,
    186350,
    147255,
    147257,
    171733,
    141567,
    157803,
    157802,
    141568,
    186348,
    187670,
    183314,
    169355,
    155448,
    169354,
    183315,
    162852,
    162853,
    146794,
    155469,
    146808,
    187669,
    158824,
    158825,
    165385,
    165384,
    161547,
    161548,
    185113,
    185112,
    175389,
    175388,
    191192,
    191191,
    189277,
    189279,
    200810,
    178832,
    171952,
    178829,
    171951,
    189957,
    185912,
    185911,
    185946,
    175910,
    194080,
    175909,
    194078,
    188230,
    188229,
    169731,
    195632,
    192202,
    158276,
    44296,
    109219,
    189306,
    189307,
    190420,
    189439,
    157613,
    157612,
    194919,
    141720,
    158242,
    44294,
    158780,
    171779,
    170150,
    171780,
    161699,
    161698,
    170149,
    185922,
    185924,
    154176,
    154177,
    169962,
    169963,
    171862,
    192050,
    171864,
    192433,
    182079,
    182080,
    153544,
    148234,
    185167,
    150149,
    174965,
    163992,
    150158,
    171223,
    168480,
    160110,
    190246,
    194005,
    145778,
    148229,
    196161,
    196162,
    166507,
    154822,
    154823,
    178843,
    178844,
    166508,
    174547,
    160272,
    160273,
    185513,
    185514,
    160231,
    185512,
    169281,
    169282,
    147277,
    183665,
    183664,
    170169,
    147275,
    158680,
    158681,
    170170,
    186422,
    186423,
    172240,
    172239,
    171407,
    164718,
    164719,
    171408,
    162074,
    191111,
    184800,
    188990,
    188991,
    174916,
    174917,
    150782,
    186924,
    186328,
    186329,
    150784,
    173810,
    111766,
    111765,
    173809,
    161971,
    161972,
    186019,
    114004,
    195902,
    113770,
    113769,
    210112,
    178894,
    153193,
    153182,
    178890,
    165266,
    159254,
    157972,
    110779,
    143161,
    178966,
    146378,
    155892,
    104165,
    111706,
    181500,
    161726,
    155888,
    178021,
    161797,
    109669,
    152633,
    154181,
    112330,
    142419,
    152632,
    112329,
    151938,
    112331,
    156134,
    111707,
    155893,
    155887,
    104157,
    151936,
    155885,
    155894,
    110211,
    155890,
    156133,
    165630,
    192577,
    110780,
    112327,
    147553,
    157973,
    155889,
    155886,
    147552,
    112328,
    143182,
    110212,
    155895,
    159256,
    104156,
    154180,
    165614,
    146376,
    149100,
    110781,
    111975,
    142421,
    109668,
    165617,
    140142,
    147021,
    171833,
    171832,
    171735,
    184200,
    184202,
    147031,
    159116,
    159115,
    185704,
    185709,
    168605,
    168606,
    159391,
    159390,
    185706,
    172836,
    172837,
    155052,
    155050,
    172835,
    183544,
    183543,
    196359,
    182708,
    196653,
    188998,
    167040,
    167041,
    165187,
    165186,
    196017,
    156907,
    177182,
    177181,
    143408,
    176056,
    176057,
    155781,
    155782,
    168080,
    168079,
    143280,
    194645,
    194647,
    167495,
    167494,
    179342,
    179343,
    163288,
    157748,
    152228,
    176142,
    176143,
    157744,
    157741,
    157742,
    153739,
    160716,
    160715,
    157750,
    188000,
    146789,
    157740,
    159736,
    195197,
    195196,
    185933,
    146792,
    157747,
    170883,
    158349,
    185935,
    153746,
    170885,
    175692,
    152224,
    157749,
    157743,
    157745,
    145686,
    157746,
    163287,
    147729,
    191945,
    177517,
    180057,
    161976,
    178515,
    176248,
    147649,
    147723,
    146961,
    169734,
    158854,
    158853,
    146315,
    189108,
    195511,
    189109,
    195513,
    158856,
    158860,
    158858,
    153740,
    172147,
    172145,
    158861,
    175189,
    150315,
    163938,
    163939,
    175187,
    146347,
    158859,
    160556,
    169167,
    169166,
    160557,
    185932,
    153738,
    146322,
    158857,
    185931,
    150296,
    158855,
    142803,
    172299,
    196911,
    178914,
    192989,
    172300,
    178913,
    171143,
    188193,
    171141,
    194004,
    174910,
    163273,
    158121,
    159728,
    167108,
    153516,
    159727,
    153517,
    146128,
    184816,
    163274,
    150302,
    157938,
    170837,
    184814,
    157939,
    187671,
    187672,
    151673,
    193606,
    151678,
    193604,
    174684,
    174682,
    151675,
    145687,
    150285,
    151676,
    170839,
    159740,
    167107,
    151674,
    156838,
    151677,
    191229,
    170518,
    170520,
    191227,
    168701,
    168700,
    183585,
    183584,
    181237,
    196078,
    196080,
    181238,
    150652,
    101982,
    36661,
    112781,
    175656,
    162464,
    187335,
    174286,
    168405,
    183998,
    168406,
    183997,
    161391,
    161392,
    152354,
    173891,
    188841,
    188840,
    173979,
    173981,
    185327,
    185325,
    190792,
    197061,
    190794,
    189818,
    196944,
    189820,
    196942,
    171573,
    171572,
    194468,
    194469,
    183886,
    183885,
    156732,
    187602,
    155459,
    155464,
    187604,
    157161,
    167701,
    157162,
    167702,
    182780,
    182782,
    186810,
    175039,
    185357,
    184779,
    175041,
    175038]


doublecheck =[109796,
    160973,
    154915,
    154919,
    174864,
    175087,
    110980,
    173599,
    111195,
    109649,
    144084,
    163372,
    173717,
    172428,
    158303,
    158329,
    156136,
    113998,
    113672,
    180740,
    177543,
    178471,
    178477,
    178697,
    112616,
    142558,
    179107,
    169480,
    179917,
    27076,
    175261,
    157611,
    173644,
    157988,
    176615,
    176663,
    176746,
    180954,
    180995,
    159687,
    159880,
    177121,
    177331,
    188551,
    188570,
    188571,
    188573,
    188593,
    188599,
    188615,
    188616,
    188618,
    183831,
    184027,
    184220,
    184228,
    184234,
    184399,
    184551,
    143153,
    143174,
    143284,
    170759,
    171157,
    185075,
    185153,
    185215,
    172537,
    185345,
    36625,
    185386,
    143694,
    185483,
    185501,
    185506,
    185652,
    175407,
    185866,
    186290,
    157923,
    175797,
    186754,
    186761,
    186768,
    176379,
    187409,
    187412,
    185428,
    185429,
    185902,
    178681,
    185907,
    185918,
    166480,
    187488,
    187909,
    188084,
    182101,
    182493,
    183556,
    183560,
    188096,
    188130,
    188145,
    188207,
    188537,
    33538,
    189943,
    190309,
    190353,
    180310,
    190645,
    191226,
    181498,
    181672,
    191477,
    191675,
    191688,
    191693,
    191766,
    191938,
    162378,
    162385,
    181762,
    191942,
    191971,
    192002,
    192012,
    192861,
    192894,
    182396,
    182443,
    191520,
    193337,
    193458,
    193496,
    193552,
    193569,
    193571,
    193582,
    163682,
    182904,
    193962,
    194075,
    194108,
    194195,
    194393,
    183368,
    192086,
    192134,
    192137,
    192294,
    192305,
    192310,
    192323,
    192340,
    192342,
    192411,
    192568,
    192769,
    192779,
    192785,
    192789,
    192879,
    193623,
    193677,
    193679,
    183913,
    192964,
    193399,
    193406,
    193573,
    193609,
    194421,
    194471,
    194482,
    194492,
    194493,
    194499,
    194507,
    194509,
    180527,
    180569,
    184011,
    184047,
    184044,
    192973,
    192976,
    193053,
    193061,
    193124,
    193152,
    180921,
    181212,
    184089,
    184168,
    184232,
    193615,
    193687,
    193939,
    193947,
    193955,
    193956,
    193961,
    175956,
    158978,
    184329,
    189930,
    189933,
    189960,
    190419,
    190425,
    190498,
    159327,
    184732,
    184738,
    190720,
    190845,
    184853,
    191047,
    191054,
    191057,
    191103,
    191387,
    191392,
    191470,
    171422,
    186010,
    186022,
    186050,
    186152,
    191562,
    191582,
    191597,
    191600,
    191817,
    191819,
    178077,
    178121,
    186204,
    186260,
    187841,
    189091,
    189205,
    189769,
    191976,
    192676,
    192099,
    192683,
    192699,
    192702,
    178858,
    160584,
    160585,
    194534,
    194557,
    194575,
    194617,
    194660,
    194710,
    194716,
    194734,
    160724,
    181072,
    194782,
    194803,
    194808,
    194809,
    194810,
    194812,
    194825,
    194833,
    194835,
    194840,
    194850,
    194853,
    194877,
    194910,
    194947,
    194955,
    194979,
    195010,
    195027,
    195050,
    195059,
    195061,
    195063,
    195074,
    195083,
    195089,
    195187,
    195200,
    189996,
    190668,
    190937,
    191005,
    191701,
    192355,
    192502,
    192547,
    171794,
    192984,
    193063,
    193614,
    193684,
    194414,
    195340,
    195342,
    195426,
    162936,
    162939,
    181131,
    143654,
    169861,
    173463,
    181235,
    181488,
    181546,
    181555,
    195302,
    195306,
    195331,
    149264,
    174294,
    192885,
    195550,
    195576,
    195578,
    195580,
    195600,
    195602,
    195637,
    195670,
    175220,
    176400,
    178491,
    195437,
    195441,
    195447,
    195455,
    195461,
    195537,
    172542,
    186966,
    187030,
    187053,
    187361,
    187444,
    187645,
    187665,
    187668,
    187844,
    187858,
    188018,
    188021,
    175652,
    188045,
    188199,
    189972,
    190379,
    190416,
    190429,
    190554,
    190567,
    190749,
    190752,
    190765,
    190810,
    190820,
    178374,
    191001,
    191006,
    191025,
    191026,
    191295,
    191302,
    191397,
    160112,
    191649,
    191651,
    191869,
    191881,
    191894,
    192029,
    192043,
    192061,
    192072,
    160376,
    179315,
    180156,
    192351,
    192429,
    192451,
    192503,
    192530,
    192560,
    147716,
    176834,
    181403,
    181431,
    180735,
    181037,
    183907,
    184757,
    184912,
    184920,
    184947,
    184971,
    184995,
    185820,
    186119,
    189935,
    190082,
    190084,
    193300,
    193575,
    193579,
    193587,
    193602,
    193648,
    189192,
    189336,
    189345,
    189349,
    189378,
    189481,
    193713,
    193716,
    193717,
    193856,
    193862,
    193909,
    193912,
    193920,
    193923,
    193963,
    194031,
    156958,
    189489,
    189496,
    189498,
    189520,
    189533,
    189567,
    189573,
    189785,
    189800,
    194061,
    194100,
    194223,
    194361,
    147839,
    189955,
    192995,
    193144,
    193150,
    193151,
    194413,
    194475,
    194487,
    194489,
    195309,
    195688,
    195691,
    195749,
    195755,
    195780,
    195786,
    195803,
    195808,
    195907,
    195908,
    195914,
    195923,
    195953,
    195974,
    196004,
    163278,
    185604,
    196056,
    196121,
    170036,
    178153,
    196159,
    196183,
    196305,
    196307,
    196311,
    196474,
    196509,
    196515,
    179185,
    196529,
    196537,
    196549,
    196553,
    196565,
    196579,
    196710,
    196771,
    196782,
    196853,
    172346,
    179993,
    180113,
    180138,
    196916,
    196918,
    196923,
    196939,
    196945,
    197080,
    197084,
    197096,
    197124,
    175335,
    180494,
    197193,
    197254,
    197251,
    197252,
    197261,
    197306,
    197309,
    197323,
    197325,
    197330,
    197334,
    197374,
    197389,
    197496,
    197502,
    185832,
    186071,
    146076,
    140208,
    185314,
    185778,
    185791,
    186118,
    186355,
    186419,
    163780,
    164063,
    187081,
    187188,
    187252,
    187643,
    187846,
    154775,
    154912,
    164138,
    188542,
    164335,
    190688,
    190978,
    191126,
    176819,
    177296,
    164802,
    191804,
    191816,
    191922,
    191926,
    191928,
    192152,
    192154,
    192161,
    168052,
    168343,
    192174,
    192219,
    192233,
    192366,
    192602,
    192615,
    192786,
    192811,
    192814,
    190048,
    190173,
    190189,
    190307,
    190310,
    190587,
    190595,
    190676,
    151438,
    168681,
    168793,
    168940,
    168954,
    151893,
    171709,
    172327,
    172785,
    168545,
    145766,
    183823,
    169721,
    169724,
    185015,
    140406,
    188882,
    188936,
    189394,
    189399,
    189400,
    189402,
    189405,
    189408,
    172021,
    186435,
    186623,
    196074,
    196400,
    196425,
    196434,
    196592,
    196603,
    165429,
    165457,
    180425,
    173375,
    173733,
    173749,
    194614,
    194743,
    194791,
    194820,
    194866,
    194870,
    194876,
    194879,
    194893,
    194897,
    167058,
    194905,
    194912,
    194915,
    194918,
    194936,
    195105,
    195110,
    195125,
    195130,
    195134,
    195152,
    195157,
    195160,
    195162,
    195164,
    195166,
    195169,
    195170,
    174992,
    186712,
    189576,
    195210,
    195312,
    195329,
    195439,
    195458,
    195584,
    195590,
    195591,
    195619,
    195620,
    195704,
    196898,
    197270,
    197284,
    195730,
    195813,
    195833,
    195837,
    197288,
    189011,
    189506,
    189674,
    189690,
    189714,
    190510,
    159183,
    195868,
    195887,
    195892,
    195935,
    195955,
    195962,
    195966,
    196011,
    196016,
    196025,
    196039,
    192900,
    192935,
    193138,
    193154,
    193206,
    191663,
    191717,
    191838,
    191930,
    192164,
    192251,
    192275,
    192679,
    159899,
    196143,
    196360,
    196386,
    196396,
    196580,
    193410,
    193506,
    193555,
    193728,
    194001,
    194335,
    192746,
    192749,
    192757,
    192809,
    196582,
    196594,
    196636,
    196689,
    196699,
    196719,
    196732,
    196739,
    109699,
    186815,
    182906,
    182923,
    182927,
    179911,
    181640,
    183065,
    183129,
    183130,
    158557,
    159065,
    185410,
    185565,
    185581,
    185862,
    183194,
    160275,
    178555,
    160728,
    186132,
    186135,
    161059,
    161130,
    179513,
    184076,
    184085,
    154461,
    184873,
    184890,
    185556,
    154657,
    154749,
    164392,
    154895,
    155151,
    182258,
    165977,
    147836,
    182723,
    182830,
    182846,
    148495,
    140748,
    185240,
    185459,
    192901,
    193080,
    193084,
    193086,
    193162,
    193118,
    193177,
    193189,
    193190,
    193385,
    193388,
    193413,
    193415,
    193588,
    193625,
    193658,
    193771,
    193817,
    193849,
    194142,
    194148,
    194150,
    194362,
    194201,
    194229,
    194298,
    194323,
    197076,
    197099,
    197100,
    197103,
    197105,
    197114,
    194410,
    194417,
    194514,
    197068,
    197147,
    195716,
    195782,
    197378,
    197387,
    197407,
    197411,
    197415,
    197423,
    197426,
    176382,
    176388,
    195865,
    196073,
    196092,
    196110,
    196255,
    196271,
    196283,
    188857,
    189398,
    189392,
    189992,
    190038,
    190109,
    196296,
    196302,
    196444,
    196460,
    196461,
    196472,
    196476,
    196481,
    196609,
    196617,
    196618,
    162933,
    186438,
    186476,
    190710,
    195763,
    196829,
    196830,
    196832,
    196836,
    196998,
    197009,
    197018,
    197194,
    197196,
    197206,
    190934,
    190971,
    191003,
    191014,
    191055,
    191224,
    197218,
    197226,
    197229,
    197232,
    197509,
    172493,
    191603,
    191733,
    191806,
    195064,
    191873,
    192389,
    192443,
    192446,
    192730,
    192745,
    192798,
    192805,
    192808,
    192810,
    193051,
    185898,
    186073,
    186127,
    186390,
    181976,
    151266,
    184157,
    184452,
    184687,
    192673,
    192740,
    193024,
    193068,
    193303,
    193356,
    160454,
    173231,
    186984,
    187495,
    187496,
    165159,
    187739,
    188154,
    188159,
    188161,
    188447,
    188457,
    188460,
    188466,
    194329,
    194364,
    194371,
    194375,
    194382,
    194398,
    195204,
    195217,
    195239,
    195927,
    196034,
    163122,
    175967,
    176001,
    176497,
    190725,
    190787,
    192320,
    187112,
    187281,
    187300,
    194595,
    194603,
    194622,
    194624,
    195008,
    195016,
    195188,
    187581,
    187598,
    187600,
    187627,
    196548,
    196662,
    196886,
    197468,
    197492,
    197493,
    197495,
    168458,
    188226,
    194013,
    194088,
    194104,
    194254,
    194274,
    194279,
    194294,
    188273,
    195202,
    195201,
    186880,
    190004,
    190545,
    190565,
    190726,
    190826,
    174693,
    181650,
    190916,
    190922,
    190944,
    190955,
    190967,
    191276,
    191450,
    182491,
    182557,
    191494,
    191508,
    191522,
    191560,
    191722,
    191757,
    154220,
    182957,
    186492,
    191892,
    191904,
    191981,
    192035,
    192038,
    188947,
    189288,
    189368,
    189440,
    189471,
    189640,
    192498,
    192551,
    192573,
    192619,
    192630,
    192633,
    192656,
    192664,
    159846,
    189653,
    189835,
    190078,
    190097,
    190103,
    190101,
    190112,
    190220,
    186637,
    192914,
    193319,
    193478,
    193541,
    193559,
    193898,
    194735,
    194738,
    194740,
    194751,
    194757,
    194779,
    194781,
    195499,
    194788,
    195516,
    195523,
    195531,
    195533,
    188472,
    188371,
    188475,
    188484,
    188492,
    188515,
    187219,
    187267,
    187287,
    187334,
    196437,
    196489,
    196502,
    196504,
    196643,
    196717,
    196769,
    188640,
    188641,
    188683,
    188689,
    162352,
    196797,
    196807,
    196849,
    196963,
    196968,
    197001,
    142241,
    142244,
    188741,
    188743,
    188757,
    188769,
    188771,
    188796,
    169712,
    163538,
    188846,
    188849,
    188876,
    188895,
    188901,
    188917,
    170040,
    170041,
    170177,
    170181,
    188994,
    188997,
    189008,
    189023,
    189026,
    189029,
    189088,
    189119,
    189150,
    189203,
    189214,
    189232,
    188036,
    190375,
    190398,
    148417,
    189284,
    189276,
    189302,
    189304,
    189322,
    191049,
    190929,
    191386,
    192006,
    182006,
    192807,
    192992,
    193050,
    193088,
    193117,
    193184,
    193481,
    193651,
    193830,
    193831,
    182712,
    189806,
    189856,
    193888,
    194663,
    194693,
    194951,
    194945,
    194959,
    155390,
    184306,
    184315,
    189867,
    189906,
    189909,
    189915,
    190166,
    190175,
    190180,
    190183,
    190196,
    190201,
    190211,
    190260,
    190512,
    190790,
    190799,
    183462,
    194974,
    194980,
    194981,
    195076,
    195193,
    195207,
    195268,
    195275,
    185184,
    185471,
    191134,
    191239,
    191699,
    191705,
    191769,
    191770,
    191785,
    195283,
    195285,
    195291,
    195356,
    195385,
    195393,
    195401,
    195417,
    195452,
    195558,
    162048,
    186217,
    186805,
    187177,
    187174,
    191840,
    192634,
    192636,
    192726,
    193926,
    193930,
    195630,
    195636,
    195649,
    195652,
    195654,
    195760,
    195811,
    195913,
    195918,
    195959,
    163450,
    187190,
    187198,
    187319,
    187339,
    194143,
    194145,
    194198,
    194454,
    195988,
    196003,
    196194,
    196197,
    196202,
    196226,
    196238,
    110632,
    168817,
    169617,
    176975,
    179882,
    180482,
    173269,
    173462,
    173464,
    110055,
    157556,
    186667,
    186677,
    186942,
    111870,
    176201,
    176255,
    171758,
    176393,
    176825,
    170963,
    159251,
    177524,
    178523,
    178542,
    182394,
    183707,
    178923,
    178935,
    180919,
    180957,
    178038,
    184574,
    185030,
    185124,
    112749,
    184237,
    152448,
    166071,
    185443,
    186378,
    168741,
    180669,
    180684,
    180686,
    180864,
    107517,
    143302,
    143729]



for x in doublecheck:
    for g in downloadingcheck:
        if x not in downloadingcheck:
            print(x)

        



      










