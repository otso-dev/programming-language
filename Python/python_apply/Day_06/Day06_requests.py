#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests

x = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')


# In[16]:


data = []
for line in x.text.split('\n'):
    data.append(line.split(','))
for i in data:
    for e , n in enumerate(i[:-1]):
        i[e] = float(n)
print(data)

