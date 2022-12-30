#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[4]:


def sigmoid(x):
    return 1/(1+np.exp(-x))

class LogisticRegression():
    def __init__(self): 
        self.learning_rate = 0.001
        self.n_iters = 1000
        self.weights = None
        self.bias = None
        
    def fit(self, X, y): 
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for i in range(self.n_iters):
            linear_eq = np.dot(X, self.weights) + b
            predictions = sigmoid(linear_eq)
            
            dw = (1/n_samples)*np.dot(X.T, (predictions - y))
            db = (1/n_samples)*np.sum(predictions - y)
            
            self.weights = self.weights - learning_rate*dw
            self.bias = self.bias - learning_rate*db
            
        def predict():
            linear_eq = np.dot(X, self.weights) + b
            y_pred = sigmoid(linear_eq)
            class_pred = [0 if y < 0.5 else 1 for y in y_pred]
            return class_pred
        

