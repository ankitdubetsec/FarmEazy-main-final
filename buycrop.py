import json
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
import urllib.request
import sys
import pywhatkit as pwt

import pandas as pd
from datetime import *


# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('x.csv')

# def go_home():
#     weather.destroy()
#     import newDashboard

def go_home():
    weather.destroy()
    import newDashboard3

weather = Tk()
weather.title("Buy crops directly from farmers")
weather.geometry("890x470+300+200")
weather.configure(bg="gold")
weather.resizable(True,True)

nav_frame = tk.Frame(weather, bg="#57adff")
nav_frame.place(relx=0,rely=0,relwidth=1,relheight=0.08)

title_label = tk.Label(nav_frame, text="FarmEazy", bg="#57adff", fg="black", padx=10,font=("Helvetica", 15,'bold'))
title_label.pack(side="left")
# font=('poppins',25,'bold')
# Create a frame for the buttons on the right
button_frame = tk.Frame(nav_frame, bg="#57adff")
button_frame.pack(side="right")

# Create three buttons
button1 = tk.Button(button_frame, text="Home", bg="#57adff", fg="black", padx=10, borderwidth=0, highlightthickness=0,font=("Helvetica", 11,"bold"),command=go_home)
button1.pack(side="right", padx=10)

button2 = tk.Button(button_frame, text="Log Out", bg="#57adff", fg="black", padx=10, borderwidth=0, highlightthickness=0,font=("Helvetica", 11,"bold"))
button2.pack(side="right", padx=10)

button3 = tk.Button(button_frame, text="About us", bg="#57adff", fg="black", padx=10, borderwidth=0, highlightthickness=0,font=("Helvetica", 11,"bold"))
button3.pack(side="right", padx=10)

def label_clicked():
    weather.destroy()
    import send_email

   
   
i=0

def getWeather():
    
    #first cell
    
    global i
    
    

    #second cell
    loc=textfield.get()
    data1 = df.loc[df['Location'] == loc, 'Crop'].iloc[i]
    data2 = df.loc[df['Location'] == loc, 'Quantity'].iloc[i]
    data3 = df.loc[df['Location'] == loc, 'Msp'].iloc[i]
    data4=StringVar()
    data4 = (df.loc[df['Location'] == loc, 'Name'].iloc[i])
    name1.config(text=f"{data4.upper()}")
    day2temp.config(text=f"crop:{data1}\nqty:{data2} kg\nMsp:{data3}")
    img = (Image.open(f"./ttkinter2/{data1}.png"))
    resized_image = img.resize((50,45))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image=photo2
    # tempday2 = DaysjsonData['days'][1]['temp']
    # status2 =  DaysjsonData['days'][1]['icon']
    # day2temp.config(text=f"{tempday2}\n{status2}")
    

    # #third cell
    i=i+1
    loc=textfield.get()
    data1 = df.loc[df['Location'] == loc, 'Crop'].iloc[i]
    data2 = df.loc[df['Location'] == loc, 'Quantity'].iloc[i]
    data3 = df.loc[df['Location'] == loc, 'Msp'].iloc[i]
    data4=StringVar()
    data4 = (df.loc[df['Location'] == loc, 'Name'].iloc[i])
    name2.config(text=f"{data4.upper()}")
    day3temp.config(text=f"crop:{data1}\nqty:{data2} kg\nMsp:{data3}")
    img = (Image.open(f"./ttkinter2/{data1}.png"))
    resized_image = img.resize((50,45))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image=photo3

    i=i+1
    loc=textfield.get()
    data1 = df.loc[df['Location'] == loc, 'Crop'].iloc[i]
    data2 = df.loc[df['Location'] == loc, 'Quantity'].iloc[i]
    data3 = df.loc[df['Location'] == loc, 'Msp'].iloc[i]
    data4=StringVar()
    data4 = (df.loc[df['Location'] == loc, 'Name'].iloc[i])
    name3.config(text=f"{data4.upper()}")
    day4temp.config(text=f"crop:{data1}\nqty:{data2} kg\nMsp:{data3}")
    img = (Image.open(f"./ttkinter2/{data1}.png"))
    resized_image = img.resize((50,45))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image=photo4
    
    i=i+i
    loc=textfield.get()
    data1 = df.loc[df['Location'] == loc, 'Crop'].iloc[i]
    data2 = df.loc[df['Location'] == loc, 'Quantity'].iloc[i]
    data3 = df.loc[df['Location'] == loc, 'Msp'].iloc[i]
    data4=StringVar()
    data4 = (df.loc[df['Location'] == loc, 'Name'].iloc[i])
    name4.config(text=f"{data4.upper()}")
    day5temp.config(text=f"crop:{data1}\nqty:{data2} kg\nMsp:{data3}")
    img = (Image.open(f"./ttkinter2/{data1}.png"))
    resized_image = img.resize((50,45))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image=photo5
    
    i=i+1
    loc=textfield.get()
    data1 = df.loc[df['Location'] == loc, 'Crop'].iloc[i]
    data2 = df.loc[df['Location'] == loc, 'Quantity'].iloc[i]
    data3 = df.loc[df['Location'] == loc, 'Msp'].iloc[i]
    data4=StringVar()
    data4 = (df.loc[df['Location'] == loc, 'Name'].iloc[i])
    name5.config(text=f"{data4.upper()}")
    day6temp.config(text=f"crop:{data1}\nqty:{data2} kg\nMsp:{data3}")
    img = (Image.open(f"./ttkinter2/{data1}.png"))
    resized_image = img.resize((50,45))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image=photo6
    i=i+1

    loc=textfield.get()
    data1 = df.loc[df['Location'] == loc, 'Crop'].iloc[i]
    data2 = df.loc[df['Location'] == loc, 'Quantity'].iloc[i]
    data3 = df.loc[df['Location'] == loc, 'Msp'].iloc[i]
    data4=StringVar()
    data4 = (df.loc[df['Location'] == loc, 'Name'].iloc[i])
    name6.config(text=f"{data4.upper()}")
    day7temp.config(text=f"crop:{data1}\nqty:{data2} kg\nMsp:{data3}")
    img = (Image.open(f"./ttkinter2/{data1}.png"))
    resized_image = img.resize((50,45))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image=photo7
    i=i+1
    
    loc=textfield.get()
    data1 = df.loc[df['Location'] == loc, 'Crop'].iloc[i]
    data2 = df.loc[df['Location'] == loc, 'Quantity'].iloc[i]
    data3 = df.loc[df['Location'] == loc, 'Msp'].iloc[i]
    data4=StringVar()
    data4 = (df.loc[df['Location'] == loc, 'Name'].iloc[i])
    name7.config(text=f"{data4.upper()}")
    day8temp.config(text=f"crop:{data1}\nqty:{data2} kg\nMsp:{data3}")
    img = (Image.open(f"./ttkinter2/{data1}.png"))
    resized_image = img.resize((50,45))
    photo8 = ImageTk.PhotoImage(resized_image)
    eighthimage.config(image=photo8)
    eighthimage.image=photo8
    
    i=i+1
    loc=textfield.get()
    data1 = df.loc[df['Location'] == loc, 'Crop'].iloc[i]
    data2 = df.loc[df['Location'] == loc, 'Quantity'].iloc[i]
    data3 = df.loc[df['Location'] == loc, 'Msp'].iloc[i]
    data4=StringVar()
    data4 = (df.loc[df['Location'] == loc, 'Name'].iloc[i])
    name8.config(text=f"{data4.upper()}")
    day9temp.config(text=f"crop:{data1}\nqty:{data2} kg\nMsp:{data3}")
    img = (Image.open(f"./ttkinter2/{data1}.png"))
    resized_image = img.resize((50,45))
    photo9 = ImageTk.PhotoImage(resized_image)
    ninthimage.config(image=photo9)
    ninthimage.image=photo9
    i=i+1
    

    
    


