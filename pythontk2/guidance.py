from tkinter import *
import customtkinter
from PIL import Image,ImageTk
import tkinter as tk
import webbrowser


   
      
def S1():
      textbox_window = tk.Toplevel(root)
      textbox = tk.Text(textbox_window,width=250,height=80,font=("times new roman",14,"bold"),bg = "yellow")
      textbox.tag_config("red")
      textbox.pack()
      with open("pythontk2/textfile/soil.txt","r") as f:
         text = f.read()
         textbox.insert("1.0",text)

def S2():
       textbox_window = tk.Toplevel(root)
       textbox = tk.Text(textbox_window,width=250,height=80,font=("times new roman",14,"bold"),bg = "yellow")
       textbox.tag_config("red")
       textbox.pack()
       with open("pythontk2/textfile/irrigation.txt","r") as f:
         text = f.read()
         textbox.insert("1.0",text)
def S3():
       textbox_window = tk.Toplevel(root)
       textbox = tk.Text(textbox_window,width=250,height=80,font=("times new roman",14,"bold"),bg = "yellow")
       textbox.tag_config("red")
       textbox.pack()
       with open("pythontk2/textfile/wateruse.txt","r") as f:
         text = f.read()
         textbox.insert("1.0",text)

def S4():
       textbox_window = tk.Toplevel(root)
       textbox = tk.Text(textbox_window,width=250,height=80,font=("times new roman",14,"bold"),bg = "yellow")
       textbox.tag_config("red")
       textbox.pack()
       with open("pythontk2/textfile/fertilizer.txt","r") as f:
         text = f.read()
         textbox.insert("1.0",text)
         
def S5():
       textbox_window = tk.Toplevel(root)
       textbox = tk.Text(textbox_window,width=250,height=80,font=("times new roman",14,"bold"),bg = "yellow")
       textbox.tag_config("red")
       textbox.pack()
       with open("pythontk2/textfile/climate.txt","r") as f:
         text = f.read()
         textbox.insert("1.0",text)  

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.title("GUIDE")
root.geometry("600x400")
root.configure(bg='gold')



#tlabel = Label(root,text="GUIDANCE FOR FARMERS", font=("Arial", 30,"bold"))
#tlabel.grid(row=0,column=12)




add_image_s1 = ImageTk.PhotoImage(Image.open("pythontk2/images/soil.png").resize((60,60),Image.ANTIALIAS))
add_image_s2 = ImageTk.PhotoImage(Image.open("pythontk2/images/irrig.png").resize((60,60),Image.ANTIALIAS))
add_image_s3 = ImageTk.PhotoImage(Image.open("pythontk2/images/watert.png").resize((60,60),Image.ANTIALIAS))
add_image_s4 = ImageTk.PhotoImage(Image.open("pythontk2/images/fertilizer.png").resize((60,60),Image.ANTIALIAS))
add_image_s5 = ImageTk.PhotoImage(Image.open("pythontk2/images/cloud.png").resize((60,60),Image.ANTIALIAS))

btn_1 = customtkinter.CTkButton(master=root,image=add_image_s1,text="Soil Prep",width=190,height=40,compound=TOP,command=S1,border_color='black',border_width=2)
btn_1.place(x=140,y=90)
btn_2 = customtkinter.CTkButton(master=root,image=add_image_s2,text="Irrigation",width=190,height=40,compound=TOP,command=S2,border_color='black',border_width=2)
btn_2.place(x=340,y=90)
btn_3 = customtkinter.CTkButton(master=root,image=add_image_s3,text="Water Use",width=190,height=40,compound=TOP,command=S3,border_color='black',border_width=2)
btn_3.place(x=140,y=190)
btn_4 = customtkinter.CTkButton(master=root,image=add_image_s4,text="Fertilizer",width=190,height=40,compound=TOP,command=S4,border_color='black',border_width=2)
btn_4.place(x=340,y=190)
btn_5 = customtkinter.CTkButton(master=root,image=add_image_s5,text="Climate",width=190,height=40,compound=TOP,command=S5,border_color='black',border_width=2)
btn_5.place(x=240,y=290)

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

root.mainloop()


