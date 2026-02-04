"""
# install AWS CLI
# verify in cmd: `aws --version`

# Your local tech stack substitute
Local Service          -> AWS Service
-------------          -> -----------
FastAPI (local)        -> API Gateway + ECS
SQLite/PostgreSQL      -> DynamoDB
Redis/RabbitMQ         -> SQS
Local file storage     -> S3
Local authentication   -> Cognito
Docker Compose         -> ECS Fargate
"""
import os

from dotenv import load_dotenv
import boto3


load_dotenv()


access_key_id=os.getenv("AWS_ACCESS_KEY_ID", ""),
secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", ""),
region=os.getenv("AWS_REGION_NAME", "eu-central-1")
s3_bucket_name=os.getenv("S3_BUCKET_NAME", "")


lambda_client = boto3.client('lambda',
    region_name='us-east-1',
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY'
)


