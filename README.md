# WebAppLambda

Deploy a Simple Web Application in Lambda

First fase:
    Create all resources using AWS Consol

Second fase:
    Create a CloudFormation template to deploy


Resume idea:

    Build a Serverless Web Application using:
    
     - S3 to host a website
     - AWS Lambda as a backend
     - REST API using API Gateway
     - DynamoDB as database


S3

    - All public S3 Bucket
    - Allowing as well GetObject
    {
    "Version": "2012-10-17",
    "Id": "Policy1573139724816",
    "Statement": [
        {
            "Sid": "Stmt1573139723269",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3::: your bucket name /*"
        }
    ]
}
    - Static Website Hosting

IAM Role

    - AWS Service --> Lambda
    - Policy: Lambda Basic Execution Role
    - Policy: add inline policy to have access to DynamoDB tables *PutItem; Resoucers at the moment All resouces, to get access to all the tables created in the account, if you select Specific Resource you will attacht the table arn.

DynamoDB

    - Create a DynamoDB Table: table name and partition key
    - Create create items and add the fields necessaries in your db **** 
    Added by Json, givin empty space into primary key

Lambda

    - Create a Lamdbda function
    - Add Role created before
    - Add code to the lambda function (boto3)

API Gateway

    - Create a REST API
    - Add POST option with the lambda function
    - Enable CORS -- SECURITY -- 
    - Test
    - Deploy de API

Connect web with API ---- PROBLEM!
    -Create a file to add a variable in JavaScript
var api = "https://hed0mf6xyc.execute-api.eu-central-1.amazonaws.com/dev"