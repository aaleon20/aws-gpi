import boto3
import os
from boto3.dynamodb.conditions import Key, Attr

DYNAMO_BD = os.environ['DYNAMO_BD']

class DynamoAccessor:
    def __init__(self, dynamo_table):
        dynamo_db = boto3.resource('dynamodb')
        self.table = dynamo_db.Table(dynamo_table)

    def get_data_from_dynamo(self, dni):
        response = self.table.update_item(
            Key={'dni': dni},
            UpdateExpression="set evaluate=:evaluate",
            ExpressionAttributeValues={
                ':evaluate': 1,
            },
            ReturnValues="UPDATED_NEW"
        )
        return response['Attributes'] if any(response['Attributes']) else None

def lambda_handler(event, context):
    dynamo_backend = DynamoAccessor(DYNAMO_BD)
    db_element = dynamo_backend.get_data_from_dynamo(event['dni'])
    return db_element