from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.utils.dates import days_ago
import pandas as pd
import requests

MYSQL_CONNECTION = "mysql_default" # ชื่อของ connection ใน Airflow ที่ set ไว้
CONVERSION_RATE_URL = "https://demo_url"

# path ที่จะใช้
mysql_output_path = "/home/airflow/gcs/data/audible_data_merged.csv"
conversion_rate_output_path = "/home/airflow/gcs/data/conversion_rate.csv"
final_output_path = "/home/airflow/gcs/data/output.csv"

def get_data_from_mysql(transaction_path):
    # รับ transaction path มาจาก task ที่เรียกใช้

    # เรียกใช้ MySqlHook เพื่อต่อไปยัง MySQL จาก connection ที่สร้างไว้ใน Airflow
    mysqlserver = MySqlHook(MYSQL_CONNECTION)

    # Query จาก database โดยใช้ Hook ที่สร้างผลลัพธ์ได้  pandas DataFrame
    audible_data = mysqlserver.get_pandas_df(sql="SELECT * FROM audible_data")
    audible_transaction = mysqlserver.get_pandas_df(sql="SELECT * FROM audible_transaction")

    # Merge data จาก 2 DataFrame
    df = audible_transaction.merge(audible_data, how="left", left_on="book_id", right_on="Book_ID")

    # Save file CSV transaction_path (/home/airflow/gcs/data/audible_data_merged.csv)
    # จะไปอยู่ที่ GCS โดยอัตโนมัติ
    df.to_csv(transaction_path,index=False)
    print(f"Output to {transaction_path}")

def get_conversion_rate(conversion_rate_path):
    r = requests.get(CONVERSION_RATE_URL)
    result_conversion_rate = r.json()
    df = pd.DataFrame(result_conversion_rate)

    # เปลี่ยนจาก index ที่เป็น date ให้เป็น column ชื่อ date แทนแล้ว save file csv
    df = df.reset_index().rename(columns={"index": "date"})
    df.to_csv(conversion_rate_path, index=False)
    print(f"Output to {conversion_rate_path}")

def merge_data(transaction_path,conversion_rate_path,output_path):
    # อ่านจากไฟล์
    transaction = pd.read_csv(transaction_path)
    conversion_rate = pd.read_csv(conversion_rate_path)

    # สร้าง colume 'date' และ แปลง data type ให้เป็น datetime และเอาเฉพาะวันที่
    transaction['date'] = transaction['timestamp']
    transaction['date'] = pd.to_datetime(transaction['date']).dt.date
    conversion_rate['date'] = pd.to_datetime(conversion_rate['date']).dt.date

    # merge 2 dataframe
    final_df = transaction.merge(conversion_rate, how="left", left_on="date", right_on="date")

    # แปลงราคา โดยเอาเครื่องหมาย $ ออกและแปลงให้เป็น float
    final_df["Price"] = final_df.apply(lambda x:x["Price"].replace("$",""), axis=1)
    final_df["Price"] = final_df["Price"].astype(float)

    final_df["THBPrice"] = final_df["Price"] * final_df["conversion_rate"]
    final_df = final_df.drop(["date", "book_id"], axis=1)

    # save to csv
    final_df.to_csv(output_path, index=False)
    print(f"Output to {output_path}")
    print("== End ==")

with DAG(
    "exercise4_final_dag",
    start_date=days_ago(1),
    schedule_interval="@once",
    tags=["workshop"]
) as dag:
    t1 = PythonOperator(
        task_id = "get_data_from_mysql",
        python_callable=get_data_from_mysql,
        op_kwargs={
            "transaction_path" : mysql_output_path,
        },
    )

    t2 = PythonOperator(
        task_id = "get_conversion_rate",
        python_callable=get_conversion_rate,
        op_kwargs={
            "conversion_rate_path": conversion_rate_output_path ,

        },
    )

    t3 = PythonOperator(
        task_id = "merge_data",
        python_callable=merge_data,
        op_kwargs={
            "transaction_path" : mysql_output_path,
            "conversion_rate_path" : conversion_rate_output_path,
            "output_path" : final_output_path,
        },
    )

# task dependencies
    [t1,t2] >> t3
