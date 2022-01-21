import requests
import os
import base64

import time
from json.decoder import JSONDecodeError

filesid = {
    203591 : "58624 - UNIV58624_VUMC59165-A6_FE_20210816",
203870 : "58712 - UNIV58712_VUMC59925_FE_20210820",
203595 : "58715 - UNIV58715_VUMC60296-A4_FE_20210816",
203119 : "59646 - UNIV59646_VUMC63022-A3_FE_20210804_",
203719 : "59807 - UNIV59807_FSU-A4_FE_20210818",
203568 : "60012 - UNIV60012_UCT_A3_FE_20210816",
203413 : "60103 - VANDERBILT SUB1118166-002 MOD 007 FE",
203175 : "60130 - UNIV60130_VUMC65119-A4_FE_20210805",
203645 : "60191 - UNIV60191_UL_Am 3_FE_20210817",
203909 : "60300 - UNIV60300-NMIMT-A2_FE_20210820",
203768 : "60323 - UNIV60323_VUMC66321_Am 3_FE_20210819",
203129 : "60555 - UNIV60555 PO 848k540_Modification FE 4Aug21",
203389 : "60665 - CA39797 UNIV60665_CARDIFF_Updated FE_20210811",
203665 : "60847 - UNIV60847_GSU SP00013765-02-A4_FE_20210817",
203179 : "60880 - UNIV60880_VUMC74445-A2_FE_20210805",
203462 : "61049 - UNIV61048 (Fingleton) DocuSign_2021-08-09b_Medicen",
203674 : "61084 - UNIV61084_SRESC-A3_FE_20210817",
203547 : "61087 - OS00000173AM1_FE Subaward Am 2_Jensen-Doss_Vanderb",
203620 : "61119 - VUMC 76701 UNIV61119_VUMC_A2_FE_20210817",
203446 : "61139 - UNIV61139_Washington University_A1_FE_20210812",
203132 : "61146 - UNIV61146_UF_A2_FE_20210805",
203465 : "61179 - 7200AA20CA00022.Modification P002_Executed",
203160 : "61195 - UNIV61195_VUMC77091_AM 1_Final Draft_20210803.fe",
203824 : "61220 - AMEND_2_RG-E1666-P002",
203386 : "61282 - UNIV61282_VUMC79016_Am 2_Final Draft_20210810",
203455 : "61319 - UNIV61319_MSU-A1_FE_20210812",
203817 : "61341 - UNIV61341_TJU_A6_FE_20210820",
203468 : "61370 - Mobilion - Vanderbilt - Amendment Letter re_ SLIM",
203577 : "61403 - UNIV61403_NG_A1_FE_20210816",
203442 : "61413 - Toyota (TEMA) - Vanderbilt (Hatzell-Caldwell) Thir",
203222 : "61435 - UNIV61435_UNM_Am 3_NCE_FE_20210806",
203397 : "61437 - 80NSSC20K0424   P00005  AWARD DOCS",
203341 : "61456 - UNIV61456_VUMC8108-A1_FE_20210810",
203308 : "61463 - UNIV61463_VUMC80598_Am 2_Final Draft_20210809",
203723 : "61488 - UNIV61488_VUMC81686-A1_FE_20210818",
203709 : "61530 - UNIV61530_VUMC82727-A2 _FE_20210817",
203575 : "61553 - 200727 MoU - Vanderbilt_Murdoch University (1) (3)",
203550 : "61564 - SDCPS ACA vFinal",
203182 : "61641 - UNIV61641_VUMC86859-A1_FE_20210805",
203634 : "61670 - UNIV61670_NCSU-A3_FE_20210817",
203641 : "61687 - UNIV61687 - 75N95020P00369_P00001_FE_17Aug21",
203548 : "61701 - Vanderbilt funding 2021 (002) (1)",
203607 : "61718 - UNIV61718_Dartmouth_Am 1_Final Draft_20210817",
203235 : "61823 - UNIV61823 Vanderbilt -w- OUHSC FE 6Aug21",
203116 : "61845 - UNIV61845 Fisk University-A1_FE_20210804",
203338 : "61860 - UNIV61860_ETSU_Am 1_FE_20210810",
203727 : "61865 - UNIV61865_Lipscomb University-A1_FE_20210818",
203619 : "61942 - UNIV61942_VUMC_Am 2_FE_20210817",
203303 : "61990 - UNIV61990 VU Core Amendment to Extend Agrmt Patter",
203821 : "62038 - UNIV62038_VUMC87548_Am 1_Final Draft_20210820",
203570 : "62060 - UNIV62060_IU_CORE_A3_FE_20210816",
203173 : "62077 - UNIV62077_DFCI 5P01AI143565-02_FE_20210805",
203844 : "62120 - 2021-08-19 - Munji_VU SPA - FY2021 NonProfit Resea",
203394 : "62139 - new SOW for stemsenergy",
203474 : "62147 - UNIV62147_University of Tennessee_Am 1_Final Draft",
203574 : "62209 - 1 Swygert_VU (VUMC88055) DTUA (2) (VU 62210)",
203552 : "62210 - 3 Swygert_VU (VUMC88057) signed",
203777 : "62234 - EPICA Membership Agreement NSF IUCRC GTRC UCF Vand",
203879 : "62239 - UNIV62239_Leland Stanford Junior Univ 230322_FE_20",
203631 : "62279 - AvalancheVandyAddendum RR_ALS",
203163 : "62282 - UNIV62282_Ohio_State_University_FE_20210805",
203336 : "62296 - UNIV62296_VUMC93815 SBA_FE_20210810",
203796 : "62297 - UNIV62297_Univ of Texas At Austin_202002128-001_FE",
203668 : "62302 - UNIV62302_VUMC88756_FE_20210817",
203573 : "62304 - UNIV62304_VUMC92501_Final Draft_20210816",
203122 : "62305 - Vanderbilt_Research_Agreement___Neurochemistry_Mic",
203121 : "62315 - UNIV62315_VUA00-62628788-199245-FX_FE_20210804",
203458 : "62316 - UNIV62316_VUMC94107_Final Draft_20210812",
203551 : "62327 - Synthetic lethality-mediated precision signed",
203622 : "62330 - UNIV62330_VUMC93323_FE_20210817",
203627 : "62331 - UNIV62331_VUMC93136_Final Draft_20210817",
203251 : "62334 - NVF-MSNW-Vanderbilt University-Subgrant-014689-202",
203525 : "62336 - UNIV62336_VUMC91876_Final Draft_20210813",
203738 : "62340 - UNIV62340_University of Utah_Final Draft_20210819",
203113 : "62341 - NPUA-21-009 Vanderbilt University",
203902 : "62354 - UNIV62354_AURI_Vanderbilt_Blake_FE_20210820",
203583 : "62356 - GlassWRX - NDA Mutual Multi-Party ARPA-E OPEN 2021",
203217 : "62358 - UNIV62358_VUMC94133_Final Draft_20210806",
203344 : "62361 - UNIV62361_Wake Forest University Health Sciences_F",
203652 : "62366 - UNIV62366_MSU 031900.01_Final Draft_20210817.fe",
203228 : "62374 - UNIV62374 Vanderbilt -w- Mayo FE 6Aug21",
203295 : "62375 - VAnderbilt-UCD-2021-0672-D VK 0427",
203302 : "62382 - UNIV62382 (Schafer) -w- Meharry Medical College CO",
203301 : "62383 - UNIV62383 VU (Schafer) -w- Patrick Fallon CORE FE",
203580 : "62390 - UNIV62390 (Milne) JHU_Vanderbilt_PE_Research Core",


          }

for x in filesid:
    
    response = requests.get("https://peer.app.vanderbilt.edu/index.php?controller=Api&call=getContractFile&fileId="+str(x)+"&token=dac9630aec642a428cd73f4be0a03569")

    try:
        time.sleep(1)
        message = response.json()["content"]
        message_bytes = message.encode('ascii')
        file = base64.b64decode(message_bytes)
        try:
              os.mkdir("/Users/everetmm/Desktop/wow/Contract_"+filesid[x][0:5])
              print("Directory " , filesid[x][0:5] ," Created ")
              open("/Users/everetmm/Desktop/wow/Contract_"+filesid[x][0:5]+"/(Original)Contract "+ filesid[x]+".pdf", 'wb').write(file)
        except FileExistsError:
              print("Directory " , filesid[x][0:5],  " already exists")
              open("/Users/everetmm/Desktop/wow/Contract_"+filesid[x][0:5]+"/(Original)Contract "+ filesid[x]+".pdf", 'wb').write(file)

        
    except JSONDecodeError:
        print("    ")
        print(str(x))
        print("    ")

