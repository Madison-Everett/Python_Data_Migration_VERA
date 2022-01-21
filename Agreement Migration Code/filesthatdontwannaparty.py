import requests
import os
import base64
import time
#500 Internal Server Error
#filesid=[183981,183983,169211,157178,157179,191506,191504,144781,191666
#191667,176064,145868,144727,

145887, 176065, 177069, 177071,169212]

#filesid=[195902, 189958, 189957] 189958

#Python Errors
#195902, 195904, 189958, 189957
#"Missing or empty value: file->id"
#195904 189958

filesid={
    #195902 : '58727 - UNIV58727_VUMCxxxxx_FE_20210112', 
    195904 : '58727 - UNIV58727_VUMCxxxxx_FE_20210112',
    #189957 : '60631 - UNIV60631_Technische_Am 2 - FE_20200810', 
    189958 : '60631 - UNIV60631_Technische_Am 2 - FE_20200810'
}

for x in filesid:
    response = requests.get("https://peer.app.vanderbilt.edu/index.php?controller=Api&call=getContractFile&fileId="+str(x)+"&token=dac9630aec642a428cd73f4be0a03569")

    time.sleep(60)
    
    message = response.json()["content"]
    print(message)
    message_bytes = message.encode('ascii')
    file = base64.b64decode(message_bytes)

    try:
          os.mkdir("/Users/everetmm/Desktop/Contracts/Contract_"+filesid[x][0:5])
          print("Directory " , filesid[x][0:5] ," Created ")
          open("/Users/everetmm/Desktop/Contracts/Contract_"+filesid[x][0:5]+"/Contract "+ filesid[x]+".pdf", 'wb').write(file)
    except FileExistsError:
          print("Directory " , filesid[x][0:5],  " already exists")
          open("/Users/everetmm/Desktop/Contracts/Contract_"+filesid[x][0:5]+"/Contract "+ filesid[x]+".pdf", 'wb').write(file)


  


