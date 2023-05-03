from tkinter import *
from tkinter import messagebox
import tkinter as tk
import customtkinter
from PIL import Image,ImageTk
from garlic import garlic_info
from wheat import wheat_info
from soybean import soy_info
from maize import maize_info
from orange import orange_info
from groundnut import groundnut_info
from sugarcane import sugar_info
from tea import tea_info
from coffee import coffee_info
from sunflower import sunflower_info
from cotton import cotton_info
from mango import mango_info
from banana import banana_info
from lemon import lemon_info


class crop_info:

    def __init__(self,root):
        self.root=root
        self.root.title("CROP SECTION")
        self.root.geometry("1295x650+0+0")
        self.root.config(bg = "orange")

        #background_image = PhotoImage(file = "image/kbg.jpg")
        #label = Label(root, image = background_image)
        #label.place(x=0, y=0, relwidth=1, relheight=1)
        #self.root.color("Green")
        
        
        #root.mainloop()
        
        lbl_title=Label(self.root,text="PLANTATION",font=("times new roman",40,"bold"),bg="green",fg="black")
        lbl_title.place(x=125,y=50,width=1000,height=50)

        btn_frame=Frame(self.root,bd=4,relief=SUNKEN,bg="cyan")
        btn_frame.place(x=320,y=130,width=250,height=480)

        #img4=Image.open(r"C:\Users\hp\Desktop\python\image\bg.jpg")
        #img4=img4.resize((380,450),Image.ANTIALIAS)
        #self.photoimg4=ImageTk.PhotoImage(img4)

        #lbl1=Label(self.root,image=self.photoimg4,bd=4,relief=RIDGE)
        #lbl1.place(x=875,y=250,width=300,height=300)

        img4=Image.open("images/image/farmer.jpg")
        img4=img4.resize((380,450),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lbl1=Label(self.root,image=self.photoimg4,bd=4,relief=RIDGE)
        lbl1.place(x=875,y=250,width=300,height=300)

        img3=Image.open("images/image/farmer1.jpg")
        img3=img3.resize((380,450),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbl2=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lbl2.place(x=10,y=250,width=300,height=300)

        lbl_title=Label(self.root,text="SELECT CROP",font=("times new roman",20,"bold"),bg="red",fg="black")
        lbl_title.place(x=55,y=200,width=200,height=50)

        lbl_title1=Label(self.root,text="SELECT CROP",font=("times new roman",20,"bold"),bg="red",fg="black")
        lbl_title1.place(x=930,y=200,width=200,height=50)

        btn_frame1=Frame(self.root,bd=4,relief=SUNKEN,bg="cyan")
        btn_frame1.place(x=600,y=130,width=250,height=480)

        

        info_btn=Button(btn_frame,text="GARLIC",width=30,command=self.garlic_details,height=3,font=("TIMES NEW ROMAN",10,"bold"),bg="black",fg="yellow",bd=6,relief="sunken")
        info_btn.grid(row=0,column=0,pady=1)
        info_btn.place(x=10,y=5)
        

        info1_btn=Button(btn_frame,text="WHEAT",width=30,command=self.wheat_details,height=3,font=("TIMES NEW ROMAN",10,"bold"),bg="black",fg="yellow",bd=6,relief="sunken")
        info1_btn.grid(row=1,column=0,pady=1)
        info1_btn.place(x=10,y=70)

        info2_btn=Button(btn_frame,text="SOYABEAN",width=30,command=self.soy_details,height=3,font=("TIMES NEW ROMAN",10,"bold"),bg="black",fg="yellow",bd=6,relief="sunken")
        info2_btn.grid(row=2,column=0,pady=1)
        info2_btn.place(x=10,y=135)

        info3_btn=Button(btn_frame,text="MAIZE",width=30,command=self.maize_details,height=3,font=("TIMES NEW ROMAN",10,"bold"),bg="black",fg="yellow",bd=6,relief="sunken",)
        info3_btn.grid(row=3,column=0,pady=1)
        info3_btn.place(x=10,y=200)

        info4_btn=Button(btn_frame,text="ORANGE",width=30,command=self.orange_details,height=3,font=("TIMES NEW ROMAN",10,"bold"),bg="black",fg="yellow",bd=6,relief="sunken")
        info4_btn.grid(row=4,column=0,pady=1)
        info4_btn.place(x=10,y=265)

        info5_btn=Button(btn_frame,text="GROUNDNUT",width=30,command=self.groundnut_details,height=3,font=("TIMES NEW ROMAN",10,"bold"),bg="black",fg="yellow",bd=6,relief="sunken")
        info5_btn.grid(row=5,column=0,pady=1)
        info5_btn.place(x=10,y=330)

        info6_btn=Button(btn_frame,text="SUGARCANE",width=30,command=self.sugar_details,height=3,font=("TIMES NEW ROMAN",10,"bold"),bg="black",fg="yellow",bd=6,relief="sunken")
        info6_btn.grid(row=6,column=0,pady=1)
        info6_btn.place(x=10,y=395)

        info7_btn=Button(btn_frame1,text="TEA LEAVES",width=30,command=self.tea_details,height=3,font=("TIMES NEW ROMAN",10,"bold"),bg="black",fg="yellow",bd=6,relief="sunken")
        info7_btn.grid(row=0,column=0,pady=1)
        info7_btn.place(x=10,y=5)

        info8_btn=Button(btn_frame1,text="COFFEE",width=30,command=self.coffee_details,height=3,font=("TIMES NEW ROMAN",10,"bold"),bg="black",fg="yellow",bd=6,relief="sunken")
        info8_btn.grid(row=1,column=0,pady=1)
        info8_btn.place(x=10,y=70)

        info9_btn=Button(btn_frame1,text="LEMON",width=30,command=self.lemon_details,height=3,font=("TIMES NEW ROMAN",10,"bold"),bg="black",fg="yellow",bd=6,relief="sunken")
        info9_btn.grid(row=2,column=0,pady=1)
        info9_btn.place(x=10,y=135)

        info10_btn=Button(btn_frame1,text="SUNFLOWER",width=30,command=self.sunflower_details,height=3,font=("TIMES NEW ROMAN",10,"bold"),bg="black",fg="yellow",bd=6,relief="sunken")
        info10_btn.grid(row=3,column=0,pady=1)
        info10_btn.place(x=10,y=200)

        info11_btn=Button(btn_frame1,text="COTTON",width=30,command=self.cotton_details,height=3,font=("TIMES NEW ROMAN",10,"bold"),bg="black",fg="yellow",bd=6,relief="sunken")
        info11_btn.grid(row=4,column=0,pady=1)
        info11_btn.place(x=10,y=265)

        info12_btn=Button(btn_frame1,text="MANGO",width=30,command=self.mango_details,height=3,font=("TIMES NEW ROMAN",10,"bold"),bg="black",fg="yellow",bd=6,relief="sunken")
        info12_btn.grid(row=5,column=0,pady=1)
        info12_btn.place(x=10,y=330)

        info13_btn=Button(btn_frame1,text="BANANA",width=30,command=self.banana_details,height=3,font=("TIMES NEW ROMAN",10,"bold"),bg="black",fg="yellow",bd=6,relief="sunken")
        info13_btn.grid(row=6,column=0,pady=1)
        info13_btn.place(x=10,y=395)

        #info14_btn=Button(btn_frame1,text="LEMON",width=30,command=self.lemon_details,height=3,font=("TIMES NEW ROMAN",10,"bold"),bg="black",fg="yellow",bd=6,relief="sunken")
        #info14_btn.grid(row=7,column=0,pady=1)
        nav_frame = tk.Frame(root, bg="#badc57")
        nav_frame.place(relx=0,rely=0,relwidth=1,relheight=0.08)

# Create a label for the title on the left corner
        title_label = tk.Label(nav_frame, text="Farm Eazy", bg="#badc57", fg="black", padx=10,font='Helvetica 18 bold')
        title_label.pack(side="left")

# Create a frame for the buttons on the right
        button_frame = tk.Frame(nav_frame, bg="#badc57")
        button_frame.pack(side="right")

# Create three buttons
        button1 = tk.Button(button_frame, text="Home", bg="#badc57", fg="black", padx=10, borderwidth=0, highlightthickness=0,font='Helvetica 14 bold')
        button1.pack(side="right", padx=10)

        button2 = tk.Button(button_frame, text="Log Out", bg="#badc57", fg="black", padx=10, borderwidth=0, highlightthickness=0,font='Helvetica 14 bold')
        button2.pack(side="right", padx=10)

        button3 = tk.Button(button_frame, text="About us", bg="#badc57", fg="black", padx=10, borderwidth=0, highlightthickness=0,font='Helvetica 14 bold')
        button3.pack(side="right", padx=10)
        


        
        
        
        #btn_frame=Frame(self.root,bd=4,relief=RIDGE)
        #btn_frame.place(x=350,y=175,width=200,height=550)


    def garlic_details(self):
        self.new_window=Toplevel(self.root)
        self.app=garlic_info(self.new_window)

    def wheat_details(self):
        self.new_window=Toplevel(self.root)
        self.app=wheat_info(self.new_window)

    def soy_details(self):
        self.new_window=Toplevel(self.root)
        self.app=soy_info(self.new_window)

    def maize_details(self):
        self.new_window=Toplevel(self.root)
        self.app=maize_info(self.new_window)

    def orange_details(self):
        self.new_window=Toplevel(self.root)
        self.app=orange_info(self.new_window)

    def groundnut_details(self):
        self.new_window=Toplevel(self.root)
        self.app=groundnut_info(self.new_window)

    def sugar_details(self):
        self.new_window=Toplevel(self.root)
        self.app=sugar_info(self.new_window)

    def tea_details(self):
        self.new_window=Toplevel(self.root)
        self.app=tea_info(self.new_window)

    def coffee_details(self):
        self.new_window=Toplevel(self.root)
        self.app=coffee_info(self.new_window)

    def sunflower_details(self):
        self.new_window=Toplevel(self.root)
        self.app=sunflower_info(self.new_window)

    def cotton_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cotton_info(self.new_window)

    def mango_details(self):
        self.new_window=Toplevel(self.root)
        self.app=mango_info(self.new_window)

    def banana_details(self):
        self.new_window=Toplevel(self.root)
        self.app=banana_info(self.new_window)

    def lemon_details(self):
        self.new_window=Toplevel(self.root)
        self.app=lemon_info(self.new_window)


    
if __name__=="__main__":

   root=Tk()
   obj=crop_info(root)
   root.mainloop()
