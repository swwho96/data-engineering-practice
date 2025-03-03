from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests

def index_articles():
    url = "http://host.docker.internal:8000/index_articles"
    response = requests.get(url)



default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 3, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}

dag = DAG(
    "fetch_articles",
    default_args=default_args,
    description="기사 최신화 테스트",
    schedule_interval="*/5 0 * * *",
)

news_update_task = PythonOperator(
    task_id="fetch_and_store_articles",
    python_callable=index_articles,
    dag=dag
)

news_update_task