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



weather = Tk()
weather.title("Weather App")
weather.geometry("890x470+300+200")
weather.configure(bg="#57adff")
weather.resizable(False,False)

def go_home():
    weather.destroy()
    import newDashboard5


def currWeatherIcon(location):
    currtime = datetime.now()
    currhour = currtime.hour
    try:
        ResultBytes = urllib.request.urlopen(
            "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"+location+"?unitGroup=us&include=alerts%2Chours%2Cdays%2Ccurrent&key=GUGUVPE393UQGQWTFKA5RE7G2&contentType=json")

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

def getWeather():
    city=textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    #weather
    api_key = "b5765b346a0d53eae55bb58181ee09b4"
    #API_KEY = "a38e8a9065e5a25cbc3f6a9316ddfa5c"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city

    response = requests.get(complete_url)
    json_data = response.json()
    print(json_data)
    temp = round((json_data['main']['temp'])-273.15,0)
    humidity = json_data['main']['humidity']
    pressure = json_data['main']['pressure']
    wind = json_data['wind']['speed']
    description = json_data['weather'][0]['description']

    t.config(text=(temp,"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure , "hPa"))
    w.config(text=(wind,"m/s"))
    d.config(text=description)

#WEATHER FORECAST
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

    #first cell

    firstdayimage = currWeatherIcon(city)
    print(firstdayimage)
    photo1 = ImageTk.PhotoImage(file=f"images/weathericons/{firstdayimage}.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1

    tempday1 = DaysjsonData['days'][0]['temp']
    status1 = currWeatherIcon(city)
    day1temp.config(text=f"Temp:{tempday1}\n{status1}")

    #second cell
    seconddayimage = DaysjsonData['days'][1]['icon']
    img = (Image.open(f"images/weathericons/{seconddayimage}.png"))
    resized_image = img.resize((50,50))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image=photo2
    tempday2 = DaysjsonData['days'][1]['temp']
    status2 =  DaysjsonData['days'][1]['icon']
    day2temp.config(text=f"{tempday2}\n{status2}")

    #third cell
    thirddayimage = DaysjsonData['days'][2]['icon']
    img = (Image.open(f"images/weathericons/{thirddayimage}.png"))
    resized_image = img.resize((50, 50))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image = photo3
    tempday3 = DaysjsonData['days'][2]['temp']
    status3 = DaysjsonData['days'][2]['icon']
    day3temp.config(text=f"{tempday3}\n{status3}")

    #fourth cell
    fourthdayimage = DaysjsonData['days'][3]['icon']
    img = (Image.open(f"images/weathericons/{fourthdayimage}.png"))
    resized_image = img.resize((50, 50))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image = photo4
    tempday4 = DaysjsonData['days'][3]['temp']
    status4 = DaysjsonData['days'][3]['icon']
    day4temp.config(text=f"{tempday4}\n{status4}")

    #fifth cell
    fifthdayimage = DaysjsonData['days'][4]['icon']
    img = (Image.open(f"images/weathericons/{fifthdayimage}.png"))
    resized_image = img.resize((50, 50))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image = photo5
    tempday5 = DaysjsonData['days'][4]['temp']
    status5 = DaysjsonData['days'][4]['icon']
    day5temp.config(text=f"{tempday5}\n{status5}")


    #sixth cell
    sixthdayimage = DaysjsonData['days'][5]['icon']
    img = (Image.open(f"images/weathericons/{sixthdayimage}.png"))
    resized_image = img.resize((50, 50))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image = photo6
    tempday6 = DaysjsonData['days'][5]['temp']
    status6 = DaysjsonData['days'][5]['icon']
    day6temp.config(text=f"{tempday6}\n{status6}")


    #seventh cell
    seventhdayimage = DaysjsonData['days'][6]['icon']
    img = (Image.open(f"images/weathericons/{seventhdayimage}.png"))
    resized_image = img.resize((50, 50))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image = photo7
    tempday7 = DaysjsonData['days'][6]['temp']
    status7 = DaysjsonData['days'][6]['icon']
    day7temp.config(text=f"{tempday7}\n{status7}")


    #days

    first = datetime.now()
    day1.config(text=first.strftime('%A'))

    second = first + timedelta(days=1)
    day2.config(text=second.strftime('%A'))

    third = first + timedelta(days=2)
    day3.config(text=third.strftime('%A'))

    fourth = first + timedelta(days=3)
    day4.config(text=fourth.strftime('%A'))

    fifth = first + timedelta(days=4)
    day5.config(text=fifth.strftime('%A'))

    sixth = first + timedelta(days=5)
    day6.config(text=sixth.strftime('%A'))

    seventh = first + timedelta(days=6)
    day7.config(text=seventh.strftime('%A'))


##icon
image_icon = PhotoImage(file="images/weatherlogo.png")
weather.iconphoto(False,image_icon)

Round_box = PhotoImage(file="images/Rounded Rectangle 1.png")
Label(weather,image=Round_box,bg="#57adff").place(x=30,y=110)

label1 = Label(weather,text="Temperature",font=("Helvetica",11),fg='white',bg="#203243")
label1.place(x=50,y=120)
label2 = Label(weather,text="Humidity",font=("Helvetica",11),fg='white',bg="#203243")
label2.place(x=50,y=140)
label3 = Label(weather,text="Pressure",font=("Helvetica",11),fg='white',bg="#203243")
label3.place(x=50,y=160)
label4 = Label(weather,text="Wind Speed",font=("Helvetica",11),fg='white',bg="#203243")
label4.place(x=50,y=180)
label5 = Label(weather,text="Description",font=("Helvetica",11),fg='white',bg="#203243")
label5.place(x=50,y=200)

#search box
Search_image = PhotoImage(file="images/longrec4.png")
myimage=Label(image=Search_image,bg="#57adff")
myimage.place(x=270,y=80)

weat_image=PhotoImage(file='images/sun.png')
weatherimage=Label(weather,image=weat_image,bg="#203243",border=0)
weatherimage.place(x=308,y=137)

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
firstbox = PhotoImage(file="images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="images/Rounded Rectangle 2 copy.png")

Label(weatherframe,image=firstbox,bg="#212120").place(x=30,y=20)
Label(weatherframe,image=secondbox,bg='#212120').place(x=300,y=30)
Label(weatherframe,image=secondbox,bg='#212120').place(x=400,y=30)
Label(weatherframe,image=secondbox,bg='#212120').place(x=500,y=30)
Label(weatherframe,image=secondbox,bg='#212120').place(x=600,y=30)
Label(weatherframe,image=secondbox,bg='#212120').place(x=700,y=30)
Label(weatherframe,image=secondbox,bg='#212120').place(x=800,y=30)

#clock
clock=Label(weather,font=("Helvetica",30,'bold'),fg="white",bg='#57adff')
clock.place(x=30,y=20)

#timezone
timezone=Label(weather,font=("Helvetica",20),fg="white",bg='#57adff')
timezone.place(x=700,y=20)

long_lat=Label(weather,font=("Helvetica",10),fg="white",bg='#57adff')
long_lat.place(x=700,y=50)

t=Label(weather,font=('Helvetica',11),fg='white',bg="#203243")
t.place(x=150,y=120)
h=Label(weather,font=('Helvetica',11),fg='white',bg="#203243")
h.place(x=150,y=140)
p=Label(weather,font=('Helvetica',11),fg='white',bg="#203243")
p.place(x=150,y=160)
w=Label(weather,font=('Helvetica',11),fg='white',bg="#203243")
w.place(x=150,y=180)
d=Label(weather,font=('Helvetica',11),fg='white',bg="#203243")
d.place(x=150,y=200)

firstframe=Frame(weather,width=230,height=132,bg='#282829')
firstframe.place(x=35,y=315)
day1=Label(firstframe,font="arial 20",bg='#282829',fg="#fff")
day1.place(x=100,y=5)
firstimage=Label(firstframe,bg="#282829")
firstimage.place(x=1,y=15)
day1temp=Label(firstframe,bg="#282829",fg="#57adff",font='arial 15 bold')
day1temp.place(x=80,y=50)


secondframe=Frame(weather,width=70,height=115,bg='#282829')
secondframe.place(x=305,y=325)
day2=Label(secondframe,bg='#282829',fg="#fff")
day2.place(x=10,y=5)
secondimage=Label(secondframe,bg='#282829')
secondimage.place(x=7,y=20)
day2temp=Label(secondframe,bg='#282829',fg='#fff')
day2temp.place(x=0,y=70)

thirdframe=Frame(weather,width=70,height=115,bg='#282829')
thirdframe.place(x=405,y=325)
day3=Label(thirdframe,bg='#282829',fg="#fff")
day3.place(x=10,y=5)
thirdimage=Label(thirdframe,bg='#282829')
thirdimage.place(x=7,y=20)
day3temp=Label(thirdframe,bg='#282829',fg='#fff')
day3temp.place(x=0,y=70)

fourthframe=Frame(weather,width=70,height=115,bg='#282829')
fourthframe.place(x=505,y=325)
day4=Label(fourthframe,bg='#282829',fg="#fff")
day4.place(x=10,y=5)
fourthimage=Label(fourthframe,bg='#282829')
fourthimage.place(x=7,y=20)
day4temp=Label(fourthframe,bg='#282829',fg='#fff')
day4temp.place(x=0,y=70)

fifthframe=Frame(weather,width=70,height=115,bg='#282829')
fifthframe.place(x=605,y=325)
day5=Label(fifthframe,bg='#282829',fg="#fff")
day5.place(x=10,y=5)
fifthimage=Label(fifthframe,bg='#282829')
fifthimage.place(x=7,y=20)
day5temp=Label(fifthframe,bg='#282829',fg='#fff')
day5temp.place(x=0,y=70)

sixthframe=Frame(weather,width=70,height=115,bg='#282829')
sixthframe.place(x=705,y=325)
day6=Label(sixthframe,bg='#282829',fg="#fff")
day6.place(x=10,y=5)
sixthimage=Label(sixthframe,bg='#282829')
sixthimage.place(x=7,y=20)
day6temp=Label(sixthframe,bg='#282829',fg='#fff')
day6temp.place(x=0,y=70)


seventhframe=Frame(weather,width=70,height=115,bg='#282829')
seventhframe.place(x=805,y=325)
day7=Label(seventhframe,bg='#282829',fg="#fff")
day7.place(x=10,y=5)
seventhimage=Label(seventhframe,bg='#282829')
seventhimage.place(x=7,y=20)
day7temp=Label(seventhframe,bg='#282829',fg='#fff')
day7temp.place(x=0,y=70)

# Load the image
image = Image.open("images/home.png")

# Remove the background
image = image.convert("RGBA")
data = image.getdata()
new_data = []
for item in data:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        # new_data.append((60,150,255,255))
        new_data.append((99,164,255,255))
    else:
        new_data.append(item)
image.putdata(new_data)

# Create a PhotoImage object with transparent background
photo_image = ImageTk.PhotoImage(image)

# Create a button with the PhotoImage object
button = Button(weather, image=photo_image, bd=0, highlightthickness=0,activebackground='Steelblue1',command=go_home)
button.place(x=840,y=60)

weather.mainloop()
