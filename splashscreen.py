from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import os

def bar():
    l4 = Label(splash, text='Loading...', fg='white', bg='#249794')
    lst4 = ('Calibri (Body)', 10)
    l4.config(font=lst4)
    l4.place(x=18, y=600)

    import time
    r = 0
    for i in range(100):
        progress['value'] = r
        splash.update_idletasks()
        time.sleep(0.03)
        r = r + 1

    splash.destroy()
    import loginpage



splash=Tk()
image=PhotoImage(file="images/welcomefarm1.png")
height = 650
width = 1110
x=(splash.winfo_screenwidth()//2)-(width//2)
y=(splash.winfo_screenheight()//2)-(height//2)
splash.geometry('{}x{}+{}+{}'.format(width,height,x,y))
splash.overrideredirect(True)

splash.config(background="#2F6C60")
bg_label = Label(splash,image=image)
bg_label.pack()
b1=Button(splash,width=10,height=2,text='Get Started',border=0,command=bar,bg='dark green',fg="white",font=('Microsoft YaHei UI Light',11,'bold'))
b1.place(x=170,y=500)

s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='forest green')
progress=Progressbar(splash,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=1110,mode='determinate',)

progress.place(x=-10, y=630)

splash.resizable(False,False)
splash.mainloop()
