from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
sys.path.append('/opt/airflow/scripts')

from fetch_weather import fetch_and_store_weather_for_city

cities = ['Bangkok', 'Chiang Mai', 'Phuket']

def fetch_for(city):
    return lambda: fetch_and_store_weather_for_city(city)

with DAG(
    dag_id="daily_weather_multi_city",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:
    for city in cities:
        PythonOperator(
            task_id=f"fetch_weather_{city.replace(' ', '_').lower()}",
            python_callable=fetch_for(city)
        )
