from tkinter import *
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
from tkinter import PhotoImage
import requests
import pytz

class WeatherApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Weather App")
        self.root.geometry("900x500+10+10")
        self.root.resizable(0, 0)
        
        # Default city name
        self.default_city = "New Delhi"  # Change this to your preferred default city
        
        # City Name Entry
        self.EntrycityName = Label(self.root, text='Enter City Name:', font=('Roboto', 12))
        self.EntrycityName.place(x=10, y=10)
        self.entryCity = Entry(self.root, bd=1, relief='solid', font=('Roboto', 12))
        self.entryCity.insert(0, self.default_city)  # Set default value
        self.entryCity.place(x=150, y=10, width=500, height=25)
        self.searchbtn = Button(self.root, text='Search', font=('Roboto', 14), bd=1, relief='solid', bg='green', fg='#FFFFFF', command=self.weather)
        self.searchbtn.place(x=660, y=10, width=100, height=25)
        
        # Current Weather Labels
        self.timeZoneShow = Label(self.root, text='Current Weather', font=('roboticl', 15))
        self.timeZoneShow.place(x=10, y=50)
        self.t = StringVar()
        self.timeShow = Label(self.root ,textvariable=self.t, font=('robotic', 15,'bold'))
        self.timeShow.place(x=10, y=90)
        
        # Weather image
        try:
            self.img = PhotoImage(file="C:\\Users\\hp\\Desktop\\python Mysql Project\\tkinter project\\Weather Application GUI\\weather.png")
            # Resize image
            self.img = self.img.subsample(5)  # Change the number as needed for scaling
            self.imgBtn = Label(self.root, image=self.img)
            self.imgBtn.place(x=200, y=60)
        except Exception as e:
            print(f"Error loading image: {e}")
        
        # Temperature and Condition
        self.showcityname=Label(self.root, text='', font=('Arial', 30,'bold'))
        self.showcityname.place(x=500,y=90)
        self.showTemperature = Label(self.root, text='0°c', font=('Arial', 50,'bold'),fg='red')
        self.showTemperature.place(x=500, y=150)
        # self.conditionLabel = Label(self.root, text='Condition : ', font=('Arial', 15,'bold'))
        # self.conditionLabel.place(x=500, y=210)
        self.conditionText = StringVar()
        self.conditionShow = Label(self.root, textvariable=self.conditionText, font=('Arial', 15,'bold'))
        self.conditionShow.place(x=500, y=250)
        
        # Weather details frame
        self.frame = Frame(self.root, bd=0, relief='solid',bg='green')
        self.frame.place(x=0, y=400, width=900, height=100)
        
        self.windlb = Label(self.frame, text='Wind', font=('Roboto', 12),bg='green',fg='white')
        self.windlb.place(x=50, y=10)
        self.w = Label(self.frame, text='0',bg='green',fg='white')
        self.w.place(x=60, y=30)
        
        self.humiditylb = Label(self.frame, text='Humidity', font=('Roboto', 12),bg='green',fg='white')
        self.humiditylb.place(x=250, y=10)
        self.h = Label(self.frame, text='0',bg='green',fg='white')
        self.h.place(x=260, y=30)
        
        self.descriptionlb = Label(self.frame, text='Description', font=('Roboto', 12),bg='green',fg='white')
        self.descriptionlb.place(x=450, y=10)
        self.d = Label(self.frame, text='0',bg='green',fg='white')
        self.d.place(x=460, y=30)
        
        self.pressurelb = Label(self.frame, text='Pressure', font=('Roboto', 12),bg='green',fg='white')
        self.pressurelb.place(x=650, y=10)
        self.p = Label(self.frame, text='0',bg='green',fg='white')
        self.p.place(x=660, y=30)
        
        # Loading Label
        self.loadingLabel = Label(self.root, text='Fetching data...', font=('Arial', 12))
        
        self.root.mainloop()
    
    def show_loading(self):
        # Place loading message on screen
        self.loadingLabel.place(x=10, y=320)
        self.root.update()  # Force update to show loading message
    
    def hide_loading(self):
        # Remove loading message from screen
        self.loadingLabel.place_forget()
        self.showcityname.config(text=city_name.capitalize())
    
    def weather(self):
        global city_name
        city_name = self.entryCity.get()
        
        if not city_name:
            messagebox.showerror("Error", "Please enter a city name")
            return
        
        self.show_loading()  # Show loading message
        
        geolocator = Nominatim(user_agent='geoapiExercise')
        location = geolocator.geocode(city_name)
        if not location:
            self.hide_loading()  # Hide loading message
            messagebox.showerror("Error", "City not found")
            return
        
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime('%I:%M %p')
        self.t.set(current_time)
        
        # API call
        api_key = '700b7cc64390310fdffa2dfdbff81ec5'
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        
        try:
            response = requests.get(api_url, timeout=5)  # Timeout set to 5 seconds
            response.raise_for_status()  # Raise error for bad response codes
        except requests.exceptions.RequestException as e:
            self.hide_loading()  # Hide loading message
            messagebox.showerror("Error", f"Failed to get weather data: {e}")
            return
        
        self.hide_loading()  # Hide loading message after API call
        
        json_data = response.json()
        self.condition = json_data['weather'][0]['main']
        self.description = json_data['weather'][0]['description']
        self.temp = int(json_data['main']['temp'] - 273.15)
        self.humidity = json_data['main']['humidity']
        self.pressure = json_data['main']['pressure']
        self.wind_speed = json_data['wind']['speed']
        
        self.showTemperature.config(text=f"{self.temp} °C")
        self.conditionText.set(f"Condition - {self.condition} | Feels like {self.temp} °C")
        self.w.config(text=f"{self.wind_speed} m/s")
        self.h.config(text=f"{self.humidity} %")
        self.d.config(text=self.description)
        self.p.config(text=f"{self.pressure} hPa")

if __name__ == '__main__':
    WeatherApp()
