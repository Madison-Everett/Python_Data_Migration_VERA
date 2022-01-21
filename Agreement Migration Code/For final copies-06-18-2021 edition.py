import requests
import os
import base64

import time
from json.decoder import JSONDecodeError

filesid = {
    201240 : "58452 - UNIV58452_VUMC59882-A4_FE_20210617",
    201238 : "60184 - UNIV60184_VUMC66058_Am 6_FE_20210617",
    201234 : "60445 - UNIV60445_UVA_Am 2_Bilateral Agt_FE_20210617",
    201273 : "60557 - UNIV60557_VUMC71429_FE_20210601",
    201229 : "60584 - UNIV60584_VUMC69141_FE_20210617",
    201176 : "61131 - UNIV61131_University of Illinois 17584-02-Am 2_FE_",
    201173 : "61503 - UNIV61503_VUMC83145 A1_FE_20210615",
    201186 : "61512 - UNIV61512_VUMC82740-A2_FE_20210616",
    201293 : "61808 - UNIV61808_University of North Carolina, Greensboro",
    201287 : "62177 - UNIV62177_University of Alabama_Final Draft_202106",
    201297 : "62193 - UNIV62193_VUMC90495_FE_20210618",
    201191 : "62195 - U Minnesota - VU VAPR Core (Spiller) - SPA - Resea",
    201276 : "62238 - UNIV62238_Michigan State University_Final Draft_20",
    201216 : "62242 - UNIV62242_UVA_FE_20210616",
    201210 : "62278 - UNIV62278_UTC_core_FE_20210616"
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

