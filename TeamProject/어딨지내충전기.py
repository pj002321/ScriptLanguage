from glob import glob
from msilib.schema import ListBox
from textwrap import fill
from tkinter import*
from tkinter import font
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pprint
import folium
import webbrowser

BooksDoc=None
g_Tk = Tk()
g_Tk.geometry("400x600+450+100")

import requests

url = 'http://apis.data.go.kr/B552584/EvCharger/getChargerStatus'
params ={'serviceKey' : '2z8Dr3zPn9Tek3B9kij2pwdidbbelPfo219UZdsDuWPrnRFolaLWJ2ye1/j9EaAddINmI2ulPfdhz/iUg6teyw==', 'pageNo' : '1', 'numOfRows' : '10', 'period' : '5', 'zcode' : '11' }


response = requests.get(url, params=params)

pp = pprint.PrettyPrinter(indent=4)
print(pp.pprint(response.content))
senderAddr="tlsehdduq98@gmail.com"
recipientAddr="tlsehdduq98@gmail.com"
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
    s.login('tlsehdduq98@gmail.com','idmw bebw lzem kxot')
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

def SearchLibrary():
    from xml.etree import ElementTree 
    global listBox
    listBox.delete(0,listBox.size()) 

    with open('getChargerInfo.xml', 'rb') as f: 
        strXml = f.read().decode('utf-8')
    parseData = ElementTree.fromstring(strXml) 
    elements = parseData.iter('row')

    i = 1
    for item in elements:
        part_el = item.find('pageNo')

        if InputLabel.get() not in part_el.text:
            continue

        _text = '['+str(i)+']'+ \
            getStr(item.find('numOfRows').text)+ \
            ':' + getStr(item.find('period').text)+\
            ':' + getStr(item.find('zcode').text)+\
        listBox.insert(i-1,_text)
        i=i+1


def onSearch(): 
    global SearchListBox
    sels = SearchListBox.curselection()
    iSearchIndex = \
    0 if len(sels) == 0 else SearchListBox.curselection()[0]
    if iSearchIndex == 0:
         SearchLibrary() 
    elif iSearchIndex == 1: pass 
    elif iSearchIndex == 2: pass 
    elif iSearchIndex == 3: pass  

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

    Button(frameCombo,font=fontNormal,text='충전소명').pack(side='left',padx=10,fill='y')
    
    Button(frameCombo,font=fontNormal,text='충전기 타입').pack(side='right',padx=10,fill='y')

    Button(frameCombo,font=fontNormal,text='지도상 위치',command=Pressed).pack(side='right',padx=10,fill='y')

    Button(frameEntry,font=fontNormal,text="이메일",command=sendMail(senderAddr,recipientAddr,msg)).pack(side="bottom",padx=10,expand=True,fill='both')
    
    resetButton = Button(frameReset,font=fontNormal,text='초기화')
    resetButton.pack(side='bottom',padx=10,fill='y')
    global InputLabel
    InputLabel = Entry(frameEntry,font=fontNormal,width=35,borderwidth=12,relief='ridge')
    InputLabel.pack(side="left",padx=15,expand=True)

    SearchButton = Button(frameEntry,font=fontNormal,text="검색",command=SearchLibrary)
    SearchButton.pack(side="right",padx=10,expand=True,fill='y')

    global listBox
    LBScrollbar = Scrollbar(frameList)
    listBox = Listbox(frameList,selectmode='extended',font=fontNormal,width=10,height=15,borderwidth=5,relief='solid',yscrollcommand=LBScrollbar.set)
    listBox.bind('<<ListboxSelect>>',event_for_listbox)
    listBox.pack(side='left',anchor='n',expand=True,fill="x")

    LBScrollbar.pack(side="right",fill='y')
    LBScrollbar.config(command=listBox.yview)

    global Maplabel
    Maplabel = Listbox(frameList,selectmode='extended',font=fontNormal,width=10,height=15,borderwidth=5,relief='solid',background='red')
    Maplabel.pack(side='right',anchor='n',expand=True,fill="x")


InitScreen()
g_Tk.mainloop()