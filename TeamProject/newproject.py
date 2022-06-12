# 주유소 찾기 프로젝트로 새로 시작  --
# 
from tkinter import *
from tkinter import font
from tkinter import messagebox
import tkinter
import urllib
import http.client
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
import datetime
#import folium
# pip install cefpython3==66.0
import sys
#from cefpython3 import cefpython as cef
import threading
#import gmail
#import internetbook
import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText 



g_TK = Tk()
g_TK.title("주유소 찾기")
g_TK.geometry("550x600")
DataList = []
DustState = []
Dust10 = []
Dust25 = []
DustInfo = []
myimagelabel = []
now = datetime.datetime.now()

def event_for_listbox(self,event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        print(data)


class MainGUI:

    def InitSearch(self):
        global SearchListBox

        myFont2 = font.Font(g_TK, size=20, weight='bold')
        MainName = Label(g_TK, font = myFont2, text="주유소 찾기")
        MainName.place(x=140,y=20)
        
        ListBoxScrollBar = Scrollbar(g_TK)
        ListBoxScrollBar.pack()
        ListBoxScrollBar.place(x=130,y=70)

        myFont =font.Font(g_TK, size=10, weight='bold')
        SearchListBox = Listbox(g_TK, font=myFont, activestyle='none',
                                width=10, height=1, borderwidth=12, relief='ridge',
                                yscrollcommand=ListBoxScrollBar.set)
        SearchListBox.insert(1, "이름")

        SearchListBox.pack()
        SearchListBox.place(x=30, y=70)
        

    def InitSearcButton(self):
        myFont = font.Font(g_TK,size=10,weight='bold')
        SearchButton = Button(g_TK,font=myFont,text="Search",
        command=self.SearchButtonAction)
        SearchButton.pack()
        SearchButton.place(x=170, y=80)

    def SearchButtonAction(self):
        myListBox = SearchListBox.curselection()[0]
        if myListBox == 0 :
            self.searchMichuhole()

    def searchMichuhole(self):
        pass


    def __init__(self):
        self.canvas = Canvas(g_TK, bg='azure', width='550', height='600')
        self.canvas.pack()
        self.canvas.place(x=0,y=0)
        self.InitSearch()
        self.InitSearcButton()
        
        g_TK.mainloop()

MainGUI()