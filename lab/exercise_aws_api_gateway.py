"""
Here we use the AWS SDK to invoke a Lambda function named `ReportGenerator`.
"""
import os
import json

import requests
from dotenv import load_dotenv


load_dotenv()


access_key_id=os.getenv("AWS_ACCESS_KEY_ID", ""),
secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", ""),
region=os.getenv("AWS_REGION_NAME", "eu-central-1")
s3_bucket_name=os.getenv("S3_BUCKET_NAME", "")


# API Gateway endpoint
API_URL = "https://8s57u364el.execute-api.eu-central-1.amazonaws.com/generate-report"


def trigger_via_api():
    """Trigger the Lambda chain via API Gateway"""

    # Optional payload
    payload = {
        "message": "Hello from Python via API Gateway!",
        "api_test": True
    }

    try:
        print(f"Calling API Gateway: {API_URL}")

        # Make POST request
        response = requests.post(
            API_URL,
            json=payload,  # Sends as JSON
            headers={"Content-Type": "application/json"}
        )

        print(f"API Response Status: {response.status_code}")

        if response.status_code == 200:
            result = response.json()
            print(f"📋 Response: {json.dumps(result, indent=2)}")

            if result.get('status') == 'success':
                print("\nSuccess! Check the S3 bucket for the new report.")
            return result
        else:
            print(f"Error: {response.text}")
            return None

    except Exception as e:
        print(f"API Call Failed: {str(e)}")
        return None


if __name__ == "__main__":
    trigger_via_api()
