from airflow.decorators import dag, task
from datetime import datetime


@dag(
    start_date=datetime(2024, 8, 2),
    schedule=None,
    catchup=False,
    tags=['test'],
)
def test_dag():

    @task
    def simple_task():
        print("Task executed")

    simple_task()


test_dag()
