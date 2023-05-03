# # import requests
# # from bs4 import BeautifulSoup
# # url = "https://www.msamb.com/ApmcDetail/APMCPriceInformation"
# #
# # from selenium import webdriver
# # import time
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import Select
# # # create webdriver object
# # driver = webdriver.Chrome()
# #
# # # get geeksforgeeks.org
# # driver.get("https://www.msamb.com/ApmcDetail/APMCPriceInformation")
# # # time.sleep(2)
# #
# # selectlang = driver.find_element(By.XPATH,'//*[@id="language"]')
# # drp1 =Select(selectlang)
# # drp1.select_by_visible_text('English')
# #
# # time.sleep(2)
# # # drp1.select_by_index(1)
# # # get element
# # element = driver.find_element(By.XPATH,'//*[@id="drpCommodities"]')
# # drp = Select(element)
# # # drp.select_by_visible_text('Apple')
# # drp.select_by_index(3)
# #
# #
# # # time.sleep(10)
# # # send keys
# # # element.send_keys("Apple")
# #
# # r = requests.get(url)
# # htmlContent = r.content
# # # print(htmlContent)
# #
# # soup = BeautifulSoup(htmlContent,'html.parser')
# # # print(soup)
# #
# # title = soup.title
# # # print(title)
# # paras = soup.findAll('table')
# # print(paras)
# #
# #
# import tkinter as tk
#
#
# class Page1(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#
#         # Create widgets for page 1
#         label = tk.Label(self, text="Page 1")
#         label.pack(pady=10, padx=10)
#
#         button = tk.Button(self, text="Go to Page 2", command=lambda: controller.show_page(Page2))
#         button.pack()
#
#
# class Page2(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#
#         # Create widgets for page 2
#         label = tk.Label(self, text="Page 2")
#         label.pack(pady=10, padx=10)
#
#         button = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_page(Page1))
#         button.pack()
#
#
# class MainApplication(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#
#         # Create a container to hold the frames
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#
#         # Create a dictionary to hold the frames
#         self.frames = {}
#
#         # Create instances of the frames and add to dictionary
#         for F in (Page1, Page2):
#             frame = F(container, self)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
#
#         # Show the first frame
#         self.show_page(Page1)
#
#     def show_page(self, cont):
#         """Show the frame for the given class."""
#         frame = self.frames[cont]
#         frame.tkraise()
#
#
# app = MainApplication()
# app.mainloop()
#
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# import tkinter as tk
# from tkinter import ttk
# from tkinter import *

#
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         # Creating a PyQT button
#         pyqt_button = QPushButton('PyQT Button', self)
#         pyqt_button.move(50, 50)
#
#         # Creating a Tkinter button
#         root = tk.Tk()
#         root.withdraw()
#         tkinter_button = ttk.Button(root, text='Tkinter Button')
#         tkinter_button_window = self.createWindowContainer(root.winfo_toplevel())
#         tkinter_button_window.setGeometry(QRect(100, 100, 120, 30))
#
#         # Connecting the PyQT button to a function
#         pyqt_button.clicked.connect(self.on_pyqt_button_clicked)
#
#         # Creating the PyQT window
#         self.setGeometry(300, 300, 400, 300)
#         self.setWindowTitle('PyQT-Tkinter Example')
#         self.show()
#
#     def on_pyqt_button_clicked(self):
#         print('PyQT button clicked')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main_window = MainWindow()
#     sys.exit(app.exec_())
import json
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
import urllib.request
import sys




def go_home():
    weather.destroy()
    import myDashboard1


def currWeatherIcon(location):
    currtime = datetime.now()
    currhour = currtime.hour
    try:
        ResultBytes = urllib.request.urlopen(
            "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/" + location + "?unitGroup=us&include=alerts%2Chours%2Cdays%2Ccurrent&key=GUGUVPE393UQGQWTFKA5RE7G2&contentType=json")

        # Parse the results as JSON
        jsonData = json.load(ResultBytes)
        curricon = jsonData['days'][0]['hours'][currhour]['icon']
        return curricon

    except urllib.error.HTTPError as e:
        ErrorInfo = e.read().decode()
        print('Error code: ', e.code, ErrorInfo)

    except  urllib.error.URLError as e:
        ErrorInfo = e.read().decode()
        print('Error code: ', e.code, ErrorInfo)


