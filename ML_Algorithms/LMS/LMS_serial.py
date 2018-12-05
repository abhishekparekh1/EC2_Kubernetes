import sys
import os
import time

hyper_param_filename = sys.argv[1]
hyper_param_fp = open(hyper_param_filename, 'r')

start_time = time.time()

for line in hyper_param_fp:
	os.system('python LMS_driver.py ' + line[:-1] + ' SN_m_tot_V2.0.csv 1 0.10 1')

total_time = time.time() - start_time

time_fp = open('time_elapsed.csv', 'w+')
time_fp.write(str(total_time) + '\n')
time_fp.close()

os.system('cat *.txt > LMS_all_params.csv')
