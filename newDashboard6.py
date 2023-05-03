# from tkinter import *
#
# import customtkinter
# from PIL import Image,ImageTk;
# import datetime
# now=datetime.datetime.now
#
#
# def get_weather_window():
#     root.destroy()
#     import weather
#
# class DashBoard:
#
#      def __init__(self,root):
#
#             self.root=root
#             self.root.geometry("1050x600+100+100")
#             self.root.title("FarmEazy: Farmer's Friend")
#             self.root.config(bg="white")
#
#             img1=Image.open(r"images/bgDashboaard.jpg")
#             img1 = img1.resize((1110,625),Image.LANCZOS)
#             self.photoimg1=ImageTk.PhotoImage(img1)
#
#             lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
#             lblimg.place(x=0,y=60,width=1550,height=680)
#
#             self.icon_title=PhotoImage(file="Logo_OG.png")
#             title=Label(self.root,text="FarmEazy: Farmer's Friend",image=self.icon_title,compound=LEFT,font=("Times New Roman",40,"bold"),bg="#010c48",fg="gold",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
#
#             btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1100,y=10,height=50,width=150)
#
#             self.lbl_clock=Label(self.root,text=f"Welcome to FarmEazy\t\t Login Date:{str(now().date())} \t\t Login Time:{str(now().time())}",font=("Times New Roman",15,"bold"),bg="#4d636d",fg="white")
#             self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
#
#
#             self.MenuLogo=Image.open(r"Govt_03.png")
#             self.MenuLogo=self.MenuLogo.resize((180,180),Image.LANCZOS)
#             self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
#
#
#             LeftMenu=Frame(self.root,bd=2,relief=RIDGE)
#             LeftMenu.place(x=0,y=102,width=200,height=565)
#
#             lbl_MenuLogo=Label(LeftMenu,image=self.MenuLogo)
#             lbl_MenuLogo.pack(side=TOP,fill=X)
#
#             self.AnotherLogo = Image.open(r"AnnaData.png")
#             self.AnotherLogo = self.AnotherLogo.resize((180, 180), Image.LANCZOS)
#             self.AnotherLogo = ImageTk.PhotoImage(self.AnotherLogo)
#
#             lbl_AnotherLogo = Label(LeftMenu, image=self.AnotherLogo)
#             lbl_AnotherLogo.pack(side=TOP, fill=X)
#
#             self.ThirdLogo = Image.open(r"BaliRaja.png")
#             self.ThirdLogo = self.ThirdLogo.resize((180,180), Image.LANCZOS)
#             self.ThirdLogo = ImageTk.PhotoImage(self.ThirdLogo)
#
#             lbl_ThirdLogo = Label(LeftMenu,image=self.ThirdLogo)
#             lbl_ThirdLogo.pack(side=TOP, fill=X)
#
#             lbl_footer=Label(self.root,text="FarmEazy: Farmer's Friend | Copyright: Group_07",font=("times new roman",15),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
#
#             # CropPrices = Image.open("CropPrices.png")
#             # CropPrices = CropPrices.resize((300, 150), Image.LANCZOS)
#             # CropPrices = ImageTk.PhotoImage(CropPrices)
#
#
#             add_image_s1 = ImageTk.PhotoImage(Image.open("images/sunny.png").resize((100, 100), Image.ANTIALIAS))
#             btn_1 = customtkinter.CTkButton(master=root, image=add_image_s1, text="Weather Forecast", width=220, height=80,
#                                             compound=TOP, border_color='black', border_width=3,command=get_weather_window())
#             btn_1.place(x=200, y=105)
#
#             add_image_s2 = ImageTk.PhotoImage(Image.open("images/DashGrant.png").resize((100, 100), Image.ANTIALIAS))
#             btn_2 = customtkinter.CTkButton(master=root, image=add_image_s2, text="Schemes & Magazines", width=220,
#                                             height=80,
#                                             compound=TOP, border_color='black', border_width=3)
#             btn_2.place(x=450, y=105)
#
#             add_image_s3 = ImageTk.PhotoImage(Image.open("images/seeds.png").resize((100, 100), Image.ANTIALIAS))
#             btn_3 = customtkinter.CTkButton(master=root, image=add_image_s3, text="Seed Calculator", width=220,
#                                             height=80,
#                                             compound=TOP, border_color='black', border_width=3)
#             btn_3.place(x=200, y=375)
#
#             add_image_s4 = ImageTk.PhotoImage(Image.open("images/chemical.png").resize((100, 100), Image.ANTIALIAS))
#             btn_4 = customtkinter.CTkButton(master=root, image=add_image_s4, text="Fertilizer Calculator", width=220,
#                                             height=80,
#                                             compound=TOP, border_color='black', border_width=3)
#             btn_4.place(x=200, y=240)
#
#             add_image_s5 = ImageTk.PhotoImage(Image.open("images/wheat.png").resize((100, 100), Image.ANTIALIAS))
#             btn_5 = customtkinter.CTkButton(master=root, image=add_image_s5, text="Crop Market Prices", width=220,
#                                             height=80,
#                                             compound=TOP, border_color='black', border_width=3)
#             btn_5.place(x=700, y=105)
#
#
#             add_image_s6 = ImageTk.PhotoImage(Image.open("images/harvest.png").resize((100, 100), Image.ANTIALIAS))
#             btn_6 = customtkinter.CTkButton(master=root, image=add_image_s6, text="Crop Guide", width=220,
#                                             height=80,
#                                             compound=TOP, border_color='black', border_width=3)
#             btn_6.place(x=450, y=240)
#
#
#
# root=customtkinter.CTk()
# obj=DashBoard(root)
# root.mainloop()

