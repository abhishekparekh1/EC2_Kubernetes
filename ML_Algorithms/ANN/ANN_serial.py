import sys
import os

hyper_param_filename = sys.argv[1]
hyper_param_fp = open(hyper_param_filename, 'r')

for line in hyper_param_fp:
	os.system('python ANN_TF_Driver.py --learning_rate ' + line.split()[0] + ' --network_size ' + line.split()[1] + ' --DEBUG 2')
