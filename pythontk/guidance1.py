from tkinter import *
import customtkinter
from PIL import Image,ImageTk
import tkinter as tk
import webbrowser

class guide_details:
    def _init_(self,master):
        master = customtkinter.CTk()
        master.title("GUIDE")
        master.geometry("600x400")
        master.configure(bg='gold')

        tlabel = Label(self.master, text="GUIDANCE FOR FARMERS", font=("Arial", 30,"bold"))
        tlabel.grid(row=0, column=1)

        add_image_s1 = ImageTk.PhotoImage(Image.open("images/soil.png").resize((60,60),Image.ANTIALIAS))
        add_image_s2 = ImageTk.PhotoImage(Image.open("images/irrig.png").resize((60,60),Image.ANTIALIAS))
        add_image_s3 = ImageTk.PhotoImage(Image.open("images/watert.png").resize((60,60),Image.ANTIALIAS))
        add_image_s4 = ImageTk.PhotoImage(Image.open("images/fertilizer.png").resize((60,60),Image.ANTIALIAS))
        add_image_s5 = ImageTk.PhotoImage(Image.open("images/cloud.png").resize((60,60),Image.ANTIALIAS))

        btn_1 = customtkinter.CTkButton(root=master, image=add_image_s1, text="Soil Prep", width=190, height=40, compound=TOP, command=self.S1, border_color='black', border_width=2)
        btn_1.place(x=140,y=90)
        btn_2 = customtkinter.CTkButton(root=master, image=add_image_s2, text="Irrigation", width=190, height=40, compound=TOP, command=self.S2, border_color='black', border_width=2)
        btn_2.place(x=340,y=90)
        btn_3 = customtkinter.CTkButton(root=master, image=add_image_s3, text="Water Use", width=190, height=40, compound=TOP, command=self.S3, border_color='black', border_width=2)
        btn_3.place(x=140,y=190)
        btn_4 = customtkinter.CTkButton(root=master, image=add_image_s4, text="Fertilizer", width=190, height=40, compound=TOP, command=self.S4, border_color='black', border_width=2)
        btn_4.place(x=340,y=190)
        btn_5 = customtkinter.CTkButton(root=master, image=add_image_s5, text="Climate", width=190, height=40, compound=TOP, command=self.S5, border_color='black', border_width=2)
        btn_5.place(x=240,y=290)

    def S1(self):
          textbox_window = tk.Toplevel(master)
          textbox = tk.Text(textbox_window,width=250,height=80,font=("times new roman",14,"bold"),bg = "yellow")
          textbox.tag_config("red")
          textbox.pack()
          with open("textfile/soil.txt","r") as f:
             text = f.read()
             textbox.insert("1.0",text)

    def S2(self):
           textbox_window = tk.Toplevel(master)
           textbox = tk.Text(textbox_window,width=250,height=80,font=("times new roman",14,"bold"),bg = "yellow")
           textbox.tag_config("red")
           textbox.pack()
           with open("textfile/irrigation.txt","r") as f:
              text = f.read()
              textbox.insert("1.0",text)
    def S3(self):
           textbox_window = tk.Toplevel(master)
           textbox = tk.Text(textbox_window,width=250,height=80,font=("times new roman",14,"bold"),bg = "yellow")
           textbox.tag_config("red")
           textbox.pack()
           with open("textfile/wateruse.txt","r") as f:
             text = f.read()
             textbox.insert("1.0",text)
    def S4(self):
           textbox_window = tk.Toplevel(master)
           textbox = tk.Text(textbox_window,width=250,height=80,font=("times new roman",14,"bold"),bg = "yellow")
           textbox.tag_config("red")
           textbox.pack()
           with open("textfile/fertilizer.txt","r") as f:
             text = f.read()
             textbox.insert("1.0",text)
    def S5(self):
           textbox_window = tk.Toplevel(master)
           textbox = tk.Text(textbox_window,width=250,height=80,font=("times new roman",14,"bold"),bg = "yellow")
           textbox.tag_config("red")
           textbox.pack()
           with open("textfile/climate.txt","r") as f:
             text = f.read()
             textbox.insert("1.0",text)

if __name__=="__main__":
    master=Tk()
    obj=guide_details()
    master.mainloop()
    
    