from tkinter import *

import customtkinter
from PIL import Image, ImageTk;
import datetime

now = datetime.datetime.now

def seedcal():
    root.destroy()
    import seeddcalculator

def get_weather_window():
    root.destroy()
    import weather

def get_guidance_window():
    root.destroy()
    import info

def get_guidance_sellcrop():
    root.destroy()
    import sellcrop

def get_guidance_buycrop():
    root.destroy()
    import buycrop

def schemes():
    root.destroy()
    import Schemes
root = customtkinter.CTk()
root.geometry("1050x600+100+100")
root.title("FarmEazy: Farmer's Friend")
root.config(bg="white")

def callCropPrices():
    root.destroy()
    import CropPrice

def x():
    root.destroy()
    import fertilizercalculator
    

img1 = Image.open(r"images/bgDashboaard.jpg")
img1 = img1.resize((1110, 625), Image.LANCZOS)
photoimg1 = ImageTk.PhotoImage(img1)

lblimg = Label(root, image=photoimg1, bd=4, relief=RIDGE)
lblimg.place(x=0, y=60, width=1550, height=680)

icon_title = PhotoImage(file="Logo_OG.png")
title = Label(root, text="FarmEazy: Farmer's Friend", image=icon_title, compound=LEFT,
                      font=("Times New Roman", 40, "bold"), bg="#010c48", fg="gold", anchor="w", padx=20).place(x=0,
                                                                                                                y=0,
                                                                                                                relwidth=1,
                                                                                                                height=70)

btn_logout = Button(root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow",
                            cursor="hand2").place(x=1100, y=10, height=50, width=150)

lbl_clock = Label(root,
                               text=f"Welcome to FarmEazy\t\t Login Date:{str(now().date())} \t\t Login Time:{str(now().time())}",
                               font=("Times New Roman", 15, "bold"), bg="#4d636d", fg="white")
lbl_clock.place(x=0, y=70, relwidth=1, height=30)

MenuLogo = Image.open(r"Govt_03.png")
MenuLogo = MenuLogo.resize((180, 180), Image.LANCZOS)
MenuLogo = ImageTk.PhotoImage(MenuLogo)

LeftMenu = Frame(root, bd=2, relief=RIDGE)
LeftMenu.place(x=0, y=102, width=200, height=565)

lbl_MenuLogo = Label(LeftMenu, image=MenuLogo)
lbl_MenuLogo.pack(side=TOP, fill=X)

AnotherLogo = Image.open(r"AnnaData.png")
AnotherLogo = AnotherLogo.resize((180, 180), Image.LANCZOS)
AnotherLogo = ImageTk.PhotoImage(AnotherLogo)

