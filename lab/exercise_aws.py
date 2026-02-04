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


