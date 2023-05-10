#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_df = pd.read_csv(url,header=None)
print(iris_df)


# In[2]:


print(iris_df.index)
print(iris_df.columns)
iris_df.columns = list('abcde')
print(iris_df.head())


# In[3]:


#iris_df['x'] = iris_df['a']/iris_df['b'] # 생성
iris_df.insert(2,'x2',iris_df['a']/iris_df['b'])
print(iris_df)
iris_df_d = iris_df.drop(['a','d','e'],axis = 1) # 제거
print(iris_df_d.head())


# In[6]:


s1 = pd.Series(list('abcde'), index = [x for x in range(5)])
s2 = pd.Series(list('XYZF'), index = [3,2,5,1])
df1 = pd.DataFrame({'a':s1,'b':s2})
print(df1)


# In[16]:


#print(df1.isna())
#print(df1.dropna())
#print(df1.replace(np.NaN,'x'))
df1['a'] = df1['a'].replace(np.NaN,'xx') # 원본을 바꾸지 않음
df1['b'].replace(np.NaN,'ppp',inplace =True)# 원본을 바꿈
print(df1)
#print(df1[df1.isna()])

