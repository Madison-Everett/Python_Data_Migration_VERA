import requests
import os
import base64

import time
from json.decoder import JSONDecodeError

filesid = {
    201479 : "40151 - MIHOW UNIV40151_ABLE_FE_20210623",
    202689 : "40153 - UNIV40153_MIHOW_FE_20210726",
    202110 : "40154 - UNIV40154_MIHOW_FE_20210709",
    202536 : "40155 - UNIV40155_NRHA_MIHOW_FE_20210720",
    201644 : "43183 - FW_ Impedimed (Ridner)",
    202819 : "58602 - UNIV58602_VUMC59770-A8_FE_20210727",
    202620 : "58653 - UNIV58653_UoI_FE_20210722",
    201954 : "58720 - UNIV58720_AT_A3_FE_20210707",
    202616 : "58742 - UNIV58742_VUMC59374_FE_20210722",
    201927 : "58865 - UNIV58865_VUMC59466_FE_A10_20210706",
    201689 : "58933 - UNIV58933_VUMC_AM6_Final Draft_20210628.fe",
    201822 : "59425 - Thomas Jefferson U (Eischen) -  Vanderbilt cryo Am",
    201708 : "59437 - Vanderbilt_SAPT_Workgroup_Services_Contract_FY_22 ",
    202108 : "59443 - UNIV59443_VUMC62040_A6_FE_20210709",
    202605 : "59452 - UNIV59452_Rutgers_Am 46_FE_20210721",
    202763 : "59478 - Skelton CORE FE 27July21",
    201503 : "59533 - UNIV59533_MITs4377_AM 5_Final Draft_20210623",
    202648 : "59730 - UNIV59730_vumc 63594_A4_FE_20210722",
    202686 : "59749 - UNIV59749_VUMC63268-A4_FE_20210726",
    202275 : "59754 - UNIV59754_VUMC63295_Am 6_FE_20210713",
    202288 : "59768 - UNIV59768_VUMC63765-A4_FE_20210713",
    202120 : "59808 - UNIV59808_SMU-A4_FE_20210709",
    202092 : "59839 - UNIV59839_NYU_AM 2_Final Draft_20210709",
    201758 : "59931 - 18-D-0010 0007 fully executed (002)",
    202693 : "59946 - UNIV59946_MMC_FE_20210726",
    201607 : "59969 - UNIV59969_GIT_A3_FE_20210625",
    201815 : "60040 - UNIV60040_DOLL_A6_FE_20210630",
    201901 : "60055 - UNIV6055  - FA875018C0089 P00006 FE 6July21",
    201398 : "60124 - Vanderbilt University 46100-324-0000112273 FY 22",
    202348 : "60161 - UNIV60161 VU (Weiss Sharon) -w- Nanosys - First Am",
    202576 : "60193 - Tenn Tech_Vanderbilt Research Core amendment FE 21",
    201799 : "60217 - UNIV60217_VUMC65981-A3_FE_20210630",
    201429 : "60280 - UNIV60280_OSU_Final Draft_20210622",
    202461 : "60322 - UNIV60322_SUNY_Am 3_FE_20210719",
    202412 : "60380 - UNIV60380_TXAM_FE_20210716",
    202493 : "60381 - UNIV60381_DFCI_FE_20210720",
    202264 : "60382 - NCE FullyX_VANDERBILT_F0253-03_A03_NYU July 12 202",
    202194 : "60421 - UNIV60421_MP_A2_FE_20210712",
    202525 : "60533 - 2021-06-22-WCNDD-BI-Second Amendment draft-BI 4309",
    201795 : "60539 - UNIV60539_VUMC73328-A2_FE_20210630",
    202834 : "60573 - Vanderbilt Amendment  3 to Sponsored Research Agre",
    201399 : "60592 - UNIV60592 (Valentine) SRI PO30123 Vanderbilt Mod 5",
    202350 : "60597 - UNIV60597_U Mass-S51110000040449-A3_FE_20210714",
    201924 : "60617 - UNIV60617_Idaho_FE_20210701",
    202201 : "60623 - Ancora-AmendmentNo.4toM4WorkPlanv1 FE 12July21",
    202535 : "60663 - UNIV60663_CW_A4_20210720",
    202464 : "60674 - Re_ ZTRAX program ending -- Important Request for ",
    201643 : "60688 - Change Order 3 To PO 7600030900 Fully Signed",
    201956 : "60689 - UNIV60689_AMA_A1_FE_20210707",
    202362 : "60696 - UNIV60696_VUMC70520_FE_20210715",
    201820 : "60716 - RE_ dua #2014103 Health Impacts of Environmental T",
    201845 : "60800 - UNIV60800_VUMC71719_Am 2_FE_20210701",
    201592 : "60842 - UNIV60842_Pajarito Powder LLC-A2_FE_20210624",
    201555 : "60862 - UNIV60862_Drexel_FE_20210624",
    201831 : "60868 - COLUMBIA U - VANDERBILT-S01A05(PG009358)(16-0029)_",
    202437 : "60873 - UNIV60873_VUMC74435_AM 2_Final Draft_20210716",
    202449 : "61012 - UNIV61012_UF_FE_20210719",
    202032 : "61014 - UNIV61014_MMC_FE_20210708",
    201651 : "61053 - PO (2)",
    202755 : "61066 - UNIV61066_University of Cape Town_AM 2_Final Draft",
    202197 : "61123 - UNIV61123_Rectors and Visitors of University 02-GB",
    202823 : "61144 - UNIV61144_VUMC76468-A2_FE_20210727",
    201525 : "61182 - UNIV61182_UC-Berkeley 00010220-03_FE_20210623",
    202424 : "61230 - UNIV61230_National Opinion Research Center_Final D",
    201754 : "61254 - 16X117 Modification 4Q FE",
    201604 : "61270 - PO_104352_CO 1",
    202272 : "61317 - LO Increase_Mahadevan Sandia",
    201520 : "61350 - UNIV61350_Univ of Maryland 85338-Z0264207 Mod B_FE",
    201576 : "61365 - UNIV61365_UNTHSC_Am 1_FE_20210607",
    202077 : "61406 - Penn State Subaward 6126-VU-NSF-9916 Amend 1 PSU L",
    202006 : "61410 - UNIV61410_UTSA_FE_20210708",
    202107 : "61413 - ARA 1375 Toyota (TEMA) - Vanderbilt (Hatzell-Caldw",
    202451 : "61435 - UNIV61435_UNM_Am 3_NCE_FE_20210719",
    201473 : "61471 - UNIV61471_VUMC81396_Am 2_FE_20210623",
    202188 : "61501 - UNIV61501 (Kosson) PO_TERMS_102_2282688_0_US FE 12",
    201439 : "61505 - UNIV61505_VUMC81692-A3_FE_20210622",
    201437 : "61519 - UNIV61519_University of California-A1_FE_20210622",
    202482 : "61528 - UNIV61528_VUMC81252_Am 1_FE_20210720",
    202018 : "61543 - UNIV61543_VUMC81541_FE_20210708",
    201664 : "61552 - 01_CPO_APPROVED_VU_PathfinderEval_Amendment1 (002)",
    201646 : "61559 - UNIV61559_VRH_FE_20200903_20210625 _NR Copy",
    201667 : "61559 - UNIV61559_VRH-A1_FE_20210628",
    202299 : "61568 - UNIV61568_VUMC82376_Am 1_FE_20210713",
    202073 : "61570 - BMS  PO#0082096597 OT125-295_VU (Cherrington) Amen",
    201788 : "61582 - UNIV61582_VUMC84234_Am 1_FE_20210630",
    201378 : "61588 - UNIV61588_VUMC82492_FE_20210621",
    202762 : "61594 - Vanderbilt (Schafer Jenny) -w- PureTech Health FE ",
    202457 : "61611 - UNIV61611_VUMC83006-A1_FE_20210719",
    202851 : "61637 - UNIV61637_VUMC84776_Zhang_SBA_Am 1_FE_20210728",
    201871 : "61671 - UNIV61671_MTSU C21-0233A-A1_FE_20210704",
    202550 : "61681 - UNIV61681_VUMC84580_Am 1_FE_20210721",
    201534 : "61701 - Vanderbilt funding 2021",
    202266 : "61714 - MOU - OKCo - USD - Vanderbilt 06.24.2021",
    202487 : "61753 - UNIV61753_SIIM_FE_20210720",
    202664 : "61762 - UNIV61762-VUMC_Am 1_FE_20210723",
    202573 : "61766 - Addendum_for_Research_Core_Agreement_UTSI_Liu",
    201456 : "61809 - UNIV61809_VUMC86804_Am 1_Final Draft_20210622.fe",
    201446 : "61820 - UNIV61820_University of Szeged-A2_FE_20210622",
    202372 : "61824 - UNIV61824 NPEF NCE - FE 15July21",
    201686 : "61826 - UNIV61826_VUMC86293_AM 1_Final Draft_20210628",
    201357 : "61830 - EPA - Jacobs - VU (Kosson) Mod1-VanderbiltSubcontr",
    202434 : "61840 - UNIV61840_Emory University_AM 1_Final Draft_202107",
    202622 : "61846 - UNIV61846_MTSU_Am 1_FE_20210722",
    201546 : "61848 - UNIV61848_UTC_Am 1_FE_20210624",
    202518 : "61852 - Vanderbilt University_FEX AMD1 Subaward 62441926-1",
    202260 : "61855 - UNIV61855_UTSI-A1_FE_20210713",
    202293 : "61856 - UNIV61856_TTU-A2_FE_20210713",
    202473 : "61857 - UNIV61857_University of Tennessee-Knoxville_AM 2_F",
    202489 : "61858 - UNIV61858_CBU_Am 1_FE_20210720",
    202276 : "61873 - 10012907 CHNG 1",
    202526 : "61882 - EPA-NSWCCD-20-0956 FINAL",
    202477 : "61883 - UNIV61883 VU (Milne Ginger) -w- University of Nort",
    202684 : "61904 - UNIV61904_UTK_Amend 1_Deob_FE_20210721",
    202428 : "61909 - UNIV61909_Soleno_A1_FE_20210716",
    201587 : "61924 - UNIV61924_CIRD-A1_FE_20210624",
    202297 : "61932 - UNIV61932_APSU_A2_FE_20210713",
    202660 : "61946 - UNIV61946_NU_FE_20210723",
    201750 : "61954 - FE__Vanderbilt__Mod 1_Exercise Option 1 FE",
    202179 : "61975 - Stony Brook - VU BRET (Gilbert and Jallinoja) - FE",
    201649 : "61976 - National Center for Health Statistics_signed-2 (3)",
    202821 : "61979 - UNIV61979_VUMC85879-A1_FE_20210727",
    201835 : "62020 - DTHF (Desmond Tutu Health Foundation) NIH FDP Cost",
    202058 : "62032 - UNIV62032_VUMC90083_Am 1_FE_20210709",
    202554 : "62033 - UNIV62033_University of Utah_Am 1_Final Draft_2021",
    202559 : "62035 - HUP DUA - Bethany Young - FE 21July21",
    201707 : "62049 - UNIV62049 VU (Sheldon) -w- FermiLab DE-AC02-07CH11",
    201598 : "62051 - UNIV62051_UStutt_FE_20210625",
    201637 : "62059 - UNIV62059_CB_A1_FE_20210628",
    201663 : "62073 - Vanderbilt Univ_JHUAPL NDA 2-17-2021 (15711) FE",
    202747 : "62079 - UNIV62079_Dana-Farber Cancer Institute_Am 1_Final ",
    202038 : "62082 - UNIV62082_University of Kentucky 3200003835-21-261",
    202199 : "62090 - UNIV62090_Amendment 2 FE 12July21",
    201324 : "62106 - BRW9C305BC2AA59_0000003095",
    201752 : "62114 - 67050_signed",
    201560 : "62116 - UNIV62116_NYU_FE_20210624",
    201631 : "62135 - UNIV62135 Signed CDAs combined",
    201740 : "62138 - 1504_001",
    202528 : "62161 - Attachments AB Dana Dement (1)",
    202618 : "62162 - UNIV62162_Upenn_DUA_FE_20210722",
    202527 : "62163 - Wawrzynski_Vanderbilt University",
    202476 : "62166 - UNIV62166 VU (Wadzinski) -w- University of Arizona",
    202311 : "62174 - UNIV62174_Univ of Texas at Austin 202100034-001_FE",
    201778 : "62183 - UNIV62183_UM_FE_20210630",
    202688 : "62184 - UNIV62184_VUMC89680-A1_FE_20210726",
    201721 : "62186 - UNIV62186_BEC_FE_20210629",
    201782 : "62187 - UNIV62187_VUMCxxxxx_FE_20210629",
    201458 : "62188 - UNIV62188_Pennsylvania State University 244757_FE_",
    201452 : "62199 - UNIV62199_VUMC90311_FE_20210622",
    202269 : "62211 - UNIV 62211",
    201574 : "62215 - Senda - Vanderbilt University (Cherrington) - MSA_",
    201380 : "62217 - Koutalos_VU_SPA_Research_Core_Agreement -w- MUSC F",
    201617 : "62220 - UNIV62220_University of Louisville_FE_20210625",
    202757 : "62222 - UNIV62222_VUMC93134_FE_20210727",
    201767 : "62224 - PRAMS-Data-Sharing-Agreement_(VU.edited.Final)(06.",
    202098 : "62227 - CSI academic data use agreement (OP Orig)(VU.Updat",
    201389 : "62228 - UNIV62228_Temple University_Final Draft_20210618",
    202448 : "62231 - UNIV62231 (Gonzales) DUA FE 19July21",
    202223 : "62232 - UNIV62232 Vanderbilt (Bornhop) -w- Meru Biotechnol",
    201859 : "62240 - Final 7-1",
    201747 : "62244 - UNIV62244_Clemson University_Final Draft_20210630",
    201776 : "62245 - UNIV62245_VUMCxxxxx_Farrow SBA_FE_20210630",
    202580 : "62246 - UNIV62246_Utah_FE_20210721",
    201833 : "62248 - THEC Grant Contract (3) - (FE)",
    202544 : "62250 - V2 UO(Leve)-Vanderbilt(Bordenstein) DUA PE 19July2",
    201983 : "62251 - UNIV62251_VUMC93088_FE_20210707",
    202769 : "62252 - UNIV62252_VUMC87508_FE__20210726",
    201506 : "62255 - UNIV62255_Oregon State University_Final Draft_2021",
    201401 : "62257 - UNIV62257_UD_FE_20210622",
    201975 : "62259 - UNIV62259 Vanderbilt -w- University of Waterloo_FE",
    202375 : "62260 - UNIV62260_Experian_FE_20210715",
    201934 : "62261 - UNIV62261_Georgia State University Research_Final ",
    202186 : "62263 - UNIV62263_VUMC90498_FE_20210711",
    201497 : "62264 - VU SPA - ISDE Core Agreement_CFDRC-consolidated-fi",
    201424 : "62269 - Soliz External Researcher Agreement -w- P20 Connec",
    201533 : "62271 - UNIV62271_NIH_DUA_FE_20210623",
    201636 : "62273 - Ittner_Macquarie University 5.13.21 VU_Core Agrmt ",
    202583 : "62274 - UNIV62274_VUMC93380_Final Draft_20210721.vuao",
    202589 : "62275 - UNIV62275_VUMC93465_Vazquez SBA_FE_20210721",
    202029 : "62277 - UNIV62277_VUMC91493_FE_20210708",
    202087 : "62279 - AvalancheTech-VandyAgreement (2)(Core Agrmt)(FE)",
    202387 : "62280 - UNIV62280_University of Dayton_Final Draft_2021071",
    202624 : "62281 - UNIV62281_VUMCxxxxx_Saif SBA_FE_20210722",
    201926 : "62284 - UNIV62284_FSU_FE_20210706",
    201710 : "62286 - Infineon - VU ISDE (Kauppila) - SRA  (UNIV62286)(F",
    202397 : "62287 - UNIV62287_BT_FE_20210716",
    202445 : "62288 - UNIV62288_Vanderbilt_University_(Gualda)_-w-_Dia_C",
    202751 : "62289 - Vanderbilt_University -w- St. Marys College of Cal",
    201614 : "62290 - Fully executed - Vanderbilt Keystone - HR001121200",
    201817 : "62291 - UNIV62291 (Adams) -w- Sandia PO_TERMS_102_2275697_",
    202400 : "62291 - Amendment 1 - UNIV62291 Adams Douglas - Sandia Nat",
    202789 : "62292 - UNIV62292_MCA_revFE_20210727",
    201654 : "62294 - UNIV62294_Core_FE_20210628",
    202187 : "62298 - UNIV62298 VU (Milne) -w- HHMC FE 12July21",
    202429 : "62299 - UNIV62299_DARPA_FE_20210716",
    201756 : "62300 - MNDA Vanderbilt University Signed",
    202761 : "62301 - Cigna_Foundation_Grant_Agreement FE 27July21",
    201957 : "62309 - UNIV62309_PHC_SRA_20210707",
    202089 : "62311 - ICD1602105_Janssen_VU MMPC_v1_06042021 FINAL.FINAL",
    202192 : "62312 - UNIV62312_EL_SRA_FE_20210712",
    202249 : "62313 - UNIV62313_DPR_NDA_FE_20210713",
    202467 : "62324 - TN_Arts_Contract_12153_to_Sign (1)",
    202697 : "62325 - EC Visiting Student Agreement FN 1.23.19-v2_FM Sig",
    202374 : "62328 - UNIV62328_GSK_FE_20210715",
    202515 : "62338 - 27976 Stassun Acceptance of Conditions- Need Signa",
    202494 : "62339 - Agreement(externalpartysigned)",
    202760 : "62344 - VU_CDAK 2way CDA final",
    202537 : "62345 - NondisclosureAgreement_Vanderbiltjb",
    202521 : "62346 - 20210719_Agreement_draft_NEQ_signed"
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

