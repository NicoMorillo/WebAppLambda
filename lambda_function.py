import json
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('nico-lambda-table')

def lambda_handler(event, context):
    email = event['email']
    username = event['username']
    password = event['password']
    userdetails = event['userdetails']

    response = table.put_item(
        Item={
            'email': email,
            'username': username,
            'password': password,
            'userdetails': userdetails
        })
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from lambda, ' + username)
    }