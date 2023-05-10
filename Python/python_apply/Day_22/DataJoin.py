#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

pd_oneway = pd.read_csv('전국일방통행도로표준데이터_pass1.csv')
#print(pd_oneway.describe(include='all'))
pd_child = pd.read_csv('전국어린이보호구역표준데이터_pass1.csv')
#print(pd_child)
pd_elder = pd.read_csv('전국노인장애인보호구역표준데이터_pass1.csv')
#print(pd_elder)


# In[2]:


#print(pd_oneway.head())   # 시도명 별 보차분리여부  y count
#print(pd_child.head())     # 시도명(지자체명) 별 CCTV 설치대수 count    
print(pd_elder.head())      # 시도명 별 CCTV 설치대수


# In[3]:


pd_child['보호구역도로폭'].value_counts()


# In[4]:


g1 = pd_oneway[pd_oneway['보차분리여부']=='Y'].groupby('시도명')
s1 = g1['보차분리여부'].count()
s1.name = '일방통행보차분리Y_COUNT'
print(s1)


# In[5]:


g2 = pd_child.groupby('지자체명')
s2 = g2['CCTV설치대수'].sum()
s2.name = '어린이CCTV_COUNT'
print(s2)


# In[6]:


g3 = pd_elder.groupby('시도명')
s3 = g3['CCTV설치대수'].sum()
s3.name = '노인장애인CCTV_COUNT'
print(s3)


# In[7]:


df_combined = pd.concat((s1,s2,s3), axis=1)
df_combined


# In[8]:


import matplotlib.pyplot as plt

_, axe = plt.subplots()
axe.plot(df_combined['어린이CCTV_COUNT'])
axe.plot(df_combined['노인장애인CCTV_COUNT'])


# In[9]:


df_combined.reset_index(inplace = True)


# In[10]:


_, axe = plt.subplots()
axe.plot(df_combined['어린이CCTV_COUNT'])
axe.plot(df_combined['노인장애인CCTV_COUNT'])


# In[11]:


df_child_min = df_combined['어린이CCTV_COUNT'].min()
df_child_max = df_combined['어린이CCTV_COUNT'].max()

df_old_min = df_combined['노인장애인CCTV_COUNT'].min()
df_old_max = df_combined['노인장애인CCTV_COUNT'].max()

df_combined['어린이_norm'] = df_combined['어린이CCTV_COUNT'].apply(lambda x : (x-df_child_min)/(df_child_max - df_child_min))
df_combined['노인장애인_norm'] = df_combined['노인장애인CCTV_COUNT'].apply(lambda x : (x-df_old_min)/(df_old_max - df_old_min))

_, axe = plt.subplots()
axe.plot(df_combined['어린이_norm'])
axe.plot(df_combined['노인장애인_norm'], color = 'green')


# In[12]:


child_mean =  df_combined['어린이CCTV_COUNT'].mean()
child_std =  df_combined['어린이CCTV_COUNT'].std()
df_combined['어린이CCTV_COUNT_std'] =  df_combined['어린이CCTV_COUNT'].apply(lambda x : (x - child_mean)/(child_std))

old_mean = df_combined['노인장애인CCTV_COUNT'].mean()
old_std = df_combined['노인장애인CCTV_COUNT'].std()
df_combined['노인장애인CCTV_COUNT_std'] = df_combined['노인장애인CCTV_COUNT'].apply(lambda x: (x - old_mean)/(old_std))

_, axe = plt.subplots()
axe.plot(df_combined['어린이CCTV_COUNT_std'])
axe.plot(df_combined['노인장애인CCTV_COUNT_std'],color = 'green')


# In[13]:


np.corrcoef(df_combined['어린이CCTV_COUNT'], df_combined['노인장애인CCTV_COUNT'])


# In[14]:


df1 = pd_child[['CCTV설치여부','CCTV설치대수','지자체명']]
df2 = pd_elder[['CCTV설치여부','CCTV설치대수','시도명']]
df1.columns = df2.columns
# print(df1.head())
# print(df2.head())
df12 = pd.concat((df1,df2),axis = 0,keys=['어린이','노인장애인'])
df12.reset_index(level =0,inplace = True)
df12

