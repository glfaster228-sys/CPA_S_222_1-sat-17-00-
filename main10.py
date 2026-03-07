import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
conn = sqlite3.connect('weather.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS weather (date TEXT, time TEXT, temperature REAL)''')
conn.commit()
url = "https://www.gismeteo.ru/weather-<ваш_город>/10-days/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
temperature = soup.find("span", class_="unit unit_temperature_c").text
temperature = float(temperature.replace("°", ""))
now = datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")
cursor.execute("INSERT INTO weather (date, time, temperature) VALUES (?, ?, ?)", (date, time, temperature))
conn.commit()
print(f"Данные о погоде сохранены: {date} {time} {temperature}°C")
conn.close()