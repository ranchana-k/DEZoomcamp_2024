# Homework Week 03
For Week 3, we learned about data warehouse, creating a table from external sources, table optimization by partitioning and clustering, and Bigquery ML. The query used to answer the homework this week are as followings:


```
-- Create an external table from files in GCS
CREATE OR REPLACE EXTERNAL TABLE `nyc_taxi_data.external_green_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://mage-zoomcamp-2024/green_taxi/green_tripdata_2022-*.parquet']
);

-- Create a non partitioned table from external table
CREATE OR REPLACE TABLE nyc_taxi_data.green_tripdata_nonpartitioned AS
SELECT * FROM nyc_taxi_data.external_green_tripdata;

-- Question 1 -- count records
SELECT COUNT(*)
FROM `nyc_taxi_data.external_green_tripdata`

-- Question 2 
-- compared estimated bytes that the query will process when run between an external table and materialized table

-- An external table has estimated bytes of 0 MB

SELECT COUNT(DISTINCT PULocationID)
from `nyc_taxi_data.external_green_tripdata`

-- A materialized table has estimated bytes of 6.41 MB
SELECT COUNT(DISTINCT PULocationID)
from `nyc_taxi_data.green_tripdata_nonpartitioned`

-- Question 3 -- count records with fare_amount equal to 0
SELECT COUNT(*)
from `nyc_taxi_data.external_green_tripdata` 
where fare_amount = 0

-- Question 4
-- Create a new table with partitioning and clustering strategy in case your queries will always order the results by PUlocationID and filter based on lpep_pickup_datetime.

CREATE OR REPLACE TABLE nyc_taxi_data.green_tripdata_partitoned
PARTITION BY
  DATE(lpep_pickup_datetime) 
  CLUSTER BY PULocationID AS
SELECT * FROM nyc_taxi_data.external_green_tripdata;

-- Question 5
-- Query to check estimated bytes to be processed to compared between non-partitioned and partitioned tables
-- Non-partitioned 12.82 MB
SELECT distinct(PULocationID)
FROM `nyc_taxi_data.green_tripdata_nonpartitioned`
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30'

-- Partitioned 1.12 MB
SELECT distinct(PULocationID)
FROM `nyc_taxi_data.green_tripdata_partitoned`
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30'
```
