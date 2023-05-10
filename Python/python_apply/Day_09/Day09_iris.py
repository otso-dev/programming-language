#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import numpy as np
x = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')


# In[23]:


raw_data=[]
for line in x.text.split('\n'):
    raw_data.append(line.split(','))
for sample in raw_data:
    for i,value in enumerate(sample[0:4]):
        if len(sample) < 1:
            continue
        try:
            sample[i] = float(value)
        except:
            sample[i] = 0.0
print(raw_data[0::50])


# In[24]:


for sample in raw_data:
    if len(sample) < 2:
        continue
    if 'setosa' in sample[-1]:
        sample[-1] = 0.0
    elif 'versicolor' in sample[-1]:
        sample[-1] = 1.0
    elif 'virginica' in sample[-1]:
        sample[-1] = 2.0


# In[26]:


raw_data = raw_data[:150]
print(len(raw_data))


# In[27]:


np_data = np.array(raw_data)
np_data.shape


# ### 기본 통계값
# * 전체(150샘플) 평균, 표준편차 - sepal length, sepal width, petal length, petal with
# * 품종별 평균, 표준편차
# * 평균 np.mean()
# * 평균 np.std()

# In[87]:


print(np.mean(np_data[:,:-1] ,axis = 0), np.std(np_data[:,:-1], axis = 0))
print('setosa 평균: {}'.format(np.mean(np_data[0:50,:-1],axis = 0)),'\tsetosa 표준편차:{}'.format(np.std(np_data[0:50,:-1],axis = 0)),
      '\nversicolor 평균: {}'.format(np.mean(np_data[50:100,:-1], axis = 0)),'\tversicolor 표준편차:{}'.format(np.std(np_data[50:100,:-1],axis = 0)),
      '\nvirginica 평균: {}'.format(np.mean(np_data[100:,:-1],axis = 0)),'\tvirginica 표준편차:{}'.format(np.std(np_data[100:,:-1],axis = 0)))


# In[82]:


print(np.mean(np_data,axis = 0))
print(np.std(np_data,axis = 0))
print(np.corrcoef(np_data.T))# 상관도


# In[85]:


fiter_setosa = np_data[:,-1] ==0.0
fiter_versicolor = np_data[:,-1] ==1.0
fiter_virginica = np_data[:,-1] ==2.0

print(np.mean(np_data[fiter_setosa],axis = 0))
print(np.std(np_data[fiter_setosa],axis = 0))

