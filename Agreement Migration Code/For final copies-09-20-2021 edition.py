import requests
import os
import base64

import time
from json.decoder import JSONDecodeError

filesid = {
       205154 : "58254 - UNIV58254_UWM_FE_20210917",
205179 : "59016 - UNIV59016_VUMC61264_Am 4_FE_20210917",
205234 : "59353 - UNIV59353_Ark_A7_FE_20210920",
205163 : "59953 - UNIV59953_UCB_Am 5_FE_20210917",
205231 : "60418 - UNIV60418_VUMC68022-A3_FE_20210920",
205229 : "60799 - UNIV60799_Urban Institute-Am 3_FE VU Initialed_202",
205150 : "60916 - UNIV60916_Emory_FE_20210917",
205195 : "61118 - UNIV61118_CHOP_Am 2_FE_20210917",
205181 : "61136 - UNIV61136_KPPT_Am 5_FE_20210917",
205222 : "61165 - UNIV61165_Univ of Illinois 096585-17524-02-Boppart",
205165 : "61354 - UNIV61354_VUMC79040_Am 3_FE_20210917",
205183 : "61733 - UNIV61733_GATech_Am 1_FE_20210917",
205203 : "62283 - UNIV62283_University of Sheffield_Final Draft_2021",
205208 : "62402 - UNIV62402_TBR_FE_20210917",
205188 : "62405 - UNIV62405_UCCS_FE_20210917",
205235 : "62445 - UNIV62445_NI_FE_20210920",
205233 : "62456 - UNIV62456_Mayo_FE_20210920",
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

