from airflow.decorators import dag, task
from datetime import datetime
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator


@dag(
    start_date=datetime(2024, 8, 2),
    schedule=None,
    catchup=False,
    tags=['retail'],
)
def retail():
    upload_csv_to_gcs = LocalFilesystemToGCSOperator(
        task_id='upload_csv_to_gcs',
        src='include/dataset/online_retail.csv',
        dst='raw/online_retail.csv',
        bucket='marclamberti_online_retail',
        gcp_conn_id='gcp',
        mime_type='text/csv',
    )


retail()
