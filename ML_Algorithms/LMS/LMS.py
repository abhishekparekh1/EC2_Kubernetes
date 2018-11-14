#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Name: Ruben Vazquez
# UFID: 2143-1351
# Title: Least Mean Squares Algorithm
# Description: Code that implements the least mean squares learning algorithm


# In[2]:


# Preconditions:

# train_data: MxN matrix, rows are observations, columns are measured features
# train_desired: Mx1 vector, each element is a desired output
# test_data: PxN matrix, rows are observations, columns are measured features
# test_desired: Px1 vector, each element is a desired output
# learning step: scalar

# In[18]:


import csv
import numpy as np
import matplotlib.pyplot as plt


# Function for generating the data used for training and testing

def generate_data(mu, sigma, filter_size, use_real_data, filename, percent_test, DEBUG):
    
    if DEBUG > 1:
        print('Generating new data...')
    
    # Predict D + 1 values into the future
    D = 0
    
    # Generate data from a normal distribution
    if use_real_data == 0:
        
        num_data_points = 10000
        num_test_points = np.int(np.floor(num_data_points*percent_test))
        
        data = np.random.normal(mu,sigma,num_data_points)
        
        y = np.append(data, np.zeros((1,)))
        t = -0.8*y[0:num_data_points] + 0.7*y[1:num_data_points+1]
        q = t + 0.25*t**2 + 0.11*t**3
        
        data = q
    
    # Import monthly sunspot data
    else:
        
        data = np.array([])
        
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                data = np.append(data,float(row[3]))
                
    num_data_points = data.shape[0]
    num_test_points = np.int(np.floor(num_data_points*percent_test))
    
    # Create the train_data, train_desired, test_data, and test_desired data sets
    train_temp = np.array(data[0:num_data_points-num_test_points])
    test_temp = np.array(data[num_data_points-num_test_points:])

    x = np.zeros((0,filter_size))
    t = np.zeros((0,1))

    z = np.zeros((0,filter_size))
    d = np.zeros((0,1))

    for i in range(0,train_temp.shape[0]-filter_size-D):
        x = np.append(x,[train_temp[i:i+filter_size]],axis=0)
        t = np.append(t,train_temp[i+filter_size+D])

    for i in range(0,test_temp.shape[0]-filter_size-D):
        z = np.append(z,[test_temp[i:i+filter_size]],axis=0)
        d = np.append(d,test_temp[i+filter_size+D])

    return x,t,z,d


# In[19]:


# Function used for creating the required data structures

def initialization(filter_size, DEBUG):
    
    if DEBUG > 0:
        print('Initializing required data structures...')
    
    # Initialize the matrix of weight vectors
    weights = np.random.rand(filter_size,1)
    
    return weights


# In[20]:


# Function that trains the weights of the filter

def train(train_data, train_desired, learning_step, weights, DEBUG):
    
    if DEBUG > 0:
        print('Training the weights...')
    
    # Train the weights using the least mean squares algorithm
    for i in range(0,train_data.shape[0]):
        y = np.dot(weights[:,i],train_data[i])
        e = train_desired[i] - y
        delta = learning_step*e*np.atleast_2d(train_data[i]).T
        weights = np.append(weights, weights[:,i]+delta, axis=1)
    
    return weights


# In[21]:


# Function that returns the error of the test data

def test_error(test_data, test_desired, weights, DEBUG):
    
    if DEBUG > 0:
        print('Obtaining the error...')
    
    # Initialize the array of predicted values
    y = np.array([])
    
    # Calculate the predicted values using the trained weights
    for i in range(0,test_data.shape[0]):
        y = np.append(y, np.dot(weights[:,-1],test_data[i]))
    
    # Calculate the normalized mean-squared error
    NMSE = (np.dot(test_desired - y, test_desired - y)/test_data.shape[0])/(np.mean(test_desired)*np.mean(y))
    
    # Plot the graph of the desired output against the predicted output
    if DEBUG > 1:
        plt.plot(range(1,test_data.shape[0]+1), y, range(1,test_data.shape[0] + 1), test_desired)
        plt.show()
    
    return NMSE
