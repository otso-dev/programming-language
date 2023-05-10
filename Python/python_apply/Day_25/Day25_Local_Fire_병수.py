#!/usr/bin/env python
# coding: utf-8

# #### kosis.kr: 소방청->시도별화재발생현황(총괄)2010~2021
# * 시각화 기획,설계,구현
# * 기획
#     - 전국 기준으로 년도별 사망자와 부상자 증가 추이 -> 왼쪽에는 사망자 추이, 오른쪽에는 부상자 추이
#     - 사망자와 부상자간의 상관관계 구하기
#     - 부산에서 년도별 재산 피해 비율 (2010, 2021)
#     - 지역별 화재건수 구하기 (2010, 2021)
#     - 시별, 도별 사망자와 부상자간의 상관관계 구하기
#     - 시별, 도별 년도별 이재민 수 포인트 그래프 만들기
# * 참고: https://www.nfds.go.kr/

# In[1]:


# 필요 라이브러리
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


# In[2]:


# 한글 글꼴 넣어주기
current_font_list = matplotlib.rcParams['font.family']
font_path = "C:\Windows\Fonts\gulim.ttc"
kfont = matplotlib.font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rcParams['font.family'] = [kfont] + current_font_list


# In[3]:


# 데이터 불러오기
pd_data = pd.read_csv('시도별_화재발생_현황_총괄__20230307153251.csv', encoding = 'cp949')
pd_data


# In[4]:


pd_data['시점'] = pd_data['시점'].astype('category')
pd_data['행정구역별'] = pd_data['행정구역별'].astype('str')


# In[5]:


pd_data['사망 (명)'] = pd_data['사망 (명)'].replace('-', '0')
pd_data['사망 (명)'].unique()
pd_data['사망 (명)'] = pd_data['사망 (명)'].astype(np.int64)


# In[6]:


pd_data.dtypes


# In[7]:


pd_data['행정구역별'].unique()


# In[8]:


fig = plt.figure(figsize=(6.4*2, 4.8))
a = fig.add_subplot(1,2,1)
b = fig.add_subplot(1,2,2)
filter1 = pd_data['행정구역별'] == '전국'
sns.barplot(data=pd_data[filter1], x="시점", y='사망 (명)', ax=a)
a.set_title('전국 년도별 사망자')
sns.barplot(data=pd_data[filter1], x="시점", y='부상 (명)', ax=b)
b.set_title('전국 년도별 부상자')


# In[9]:


filter1 = pd_data['행정구역별'] != '전국'
local_data = pd_data[filter1]
local_data = local_data.reset_index()
local_data = local_data.drop(labels='index',axis=1)
local_data['행정구역별'].value_counts()


# In[10]:


fig = plt.figure(figsize=(6.4*2, 4.8))
c = fig.add_subplot()
sns.scatterplot(data=local_data, x="사망 (명)", y='부상 (명)', hue = '행정구역별')
c.set_title('행정 구역별 부상자와 사망자의 상관관계')


# In[11]:


local_data


# In[12]:


fig = plt.figure(figsize=(6.4*2, 4.8))
d = fig.add_subplot(1,2,1)
f = fig.add_subplot(1,2,2)

filter1 = (local_data['행정구역별'] == '부산광역시') & (local_data['시점'] == 2010)
# local_data[filter1]
filter2 = (local_data['행정구역별'] == '부산광역시') & (local_data['시점'] == 2021)
# local_data[filter2]

d.pie(local_data.iloc[12, 6:8], labels = ['부동산', '동산'], autopct= '%.2f')
d.set_title('2010년 부산 재산피해 비율')
f.pie(local_data.iloc[23, 6:8], labels = ['부동산', '동산'], autopct= '%.2f')
f.set_title('2021년 부산 재산피해 비율')


# In[13]:


fig = plt.figure(figsize=(6.4*3, 4.8*2))
g = fig.add_subplot(2,1,1)
h = fig.add_subplot(2,1,2, sharey=g)

filter1 = local_data['시점'] == 2010
filter2 = local_data['시점'] == 2021

sns.barplot(data=local_data[filter1], x='행정구역별', y='건수 (건)', ax=g)
g.set_title('2010 지역별 사고 건수')
sns.barplot(data=local_data[filter2], x='행정구역별', y='건수 (건)', ax=h)
h.set_title('2021 지역별 사고 건수')


# In[14]:


si_data = local_data[local_data['행정구역별'].str.contains('시')]
print(si_data['행정구역별'].value_counts())
do_data = local_data[local_data['행정구역별'].str.contains('도')]
print(do_data['행정구역별'].value_counts())


# In[80]:


x = sns.scatterplot(data=si_data, x='사망 (명)', y='부상 (명)', hue='행정구역별', s= 55)
x.set_title('시별 사망자와 부상자의 상관관계')
x.figure.set_size_inches(6.4*2, 4.8*2)


# In[76]:


x = sns.scatterplot(data=do_data, x='사망 (명)', y='부상 (명)', hue='행정구역별', s= 55)
x.set_title('도별 사망자와 부상자의 상관관계')
x.figure.set_size_inches(6.4*2, 4.8*2)


# In[44]:


x = sns.catplot(data=si_data, x='시점', y='이재민수 (명)', hue = '행정구역별', kind='point', dodge=False)
x.figure.suptitle('시별 이재민 수')
x.figure.set_size_inches(6.4*2, 4.8*2)


# In[46]:


x = sns.catplot(data=do_data, x='시점', y='이재민수 (명)', hue = '행정구역별', kind='point', dodge=False)
x.figure.suptitle('시별 이재민 수')
x.figure.set_size_inches(6.4*2, 4.8*2)