class weatherApp:

    def __init__(self,weather):
        self.weather=weather
        self.weather.title("Weather App")
        self.weather.geometry("890x470+300+200")
        self.weather.configure(bg="#57adff")
        self.weather.resizable(False, False)

        ##icon
        self.image_icon = PhotoImage(file="images/weatherlogo.png")
        self.weather.iconphoto(False, self.image_icon)

        self.Round_box = PhotoImage(file="images/Rounded Rectangle 1.png")
        Label(self.weather, image=self.Round_box, bg="#57adff").place(x=30, y=110)

        label1 = Label(self.weather, text="Temperature", font=("Helvetica", 11), fg='white', bg="#203243")
        label1.place(x=50, y=120)
        label2 = Label(self.weather, text="Humidity", font=("Helvetica", 11), fg='white', bg="#203243")
        label2.place(x=50, y=140)
        label3 = Label(self.weather, text="Pressure", font=("Helvetica", 11), fg='white', bg="#203243")
        label3.place(x=50, y=160)
        label4 = Label(self.weather, text="Wind Speed", font=("Helvetica", 11), fg='white', bg="#203243")
        label4.place(x=50, y=180)
        label5 = Label(self.weather, text="Description", font=("Helvetica", 11), fg='white', bg="#203243")
        label5.place(x=50, y=200)

        # search box
        self.Search_image = PhotoImage(file="images/longrec4.png")
        myimage = Label(image=self.Search_image, bg="#57adff")
        myimage.place(x=270, y=80)

        self.weat_image = PhotoImage(file='images/sun.png')
        weatherimage = Label(self.weather, image=self.weat_image, bg="#203243", border=0)
        weatherimage.place(x=308, y=137)

        self.textfield = tk.Entry(self.weather, justify='center', width=15, font=('poppins', 25, 'bold'), bg="black", border=0,
                             fg="white")
        self.textfield.place(x=370, y=150)
        self.textfield.focus()

        self.Search_icon = PhotoImage(file="images/searchicon.png")
        myimage_icon = Button(image=self.Search_icon, borderwidth=0, cursor="hand2", bg="black", activebackground="black",
                              command=self.getWeather)
        myimage_icon.place(x=700, y=145)

        # Bottom Box
        weatherframe = Frame(self.weather, width=900, height=180, bg='#212120')
        weatherframe.pack(side=BOTTOM)

        # bottom boxes
        self.firstbox = PhotoImage(file="images/Rounded Rectangle 2.png")
        self.secondbox = PhotoImage(file="images/Rounded Rectangle 2 copy.png")

        Label(weatherframe, image=self.firstbox, bg="#212120").place(x=30, y=20)
        Label(weatherframe, image=self.secondbox, bg='#212120').place(x=300, y=30)
        Label(weatherframe, image=self.secondbox, bg='#212120').place(x=400, y=30)
        Label(weatherframe, image=self.secondbox, bg='#212120').place(x=500, y=30)
        Label(weatherframe, image=self.secondbox, bg='#212120').place(x=600, y=30)
        Label(weatherframe, image=self.secondbox, bg='#212120').place(x=700, y=30)
        Label(weatherframe, image=self.secondbox, bg='#212120').place(x=800, y=30)

        # clock
        self.clock = Label(self.weather, font=("Helvetica", 30, 'bold'), fg="white", bg='#57adff')
        self.clock.place(x=30, y=20)

        # timezone
        self.timezone = Label(self.weather, font=("Helvetica", 20), fg="white", bg='#57adff')
        self.timezone.place(x=700, y=20)

        self.long_lat = Label(self.weather, font=("Helvetica", 10), fg="white", bg='#57adff')
        self.long_lat.place(x=700, y=50)

        self.t = Label(self.weather, font=('Helvetica', 11), fg='white', bg="#203243")
        self.t.place(x=150, y=120)
        self.h = Label(self.weather, font=('Helvetica', 11), fg='white', bg="#203243")
        self.h.place(x=150, y=140)
        self.p = Label(self.weather, font=('Helvetica', 11), fg='white', bg="#203243")
        self.p.place(x=150, y=160)
        self.w = Label(self.weather, font=('Helvetica', 11), fg='white', bg="#203243")
        self.w.place(x=150, y=180)
        self.d = Label(self.weather, font=('Helvetica', 11), fg='white', bg="#203243")
        self.d.place(x=150, y=200)

        firstframe = Frame(self.weather, width=230, height=132, bg='#282829')
        firstframe.place(x=35, y=315)
        self.day1 = Label(firstframe, font="arial 20", bg='#282829', fg="#fff")
        self.day1.place(x=100, y=5)
        self.firstimage = Label(firstframe, bg="#282829")
        self.firstimage.place(x=1, y=15)
        self.day1temp = Label(firstframe, bg="#282829", fg="#57adff", font='arial 15 bold')
        self.day1temp.place(x=80, y=50)

        secondframe = Frame(self.weather, width=70, height=115, bg='#282829')
        secondframe.place(x=305, y=325)
        self.day2 = Label(secondframe, bg='#282829', fg="#fff")
        self.day2.place(x=10, y=5)
        self.secondimage = Label(secondframe, bg='#282829')
        self.secondimage.place(x=7, y=20)
        self.day2temp = Label(secondframe, bg='#282829', fg='#fff')
        self.day2temp.place(x=0, y=70)

        thirdframe = Frame(self.weather, width=70, height=115, bg='#282829')
        thirdframe.place(x=405, y=325)
        self.day3 = Label(thirdframe, bg='#282829', fg="#fff")
        self.day3.place(x=10, y=5)
        self.thirdimage = Label(thirdframe, bg='#282829')
        self.thirdimage.place(x=7, y=20)
        self.day3temp = Label(thirdframe, bg='#282829', fg='#fff')
        self.day3temp.place(x=0, y=70)

        fourthframe = Frame(self.weather, width=70, height=115, bg='#282829')
        fourthframe.place(x=505, y=325)
        self.day4 = Label(fourthframe, bg='#282829', fg="#fff")
        self.day4.place(x=10, y=5)
        self.fourthimage = Label(fourthframe, bg='#282829')
        self.fourthimage.place(x=7, y=20)
        self.day4temp = Label(fourthframe, bg='#282829', fg='#fff')
        self.day4temp.place(x=0, y=70)

        fifthframe = Frame(self.weather, width=70, height=115, bg='#282829')
        fifthframe.place(x=605, y=325)
        self.day5 = Label(fifthframe, bg='#282829', fg="#fff")
        self.day5.place(x=10, y=5)
        self.fifthimage = Label(fifthframe, bg='#282829')
        self.fifthimage.place(x=7, y=20)
        self.day5temp = Label(fifthframe, bg='#282829', fg='#fff')
        self.day5temp.place(x=0, y=70)

        sixthframe = Frame(self.weather, width=70, height=115, bg='#282829')
        sixthframe.place(x=705, y=325)
        self.day6 = Label(sixthframe, bg='#282829', fg="#fff")
        self.day6.place(x=10, y=5)
        self.sixthimage = Label(sixthframe, bg='#282829')
        self.sixthimage.place(x=7, y=20)
        self.day6temp = Label(sixthframe, bg='#282829', fg='#fff')
        self.day6temp.place(x=0, y=70)

        seventhframe = Frame(self.weather, width=70, height=115, bg='#282829')
        seventhframe.place(x=805, y=325)
        self.day7 = Label(seventhframe, bg='#282829', fg="#fff")
        self.day7.place(x=10, y=5)
        self.seventhimage = Label(seventhframe, bg='#282829')
        self.seventhimage.place(x=7, y=20)
        self.day7temp = Label(seventhframe, bg='#282829', fg='#fff')
        self.day7temp.place(x=0, y=70)

        # Load the image
        image = Image.open("images/sun.png")

        # Remove the background
        image = image.convert("RGBA")
        data = image.getdata()
        new_data = []
        for item in data:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                # new_data.append((60,150,255,255))
                new_data.append((99, 164, 255, 255))
            else:
                new_data.append(item)
        image.putdata(new_data)

        # Create a PhotoImage object with transparent background
        self.photo_image = ImageTk.PhotoImage(image)

        # Create a button with the PhotoImage object
        button = Button(self.weather, image=self.photo_image, bd=0, highlightthickness=0, activebackground='Steelblue1',
                        command=go_home)
        button.place(x=840, y=60)

    def getWeather(self):
        city = self.textfield.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()

        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        self.timezone.config(text=result)
        self.long_lat.config(text=f"{round(location.latitude, 4)}°N,{round(location.longitude, 4)}°E")

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        self.clock.config(text=current_time)

        # weather
        api_key = "b5765b346a0d53eae55bb58181ee09b4"
        # API_KEY = "a38e8a9065e5a25cbc3f6a9316ddfa5c"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + city

        response = requests.get(complete_url)
        json_data = response.json()
        print(json_data)
        temp = round((json_data['main']['temp']) - 273.15, 0)
        humidity = json_data['main']['humidity']
        pressure = json_data['main']['pressure']
        wind = json_data['wind']['speed']
        description = json_data['weather'][0]['description']

        self.t.config(text=(temp, "°C"))
        self.h.config(text=(humidity, "%"))
        self.p.config(text=(pressure, "hPa"))
        self.w.config(text=(wind, "m/s"))
        self.d.config(text=description)

        # WEATHER FORECAST
        try:

            ResultBytes = urllib.request.urlopen(
                "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/" + city + "?unitGroup=metric&include=days&key=GUGUVPE393UQGQWTFKA5RE7G2&contentType=json")

            # Parse the results as JSON
            DaysjsonData = json.load(ResultBytes)

        except urllib.error.HTTPError as e:
            ErrorInfo = e.read().decode()
            print('Error code: ', e.code, ErrorInfo)

        except  urllib.error.URLError as e:
            ErrorInfo = e.read().decode()
            print('Error code: ', e.code, ErrorInfo)

        # first cell

        firstdayimage = currWeatherIcon(city)
        print(firstdayimage)
        photo1 = ImageTk.PhotoImage(file=f"images/weathericons/{firstdayimage}.png")
        self.firstimage.config(image=photo1)
        self.firstimage.image = photo1

        tempday1 = DaysjsonData['days'][0]['temp']
        status1 = currWeatherIcon(city)
        self.day1temp.config(text=f"Temp:{tempday1}\n{status1}")

        # second cell
        seconddayimage = DaysjsonData['days'][1]['icon']
        img = (Image.open(f"images/weathericons/{seconddayimage}.png"))
        resized_image = img.resize((50, 50))
        photo2 = ImageTk.PhotoImage(resized_image)
        self.secondimage.config(image=photo2)
        self.secondimage.image = photo2
        tempday2 = DaysjsonData['days'][1]['temp']
        status2 = DaysjsonData['days'][1]['icon']
        self.day2temp.config(text=f"{tempday2}\n{status2}")

        # third cell
        thirddayimage = DaysjsonData['days'][2]['icon']
        img = (Image.open(f"images/weathericons/{thirddayimage}.png"))
        resized_image = img.resize((50, 50))
        photo3 = ImageTk.PhotoImage(resized_image)
        self.thirdimage.config(image=photo3)
        self.thirdimage.image = photo3
        tempday3 = DaysjsonData['days'][2]['temp']
        status3 = DaysjsonData['days'][2]['icon']
        self.day3temp.config(text=f"{tempday3}\n{status3}")

        # fourth cell
        fourthdayimage = DaysjsonData['days'][3]['icon']
        img = (Image.open(f"images/weathericons/{fourthdayimage}.png"))
        resized_image = img.resize((50, 50))
        photo4 = ImageTk.PhotoImage(resized_image)
        self.fourthimage.config(image=photo4)
        self.fourthimage.image = photo4
        tempday4 = DaysjsonData['days'][3]['temp']
        status4 = DaysjsonData['days'][3]['icon']
        self.day4temp.config(text=f"{tempday4}\n{status4}")

        # fifth cell
        fifthdayimage = DaysjsonData['days'][4]['icon']
        img = (Image.open(f"images/weathericons/{fifthdayimage}.png"))
        resized_image = img.resize((50, 50))
        photo5 = ImageTk.PhotoImage(resized_image)
        self.fifthimage.config(image=photo5)
        self.fifthimage.image = photo5
        tempday5 = DaysjsonData['days'][4]['temp']
        status5 = DaysjsonData['days'][4]['icon']
        self.day5temp.config(text=f"{tempday5}\n{status5}")

        # sixth cell
        sixthdayimage = DaysjsonData['days'][5]['icon']
        img = (Image.open(f"images/weathericons/{sixthdayimage}.png"))
        resized_image = img.resize((50, 50))
        photo6 = ImageTk.PhotoImage(resized_image)
        self.sixthimage.config(image=photo6)
        self.sixthimage.image = photo6
        tempday6 = DaysjsonData['days'][5]['temp']
        status6 = DaysjsonData['days'][5]['icon']
        self.day6temp.config(text=f"{tempday6}\n{status6}")

        # seventh cell
        seventhdayimage = DaysjsonData['days'][6]['icon']
        img = (Image.open(f"images/weathericons/{seventhdayimage}.png"))
        resized_image = img.resize((50, 50))
        photo7 = ImageTk.PhotoImage(resized_image)
        self.seventhimage.config(image=photo7)
        self.seventhimage.image = photo7
        tempday7 = DaysjsonData['days'][6]['temp']
        status7 = DaysjsonData['days'][6]['icon']
        self.day7temp.config(text=f"{tempday7}\n{status7}")

        # days

        first = datetime.now()
        self.day1.config(text=first.strftime('%A'))

        second = first + timedelta(days=1)
        self.day2.config(text=second.strftime('%A'))

        third = first + timedelta(days=2)
        self.day3.config(text=third.strftime('%A'))

        fourth = first + timedelta(days=3)
        self.day4.config(text=fourth.strftime('%A'))

        fifth = first + timedelta(days=4)
        self.day5.config(text=fifth.strftime('%A'))

        sixth = first + timedelta(days=5)
        self.day6.config(text=sixth.strftime('%A'))

        seventh = first + timedelta(days=6)
        self.day7.config(text=seventh.strftime('%A'))


if __name__=="__main__":
    weather = Tk()
    obj=weatherApp(weather)
    weather.mainloop()

