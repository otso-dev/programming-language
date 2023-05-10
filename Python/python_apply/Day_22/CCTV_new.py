#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd_rawdata = pd.read_csv('전국어린이보호구역표준데이터.csv', encoding='cp949')

#print(pd_rawdata.columns)

column_selection = ['시설종류', '관할경찰서명', 'CCTV설치여부','CCTV설치대수','제공기관명', '보호구역도로폭']
pd_data = pd_rawdata[column_selection]
del pd_rawdata
#print(pd_rawdata[:3])


# In[2]:


print(pd_data.columns)
print(pd_data.dtypes)

print(pd_data['보호구역도로폭'].value_counts())
print(pd_data['보호구역도로폭'].isna().value_counts())

pd_data['시설종류'] = pd_data['시설종류'].astype('category')
pd_data['CCTV설치여부'] = pd_data['CCTV설치여부'].astype('category')
#print(pd_data.dtypes)


# In[3]:


# 결측치 확인

#print(pd_data.shape)
#print(pd_data.describe(include='all'))

for e in pd_data:
    print(e, pd_data[e].hasnans)
    if pd_data[e].hasnans==True:
        print(pd_data[e].isna().value_counts())


# In[4]:


# CCTV 설치대수: 결측치 처리
# CCTV 설치여부 Y --> 1
# CCTV 설치여부 N --> 0
print(pd_data['CCTV설치대수'].isna().value_counts())
filter_y = pd_data['CCTV설치여부'] == 'Y'
filter_n = pd_data['CCTV설치여부'] == 'N'
pd_data.loc[filter_y, 'CCTV설치대수'] = pd_data.loc[filter_y, 'CCTV설치대수'].replace(np.NaN, 1)
pd_data.loc[filter_n, 'CCTV설치대수'] = pd_data.loc[filter_n, 'CCTV설치대수'].replace(np.NaN, 0)

#pd_data.replace({'CCTV설치여부':'Y', 'CCTV설치대수':np.NaN}, {'CCTV설치여부':'Y', 'CCTV설치대수':1}, inplace=True)
#pd_data.replace({'CCTV설치여부':'N', 'CCTV설치대수':np.NaN}, {'CCTV설치여부':'N', 'CCTV설치대수':0}, inplace=True)

# 잘못된 코드.
#pd_data.replace({'CCTV설치여부':'N', 'CCTV설치대수':np.NaN}, 0, inplace=True)
#pd_data.replace({'CCTV설치여부':'Y', 'CCTV설치대수':np.NaN}, 1, inplace=True)

print(pd_data['CCTV설치대수'].isna().value_counts())


# In[5]:


pd_data['CCTV설치여부'].value_counts()


# In[6]:


def myfn1(x):
    if type(x) == type(' '):
        if '~' in x:
            m = np.array(x.split('~')).astype(np.float64).mean()
            return str(m)

# 도로폭: 오류치 처리
# '숫자a~숫자b' 형태의 문자열 --> '숫자a'와 '숫자b'의 평균치(np.float64) 값으로 대체
#print(pd_data['보호구역도로폭'].value_counts())
y = pd_data['보호구역도로폭'].apply(myfn1)
#print(pd_data['보호구역도로폭'].value_counts())
#print(y.dtype)
#print(y.value_counts())


# 도로폭: 결측치 처리
# 전체 도로폭 평균치로 대체.
print(pd_data['보호구역도로폭'].isna().value_counts())
y = y.astype(np.float64)
y = y.replace(np.NaN, y.mean())
print(y.isna().value_counts())
pd_data['보호구역도로폭'] = y


# In[7]:


for e in pd_data:
    print(e, pd_data[e].hasnans)
    if pd_data[e].hasnans==True:
        print(pd_data[e].isna().value_counts())


# In[8]:


pd_data['제공기관명'].unique()
pd_data['지자체명'] = pd_data['제공기관명'].apply(lambda x: x.split()[0])
# apply, map, applymap, aggregate, agg


# In[9]:


x = pd_data['지자체명'].unique()
print(len(x))


# In[10]:


pd_data.to_csv('전국어린이보호구역표준데이터_pass1.csv')

