# # import required modules
# #{'coord': {'lon': 72.8479, 'lat': 19.0144}, 'weather': [{'id': 711, 'main': 'Smoke', 'description': 'smoke', 'icon': '50d'}], 'base': 'stations',
# # 'main': {'temp': 309.14, 'feels_like': 307.81, 'temp_min': 305.09, 'temp_max': 309.14, 'pressure': 1013, 'humidity': 23}, 'visibility': 2500,
# # 'wind': {'speed': 4.12, 'deg': 260}, 'clouds': {'all': 0}, 'dt': 1677924121, 'sys': {'type': 1, 'id': 9052, 'country': 'IN', 'sunrise': 1677893177, 'sunset': 1677935699},
# # 'timezone': 19800, 'id': 1275339, 'name': 'Mumbai', 'cod': 200}
# import requests, json
#
# # Enter your API key here
# api_key = "b5765b346a0d53eae55bb58181ee09b4"
#
# # base_url variable to store url
# base_url = "http://api.openweathermap.org/data/2.5/weather?"
#
# # Give city name
# city_name = input("Enter city name : ")
#
# # complete_url variable to store
# # complete url address
# complete_url = base_url + "appid=" + api_key + "&q=" + city_name
#
# # get method of requests module
# # return response object
# response = requests.get(complete_url)
#
# # json method of response object
# # convert json format data into
# # python format data
# x = response.json()
# print(x)
# # Now x contains list of nested dictionaries
# # Check the value of "cod" key is equal to
# # "404", means city is found otherwise,
# # city is not found
# if x["cod"] != "404":
#
# 	# store the value of "main"
# 	# key in variable y
# 	y = x["main"]
#
# 	# store the value corresponding
# 	# to the "temp" key of y
# 	current_temperature = y["temp"]
#
# 	# store the value corresponding
# 	# to the "pressure" key of y
# 	current_pressure = y["pressure"]
#
# 	# store the value corresponding
# 	# to the "humidity" key of y
# 	current_humidity = y["humidity"]
#
# 	# store the value of "weather"
# 	# key in variable z
# 	z = x["weather"]
#
# 	# store the value corresponding
# 	# to the "description" key at
# 	# the 0th index of z
# 	weather_description = z[0]["description"]
#
# 	# print following values
# 	print(" Temperature (in kelvin unit) = " +
# 					str(current_temperature) +
# 		"\n atmospheric pressure (in hPa unit) = " +
# 					str(current_pressure) +
# 		"\n humidity (in percentage) = " +
# 					str(current_humidity) +
# 		"\n description = " +
# 					str(weather_description))
#
# else:
# 	print(" City Not Found ")
from tkinter import *
import customtkinter
from PIL import Image,ImageTk
import tkinter as tk
import webbrowser
from tkinter import *
from PIL import Image,ImageTk

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
# Define a function to be executed when the home button is clicked

class garlic_info:
    def __init__(self,root):
      self.root=root
      self.root.title("Government Schemes")
      self.root.geometry("750x550")


      image = Image.open("images/grant.png")

      # Convert the image to a Tkinter-compatible photo image
      self.tk_image = ImageTk.PhotoImage(image.resize((100, 100), Image.ANTIALIAS))

      # Create a label to display the image
      image_label = tk.Label(root, image=self.tk_image, anchor=NW)
      image_label.grid(row=0, column=0, sticky=NW, padx=20, pady=10)

      tlabel = Label(root, text="Schemes and Magazines", font=("Arial", 30, "bold"))
      tlabel.grid(row=0, column=1)

      # Add the label to the windor (100)w
      # image_label.pack(side=LEFT,padx=10)

      self.add_image_s1 = ImageTk.PhotoImage(Image.open("images/magazine.png").resize((60, 60), Image.ANTIALIAS))
      self.add_image_s2 = ImageTk.PhotoImage(Image.open("images/newspaper.png").resize((60, 60), Image.ANTIALIAS))
      self.add_image_s3 = ImageTk.PhotoImage(Image.open("images/wheat.png").resize((60, 60), Image.ANTIALIAS))

      btn_1 = customtkinter.CTkButton(master=self.root, image=self.add_image_s1, text="Click Me!", width=190, height=40,
                                      compound=TOP, command=S1, border_color='black', border_width=2)
      btn_1.place(x=160, y=100)
      btn_2 = customtkinter.CTkButton(master=self.root, image=self.add_image_s2, text="Click Me!", width=190, height=40,
                                      compound=TOP, command=S2, border_color='black', border_width=2)
      btn_2.place(x=380, y=100)
      btn_3 = customtkinter.CTkButton(master=self.root, image=self.add_image_s3, text="Click Me!", width=190, height=40,
                                      compound=TOP, command=S3, border_color='black', border_width=2)
      btn_3.place(x=160, y=220)
      btn_4 = customtkinter.CTkButton(master=self.root, image=self.add_image_s1, text="Click Me!", width=190, height=40,
                                      compound=TOP, command=S4, border_color='black', border_width=2)
      btn_4.place(x=380, y=220)
      btn_5 = customtkinter.CTkButton(master=self.root, image=self.add_image_s2, text="Click Me!", width=190, height=40,
                                      compound=TOP, command=S5, border_color='black', border_width=2)
      btn_5.place(x=160, y=330)
      btn_6 = customtkinter.CTkButton(master=self.root, image=self.add_image_s3, text="Click Me!", width=190, height=40,
                                      compound=TOP, command=S6, border_color='black', border_width=2)
      btn_6.place(x=380, y=330)

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
      self.photo_image = ImageTk.PhotoImage(image)

      # Create a button with the PhotoImage object
      button = Button(root, image=self.photo_image, bd=0, highlightthickness=0)
      button.place(x=650, y=20)


if __name__=="__main__":
    root = Tk()
    obj=garlic_info(root)
    root.mainloop()