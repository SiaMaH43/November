import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


# Создаю бота в телеграм c помощью BotFather. Получаю токен для него
# Регистрируюсь на сайте openweather, получаю токен и API

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

# создаю функцию запроса погоды
def get_weather(city, open_weather_token):

    # добавляю юникоды эмоджи для визуализации наиболее частых вариантов прогноза
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Couds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        # в документации сервиса openweather получаем ссылку, по которой будем получать прогноз
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
        )
        data = r.json() # переменная с результатом прогноза в формате json

        city = data['name']
        cur_weather = data['main']['temp']

        weather_description = data["weather"][0]["main"]

        # прописываю алгоритм действий на случай, когда подходящего эмоджи не окажется
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму, что там за погода!"

        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f'Погода в городе: {city}\nТемпература: {cur_weather}°C {wd}\n'
              f'Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n'
              f'Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n'
              f'Хорошего дня!'
              )


    except Exception as ex: # создаю исключение на случай опечаток и ошибок в запросе города
        print(ex)
        print("Проверьте название города")

# создаем ф-цию для запроса города у пользователя
def main():
    city = input("Введите название города: ")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()