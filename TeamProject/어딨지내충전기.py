
from msilib.schema import ListBox
from textwrap import fill
from tkinter import*
from tkinter import font
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pprint
import folium
import webbrowser
from codecs import utf_16_be_encode
from encodings import utf_8
from http.client import HTTPSConnection
import json
from xml.etree import ElementTree 



BooksDoc=None
g_Tk = Tk()
g_Tk.geometry("400x600+450+100")

import requests




competitionApiAddress = 'https://infuser.odcloud.kr/oas/docs?namespace=15039765/v1'
competitionConnect = None
sellAptInfoApiAddress = 'http://apis.data.go.kr/B552584/EvCharger/getChargerStatus'
sellAptInfoConnect = None
priceAptApiAddress = 'https://infuser.odcloud.kr/oas/docs?namespace=15039765/v1'
priceAptConnect = None



pp = pprint.PrettyPrinter(indent=4)
#print(pp.pprint(response.content))
senderAddr="t55300354@gmail.com"
recipientAddr="t55300354@gmail.com"
msg=MIMEMultipart('alternative')

def event_for_list(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]    
        data = event.widget.get(index)
        print(data)

    
def sendMail(fromAddr,toAddr,msg):
    global senderAddr,recipientAddr
    import smtplib # 실제 보내는 녀석
    s=smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()

    #앱 패스워드 이용
    s.login('t55300354@gmail.com','kqvn jvje wfsk saau')
    s.sendmail(fromAddr,[toAddr],msg.as_string())
    s.close()
    
    msg['Subject'] = '제목 : 파이썬으로 gmail 보내기'
    msg['From'] = senderAddr
    msg['To']=recipientAddr

    htmlFD=open("logo.html",'rb')
    HtmlPart=MIMEText(htmlFD.read(),'html',_charset='UTF-8')
    htmlFD.close()
    msg.attach(HtmlPart)

def Pressed():
    # Create a Map with Folium and Leaflet.js (위도 경도 지정) 
    map_osm = folium.Map(location=[37.3402849,126.7313189], zoom_start=13)
    # 마커 지정
    folium.Marker([37.3402849,126.7313189],
        popup='한국공학대학교').add_to(map_osm)
    # html 파일로 저장
    map_osm.save('osm.html')
    webbrowser.open_new('osm.html')

<<<<<<< HEAD
def SearchLibrary():
    pass
=======
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
    url = 'http://apis.data.go.kr/B552584/EvCharger?serviceKey=lG82c%2B9oYvMU4QwfaSNiAMTU%2BacChjPPigBb6e%2FmvQXhkxwAcoxyi4BPi1SvjmmWQSUz41ofz%2Bhm6ei5vwvjYg%3D%3D&'
    params ={'pageNo' : '1', 'numOfRows' : '10', 'period' : '5', 'zcode' : '11' }

    response = requests.get(url, params=params)
    #print(response.content)

    global listBox
    listBox.delete(0,listBox.size()) 

    parseData = ElementTree.fromstring(response.content) 

    i = 1
    for item in parseData.findall('item'):
        #part_el = item.find('items')
        
        _text = '['+str(i)+']'+ \
            getStr(item.find('statNm').text)+ \
            ':' + getStr(item.find('addr').text)+ \
            ':' + getStr(item.find('useTime').text)
        listBox.insert(i-1,_text)
        print(_text)
        i=i+1
>>>>>>> b77169e7db604df67f03c977e4807f3cf2e4b588



def getStr(s):
    return ''if not s else s     

def event_for_listbox(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        print(index)

def InitScreen():
    global senderAddr,recipientAddr,msg
    fontTitle = font.Font(g_Tk,size=18,weight='bold',family="Bahnschrift",slant="italic")
    fontNormal = font.Font(g_Tk,size=11,weight='bold')

    frameTitle = Frame(g_Tk,padx=10,pady=10,bg='#000000')
    frameTitle.pack(side="top",fill="x")
    frameCombo = Frame(g_Tk,pady=10,bg='#ffffff')
    frameCombo.pack(side="top",fill="x")
    frameReset = Frame(g_Tk,pady=15,bg='#ffffff')
    frameReset.pack(side="bottom",fill="x")
    frameEntry = Frame(g_Tk,pady=10,bg='#ffffff')
    frameEntry.pack(side="top",fill="x")
    frameList = Frame(g_Tk,padx=10,pady=10,bg='#ffffff')
    frameList.pack(side="bottom",fill="both",expand=True)
    
    Label(frameTitle, font = fontTitle, text="[어딨지? 내 충전기]").pack(anchor="center", fill="both")

    Button(frameCombo,font=fontNormal,text='도로명').pack(side='left',padx=10,fill='y')

    Button(frameCombo,font=fontNormal,text='충전소 수',command=getsellAptInfo).pack(side='left',padx=10,fill='y')
    
    Button(frameCombo,font=fontNormal,text='충전기 타입').pack(side='right',padx=10,fill='y')

    Button(frameCombo,font=fontNormal,text='지도상 위치',command=Pressed).pack(side='right',padx=12,fill='y')

    Button(frameEntry,font=fontNormal,text="이메일",command=sendMail(senderAddr,recipientAddr,msg)).pack(side="bottom",padx=10,expand=True,fill='both')
    
    Button(frameReset,font=fontNormal,text='초기화').pack(side='bottom',padx=10,fill='y')

    global InputLabel
    InputLabel = Entry(frameEntry,font=fontNormal,width=35,borderwidth=12,relief='ridge')
    InputLabel.pack(side="left",padx=15,expand=True)

    SearchButton = Button(frameEntry,font=fontNormal,text="검색",command=getsellAptInfo)
    SearchButton.pack(side="right",padx=10,expand=True,fill='y')

    global listBox
    LBScrollbar = Scrollbar(frameList)
    listBox = Listbox(frameList,selectmode='extended',font=fontNormal,width=10,height=15,borderwidth=5,relief='solid',yscrollcommand=LBScrollbar.set)
    listBox.bind('<<ListboxSelect>>',event_for_listbox)
    listBox.pack(side='left',anchor='n',expand=True,fill="x")

    slist = ['강원','경기','서울','']
    for i,s in enumerate(slist):
        listBox.insert(i,s)

    LBScrollbar.pack(side="right",fill='y')
    LBScrollbar.config(command=listBox.yview)

    global Maplabel
    Maplabel = Listbox(frameList,selectmode='extended',font=fontNormal,width=10,height=15,borderwidth=5,relief='solid',background='red')
    Maplabel.pack(side='right',anchor='n',expand=True,fill="x")


InitScreen()
g_Tk.mainloop()