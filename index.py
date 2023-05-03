import tkinter as tk
from PIL import ImageTk, Image
import pandas as pd
from tkinter import StringVar,ttk,Button
import csv


# Create the main window
root=tk.Tk()
root.title("Seed Calculator")

# Set the window size and position
root.geometry("1000x500")
# root.minsize(100,100)
# root.maxsize(800,800)
root.configure(background='white')

df = pd.read_csv("CsvFiles/data.csv")

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
    seed_kg_per_hectare = float(df.loc[input_crop]['Seed Kg/Hect.'])
    x.set(str('%.2f' % (seed_kg_per_hectare*(area/ 2.471))))


# Load the background image
bg_image = Image.open("images/farmer2.jpg")
bg_image = bg_image.resize((1500, 1200), Image.ANTIALIAS)
bg_image = ImageTk.PhotoImage(bg_image)

# Create a Label widget to hold the background image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the login form
frame = tk.Frame(root, bg="white")
frame.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.5, anchor="center")

# Create labels and entry widgets for username and password
area_label = tk.Label(frame, text="Area:", bg="white" ,font=("Helvetica", 15))
area_label.place(relx=0.1, rely=0.3, relheight=0.1)

area_entry = ttk.Entry(frame,textvariable="enter area in acres")
area_entry.place(relx=0.3, rely=0.3, relwidth=0.5, relheight=0.1)

crop_label = tk.Label(frame, text="crop:", bg="white",font=("Helvetica", 15))
crop_label.place(relx=0.1, rely=0.5, relheight=0.1)

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
button.place(x=900,y=20)
# crop_entry = ttk.Entry(frame,)
# crop_entry.place(relx=0.3, rely=0.5, relwidth=0.5, relheight=0.1)
options = []
with open('CsvFiles/data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        options.append(row[1]) # assuming the desired column is the first one

selected_option = tk.StringVar()
selected_option.set(options[0])

dropdown = ttk.OptionMenu(frame, selected_option, *options)
dropdown.place(relx=0.3, rely=0.5, relwidth=0.5, relheight=0.1)

# crop_entry.insert(0, "Enter name of the crop")


# Create the login button
calculate_btn = tk.Button(frame, text="Calculate", bg="red", fg="white",command=cal )
calculate_btn.place(relx=0.5, rely=0.7, relwidth=0.3, relheight=0.1, anchor="center")

# display = tk.Entry(frame, width=20, font=('Arial', 16))
# display.grid(row=0, column=0, columnspan=4)
x = StringVar()
# display_label=ttk.Label(frame,textvariable=x)
# display_label.grid(row=3,column=1,padx=5, pady=5)
display_label = tk.Label(frame, text="Quantity of seeds: ", bg="white",font=("Helvetica", 10))
display_label.place(relx=0.1, rely=0.85, relheight=0.1)

quantity_label = tk.Label(frame, textvariable=x, bg="white",font=("Helvetica", 15))
quantity_label.place(relx=0.4, rely=0.85, relheight=0.1)
style = ttk.Style()
style.configure("TEntry", font=("Helvetica", 12),padx=5,pady=5)
style.configure("TOptionMenu", font=("Helvetica", 12),padx=5,pady=5)
# Run the main loop
root.mainloop()
