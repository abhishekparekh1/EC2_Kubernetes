#!/bin/bash
sudo su <<EOF
git clone https://github.com/abhishekparekh1/EC2_Kubernetes.git
source EC2_Kubernetes/kubeadm_ec2_master.sh
EOF
