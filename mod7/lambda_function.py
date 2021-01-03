# Copyright 2021 Amazon Web Services, Inc. or its affiliates. All rights reserved.
'''
  eventオブジェクトからバケットとオブジェクトの情報を取得して表示
'''
import json
import urllib.parse
import boto3

print('Loading function')

#s3 = boto3.client('s3')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object infor from the event 
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        print("Bucket=" + bucket + " : Object= " + key)
        #response = s3.get_object(Bucket=bucket, Key=key)
        #print("CONTENT TYPE: " + response['ContentType'])
        return key
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e


