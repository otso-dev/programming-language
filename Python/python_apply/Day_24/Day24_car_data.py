#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
current_font_list = matplotlib.rcParams['font.family']

font_path = "C:/Windows/Fonts/H2GTRE.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()

matplotlib.rcParams['font.family'] = [font]+current_font_list

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data'
pd_data = pd.read_csv(url,header=None)
pd_data.columns = ['구매가','유지비용','문갯수','탑승인원','수납공간','안전도','만족도']
pd_data.head()


# In[40]:


# 구매가가 만족도에 미치는 영향
    # - figure를 좌우로 나누어, 왼쪽은 구매가 vs 만족도 산점도, 오른쪽은 아래위로 분할, 위쪽은 구매가 vhigh중 만족도 별 count,
# 수납공간이 크면 탑승인원도 많은가
fig1 = plt.figure(figsize=(6.4*2,6.8))
a = fig1.add_subplot(1,2,1)
#a.scatter(pd_data['구매가'],pd_data['만족도'])
a.set_title("구매가가 만족도에 미치는 영향")

b = fig1.add_subplot(2,2,2)
filter1 = pd_data['구매가'] =='vhigh'
s1 = pd_data.loc[filter1,'만족도'].value_counts()
s2 = pd.Series(list(s1.values)+[0,0], index=['unacc','acc','good','vgood'])
b.bar(s2.index,s2)
#print(s2)
b.set_title("구매가가 높은 차량의 만족도")

c = fig1.add_subplot(2,2,4)
filter1 = pd_data['구매가'] == 'low'
s1 = pd_data.loc[filter1,'만족도'].value_counts()
c.bar(s1.index,s1)
c.set_title("구매가가 낮은 차량의 만족도")

from pandas.api.types import CategoricalDtype

price_category = CategoricalDtype(categories=["low","med","high","vhigh"],ordered=True)
eval_category = CategoricalDtype(categories=["unacc","acc","good","vgood"],ordered=True)

g1 = pd_data.groupby(['구매가','만족도'])
s3 = g1['안전도'].count()
s3 = s3.reset_index()
s3['구매가'] = s3['구매가'].astype(price_category)
s3['만족도'] = s3['만족도'].astype(eval_category)
s3.sort_values('구매가',inplace=True)
s3.sort_values('만족도',inplace=True)
a.scatter(s3['구매가'],s3['만족도'], s=s3['안전도'])


# In[ ]:




