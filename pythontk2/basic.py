from tkinter import *
from PIL import Image,ImageTk
from info import crop_info
#import PIL.Image
import tkinter as tk
import webbrowser
#import guidance

class Seeds:
   def __init__(self,root):
        self.root=root
        self.root.title("CROP SECTION")
        self.root.geometry("800x800+0+0")
        self.root.config(bg = "green")
        
              
        #img4=Image.open(r"C:\Users\hp\Desktop\image\logo.png")
        #img4=img4.resize((380,450),Image.ANTIALIAS)
        #self.photoimg4=ImageTk.PhotoImage(img4)

        #lbl1=Label(self.root,image=self.photoimg4,bd=4,relief=RIDGE,bg="orange")
        #lbl1.place(x=80,y=250,width=1000,height=400)

        #img1=Image.open(r"C:\Users\hp\Desktop\image\learn.jpg")
        #img1=img1.resize((450,500),Image.ANTIALIAS)
        #self.photoimg1=ImageTk.PhotoImage(img1)

        #lbl=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        #lbl.place(x=800,y=250,width=275,height=200)

    #----------TITLE------------
        lbl_title=Label(self.root,text="CROP ADVISORY",font=("times new roman",40,"bold"),bg="black",fg="gold")
        lbl_title.place(x=15,y=100,width=750,height=50)

    #---------main_frame----------
        #main_frame=Frame(self.root,bd=4,relief=RIDGE)
        #main_frame.place(x=10,y=250,width=1000,height=400)

    #---------button_frame----------
        
        btn_frame=Frame(self.root,bd=4,relief=RIDGE,bg="cyan")
        btn_frame.place(x=300,y=250,width=230,height=170)

        info_btn=Button(btn_frame,text="CROP  PRACTICES",command=self.crop_details,width=30,height=4,font=("TIMES NEW ROMAN",10,"bold"),bg="black",fg="yellow",bd=4,relief=RIDGE)
        info_btn.grid(row=0,column=0,padx =1,pady=3)

        #price_btn=Button(btn_frame,text="PRICE DETAILS",width=30,height=3,font=("times new roman",10,"bold"),bg="black",fg="yellow",bd=0)
        #price_btn.grid(row=1,column=0,pady=1)

        guide_btn=Button(btn_frame,text="GUIDANCE",width=30,height=4,font=("times new roman",10,"bold"),bg="black",fg="yellow",bd=4,relief=RIDGE)
        guide_btn.grid(row=2,column=0,pady=3)

    def crop_details(self):
        self.new_window=Toplevel(self.root)
        self.app=crop_info(self.new_window)

        #cust_btn=Button(btn_frame,text="Seed Info",width=220,font=("times new roman",40,"bold"),bg="black",fg="gold",cursor="hand1")
        #cust_btn.grid
        #img2=Image.open(r"C:\Users\hp\Desktop\image\price1.jpg")
        #img2=img2.resize((380,450),Image.ANTIALIAS)
        #self.photoimg2=ImageTk.PhotoImage(img2)

        #lbl1=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        #lbl1.place(x=80,y=450,width=300,height=200)

        #img3=Image.open(r"C:\Users\hp\Desktop\image\guide.jpg")
        #img3=img3.resize((450,500),Image.ANTIALIAS)
        #self.photoimg3=ImageTk.PhotoImage(img3)

        #lbl1=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        #lbl1.place(x=780,y=450,width=300,height=200)

    
        
           
        

        
        
        



if __name__=="__main__":
    root = Tk()
    obj=Seeds(root)
    root.mainloop()




