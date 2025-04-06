import requests

city = input("Check temperature : ")

if city == "":
    print("\nPlease enter your city name")

else:
    api_key = "5fd67ac122390c25e3a0a4f8a7124751"

    base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+city

    weather_data = requests.get(base_url).json()

    if weather_data["cod"] == 200:
        print("\nCity Name:", weather_data["name"])
        print("Country:", weather_data["sys"]["country"])
        print("Temperature:", weather_data["main"]["temp"])
        print("Feels Like:", weather_data["main"]["feels_like"])
        print("Minimum Temperature:", weather_data["main"]["temp_min"])
        print("Maximum Temperature:", weather_data["main"]["temp_max"])
        print("Humidity:", weather_data["main"]["humidity"], "%")
        print("Weather Description:", weather_data["weather"][0]["description"])
        print("Wind Speed:", weather_data["wind"]["speed"], "m/s")
        print("Wind Direction:", weather_data["wind"]["deg"], "°")

    else:
        print("\nNot Find Your Country Temperature")

