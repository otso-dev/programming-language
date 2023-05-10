#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd

pd_hydrant = pd.read_csv('전국소방용수시설표준데이터.csv',encoding='cp949')
pd_parking = pd.read_csv('전국소방자동차전용구역표준데이터.csv',encoding='cp949')


# In[25]:


df1 = pd_hydrant[['시도명','소재지도로명주소','위도','경도']]
df2 = pd_parking[['시도명','소재지도로명주소','위도','경도']]

df_combined = pd.concat((df1,df2),axis = 0,keys=['hydrant','parking'])
df_combined.reset_index(level = 0,inplace=True,names = '종류')
df_combined

# ex 강사님 code
# df_combined.reset_index(inplace = True)
# df_combined.drop('level_1',axis = 1, inplace = True)
# cname_list = list(df_combined.columns)
# cnmae_list[0] = '종류'
# df_combined.columns = cname_list
# df_combined


# In[27]:


# g1 = pd_hydrant.groupby('시도명')
# s1 = g1['시도명'].count()
# s1.name = 'hydrant시도명'
# g2 = pd_parking.groupby('시도명')
# s2 = g2['시도명'].count()
# s2.name = 'parking시도명'
# print(s1)
# print(s2)


#강사님 code
g1 = df_combined.groupby(['시도명','종류'])
g1.count()

g2 = df_combined.groupby(['종류','시도명'])
g2.count()

