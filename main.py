from config import open_weather_token
import requests

# создаем ф-цию-запрос для получения данных о погоде
def get_weather(city, open_weather_token):
    # в документации сервиса openweather получаем ссылку, по которой будем получать прогноз
    r = requests( тут будет ссылка)
    data = r.json # запрошенный прогноз в формате json
    print(data)

# создаем ф-цию для запроса города у пользователя
def main():
    city = input("Введите название города: ")
    get_weather(city, open_weather_token)

if name == '__main__':
    main()