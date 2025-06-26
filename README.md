ยังไม่เสร็จนะครับรอสักครู่
กำลังเพิ่ม metabase
# 🌤️ Airflow Weather Pipeline

โปรเจกต์นี้ใช้ **Apache Airflow**, **PostgreSQL**, และ **OpenWeatherMap API** เพื่อดึงข้อมูลสภาพอากาศรายวันของหลายเมือง และเก็บข้อมูลลงในฐานข้อมูล
และใช้ Metabase สำหรับเป็น report

---

## 🧰 Tech Stack

- Apache Airflow 2.9.1 (รันใน Docker Container)
- PostgreSQL 13 (รันใน Docker Container)
- Python 3.x
- Docker & Docker Compose
- OpenWeatherMap API
- Metabse

---

## 📁 โครงสร้างโปรเจกต์

weather-pipeline/

เมื่อติดตั้งทุกอย่างเสร็จให้สร้าง DataBase ชื่อ weather เพิ่ม
และ นี่คือ table สำหรับ บันทึกและดึงข้อมูล
CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100),
    temperature FLOAT,
    recorded_at TIMESTAMP
);

---

### Special thanks
chatgpt


