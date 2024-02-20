import requests
import pytemperature
api_key = 'Provide_API_Key'

nameOfCity = input("Provide the name of the city: ")

result = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={nameOfCity}&appid={api_key}', timeout=60)

if result.status_code == 200:
    data = result.json()
    kelvin = data['main']['temp']
    kelvin = round(kelvin,2)
    desc = data['weather'][0]['description']
    celsius = round(pytemperature.k2c(kelvin),2)
    fahrenheit = round(pytemperature.k2f(kelvin),2)
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    
    print(f'Humidity: {humidity}%')
    print(f'Wind: {round(wind*2.237,2)} mph')
    print(f'Temperature in Kelvin: {kelvin} K')
    print(f'Temperature in Celsius: {celsius} C')
    print(f'Temperature in Fahrenheit: {fahrenheit} F')
    print(f'Description: {desc.capitalize()}')

else:
    print("There was an error receiving the data, please retry.")
