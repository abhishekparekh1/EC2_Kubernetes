import sys
import os
import time

hyper_param_filename = sys.argv[1]
hyper_param_fp = open(hyper_param_filename, 'r')

yaml_templ_filename = sys.argv[2]
yaml_templ_fp = open(yaml_templ_filename, 'r')

yaml_deploy_filename = 'Job.yaml'
yaml_deploy_fp = open(yaml_deploy_filename, 'w')

#start_time = time.time()

delete_jobs = int(sys.argv[3])
how_many = int(sys.argv[4])

for i,line in enumerate(hyper_param_fp,1):

	if i > how_many:
		continue

	for yaml_line in yaml_templ_fp:
		temp_line = yaml_line
		if '$1' in temp_line:
			temp_line = temp_line.replace('$1',line.split()[0])
		if '$2' in temp_line:
			temp_line = temp_line.replace('$2',line.split()[1])
		if '$3' in temp_line:
			temp_line = temp_line.replace('$3',str(i))
		yaml_deploy_fp.write(temp_line)

	yaml_deploy_fp.flush()

	yaml_templ_fp.seek(0)
	yaml_deploy_fp.seek(0)

	#18.225.22.214

	if not delete_jobs:
		os.system('kubectl create -f ' + yaml_deploy_filename)
	else:
		os.system('kubectl delete -f ' + yaml_deploy_filename)


yaml_templ_fp.close()
yaml_deploy_fp.close()
hyper_param_fp.close()

#total_time = time.time() - start_time

#time_fp = open('time_elapsed.csv', 'w+')
#time_fp.write(str(total_time) + '\n')
#time_fp.close()

#os.system('cat *.txt > LMS_all_params.csv')
