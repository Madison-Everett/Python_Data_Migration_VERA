import requests
import os
import base64

import time
from json.decoder import JSONDecodeError

filesid = {
    204595 : "59322 - VU-Accenture MRA - Amendment August 2021 - signed",
    204673 : "60204 - UNIV60204_VUMC65595_AM 4_Final Draft_20210903",
    204603 : "60352 - UNIV60352_Indiana Universit Sub 8076-A3_FE_2021090",
    204631 : "60720 - UNIV60720_Fisk University_Am 3_Final Draft_2021090",
    204660 : "60834 - UNIV60834_BU_PE_20210902 approved",
    204655 : "61173 - TDOE_DUA_Amd 2_Vanderbilt TERA_FINAL",
    204658 : "61199 - N00173-19-1-G020 P00004 INC KO signed",
    204589 : "61404 - UNIV61404_FII_A2_FE_20210901",
    204625 : "61734 - UNIV61734_Yale Univ-A1_FE_20210902",
    204628 : "61748 - UNIV61748_VUMC85210_FE_20210902",
    204607 : "61818 - UNIV61818_VUMC84387-A1_FE_20210902",
    204620 : "62189 - 7603622 Vanderbilt NAWI (FE",
    204639 : "62198 - UNIV62198_Florida International University 000441_",
    204588 : "62276 - UNIV62276_VUMC94946_FE_20210902",
    204649 : "62351 - UNIV62351_UWSC12923_FE_20210902",
    204676 : "62370 - UNIV62370_Augusta University_33737-19_FE_20210903",
    204708 : "62400 - UNIV62400_VUMC93904_Final Draft_20210907",
    204600 : "62415 - UNIV62415_Carle_Foundation_Hospital_FE_20210902",
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

