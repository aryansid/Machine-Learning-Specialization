#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Importing data
import pandas as pd
dataset = pd.read_csv("C:\CSV\dataset_iris.csv")
x = dataset.iloc[:,1:-1].values
y = dataset.iloc[:,-1].values
print(x[:10])
print(y[:10])


# In[15]:


#Splitting the data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)


# In[16]:


#Scaling the data
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)


# In[17]:


#Training model
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(multi_class = "ovr", random_state = 0)
classifier.fit(x_train, y_train)


# In[18]:


#Testing model
from sklearn.metrics import confusion_matrix, accuracy_score
predictions = classifier.predict(x_test)
cm = confusion_matrix(predictions, y_test)
print(cm)
accuracy_score(predictions, y_test)

