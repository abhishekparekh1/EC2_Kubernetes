# DeepOptimization - OptML

This repository is for the course project of EEL6761 - Cloud Computing and Storage at the University of Florida. Our team is T1-DeepOptimization and the contributors are - 

Abhishek "The Snow" Parekh

Ruben "The Hail" Vazquez

Justin "The Rain" Calean

Make sure the EC2 instance has access to S3 with IAM role or AWS Credentials
To do that please check out the Amazon AWS Website

To run the kubernetes cluster first launch an EC2 instance as the master and configure as follows -
Choose Ubuntu 16.04 x64 bit as the AMI
Edit the instance user data in advanced settings and add the contents of master-user-data.sh script
Configure the instance to have public ip address
Configure the security groups to have public access

Please wait upto 15 minutes to allow the cluster to be setup.

Now try to see the public ip it will show the apache server default ubuntu page.
Navigate to <IP>/serviceport.html you will see a port for the kubernetes dashboard of the format 30000
Navigate to <IP>:port to view the kubernetes dashboard
  
  
To add nodes to the kubernetes cluster make a record of the public ip of the master ec2 instance -
Choose Ubuntu 16.04 x64 bit as the AMI
Edit the instance user data in advanced settings and add the contents of slave-user-data.sh script
Change the contents of the ip addresses of the master instance
Configure the instance to have public ip address
Configure the security groups to have public access

This will add the instance to the cluster.

This can also be done by creating a launch configuration and using it to form an Autoscaling group.
The scaling policies will trigger new nodes to join the cluster whenever the threshold is reached.

To run the code copy and paste the yaml file in the kubernetes dashboard page after hitting +create on the top right corner
The YAML file will create a job for the code and this job will run within a docker container in a kubernetes pod and push the end results to s3 bucket

You can view this results in the S3.



