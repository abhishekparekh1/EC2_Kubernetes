import boto3

s3 = boto3.resource('s3')
s3.Object('my-unique-fucking1-test-bucket', 'hello.txt').put(Body=open('/home/ubuntu/tmp/hello.txt', 'rb'))
