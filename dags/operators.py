from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

def greet():
    print("Hello from Techjedi")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 4, 22),
}

dag = DAG('test_dag', default_args=default_args, schedule=None)

task1 = PythonOperator(task_id='greet_task', python_callable=greet, dag=dag)
task2 = PythonOperator(task_id='greet_task2', python_callable=greet, dag=dag)


task1 >> task2  # Define task order
