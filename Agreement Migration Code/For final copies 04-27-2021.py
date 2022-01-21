import requests
import os
import base64

import time
from json.decoder import JSONDecodeError

filesid = {
    58623 : "199238 - UNIV58623_VUMC59163-A3_FE_20210423",
    59587 : "199218 - UNIV59587_NW_Am 4_FE_20210422",
    59824 : "199257 - Northwestern U - VUSPA-ResearchCoreAddendum-Larond",
    60079 : "199308 - UNIV60079_UM_A3_FE_20210426",
    60201 : "199241 - UNIV60201_VUMC 64863_A3_FE_20210423",
    60215 : "199333 - UNIV60215_UNC-CH_FE_20210426",
    60425 : "199285 - UNIV60425_Berea_Am 4_FE_20210426",
    60609 : "199292 - UNIV60609_TDOT_A2_FE_20210426",
    60950 : "199233 - UNIV60950_VUMC74777_FE_20210423",
    61090 : "199242 - UNIV61090_UWM_A2_FE_20210423",
    61322 : "199289 - UNIV61322_VUMC_Am 4_Liu SBA_FE_20210426",
    61323 : "199287 - UNIV61323_VUMC_Am 4_Wang SBA_FE_20210426",
    61366 : "199235 - Toyota (TEMA) - CW2524321_2020VAN001-A02_VU - Amen",
    61453 : "199189 - UNIV61453_GS_A1_FE_20210422",
    61471 : "199338 - UNIV61471_VUMC81396_Am 1_FE_20210426",
    61521 : "199328 - UNIV61521_VUMC81649-A1_FE",
    61758 : "199325 - UNIV61758_VUMC82169_Am 2_FE_20210426",
    61841 : "199222 - PE-UNIV61841_UW_Am 1_NCE_FE_20210422",
    61892 : "199249 - UNIV61892 Vanderbilt (Warren) -w- Sandia PO_TERMS_",
    62111 : "199336 - UNIV62111_Emory University_SC10413_NEW_VANDERBILT_",
    62133 : "199306 - UNIV62133_AWD00002020 (134625-1) Vanderbuilt Unive",
    }

for x in filesid:
    
    response = requests.get("https://peer.app.vanderbilt.edu/index.php?controller=Api&call=getContractFile&fileId="+str(x)+"&token=dac9630aec642a428cd73f4be0a03569")

    try:
        time.sleep(1)
        message = response.json()["content"]
        message_bytes = message.encode('ascii')
        file = base64.b64decode(message_bytes)
        try:
              os.mkdir("/Users/everetmm/Desktop/redo/Contract_"+filesid[x][0:5])
              print("Directory " , filesid[x][0:5] ," Created ")
              open("/Users/everetmm/Desktop/redo/Contract_"+filesid[x][0:5]+"/(Original)Contract "+ filesid[x]+".pdf", 'wb').write(file)
        except FileExistsError:
              print("Directory " , filesid[x][0:5],  " already exists")
              open("/Users/everetmm/Desktop/redo/Contract_"+filesid[x][0:5]+"/(Original)Contract "+ filesid[x]+".pdf", 'wb').write(file)

        
    except JSONDecodeError:
        print("    ")
        print(str(x))
        print("    ")
        
   


