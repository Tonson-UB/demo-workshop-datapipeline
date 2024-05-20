import datetime

from airflow.models import DAG
from airflow.opertors.python import PythonOperator
from airflow.operators.bash import BashOpertor
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'admin',
}

def my_function(something: str):
    print(something)

with DAG(
    "ws_exercise1_dag",
    start_date=days_ago(1),
    schedule_interval=None,
    tags=["exercise"]
) as dag:
    
    # create task
    t1 = PythonOperator(
        task_id="print_hello",
        python_callable=my_function,
        op_kwargs={"somthing":"Hello World"},
    )

    t2 = BashOpertor(
        task_id="print_date",
        bash_command="echo $(date)",
    )

    # task dependencies
    t1 >> t2