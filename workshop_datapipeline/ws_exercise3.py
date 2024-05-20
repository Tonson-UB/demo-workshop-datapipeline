from airflow.models import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

with DAG(
    "exercise_fan_in_dag",
    start_date=days_ago(1),
    schedule_interval=None,
    tag=["exercise"],
) as dag:
    
    # Exercise3: Fan-in Pipeline

    t0 = DummyOperator(task_id="task_0")
    t4 = DummyOperator(task_id="task_4")

    t0 >> t4

    # สร้าง DummyOperator เพื่อสร้าง dependency ที่ซับซ้อน
    
    t1 =DummyOperator(task_id="task_1")
    t2 =DummyOperator(task_id="task_2")
    t3 =DummyOperator(task_id="task_3")

    t5 =DummyOperator(task_id="task_5")
    t6 =DummyOperator(task_id="task_6")
    
    # task dependencies
    [t0, t1, t2] >> t4
    [t3, t4, t5] >> t6
