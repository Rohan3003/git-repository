from enum import Enum
import boto3
import json
import logging
from configparser import ConfigParser, RawConfigParser
from string import Template
from datetime import datetime
import botocore

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def split_s3_path(s3_path):
    """splitting the s3 path for boto3 read"""
    path_parts = s3_path.replace("s3://", "").split("/")
    bucket = path_parts.pop(0)
    key = "/".join(path_parts)
    return bucket, key


def get_mapplet_conf_details(mapplet_config_path: str, env=None):
    """Getting the Job Config Object File Details Based on the Section"""
    logger.info("Creating Mapplet Configuration Object")
    if env is None:
        s3_boto = boto3.client("s3")
        bucket, key = split_s3_path(mapplet_config_path)
        obj = s3_boto.get_object(Bucket=bucket, Key=key)
        config = RawConfigParser()
        config.read_string(obj["Body"].read().decode())
    else:
        config = RawConfigParser()
        config.read(mapplet_config_path)
    return config


def get_map_details_json(mapplet_config_path: str, env=None):
    """Getting the Job Config Object File Details Based on the Section"""
    try:
        if env is None:
            s3_boto = boto3.client("s3")
            bucket, key = split_s3_path(mapplet_config_path)
            obj = s3_boto.get_object(Bucket=bucket, Key=key)
            file_content = obj["Body"].read().decode()
            json_content = json.loads(file_content)
            logger.info("Creating get_map_details_json")
        else:
            # Opening JSON file
            open_file = open(mapplet_config_path)
            json_content = json.load(open_file)
        return json_content
    except Exception as error:
        logger.error(f"Error occurred in loading the config file - {error}")
        raise error


def download_from_s3(download_file, s3_bucket, region_name, obj):
    """
    Download config file from s3
    Common function to get file from S3
    """
    try:
        s3 = boto3.client("s3", region_name=region_name)
        ingest_key = obj + download_file
        s3.download_file(s3_bucket, ingest_key, download_file)
        print("Config Download Completed")
        return True
    except Exception as error:
        logger.error(f"Error occurred in downloading the config file - {error}")
        raise error


def get_config(download_file, s3_bucket, region_name, object, strictflg=True):
    # read the config_file from the s3 config file
    try:
        flag = False
        flag = download_from_s3(download_file, s3_bucket, region_name, object)
        if flag:
            # Read the credentials from the config file
            with open(download_file, "r") as config_file:
                jsonprop = json.load(config_file, strict=strictflg)
            return jsonprop

    except Exception as error:
        logger.error(f"Error occurred in reading the config file - {error}")
        raise error


class NotificationParameters:
    """Notification Parameters for Email Notification"""

    notification_type = str()
    env = str()
    process = str()
    message = str()
    aws_account_number = str()


class NotificationType(Enum):
    """Notification Parameters for Email Notification"""

    SUCCESS = 1
    FAILURE = 2
    REPORT = 3
    WARNING = 4


class Notification:
    """Notification Parameters for Email Notification"""

    def __init__(self):
        global parser
        parser = ConfigParser()
        parser.read("notification.properties")

    def send_email_via_sns(self, notification_parameter: NotificationParameters):
        """Send email notification via SNS"""
        try:
            sns_arn = parser.get(
                notification_parameter.notification_type, "sns_arn"
            ).format(notification_parameter.aws_account_number)
            temp_obj = Template(
                            parser.get(notification_parameter.notification_type, "subject")
            )
            subject = temp_obj.substitute(
                ENV=notification_parameter.env,
                Process=notification_parameter.process,
                CurrentDate=datetime.now().strftime("%d/%m/%Y"),
            )
            client = boto3.client("sns")
            client.publish(
                TargetArn=sns_arn,
                Message=notification_parameter.message,
                Subject=str(subject),
            )

        except Exception as exception:
            logger.error(exception)
            raise exception("Exception in send_email_via_sns method")


if __name__ == "__main__":
    notifyParameters = NotificationParameters()
    notifyParameters.env = "QA"
    notifyParameters.notification_type = NotificationType.SUCCESS.name
    notifyParameters.process = "My First Message"
    notifyParameters.message = "Hellow How a"
    notifyParameters.aws_account_number = "434543452053"
    Notification().send_email_via_sns(notifyParameters)