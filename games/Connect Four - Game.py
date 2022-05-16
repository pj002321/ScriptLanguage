from logging import root
from tkinter import *
from tkinter import messagebox

ROW = 6 
COL = 7 
class Cell(Canvas):
    def __init__(self, frame, row, col, width = 20, height = 20):
        Canvas.__init__(self, frame, width = width, height = height, \
            bg = "blue", borderwidth = 2)
        self.color = "white"
        self.row = row 
        self.col = col 
        self.token = ''
        self.state = NORMAL 
        self.create_oval(5, 5, 20, 20, fill = "white") 
        self.bind("<Button-1>", self.Click_Token) 

    def Update_Token(self): 
        global CT 
        if CT == 'R':
            self.Setcolor("red") 
        elif CT =='Y':
            self.Setcolor("yellow")  
        elif CT=='W':
            self.Setcolor("white") 
 
    def Click_Token(self, event): # red 또는 yellow 돌 놓기.  
        if self.token == '':
            self.token = CT 
            self.state = DISABLED   
            self.Update_Token()   
            Check()  
            Change()
        
    def Setcolor(self, color):         
        self.color = color  
        self.create_oval(5, 5, 20, 20, fill = self.color)  


def Change():
    global CT
    for i in ['R','Y']:   
        if i!=CT:
            CT=i
            break

def Reset():   
    global CT 
    CT = 'W' 
    for i in range(ROW):
        for j in range(COL): 
            y[i][j].token='' 
            y[i][j].state = NORMAL 
            y[i][j].Update_Token()  
   

def Check():
    # 가로                 
    for i in range(6):
            for j in range(4):
                if y[i][j].token!=' ' and\
                    y[i][j].token==y[i][j+1].token==CT and \
                    y[i][j].token==y[i][j+2].token==CT and\
                    y[i][j].token==y[i][j+3].token==CT:
                    messagebox.showinfo("GameOver",CT+"->WIn!!") 
                    Reset()
                   
    # 세로
    for i in range(3):
        for j in range(7):
            if  y[i][j].token!=' ' and\
                    y[i][j].token==y[i+1][j].token==CT and \
                    y[i][j].token==y[i+2][j].token==CT and\
                    y[i][j].token==y[i+3][j].token==CT:
                    messagebox.showinfo("GameOver",CT+"->Win!!") 
                    Reset()

    # 대각 : 우 하단, 좌 상단 
    for i in range(3):
        for j in range(4):
            if  y[i][j].token!=' ' and\
                    y[i][j].token==y[i+1][j+1].token==CT and \
                    y[i][j].token==y[i+2][j+2].token==CT and\
                    y[i][j].token==y[i+3][j+3].token==CT:
                    messagebox.showinfo("GameOver",CT+"->Win!!") 
                    Reset()

    # 대각 : 좌 하단, 우 상단                
    for i in range(3):
        for j in range(3,7):
            if  y[i][j].token!=' ' and\
                    y[i][j].token==y[i+1][j-1].token==CT and \
                    y[i][j].token==y[i+2][j-2].token==CT and\
                    y[i][j].token==y[i+3][j-3].token==CT:
                    messagebox.showinfo("GameOver",CT+"->Win!!") 
                    Reset() 


              

root = Tk()
root.title("Connect Four - Game")
CT = 'Y'  

frame = Frame(root) 
frame.pack() 

frameButton = Frame(root)
frameButton.pack() 

y=([],[],[],[],[],[])   
for i in range(ROW):
    for j in range(COL):
        y[i].append(Cell(frame, i,j,width = 20,height = 20) )    
        y[i][j].grid(row=i,column=j)     
 
Button(root,text = "새로 시작",command=Reset).pack()   

root.mainloop()   
