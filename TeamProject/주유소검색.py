from ast import Index
from http.client import HTTPSConnection
from tkinter import *
from tkinter import font
from unicodedata import name
from PIL import Image, ImageTk
import datetime
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from urllib.request import urlopen
from xml.etree import ElementTree
from xml.dom.minidom import parse, parseString
import folium
import webbrowser
import mysmtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkintermapview
import parsing
import gmail_send

list=[]
g_Tk = Tk()
g_Tk.geometry("800x600") 
res_list = []
# photo = ImageTk.PhotoImage(file="Mail.png")
# mapphoto = ImageTk.PhotoImage(file="Map.png")
now = datetime.datetime.now()
key = 'lG82c%2B9oYvMU4QwfaSNiAMTU%2BacChjPPigBb6e%2FmvQXhkxwAcoxyi4BPi1SvjmmWQSUz41ofz%2Bhm6ei5vwvjYg%3D%3D'
baseurl = 'http://apis.data.go.kr/3510500/gas_station/getList?type=xml&pageNo=1&numOfRows=10&serviceKey='+key
DOC = []
data2=[]
mylist=[]
str = ""
def event_for_listbox(event): 
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        print(data)

def clicked_listbox(event):  # 리스트 선택 시 내용 출력
    global data2
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data2 = event.widget.get(index)
        print(data2)
    print('클릭')


popup = inputEmail = btnEmail = None 
addrEmail = None

