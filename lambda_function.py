import json
import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    
    username = event['username']
    email = event['email']
    password = event['password']
    userdetails = event['userdetails']
    
    response = dynamodb.put_item(TableName='nico-lambda-table', Item={'username':{'S':username},'email':{'S':email},'password':{'S':password},'userdetails':{'S':userdetails}})
    
    print(email)