import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Yes, you successfully deployed the CI/CD pipeline for that!')
    }
