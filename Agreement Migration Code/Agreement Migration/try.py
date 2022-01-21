import requests
import os


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
    response = requests.get("http://peer.app.vanderbilt.edu?controller=api&action=getContract&id=["+str(x)+"]",
                            headers={"Authorization": 'Bearer 6c74a2b815ef5735a9db1e4c7ba536c9'})

    if x == 158828 or x==159296 or x== 186958: 
        try:
          os.mkdir("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5])
          print("Directory " , troublesome[x][0:5] ," Created ")
          open("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5]+"/Contract "+ troublesome[x]+".docx", 'wb').write(response.content)
        except FileExistsError:
          print("Directory " , troublesome[x][0:5],  " already exists")
          open("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5]+"/Contract "+ troublesome[x]+".docx", 'wb').write(response.content)
    elif x == 184436:
        try:
          os.mkdir("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5])
          print("Directory " , troublesome[x][0:5] ," Created ")
          open("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5]+"/Contract "+ troublesome[x]+".xlsx", 'wb').write(response.content)
        except FileExistsError:
          print("Directory " , troublesome[x][0:5],  " already exists")
          open("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5]+"/Contract "+ troublesome[x]+".xlsx", 'wb').write(response.content)         
    elif x == 192730:
        try:
          os.mkdir("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5])
          print("Directory " , troublesome[x][0:5] ," Created ")
          open("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5]+"/Contract "+ troublesome[x]+".jpg", 'wb').write(response.content)
        except FileExistsError:
          print("Directory " , troublesome[x][0:5],  " already exists")
          open("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5]+"/Contract "+ troublesome[x]+".jpg", 'wb').write(response.content)
    elif x == 180507 or x== 166920:
        try:
          os.mkdir("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5])
          print("Directory " , troublesome[x][0:5] ," Created ")
          open("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5]+"/Contract "+ troublesome[x]+".txt", 'wb').write(response.content)
        except FileExistsError:
          print("Directory " , troublesome[x][0:5],  " already exists")
          open("/Users/everetmm/Desktop/Contracts/Contract_"+troublesome[x][0:5]+"/Contract "+ troublesome[x]+".txt", 'wb').write(response.content)

    




        




