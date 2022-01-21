import requests
import os
import base64

import time
from json.decoder import JSONDecodeError

filesid = {
    200466 : "58405 - UNIV58405_VUMC59472-A7_FE_20210526",
    200538 : "58519 - UNIV58519_VUMC59344_FE_20210601",
    200687 : "59030 - UNIV59030_UTChattanooga_Amendment 9_Final Draft_20",
    200513 : "59359 - UNIV59359_VUMC61674-A6 VOID_20210527",
    200515 : "59359 - UNIV59359_VUMC 61674-New_FE_20210527",
    200425 : "59483 - 20160752 (0000000069) Vanderbilt University Mod 00",
    200776 : "59545 - EPRI 10008038 AMD 3 EXEC (FE)",
    200485 : "59643 - UNIV59643_VUMC62974_Am 5_FE_20210526",
    200208 : "59913 - UNIV59913_VUMC63572_Am 3_FE_20210519",
    200188 : "60060 - UNIV60060_UIC_A4_FE_20210519",
    200477 : "60062 - UNIV60062_URMC_FE_20210526",
    200445 : "60246 - Addendum (Amend 30) Adds Work - 2021-05-03_SusanPi",
    200446 : "60246 - Addendum (Amend 31) SELRA1b_VUSPA-FY2021-withMilne",
    200220 : "60405 - UNIV60405_VUMC66642-A3_FE_20210519",
    200256 : "60436 - UNIV60436_A3_FE_20210520",
    200794 : "60484 - UNIV60484_ASU 033519 Das MOD04_FE_20210604",
    200634 : "60485 - UNIV60485_OHSU_Am 3_FE_20210602",
    200255 : "60635 - UNIV60635_UnivSouthFlorida-A3_FE_20210520",
    200181 : "60752 - UNIV60752_University of Washington_Final Draft_202",
    200703 : "60759 - UNIV60759_NHDOE_A1_FE_20210603",
    200433 : "60907 - Massengill W52P1J-19-9-3008 P00003 Signed",
    200841 : "60924 - UNIV60924_UM_Am 2_FE_20210607",
    200609 : "61086 - UNIV61086_University of California-San Francisco_F",
    200237 : "61136 - UNIV61136_KPPT_Am 4_ FE_20210518",
    200194 : "61184 - UNIV61184_WNMU_Am 1_FE_20210519",
    200326 : "61337 - UNIV61337 Dougherty External Research Partner Agre",
    200774 : "61419 - UNIV61419 (Massengill) 20-C-0174-P00003_FE NCE 3Ju",
    200173 : "61480 - UNIV61480_VUMC80403_FE_20210519",
    200309 : "61525 - UNIV61525_Ohio_State_University-A1_FE_20210524",
    200234 : "61539 - UNIV61539_Kestrel Institute-A3_FE_20210520",
    200494 : "61555 - UNIV 61555_Loyola University Chicago_AM1 Final Dra",
    200685 : "61635 - UNIV61635_VUMC91588_FE_20210602",
    200784 : "61646 - UNIV61646_VUMC81912-A1_FE_20210604",
    200803 : "61772 - LO for Sandia TCAD and Sandia MRED Doug FE 4June21",
    200716 : "61793 - UNIV61793_UA_FE_20210603",
    200355 : "61798 - Sponsored Research Agreement_BasePair-Vandy_Signed",
    200542 : "61821 - UNIV61821_University of Alberta RES0048230-A1_FE_2",
    200337 : "61822 - UNIV61822_VUMC84206-A1_FE_20210524",
    200788 : "61834 - UNIV61834_Harris County Public Health NSF Converge",
    200564 : "61835 - UNIV61835_ClimaCell Inc_Tomorrow Companies_Am 1_FE",
    200811 : "61856 - UNIV61856_Tennessee Technological University A1_FE",
    200640 : "61857 - UNIV61857_University of Tennessee-Knoxville_AM 1_F",
    200419 : "61906 - UNIV61906_UC-D_FE_20210525",
    200807 : "61932 - UNIV61932_Austin Peay State University-A1_FE_20210",
    200637 : "61998 - UNIV61998_VUMC_Amendment 1_Final Draft_20210602",
    200222 : "62024 - FINAL_DocuSign_Vanderbilt_Infineon_VU_SPA_- FE 05.",
    200297 : "62090 - UNIV62090_Vanderbilt_(Zhou_Xingyu)_-w-_Carle_Found",
    200853 : "62099 - UNIV62099_VUMC_FE_20210607",
    200773 : "62100 - UNIV62100_VUMC_Final Draft_20210604",
    200286 : "62132 - UNIV62132_George Washington University_Final Draft",
    200305 : "62137 - UNIV62137_UWSA12674_FE_20210524",
    200779 : "62139 - StemSynergy. Orton 3.22.21 VU_SPA_Research_Core_Ag",
    200216 : "62140 - UNIV62140_The Leland Stanford Jr University A00-17",
    200709 : "62147 - UNIV62147_University of Tennessee_Final Draft_2021",
    200621 : "62149 - UNIV62149_VUMC92483_FE_20210601",
    200377 : "62158 - UNIV62158_VUMC88854_FE_20210524",
    200490 : "62164 - UNIV62164_Emory University_Final Draft_20210527",
    200258 : "62175 - UNIV62175_VUMC91425_FE_20210520",
    200724 : "62181 - Tokyo Tech Collaboration Agreement FE 3June21_KY21",
    200339 : "62185 - UNIV62185_University of Houston_Final Draft_202105",
    200274 : "62191 - UNIV62191_VUMC91489_Final Draft_20210520",
    200295 : "62194 - Vanderbilt Susan Gray HCB 69640 Final - 7.1.2021-6",
    200506 : "62198 - UNIV62198_Florida International University 000441_",
    200459 : "62200 - UNIV62200_Vanderbilt_(Dubey)_-w-_WeGo_MTA_FE_26May",
    200601 : "62204 - U Colorado VU MMPC (FE)",
    200211 : "62208 - UNIV62208_VUMC91760_FE_Gore SBA_20210519",
    200549 : "62212 - UNIV62212_Pennsylvania State University_Final Draf",
    200562 : "62221 - UNIV62221_VUMC88488_FE_20210601",
    200694 : "62223 - Vanderbilt Univeristy Fluidigm FE 05.27.2021",
    200857 : "62229 - UNIV62229_Brown University_Final Draft_20210607",
    200843 : "62230 - UNIV62230_UM_FE_20210607",
    200723 : "62247 - U Washington (McDonogh) VU Genome Editing Core (Ma",
    200768 : "62254 - Yale - VU TIssue Imaging Core (Reyzer) - UNIV62254",
    200132 : "62189 - UNIV62189 Vanderbilt -w- NAWI_Consortium_Agreement"
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

