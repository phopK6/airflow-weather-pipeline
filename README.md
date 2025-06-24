# 🌤️ Airflow Weather Pipeline

โปรเจกต์นี้ใช้ **Apache Airflow**, **PostgreSQL**, และ **OpenWeatherMap API** เพื่อดึงข้อมูลสภาพอากาศรายวันของหลายเมือง และเก็บข้อมูลลงในฐานข้อมูล

---

## 🧰 Tech Stack

- Apache Airflow 2.9.1 (รันใน Docker Container)
- PostgreSQL 13 (รันใน Docker Container)
- Python 3.x
- Docker & Docker Compose
- OpenWeatherMap API

---

## 📁 โครงสร้างโปรเจกต์

weather-pipeline/
├── dags/ # โฟลเดอร์เก็บ Airflow DAG
│ └── daily_weather_multi_city.py
├── scripts/ # Python scripts ที่ใช้ใน DAG
│ └── fetch_weather.py
├── requirements.txt # ไลบรารี Python ที่ต้องติดตั้ง
├── docker-compose.yaml # สคริปต์รัน Airflow + PostgreSQL ด้วย Docker
├── .gitignore
└── README.md

