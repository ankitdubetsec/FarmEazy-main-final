from tkinter import *
from PIL import Image,ImageTk

class mango_info:
    def __init__(self,root):
      self.root=root
      self.root.title("MANGO")
      self.root.geometry("1000x650+0+0")
      self.root.config(bg = "orange")

      img1=Image.open("images/image/mangoin.jpg")
      img1=img1.resize((420,500),Image.ANTIALIAS)
      self.photoimg1=ImageTk.PhotoImage(img1)

      lbl=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE,bg="green")
      lbl.place(x=300,y=100,width=500,height=550)

      img2=Image.open("images/image/mango.jpg")
      img2=img2.resize((250,230),Image.ANTIALIAS)
      self.photoimg2=ImageTk.PhotoImage(img2)

      lbl=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
      lbl.place(x=25,y=125,width=250,height=230)


if __name__=="__main__":
    root = Tk()
    obj=mango_info(root)
    root.mainloop()
