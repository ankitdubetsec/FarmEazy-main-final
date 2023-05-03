from tkinter import *
import customtkinter
from PIL import Image,ImageTk
import tkinter as tk
import webbrowser


def S1():
    webbrowser.open('https://drive.google.com/file/d/1yiU4XgDxtYWh-Jx1yYb6cs5ymNbgOnH8/view?usp=share_link')
def S2():
    webbrowser.open('https://drive.google.com/file/d/1g_zLROiBhY5lYogxp2GvTOWrlftwxaWj/view?usp=share_link')
def S3():
    webbrowser.open('https://drive.google.com/file/d/1g6Hy6nxks3gPIKu9WxD4wAyUEWgc9sJz/view?usp=share_link')

def S4():
    webbrowser.open('https://drive.google.com/file/d/1HwacMFEcQZLSOLkLR_4uRLsUJn6cBStJ/view?usp=share_link')

def S5():
    webbrowser.open('https://drive.google.com/file/d/1-FCxs_sJWvm6gXrypcjTutnZHZUpFIkT/view?usp=share_link')

def S6():
    webbrowser.open('https://drive.google.com/file/d/1wlaVvl2tZW12NCAw-JaB9LmkQoItXNit/view?usp=share_link')

def go_home():
    root.destroy()
    import newDashboard

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.title("Government Schemes")
root.geometry("600x400")
root.configure(bg='gold')
image = Image.open("images/grant.png")

# Convert the image to a Tkinter-compatible photo image
tk_image = ImageTk.PhotoImage(image.resize((100,100),Image.ANTIALIAS))

# Create a label to display the image
image_label = tk.Label(root, image=tk_image,anchor=NW)
image_label.grid(row=0,column=0,sticky=NW,padx=20,pady=10)

tlabel = Label(root,text="Schemes and Magazines", font=("Arial", 30,"bold"))
tlabel.grid(row=0,column=1)


# Add the label to the windor (100)w
# image_label.pack(side=LEFT,padx=10)

add_image_s1 = ImageTk.PhotoImage(Image.open("images/magazine.png").resize((60,60),Image.ANTIALIAS))
add_image_s2 = ImageTk.PhotoImage(Image.open("images/newspaper.png").resize((60,60),Image.ANTIALIAS))
add_image_s3 = ImageTk.PhotoImage(Image.open("images/wheat.png").resize((60,60),Image.ANTIALIAS))

btn_1 = customtkinter.CTkButton(master=root,image=add_image_s1,text="Click Me!",width=190,height=40,compound=TOP,command=S1,border_color='black',border_width=2)
btn_1.place(x=140,y=90)
btn_2 = customtkinter.CTkButton(master=root,image=add_image_s2,text="Click Me!",width=190,height=40,compound=TOP,command=S2,border_color='black',border_width=2)
btn_2.place(x=340,y=90)
btn_3 = customtkinter.CTkButton(master=root,image=add_image_s3,text="Click Me!",width=190,height=40,compound=TOP,command=S3,border_color='black',border_width=2)
btn_3.place(x=140,y=180)
btn_4 = customtkinter.CTkButton(master=root,image=add_image_s1,text="Click Me!",width=190,height=40,compound=TOP,command=S4,border_color='black',border_width=2)
btn_4.place(x=340,y=180)
btn_5 = customtkinter.CTkButton(master=root,image=add_image_s2,text="Click Me!",width=190,height=40,compound=TOP,command=S5,border_color='black',border_width=2)
btn_5.place(x=140,y=270)
btn_6 = customtkinter.CTkButton(master=root,image=add_image_s3,text="Click Me!",width=190,height=40,compound=TOP,command=S6,border_color='black',border_width=2)
btn_6.place(x=340,y=270)

# Load the image
image = Image.open("images/eco-home.png")

# Remove the background
image = image.convert("RGBA")
data = image.getdata()
new_data = []
for item in data:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)
image.putdata(new_data)

# Create a PhotoImage object with transparent background
photo_image = ImageTk.PhotoImage(image)

# Create a button with the PhotoImage object
button = Button(root, image=photo_image, bd=0, highlightthickness=0,command=go_home)
button.place(x=650,y=20)



root.mainloop()

