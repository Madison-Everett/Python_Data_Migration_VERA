import requests
import os
import base64

import time
from json.decoder import JSONDecodeError

filesid = {
    200985 : "58780 - UNIV58780_Regents of the University of Minnesota_F",
    200974 : "58832 - UNIV58832 Vanderbilt -w- MNPS_ Day of Discovery Ag",
    201104 : "59366 - UNIV59366_OSU_FE_20210614",
    201002 : "59931 - 18-D-0010 DO 6  fully executed",
    201009 : "60027 - UNIV60027_UCB_A5_FE_20210611",
    201092 : "60559 - UNIV60559_CRISP_FE_20210614",
    201071 : "60612 - UNIV60612_UNC-CH_A1_FE_20210614",
    201056 : "60798 - UNIV60798_NCST_A3_FE_20210614",
    201106 : "60920 - UNIV60920_UIL_FE_20210614",
    201078 : "61449 - EPRI - Vanderbilt 10012233 Mod. 1 FULLY EXECUTED (",
    200990 : "61558 - UNIV 61558_VUMC 76761_AM 1_Final Draft_20210610",
    201094 : "61698 - UNIV61698_VUMC84645-A1_FE_20210615",
    201114 : "61749 - UNIV61749_VUMC86131_FE_20210614",
    200907 : "61918 - UNIV61918 LO for PO 2210612 Sandia AlGaN_ Witulski",
    200894 : "61936 - UNIV61936 Vanderbilt -w- Amendment-TERA CIRN Suppo",
    200914 : "61942 - UNIV61942_VUMC87452_Am 1_FE_20210608",
    200964 : "62040 - UNIV62040_VUMC86181-A1_FE_2021609",
    201100 : "62107 - UNIV62107_VUMC91166_FE_20210615",
    201074 : "62118 - UNIV62118 VU -w- CCF - 4238295 FE DUA 14June21",
    200954 : "62148 - UNIV62148_VUMC6838-A2_FE_20210609",
    200911 : "62202 - CCSC (IACMI) - Prescott Composites - VU (Adams) -",
    201022 : "62206 - RIGImmune - Vanderbilt NDA _ RIGImmune Executed -",
    200945 : "62236 - UNIV62236_VUMC84045_FE_20210608",
    201075 : "62249 - UNIV62249 Vanderbilt University -w- University of",
    201070 : "62258 - State of TN P20 Connect - VU (Corcoran)_External R"
    
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

