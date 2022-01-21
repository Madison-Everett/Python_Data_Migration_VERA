import requests
import os
import base64

import time
from json.decoder import JSONDecodeError

filesid = {
    200076 : "58517 - UNIV58517_VUMC63366-A4_FE_20210514",
    200031 : "58778 - UNIV58778_VUMC59496_FE_20210514",
    200013 : "59304 - UNIV59304 (formerly 3794-019687)-A5_FE_202010513",
    199883 : "59399 - UNIV59399_VUMC61472_Am 6_FE_20210511",
    199943 : "59572 - UNIV59572 (Krahn) EPI 10007945 AMD4 EXEC",
    199950 : "60034 - UNIV60034_CGI-Institute for Basic Science_Final Dr",
    199910 : "60370 - UNIV60370_VUMC65678_FE_20210511",
    199967 : "60444 - UNIV60444_OSU_FE_20210512",
    199894 : "60676 - UNIV60676_A2_FE_20210511",
    199905 : "60787 - UNIV60787_VUMC72178-A2_FE_20210511",
    199887 : "60821 - UNIV62060_Pitt_A1_FE_20210511",
    199963 : "60916 - UNIV60916_Emory_FE_20210512",
    200062 : "60954 - UNIV60954_Rector & Visitors of the Univ. of VA 02-",
    200021 : "61158 - UNIV61158_UCLA-A1_FE_20210514",
    199994 : "61341 - UNIV61341_TJU_A5_FE_20210513",
    199969 : "61353 - UNIV61353_SK_Am 1_FE_20210512",
    199864 : "61428 - UNIV61428_VUMC80270_Am 2_FE_20210511",
    200088 : "61442 - UNIV61442 Vanderbilt (Karsai) -w- AFRL Amend 4 FE ",
    199919 : "61499 - UNIV61499_University of Pittsburgh-A1_FE_20210511",
    199899 : "61635 - UNIV61635_VUMC83133-A1 SBA_FE_20210511",
    200113 : "61817 - UNIV61817_University of Pittsburgh AWD3241-A1_FE_2",
    200087 : "61825 - UNIV61825 (Bapty) -w- PMA209 CMP Vanderbilit P0000",
    200040 : "61953 - UNIV61953 Emory Updated DUC FE 14May21",
    199888 : "62060 - UNIV62060_IU_CORE_A1_FE_20210511",
    199998 : "62060 - UNIV62060_IU_CORE_A2_FE_20210513",
    199871 : "62098 - UNIV62098_VUMC90923_FE_20210511",
    200041 : "62142 - 5B51127-UNIV62142_Vanderbilt_Verdure Sciences FE 1",
    200122 : "62150 - UNIV62150_VUMC89804_FE_20210518",
    199992 : "62152 - UNIV62152 VU - CPI DelGiorno PI MTA non-clinical F",
    199915 : "62156 - UNIV62156_Subaward-A00-62549621-115277_FE__2021050",
    199932 : "62172 - UNIV62172_Carnegie Mellon A022631_Final Draft_2021",
    200007 : "62178 - UNIV62178_Texas Tech University_FE_20210513",
    200115 : "62205 - UNIV62205_VUMC91816_FE_20210514",
    200059 : "62213 - Vanderbilt_TO_001_FE (002)",
    200045 : "62214 - CMI2_Vanderbilt_Subk_210503_FE"
    }

for x in filesid:
    
    response = requests.get("https://peer.app.vanderbilt.edu/index.php?controller=Api&call=getContractFile&fileId="+str(x)+"&token=dac9630aec642a428cd73f4be0a03569")

    try:
        time.sleep(1)
        message = response.json()["content"]
        message_bytes = message.encode('ascii')
        file = base64.b64decode(message_bytes)
        try:
              os.mkdir("/Users/everetmm/Desktop/Missing/Contract_"+filesid[x][0:5])
              print("Directory " , filesid[x][0:5] ," Created ")
              open("/Users/everetmm/Desktop/Missing/Contract_"+filesid[x][0:5]+"/(Original)Contract "+ filesid[x]+".pdf", 'wb').write(file)
        except FileExistsError:
              print("Directory " , filesid[x][0:5],  " already exists")
              open("/Users/everetmm/Desktop/Missing/Contract_"+filesid[x][0:5]+"/(Original)Contract "+ filesid[x]+".pdf", 'wb').write(file)

        
    except JSONDecodeError:
        print("    ")
        print(str(x))
        print("    ")

