# scripts/fetch_weather.py
import requests
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv("/opt/airflow/.env")  # path ภายใน container
from datetime import datetime

def fetch_and_store_weather_for_city(city):
    API_KEY = os.getenv("API_KEY") #!!<---------- ใส่ API KEY ที่นี่ 
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    res = requests.get(URL)
    data = res.json()
    temp = data["main"]["temp"]

    conn = psycopg2.connect(
        host="postgres",      # ชื่อ service postgres ใน docker-compose
        database="weather",
        user="airflow",
        password="airflow"
    )
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO weather_data (city, temperature, recorded_at) VALUES (%s, %s, %s)",
        (city, temp, datetime.now())
    )
    conn.commit()
    cur.close()
    conn.close()
