import sys
import telepot
from pprint import pprint # 데이터를 읽기 쉽게 출력
from urllib.request import urlopen
import traceback
from xml.etree import ElementTree
from xml.dom.minidom import parseString
key = 'lG82c%2B9oYvMU4QwfaSNiAMTU%2BacChjPPigBb6e%2FmvQXhkxwAcoxyi4BPi1SvjmmWQSUz41ofz%2Bhm6ei5vwvjYg%3D%3D'
TOKEN = '5583123871:AAETLHE2voiBMydob3opuTzGUYCi93cAbDc'
MAX_MSG_LENGTH = 300
baseurl = 'http://apis.data.go.kr/3510500/gas_station/getList?type=xml&pageNo=1&numOfRows=10&serviceKey='+key
bot = telepot.Bot(TOKEN)


def getData(): 
    res_list = [] 
    url = baseurl
    res_body = urlopen(url).read() 
    strXml = res_body.decode('utf-8')
    tree = ElementTree.fromstring(strXml)
    items = tree.iter("item") # return list type
    for item in items: 
            Index = item.find("no").text.strip()
            name = item.find("bsn_nm").text
            addr = item.find("road_nm_addr").text
            location = item.find("lat").text 
            brand = item.find("cat").text 
            tel = item.find("tel_no").text
            yesorno = item.find("self_yn").text
           
            row = Index + '/' + '주유소이름 : ' +name + '/' +'도로명 : '+ addr + ', ' \
                + '위도 : '+ location + ' ' + '주유소 브랜드 : '+brand + ' [' + '번호 : '+ tel+' ] ,' +'사용가능 : '+ yesorno
            res_list.append(row)
            sendMessage('5572194409',row)

    print(res_list)
        
    
    

def sendMessage(user, msg): 
    try:
        bot.sendMessage(user, msg) 
    except:
        traceback.print_exception(*sys.exc_info(), file=sys.stdout)


getData()