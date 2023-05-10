#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

pd_raw = pd.read_csv('전국노인장애인보호구역표준데이터.csv',encoding='cp949')
col_selected = ['시도명','제한속도','CCTV설치여부','CCTV설치대수','보호구역도로폭']
pd_data = pd_raw[col_selected]


# In[2]:


for e in pd_data:
    print(e,pd_data[e].hasnans)


# In[3]:


#시도명
print(pd_data['시도명'].unique())
print(pd_data['시도명'].hasnans)
#결측치 이상치 오류치 없음


# In[4]:


#제한속도
print(pd_data['제한속도'].unique())
print(pd_data['제한속도'].hasnans)
print(pd_data['제한속도'].describe())

# 이상치

q1, q3 = pd_data['제한속도'].quantile([0.25,0.75])
iqr = q3 - q1
upper = q3 + 1.5 * iqr
lower = q1 - 1.5 * iqr
print(q1,q3,iqr,lower,upper)


# In[5]:


#CCTV설치여부
print(pd_data['CCTV설치여부'].unique())
print(pd_data['CCTV설치여부'].hasnans)
#결측치 이상치 오류치 없음


# In[6]:


#CCTV설치대수
print(pd_data['CCTV설치대수'].unique())
print(pd_data['CCTV설치대수'].hasnans)
#결측치 설치여부가 Y이면 1 N이면 0으로 대체
filter_y = pd_data['CCTV설치여부'] == 'Y'
filter_n = pd_data['CCTV설치여부'] == 'N'
pd_data.loc[filter_y,'CCTV설치대수'] = pd_data.loc[filter_y,'CCTV설치대수'].replace(np.NaN,1)#fillna를 써도 됨
pd_data.loc[filter_n,'CCTV설치대수'] = pd_data.loc[filter_n,'CCTV설치대수'].replace(np.NaN,1)

print(pd_data['CCTV설치대수'].unique())
print(pd_data['CCTV설치대수'].hasnans)


# In[7]:


#'보호구역도로폭'
#print(pd_data['보호구역도로폭'].unique())
#print(pd_data['보호구역도로폭'].hasnans)
#결측치는 도로폭의 평균치로 대체
#오류치 숫자 ~ 숫자의 형태는 분리후 np.float64로 대체
def myfn1(x):
    if (x == np.NaN) or (type(x) == type(1.0)):
        return x
    if '~' in x:
        m = np.mean(np.array(x.split('~')).astype(np.float64))
        return str(m)
    else:
        return x
pd_data['보호구역도로폭'] = pd_data['보호구역도로폭'].apply(myfn1).astype(np.float64)
#print(pd_road_f.value_counts())
#print(pd_data['보호구역도로폭'].value_counts())
pd_data['보호구역도로폭'].replace(np.NaN,pd_data['보호구역도로폭'].mean(),inplace=True)
print(pd_data['보호구역도로폭'].value_counts())


# In[8]:


for e in pd_data:
    print(e,pd_data[e].hasnans)


# In[10]:


filename = '전국노인장애인보호구역표준데이터(정제완료).csv'

pd_data.to_csv(filename,index=False)

