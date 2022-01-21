import requests
import os
import base64

import time
from json.decoder import JSONDecodeError

filesid = {
    204256 : "59382 - Vanderbilt_University_2-218740-27_(Amendment_",
    204293 : "59652 - UNIV59652_Wake Forest Univ Health Sciences-A4_FE_2",
    204281 : "59962 - UNIV59962_FE_20210830",
    204333 : "60062 - UNIV60062_URMC_Am 4_FE_20210830",
    204010 : "60246 - UNIV60246_UNH_FE_20210824",
    204193 : "60628 - UNIV60628_University of Connecticut_Am 4_Final Dra",
    204138 : "60637 - UNIV60637_AIR_A4_FE_20210826",
    204251 : "60799 - UNIV60799_Urban Institute-Am 3_FE_20210830",
    204183 : "61128 - UNIV61128_IBP_A3_FE_20210827",
    204166 : "61145 - UNIV61145_VUMC75785_Am 2_FE_20210827",
    204335 : "61372 - UNIV61372_UC_FE_20210830",
    204002 : "61419 - Finalized Signed SF30",
    204100 : "61439 - UNIV61439_UD_Am 2_FE_20210826",
    204068 : "61450 - UNIV61450_MWHC_FE_20210825",
    204196 : "61585 - Signed for Ross King 210827",
    204030 : "61638 - UNIV61638_WSU20081-A1_FE_20210824",
    204017 : "61655 - UNIV61655_WE_A1_FE_20210824",
    204061 : "61682 - UNIV61682_VUMC84473_Am 2_FE_20210825",
    204137 : "61720 - UNIV61720_Meharry Medical College_Am 1_Final Draft",
    204261 : "61757 - UNIV61757_VUMC86188-A1_FE_20210830",
    204188 : "61772 - PO_TERMS_102_2185860_2_US",
    204048 : "61848 - UNIV61848_UTC_Am 2_FE_20210824",
    204265 : "61861 - UNIV61861_ETSU Mei 20-167 -A1_FE_20210830",
    204028 : "61888 - UNIV61888-NCIRE_Am 1 _FE_20210824",
    204126 : "62017 - UNIV62017_NAI_A4_FE_20210826",
    204210 : "62028 - 20210827_CDA_Vanderbilt University_Sivananthan Lab",
    204123 : "62080 - UNIV62080_DFCI_Reinherz_5P01AI143565-02_1313502_A1",
    204331 : "62249 - Addendum to Research Core Agreement_GPlab",
    204104 : "62254 - Amend to add funds",
    204055 : "62262 - UNIV62262_VUMC93164_FE_20210825",
    204253 : "62266 - UNIV62266_UT_Crawford Vanderbilt A21-1166-S003_FE_",
    204125 : "62267 - UNIV62267_VUMCxxxxx_FE_20210826",
    204082 : "62323 - UNIV62323_Northwestern University_Final Draft_2021",
    204296 : "62329 - UNIV62329_VUMC93385_FE_20210830",
    204008 : "62342 - UNIV62342_PC_FE_20210818",
    204144 : "62350 - UNIV62350_VUMC 92991_Final Draft_20210826",
    204194 : "62363 - Scientic Core Agreement and Addendum - 7_14_2021 (",
    204167 : "62376 - NDA - Vanderbilt University - Leipzig University -",
    204103 : "62379 - UNIV62379_UK_FE_20210826",
    204221 : "62381 - UNIV62381_UW_FE_20210827",
    203991 : "62387 - Vanderbilt Historical Purchase Agreement and Fee W",
    204201 : "62392 - UNIV62392_Wake Forest University Health Sciences_F",
    204160 : "62393 - UNIV62393_AURI_FE_20210827",
    204011 : "62418 - UNIV62418_Core_FE_20210824",
    204009 : "62419 - UNIV62419_UA_CORE_FE_20210824",
    204169 : "62420 - FE Vanderbilt University CDA 24AUG2021 (002) (002)",
    204195 : "62424 - 2",
    204184 : "62425 - UNIV62425_KT_FE_20210827",
    204325 : "62427 - UNIV62427_UPenn_CORE_FE_20210830",
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

