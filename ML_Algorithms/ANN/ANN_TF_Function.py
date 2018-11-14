
# coding: utf-8

# In[1]:


# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)


# In[10]:



def generate_data(DEBUG):
    
    if (DEBUG > 1):
        print('Generating data...')
    
    mnist = keras.datasets.mnist
    (train_data, train_desired), (test_data, test_desired) = mnist.load_data()
    
    train_data = train_data / 255.0
    test_data = test_data / 255.0
    
    train_desired = keras.utils.to_categorical(train_desired)
    test_desired = keras.utils.to_categorical(test_desired)
    
    return train_data, train_desired, test_data, test_desired


# In[11]:



def initialization(train_data, train_desired, network_size, DEBUG):
    
    if (DEBUG > 1):
        print('Initializing network...')
    
    model = keras.Sequential()
    
    model.add(keras.layers.Flatten(input_shape=(28, 28)))
    
    for i in range(0,len(network_size)):
        model.add(keras.layers.Dense(network_size[i], activation=tf.nn.relu))
    
    model.add(keras.layers.Dense(10, activation=tf.nn.softmax))
    
    return model
    


# In[14]:



def train(train_data, train_desired, learning_rate, model, DEBUG):
    
    if (DEBUG > 1):
        print('Training model...')
    
    sgd = keras.optimizers.SGD(lr=learning_rate)
    
    model.compile(optimizer=sgd, loss='mean_squared_error', metrics=['accuracy'])
    
    model.fit(train_data, train_desired, epochs=10)
    
    return model
    


# In[19]:



def test_error(test_data, test_desired, model, DEBUG):
    
    if (DEBUG > 1):
        print('Getting error...')
    
    test_loss, test_acc = model.evaluate(test_data, test_desired)
    
    return (1 - test_acc)

