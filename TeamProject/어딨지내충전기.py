from msilib.schema import ListBox
from tkinter import*
from tkinter import font
import tkinter.font as tkFont

from pygame import GL_BLUE_SIZE

g_Tk = Tk()
g_Tk.geometry("400x600+450+100")

def event_for_list(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]    
        data = event.widget.get(index)
        print(data)

def SearchLibrary():
    from xml.etree import ElementTree 
    global listBox
    listBox.delete(0,listBox.size()) 

    with open('서울도서관.xml', 'rb') as f: 
        strXml = f.read().decode('utf-8')
    parseData = ElementTree.fromstring(strXml) 
    elements = parseData.iter('row')

    i = 1
    for item in elements:
        part_el = item.find('CODE_VALUE')

        if InputLabel.get() not in part_el.text:
            continue

        _text = '['+str(i)+']'+ \
            getStr(item.find('LBRRY_NAME').text)+ \
            ':' + getStr(item.find('ADRES').text)+ \
            ':' + getStr(item.find('TEL_NO').text)
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
    
    MainText = Label(frameTitle, font = fontTitle, text="[어딨지? 내 충전기]")
    MainText.pack(anchor="center", fill="both")

    roadaddressButton = Button(frameCombo,font=fontNormal,text='도로명')
    roadaddressButton.pack(side='left',padx=10,fil='y')

    addressButton = Button(frameCombo,font=fontNormal,text='충전소명')
    addressButton.pack(side='left',padx=10,fil='y')
    
    typeButton = Button(frameCombo,font=fontNormal,text='충전기 타입')
    typeButton.pack(side='right',padx=10,fil='y')

    mapButton = Button(frameCombo,font=fontNormal,text='지도상 위치')
    mapButton.pack(side='right',padx=10,fil='y')

    
    resetButton = Button(frameReset,font=fontNormal,text='초기화')
    resetButton.pack(side='bottom',padx=10,fil='y')
    global InputLabel
    InputLabel = Entry(frameEntry,font=fontNormal,width=35,borderwidth=12,relief='ridge')
    InputLabel.pack(side="left",padx=15,expand=True)

    SearchButton = Button(frameEntry,font=fontNormal,text="검색",command=onSearch)
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
