#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
import requests

#iris_data_str = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
iris_df = pd.read_csv('iris.data',header = None)
print(iris_df)


# In[13]:


s1 = pd.Series(list('abcde'))
print(s1)
print(type(iris_df),type(s1))


# In[24]:


s2 = pd.Series([1,1.0,'a'])
s3 = pd.Series([x for x in range(10,21)])
#print(s3)
#print(s3[3])
#print(s3[3:8:2])
#print(s3[[3,7,9]])
print(s3[s3>15])


# In[27]:


print(s3.ndim)
print(s3.dtype)
print(s3.shape)
s3_f=s3.astype(np.float64)
print(s3_f)


# In[28]:


s3_np = s3.to_numpy()
print(s3_np,type(s3_np))


# In[30]:


print(s3*3)


# In[48]:


### DataFrame
s1 = pd.Series([x for x in range(10,20)])
s2 = pd.Series([x for x in range(100,120)])
s3 = pd.Series(list('abcdefghijk'))
df1 = pd.DataFrame({'a':s1,'b':s2,'c':s3})
#print(df1)
#print(df1['b'])
#print(df1[['a','c']])
#print(df1[2:5]['a'])
print(df1[:5])


# In[51]:


print(df1.head())
print(df1.tail(10))


# In[59]:


#print(df1)
print(df1.loc[3:10,['a','c']])#key값으로 indexing
print(df1.iloc[3:10,[0,1]])#index값으로 indexing

