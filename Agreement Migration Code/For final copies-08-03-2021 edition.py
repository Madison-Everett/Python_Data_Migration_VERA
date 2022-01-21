import requests
import os
import base64

import time
from json.decoder import JSONDecodeError

filesid = {
    202948 : "40157 - UNIV40157_MIHOW_FE_20210730",
203037 : "58990 - UNIV58990_VUMC60278_Am 5_FE_20210802",
202917 : "61065 - UNIV61065 NCE Amendment FE 29July21",
203025 : "61079 - UNIV61079_VCU_A2_FE_20210802",
202949 : "61477 - UNIV61477_VUMC85315_Am 1_FE_20210730",
202983 : "61546 - UNIV61546_Yr 2 Wits Health Consortium-A1_FE_202107",
203000 : "61735 - UNIV61735_Univ of Mass at Amherst Poudel-Tandukar-",
202987 : "61842 - UNIV61842_George Mason University-A1_FE_20210730",
203023 : "61847 - UNIV61847_Univ of Memphis-A1_FE_20210802",
202980 : "61868 - UNIV61868_PSCC-A1_FE_20210730",
202891 : "62017 - UNIV62017_NAI_A3_FE_20210729",
203019 : "62265 - UNIV62265_VUMC92130_Final Draft_20210726.fe",
203053 : "62270 - CT DOE CTDOE226522SEPBH1VANDERBI - FY22 Renewal - ",
203052 : "62303 - IPA - new - Aldrich - ECA - aok - July 2021",
203045 : "62310 - UNIV62310_VUMC93653_FE_20210803",
202976 : "62318 - UNIV62318_Hull 3200004065-21-348 Vanderbilt PO#780",
202915 : "62333 - UNIV62333_VUMC92750_Final Draft_20210729",
203051 : "62347 - SEAKR - VU Master Agreement for Sponsored Research"        }

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

