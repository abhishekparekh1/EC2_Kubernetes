import boto3

s3 = boto3.resource('s3')
s3.create_bucket(Bucket='my-unique-fucking1-test-bucket',CreateBucketConfiguration={
    'LocationConstraint': 'us-east-2'})
