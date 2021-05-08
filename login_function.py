import boto3
import os
from boto3.dynamodb.conditions import Key

# Hola a todos companeros, Carlos es el mejor profe de AWS del Mundo

DYNAMO_BD = os.environ['DYNAMO_BD']

class DynamoAccessor:
    def __init__(self, dynamo_table):
        dynamo_db = boto3.resource('dynamodb')
        self.table = dynamo_db.Table(dynamo_table)

    def get_data_from_dynamo(self, dni, password):
        response = self.table.query(KeyConditionExpression=Key('dni').eq(dni) && Key('password').eq(password))
        return response["Items"][0] if any(response["Items"]) else None

def lambda_handler(event, context):
    dynamo_backend = DynamoAccessor(DYNAMO_BD)
    db_element = dynamo_backend.get_data_from_dynamo(event['dni'])
    return db_element

