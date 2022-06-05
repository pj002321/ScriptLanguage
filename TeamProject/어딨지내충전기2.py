
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
import http.client
import json
from xml.etree import ElementTree 
import datatime

g_Tk = Tk()
g_Tk.title("어딨지 내 충전기")
g_Tk.geometry("400x600+450+100")
now = datetime.datetime.now()

class MainGUI:
    def InitSearch(self):
        global SearchListBox

        myFont2 = font.Font(g_Tk,size=20,weight='bold')
        MainName = Label(g_Tk,font= myFont2, text="어딨지 내 충전기")
        MainName.place(x=140,y=20)

        ListBoxScrollBar = Scrollbar(g_Tk)
        ListBoxScrollBar.pack()
        ListBoxScrollBar.place(x=130,y=70)

        myFont = font.Font(g_Tk,size=10,weight='bold')
        SearchListBox = ListBox(g_Tk,font=myFont,activestyle='none',
        width=10,height=1,borderwidth=12,relief='ridge',yscrollcommand=ListBoxScrollBar.set)
        SearchListBox.insert(1,"서울")
        SearchListBox.insert(2,"경기도")
        SearchListBox.pack()
        SearchListBox.place(x=30,y=70)

    def InitSearchButton(self):
        myFont = font.Font(g_Tk,size=10,weight='bold')
        SearchButton = Button(g_Tk,font=myFont,text='검색',
        command=self.SearchButtonAction)
        SearchButton.pack()
        SearchButton.place(x=170,y=80)

    def SearchButtonAction(self):
        myListBox = SearchListBox.curselection()[0]
        if myListBox == 0:
            self.SearchSeoul()
        elif myListBox == 1:
            a = 2
        elif myListBox == 2:
            a = 3

    def SearchSeoul():
        conn = http.client.HTTPConnection("apis.data.go.kr")
        nowData = now




InitScreen()
g_Tk.mainloop()