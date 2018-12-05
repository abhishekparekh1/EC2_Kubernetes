import sys
import os
import time

hyper_param_filename = sys.argv[1]
hyper_param_fp = open(hyper_param_filename, 'r')

start_time = time.time()

for line in hyper_param_fp:
	os.system('python ANN_TF_Driver.py --learning_rate ' + line.split()[0] + ' --network_size ' + line.split()[1] + ' --DEBUG 2')

total_time = time.time() - start_time

time_fp = open('time_elapsed.csv', 'w+')
time_fp.write(str(total_time) + '\n')
time_fp.close()

os.system('cat *.txt > ANN_all_params.csv')
