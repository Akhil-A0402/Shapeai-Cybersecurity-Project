import requests
from datetime import datetime

api="326b403c89f8680312153782cf6b5d6c"

city=input("Enter the name of city:")

data = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api)

if(data.status_code<300 and data.status_code>=200):
        data=data.json()

        #data
        city_name=data["name"]
        temp=data["main"]["temp"]-273.15
        weather=data["weather"][0]["main"]
        pressure=data["main"]["pressure"]
        humidity=data["main"]["humidity"]
        max_temp=data["main"]["temp_max"]-273.15
        min_temp=data["main"]["temp_min"]-273.15
        today=datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        #file
        f=open("data.txt",'w')
        f.write("City:{}\nDate:{}\n\n".format(city_name,today))
        f.write("Temperature:{:.2f}, Weather:{}, Pressure:{}, Humidity:{}, Maximum Temperature:{:.2f}, Minimum Temperature:{:.2f}".format
                (temp,weather,pressure,humidity,max_temp,min_temp))
        f.close()

        print("The weather at {} on {} is:\n".format(city_name,today))

        print("Temperature:{:.2f}".format(temp))
        print("Weather:{}".format(weather))
        print("Pressure:{}".format(pressure))
        print("Humidity:{}".format(humidity))
        print("Maximum Temperature:{:.2f}".format(max_temp))
        print("Minimum Temperature:{:.2f}".format(min_temp))

else:
        print("Invalid name was provided or server is down")