class MainGUI():
    def __init__(self):
        self.frameList = Frame(g_Tk, padx=10, pady=10, bg='#ffffff')
        self.LBScrollbar = Scrollbar(self.frameList)
        self.frameCombo = Frame(g_Tk, pady=10, bg='#000000')
        self.frameCombo.pack(side="top", fill="x")
        self.fontNormal = font.Font(g_Tk, size=12, weight='bold')
        self.listbox=Listbox(self.frameCombo,font=self.fontNormal, activestyle='none', width=10, height=1, borderwidth=7, relief='solid', yscrollcommand=self.LBScrollbar.set)
        self.InitScreen()

    def onEmailInput(self): 
        global addrEmail 
        global resultEmail
        global str
        global popup, data2
        resultEmail = "tlsehdduq98@gmail.com"
        addrEmail = inputEmail.get()
        str = MIMEText("2018180024신동엽")
        
        gmail_send.sendMail(addrEmail,resultEmail,str)

        popup.destroy() # popup 내리기
    
    def onEmailPopup(self): 
        global g_Tk, addrEmail, popup
        addrEmail = None 
        
        popup = Toplevel(g_Tk)
        popup.geometry("300x150")
        popup.title("받을 이메일 주소 입력")
        
        global inputEmail, btnEmail
        inputEmail = Entry(popup, width = 200,)
        inputEmail.pack(fill='x', padx=10, expand=True)
        btnEmail = Button(popup, text="확인", command=self.onEmailInput)
        btnEmail.pack(anchor="s", padx=10, pady=10)

    def onMapPopup(self):
        global g_Tk, data2
        
        for s in parsing.mylist:
            if s['TMP01'] == data2:
                popup = Toplevel(g_Tk)  # popup 띄우기
                popup.geometry(f"{800}x{600}")
                popup.title("map.py")
                map_widget = tkintermapview.TkinterMapView(popup, width=800, height=500, corner_radius=0)
                map_widget.pack()

                print(s['REFINE_WGS84_LOGT'], s['REFINE_WGS84_LAT'])
                marker_1 = map_widget.set_address(s['REFINE_ROADNM_ADDR'], marker=True)

                print(marker_1.position, marker_1.text)
                marker_1.set_text(s['TMP01'])
                map_widget.set_zoom(15)
   

    def Pressed(self):
        # # Create a Map with Folium and Leaflet.js (위도 경도 지정) 
        # map_osm = folium.Map(location=[37.3402849,126.7313189], zoom_start=13)
        # # 마커 지정
        # folium.Marker([37.3402849,126.7313189],popup='한국공학대학교').add_to(map_osm)
        # # html 파일로 저장
        # map_osm.save('osm.html')
        # webbrowser.open_new('osm.html')
        pass

    def InitScreen(self): 
        self.fontTitle = font.Font(g_Tk, size=20, weight='bold', family = '바탕체')
        self.fontNormal = font.Font(g_Tk, size=12, weight='bold')
        # 화면 전체 구도 잡기
        self.frameTitle = Frame(g_Tk, padx=10, pady=10, bg='#ffffff')
        self.frameTitle.pack(side="top", fill="x")
        self.frameCombo = Frame(g_Tk, pady=10, bg='#ffffff')
        self.frameCombo.pack(side="top", fill="x")
        self.frameEntry = Frame(g_Tk, pady=10, bg='#ffffff')
        self.frameEntry.pack(side="top", fill="x")
        self.frameList = Frame(g_Tk, padx=10, pady=10, bg='#ffffff')
        self.frameList.pack(side="bottom", fill="both", expand=True)
        # title 부분
        self.MainText = Label(self.frameTitle, font = self.fontTitle, text=" 주유소 검색 ")
        self.MainText.pack(anchor="center", fill="both")

        self.LBScrollbar2 = Scrollbar(self.frameList)
        self.SearchListBox = Listbox(self.frameList,font=self.fontNormal, width=10, height=1, borderwidth=7, relief='solid',yscrollcommand=self.LBScrollbar2.set) 
        slist = ['경인오일티엠(주)', '동원주유소', '인하주유소', '명보주유소', 'KH에너지(주)직영 청도1주유소', '제물포하이웨이주유소', '황금주유소', '다솜주유소', '통일주유소', '큰나무주유소']
        for i, s in enumerate(slist): 
            self.SearchListBox.insert(i, s)
        self.SearchListBox.pack(side='left', padx=10, expand=True,fill="both")
        self.LBScrollbar.pack(side="left")
        self.LBScrollbar.config(command=self.SearchListBox.yview) 
          
        self.GMailButton = Button(self.frameCombo,command=self.onEmailPopup,bg='#ffff00')
        self.GMailButton.pack(side='left',padx=10,expand=True)
        
        self.MapButton = Button(self.frameCombo ,command=self.onMapPopup,bg='#ffffff')
        self.MapButton.pack(side='left',padx=10,expand=True)


        global InputLabel
        InputLabel = Entry(self.frameEntry, font = self.fontNormal,width = 75, borderwidth = 5, relief = 'solid')
        InputLabel.pack(side="left", padx=10, expand=True)
        SearchButton = Button(self.frameEntry, font = self.fontNormal,text="검색", command=self.getData)           #############
        SearchButton.pack(side="right", padx=10, expand=True, fill='y')

        global listBox 
        global res_list
        global mylist
        LBScrollbar = Scrollbar(self.frameList)
        listBox = Listbox(self.frameList, selectmode='extended',font=self.fontNormal,height=15,borderwidth=12, relief='groove', yscrollcommand=LBScrollbar.set)
        for t in mylist:
            listBox.insert(END,t)
        listBox.insert(END,' ================================================================================')
        #listBox.insert(END,' 주유소이름 : ' + res_list['bsn_nm'])

        #listBox.bind('<<ListboxSelect>>', clicked_listbox)
        listBox.pack(side='left', anchor='n', expand=True, fill="x")
        LBScrollbar.pack(side="right",fill='y')
        LBScrollbar.config(command=listBox.yview)

    def getData(self): 
        global res_list
        global listBox
        global mylist 
        url = baseurl
        res_body = urlopen(url).read() 
        strXml = res_body.decode('utf-8')
        tree = ElementTree.fromstring(strXml)
        items = tree.iter("item") # return list type

        for item in items: 
            Index = item.find("no").text.strip()
            name = item.find("bsn_nm").text
            addr = item.find("road_nm_addr").text
            global str
            str = addr
            location = item.find("lat").text 
            brand = item.find("cat").text 
            tel = item.find("tel_no").text
            yesorno = item.find("self_yn").text
            mylist.append(item.find("bsn_nm").text)
            row = Index + '/' + '주유소이름 : ' +name + '/' +'도로명 : '+ addr + ', ' \
                + '위도 : '+ location + ' ' + '주유소 브랜드 : '+brand + ' [' + '번호 : '+ tel+' ] ,' +'사용가능 : '+ yesorno
            listBox.insert(END,row)  
            res_list.append(row)
        
           
    
        #print(res_list)
        print(mylist)
        return mylist



MainGUI()
g_Tk.mainloop()
