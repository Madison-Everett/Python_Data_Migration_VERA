import requests
import os
import base64

import time
from json.decoder import JSONDecodeError

filesid = {
    203119 : "59646 - UNIV59646_VUMC63022-A3_FE_20210804_",
203116 : "61845 - UNIV61845 Fisk University-A1_FE_20210804",
203122 : "62305 - Vanderbilt_Research_Agreement___Neurochemistry_Mic",
203121 : "62315 - UNIV62315_VUA00-62628788-199245-FX_FE_20210804",
203113 : "62341 - NPUA-21-009 Vanderbilt University",




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

