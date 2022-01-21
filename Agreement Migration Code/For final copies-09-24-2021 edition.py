import requests
import os
import base64

import time
from json.decoder import JSONDecodeError

filesid = {
       205504 : "58549 - NLS 3373-3 Extension_BLS to Vanderbilt_Christie-Mi",
205490 : "59359 - UNIV59359_VUMC61674_FE_20210924",
205519 : "59517 - UNIV59517 (formerly 3844-019947)_H. Lee Moff. Canc",
205354 : "59799 - UNIV59799_UTSMC_Am 4_FE_20210921",
205347 : "59913 - UNIV59913_VUMC63572_Am 4_FE_20210921",
205388 : "60450 - UNIV60450_VUMC69289_Am 3_Final Draft_20210922",
205485 : "60484 - UNIV60484_ASU 033519 Das MOD05_FE_20210923",
205349 : "60534 - UNIV60534_VUMC68640_Am 3_FE_20210921",
205438 : "60639 - UNIV60639_VUMC70847-A3_FE_20210923",
205358 : "60811 - UNIV60811_BCH_A6_FE_20210922",
205402 : "61125 - UNIV61125_VUMC77338-A2_FE_20210922",
205377 : "61142 - UNIV61142_Fisk_A2_FE_20210922",
205342 : "61352 - UNIV61352_VUMC77235_FE_20210920",
205371 : "61437 - 80NSSC20K0424-AWARD DOCS (002)P00006 (1)",
205502 : "61484 - UNIV61484_Mass_core_A1_FE_20210924",
205432 : "61488 - UNIV61488_VUMC81686-A2_FE_20210923",
205433 : "61538 - UNIV61538_PGN_A2_FE_20210923",
205414 : "61798 - Amendment 1_BasePair_Vandy_PhaseII",
205380 : "61830 - Mod 2 - Vanderbilt RLS2-VB-399 Sub_signed",
205297 : "61867 - UNIV61867_UWSC12211_Am 1_Final Draft_20210921",
205378 : "61873 - 10012233 Mod. 2 F.E. Vanderbilt_",
205382 : "61873 - 10012907 AMD 1 EXEC",
205393 : "61900 - UNIV61900_VUMC87561_Am 1_Final Draft_20210922",
205368 : "61906 - UNIV61906_UCD_Am 2_PE_20210921",
205498 : "61910 - UNIV61910_VUMC87063-A1_FE_20210924",
205435 : "61965 - UNIV61965_Reg Univ of CA UC San Diego PITT KR 2738",
205374 : "62096 - Purchase Order for Services (1)",
205514 : "62368 - UNIV62368_VUMC93402_FE_20210924",
205493 : "62416 - UNIV62416_VUMC92816_FE_20210924",
205365 : "62447 - UNIV62447_NCState_FE_20210922",
205516 : "62462 - UNIV62462_LookingGlass_FE_20210924",
205512 : "62475 - UNIV62475_University of Washington_Final Draft_202",
205293 : "62478 - UNIV62478_LT_FE_20210921",
205366 : "62485 - UNIV62485_BI_FE_20210922",
205506 : "62491 - UNIV62491 MThomsen_VU_SPA_Research_Core_Agreement_",
          }

for x in filesid:
    
    response = requests.get("https://peer.app.vanderbilt.edu/index.php?controller=Api&call=getContractFile&fileId="+str(x)+"&token=dac9630aec642a428cd73f4be0a03569")

    try:
        time.sleep(1)
        message = response.json()["content"]
        message_bytes = message.encode('ascii')
        file = base64.b64decode(message_bytes)
        try:
              os.mkdir("/Users/everetmm/Desktop/Agreement_Migration_pt10/Contract_"+filesid[x][0:5])
              print("Directory " , filesid[x][0:5] ," Created ")
              open("/Users/everetmm/Desktop/Agreement_Migration_pt10/Contract_"+filesid[x][0:5]+"/(Original)Contract "+ filesid[x]+".pdf", 'wb').write(file)
        except FileExistsError:
              print("Directory " , filesid[x][0:5],  " already exists")
              open("/Users/everetmm/Desktop/Agreement_Migration_pt10/Contract_"+filesid[x][0:5]+"/(Original)Contract "+ filesid[x]+".pdf", 'wb').write(file)

        
    except JSONDecodeError:
        print("    ")
        print(str(x))
        print("    ")

