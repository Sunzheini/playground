"""
Here we use the AWS SDK to invoke a Lambda function named `ReportGenerator`.
https://8s57u364el.execute-api.eu-central-1.amazonaws.com
"""
import os
import json

from dotenv import load_dotenv
import boto3


load_dotenv()


access_key_id=os.getenv("AWS_ACCESS_KEY_ID", ""),
secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", ""),
region=os.getenv("AWS_REGION_NAME", "eu-central-1")
s3_bucket_name=os.getenv("S3_BUCKET_NAME", "")


