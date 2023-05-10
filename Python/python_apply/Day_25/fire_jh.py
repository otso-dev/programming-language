#!/usr/bin/env python
# coding: utf-8

# kosis.kr: 소방청->시도별화재발생현황(총괄) 2010~2021
# * 시각화 기획, 설계, 구현
# * 지자체별 화재 건수

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from matplotlib import font_manager, rc

current_font_list = matplotlib.rcParams['font.family']

font_path = "C:/Windows/Fonts/H2GTRE.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font)
matplotlib.rcParams['font.family'] = [font]+current_font_list
print(matplotlib.rcParams['font.family'])


# In[2]:


pd_data = pd.read_csv('시도별_화재발생_현황_총괄__20230307153228.csv', encoding='cp949')
filter1 = pd_data['행정구역별'] != '전국'
pd_data = pd_data[filter1]
pd_data = pd_data.reset_index()
pd_data = pd_data.drop(['index'], axis=1)

pd_data['행정구역별'].value_counts()
# pd_data
# pd_data.iloc[94]['시점'] = '2010'
# pd_data.iloc[83]


# In[3]:


pd_data[pd_data['행정구역별'] == '세종특별자치시']
for i in range(84,86):
    if(i == 84):
        new_data = {
        '행정구역별' : '세종특별자치시',
        '시점' : 2010,
        '건수 (건)':0, '사망 (명)':0, '부상 (명)':0, '재산피해(계) (천원)':0, '부동산 (천원)':0, '동산 (천원)':0, '이재가구수 (가구)':0, '이재민수 (명)': 0
        }
    if(i == 85):
        new_data = {
        '행정구역별' : '세종특별자치시',
        '시점' : 2011,
        '건수 (건)':0, '사망 (명)':0, '부상 (명)':0, '재산피해(계) (천원)':0, '부동산 (천원)':0, '동산 (천원)':0, '이재가구수 (가구)':0, '이재민수 (명)': 0
        }
    temp1 = pd_data[pd_data.index < i]
    temp2 = pd_data[pd_data.index >= i]
    pd_data = temp1.append(new_data,ignore_index=True).append(temp2, ignore_index=True)


# In[4]:


pd_data[pd_data['행정구역별'] == '세종특별자치시']
# pd_data.groupby(['시점','행정구역별'])
# pd_data.


# In[56]:


fig, axe = plt.subplots(figsize=(8, 8))
x = pd_data['시점'].unique()
axe.set(title='지자체별 화재 건수',xlabel='시점', xticks=x,
       ylabel='건수 (건)')
# axe.set_xlabel('시점')
# axe.set_ylabel('건수 (건)')
bottom = np.zeros(len(x))
for region in pd_data['행정구역별'].unique():
    filter1 = pd_data['행정구역별'] == region
    y = list(pd_data.loc[filter1, '건수 (건)']) 
#     print(bottom)
#     print(y)
    p = axe.bar(x,y, bottom=bottom)
    bottom += y
    
axe.legend(labels=pd_data['행정구역별'].unique())


# In[7]:


fig, axe = plt.subplots()
x = pd_data['시점'].unique()
# 막대 그래프 그리기
bottom = np.zeros(len(x))
for region in pd_data['행정구역별'].unique():
    filter1 = pd_data['행정구역별'] == region
    y = list(pd_data.loc[filter1, '건수 (건)'])
    p = axe.bar(x, y, bottom=bottom)

plt.show()


# In[14]:


a = pd_data.groupby(['시점','행정구역별']).sum()
a
axe = pd_data.plot.bar(x = '시점', y = '건수 (건)', rot=0, stacked=True)

