"""
UDF function class which contain all class variable and use case related function
"""
import os
import shutil
import sys
from datetime import *

from pyspark.sql.functions import (
    concat,
    col,
    udf,
    when,
    rpad,
    row_number,
    to_timestamp,
    to_date,
    length,
    lit,
    max,
    sum,
    first,
    concat_ws,
    ltrim,
    substring,
    expr,
    trim,
    monotonically_increasing_id,
    format_number,
    asc,
    count,
    collect_list
)

from pyspark.sql.types import *
from pyspark.sql import functions as f
from pyspark.sql import *

from rscycle_module.db_utility import rscycle_db_utility
from rscycle_module.spark_utility import rscycle_spark_config, rscycle_logger_utility
from rscycle_module.aws_utility.rscycle_aws_utility import get_map_details_json

logger = rscycle_logger_utility.get_logger()

class Baseparam:
    
    """
    Base param class
    """

    def __init__(self, args, env=None):
        self.source_path = args["src_bucket_name"]
        self.process_path = args["process_bucket_name"]
        self.destination_path = args["dst_bucket_name"]
        self.secret_name = args["secret_name"]
        self.region = args["region_name"]
        self.get_job_json = args["get_job_json"]
        self.global_properties_json = args["global_properties_json"]
        self.cert_file = args["cert_file"]
        self.conf_path = args["conf_path"]
        self.conf_bucketname = args["conf_bucketname"]
        self.card_input_json = args["card_input_json"]
        self.get_config_json = get_map_details_json(self.global_properties_json, env)
        self.get_job_json = get_map_details_json(self.get_job_json, env)
        self.get_card_input_json = get_map_details_json(self.card_input_json, env)
        if env is not None:
            self.env = env
        else:
            self.env = None