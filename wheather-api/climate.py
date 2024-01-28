from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from dateutil import tz
from datetime import datetime
from timezonefinder import TimezoneFinder
import requests
import pytz

root =Tk()
root.title("Wheater App")
root.geometry("1000x500+250+125")
root.resizable(False,False)

def getWeather():
    try:
        city=textfield.get()
        # Build the request URL including the API key
        geolocator=Nominatim(user_agent="manu-api-practice-1")
        location = geolocator.geocode(city)
    
        #proof
        """"if location:
            lat = location.latitude
            lon = location.longitude
            print(f"Latitud: {lat}, Longitud: {lon}")
            obj = TimezoneFinder()
            timezone_str = obj.timezone_at(lng=lon, lat=lat)
            print(f"Zona horaria: {timezone_str}")
        
            #Here you can perform other actions with the latitude and longitude, since you already have them available.

        else:
            print("Location not found for the city provided.")
        """
        obj = TimezoneFinder()
   
    
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        # print(result)
        home= pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WHEATHER")
    
        #Wwheather
        lng=location.longitude
        lat=location.latitude
        api_key = "8abbfe4291c8beef8dc8d5902ae38472"
        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}"
        json_data = requests.get(api_url).json()
        condition = json_data['weather'][0]['main']
        description =json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
    
        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Wheather App","Invalid Entry!!")
#search box
search_image=PhotoImage(file="search.png")
my_image= Label(image=search_image)
my_image.place(x=15,y=15)

textfield=tk.Entry(root, justify="center",width=18, font=("poppins",25, "bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

search_icon=PhotoImage(file="search_icon.png")
my_image_icon=Button(image=search_icon,borderwidth=0,cursor="hand2", bg="#404040", command=getWeather)
my_image_icon.place(x=390,y=29)


#logo
logo_image= PhotoImage(file="logo.png")
logo=Label(image=logo_image)
logo.place(x=150,y=100)


#bottom box
Frame_image= PhotoImage(file="box.png")
frame_image= Label(image=Frame_image)
frame_image.pack(padx=5,pady=5,side=BOTTOM)

#Time
name= Label(root,font=("arial",13,"bold"))
name.place(x=20,y=100)
clock= Label(root, font=("Helvetica",18))
clock.place(x=30,y=130)
#label 
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=170,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=270,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=460,y=400)


label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=680,y=400)


t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=180,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=305,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=460,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=700,y=430)


root.mainloop()

