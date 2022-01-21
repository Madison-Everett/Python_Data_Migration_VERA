import requests
import os
import base64

import time
from json.decoder import JSONDecodeError

filesid = {
   204385 : "59970 - Your_Databrary_Access_Agreement",
    204381 : "60690 - UNIV60690_VUMC66698-A3_FE_20210831",
    204379 : "61056 - UNIV61056  VU (Kim) 5U1QHP33085 AMD 3 13Aug2021",
    204418 : "61455 - UNIV61455_Regents Univ of Minnesota-A1_FE_20210831",
    204384 : "61814 - UNIV61814_VUMC86934-A1_FE_20210831",
    204357 : "62064 - UNIV62064_UCSF NEW_P0551198_DUH_Q-Y_VANDERBILT_FE_",
    204375 : "62237 - UNIV62237_GE_FE_20210831",
    204363 : "62401 - RESEARCH LOAN AGREEMENT - PREOPERATIVE_VANDERBILT ",
    204399 : "62422 - UNIV62422_SNL_FE_20210831",
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

