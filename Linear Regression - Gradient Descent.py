#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 


# In[ ]:


def gradient_descent(x, y): 
    w_curr = 0
    b_curr = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.001
    
    for i in range(iterations):
        y_predicted = w_curr*x + b_curr
        dw = -(2/n)*sum(x*(y - y_predicted))
        db = -(2/n)*sum(y - y_predicted)
        w_curr = w_curr - learning_rate*dw 
        b_curr = b_curr - learning_rate*db

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])


