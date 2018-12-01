Usage:
python LMS_driver.py "learning rate" SN_m_tot_V2.0.csv "use data from file" "test set percentage" "debug"

learning rate: float
use data from file: integer, either 0 (pick data from a normal distribution) or 1 (load data from SN_m_tot_V2.0.csv)
test set percentage: float, in the range 0 to 1
debug: int, from 0 to 3 (greater value displays more debugging messages)

output: a file containing the test set error
