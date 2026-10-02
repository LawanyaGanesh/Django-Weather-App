from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv

load_dotenv()
# Create your views here.
def weather_home(request):
    # API_KEY = "ba33185df9b1656675359751cb2deaf0"

    API_KEY = os.getenv("SECRET_KEY")

    current_temp = 0
    current_celsius = 0
    city = None
    humidity = None
    weather_des = None
    error = None
    
    # weather_url = "https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=API_KEY"
    
    
    if request.method == "POST":

        
        city = request.POST.get("city").strip()

        if not city:

            error = "Please Enter a City"
        
        else:
            try:
                
                
                print(city)
                # geo_url = "https://api.openweathermap.org/data/2.5/weather"
                geo_url = os.getenv("WEATHER_URL")
                params = {
                        "q":request.POST.get("city"),
                        "APPID":API_KEY
                    }

                response = requests.get(geo_url,params=params,timeout=10)

                if response.status_code != 200:
                    error = "City Not Found"

                else:
                    data = response.json()
                    current_temp = data["main"]["temp"] 
                    humidity = data["main"]["humidity"] 
                    weather_des = data["weather"][0]["description"] 
                
                    current_celsius = current_temp - 273.15
                    print("Weather",response.json())
                    print("Current Temp",current_temp)
                

            except requests.RequestException:

                error = "Unable to connect to weather service"

    

    return render(request, "weather/home.html", {
                           "current_temp": current_celsius,
                           "city":city,
                           "humidity":humidity,
                           "weather_des":weather_des,
                           "error":error
                       })

           
            
            

    