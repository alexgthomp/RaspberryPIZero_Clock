import pyautogui
from tkinter import *
import datetime



def updateTimeDate():
    
    date = '{:%B-%d-%y}'.format(datetime.datetime.now())
    mainCanvas.itemconfigure(labelDate, text=date)
    
    time = '{:%-I:%M:%S %p}'.format(datetime.datetime.now())
    mainCanvas.itemconfigure(labelTime, text=time)
    
    pyautogui.moveRel(0, 1)
    pyautogui.moveRel(0, -1)
    root.after(1, updateTimeDate)



class CanvasCreate:
    def __init__(self,master):
        global mainCanvas, labelTime, labelDate
        mainCanvas = Canvas(root, width=480, height=320)
        mainCanvas.config(cursor='none')
        mainCanvas.pack()
        
        mainCanvas.focus_set()
        mainCanvas.bind("<Key>", self.key)
        mainCanvas.bind("<Escape>", self.key)
        
        canvasBackground = mainCanvas.create_image( 0,0, image = background, anchor=NW)
        
        date = '{:%B-%d-%y}'.format(datetime.datetime.now())
        labelDate = mainCanvas.create_text(240,20, text=date, font=("Anonymous Pro", 30), fill ="white")
        
        time = '{:%-I:%M:%S %p}'.format(datetime.datetime.now())
        labelTime = mainCanvas.create_text(240,160, text=time, font=("Anonymous Pro", 55), fill ="white")
        updateTimeDate()
    
    def key(self,event):
        print('Quit')
        root.destroy()

#setup GUI to Fit Screen
root = Tk()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))



background = PhotoImage(file = "~/Downloads/mkl1sq0twt7z.gif") #Change path to path of your selected photo

CanvasCreate(root)


root.mainloop()
root.destroy()
