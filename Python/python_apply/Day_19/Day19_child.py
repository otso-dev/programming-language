#!/usr/bin/env python
# coding: utf-8

# #### 전국어린이보호구역표준데이터
#  * CCTV 설치 대수가 없을 경우, Y이면 1, N이면 0으로 대체
# - 시설종류별 CCTV 설치여부 카운트 / 대수
# - 광역시도별, 시설 종류별 카운트
# - 관할경찰서별 CCTV 설치 대수
# - CCTV평균 설치 대수
# - 도로폭/ CCTV 설치 대수 상관도

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd_rawdata = pd.read_csv('전국어린이보호구역표준데이터.csv',encoding='cp949')
colum_selection = ['시설종류','관할경찰서명','CCTV설치여부','CCTV설치대수','제공기관명','보호구역도로폭']
pd_data = pd_rawdata[colum_selection]
del pd_rawdata
#print(pd_data[:3])


# In[2]:


# EDA : Exploratory Data Analysis
print(pd_data.columns)
print(pd_data.dtypes)

pd_data['시설종류'] = pd_data['시설종류'].astype('category')
pd_data['CCTV설치여부'] = pd_data['CCTV설치여부'].astype('category')
#print(pd_data.dtypes)
#print(pd_data.shape)
#pd_data.describe(include='all')
print(pd_data['보호구역도로폭'].value_counts())
print(pd_data['보호구역도로폭'].isna().value_counts())


# In[3]:


for e in pd_data:
    print(e,pd_data[e].hasnans)
    if pd_data[e].hasnans == True:
        print(pd_data[e].isna().value_counts())


# In[4]:


# CCTV결측치 처리
print(pd_data['CCTV설치대수'].isna().value_counts())

filter_y = pd_data['CCTV설치여부'] == 'Y'
filter_n = pd_data['CCTV설치여부'] == 'N'
pd_data.loc[filter_y,'CCTV설치대수'] = pd_data.loc[filter_y,'CCTV설치대수'].replace(np.NaN,1)
pd_data.loc[filter_n,'CCTV설치대수'] = pd_data.loc[filter_n,'CCTV설치대수'].replace(np.NaN,0)

#pd_data.replace({'CCTV설치여부':'Y','CCTV설치대수':np.NaN},1,inplace=True)
#pd_data.replace({'CCTV설치여부':'N','CCTV설치대수':np.NaN},0,inplace=True)

print(pd_data['CCTV설치대수'].isna().value_counts())


# In[5]:


def myfn1(x):
    if type(x) == type(' '):
        if '~' in x:
            m = np.array(x.split('~')).astype(np.float64).mean()
            return str(m)

# 도로폭 : 오류치 처리
# 숫자 ~ 숫자 형태의 문자열 -> 평균치 np.float64 값으로 대체
#print(pd_data['보호구역도로폭'].value_counts())
y = pd_data['보호구역도로폭'].apply(myfn1)
#print(pd_data['보호구역도로폭'].value_counts())
#print(y.value_counts())


# 도로폭 : 결측치 처리
# 전체 도로폭 평균치로 대처
print(pd_data['보호구역도로폭'].isna().value_counts())
y = y.astype(np.float64)
y = y.replace(np.NaN,y.mean())
print(y.isna().value_counts())
pd_data['보호구역도로폭'] = y


# In[6]:


for e in pd_data:
    print(e,pd_data[e].hasnans)
    if pd_data[e].hasnans == True:
        print(pd_data[e].isna().value_counts())


# #### 시설종류
# * dtype : category
# * value : 
# * 결측치 없음
# #### 관할경찰서명
# * dtype : object
# * 결측치 없음
# #### CCTV 설치여부
# * dtype : category
# * value : 'Y','N'
# * 결측치 없음
# #### CCTV 설치대수
# * dtype : np.int64
# * min/ max : 0 / _
# * 결측치 (개)
#     - CCTV 설치여부 'Y' --> 1
#     - CCTV 설치여부 'N' --> 0
# #### 보호구역 도로폭
# * dtype : np.float64
# * min/max
# * 오류치 (   개,처리후 오류치 없음)
#     - 숫자 ~ 숫자 형태의 문자열 -> 평균치 np.float64 값으로 대체
# * 결측치 (  개,처리후 결측 없음)
#     - 전체 평균값으로 대체

# In[7]:


#print(pd_data)
#print(pd_data['보호구역도로폭'].value_counts())
g1 = pd_data.groupby('시설종류')
#print(g1)
#g1.count()
#g1['CCTV설치대수'].sum()


# In[8]:


g2 = pd_data.groupby(['제공기관명','시설종류'])
g2.count()


# In[9]:


pd_data['CCTV설치대수'].mean()


# In[10]:


x = pd_data['보호구역도로폭']
y = pd_data['CCTV설치대수']
np.corrcoef(x,y)

_, axe = plt.subplots()
axe.scatter(x,y)


# In[13]:


# 조건이 1개 일 때
df_t = pd.DataFrame({'a':[1,1,2,2],'b': [5,6,5,6]})
print(df_t)
f1 = df_t['a'] ==1
print("*****")
print(df_t.loc[f1,:])
print("replace")
df_t.loc[f1,'b'] = 100
print(df_t)


# In[ ]:


# 조건이 2개일때
df_t = pd.DataFrame({'a':[1,1,2,2],'b': [5,6,5,6]})
print(df_t)
f1 = df_t['a'] ==1
print("*****")
print(df_t.loc[f1,:])
print("replace")
df_t.loc[f1,'b'] = df_t.loc[f1,'b'].replace(6,100)
print(df_t)


# In[12]:


import sklearn
from sklearn import datasets
x = datasets.load_diabetes()
print(x)

