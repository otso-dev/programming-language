#!/usr/bin/env python
# coding: utf-8

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


# In[2]:


pd_data = pd.read_csv('../이륜차신고현황_시도별_20230310151721.csv',encoding='cp949',header=1)
pd_data['시점'] = pd_data['시점'].astype(str)
for i,v in enumerate(pd_data['시점']):
    pd_data['시점'][i] = v.split('.')[0]

print(pd_data)


# In[3]:


ple_data=pd.read_csv('../인구_가구_및_주택_–_읍면동_연도_끝자리_0_5___시군구_그_외_연도__20230310170639.csv',encoding='cp949')
ple_data.head()
ple_data.columns=['시군구(1)','시점','총인구']
ple_data.drop([0,1,2,3,4],inplace=True)


# In[4]:


ple_data=ple_data.reset_index()
ple_data.drop(['index'],axis=1,inplace=True)


# In[18]:


ple_data['시점']=ple_data['시점'].astype(str)


# In[5]:


g1 = pd_data.groupby(['시군구(1)','시점'])
sum_motorcycle = g1.sum()
filter1 = sum_motorcycle.reset_index()['시점'] != '2023'
df_motorcycle=sum_motorcycle.reset_index()[filter1]



fig1 = plt.figure(figsize=(20,10))
a = fig1.add_subplot(2,2,1)
b = fig1.add_subplot(2,2,2)
c = fig1.add_subplot(2,2,3)
d = fig1.add_subplot(2,2,4)

a_h=df_motorcycle.pivot('시군구(1)','시점','경형')
b_h=df_motorcycle.pivot('시군구(1)','시점','소형')
c_h=df_motorcycle.pivot('시군구(1)','시점','중형')
d_h=df_motorcycle.pivot('시군구(1)','시점','대형')

sns.heatmap(a_h,linewidths=0.5,annot=True,fmt=".0f",linecolor='black',cmap='crest',ax=a)
sns.heatmap(b_h,linewidths=0.5,annot=True,fmt=".0f",linecolor='black',cmap='crest',ax=b)
sns.heatmap(c_h,linewidths=0.5,annot=True,fmt=".0f",linecolor='black',cmap='crest',ax=c)
sns.heatmap(d_h,linewidths=0.5,annot=True,fmt=".0f",linecolor='black',cmap='crest',ax=d)

a.set_title('경형')
b.set_title('소형')
c.set_title('중형')
d.set_title('대형')


# In[6]:


filter1 = pd_data['시점'] != '2023'
df_data=pd_data[filter1]

g2=df_data.groupby(['시도명(1)','시점'])
time_sum_data=g2.sum()

fig1 = plt.figure(figsize=(15,10))
a = fig1.add_subplot(2,2,1)
b = fig1.add_subplot(2,2,2)
c = fig1.add_subplot(2,2,3)
d = fig1.add_subplot(2,2,4)

sns.lineplot(data=time_sum_data.reset_index(),x='시점',y='경형', ax=a)
sns.lineplot(data=time_sum_data.reset_index(),x='시점',y='소형', ax=b)
sns.lineplot(data=time_sum_data.reset_index(),x='시점',y='중형', ax=c)
sns.lineplot(data=time_sum_data.reset_index(),x='시점',y='대형', ax=d)


# In[26]:


g4=df_motorcycle.groupby('시군구(1)')
city_data = g4.sum()

fig2 = plt.figure(figsize=(6*4,10))
a = fig2.add_subplot(2,2,1)
b = fig2.add_subplot(2,2,2)
c = fig2.add_subplot(2,2,3)
d = fig2.add_subplot(2,2,4)

sns.barplot(data=city_data.reset_index().sort_values(by=['경형'],ascending=False),x='시군구(1)',y='경형',ax=a)
sns.barplot(data=city_data.reset_index().sort_values(by=['소형'],ascending=False),x='시군구(1)',y='소형',ax=b)
sns.barplot(data=city_data.reset_index().sort_values(by=['중형'],ascending=False),x='시군구(1)',y='중형',ax=c)
sns.barplot(data=city_data.reset_index().sort_values(by=['대형'],ascending=False),x='시군구(1)',y='대형',ax=d)


# In[35]:


g5 = ple_data.groupby(['시군구(1)']).sum()
p_data=g5.reset_index()
p_data.drop(['시군구(1)'],axis=1,inplace=True)
c_data=city_data.reset_index()
df_combined=pd.concat((c_data,p_data),axis=1)
df_combined


# In[41]:


fig3 = plt.figure(figsize=(6*4,10))
a = fig3.add_subplot(2,2,1)
b = fig3.add_subplot(2,2,2)
c = fig3.add_subplot(2,2,3)
d = fig3.add_subplot(2,2,4)
a2=a.twinx()
sns.barplot(data=df_combined, x='시군구(1)',y='경형',ax=a)
sns.lineplot(data=df_combined,x=np.arange(15),y='총인구',ax=a2)

