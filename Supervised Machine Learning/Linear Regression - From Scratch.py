#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

class LinearRegression: 
    def __init(self)__: 
        self.learning_rate = 0.001
        self.n_iters = 1000
        self.weights = None
        self.bias = None
        
    #Training the data 
    def fit(self, X, y):
        n_samples = X.shape[0]
        n_features = X.shape[1]
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for i in range(n_iters):
            y_pred = np.dot(X, self.weights) + self.bias
        
            dw = (1/n_features)*np.dot(X, (y_pred - y))
            db = (1/n_features)*np.sum(y_pred - y)
        
            self.weights = self.weights - self.lr * dw 
            self.bias = self.bias - self.lr * db
        
        
        
        
        

