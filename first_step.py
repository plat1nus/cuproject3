import requests

API_KEY = 'LY9AQYq7HoGraGryaCkDDM77Wo6yevyU' # сначала хотел в отдельный файл токен запихнуть, но здесь это как будто вообще некритично
latitude = '35.6895'  # Пример: широта Токио
longitude = '139.6917'  # Пример: долгота Токио

# Получение location_key по координатам
def get_location_key(latitude, longitude):
    location_url = f"http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={API_KEY}&q={latitude},{longitude}"
    response = requests.get(location_url)
    location_data = response.json()
    return location_data['Key']

latitude = '35.6895'  # Пример: широта Токио
longitude = '139.6917'  # Пример: долгота Токио

location_key = get_location_key(latitude, longitude)
# print(f"Location Key: {location_key}")


url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={API_KEY}&details=true"

response = requests.get(url)
data = response.json()

print(data)

temperature = data[0]['Temperature']['Metric']['Value']
humidity = data[0]['RelativeHumidity'] 
wind_speed = data[0]['Wind']['Speed']['Metric']['Value'] 
precipitation_probability = data[0]['PrecipitationSummary']['Precipitation']['Metric']['Value']

with open('weather_data.txt', 'w', encoding='utf-8') as file:
    file.write(f"Температура: {temperature}°C\n")
    file.write(f"Влажность: {humidity}%\n")
    file.write(f"Скорость ветря: {wind_speed} км/ч\n")
    file.write(f"Вероятность дождя в процентах: {precipitation_probability}%\n")

# print("Данные о погоде успешно сохранены в файл weather_data.txt.")
