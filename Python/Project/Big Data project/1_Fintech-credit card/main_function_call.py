# standard imports 
import findspark            # used to locate & initialize spark environmemt
import pg8000               # a PostgresSQL adapter for Python
findspark.init()
import os                   # to interact with os
import boto3                # the AWS services SDK for python 
import ssl                  # provides SSL support for secure connections
import logging              # enable logging capabilities in program
import sys                  # provides access to system specific parameters & functions
import datetime


from enum import Enum
from pyspark.context import SparkContext
from pyspark.sql import SparkSession,Window
from pyspark.sql import functions as f
from pyspark.sql import *
from pyspark.sql.types import *

# custom/local imports
from rscycle_module import rscycle_lfgrsudf
from rscycle_module.db_utility import rscycle_db_utility
from rscycle_module.aws_utility import rscycle_aws_utility
from rscycle_module.spark_utility import rscycle_spark_config

postgresql = BASE_DIR + "\src\postgresql-42.5.4.jar"
spark = (
    SparkSession.
    builder.appName("Python Spark SQL basic example")
    .config("spark.jars", postgresql)
    .getOrCreate()
)
print("Spark session established successfully")

########################################################################
args = {}
args["src_bucket_name"] = BASE_DIR + "\\input\\"
args["process_bucket_name"] = BASE_DIR + "\\processing\\"
args["dst_bucket_name"] = BASE_DIR + "\\output\\"

args["cert_file"] = "rds-ca-rsa2048-g1.pem"
args["conf_path"] = "cert_file"
args["conf_bucketname"] = "cert_file"

args["secret_name"] = "lfgapp/rscclrycle/rds/glue"
args["region_name"] = "us-east-1"
args["global_properties_json"] = BASE_DIR + "\\lib\\lfgapp-rpsdiradmn-rscyle-lfgrsudf.json"
args["get_job_json"] = BASE_DIR + "\\lib\\lfgapp-rpsdiradmn-rscyle-webcon.json"
args["card_input_json"] = BASE_DIR + "\\lib\\cardinput.json"

#import findspark   
############################################################################

env = "local"
rscycle = rscycle_lfgrsudf.Baseparam(args, env)
connection_str = rscycle.get_key_for_database_connection()
property_file = rscycle.get_db_properties()

#rstable_df = rscycle_db_utility.read_table(spark, connection_str, "rsdisex")
#rstable_df.show(1)
#df,df_header_tail = rscycle.rsstadld_load_method(spark)
#rscycle.rsstadld_load_method2(spark)
#rscycle.toolpv_transform_method(spark)

rscycle.webcon_method(spark)

#rscycle.pbiin2_method(spark)
#rscycle.rsstadld_validation_method(spark, df,df_header_tail)
#rscycle.rsstadhd_method(spark)
#rscycle.rsstadup_method(spark)
#rscycle.rsstaded_load_method(spark)
# print("start_second")
# rstrnp2_df=rscycle.rstrnup_out( spark, df_rstrnup)
# print("rstrnp2_df")
# rstrnp2_df.show(1)
# rscycle.rsup2l_method( spark, rstrnp2_df, job_run_id)