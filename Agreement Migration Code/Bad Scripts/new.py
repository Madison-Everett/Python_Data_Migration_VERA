import requests
import os
# Making a get request 


response = requests.get('https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf') 

print(response.content)

# printing request content 
#open("/Users/everetmm/Desktop/Contracts/Contract.pdf", 'wb').write(response.content) 

dirName = 'tempDir'
try:
    # Create target Directory
    os.mkdir("/Users/everetmm/Desktop/Contracts/"+dirName)
    print("Directory " , dirName ,  " Created ")
    open("/Users/everetmm/Desktop/Contracts/"+dirName+"/Contract168957.pdf", 'wb').write(response.content)
except FileExistsError:
    print("Directory " , dirName ,  " already exists")
    open("/Users/everetmm/Desktop/Contracts/"+dirName+"/Contract1689572.pdf", 'wb').write(response.content)
