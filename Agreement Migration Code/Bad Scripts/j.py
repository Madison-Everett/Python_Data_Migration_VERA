import os

filesid= {

    "20170313144120_harrisdj_mjwt8.pdf": 'Contract 59322 - Document-Vanderbilt MSA_fully executedID/144727.pdf',
    "20170314_UNIV59322_t1dq4.pdf": 'Contract 59322 - Document-Vanderbilt MSA_fully executedID/144781.pdf',
    "20170330_UNIV59308_vwn40.pdf": 'Contract 59308 - UNIV59308_PellissippiTSGC_FE_20170330ID/145868.pdf',
    "20170330_UNIV59308_kv2tj.pdf": 'Contract 59308 - UNIV59308_PellissippiTSGC_FE_20170330ID/145887.pdf',
    
    "20180119_UNIV59845_j9gy1.pdf": 'Contract 59845 - UNIV59845_The Aerospace Corporation FE 01192018ID/157178.pdf',
    
    "20180119_UNIV59845_hvqmc.pdf": 'Contract 59845 - UNIV59845_The Aerospace Corporation FE 01192018ID/157179.pdf',
    
    "20190204_UNIV60494_k4hj3.pdf": 'Contract 60494 - UNIV60494_UGARF_FE_20190204ID/169211.pdf',
    "20190204_UNIV60494_4swc0.pdf": 'Contract 60494 - UNIV60494_UGARF_FE_20190204ID/169212.pdf',
    "20190801_UNIV61012_q7v0j.pdf": 'Contract 61012 - UNIV61012_Uof Florida_FE_073119ID/176064.pdf',
    "20190801_UNIV61012_1mb8d.pdf": 'Contract 61012 - UNIV61012_Uof Florida_FE_073119ID/176065.pdf',
    "20190821_UNIV59583_m61hs.pdf": 'Contract 59583 - UNIV59583-(formerly 3799-019687)-UTC-A6-Strauss-SuID/177069.pdf',
    "20190821_UNIV59583_jbz8v.pdf": 'Contract 59583 - UNIV59583-(formerly 3799-019687)-UTC-A6-Strauss-SuID/177071.pdf',
    "20200226_UNIV61232_wnm09.pdf": 'Contract 61232 - UNIV61232_Augusta University 32307-56_DiaComp_FE_2ID/183981.pdf',
    
    "20200226_UNIV61232_4zyc6.pdf": 'Contract 61232 - UNIV61232_Augusta University 32307-56_DiaComp_FE_2ID/183983.pdf',
    "20200909_UNIV61614_rpkvb.pdf": 'Contract 61614 - UNIV61614_DATA Opinion Publica y Mercados_FE_20200ID/191504.pdf',
    "20200909_UNIV61614_byzh2.pdf": 'Contract 61614 - UNIV61614_DATA Opinion Publica y Mercados_FE_20200ID/191506.pdf',
    "20200914_UNIV61758_hr41j.pdf": 'Contract 61758 - UNIV61758_VUMC82169_FE_20200914ID/191666.pdf',
    "20200914_UNIV61758_m8jps.pdf": 'Contract 61758 - UNIV61758_VUMC82169_FE_20200914ID/191667.pdf'

}


root_dir = "/Users/everetmm/Desktop/manually_extracted_files"

for dir_, _,files in os.walk(root_dir):
    for file_name in files:
        rel_dir = os.path.relpath(dir_,root_dir)
        rel_file = os.path.join(rel_dir, os.rename(file_name,filesid[file_name]))
     



    
