from airflow.decorators import dag, task
from datetime import datetime


@dag(dag_id="calcu_eg", start_date=datetime(2025, 1, 1), schedule="@daily")
def calcu_eg():
    @task()
    def add():
        return a+b

    @task()
    def mult(res):
        return res*4
    @task()
    def show_res(result):
        print(f"final result is:{result}")
    

    sum_res=add(3,9)
    mult_res=mult(sum_res)
    show_res(mult_res)
    

    # Define dependencies
calcu_eg()