lbl_AnotherLogo = Label(LeftMenu, image=AnotherLogo)
lbl_AnotherLogo.pack(side=TOP, fill=X)

ThirdLogo = Image.open(r"BaliRaja.png")
ThirdLogo = ThirdLogo.resize((180, 180), Image.LANCZOS)
ThirdLogo = ImageTk.PhotoImage(ThirdLogo)

lbl_ThirdLogo = Label(LeftMenu, image=ThirdLogo)
lbl_ThirdLogo.pack(side=TOP, fill=X)

lbl_footer = Label(root, text="FarmEazy: Farmer's Friend | Copyright: Group_07",
                           font=("times new roman", 15), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)

        # CropPrices = Image.open("CropPrices.png")
        # CropPrices = CropPrices.resize((300, 150), Image.LANCZOS)
        # CropPrices = ImageTk.PhotoImage(CropPrices)

add_image_s1 = ImageTk.PhotoImage(Image.open("images/sunny.png").resize((100, 100), Image.ANTIALIAS))
btn_1 = customtkinter.CTkButton(master=root, image=add_image_s1, text="Weather Forecast", width=220, height=80,
                                        compound=TOP, border_color='black', border_width=3,
                                        command=get_weather_window)
btn_1.place(x=200, y=105)

add_image_s2 = ImageTk.PhotoImage(Image.open("images/DashGrant.png").resize((100, 100), Image.ANTIALIAS))
btn_2 = customtkinter.CTkButton(master=root, image=add_image_s2, text="Schemes & Magazines", width=220,
                                        height=80,
                                        compound=TOP,command=schemes ,border_color='black', border_width=3)
btn_2.place(x=450, y=105)

add_image_s3 = ImageTk.PhotoImage(Image.open("images/seeds.png").resize((100, 100), Image.ANTIALIAS))
btn_3 = customtkinter.CTkButton(master=root, image=add_image_s3, text="Seed Calculator", width=220,
                                        height=80,
                                        compound=TOP,command=seedcal, border_color='black', border_width=3)
btn_3.place(x=200, y=375)

add_image_s4 = ImageTk.PhotoImage(Image.open("images/chemical.png").resize((100, 100), Image.ANTIALIAS))
btn_4 = customtkinter.CTkButton(master=root, image=add_image_s4, text="Fertilizer Calculator", width=220,
                                        height=80,
                                        compound=TOP, border_color='black', border_width=3,command=x)
btn_4.place(x=200, y=240)

add_image_s5 = ImageTk.PhotoImage(Image.open("images/wheat.png").resize((100, 100), Image.ANTIALIAS))
btn_5 = customtkinter.CTkButton(master=root, image=add_image_s5, text="Crop Market Prices", width=220,
                                        height=80,
                                        compound=TOP, border_color='black', border_width=3,command=callCropPrices)
btn_5.place(x=700, y=105)

add_image_s6 = ImageTk.PhotoImage(Image.open("images/harvest.png").resize((100, 100), Image.ANTIALIAS))
btn_6 = customtkinter.CTkButton(master=root, image=add_image_s6, text="Crop Guide", width=220,
                                        height=80,
                                        compound=TOP, command=get_guidance_window,border_color='black', border_width=3)
btn_6.place(x=450, y=240)

add_image_s7 = ImageTk.PhotoImage(Image.open("images/harvest.png").resize((100, 100), Image.ANTIALIAS))
btn_7 = customtkinter.CTkButton(master=root, image=add_image_s6, text="Sell your crops", width=220,
                                        height=80,
                                        compound=TOP, command=get_guidance_sellcrop,border_color='black', border_width=3)
btn_7.place(x=700, y=240)


add_image_s8 = ImageTk.PhotoImage(Image.open("images/harvest.png").resize((100, 100), Image.ANTIALIAS))
btn_8 = customtkinter.CTkButton(master=root, image=add_image_s6, text="buy crops and vegetables", width=220,
                                        height=80,
                                        compound=TOP, command=get_guidance_buycrop,border_color='black', border_width=3)
btn_8.place(x=450, y=375)

root.mainloop()
