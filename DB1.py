from tkinter import *
from PIL import Image,ImageTk;
import datetime
now=datetime.datetime.now


class DashBoard:
        def __init__(self,root):
            self.root=root
            self.root.geometry("1350x700+0+0")
            self.root.title("FarmEazy: Farmer's Friend")
            self.root.config(bg="white")

            img1=Image.open(r"FanoRama.png")
            img1 = img1.resize((1550,680),Image.LANCZOS)
            self.photoimg1=ImageTk.PhotoImage(img1)

            lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
            lblimg.place(x=0,y=0,width=1550,height=680)
            
            self.icon_title=PhotoImage(file="Logo_OG.png")
            title=Label(self.root,text="FarmEazy: Farmer's Friend",image=self.icon_title,compound=LEFT,font=("Times New Roman",40,"bold"),bg="#010c48",fg="gold",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
            
            btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1100,y=10,height=50,width=150)
            
            self.lbl_clock=Label(self.root,text=f"Welcome to FarmEazy\t\t Login Date:{str(now().date())} \t\t Login Time:{str(now().time())}",font=("Times New Roman",15,"bold"),bg="#4d636d",fg="white")
            self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
            

            self.MenuLogo=Image.open(r"Govt_03.png")
            self.MenuLogo=self.MenuLogo.resize((180,180),Image.LANCZOS)
            self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        
            LeftMenu=Frame(self.root,bd=2,relief=RIDGE)
            LeftMenu.place(x=0,y=102,width=200,height=565)

            lbl_MenuLogo=Label(LeftMenu,image=self.MenuLogo)
            lbl_MenuLogo.pack(side=TOP,fill=X)

            self.AnotherLogo = Image.open(r"AnnaData.png")
            self.AnotherLogo = self.AnotherLogo.resize((180, 180), Image.LANCZOS)
            self.AnotherLogo = ImageTk.PhotoImage(self.AnotherLogo)

            lbl_AnotherLogo = Label(LeftMenu, image=self.AnotherLogo)
            lbl_AnotherLogo.pack(side=TOP, fill=X)

            self.ThirdLogo = Image.open(r"BaliRaja.png")
            self.ThirdLogo = self.ThirdLogo.resize((180,180), Image.LANCZOS)
            self.ThirdLogo = ImageTk.PhotoImage(self.ThirdLogo)

            lbl_ThirdLogo = Label(LeftMenu,image=self.ThirdLogo)
            lbl_ThirdLogo.pack(side=TOP, fill=X)

            lbl_footer=Label(self.root,text="FarmEazy: Farmer's Friend | Copyright: Group_07",font=("times new roman",15),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
            
            # CropPrices = Image.open("CropPrices.png")
            # CropPrices = CropPrices.resize((300, 150), Image.LANCZOS)
            # CropPrices = ImageTk.PhotoImage(CropPrices)
            
            btn_CropPrices=Button(self.root,text="Crop_Prices",bd=5,relief=RIDGE,bg="yellow",cursor="hand2",fg="black")
            btn_CropPrices.place(x=280,y=120,height=150,width=300)


            # lbl_CropPrices = Label(self.root, text="Check the latest prices of various crops")
            # lbl_CropPrices.place(x=280,y=270, height=50)
            
            btn_CropRecommendation=Button(self.root,text="Crop_Recommendation",bd=5,relief=RIDGE,bg="yellow",cursor="hand2",fg="black")
            btn_CropRecommendation.place(x=620,y=120,height=150,width=300)

            btn_GovernmentSchemes=Button(self.root,text="Government_Schemes",bd=5,relief=RIDGE,bg="yellow",cursor="hand2",fg="black")
            btn_GovernmentSchemes.place(x=280,y=290,height=150,width=300)

            btn_WeatherForecast=Button(self.root,text="Weather_Forecast",bd=5,relief=RIDGE,bg="yellow",cursor="hand2",fg="black")
            btn_WeatherForecast.place(x=620,y=290,height=150,width=300)

            btn_Fertilizers=Button(self.root,text="Fertilizers",bd=5,relief=RIDGE,bg="yellow",cursor="hand2",fg="black")
            btn_Fertilizers.place(x=280,y=460,height=150,width=300)

            btn_SeedRequirements=Button(self.root,text="Seed_Requirements",bd=5,relief=RIDGE,bg="yellow",cursor="hand2",fg="black")
            btn_SeedRequirements.place(x=620,y=460,height=150,width=300)

            btn_BuyCrops=Button(self.root,text="Buy_From_Farms",bd=5,relief=RIDGE,bg="yellow",cursor="hand2",fg="black")
            btn_BuyCrops.place(x=960,y=120,height=150,width=300)


root=Tk()
obj=DashBoard(root)
root.mainloop()
