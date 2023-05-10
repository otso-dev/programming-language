#!/usr/bin/env python
# coding: utf-8

# ### 시도별 화재발생 현황 총괄
#  - 행정구역별 총 사망자와 부상자
#      * 어느지역이 가장 많은 사망자와 부상자가 있는가
#  - 총 피해재산 비율
#      * 어느 재산피해 비율이 많이 차지하는가
#  - 화재발생 피해액이 2010 ~ 2021년도 까지 증가하였나
#  - 행정구역별 화재발생건수와 사망자와부상자의 상관도

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import matplotlib.ticker as ticker

current_font_list = matplotlib.rcParams['font.family']

font_path = "C:/Windows/Fonts/H2GTRE.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()

matplotlib.rcParams['font.family'] = [font]+current_font_list

df_fire = pd.read_csv('시도별_화재발생_현황_총괄__20230307153319.csv',encoding='cp949')

df_fire['사망 (명)'].unique()
for i , v in enumerate(df_fire['사망 (명)']):
    if '-' in v:
        df_fire['사망 (명)'][i] = 0
print(df_fire['사망 (명)'].unique())

filter1 = df_fire['행정구역별'] != '전국'
data = df_fire[filter1]
df_fire.head()


# In[2]:


#행정구역별로 총 부상자와 사망자
fig1 = plt.figure(figsize=(20*2,10))
a = fig1.add_subplot(1,2,1)
b = fig1.add_subplot(1,2,2)
data['부상 (명)'] = pd.to_numeric(data['부상 (명)'])
data['사망 (명)'] = pd.to_numeric(data['사망 (명)'])
sns.barplot(data=data, x="행정구역별", y="사망 (명)",ax=a,errorbar=None)
sns.barplot(data=data, x="행정구역별", y="부상 (명)",ax=b,errorbar=None)


# In[3]:


#전국 총 부동산 피해와 재산피해 비율
_,axe = plt.subplots()
filter2 = df_fire['행정구역별'] == '전국'
data2 = df_fire[filter2]
p_damage = data2['부동산 (천원)'].sum()
i_damage = data2['동산 (천원)'].sum()
total_damage = data2['재산피해(계) (천원)'].sum()
p_ratio = p_damage/total_damage
i_ratio = i_damage/total_damage
labels=['부동산피해','재고자산(동산) 피해']
sizes=[p_ratio,i_ratio]
axe.pie(sizes,labels=labels,autopct='%.2f')
axe.set_title('전국 총 부동산피해와 재산피해(동산) 비율')


# In[4]:


# 화재발생 피해액이 시간이 지날수록 늘어나는가?
plt.figure(figsize=(10,6))
ax=sns.lineplot(data=data2,x='시점',y='재산피해(계) (천원)')
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x,pos: '{:,.0f}(천원)'.format(x/1000)))


# In[5]:


# 행정구역별 화재발생건수와 사망자와부상자의 상관도
fig1 = plt.figure(figsize=(6.4*2,6.8))
a=fig1.add_subplot(1,2,1)
b=fig1.add_subplot(1,2,2)
sns.scatterplot(data=data, x='건수 (건)',y='사망 (명)',ax=a,color='red',label='사망자(명)')
sns.scatterplot(data=data, x='건수 (건)',y='부상 (명)',ax=b,color='green',label='부상자(명)')

a.set_title('행정구역별 화재발생 건수와 사망자의 상관도')
b.set_title('행정구역별 화재발생 건수와 부상자의 상관도')
a.legend()
b.legend()
cor_dead = np.corrcoef(data['건수 (건)'],data['사망 (명)'])[1][0]
cor_wounded = np.corrcoef(data['건수 (건)'],data['부상 (명)'])[1][0]
a.text(0,100,'상관도:{}'.format(round(cor_dead*100)/100 ))
b.text(0,525,'상관도:{}'.format(round(cor_wounded*100)/100 ))


# In[7]:


h_data=data.pivot('행정구역별','시점','사망 (명)')
sns.heatmap(h_data,linewidths=0.5,annot=True,fmt='.0f')


# In[14]:


# print(data['시점'].value_counts())
# sns.displot(data=data,x='시점')
print(data['건수 (건)'].value_counts())
# sns.displot(data=data,x='시점',y='건수 (건)',kind='kde')
sns.displot(data=data,x='건수 (건)',kind='kde')

