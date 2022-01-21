import requests
import os
import base64
import time
from json.decoder import JSONDecodeError

filesid = {
    199217 : "59587 - UNIV59587_NW_Am 4_FE_20210422",
    199218 : "59587 - UNIV59587_NW_Am 4_FE_20210422",
    199221 : "61841 - PE-UNIV61841_UW_Am 1_NCE_FE_20210422",
    199222 : "61841 - PE-UNIV61841_UW_Am 1_NCE_FE_20210422",
    199232 : "60950 - UNIV60950_VUMC74777_FE_20210423",
    199233 : "60950 - UNIV60950_VUMC74777_FE_20210423",
    199234 : "61366 - Toyota (TEMA) - CW2524321_2020VAN001-A02_VU - Amen",
    199235 : "61366 - Toyota (TEMA) - CW2524321_2020VAN001-A02_VU - Amen",
    199236 : "58623 - 20210423084551_VUMC59163_RVpGN",
    199238 : "58623 - UNIV58623_VUMC59163-A3_FE_20210423",
    199249 : "61892 - UNIV61892 Vanderbilt (Warren) -w- Sandia PO_TERMS_",
    199332 : "60215 - UNIV60215_UNC-CH_FE_20210426",
    199333 : "60215 - UNIV60215_UNC-CH_FE_20210426",
    199256 : "59824 - Northwestern U - VUSPA-ResearchCoreAddendum-Larond",
    199284 : "60425 - UNIV60425_Berea_Am 4_FE_20210426",
    199285 : "60425 - UNIV60425_Berea_Am 4_FE_20210426",
    199286 : "61323 - UNIV61323_VUMC_Am 4_Wang SBA_FE_20210426",
    199287 : "61323 - UNIV61323_VUMC_Am 4_Wang SBA_FE_20210426",
    199288 : "61322 - UNIV61322_VUMC_Am 4_Liu SBA_FE_20210426",
    199289 : "61322 - UNIV61322_VUMC_Am 4_Liu SBA_FE_20210426",
    199292 : "60609 - UNIV60609_TDOT_A2_FE_20210426",
    199324 : "61758 - UNIV61758_VUMC82169_Am 2_FE_20210426",
    199325 : "61758 - UNIV61758_VUMC82169_Am 2_FE_20210426",
    199334 : "62111 - UNIV62111_Emory University_SC10413_NEW_VANDERBILT_",
    199336 : "62111 - UNIV62111_Emory University_SC10413_NEW_VANDERBILT_",
    199189 : "61453 - UNIV61453_GS_A1_FE_20210422",
    199241 : "60201 - UNIV60201_VUMC 64863_A3_FE_20210423",
    199306 : "62133 - UNIV62133_AWD00002020 (134625-1) Vanderbuilt Unive",
    199308 : "60079 - UNIV60079_UM_A3_FE_20210426",
    199327 : "61521 - UNIV61521_VUMC81649-A1_FE",
    199328 : "61521 - UNIV61521_VUMC81649-A1_FE",
    199337 : "61471 - UNIV61471_VUMC81396_Am 1_FE_20210426",
    199338 : "61471 - UNIV61471_VUMC81396_Am 1_FE_20210426",
    199242 : "61090 - UNIV61090_UWM_A2_FE_20210423",
    199257 : "59824 - Northwestern U - VUSPA-ResearchCoreAddendum-Larond",
    199304 : "62133 - UNIV62133_AWD00002020 (134625-1) Vanderbuilt Unive"
    
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
              open("/Users/everetmm/Desktop/redo/Contract_"+filesid[x][0:5]+"/Contract "+ filesid[x]+".pdf", 'wb').write(file)
        except FileExistsError:
              print("Directory " , filesid[x][0:5],  " already exists")
              open("/Users/everetmm/Desktop/redo/Contract_"+filesid[x][0:5]+"/Contract "+ filesid[x]+".pdf", 'wb').write(file)
        
    except JSONDecodeError:
        print("    ")
        print(str(x))
        print("    ")






