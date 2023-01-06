#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


data = keras.datasets.fashion_mnist
(train_images, train_labels),(test_images, test_labels) = data.load_data()


# In[5]:


class_names = ["T-shirt/top","Trousser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle boot"]
train_images = train_images/255.0
test_images = test_images/255.0


# In[6]:


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128,activation="relu"),
    keras.layers.Dense(10,activation="softmax"),
    
])

model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])
model.fit(train_images,train_labels,epochs=5)


# In[7]:


test_loss, test_accuracy = model.evaluate(test_images,test_labels)
print(test_accuracy)

