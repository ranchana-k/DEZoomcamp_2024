# Homework Week 02
For week 2 in Data Engineering Zoomcamp by DataTalks.Club, I have learend to create a data pipeline using Mage.ai which is an integrated ETL framework.

## Objective
The objective of this ETL pipeline is to load data of NYC green taxi data from github release from October - December 2020 using API, have some data wrangling and then export to two sources, PostgresQL and Google Cloud Storage (in form of parguet files partitioned by date).
<p align="center">
  <img src="https://i.postimg.cc/7PTy4Rpg/etl-tree.png" alt="Pipeline Image">
</p>

## Result
- Postgres
[![postgresql-screen.png](https://i.postimg.cc/NjVqV9tk/postgresql-screen.png)](https://postimg.cc/mPQ51rtP)
- Google Cloud Storage
[![gcs-bucket.png](https://i.postimg.cc/JzDL74Y4/gcs-bucket.png)](https://postimg.cc/CRgtmYVW)

## Prerequistions
- Docker
- PosgresQL on local host
- Configured `.env` file 
- Google Service Account with read and write access to Google Cloud Storage (put in the mage project folder)
- Google Cloud Storage bucket with a global unique bucket name 

## Environment Variables
- PROJECT_NAME
- POSTGRES_DBNAME
- POSTGRES_SCHEMA
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_HOST
- POSTGRES_PORT
- GCS_BUCKET_NAME
- SERVICE_ACCOUNT_FILENAME
- GOOGLE_PROJECT_ID

## How to run a project
- Clone this github repo
- Run a docker command `docker-compose build`
- Run a docker command `docker-compose up`
- Open Mage pipeline in the project on browser at `localhost:6789`. The pipeline name is `green_taxi_etl`