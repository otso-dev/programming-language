#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


#도로
pd_doro = pd.read_csv('전국일방통행도로표준데이터(정제완료).csv')
pd_child = pd.read_csv('전국어린이보호구역표준데이터(정제완료).csv')
pd_old = pd.read_csv('전국노인장애인보호구역표준데이터(정제완료).csv')


# In[6]:


#print(pd_doro.head()) # 시도명 별 보차분리여부 Y count
#print(pd_child.head()) # 시도명 별 CCTV 설치대수 count
#print(pd_old.head()) # 시도명 별 CCTV 설치대수 count


# In[7]:


g1 = pd_doro[pd_doro['보차분리여부']=='Y'].groupby('시도명')
s1 = g1['보차분리여부'].count()
s1.name = '일반통행보차분리Y_COUNT'
print(s1)


# In[8]:


g2 = pd_child.groupby('시도명')
s2 = g2['CCTV설치대수'].sum()
s2.name = '어린이CCTV_COUNT'
print(s2)


# In[10]:


g3 = pd_old.groupby('시도명')
s3 = g3['CCTV설치대수'].sum()
s3.name = '노인장애인CCTV_COUNT'
print(s3)


# In[11]:


df_combined = pd.concat((s1,s2,s3),axis = 1)
print(df_combined)


# In[13]:


import matplotlib.pyplot as plt

_, axe = plt.subplots()
axe.plot(df_combined['어린이CCTV_COUNT'])
axe.plot(df_combined['노인장애인CCTV_COUNT'])


# In[14]:


np.corrcoef(df_combined['어린이CCTV_COUNT'],df_combined['노인장애인CCTV_COUNT'])

