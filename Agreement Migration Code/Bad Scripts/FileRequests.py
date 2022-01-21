import requests
import urllib.request
import mimetypes
import base64

url = "https://peer.app.vanderbilt.edu/index.php?controller=Api&call=getContractFile&fileId=156001&token=dac9630aec642a428cd73f4be0a03569"

response = requests.get("https://peer.app.vanderbilt.edu/index.php?controller=Api&call=getContractFile&fileId=156001&token=dac9630aec642a428cd73f4be0a03569")
#open("/Users/everetmm/Desktop/Contracts/183586.pdf", 'wb').write(response.content)

#open("/Users/everetmm/Desktop/Contracts/183586.pdf", 'wb').write("b'"+response.json()["content"])

message = response.json()["content"]
message_bytes = message.encode('ascii')
file = base64.b64decode(message_bytes)

open("/Users/everetmm/Desktop/Contracts/183586.pdf", 'wb').write(file)

#with open('/Users/everetmm/Desktop/Contracts/183586.json', 'wb') as f:
 #   f.write(response.content)


#mime = magic.Magic(mime=True)
#mime.from_file("/Users/everetmm/Desktop/Contracts/183586.txt")
#print(response.content)

#pdfkit.from_url(url,'/Users/everetmm/Desktop/Contracts/183586.pdf')



#expdf=response.content
#egpdf=open('ex.pdf','wb')
#egpdf.write(expdf)
#egpdf.close()





#with open("/Users/everetmm/Desktop/Contracts/183586", 'wb') as fd:
 #   for chunk in response.iter_content(chunk_size=100):
  #     fd.write(chunk)
