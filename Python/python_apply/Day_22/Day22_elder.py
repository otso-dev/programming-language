#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd_raw = pd.read_csv('전국노인장애인보호구역표준데이터.csv', encoding='cp949')

col_selection=['시도명','제한속도','CCTV설치여부','CCTV설치대수','보호구역도로폭']
pd_data = pd_raw[col_selection]
print(pd_data.shape)
for e in pd_data:
    print(e, pd_data[e].dtype, pd_data[e].hasnans)


# In[3]:


#시도명
col = pd_data['시도명']
print(col.unique(), col.hasnans)
print(col.describe())


# In[4]:


# 제한속도
col = pd_data['제한속도']
print(col.unique(), col.hasnans)
print(col.describe())

# 이상치
q1, q3 = col.quantile([0.25, 0.75])
iqr = q3 - q1
upper = q3+1.5*iqr
lower = q1-1.5*iqr
print(q1, q3, iqr, lower, upper)

#col[col>41]
#col[col<21]
#col[col==60]


# In[5]:


# CCTV 설치여부
col = pd_data['CCTV설치여부']
print(col.unique(), col.hasnans)
print(col.describe())


# In[6]:


# CCTV 설치대수
col = pd_data['CCTV설치대수']
print(col.unique(), col.hasnans)
print(col.describe())

yfilter = pd_data['CCTV설치여부']=='Y'
nfilter = pd_data['CCTV설치여부']=='N'
pd_data.loc[yfilter, 'CCTV설치대수'] = pd_data.loc[yfilter, 'CCTV설치대수'].fillna(1.0)
pd_data.loc[nfilter, 'CCTV설치대수'] = pd_data.loc[nfilter, 'CCTV설치대수'].fillna(0.0)

print(col.unique(), col.hasnans)
print(col.describe())


# In[9]:


# 보호구역도로폭
col = pd_data['보호구역도로폭']
print(col.unique(), col.hasnans)
print(col.describe())

def fn1(x):
    if (x == np.NaN) or (type(x)==type(1.0)):
        return x
    if '~' in x:
        return np.mean(np.array(x.split('~')).astype(np.float64))
    else:
        return float(x)
    
pd_data.fillna(0.0, inplace=True)
pd_data['보호구역도로폭'] = pd_data['보호구역도로폭'].apply(fn1)
print(col.unique(), col.hasnans)
print(col.describe())


# In[11]:


pd_data.to_csv('전국노인장애인보호구역표준데이터_pass1.csv')

