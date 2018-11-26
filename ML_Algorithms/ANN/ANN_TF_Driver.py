
# coding: utf-8

# In[1]:



import argparse
import sys
import ANN_TF_Function
import boto3

# In[2]:



CLI=argparse.ArgumentParser()

CLI.add_argument(
    "--DEBUG",
    nargs = 1,
    type = int,
    default = 0
)

CLI.add_argument(
    "--network_size",
    nargs = "*",
    type = int,
    default = [128]
)

CLI.add_argument(
    "--learning_rate",
    nargs = 1,
    type = float,
    default = 0.1
)

args = CLI.parse_args()

# Driver
DEBUG = args.DEBUG[0]
network_size = args.network_size
learning_rate = args.learning_rate[0]

train_data, train_desired, test_data, test_desired = ANN_TF_Function.generate_data(DEBUG)
model = ANN_TF_Function.initialization(train_data, train_desired, network_size, DEBUG)
model = ANN_TF_Function.train(train_data, train_desired, learning_rate, model, DEBUG)
error = ANN_TF_Function.test_error(test_data, test_desired, model, DEBUG)

output_name = sys.argv[0]
output_name = output_name[:-3]

for layer_size in network_size:
    output_name = output_name + '-' + str(layer_size)
    
output_name = output_name + '-' + str(learning_rate).replace('.','_')

output_fp = open(output_name + '.txt', 'w+')
output_fp.write(str(error))
output_fp.close()

s3 = boto3.resource('s3')
s3.Object('deepoptimization-uf-optml-bucket', output_name + '.txt').put(Body=open(output_name + '.txt', 'rb'))
