import requests
import os
import base64

import time
from json.decoder import JSONDecodeError

filesid = {
       204989 : "60030 - UNIV60030_UP_Am 4_FE_20210913",
    205002 : "60176 - UNIV60176_UCF_A3_FE_20210914",
    204780 : "60214 - UNIV60214_VUMC64982-A4_FE_20210908",
    204825 : "60392 - UNIV60392_University at Buffalo_Am 3_Final Draft_2",
    204941 : "60464 - UNIV60464_UTSM_Fully Executed_20210913",
    205072 : "60583 - UNIV60583_Univ of Calgary-A2_FE_20210915",
    205032 : "60610 - UNIV60610_UT_Am 3_woFE_20210914 approved",
    204953 : "61106 - UNIV61106_WUSTL_A2_FE_20210913",
    204990 : "61176 - UNIV61176_EDC_FE_20210913",
    205075 : "61180 - TSI-2620-19-2020223 Vanderbilt Amendment 1 FE",
    204948 : "61317 - PO_TERMS_102_2125099_4_US",
    204951 : "61345 - UNIV61345_UZ_A1_FE_2021913",
    204852 : "61392 - UNIV61392_VUMC_Am 1_FE_20210908",
    204933 : "61438 - UNIV61438_California Insitute of Technology_Amendm",
    204870 : "61497 - UNIV61497_VUMC84924-Am 1_FE_20210909",
    204822 : "61583 - UNIV61583_Rutgers University_Amendment 2_Final Dra",
    204833 : "61663 - UNIV61663_MMC-A1_FE_20210909",
    204848 : "61738 - UNIV61738_Cornell_FE_20210908",
    205089 : "61919 - UNIV61919_IU_FE_20210820",
    204828 : "61991 - VU_SPA_Research_Core_Addendum_dimethyl analog-sign",
    204778 : "62111 - UNIV62111_UE_A510055-A1_FE_20210908",
    205114 : "62113 - UNIV62113_VUMC90528_FE_20210916",
    205118 : "62184 - UNIV62184_VUMC89680-A2_FE_20210916",
    205055 : "62236 - UNIV62236_VUMC84045_A2_FE_20210915",
    205042 : "62332 - UNIV62332_VUMC92999_Final Draft_20210914",
    205029 : "62348 - CSL-Vanderbilt RCA (CSL112 in wound healing) (clea",
    204843 : "62355 - UNIV62355_UP_FE_20210908",
    205059 : "62363 - Scientic Core Agreement and Addendum - final",
    205104 : "62378 - UNIV62378_Children's Hosptial Medical Center_Final",
    204819 : "62408 - UNIV62408_VUMC94135_Final Draft_20210908",
    204805 : "62409 - UNIV62409_The Reg. of the Univ. of CA Berkley_FE_2",
    205039 : "62423 - UNIV62423_UCSF12940_Final Draft_20210914",
    204976 : "62426 - Contract RG-T3609-P002  VANDERBILT University 09.1",
    205080 : "62434 - UNIV62434_WF_FE_20210915",
    205111 : "62438 - UNIV62438_UWis_FE_20210916",
    204875 : "62451 - 2021_09_07_13_59_25",
    204883 : "62453 - signed _VU_SPA_Research_Core_Agreement_040118 - ed",
    204888 : "62455 - 201218-VUSPA-ResearchCoreAgreement-Dubland_GS1.PDF",
    204946 : "62458 - Alphacore Core Agreement",
    205076 : "62465 - UNIV62465_CORE_UI_FE_20210915",
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

