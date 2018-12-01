Usage: python ANN_TF_Driver.py [--learning_rate LEARNING_RATE --network_size LAYER_1_SIZE LAYER_2_SIZE ... LAYER_N_SIZE --DEBUG DEBUG]

Arguments:
learning_rate: float
network_size: sequence of space delimited integers greater than 0
DEBUG: integer, greater integer values display more debugging messages

File can be run with no arguments. In that the case, the program is run with default values:
--learning_rate 0.1
--network_size 128
--DEBUG 0