##icon
image_icon = PhotoImage(file="./ttkinter2/location.png")
weather.iconphoto(False,image_icon)


#search box
Search_image = PhotoImage(file="images/longrec4.png")
myimage=Label(image=Search_image,bg="gold")
myimage.place(x=270,y=80)

# Round_box = PhotoImage(file="./ttkinter2/farmergold.png")
Round_box = (Image.open(f"./ttkinter2/farmergold.png"))
resized_image = Round_box.resize((250,250))
photox = ImageTk.PhotoImage(resized_image)
Label(weather,image=photox,bg="gold",borderwidth=3).place(x=30,y=50)


weat_image = (Image.open(f"./ttkinter2/location.png"))
resized_image = weat_image.resize((55,50))
photo = ImageTk.PhotoImage(resized_image)
weatherimage=Label(weather,image=photo,bg="#203243",border=0)
weatherimage.place(x=308,y=145)

textfield = tk.Entry(weather,justify='center',width=15,font=('poppins',25,'bold'),bg="black",border=0,fg="white")
textfield.place(x=370,y=150)
textfield.focus()

Search_icon =PhotoImage(file="images/searchicon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="black",activebackground="black",command=getWeather)
myimage_icon.place(x=700,y=145)


#Bottom Box
weatherframe = Frame(weather,width=900,height=180,bg='#212120')
weatherframe.pack(side=BOTTOM)

#bottom boxes
# firstbox = PhotoImage(file="images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="images/Rounded Rectangle 2 copy.png")

Label(weatherframe,image=secondbox,bg='#212120').place(x=250,y=15)


# Bind the label to the label_clicked function

x=tk.Label(weatherframe,image=secondbox,bg='#212120')
x.place(x=350,y=15)
Label(weatherframe,image=secondbox,bg='#212120').place(x=450,y=15)
Label(weatherframe,image=secondbox,bg='#212120').place(x=550,y=15)
Label(weatherframe,image=secondbox,bg='#212120').place(x=650,y=15)
Label(weatherframe,image=secondbox,bg='#212120').place(x=750,y=15)
Label(weatherframe,image=secondbox,bg='#212120').place(x=45,y=15)
Label(weatherframe,image=secondbox,bg='#212120').place(x=145,y=15)
Button(weatherframe,bg='#57adff',text="Buy",command=label_clicked,width=7,height=1).place(x=55,y=145)
Button(weatherframe,bg='#57adff',text="Buy",command=label_clicked,width=7,height=1).place(x=155,y=145)
Button(weatherframe,bg='#57adff',text="Buy",command=label_clicked,width=7,height=1).place(x=260,y=145)
Button(weatherframe,bg='#57adff',text="Buy",command=label_clicked,width=7,height=1).place(x=360,y=145)
Button(weatherframe,bg='#57adff',text="Buy",command=label_clicked,width=7,height=1).place(x=460,y=145)
Button(weatherframe,bg='#57adff',text="Buy",command=label_clicked,width=7,height=1).place(x=560,y=145)
Button(weatherframe,bg='#57adff',text="Buy",command=label_clicked,width=7,height=1).place(x=660,y=145)
def what():
    currtime=datetime.now()
    hr=currtime.hour
    min=currtime.minute+1
    print(hr)
    print(min)
    pwt.sendwhatmsg("+917666985886","I want buy your crops",hr,min)

Button(weatherframe,bg='#57adff',text="Buy",command=what,width=7,height=1).place(x=760,y=145)





Search_icon2 =PhotoImage(file="ttkinter2/right3.png")
Button(weatherframe,image=Search_icon2,borderwidth=0,cursor="hand2",bg="#212120",command=getWeather).place(x=835,y=56)



secondframe=Frame(weather,width=70,height=115,bg='#282829')
secondframe.place(x=255,y=310)
name1=Label(secondframe,bg='#282829',fg='#fff')
name1.place(x=12,y=0)
secondimage=Label(secondframe,bg='#282829')
secondimage.place(x=7,y=17)

day2temp=Label(secondframe,bg='#282829',fg='#fff')
day2temp.place(x=0,y=65)

thirdframe=Frame(weather,width=70,height=115,bg='#282829')
thirdframe.place(x=355,y=310)

name2=Label(thirdframe,bg='#282829',fg='#fff')
name2.place(x=12,y=0)
thirdimage=Label(thirdframe,bg='#282829')
thirdimage.place(x=7,y=17)
day3temp=Label(thirdframe,bg='#282829',fg='#fff')
day3temp.place(x=0,y=65)

fourthframe=Frame(weather,width=70,height=115,bg='#282829')
fourthframe.place(x=455,y=310)
name3=Label(fourthframe,bg='#282829',fg="#fff")
name3.place(x=12,y=0)
fourthimage=Label(fourthframe,bg='#282829')
fourthimage.place(x=7,y=17)
day4temp=Label(fourthframe,bg='#282829',fg='#fff')
day4temp.place(x=0,y=65)

fifthframe=Frame(weather,width=70,height=115,bg='#282829')
fifthframe.place(x=555,y=310)
name4=Label(fifthframe,bg='#282829',fg="#fff")
name4.place(x=12,y=0)
fifthimage=Label(fifthframe,bg='#282829')
fifthimage.place(x=7,y=17)
day5temp=Label(fifthframe,bg='#282829',fg='#fff')
day5temp.place(x=0,y=65)

sixthframe=Frame(weather,width=70,height=115,bg='#282829')
sixthframe.place(x=655,y=310)
name5=Label(sixthframe,bg='#282829',fg="#fff")
name5.place(x=12,y=0)
sixthimage=Label(sixthframe,bg='#282829')
sixthimage.place(x=7,y=17)
day6temp=Label(sixthframe,bg='#282829',fg='#fff')
day6temp.place(x=0,y=65)


seventhframe=Frame(weather,width=70,height=115,bg='#282829')
seventhframe.place(x=755,y=310)
name6=Label(seventhframe,bg='#282829',fg="#fff")
name6.place(x=12,y=0)
seventhimage=Label(seventhframe,bg='#282829')
seventhimage.place(x=7,y=17)
day7temp=Label(seventhframe,bg='#282829',fg='#fff')
day7temp.place(x=0,y=65)

eighthframe=Frame(weather,width=70,height=115,bg='#282829')
eighthframe.place(x=50,y=310)
name7=Label(eighthframe,bg='#282829',fg="#fff")
name7.place(x=12,y=0)
eighthimage=Label(eighthframe,bg='#282829')
eighthimage.place(x=7,y=17)
day8temp=Label(eighthframe,bg='#282829',fg='#fff')
day8temp.place(x=0,y=65)


ninthframe=Frame(weather,width=70,height=115,bg='#282829')
ninthframe.place(x=150,y=310)
name8=Label(ninthframe,bg='#282829',fg="#fff")
name8.place(x=12,y=0)
ninthimage=Label(ninthframe,bg='#282829')
ninthimage.place(x=7,y=17)
day9temp=Label(ninthframe,bg='#282829',fg='#fff')
day9temp.place(x=0,y=65)
weather.mainloop()
