import datetime

from airflow.decorators import dag,task
from airflow.utils.dates import day_ago

default_args = {
    'owner': 'admin'
}

@task()
def print_hello():

    print("Hello World")

@task()
def print_date():

    print(datetime.datetime.now())

@dag(default_args=default_args, schedule_interval=None, start_date=day_ago(1), tag=['exercise'])
def exercise_taskflow_dag():

    t1 = print_hello()
    t2 = print_date()

    # task dependencies
    t1 >> t2

exercise1_dag = exercise_taskflow_dag()
