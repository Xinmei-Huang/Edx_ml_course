#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 12:59:45 2019

@author: dileepn

Perceptron algorithm with offset
"""
import numpy as np

# Data points
x = np.array([[-4,2],[-2,1],[-1,-1],[2,2],[1,-2]])
#x = np.array([[1,0],[-1,10],[-1,-1]])

# Labels
y = np.array([[1],[1],[-1],[-1],[-1]])
#y = np.array([[-1],[1],[1]])

# Number of examples
n = x.shape[0]

# Number of features
m = x.shape[1]

# No. of iterations
T = 10

# Initialize parameter vector and offset
theta = np.array([[0],[0]])
theta0 = 0

# Start the perceptron update loop
mistakes = 0    # Keep track of mistakes
for t in range(T):
    counter = 0     # To check if all examples are classified correctly in loop
    for i in range(n):
        if float(y[i]*(theta.T.dot(x[i,:]) + theta0)) <= 0:
            theta += y[i]*x[i,:].reshape((m,1))
            theta0 += float(y[i])
            print("current parameter vector:", theta)
            print("current offset: {:.1f}".format(theta0))
            mistakes += 1
        else:
            counter += 1
    
    # If all examples classified correctly, stop
    if counter == n:
        print("No. of iteration loops through the dataset:", t+1)
        break
    
# Print total number of mistakes
print("Total number of misclassifications:", mistakes)