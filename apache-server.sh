#!/bin/bash
sudo apt-get update
sudo apt-get install -y awscli
sudo apt-get install -y apache2
systemctl start apache2
