import boto3
import json

lambda_client = boto3.client('lambda')

def lambda_handler(event, context):
    response = lambda_client.invoke(
        FunctionName='lambda_function.py',
        InvocationType='RequestResponse',
        Payload=json.dumps(event)
    )
    
    return {
        'statusCode': 200,
        'body': response['Payload'].read().decode('utf-8')
    }
