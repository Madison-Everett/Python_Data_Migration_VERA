import requests
import os
import base64
import time
from json.decoder import JSONDecodeError

filesid = {

    188991 : "60950 - UNIV60950_VUMC_SBA FE_20200720",
    188990 : "60950 - UNIV60950_VUMC_SBA FE_20200720",
    174916 : "60950 - UNIV60950_VUMC74777_FE_070319 mw",
    199232 : "60950 - UNIV60950_VUMC74777_FE_20210423",
    199233 : "60950 - UNIV60950_VUMC74777_FE_20210423",
    174917 : "60950 - UNIV60950_VUMC74777_FE_070319 mw",
    188387 : "61090 - UNIV61090_UWM_A1_FE",
    178803 : "61090 - UNIV61090_UWM_FE_20191001",
    199242 : "61090 - UNIV61090_UWM_A2_FE_20210423",
    183294 : "61366 - TEMA-Vanderbilt NDA (22562-4622)_(15930427)_(2) (F",
    184280 : "61366 - TEMA-Vanderbilt ARA (Y. Song) (22562-4634)(FINAL-4",
    199234 : "61366 - Toyota (TEMA) - CW2524321_2020VAN001-A02_VU - Amen",
    199235 : "61366 - Toyota (TEMA) - CW2524321_2020VAN001-A02_VU - Amen",
    194496 : "61366 - Toyota (TEMA) ARA.1629.03 Vanderbilt University - ",
    192231 : "61366 - Pajarito Powder - VU (Pintauro) - Mutual NDA - Ame",
    184276 : "61366 - TEMA-Vanderbilt ARA (Y. Song) (22562-4634)(FINAL-4",
    184277 : "61366 - TEMA-Vanderbilt ARA (Y. Song) (22562-4634)(FINAL-4",
    154507 : "58623 - UNIV58623_VUMC59163_A2_FE_20171020",
    154508 : "58623 - UNIV58623_VUMC59163_A2_FE_20171020",
    145492 : "58623 - UNIV58623_VUMC59163_A1_FE_20160316",
    174918 : "58623 - UNIV58623_VUMC59163-New_2019-FE-070319",
    197781 : "58623 - UNIV58623_VUMC59163_FE_20210311",
    158877 : "58623 - UNIV58623_VUMC59163_A3_FE_20180309",
    158878 : "58623 - UNIV58623_VUMC59163_A3_FE_20180309",
    164042 : "58623 - UNIV58623_VUMC59163-A4_FE_20180820",
    164043 : "58623 - UNIV58623_VUMC59163-A4_FE_20180820",
    112060 : "58623 - UNIV58623 VUMC59163 FINAL",
    174922 : "58623 - UNIV58623_VUMC59163-A6-revised-Working Draft-06181",
    199236 : "58623 - 20210423084551_VUMC59163_RVpGN",
    199238 : "58623 - UNIV58623_VUMC59163-A3_FE_20210423",
    167461 : "58623 - UNIV58623_VUMC59163-A5_FE_20181204",
    167462 : "58623 - UNIV58623_VUMC59163-A5_FE_20181204",
    145491 : "58623 - UNIV58623_VUMC59163_A1_FE_20160316",
    174919 : "58623 - UNIV58623_VUMC59163-New_2019-FE-070319",
    174921 : "58623 - UNIV58623_VUMC59163-New_2019-FE-070319",
    186493 : "58623 - 20200430141634_VUMC59163_awVCS",
    186495 : "58623 - UNIV58623_VUMC59163-A1_FE_20200511",
    197777 : "58623 - UNIV58623_VUMC59163_FE_20210311",
    112058 : "58623 - UNIV58623 VUMC59163 FINAL",
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






