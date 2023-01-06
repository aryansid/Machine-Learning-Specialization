#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# In[25]:


#Forward propogation using tensorflow
layer_1 = Dense(units=3, activation='sigmoid')
layer_2 = Dense(units=1, activation='sigmoid')
model = Sequential([layer_1,layer_2])
x = np.array([[200.0,17.0],
             [120.0,5.0],
             [425.0,20.0],
             [212.0,18.0]])
y = np.array([1,0,0,1])
#model.compile(...)
model.fit(x,y)


# In[21]:


#Forward propogation from scratch
def dense(a_in, W, b, g):
    units = W.shape(1)
    a_out = np.zeros(units)
    for i in range(units):
        w = [:,j]
        z = np.dot(w,a_in[j]) + b[j]
        a_out[j] = g(z)
    return a_out

def sequential(x):
    a1 = dense(x,W1,b1)
    a2 = dense(a1,W2,b2)
    a3 = dense(a1,W3,b3)
    f_x = a3
    return f_x

