# WORKSHOP: DATA PIPELINE
> This workshop is an example of processing data pipeline on Google Cloud Platform.

## Contents

- [About The Project](#About-The-Project)
- [Technologies Used](#Technologies-Used)
- [Getting Started](#Getting-Started)
  - [Installation](#Installation)
- [Workshop](#Workshop)
    
## About The Project
This workshop showcases processing data pipelines on Google Cloud Platform. It covers basic pipelines like fan-in and fan-out patterns, and includes a mini-project that applies these concepts in practice. 

## Technologies Used
- Python
- Google Cloud Storage
- Google BigQuery
- Apache Airflow
- Google Cloud Composer

## Getting Started


### Installation
- Create a Cloud Composer Cluster to run Apache Airflow
  - https://console.cloud.google.com/

- Install Python packages in Airflow
  - https://console.cloud.google.com/composer/environments
  - packeage name : pymysql, requests, pandas
- Create a dataset in BigQuery
  - https://cloud.google.com/bigquery/docs/datasets
- Create MySQL connection 
  - [https://airflow.apache.org/docs/apache-airflow](#https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html#editing-a-connection-with-the-ui)


### Workshop
- [Workshop1](#https://github.com/Tonson-UB/demo-workshop-datapipeline/blob/main/workshop_datapipeline/ws_exercise1.py)

- [Workshop1 taskflow](#https://github.com/Tonson-UB/demo-workshop-datapipeline/blob/main/workshop_datapipeline/ws_exercise1_taskflow.py)

- [Workshop2 (Fan-out Pipeline)](#https://github.com/Tonson-UB/demo-workshop-datapipeline/blob/main/workshop_datapipeline/ws_exercise2.py)

- [Workshop2 taskflow (Fan-out Pipeline)](#https://github.com/Tonson-UB/demo-workshop-datapipeline/blob/main/workshop_datapipeline/ws_exercise2_taskflow.py)

- [Workshop3 (Fan-in Pipeline)](#https://github.com/Tonson-UB/demo-workshop-datapipeline/blob/main/workshop_datapipeline/ws_exercise3.py)

- [Workshop data pipeline](#https://github.com/Tonson-UB/demo-workshop-datapipeline/blob/main/demo_datapipeline.py)

- [Workshop data pipeline to bigquery](#https://github.com/Tonson-UB/demo-workshop-datapipeline/blob/main/demo_datapipeline_to_bigquery.py)

- [Workshop data pipeline to bigquery with schema](#https://github.com/Tonson-UB/demo-workshop-datapipeline/blob/main/demo_datapipeline_gcs_to_bq_w_schema.py)
