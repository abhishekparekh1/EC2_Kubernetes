#!/bin/bash
sudo su <<EOF
git clone https://github.com/abhishekparekh1/EC2_Kubernetes.git
bash EC2_Kubernetes/apache-server.sh
source EC2_Kubernetes/kubeadm_ec2_master.sh
cp EC2_Kubernetes/kubeadm_join.sh /var/www/html/
tail -n 2 /var/www/html/jointoken.html >> /var/www/html/kubeadm_join.sh
cp EC2_Kubernetes/slave_script.sh /var/www/html/
EOF
