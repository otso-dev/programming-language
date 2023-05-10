#!/usr/bin/env python
# coding: utf-8

# #### 전국푸드트럭허가구역표준데이터
# - 전국/지자체별 푸드트럭허가구역 갯수
# - 전국/지자체별 푸드트럭 운영대수

# In[4]:


import numpy as np
import pandas as pd

food_df = pd.read_csv('전국푸드트럭허가구역표준데이터.csv',encoding='cp949')
food_df.head()


# In[28]:


food_df_drop_truck = food_df['푸드트럭운영대수'].dropna()
truck_group = food_df.groupby('시도명').size().reset_index(name='푸드트럭운영대수')
print(truck_group)
print(food_df['푸드트럭운영대수'].dtype)
print('전국 푸드트럭 운영대수: {} '.format(int(np.sum(food_df_drop_truck))))


# In[27]:


group_df = food_df.groupby('시도명').size().reset_index(name='허가구역수')
print(group_df)
print('전국푸드트럭허가구역:',342)

