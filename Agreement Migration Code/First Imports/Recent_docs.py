import requests
import os
import base64
import time
from json.decoder import JSONDecodeError

filesid = {
##    197778 : '35318 - UNIV35318_UA_A12_FE_20210311', 
##    197529 : '57992 - 16X117 Modification 1X FE', 
##    197226 : '58389 - UNIV58389_VUMC60122_FE_20210222', 
##    197306 : '58519 - UNIV58519_VUMC59344_Am 10 FE_20201224', 
##    197378 : '58602 - UNIV58602_VUMC59770-A7_FE_20210225', 
##    197781 : '58623 - UNIV58623_VUMC59163_FE_20210311', 
##    197309 : '58727 - UNIV58727_VUMC60054_FE_20210224I', 
##    197468 : '59030 - UNIV59030_UTChattanooga_Amendment 8_Final Draft_20', 
##    197668 : '59360 - UNIV59360 (formerly 19067-S3)_Rutgers_Am 47-FE_202', 
##    197779 : '59394 - UNIV59394_HU_A33_FE_20210311', 
##    197640 : '59678 - UNIV59678_UN_Am 4 FE_20210305', 
##    197727 : '59725 - UNIV59725_Northwestern University-A04_FE_20210309', 
##    197685 : '59814 - UNIV59814_UO-A5_FE_20210305', 
##    197492 : '59914 - 5830-1526-00-B_mod_4', 
##    197587 : '60073 - UNIV60073_MIT_Final Draft_20210303_fe', 
##    197218 : '60096 - UNIV60096_VUMC64813-A3_FE_202102122', 
##    197761 : '60289 - CHLA  Laboratory Service Provider Agrmt Vanderbilt', 
##    197387 : '60498 - 1a_7000437184_CO02_Change Order', 
##    197193 : '60566 - UNIV60566_UTG_Am 2 FE_20210222', 
##    197496 : '60623 - Ancora - Amendment No. 3 to M4 Work Plan v1', 
##    197232 : '60631 - UNIV60631_Technische_Am 2 - FINAL FE_Redline FaceP', 
##    197411 : '60688 - Rev00000001 POCO Image', 
##    197330 : '60761 - UNIV60761_VUMC71103-A2_FE_20210224', 
##    197899 : '60763 - UNIV60763_MU_A3_FE_20210315', 
##    197323 : '60764 - UNIV60764_UC_FE_20210224', 
##    197556 : '60831 - UNIV60831_TSU_A2_FE_20210303', 
##    197702 : '60938 - UNIV60938 (Gualda Guilherme) -w- Nittetsu Mining N', 
##    197206 : '60981 - UNIV60981_Cornell University 78877-11227-A3_FE_202', 
##    197415 : '61199 - N00173-19-1-G020 P00003 INC SIGNED GF', 
##    197676 : '61215 - UNIV61215_UCSF 11603SC-01_FE_20210305', 
##    197897 : '61302 - TSI-4088-19-2020806VanderbiltMod1FE', 
##    197196 : '61341 - UNIV1341_TJU_FE_A3_20210222', 
##    197662 : '61368 - UNIV61368_VUMC71942-A1_FE_20210305', 
##    197534 : '61400 - UNIV61400_VTC 698_ AI149906_FE_20210302', 
##    197284 : '61409 - UNIV61409_State of TN Dept of Transportation-A1_FE', 
##    197649 : '61422 - UNIV61422_VUMC80507-A1_FE_20210304', 
##    197493 : '61427 - UNIV61427_BU_A1_FE_20210301', 
##    197254 : '61490 - UNIV61490_SR_A1_Core_FE_20210223', 
##    197374 : '61512 - UNIV61512_VUMC82740-A1_FE__20210225', 
##    197775 : '61562 - UNIV61562_University of Washington-A1_FE_20210311', 
##    197389 : '61673 - UNIV61673_Princeton University SUB0000392-A1_FE (U', 
##    197730 : '61683 - UNIV61683_University of Pennsylvania 4697401-A1_FE', 
##    197547 : '61710 - UNIV61710_VUMC84497_Am 1-FE_20210302', 
##    197666 : '61739 - UNIV61739_NEW_P0548735_Capra J_VANDERBILT_FE_20210', 
##    197829 : "61740 - UNIV61740 N99099N Mod 01 - Add'l Funds_FE", 
##    197886 : '61810 - Oregon - Addendum_OHSU_Maloyan_12Jan2021_(FE)', 
##    197750 : '61824 - UNIV61824 NPEF Contract Amendment FE 10March21', 
##    197748 : '61825 - UNIV61825 PMA209 CMP Vanderbilit P000000012 R1 MOD', 
##    197911 : '61834 - UNIV61834_Harris County Public Health 1110 Grants-', 
##    197734 : '61847 - UNIV61847_University of Memphis_FE_20210309', 
##    197251 : '61909 - UNIV61909_Soleno_FE_20210223', 
##    197407 : '61915 - Vanderbilt TBR Subgrant Contract_109249 02242021 (', 
##    197531 : '61922 - VU - 48116 gap svcs', 
##    197509 : '61944 - UNIV61944 LifeMine_Vanderbilt Mutual CDA - FE 1Mar', 
##    197898 : '61950 - UNIV61950_3M_FE_20210312', 
##    197334 : '61956 - UNIV61956_VUMC81171_FE_20210224', 
##    197261 : '61963 - UNIV61963_ET_FE_20210223', 
##    197872 : '61967 - Navigo Proteins_3 WAY CDA_04-12-2020 (002)_KG (002', 
##    197288 : '61969 - UNIV61969_Regets of the University of Michigan AWD', 
##    197325 : '61988 - UNIV61988_VUMC85037_FE_20210224', 
##    197701 : '62002 - UNIV62002_Washington University_Final Draft_202103', 
##    197652 : '62003 - UNIV62003_VUMC89827_FE SBA for Dang_20210304', 
##    197229 : '62010 - UNIV62010_Univ of VA-Charlosttesville 02 - GB10884', 
##    197842 : '62011 - UCSF - VU_SPA_-_Research_Core_Agrmt (03.12.21)(FE)', 
##    197721 : '62013 - UNIV62013_MMC_FE_20210305', 
##    197495 : '62014 - UNIV62014 VU -w- Rentec STTR FullyExec 1March21', 
##    197623 : '62025 - UNIV62025_UVA_Final Draft_20210304', 
##    197426 : '62033 - UNIV62033_University of Utah_Final Draft_20210226', 
##    197746 : '62038 - UNIV62038_VUMC87548_Final Draft_20210310', 
##    197520 : '62039 - UNIV62039_UH_FE_20210302', 
##    197659 : '62042 - FE_UNIV62042_Florida International University 0003', 
##    197270 : '62043 - Murry_20135-VU_Contract_FE_2.18.21', 
##    197905 : '62046 - UNIV62046_CREE_FE_20210315', 
##    197601 : '62048 - UNIV62048_VUMC88723_Melancon SBA_FE_20210303', 
##    197423 : '62052 - UNIV62052_Hamilton College_Final Draft_20210226', 
##    197252 : '62059 - UNIV62059_CRUK_CORE_FE_2021022', 
##    197194 : '62060 - UNIV62060_IU_Core_FE_20210222', 
##    197722 : '62070 - UNIV62070_LBS_DUA_FE_20210305', 
##    197894 : '62074 - UNIV62074 Vanderbilt (Marcus) -w- Environmental Wo', 
##    197606 : '62075 - UNIV62075 Vanderbilt (Reyzer Michelle) -w- Denali', 
##    197733 : '62081 - 4ZZ4101-VanderbiltUniversity and PPG NDA (Final-03', 
##    197914 : '62084 - UNIV62084_University of Delaware R305E190002_PO586', 
##    197879 : '62086 - VA Commonwealth U - VU Syn Core - VICB-539-synthes', 
##    197841 : '62089 - Mathematica TA -  Vanderbilt (Goldring) 3 11 21_cl', 
##    197753 : '62090 - UNIV62090_Vanderbilt_(Zhou_Xingyu)_-w-_Carle_Found', 
##    197882 : '62091 - Cincinnati Childrens Hosp - VU Chem Syn - Research', 
#     197770 : '62094 - UNIV62094_Qorvo_FE_20210310', 
    197888 : '62102 - Renesas Electronics - VU ISDE (Reed) Core Agmt - (' #Doesnt exist
    }


for x in filesid:
    response = requests.get("https://peer.app.vanderbilt.edu/index.php?controller=Api&call=getContractFile&fileId="+str(x)+"&token=dac9630aec642a428cd73f4be0a03569")

    try:
        time.sleep(1)
        message = response.json()["content"]
        message_bytes = message.encode('ascii')
        file = base64.b64decode(message_bytes)
        try:
              os.mkdir("/Users/everetmm/Desktop/Agreement_Migration_pt2/Contract_"+filesid[x][0:5])
              print("Directory " , filesid[x][0:5] ," Created ")
              open("/Users/everetmm/Desktop/Agreement_Migration_pt2/Contract_"+filesid[x][0:5]+"/Contract "+ filesid[x]+".pdf", 'wb').write(file)
        except FileExistsError:
              print("Directory " , filesid[x][0:5],  " already exists")
              open("/Users/everetmm/Desktop/Agreement_Migration_pt2/Contract_"+filesid[x][0:5]+"/Contract "+ filesid[x]+".pdf", 'wb').write(file)
        
    except JSONDecodeError:
        print("    ")
        print(str(x))
        print("    ")






