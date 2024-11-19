from pendulum import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator


default_args = {
    "start_date": datetime(2024, 9, 30),
    "depends_on_past": False,
    "retries": 3,
}


dag = DAG(
    dag_id="airflow_test2",
    schedule_interval=None,
    catchup=False,
    max_active_runs=1,
    default_args=default_args,
)

start = DummyOperator(task_id="start", dag=dag)
end = DummyOperator(task_id="end", dag=dag)

start >> end
