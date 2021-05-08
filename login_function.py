import boto3
import os
from boto3.dynamodb.conditions import Key

DYNAMO_BD = os.environ['DYNAMO_BD']

def get_item():
    dynamo_db = boto3.resource('dynamodb')

    table = dynamo_db.Table(dynamo_table)

    response = table.get_item(
        Key={
            'dni':'46513503'
        }
    )

    return response["Items"][0] if any(response["Items"]) else None