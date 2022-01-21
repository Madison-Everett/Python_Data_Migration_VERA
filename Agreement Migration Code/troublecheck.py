import requests
import os
import base64
import time

filesid=[169211]


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


  


