import boto3
import os
from boto3.dynamodb.conditions import Key

DYNAMO_BD = os.environ['DYNAMO_BD']

def get_login(dni, password, dynamodb=None):
    if not dynamodb:
       dynamo_db = boto3.resource('dynamodb') 

    table = dynamo_db.Table(dynamo_table)

    try:
        response = self.table.get_item(Key={'dni':dni, 'password':password})
    except ClientError as e:
        print(e.response['Error']['Message']
    else
        return response['Item']
