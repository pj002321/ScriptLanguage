from ast import Index
from http.client import HTTPSConnection
from tkinter import *
from tkinter import font
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
import parsing

list=[]
g_Tk = Tk()
g_Tk.geometry("800x600") 
res_list = []
photo = ImageTk.PhotoImage(file="Mail.png")
mapphoto = ImageTk.PhotoImage(file="Map.png")
now = datetime.datetime.now()
key = 'lG82c%2B9oYvMU4QwfaSNiAMTU%2BacChjPPigBb6e%2FmvQXhkxwAcoxyi4BPi1SvjmmWQSUz41ofz%2Bhm6ei5vwvjYg%3D%3D'
baseurl = 'http://apis.data.go.kr/3510500/gas_station/getList?type=xml&pageNo=1&numOfRows=10&serviceKey='+key
DOC = []
data2=[]

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

class MainGUI():
    def __init__(self):
        self.frameList = Frame(g_Tk, padx=10, pady=10, bg='#ffffff')
        self.LBScrollbar = Scrollbar(self.frameList)
        self.frameCombo = Frame(g_Tk, pady=10, bg='#000000')
        self.frameCombo.pack(side="top", fill="x")
        self.fontNormal = font.Font(g_Tk, size=12, weight='bold')
        self.listbox=Listbox(self.frameCombo,font=self.fontNormal, activestyle='none', width=10, height=1, borderwidth=7, relief='solid', yscrollcommand=self.LBScrollbar.set)
        self.InitScreen()

    def SendMail(fromAddr,toAddr,msg):
        # s.starttls()

        # #앱 패스워드 이용
        # s.login('tlsehdduq98@gmail.com','idmw bebw lzem kxot')
        # s.login('t55300354@gmail.com','kqvn jvje wfsk saau')
        # s.sendmail(fromAddr,[toAddr],msg.as_string())
        # s.close()
        pass

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
        self.res_list=[]

        # global SearchListBox 
        # self.LBScrollbar = Scrollbar(self.frameCombo)
        # SearchListBox = Listbox(self.frameCombo,font=self.fontNormal, width=10, height=1, borderwidth=7, relief='solid', yscrollcommand=LBScrollbar.set) 
        # slist = ["도로명","전화번호","사용가능 여부"]
        # for i, s in enumerate(slist): 
        #     SearchListBox.insert(i, s)
        # SearchListBox.pack(side='left', padx=10, expand=True,fill="both")
        # self.LBScrollbar.pack(side="left")
        # self.LBScrollbar.config(command=SearchListBox.yview) 
       
        
        # global InputEntry
        # TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
        # InputEntry = Entry(g_Tk, font = TempFont, width = 15, borderwidth = 12, relief = 'solid')
        # InputEntry.pack()
        # InputEntry.place(x=13, y=450)

        
        self.GMailButton = Button(self.frameCombo,command=self.SendMail,image=photo,bg='#ffffff')
        self.GMailButton.pack(side='left',padx=10,expand=True)
        self.MapButton = Button(self.frameCombo ,command=self.Pressed,image=mapphoto,bg='#ffffff')
        self.MapButton.pack(side='left',padx=10,expand=True)


        global InputLabel
        InputLabel = Entry(self.frameEntry, font = self.fontNormal,width = 55, borderwidth = 5, relief = 'solid')
        InputLabel.pack(side="left", padx=10, expand=True)
        SearchButton = Button(self.frameEntry, font = self.fontNormal,text="검색", command=self.getData)           #############
        SearchButton.pack(side="right", padx=10, expand=True, fill='y')

        global listBox 
        global res_list
        LBScrollbar = Scrollbar(self.frameList)
        listBox = Listbox(self.frameList, selectmode='extended',font=self.fontNormal,height=15,borderwidth=12, relief='groove', yscrollcommand=LBScrollbar.set)
        for t in self.res_list:
            listBox.insert(END,'주유소이름 : ' +t['bsn_nm'] , '도로명 : '+ t['road_nm_addr'] , \
            '위도 : '+ t['lat'] , '주유소 브랜드 : ' +t['cat'] , '번호 : '+t['tel_no'], '사용가능 : '+ t['self_yn'])
        listBox.insert(END,' ================================================================================')
        listBox.insert(END,' 주유소이름 : ' + self.res_list['bsn_nm'])

        #listBox.bind('<<ListboxSelect>>', clicked_listbox)
        listBox.pack(side='left', anchor='s', expand=True, fill="x")
        LBScrollbar.pack(side="right",fill='y')
        LBScrollbar.config(command=listBox.yview)

    def getData(self): 
        self.res_list=[]
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
                + '위도 : '+ location + ' ' + '주유소 브랜드 : '+brand + ' [' \
                + '번호 : '+ tel+' ] ,' +'사용가능 : '+ yesorno
            self.res_list.append(row)
    
        print(self.res_list)
        return self.res_list


                

    # def onSearch():
    #     global res_list
    #     frameList = Frame(g_Tk, padx=10, pady=10, bg='#ffffff')
    #     LBScrollbar = Scrollbar(frameList)
    #     frameCombo = Frame(g_Tk, pady=10, bg='#000000')
    #     frameCombo.pack(side="top", fill="x")
    #     fontNormal = font.Font(g_Tk, size=12, weight='bold')
    #     Listbox(frameCombo,font=fontNormal, activestyle='none', width=10, height=1, borderwidth=7, relief='solid', yscrollcommand=LBScrollbar.set) 
    #     for s in parseString.res_list:
    #         Listbox.insert('이름' + s['bsn_nm'])



MainGUI()
g_Tk.mainloop()
