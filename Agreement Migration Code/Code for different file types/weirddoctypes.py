import requests
import os
import base64
import time

troublesome = {
    158828 : '59891 - Owens Addendum 12MAR18 Signed', 
    159296 : '59891 - Owens UNIV59891 VU Core (Transgenic Mouse) Addendu',
    186958 : '61084 - UNIV61084_Am 1_Placeholder for FE_20200521', 
    184436 : '61270 - Creare Budget', 
    192730 : '61021 - Amendment 1 - Kennedy', 
    180507 : '60145 - NCE approval email',
    166920 : '60145 - NCE' 
}

for x in troublesome:
    response = requests.get("https://peer.app.vanderbilt.edu/index.php?controller=Api&call=getContractFile&fileId="+str(x)+"&token=dac9630aec642a428cd73f4be0a03569")

    time.sleep(1.1)
    message = response.json()["content"]
    message_bytes = message.encode('ascii')
    file = base64.b64decode(message_bytes)
    

    if x == 158828 or x==159296 or x== 186958: 
        try:
          os.mkdir("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5])
          print("Directory " , troublesome[x][0:5] ," Created ")
          open("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5]+"/Contract "+ troublesome[x]+".docx", 'wb').write(file)
        except FileExistsError:
          print("Directory " , troublesome[x][0:5],  " already exists")
          open("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5]+"/Contract "+ troublesome[x]+".docx", 'wb').write(file)
    elif x == 184436:
        try:
          os.mkdir("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5])
          print("Directory " , troublesome[x][0:5] ," Created ")
          open("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5]+"/Contract "+ troublesome[x]+".xlsx", 'wb').write(file)
        except FileExistsError:
          print("Directory " , troublesome[x][0:5],  " already exists")
          open("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5]+"/Contract "+ troublesome[x]+".xlsx", 'wb').write(file)         
    elif x == 192730:
        try:
          os.mkdir("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5])
          print("Directory " , troublesome[x][0:5] ," Created ")
          open("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5]+"/Contract "+ troublesome[x]+".jpg", 'wb').write(file)
        except FileExistsError:
          print("Directory " , troublesome[x][0:5],  " already exists")
          open("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5]+"/Contract "+ troublesome[x]+".jpg", 'wb').write(file)
    elif x == 180507 or x== 166920:
        try:
          os.mkdir("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5])
          print("Directory " , troublesome[x][0:5] ," Created ")
          open("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5]+"/Contract "+ troublesome[x]+".txt", 'wb').write(file)
        except FileExistsError:
          print("Directory " , troublesome[x][0:5],  " already exists")
          open("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5]+"/Contract "+ troublesome[x]+".txt", 'wb').write(file)

    




        




