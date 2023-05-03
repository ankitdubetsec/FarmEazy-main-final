import tkinter as tk
from PIL import ImageTk, Image
import pandas as pd
from tkinter import GROOVE, Button, Entry, Label, LabelFrame, PhotoImage, StringVar,ttk
import csv

root=tk.Tk()
root.title("fertilizer calculator")

# Set the window size and position
root.geometry("400x300")
# root.minsize(100,100)
# root.maxsize(800,800)
root.configure(background='white')


bg_image = Image.open("./ttkinter2/farmer4.jpg")
bg_image = bg_image.resize((1400, 1200))
bg_image = ImageTk.PhotoImage(bg_image)

# Create a Label widget to hold the background image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


def go_home():
    root.destroy()
    import newDashboard7
def add_to_csv():
    # Get the user input from the entry boxes
    location =location_txt.get()
    name = name_txt.get()
    crop =crop_txt.get()
    variety =variety_txt.get()
    quantity =quantity_txt.get()
    msp =msp_txt.get()
    mobile=mobile_txt.get()

    


    # Create a dictionary with the input data
    data = {"Location": [location], "Name": [name], "Crop": [crop],"Variety": [variety],"Quantity": [quantity],"Msp": [msp],"Mobile":[mobile]}
    df = pd.DataFrame(data)
    # Create a DataFrame from the dictionary
   

    # Write the DataFrame to a CSV file
    df.to_csv("x.csv", mode="a", index=False, header=not bool(pd.read_csv("x.csv").shape[0]))
    
    # Clear the entry boxes
    location_txt.delete(0, tk.END)
    name_txt.delete(0, tk.END)
    crop_txt.delete(0, tk.END)
    variety_txt.delete(0, tk.END)
    quantity_txt.delete(0, tk.END)
    msp_txt.delete(0, tk.END)
    mobile_txt.delete(0, tk.END)
nav_frame = tk.Frame(root, bg="#badc57")
nav_frame.place(relx=0,rely=0,relwidth=1,relheight=0.08)

title_label = tk.Label(nav_frame, text="FarmEazy", bg="#badc57", fg="black", padx=10,font=("Helvetica", 15,"bold"))
title_label.pack(side="left")

# Create a frame for the buttons on the right
button_frame = tk.Frame(nav_frame, bg="#badc57")
button_frame.pack(side="right")

# Create three buttons
button1 = tk.Button(button_frame, text="Home", bg="#badc57", fg="black", padx=10, borderwidth=0, highlightthickness=0,font=("Helvetica", 11,"bold"),command=go_home)
button1.pack(side="right", padx=10)

button2 = tk.Button(button_frame, text="Log Out", bg="#badc57", fg="black", padx=10, borderwidth=0, highlightthickness=0,font=("Helvetica", 11,"bold"))
button2.pack(side="right", padx=10)

button3 = tk.Button(button_frame, text="About us", bg="#badc57", fg="black", padx=10, borderwidth=0, highlightthickness=0,font=("Helvetica", 11,"bold"))
button3.pack(side="right", padx=10)

F3 = LabelFrame(root, text="SELL YOUR CROPS", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57",padx=10,pady=10)
F3.place(x=340, y=180, width=625, height=450)


location_lbl = Label(F3, text="Location", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
location_lbl.grid(row=1, column=6, padx=10, pady=10, sticky='W')
location_txt = Entry(F3, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
location_txt.grid(row=1, column=7, padx=10, pady=10)

name_lbl = Label(F3, text="Name", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
name_lbl.grid(row=2, column=6, padx=10, pady=10, sticky='W')
name_txt = Entry(F3, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
name_txt.grid(row=2, column=7, padx=10, pady=10)
crop_lbl = Label(F3, text="Crop", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
crop_lbl.grid(row=3, column=6, padx=10, pady=10, sticky='W')
crop_txt = Entry(F3, width=10,  font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
crop_txt.grid(row=3, column=7, padx=10, pady=10)

variety_lbl = Label(F3, text="Variety", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
variety_lbl.grid(row=4, column=6, padx=10, pady=10, sticky='W')
variety_txt = Entry(F3, width=10,  font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
variety_txt.grid(row=4, column=7, padx=10, pady=10)

quantity_lbl = Label(F3, text="Quantity(kg)", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
quantity_lbl.grid(row=5, column=6, padx=10, pady=10, sticky='W')
quantity_txt = Entry(F3, width=10,  font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
quantity_txt.grid(row=5, column=7, padx=10, pady=10)

msp_lbl = Label(F3, text="Msp", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
msp_lbl.grid(row=6, column=6, padx=10, pady=10, sticky='W')
msp_txt = Entry(F3, width=10,  font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
msp_txt.grid(row=6, column=7, padx=10, pady=10)

mobile_lbl = Label(F3, text="Mobile", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
mobile_lbl.grid(row=7, column=6, padx=10, pady=10, sticky='W')
mobile_txt = Entry(F3, width=10,  font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
mobile_txt.grid(row=7, column=7, padx=10, pady=10)

sell_btn = tk.Button(F3, text="Sell", bg="red", fg="white",command=add_to_csv,borderwidth=3 ,font=("Helvetica", 15))
sell_btn.place(relx=0.75, rely=0.4, relwidth=0.3, relheight=0.1, anchor="center")

update_btn = tk.Button(F3, text="Update", bg="red", fg="white",borderwidth=3 ,font=("Helvetica", 15))
update_btn.place(relx=0.75, rely=0.6, relwidth=0.3, relheight=0.1, anchor="center")

root.mainloop()