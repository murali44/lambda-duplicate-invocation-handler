import boto3
import os
import time

from boto3.dynamodb.conditions import Key

def handler(event, context):
    # In production, you'll want to implement the following as a
    # function decorator.
    lambda_name = 'handler'
    event_id = event['requestContext']['requestId']
    key = lambda_name + '#' + event_id

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['EVENTS_TABLE'])

    # Check if event was already received.
    result = table.get_item(Key={'LambdaName#EventID': key})
    if 'Item' in result:
        msg = "Duplicate event. Ignoring this invocation."
        print(msg)
        return {"statusCode": 200, "body": msg}

    # Add event to Events table.
    item = {
        'LambdaName#EventID': key,
        'Expires': int(time.time()) + 3600 # Expire the entry in 1 hour
        }
    table.put_item(Item=item)

    return {"statusCode": 200, "body": "Successfully processed the event."}