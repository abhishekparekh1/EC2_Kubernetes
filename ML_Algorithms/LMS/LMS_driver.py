import sys
import LMS
import boto3

DEBUG = int(sys.argv[5])

mu = 0
sigma = 1
percent_test = float(sys.argv[4])
filter_size = 5
use_real_data = int(sys.argv[3])
learning_step = float(sys.argv[1])
filename = sys.argv[2]

train_data, train_desired, test_data, test_desired = LMS.generate_data(mu, sigma, filter_size, use_real_data, filename, percent_test, DEBUG)
weights = LMS.initialization(filter_size, DEBUG)

weights = LMS.train(train_data, train_desired, learning_step, weights, DEBUG)

NMSE = LMS.test_error(test_data, test_desired, weights, DEBUG)

if DEBUG > 0:
    print(NMSE)

output_fp = open('LMS-' + sys.argv[1].replace('.','_') + '.txt', 'w+')
output_fp.write(str(NMSE))
output_fp.close()

s3 = boto3.resource('s3')
s3.Object('deepoptimization-uf-optml-bucket', 'LMS-' + sys.argv[1].replace('.','_') + '.txt').put(Body=open('LMS-' + sys.argv[1].replace('.','_') + '.txt', 'rb'))
