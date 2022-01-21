import requests
import os
import base64

import time
from json.decoder import JSONDecodeError

filesid = {
    186216 : "61446 - Busek - VU (Witulski) - NDA 20200415 (FE)",
    184044 : "59425 - Thomas Jefferson U - Eischen VU_SPA_Research_Core_",
    178121 : "61049 - CDA - Medicenna - Vanderbilt (Fingleton) - VU Sign",
    170145 : "60674 - Zillow - DocuSign_ZTRAX_Data_Agreement (Final)(FE)",
    195602 : "61154 - QSI-DSC-19-009_12172020-NCE Amend 1 (PE)(FE)",
    150206 : "59496 - UNIV59496_Boeing-PIA-2017-3665_FE_20170711",
    160376 : "60161 - Nanosys-Vanderbilt - NDA - Nanosys-signed-mcbride ",
    167023 : "60408 - UNIV60408-TDOT-Dubey-VideoSharingAgreement-FE-11.1",
    180465 : "61068 - Collab_LUMICKS_Vanderbilt_20191115 (Fully Executed",
    185895 : "61389 - 23andMe - VU (Li) - SOW2_FullEx_18MAR2020",
    164138 : "60363 - Sensera-Vanderbilt (Weiss) NDA (FE-08.20.18)",
    171751 : "60767 - UNIV60767_UCSF_A1_FE_041619",
    161059 : "60172 - MOU btw ORAU and Vanderbilt",
    185222 : "61421 - 1 Metavivor - VU (Fingleton)(FE)",
    193724 : "61337 - UNIV61337 Dougherty External Research Partner Agre",
    199045 : "62144 - L3Harris (IEC) - PO SW11-00095-00 with VU Edits 04",
    198834 : "59827 - UNIV59827_VUMC63383_FE_20210412",
    199608 : "62062 - UNIV62062_UA_FE_20210504",
    199834 : "61752 - UNIV61752_VUMC_FE_20200510",
    185898 : "61274 - KCC - VU (Vito Quaranta) - Data and Collaboration ",
    175085 : "60965 - UNIV60965_PCI Synthesis_Fully Executed",
    195217 : "59924 - 67050 Vanderbilt",
    169734 : "60627 - Exhibit A Vanderbilt Ancora - M5 Jones Lindsley Re",
    191479 : "61425 - VU Ctr Innov.Tech. - European Inst. Oncology - Cor"
    }

for x in filesid:
    
    response = requests.get("https://peer.app.vanderbilt.edu/index.php?controller=Api&call=getContractFile&fileId="+str(x)+"&token=dac9630aec642a428cd73f4be0a03569")

    try:
        time.sleep(1)
        message = response.json()["content"]
        message_bytes = message.encode('ascii')
        file = base64.b64decode(message_bytes)
        try:
              os.mkdir("/Users/everetmm/Desktop/yayy/Contract_"+filesid[x][0:5])
              print("Directory " , filesid[x][0:5] ," Created ")
              open("/Users/everetmm/Desktop/yayy/Contract_"+filesid[x][0:5]+"/(Original)Contract "+ filesid[x]+".pdf", 'wb').write(file)
        except FileExistsError:
              print("Directory " , filesid[x][0:5],  " already exists")
              open("/Users/everetmm/Desktop/yayy/Contract_"+filesid[x][0:5]+"/(Original)Contract "+ filesid[x]+".pdf", 'wb').write(file)

        
    except JSONDecodeError:
        print("    ")
        print(str(x))
        print("    ")
        
   


