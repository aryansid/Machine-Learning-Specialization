#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from sklearn.linear_model import LogisticRegression


# In[4]:


X = np.array([[0.5, 1.5], [1,1], [1.5, 0.5], [3, 0.5], [2, 2], [1, 2.5]])
y = np.array([0, 0, 0, 1, 1, 1])


# In[5]:


model = LogisticRegression()
model.fit(X,y)


# In[7]:


y_pred = model.predict(X)
print("Prediction on training set:", y_pred)


# In[8]:


print("Accuracy on training set:", model.score(X, y))

