from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from timezonefinder import timezonefinder
from geopy.geocoders import Nominatim
from datetime import datetime
import requests
import pytz

class weatherApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Weather App")
        self.root.geometry("900x500+10+10")
        self.root.resizable(0,0)
        
        #================================================================
        
        self.EntrycityName=Label(self.root,text='Enter City Name :',font=('Robotic',12))
        self.EntrycityName.place(x=10,y=10)
        self.entryCity=Entry(self.root,bd=1,relief='solid',font=('Robotic',12))
        self.entryCity.place(x=150,y=10,width=500,height=25)
        self.searchbtn=Button(self.root,text='Search',font=('Robotic',14),bd=1,relief='solid',bg='green',fg='#FFFFFF',command=self.weather)
        self.searchbtn.place(x=660,y=10,width=100,height=25)
        #================================================================
        self.timeZoneShow=Label(self.root,text='Current Weather')
        self.timeZoneShow.place(x=10,y=50)
        self.t=StringVar()
        self.timeShow=Label(self.root,text='0',textvariable=self.t)
        self.timeShow.place(x=10,y=70)
        #================================================================
        self.showTemperature = Label(self.root,text='0',font=('arial',30))
        self.showTemperature.place(x=550,y=100)
        #================================================================
        self.frame=Frame(self.root,bd=1,relief='solid')
        self.frame.place(x=10,y=350,width=880,height=100)
        
        self.windlb=Label(self.frame,text='Wind',font=('Robotic',12))
        self.windlb.place(x=50,y=10)
        self.w=Label(self.frame,text='0')
        self.w.place(x=60,y=30)
        self.humidityb=Label(self.frame,text='Humidity',font=('Robotic',12))
        self.humidityb.place(x=250,y=10)
        self.h=Label(self.frame,text='0')
        self.h.place(x=260,y=30)
        self.descriptionlb=Label(self.frame,text='Description',font=('Robotic',12))
        self.descriptionlb.place(x=450,y=10)
        self.d=Label(self.frame,text='0')
        self.d.place(x=460,y=30)
        self.pressurelb=Label(self.frame,text='Pressure',font=('Robotic',12))
        self.pressurelb.place(x=650,y=10)
        self.p=Label(self.frame,text='0')
        self.p.place(x=660,y=30)
        self.root.mainloop()
    #----------------------------------------------------------------
    def weather(self):
        self.cityName=self.entryCity.get()
        self.geolocater=Nominatim(user_agent='geoapiExercise')
        self.obj=timezonefinder()
        self.result=self.obj.timezone_at(lng=self.location.longitude,lat=self.location.latitude)
        self.home=pytz.timezone(self.result)
        self.local_time=datetime.now(self.home)
        self.current_time=self.local_time.strftime('%I:%M:%P')
        self.textShow.config(Text=self.current_time)
        
        #api
        self.api="https://api.openweathermap.org/data/2.5/weather?lat=" + self.cityName+'&appid=700b7cc64390310fdffa2dfdbff81ec5'
        self.json_data=requests.get(self.api).json()  
        self.condition=self.json_data['weather'][0]['main']
        self.description=self.json_data['weather'][0]['description'] 
        self.temp=int(self.json_data['weather']['temp']-273.15)
        self.humidity=int(self.json_data['weather']['humidity'])
        self.pressure=int(self.json_data['weather']['pressure'])
        self.wind=int(self.json_data['weather']['speed'])
        self.t.config(text=(self.temp))
        self.c.congif(text=(self.condition,'|',"Feels","Like",self.temp))
        self.w.config(text= self.wind)
        self.h.config(text= self.humidity)
        self.d.config(text= self.description)
        self.p.config(text= self.pressure)
           
        
if __name__ == '__main__':
    weatherApp()