import requests
import os
import base64
import time
from json.decoder import JSONDecodeError

filesid = {
    199011 : '62041 - UNIV62041_University of Pennsylvania 581066 fx_515',
    199012 : '62041 - UNIV62041_University of Pennsylvania 581066 fx_515',
    199018 : '60675 - UNIV60675_VUMC66757-A2_FE_20210417',
    199020 : '60675 - UNIV60675_VUMC66757-A2_FE_20210417',
    198738 : '61078 - UNIV61078_AE_A4_FE_20210408',
    198742 : '61815 - UNIV61815_VUMC85793_Am1_Final Draft_20210409',
    198746 : '61579 - UNIV61579 Sandia PO_TERMS_102_2170670_1_US  FE 8Ap',
    198755 : '60396 - UNIV60396_Penner.Vanderbilt.2018-3599.amend.3_FE_2',
    198756 : '60396 - UNIV60396_Penner.Vanderbilt.2018-3599.amend.3_FE_2',
    198808 : '60040 - UNIV60040_DOLL_A5_FE_20210412',
    198819 : '61530 - UNIV61530_VUMC82727-A1_FE_20210412',
    198823 : '61613 - UNIV61613_VUMC_ SBA-Miller_FE_20210412',
    198825 : '61613 - UNIV61613_VUMC_ SBA-Miller_FE_20210412',
    198826 : '61772 - Amending the LO for PO 2185860 Sandia TCAD $95K',
    198839 : '60481 - UNIV60481_UM_FE_20210412',
    198841 : '60481 - UNIV60481_UM_FE_20210412',
    198895 : '62146 - UNIV62146 Vanderbilt (McGuinness Owen) -w- Western',
    198912 : '61645 - UNIV61645_UA_FE_20210414',
    198913 : '61645 - UNIV61645_UA_FE_20210414',
    198939 : '62138 - 62138',
    198977 : '59366 - UNIV59366_OSU_Am 40_FE_20210416',
    198983 : '60188 - UTSI (Liu) - VINSE - Attach A (Proj) and B (Waiver',
    199028 : '61872 - Merck - Vanderbilt (Young) - SRA - Final (03.10.21',
    199047 : '62134 - UNIV62134_VUMC89757_FE_20210419',
    199048 : '62134 - UNIV62134_VUMC89757_FE_20210419',
    199050 : '62145 - UNIV62145 Vanderbilt -w- Harvard - CORES - FE 13Ap',
    199091 : '59396 - UNIV59396_VUMC_A5_FE_20210420',
    199092 : '61203 - DOC041921-04192021163732',
    199120 : '61157 - Geo.Mason.U (GMU) - VU (Wikswo) Core Addendum $356',
    198625 : '62069 - Meharry - VU Mass Spec (Hayes) Core Agreement (FE)',
    198644 : '60061 - UNIV60061_VUMC65127-A3_FE_20210406',
    198660 : '61112 - UNIV61112_VUMC79115-FE-initialled',
    198662 : '61112 - UNIV61112_VUMC79115-FE-initialled',
    198663 : '61112 - UNIV61112_VUMC79115-A1-Initialled',
    198669 : '61479 - UNIV61479_VUMC(HHMI)_Am 2 FE_202010406',
    198670 : '61479 - UNIV61479_VUMC(HHMI)_Am 2 FE_202010406',
    198705 : '62071 - UNIV62071_Ohio State University_Final Draft_202104',
    198627 : '62069 - Meharry - VU Mass Spec (Hayes) Core Agreement (FE)',
    198628 : '62069 - Meharry (Alcendor)($1309)  - VU Mass.Spec (Hayes) ',
    198661 : '61112 - UNIV61112_VUMC79115-A1-Initialled',
    198684 : '62036 - UNIV62036_Massachusetts Institute of Technology_FE',
    198850 : '61331 - UNIV61331_UAH_A2_FE_20210413',
    198870 : '58822 - UNIV58822_VUMC59469_Am 3_FE_20210413',
    198874 : '62077 - UNIV62077_Agreement DFCIReinherz_1P01AI143565-01A1',
    198875 : '62080 - UNIV62080_Agreement DFCIReinherz_1P01AI143565-01A1',
    198881 : '61437 - 80NSSC20K0424-AWARD DOCS 3-22-21',
    198647 : '62021 - UNIV62021_VUMC89696_FE__20210406',
    198650 : '59156 - UNIV59156_VUMC90549_FE_20210406',
    198651 : '61788 - UNIV61788_VUMC85822-A1_FE_20210406',
    198652 : '61788 - UNIV61788_VUMC85822-A1_FE_20210406',
    198671 : '61448 - UNIV61448_VUMC81311_Am 1_ Manning SBA_FE_20210406',
    198672 : '61448 - UNIV61448_VUMC81311_Am 1_ Manning SBA_FE_20210406',
    198682 : '62036 - UNIV62036_Massachusetts Institute of Technology_FE',
    198691 : '62012 - JumpCrew CDA FE 7April21',
    198695 : '62130 - UNIV62130 Vanderbilt (Olatunji) -w- Rutgers Univer',
    198931 : '62126 - UNIV62126_ST_FE_20210414',
    198968 : '62079 - UNIV62079_Dana-Farber Cancer Institute_Final Draft',
    199094 : '61824 - UNIV61824 Vanderbilt (Mohyuddin Hasina) -w- Nashvi',
    199107 : '61929 - UNIV61929_Colorado Boulder_AM1_Final Draft_2021042',
    198849 : '60071 - UNIV60071_PSU_A3_FE_20210412',
    198869 : '58822 - UNIV58822_VUMC59469_Am 3_FE_20210413',
    198904 : '62078 - UNIV62078_UP_FE_20210413',
    198905 : '62078 - UNIV62078_UP_FE_20210413',
    198907 : '60169 - UNIV60169_Stan_A3_FE_20210414',
    198916 : '61748 - UNIV61748_VUMC85210_Am 1_FE_20210414',
    198917 : '61748 - UNIV61748_VUMC85210_Am 1_FE_20210414',
    198918 : '59766 - UNIV59766_CW_NCE_FE_20210414',
    198919 : '59766 - UNIV59766_CW_NCE_FE_20210414',
    198921 : '60428 - UNIV60428_TSU_Am 4_FE_20210414',
    198922 : '60428 - UNIV60428_TSU_Am 4_FE_20210414',
    198971 : '62136 - UNIV62136_NE FE_20210416',
    198979 : '59366 - UNIV59366_OSU_Am 40_FE_20210416',
    199017 : '60675 - UNIV60675_VUMC66757-A2_FE_20210417',
    199024 : '60673 - UNIV60673_VUMC70887_Trice SBA_FE_20210419',
    199025 : '60673 - UNIV60673_VUMC70887_Trice SBA_FE_20210419',
    199029 : '61872 - Merck - Vanderbilt (Young) - SRA - Final (03.10.21',
    198906 : '61992 - UNIV61992_INCH_FE_20210414'

}


for x in filesid:
    response = requests.get("https://peer.app.vanderbilt.edu/index.php?controller=Api&call=getContractFile&fileId="+str(x)+"&token=dac9630aec642a428cd73f4be0a03569")

    try:
        time.sleep(1)
        message = response.json()["content"]
        message_bytes = message.encode('ascii')
        file = base64.b64decode(message_bytes)
        try:
              os.mkdir("/Users/everetmm/Desktop/uhoh/Contract_"+filesid[x][0:5])
              print("Directory " , filesid[x][0:5] ," Created ")
              open("/Users/everetmm/Desktop/uhoh/Contract_"+filesid[x][0:5]+"/Contract "+ filesid[x]+".pdf", 'wb').write(file)
        except FileExistsError:
              print("Directory " , filesid[x][0:5],  " already exists")
              open("/Users/everetmm/Desktop/uhoh/Contract_"+filesid[x][0:5]+"/Contract "+ filesid[x]+".pdf", 'wb').write(file)
        
    except JSONDecodeError:
        print("    ")
        print(str(x))
        print("    ")






