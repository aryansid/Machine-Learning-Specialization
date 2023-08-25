#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


# In[9]:


df = pd.read_csv("C:\CSV\homeprices.csv")
df


# In[10]:


plt.xlabel("Area")
plt.ylabel("Price")
plt.scatter(df.area, df.price)


# In[11]:


#Create an object
reg = linear_model.LinearRegression()
#Train
reg.fit(df[['area']], df.price)


# In[12]:


reg.predict([[3300]])


# In[13]:


plt.scatter(df.area, df.price)
plt.plot(df.area, reg.predict(df[['area']]))

