# install AWS CLI
# verify in cmd: `aws --version`
"""
AWS Cheat Sheet

EC2 - Elastic Compute Cloud, virtual servers (machines) in the cloud
S3 - Simple Storage Service, object storage service (files, images, backups, etc.)
IAM - Identity and Access Management, manage users, roles, and permissions
VPC - Virtual Private Cloud, isolated network environment in the cloud
Boto3 - AWS SDK for Python, interact with AWS services programmatically
SQS - Simple Queue Service, message queuing service for decoupling components
ECS - Elastic Container Service, container orchestration service
Cognito - User authentication and management service
DynamoDB - NoSQL database service

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