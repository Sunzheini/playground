"""
Here we invoke a lambda function named `ReportGenerator` in AWS.
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


lambda_client = boto3.client('lambda',
    region_name=region,
)


def invoke_report_generator():
    """Invoke your ReportGenerator Lambda"""

    payload = {
        'trigger_source': 'python_script',
        'custom_data': {
            'user': 'pycharm_user',
            'purpose': 'test_lambda_invocation'
        }
    }

    try:
        print(" Invoking ReportGenerator Lambda...")

        # Invoke the Lambda
        response = lambda_client.invoke(
            FunctionName='ReportGenerator',
            InvocationType='RequestResponse',  # Wait for response
            Payload=json.dumps(payload)
        )

        response_payload = json.loads(response['Payload'].read())

        print(" Lambda invoked successfully!")
        print(f"   Status: {response_payload.get('status', 'unknown')}")
        print(f"   Message: {response_payload.get('message', 'No message')}")

        if 'file_name' in response_payload:
            print(f"   File to be created: {response_payload['file_name']}")

        print(f"\n Response details:")
        print(f"   Status Code: {response['StatusCode']}")
        print(f"   Executed Version: {response.get('ExecutedVersion', '$LATEST')}")

        return response_payload

    except Exception as e:
        print(f" Error invoking Lambda: {str(e)}")
        return None


# Run it
if __name__ == "__main__":
    result = invoke_report_generator()

    if result and result.get('status') == 'success':
        print("\n Success! Check your S3 bucket in a few seconds:")
