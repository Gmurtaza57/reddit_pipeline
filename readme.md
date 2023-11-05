# <AWS Based Reddit ETL Pipeline>

## Project Overview
This repository contains the ETL pipeline for aggregating data from the "MachineLearning" subreddit. The pipeline is designed to extract top posts, transform the data for analytical readiness, and load it into AWS S3, with further processing in AWS services and visualization in Tableau.

### Tools & Technologies
- Apache Airflow
- Python
- AWS Services:
  - S3
  - Redshift
  - Athena
  - Glue
- Tableau for Visualization
- PostgreSQL
- Redis
- Docker
- PRAW (Python Reddit API Wrapper)
- Pandas and NumPy for data manipulation
- Spark for large-scale data processing

## Data Extraction
The `RedditExtractor` DAG connects to Reddit using PRAW, extracts top posts from the "MachineLearning" subreddit, and uploads the raw data to an S3 bucket daily.

## Data Transformation
Transformation scripts use Pandas and NumPy to clean the data and prepare it for loading. This includes timestamp conversions, boolean data type handling, and the creation of additional analytical fields.

## AWS S3 Integration
Raw data is structured and uploaded to an AWS S3 bucket using S3FS, ensuring data is partitioned and organized efficiently.

## Automation & Orchestration
An Airflow DAG manages the workflow, automating the ETL process on a daily schedule using Redis and PostgreSQL for task coordination.

## Data Processing in AWS
AWS Glue is utilized for daily data detection in S3, quality checks, deduplication, and cleansing operations. The processed data is categorized by ingestion day and stored in a transformed S3 folder.

## AWS Processing and Transformation
The Glue Crawler, scheduled to run post the ETL job, updates the AWS Glue Data Catalog with the new schema and table definitions to accommodate the latest data.

## ETL Scheduling
ETL jobs are scheduled to run at 1 AM, with the Glue Crawler following at 2 AM to ensure data is processed, cataloged, and ready for querying.

## Data Validation and De-duplication
An additional data validation step ensures no duplicates exist between new and existing datasets within the transformed S3 data.

## Version Control
All DAGs and AWS pipeline configurations are version-controlled on GitHub, providing transparency and history for all changes and executions.

