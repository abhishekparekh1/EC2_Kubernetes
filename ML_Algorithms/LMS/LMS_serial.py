import sys
import os

hyper_param_filename = sys.argv[1]
hyper_param_fp = open(hyper_param_filename, 'r')

for line in hyper_param_fp:
	os.system('python LMS_driver.py ' + line[:-1] + ' SN_m_tot_V2.0.csv 1 0.10 2')
