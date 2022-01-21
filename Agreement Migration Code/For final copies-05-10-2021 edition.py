import requests
import os
import base64

import time
from json.decoder import JSONDecodeError

filesid = {
    199618 : "58254 - UNIV58254_WU_FE_20210504",
    199238 : "58623 - UNIV58623_VUMC59163-A3_FE_20210423",
    199803 : "58822 - UNIV58822_VUMC59469_Am 4_FE_20210507",
    199799 : "59360 - UNIV59360_Rutgers_Am 48_FE_20210506",
    199218 : "59587 - UNIV59587_NW_Am 4_FE_20210422",
    199514 : "59610 - UNIV59610_University of Pittsburgh_Final Draft Am ",
    199257 : "59824 - Northwestern U - VUSPA-ResearchCoreAddendum-Larond",
    199575 : "59891 - U.Colorado - OwensVU_SPA_Research_Core_Addendum040",
    199352 : "59931 - 18-D-0010 DO 4 Mod 05 fully executed",
    199485 : "60064 - UNIV60064_VUMC64648-A3_FE_20210430",
    199308 : "60079 - UNIV60079_UM_A3_FE_20210426",
    199677 : "60098 - UNIV60098_Rowan_FE_20210505",
    199598 : "60178 - UNIV60178_UM_A3_FE_20210504",
    199241 : "60201 - UNIV60201_VUMC 64863_A3_FE_20210423",
    199556 : "60201 - UNIV60201_VUMC 64863_A5_FE_20210503",
    199333 : "60215 - UNIV60215_UNC-CH_FE_20210426",
    199285 : "60425 - UNIV60425_Berea_Am 4_FE_20210426",
    199292 : "60609 - UNIV60609_TDOT_A2_FE_20210426",
    199455 : "60826 - UNIV60826_Univ of TX Med Branch at Galveston SUBK ",
    199824 : "60829 - UNIV60829_Duke_Am 2_FE_20210510",
    199444 : "60848 - UNIV60848_VUMC73417_FE_20210428F",
    199426 : "60860 - UNIV60860_VUMC72234_Am 4_Qi SBA_FE_20210428",
    199233 : "60950 - UNIV60950_VUMC74777_FE_20210423",
    199630 : "61040 - UNIV61040_VUMC77021-A2_FE_20210504",
    199501 : "61065 - Securboration - VU (Schmidt) - FA8650-19-C-2934-SC",
    199801 : "61093 - UNIV61093_VUMC76112_Am 2_FE_20210506",
    199361 : "61166 - UNIV61166_VUMC80654-A2_FE_20210423",
    199537 : "61194 - UNIV61194_University of Pittsburgh-A3_FE_20210430",
    199699 : "61292 - UNIV61292_VUMC80359-A1_FE_20210505",
    199289 : "61322 - UNIV61322_VUMC_Am 4_Liu SBA_FE_20210426",
    199287 : "61323 - UNIV61323_VUMC_Am 4_Wang SBA_FE_20210426",
    199740 : "61341 - UNIV1341_TJU_FE_A4_20210506",
    199489 : "61364 - UNIV61364_VUMC79022_Am 2_FE_20210430",
    199235 : "61366 - Toyota (TEMA) - CW2524321_2020VAN001-A02_VU - Amen",
    199410 : "61392 - UNIV61392_VUMC_FE_20210428",
    199189 : "61453 - UNIV61453_GS_A1_FE_20210422",
    199338 : "61471 - UNIV61471_VUMC81396_Am 1_FE_20210426",
    199432 : "61493 - UNIV61493_VUMC82497-A1_FE_20210428",
    199547 : "61518 - UNIV61518_NW_FE_202100530",
    199328 : "61521 - UNIV61521_VUMC81649-A1_FE",
    199549 : "61561 - UNIV61561_VUMC83991_FE_20210430",
    199655 : "61589 - UNIV61589_Univ of Chicago AWD101175 (SUB00000282)-",
    199776 : "61614 - UNIV61614_DATA Opinion Publica y Mercados-Am 3_FE_",
    199532 : "61670 - UNIV61670_NCSU 20-0353-A2_FE_20210430",
    199744 : "61746 - UNIV61746_MGH Polimeni_Grissom_5R01EB019437-06_VU_",
    199834 : "61752 - UNIV61752_VUMC_FE_20200510",
    199325 : "61758 - UNIV61758_VUMC82169_Am 2_FE_20210426",
    199789 : "61816 - UNIV61816_John Hopkins University 33682-A1_FE_2021",
    199733 : "61820 - UNIV61820_University of Szeged-A1_FE_20210506",
    199222 : "61841 - PE-UNIV61841_UW_Am 1_NCE_FE_20210422",
    199375 : "61845 - UNIV61845_Fisk University_FE_20210427",
    199249 : "61892 - UNIV61892 Vanderbilt (Warren) -w- Sandia PO_TERMS_",
    199612 : "61948 - UNIV61948_ASIES_Am 1_FE_20210504",
    199734 : "62054 - 4_FA_69455_34570-91622_Signed",
    199608 : "62062 - UNIV62062_UA_FE_20210504",
    199363 : "62087 - UNIV62087 Vanderbilt (Camp, Janey) -w- State of Te",
    199418 : "62092 - UNIV62092_Georgia Southern University_Final Draft_",
    199336 : "62111 - UNIV62111_Emory University_SC10413_NEW_VANDERBILT_",
    199372 : "62112 - UNIV62112_Salk InstituteA20-0026-S001_Final Draft_",
    199557 : "62119 - UNIV62119_NIDA_FE_20210503",
    199761 : "62122 - UNIV62122_Massachusetts General_Final Draft_202105",
    199759 : "62128 - UNIV62128_Univ. of N. Texas 2021-0125_FE_20210507",
    199306 : "62133 - UNIV62133_AWD00002020 (134625-1) Vanderbuilt Unive",
    199602 : "62141 - ClinicalResearchFundingAgreement_CHDI_VanderbiltUn",
    199369 : "62151 - UNIV62151_Columbia University_Final Draft_20210427",
    199833 : "62154 - UNIV62154_BORGE Y ASOCIADOS SOCIEDAD ANONIMAS_FE_2",
    199666 : "62155 - UNIV62155_Sloan-Kettering Institute_Final Draft_20",
    199399 : "62160 - UNIV62160 McLean Pfizer - Scientic Evaluation Agre",
    199727 : "62167 - MNDA Carbon with Vanderbilt University FE 4May21",
    199504 : "62168 - UNIV62168_UNT_NIH_CDA_FE_20210430",
    199503 : "62171 - NIH NIDDK - VU MMPC - PO_75N94021P00280-with core ",
    199483 : "62184 - UNIV62184_VUMC89680_FE_20210430",
    199738 : "62196 - UNIV62196_UBC_Core_FE_20210506"
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

