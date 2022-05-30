from codecs import utf_16_be_encode
from encodings import utf_8
from http.client import HTTPSConnection

import json
import urllib
import requests
import pprint

competitionApiAddress = 'https://infuser.odcloud.kr/oas/docs?namespace=15039765/v1'
competitionConnect = None
sellAptInfoApiAddress = 'https://api.odcloud.kr/api'
sellAptInfoConnect = None
priceAptApiAddress = 'https://infuser.odcloud.kr/oas/docs?namespace=15039765/v1'
priceAptConnect = None


def connectOpenAPIServer(server):   
    conn = HTTPSConnection(server) 
    conn.set_debuglevel(1)
    return conn


def userURIBuilder(uri, **user): 
    str = uri + "?"
    for key in user.keys(): 
        str += key + "=" + user[key] + "&"
    return str

def getsellAptInfo():
    serviceKey = "4VBaoIq8KK+Mqmg6ZUG7o6d7+qZGDB0EvZ388JGf1Bn4wGfLlorNjtzMOz+ILz5pPBnLGrh9JPAU8/6tSljfsw=="

    Autho = "4VBaoIq8KK%2BMqmg6ZUG7o6d7%2BqZGDB0EvZ388JGf1Bn4wGfLlorNjtzMOz%2BILz5pPBnLGrh9JPAU8%2F6tSljfsw%3D%3D" 
    
    uri = userURIBuilder('/15039765/v1/uddi:d32d99be-db1b-438f-ad2b-cb182cf81d76', serviceKey=Autho, page= '1', perPage= '10')    
    
    req =  requests.get(sellAptInfoApiAddress+uri)
    print(req)
    print(req.status_code)
    if req.status_code == 200:
        print("response complete!")
        jsonData = json.loads(req.text)
        print(jsonData)
    else:
        print("error - response!")
        return None

getsellAptInfo()