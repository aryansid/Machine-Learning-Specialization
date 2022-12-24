#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np 
import pandas as pd
from sklearn import linear_model


# In[5]:


df = pd.read_csv("C:\CSV\homeprices.csv")
df


# In[12]:


import math
median_bedroom = math.floor(df.bedrooms.median())
df.bedrooms = df.bedrooms.fillna(median_bedroom)
df


# In[14]:


reg = linear_model.LinearRegression()
reg.fit(df[['area','bedrooms','age']], df.price)


# In[ ]:




