import requests
import os
import base64
import time
from json.decoder import JSONDecodeError

filesid = {
    167267 : '59914 - UNIV59914-USF-Hemmeter-SRA-11.28.2018-FE',
    194972 : '59914 - 5830-1526-00-B_mod_3 (002)',
    167396 : '59914 - 5830-1526-00-B_Yr_2',
    180654 : '59914 - 5830-1526-00-B_mod_2',
    197492 : '59914 - 5830-1526-00-B_mod_4',
    157024 : '59914 - 5830-1526-00-B_sub_waiver FE',
    157025 : '59914 - 5830-1526-00-B_sub_waiver FE',
    167395 : '59914 - 5830-1526-00-B_Yr_2',
    167040 : '60498 - 7000437184 final',
    167041 : '60498 - 7000437184 final',
    188998 : '60498 - Renewal PO (1)',
    197387 : '60498 - 1a_70004toot37184_CO02_Change Order',
    194407 : '58602 - UNIV58602_VUMC59770-A6_FE_20201119',
    163164 : '58602 - UNIV58602_VUMC59770_A2_20180720',
    179222 : '58602 - UNIV58602-VUMC59770-A3-FE-051319-2 with comments 2',
    150654 : '58602 - UNIV58602_VUMC59770_A1_FE_20170719',
    150655 : '58602 - UNIV58602_VUMC59770_A1_FE_20170719',
    180346 : '58602 - UNIV58602_VUMC59770-A4_FE_20191112',
    163165 : '58602 - UNIV58602_VUMC59770_A2_20180720',
    189845 : '58602 - 20200805165151_VUMC59770_ce5Y4',
    189846 : '58602 - UNIV58602_VUMC59770-A5_FE_20200806',
    189848 : '58602 - UNIV58602_VUMC59770-A5_FE_20200806',
    179221 : '58602 - UNIV58602_VUMC59770_A2_20180720-2 with comments 20',
    172689 : '58602 - 59770A3F',
    172690 : '58602 - UNIV58602-VUMC59770-A3-FE-051319',
    172692 : '58602 - UNIV58602-VUMC59770-A3-FE-051319',
    113780 : '58602 - UNIV58602_VUMC59770C1F_FE_4224200043',
    113781 : '58602 - UNIV58602_VUMC59770C1F_FE_4224200043',
    194409 : '58602 - UNIV58602_VUMC59770-A6_FE_20201119',
    197376 : '58602 - UNIV58602_VUMC59770-A7_FE_20210225',
    197378 : '58602 - UNIV58602_VUMC59770-A7_FE_20210225',
    180345 : '58602 - 20191108143707_VUMC59770_R7QfJ',
    180348 : '58602 - UNIV58602_VUMC59770-A4_FE_20191112',
    197623 : '62025 - UNIV62025_UVA_Final Draft_20210304',
    197374 : '61512 - UNIV61512_VUMC82740-A1_FE__20210225',
    187789 : '61512 - UNIV61512_VUMC82740_FE_20200616',
    187791 : '61512 - UNIV61512_VUMC82740_FE_20200616'
   
    }


for x in filesid:
    response = requests.get("https://peer.app.vanderbilt.edu/index.php?controller=Api&call=getContractFile&fileId="+str(x)+"&token=dac9630aec642a428cd73f4be0a03569")

    try:
        time.sleep(1)
        message = response.json()["content"]
        message_bytes = message.encode('ascii')
        file = base64.b64decode(message_bytes)
        try:
              os.mkdir("/Users/everetmm/Desktop/toot/Contract_"+filesid[x][0:5])
              print("Directory " , filesid[x][0:5] ," Created ")
              open("/Users/everetmm/Desktop/toot/Contract_"+filesid[x][0:5]+"/Contract "+ filesid[x]+".pdf", 'wb').write(file)
        except FileExistsError:
              print("Directory " , filesid[x][0:5],  " already exists")
              open("/Users/everetmm/Desktop/toot/Contract_"+filesid[x][0:5]+"/Contract "+ filesid[x]+".pdf", 'wb').write(file)
        
    except JSONDecodeError:
        print("    ")
        print(str(x))
        print("    ")






