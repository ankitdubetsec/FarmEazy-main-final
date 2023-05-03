
import tkinter as tk
from PIL import ImageTk, Image
import pandas as pd
from tkinter import GROOVE, LabelFrame, PhotoImage, StringVar,ttk
import csv

root=tk.Tk()
root.title("fertilizer calculator")

# Set the window size and position
root.geometry("400x300")
# root.minsize(100,100)
# root.maxsize(800,800)
root.configure(background='white')

df = pd.read_csv("./ttkinter/npk.csv")

# cell_val = df.iloc[3][1]

# Set the "Crop" column as the index
df.set_index('Crop', inplace=True)

def go_home():
    root.destroy()
    import newDashboard4

def cal():
    area=float(area_entry.get())
    input_crop =selected_option.get()
    # Access the "Seed Kg/Hect" value for the input crop
    N = float(df.loc[input_crop]['N'])
    P = float(df.loc[input_crop]['P'])
    K = float(df.loc[input_crop]['K'])
    #FACTORS
    urea_factor=2.17
    ssp_factor=6.25
    mop_factor=1.67
    dap_n_factor=5.55
    dap_p_factor=2.17
    urea=N*2.17
    ssp=P*6.25
    mop=K*1.67

    x_urea = StringVar()
    x_ssp =StringVar()
    x_mop=StringVar()
 
    x_urea.set(str('%.2f' % (urea*(area/ 2.471))))
    x_ssp.set(str('%.2f' % (ssp*(area/ 2.471))))
    x_mop.set(str('%.2f' % (mop*(area/ 2.471))))

    

    firstbox = PhotoImage(file="ttkinter/rect1.png")
    quantity_label = tk.Label(frame, image=firstbox,bg="#203243",anchor="center")
    quantity_label.place(relx=0.32, rely=0.7)

    display_label1 = tk.Label(frame, text="UREA(kg): ", bg="#203243",font=("Helvetica", 15),fg="white")
    display_label1.place(relx=0.35, rely=0.71, relheight=0.05)

    display_label2 = tk.Label(frame, text="SSP(kg): ", bg="#203243",font=("Helvetica", 15),fg="white")
    display_label2.place(relx=0.35, rely=0.78, relheight=0.05)

    display_label3 = tk.Label(frame, text="Mop(kg): ", bg="#203243",font=("Helvetica", 15),fg="white")
    display_label3.place(relx=0.35, rely=0.85, relheight=0.05)

    display_label4 = tk.Label(frame, textvariable=x_urea, bg="#203243",font=("Helvetica", 14),fg="white")
    display_label4.place(relx=0.53, rely=0.71, relheight=0.05)

    display_label4 = tk.Label(frame, textvariable=x_ssp, bg="#203243",font=("Helvetica", 14),fg="white")
    display_label4.place(relx=0.51, rely=0.78, relheight=0.05)

    display_label4 = tk.Label(frame, textvariable=x_ssp, bg="#203243",font=("Helvetica", 14),fg="white")
    display_label4.place(relx=0.51, rely=0.86, relheight=0.05)

bg_image = Image.open("./ttkinter/farmer4.jpg")
bg_image = bg_image.resize((1400, 1200))
bg_image = ImageTk.PhotoImage(bg_image)

# Create a Label widget to hold the background image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
nav_frame = tk.Frame(root, bg="#badc57")
nav_frame.place(relx=0,rely=0,relwidth=1,relheight=0.08)

# Create a label for the title on the left corner
title_label = tk.Label(nav_frame, text="Farm Eazy", bg="#badc57", fg="black", padx=10,font='Helvetica 18 bold')
title_label.pack(side="left")

# Create a frame for the buttons on the right
button_frame = tk.Frame(nav_frame, bg="#badc57")
button_frame.pack(side="right")

# Create three buttons
button1 = tk.Button(button_frame, text="Home", bg="#badc57", fg="black", padx=10, borderwidth=0, highlightthickness=0,font='Helvetica 14 bold',command=go_home)
button1.pack(side="right", padx=10)

button2 = tk.Button(button_frame, text="Log Out", bg="#badc57", fg="black", padx=10, borderwidth=0, highlightthickness=0,font='Helvetica 14 bold')
button2.pack(side="right", padx=10)

button3 = tk.Button(button_frame, text="About us", bg="#badc57", fg="black", padx=10, borderwidth=0, highlightthickness=0,font='Helvetica 14 bold')
button3.pack(side="right", padx=10)

# Create the login form
frame = tk.LabelFrame(root, font=('times new roman', 15, 'bold'), bd=10, borderwidth=5,fg="Black", bg="#badc57",padx=10,pady=10)
frame.place(relx=0.3, rely=0.55, relwidth=0.4, relheight=0.75, anchor="center")
frame.configure(borderwidth=3,bd=10)
# root.attributes('-alpha', 0.5)

# F1 = LabelFrame(frame, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
# F1.place(x=0, y=80, relwidth=100)
# Create labels and entry widgets for username and password
area_label = tk.Label(frame, text="Area(acres)", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
area_label.place(relx=0.08, rely=0.2, relheight=0.1)

area_entry = tk.Entry(frame,textvariable="enter area in acres",font='Helvetica 18 bold',borderwidth=3)
area_entry.place(relx=0.3, rely=0.2, relwidth=0.5, relheight=0.1)



crop_label = tk.Label(frame, text="crop:", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
crop_label.place(relx=0.1, rely=0.4, relheight=0.1)

# crop_entry = ttk.Entry(frame)
# crop_entry.place(relx=0.3, rely=0.5, relwidth=0.5, relheight=0.1)
options = []
with open('./ttkinter/npk.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        options.append(row[0]) # assuming the desired column is the first one

selected_option = tk.StringVar()
selected_option.set(options[0])

dropdown = tk.OptionMenu(frame,selected_option, *options)
dropdown.place(relx=0.3, rely=0.4, relwidth=0.5, relheight=0.1)
dropdown.configure(borderwidth=3)
calculate_btn = tk.Button(frame, text="Calculate", bg="red", fg="white",command=cal,borderwidth=3 ,font=("Helvetica", 15))
calculate_btn.place(relx=0.5, rely=0.6, relwidth=0.3, relheight=0.1, anchor="center")

# rice_txt = ttk.Entry(frame, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
# rice_txt.grid(row=0, column=1, padx=10, pady=10)

# display = tk.Entry(frame, width=20, font=('Arial', 16))
# display.grid(row=0, column=0, columnspan=4)

# display_label=ttk.Label(frame,textvariable=x)
# display_label.grid(row=3,column=1,padx=5, pady=5)


# display_label = tk.Label(frame, text="Quantity of seeds: ", bg="white",font=("Helvetica", 15),)
# display_label.place(relx=0.1, rely=0.75, relheight=0.1)


# style = ttk.Style()
# style.configure("Toptions", font='Helvetica 18 bold',padx=15,pady=15,bg="brown",insertborderwidth=5)
# style.configure("TOptionMenu", font='Helvetica 18 bold',padx=5,pady=5)
root.mainloop()