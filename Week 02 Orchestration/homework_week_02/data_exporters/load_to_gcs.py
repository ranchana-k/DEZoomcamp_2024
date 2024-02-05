import pyarrow as pa 
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

service_account_file = os.getenv('SERVICE_ACCOUNT_FILENAME')
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/home/src/homework_week_02/terraform-dezoomcamp-daa7b576c47a.json' #+ os.environ['PROJECT_NAME']+'/' + service_account_file
project_id = os.getenv('GOOGLE_PROJECT_ID')
bucket_name = os.getenv('GCS_BUCKET_NAME')
table_name = 'nyc_taxi_data'
root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    table = pa.Table.from_pandas(data)
    gcs = pa.fs.GcsFileSystem()
    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs)
