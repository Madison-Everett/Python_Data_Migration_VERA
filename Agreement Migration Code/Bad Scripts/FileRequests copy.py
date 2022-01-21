import requests


filesid =[]

counter=0

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

for ids in filesid:
    #response = requests.get("peer.app.vanderbilt.edu?controller=api&action=getContract&id=["+ filesid[i]+ "]",
                            #auth=OAuth2AuthorizationCode(authorization_url = 'https://www.authorization.url', token_url = 'https://www.token.url',
                                                        # header_name, header_value = Bearer{}))
    response = requests.get("peer.app.vanderbilt.edu?controller=api&action=getContract&id=["+ filesid[i]+ "]",
                            auth=BearerAuth(''))
    open("/Users/everetmm/Desktop/Contracts/Contract"+ filesid[i]+".pdf", 'wb').write(response.content)
    counter++
   
