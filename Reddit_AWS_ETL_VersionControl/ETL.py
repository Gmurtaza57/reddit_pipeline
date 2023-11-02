import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import gs_null_rows
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import functions as SqlFuncs
import datetime


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)


# Construct the file path dynamically
today = datetime.date.today()
filename = f"reddit_{today.strftime('%Y%m%d')}.csv"  # Format the date to match your file naming pattern
path = f"s3://portfolio-reddit-pipeline/raw/{filename}"
# Script generated for node Amazon S3

AmazonS3_node1698926137483 = glueContext.create_dynamic_frame.from_options(
    format_options={
        "quoteChar": '"',
        "withHeader": True,
        "separator": ",",
        "optimizePerformance": False,
    },
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": [path],
        "recurse": True,
    },
    transformation_ctx="AmazonS3_node1698926137483",
)

# Script generated for node Drop Duplicates
DropDuplicates_node1698956233301 = DynamicFrame.fromDF(
    AmazonS3_node1698926137483.toDF().dropDuplicates(),
    glueContext,
    "DropDuplicates_node1698956233301",
)

# Script generated for node Remove Null Rows
RemoveNullRows_node1698956260539 = DropDuplicates_node1698956233301.gs_null_rows()

# Construct the output path dynamically
output_folder = datetime.date.today().strftime('%Y%m%d')  # Format the date to match your desired folder naming pattern
output_path = f"s3://portfolio-reddit-pipeline/transformed/{output_folder}/"
# Script generated for node Amazon S3
AmazonS3_node1698926164341 = glueContext.write_dynamic_frame.from_options(
    frame=RemoveNullRows_node1698956260539,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": output_path,
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="AmazonS3_node1698926164341",
)

job.commit()
