#!/usr/bin/env python
# coding: utf-8

# - 년도별
#     - 남/여 인구비율 - 인구_남,인구_여,column다음에 위치
#     - 한국인/외국인 비율 - 인구밀도 앞에 위치

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pop_df = pd.read_csv('등록인구추이_20230223163333.csv',encoding='cp949')
pop_df.drop(0,axis = 0,inplace=True)
pop_df.columns = ['시점','세대수','인구_남','인구_여','한국인','외국인','인구밀도']
pop_df.head()


# In[2]:


# pop_df.insert(4,'남_인구비율',pop_df['인구_남'].astype(np.int64)*100/(pop_df['인구_남'].astype(np.int64) + pop_df['인구_여'].astype(np.int64))  )
# pop_df.insert(5,'여_인구비율',pop_df['인구_여'].astype(np.int64)*100/(pop_df['인구_남'].astype(np.int64) + pop_df['인구_여'].astype(np.int64))  )
# pop_df.insert(8,'한국인_인구비율',pop_df['한국인'].astype(np.int64)*100/(pop_df['한국인'].astype(np.int64) + pop_df['외국인'].astype(np.int64))  )
# pop_df['인구_남']
# pop_df.loc[:,'인구_남']
# pop_df.iloc[:,2]
v = pop_df['인구_남'].astype(np.float64)/ pop_df['인구_여'].astype(np.float64)
pop_df.insert(4,'인구_남/여',v)


# In[4]:


v=pop_df['한국인'].astype(np.float64)/ pop_df['외국인'].astype(np.float64)
pop_df.insert(7,'한국인/외국인',v)
pop_df.head()


# In[6]:


pop_df.astype(np.float64)

