FROM python:3.6

WORKDIR /app

RUN apt-get update; \
        apt-get install python3-pip git-core -y; \
        pip3 install numpy matplotlib boto3 tensorflow; \
        git clone https://github.com/abhishekparekh1/EC2_Kubernetes/

CMD ["python"]
