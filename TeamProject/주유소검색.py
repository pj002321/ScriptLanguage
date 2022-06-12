from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import datetime
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

import mysmtplib
g_Tk = Tk()
g_Tk.geometry("800x1200") 
def event_for_listbox(event): 
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        print(data)

photo = ImageTk.PhotoImage(file="Mail.png")
mapphoto = ImageTk.PhotoImage(file="Map.png")
now = datetime.datetime.now()

def InitScreen(): 
    fontTitle = font.Font(g_Tk, size=20, weight='bold', family = '바탕체')
    fontNormal = font.Font(g_Tk, size=12, weight='bold')
    # 화면 전체 구도 잡기
    frameTitle = Frame(g_Tk, padx=10, pady=10, bg='#000000')
    frameTitle.pack(side="top", fill="x")
    frameCombo = Frame(g_Tk, pady=10, bg='#000000')
    frameCombo.pack(side="top", fill="x")
    frameEntry = Frame(g_Tk, pady=10, bg='#ffffff')
    frameEntry.pack(side="top", fill="x")
    frameList = Frame(g_Tk, padx=10, pady=10, bg='#ffffff')
    frameList.pack(side="bottom", fill="both", expand=True)
    # title 부분
    MainText = Label(frameTitle, font = fontTitle, text=" 주유소 검색 ")
    MainText.pack(anchor="center", fill="both")

    global SearchListBox 
    LBScrollbar = Scrollbar(frameCombo)
    SearchListBox = Listbox(frameCombo,font=fontNormal, activestyle='none', width=10, height=1, borderwidth=7, relief='solid', yscrollcommand=LBScrollbar.set) 
    slist = ["도로명","전화번호","사용가능 여부"]
    for i, s in enumerate(slist): 
        SearchListBox.insert(i, s)
    SearchListBox.pack(side='left', padx=10, expand=True, \
    fill="both")
    LBScrollbar.pack(side="left")
    LBScrollbar.config(command=SearchListBox.yview) 
        
    global InputEntry
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    InputEntry = Entry(g_Tk, font = TempFont, width = 15, borderwidth = 12, relief = 'solid')
    InputEntry.pack()
    InputEntry.place(x=13, y=535)

    
    GMailButton = Button(g_Tk, width='100', height='100', command=SendMail,image=photo)
    GMailButton.place(x=200,y=530)

    MapButton = Button(g_Tk, width='100', height='100',image=mapphoto)
    MapButton.place(x=500,y=530)


    global InputLabel
    InputLabel = Entry(frameEntry, font = fontNormal,width = 55, borderwidth = 5, relief = 'solid')
    InputLabel.pack(side="left", padx=10, expand=True)
    SearchButton = Button(frameEntry, font = fontNormal, \
    text="검색", command=onSearch)
    SearchButton.pack(side="right", padx=10, expand=True, fill='y')

    global listBox 
    LBScrollbar = Scrollbar(frameList)
    listBox = Listbox(frameList, selectmode='extended',\
    font=fontNormal, width=18, height=15,borderwidth=12, relief='groove', yscrollcommand=LBScrollbar.set)
    listBox.bind('<<ListboxSelect>>', event_for_listbox)
    listBox.pack(side='left', anchor='n', expand=True, fill="x")
    LBScrollbar.pack(side="right", fill='y')
    LBScrollbar.config(command=listBox.yview)


def onSearch(): 
    global SearchListBox
    sels = SearchListBox.curselection()
    iSearchIndex = 0 if len(sels) == 0 else SearchListBox.curselection()[0]
    if iSearchIndex == 0: 
        Searchgasstation() 
    elif iSearchIndex == 1: pass 
    elif iSearchIndex == 2: pass 
    elif iSearchIndex == 3: pass

def SendMail():
            #global value
    host = "smtp.gmail.com" # Gmail STMP 서버 주소.
    port = "587"
    htmlFileName = "logo.html"

    senderAddr = "tlsehddq98@gmail.com"     # 보내는 사람 email 주소.
    recipientAddr = str(InputEntry.get())  # 받는 사람 email 주소.

    DataInfo = now.strftime('%Y-%m-%d')

    text ="병신 허재성"
    msg = MIMEText(text)
    msg['Subject'] = DataInfo+" 오늘의 날씨 정보"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    s = mysmtplib.MySMTP(host,port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("kimwoochan1996@gmail.com","dkdldb127!!")
    s.sendmail(senderAddr , [recipientAddr], msg.as_string())
    s.close()


def Searchgasstation():
    pass


InitScreen() # 화면 전체 구성
g_Tk.mainloop()
