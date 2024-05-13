import datetime

from airflow.decorators import dag,task
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'admin'
}

@task()
def print_hello():
    print("Hello World")


@task()
def print_date():
    print(datetime.datetime.now())


@dag(default_args=default_args, schedule_interval=None, start_date=days_ago(1), tag=['exercise'])
def exercise2_taskflow_dag():

    t1 = print_hello()
    t2 = print_date()

    t3 = BashOperator(
        task_id="list_file_gcs",
        bash_command="gsutil ls gs://bucket",
    )

    t1 >> [t2, t3]
    
# เรียกใช้ function dag
exercise2_dag = exercise2_taskflow_dag()