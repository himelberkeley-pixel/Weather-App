import requests 

api_key = "9dfc10d9de03c56d64d055e3dc9ab2c8"

user_input = input("Enter the city name: ")
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] != 200:
    print("No city found with that name.")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    
    
    print(f"The weather in {user_input} is currently {weather} with a temperature of {temp}°F.")