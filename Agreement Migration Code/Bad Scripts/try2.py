import requests 


#print(requests.post("http://peer.app.vanderbilt.edu?controller=api&action=getContract&id=[156001]",, headers={"Authorization": "Bearer dac9630aec642a428cd73f4be0a03569"}))


response = requests.get("https://peer.app.vanderbilt.edu/controller=api&action=getContract&id=[156001]",headers={'Authorization': "Bearer dac9630aec642a428cd73f4be0a03569"})

print(response.content)
print(response.status_code)

open("/Users/everetmm/Desktop/Contracts/156001.pdf", 'wb').write(response.content)
