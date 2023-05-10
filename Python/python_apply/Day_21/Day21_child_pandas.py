#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

pd_raw = pd.read_csv('전국어린이보호구역표준데이터.csv',encoding='cp949')
col_selected = ['시설종류','관할경찰서명','CCTV설치여부','CCTV설치대수','제공기관명','보호구역도로폭']
pd_data = pd_raw[col_selected]


# In[2]:


for e in pd_data:
    print(e,pd_data[e].hasnans)


# In[3]:


# 시설종류
print(pd_data['시설종류'].unique())
print(pd_data['시설종류'].hasnans)

#결측치 이상치 없음

#오류치 : 초등학교+어린이집 -> np.NaN로 대체 후 dropnp로 제거
filter1 = pd_data['시설종류'] =='초등학교+어린이집'
print(filter1.value_counts())
pd_data.loc[filter1,'시설종류'] = np.NaN
print(pd_data['시설종류'].unique())
print(pd_data['시설종류'].hasnans)


# In[4]:


#관할경찰서명
#print(pd_data['관할경찰서명'].unique())
print(pd_data['관할경찰서명'].hasnans)
#결측치 이상치 없음

# 오류치 끝에 경찰서가 없는 단어들은 경찰서를 붙여주기
def e1(x):
    if '경찰서' not in x:
        return x+'경찰서'
    else:
        return x
pd_data.loc[:,'관할경찰서명'] = pd_data.loc[:,'관할경찰서명'].apply(e1)

#print(pd_data['관할경찰서명'].unique())
print(pd_data['관할경찰서명'].hasnans)


# In[5]:


#CCTV설치여부
print(pd_data['CCTV설치여부'].unique())
print(pd_data['CCTV설치여부'].hasnans)
#결측치 이상치 오류치 없음


# In[6]:


#CCTV설치대수
print(pd_data['CCTV설치대수'].unique())
print(pd_data['CCTV설치대수'].hasnans)
na_filter = pd_data['CCTV설치대수'].isna()
print(na_filter.value_counts())
#결측치 -> 설치여부가 Y인것은 1로 설치여부가 N인것은 0으로
filter_y = pd_data['CCTV설치여부'] == 'Y'
filter_n = pd_data['CCTV설치여부'] == 'N'
pd_data.loc[filter_y,'CCTV설치대수'] = pd_data.loc[filter_y,'CCTV설치대수'].replace(np.NaN,1)
pd_data.loc[filter_n,'CCTV설치대수'] = pd_data.loc[filter_n,'CCTV설치대수'].replace(np.NaN,1)

print(pd_data['CCTV설치대수'].unique())
print(pd_data['CCTV설치대수'].hasnans)


# In[7]:


# 이상치 6이상이면 np.NaN으로 대체 dropna로 제거
q1,q3 = pd_data['CCTV설치대수'].quantile([0.25,0.75])
iqr = q3 - q1
upper = q3 + 1.5 * iqr
lower = q1 - 1.5 * iqr
print(upper,lower)
filter1 = pd_data['CCTV설치대수'] > upper
#print(filter1.value_counts())
pd_data.loc[filter1,'CCTV설치대수'] = np.NaN
print(pd_data['CCTV설치대수'].unique())
print(pd_data['CCTV설치대수'].hasnans)


# In[8]:


# 제공기관명
print(pd_data['제공기관명'].unique())
print(pd_data['제공기관명'].hasnans)
#결측치 오류치 이상치 없음


# In[9]:


# '보호구역도로폭'
#print(pd_data['보호구역도로폭'].unique())
print(pd_data['보호구역도로폭'].hasnans)
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
print(y.value_counts())


# 도로폭 : 결측치 처리
# 전체 도로폭 평균치로 대처
#print(pd_data['보호구역도로폭'].isna().value_counts())
y = y.astype(np.float64)
y = y.replace(np.NaN,y.mean())
#print(y.isna().value_counts())
pd_data['보호구역도로폭'] = y
print(pd_data['보호구역도로폭'].value_counts())


# In[12]:


# 시도명 추가
def mysplit(x):
    return x.split(' ')[0]
new_df = pd_data['제공기관명'].apply(mysplit)
print(pd_data['제공기관명'])
pd_data.insert(0,'시도명',new_df)
print(pd_data)
#apply, map, applymap, aggreagate, agg


# In[13]:


pd_data_f = pd_data.dropna()
print(pd_data.shape)
print(pd_data_f.shape)


# In[14]:


filename = '전국어린이보호구역표준데이터(정제완료).csv'
pd_data_f.to_csv(filename,index=False)

