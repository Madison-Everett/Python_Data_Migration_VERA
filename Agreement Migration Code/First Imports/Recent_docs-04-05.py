import requests
import os
import base64
import time
from json.decoder import JSONDecodeError

filesid = {
    198004 : '43595 - UNIV43595_VU_Alnylam-A7 2021 FE 10Feb21 (003)',
    198378 : '55070 - 16X117 Modification 6F FE',
    198410 : '58451 - UNIV58451 (formerly 3402-018477)_UConn-A7_FE_20210',
    198062 : '58578 - Sponsored Research Agreement VU 58578 Amendment8_O',
    198266 : '58742 - UNIV58742_VUMC59374_Am7_FE_20210324',
    198405 : '58778 - UNIV58778_VUMC59496_FE_20210330',
    198470 : '59114 - UNIV59114_VUMC60817_FE_20210208',
    198180 : '59356 - UNIV59356_GAT_Am 29-FE_20210322',
    198167 : '59361 - UNIV59361_UVA_A17_FE_20210323',
    198402 : '59394 - UNIV59394_HU_A33_rev_FE_20210311',
    198140 : '59395 - UNIV59395_Baylor College of Medicine-A5_FE_2021031',
    198487 : '59399 - UNIV59399_VUMC61472_Am 5_FE_20210401',
    198075 : '59422 - UNIV59422_VUMC61812_FE_20210218',
    198590 : '59452 - UNIV59452_Rutgers_Am 45-FE_20210405',
    198322 : '59518 - UNIV59518 MetroLaser Mod 4 FE 25March21',
    198472 : '59545 - 10008038CHNG1 _ NCE to 12.31.21',
    198592 : '59573 - NDA_Third_Renewal_-_Vanderbilt FE20210316 - (FE)',
    198177 : '59869 - UNIV59869 Amend 7 H1.1 N6600118C4005 P00007 FE 22M',
    198014 : '59894 - TSU - Exhibit A (Phambu Group)_Adds Almarwani and ',
    198308 : '60055 - UNIV60055 (Karsai) FA8750-18-C-0089 P00005 FE 25Ma',
    198396 : '60130 - UNIV60130_VUMC65119-A3_PE_20210319_FE_20210329',
    198585 : '60187 - Nanosys-Vanderbilt 3-2021 -Amend 1 to Extend (FE)',
    198007 : '60246 - IHSMR1Addendum_2021-03-10_IHSMR1_VUSPA-FY2021 (Add',
    198008 : '60246 - ILMO3Addendum_2021-03-10_ILMOS3_ (Addend - $5664)(',
    198368 : '60274 - UNIV60274_IU_A3_FE_20210326',
    198554 : '60317 - UNIV60317_NRCG_Am 8-FE_20210402',
    197998 : '60344 - Immune Tolerance Network - VU Tissue Imaging Core ',
    198530 : '60429 - UNIV60429_Fisk_Am 3_FE_20210402',
    198170 : '60486 - NewL3HarrisVANDERBILTNDA3-3-2021 (1) - VU.Rev-03.1',
    198559 : '60593 - UNIV60593_VUMC70426_FE_20210402',
    197956 : '60626 - UNIV60626_VUMC70021_Am 2 FE_20210315',
    198128 : '60635 - UNIV60635_UnivSouthFlorida-A2_FE_20210319',
    198490 : '60699 - VA Dept Juv Justice - Vanderbilt University MOA re',
    198447 : '60741 - UNIV60741_VUMC71407-A2_FE_20210331',
    197899 : '60763 - UNIV60763_MU_A3_FE_20210315',
    198532 : '60871 - UNIV60871_Tougaloo_Am 3_FE_20210402',
    198413 : '60872 - UNIV60872_Oregon Health & Science University 10143',
    198227 : '60898 - UNIV60898_University of Illinois_Final Draft_20210',
    198519 : '61103 - UNIV61103_VUMC 77299-A2_FE_20210401',
    198318 : '61192 - UNIV61192_A3_FE_20210325',
    198069 : '61193 - UNIV61193_UH_Am 2_FE_20210318',
    198349 : '61254 - 16X117 Modification 4O FE',
    198377 : '61254 - 16X117 Modification 4P FE',
    197991 : '61259 - UNIV61259_VUMC78121-A1_FE_20210316',
    197950 : '61265 - 20210305_University NDA Amendment 1-Vanderbilt (00',
    198275 : '61275 - UNIV61275_VUMC79608-A!_FE__20210324',
    197897 : '61302 - TSI-4088-19-2020806VanderbiltMod1FE',
    198186 : '61516 - Boston Childrens Hospital (BCH) Nelson_Vanderbilt_',
    198508 : '61670 - UNIV61670_NCSU-A1_FE_20210401',
    198498 : '61691 - UNIV61691_Cornell University 79433-20671-RYD-UG-VA',
    198503 : '61766 - UTSI - VU ChemXRD Core - Core Agrmt w State of TN ',
    198195 : '61790 - 16X117 Modification 7B FE',
    198279 : '61794 - UNIV61794_University of Colorado 201620_FE__202103',
    198061 : '61799 - Enamine- Vanderbilt (Meiler) - Mutual NDA (Final.C',
    197886 : '61810 - Oregon - Addendum_OHSU_Maloyan_12Jan2021_(FE)',
    197911 : '61834 - UNIV61834_Harris County Public Health 1110 Grants-',
    197975 : '61855 - UNIV61855_UTSI_FE_20210316',
    198492 : '61893 - A Z MSA - VU MMPC - (3.30.21 - 3.30.24) (FE)',
    198001 : '61918 - Notice of Increase of LO for PO 2210612 ',
    198182 : '61946 - UNIV61946_NU_FE_20210322',
    197898 : '61950 - UNIV61950_3M_FE_20210312',
    198560 : '61954 - FE Subk__Vanderbilt with Attachments',
    198615 : '61956 - UNIV61956_VUMC81171-A1_FE_20210405',
    197872 : '61967 - Navigo Proteins_3 WAY CDA_04-12-2020 (002)_KG (002',
    198028 : '61986 - TDOT - VU ISIS (Work) Fully executed contract (UNI',
    198012 : '61987 - UNIV61987 (Goldring) Amendment_Letter_A1_20200256 ',
    198006 : '61989 - UNIV61989_Compass Evaluation and Research_FE_20210',
    198391 : '62007 - Infineon_-_VU_ISDE_(Kauppila) NDA (FE)',
    198369 : '62013 - UNIV62013_MMC_FE_rev_20210328',
    198388 : '62026 - FE Vanderbilt DUSA to Experian_03 18 2021',
    198612 : '62029 - UNIV62029_VUMC89460-_FE_20210405',
    198568 : '62030 - State of TN - VU (Adams) kkGrant_Contract_(GR)_Fin',
    198023 : '62032 - UNIV62032_VUMC90083_FE_20210316',
    198538 : '62034 - UNIV62034_MSK_FE_20210402',
    198475 : '62045 - DUA Sarah Jaser FE (002)',
    197905 : '62046 - UNIV62046_CREE_FE_20210315',
    198066 : '62050 - UNIV62050_USF_FE_20210318',
    198338 : '62055 - Arcus Vanderbilt NDA 2-26-2021 (FE)',
    198222 : '62056 - DSA between TCCCRC and Vanderbilt for CUNY Policy ',
    198032 : '62058 - UNIV62058 Vanderbilt (Bhuva Bharat_ISDE) -w- Sandi',
    197936 : '62063 - UNIV62063_YaYa_FE_20210315',
    198212 : '62066 - UNIV62066 Vanderbilt (Lau) -w- AtlasXomics 22March',
    197894 : '62074 - UNIV62074 Vanderbilt (Marcus) -w- Environmental Wo',
    198312 : '62082 - UNIV62082_University of Kentucky 3200003835-21-261',
    198341 : '62083 - UNIV62083_VUMC88030_FE_20210326',
    197914 : '62084 - UNIV62084_University of Delaware R305E190002_PO586',
    197879 : '62086 - VA Commonwealth U - VU Syn Core - VICB-539-synthes',
    198134 : '62088 - UNIV62088_UM_FE_20210319',
    197882 : '62091 - Cincinnati Childrens Hosp - VU Chem Syn - Research',
    198241 : '62102 - Renesas Electronics - VU ISDE (Reed) Core Agmt - (',
    198310 : '62108 - UNIV62108_TSU_core_FE_20210325',
    198400 : '62110 - VUSE Subcontract AIESN Final Executed',
    198302 : '62117 - StemSynergy - VU MassSpec (Calcutt)  - Agreement (',
    198304 : '62120 - UNIV62120 Vanderbilt (Milne) -w- UCSD - CORES FE 2',
    198210 : '62121 - UNIV62121_Iowa_CORE_FE_20210323',
    198339 : '62124 - CMI2_Vanderbilt_MNDA_210325_V2_FE'
    }


for x in filesid:
    response = requests.get("https://peer.app.vanderbilt.edu/index.php?controller=Api&call=getContractFile&fileId="+str(x)+"&token=dac9630aec642a428cd73f4be0a03569")

    try:
        time.sleep(1)
        message = response.json()["content"]
        message_bytes = message.encode('ascii')
        file = base64.b64decode(message_bytes)
        try:
              os.mkdir("/Users/everetmm/Desktop/pooobs/Contract_"+filesid[x][0:5])
              print("Directory " , filesid[x][0:5] ," Created ")
              open("/Users/everetmm/Desktop/pooobs/Contract_"+filesid[x][0:5]+"/Contract "+ filesid[x]+".pdf", 'wb').write(file)
        except FileExistsError:
              print("Directory " , filesid[x][0:5],  " already exists")
              open("/Users/everetmm/Desktop/pooobs/Contract_"+filesid[x][0:5]+"/Contract "+ filesid[x]+".pdf", 'wb').write(file)
        
    except JSONDecodeError:
        print("    ")
        print(str(x))
        print("    ")






