#!/usr/bin/env python
# coding: utf-8

# #### 전국일반통행도로표준데이터
#  - 데이터 전처리
#      * 시도명, 지정사유, 지정연도, 도로폭, 도로차로수, 보차분리여부
#  - 결측치 처리(column 개별기준)
#      * 지정사유 결측치 -> 결측치를 사유없음으로 대체
#      * 지정연도 결측치 -> 기준이 명확하지 않으므로 0값으로 대체
#      * 도로 차로수 -> 전체 평균의 도로차로수값으로 대체
#      * 보차분리여부 빈값 N으로 대체
#  - 오류치 처리(unit의 차이)
#      * 시도명 10인 것 강원도로 대체
#  - 이상치 처리 (iqr 사용)
#      * 도로차로수 -> 60
#  - 전처리 내용 정리
#  

# In[1]:


import numpy as np
import pandas as pd

pd_rawdata = pd.read_csv('전국일방통행도로표준데이터.csv',encoding='cp949')

col_select = ['시도명','지정사유','지정연도','도로폭','도로차로수','보차분리여부']
pd_data = pd_rawdata[col_select]


# In[2]:


print(pd_data.shape)
print(pd_data.dtypes)

for e in pd_data:
    print(e,'\t',pd_data[e].hasnans)


# In[3]:


# 시도명
print(pd_data['시도명'].unique())
print(pd_data['시도명'].hasnans)

#결측치 없음

#오류치: 10 --> 강원도
#print(pd_rawdata[pd_rawdata['시도명']== '10'])
filter1 = pd_rawdata['시도명']== '10'
pd_data.loc[filter1,'시도명'] = '강원도'
#pd_data[filter1]['시도명'] = '강원도' warning
print(pd_data['시도명'].unique())


# In[4]:


# 지정사유
print(pd_data['지정사유'].unique())
print(pd_data['지정사유'].hasnans)

# 결측치
na_filter = pd_data['지정사유'].isna()
#print(na_filter.value_counts())
pd_data.loc[na_filter,'지정사유'] = '불분명'  #pd_data['지정사유'].fillna('불분명')

# 오류치 : 같은내용 다른이름 정리
def e1(x):
    if '원활' in x:
        return '원활'
    elif '불편' in x:
        return '불편'
    elif '안전' in x:
        return '안전'
    elif '혼잡' in x:
        return '혼잡'
    else:
        return x

pd_data.loc[:,'지정사유'] = pd_data.loc[:,'지정사유'].apply(e1)

# 이상치(outlier): 없음

print(pd_data['지정사유'].unique())
print(pd_data['지정사유'].hasnans)


# In[5]:


#지정연도
print(pd_data['지정연도'].unique())
print(pd_data['지정연도'].hasnans)

# 결측치
na_filter = pd_data['지정연도'].isna()
print(na_filter.value_counts())
pd_data.loc[na_filter,'지정연도'] = 0

print(pd_data['지정연도'].unique())
print(pd_data['지정연도'].hasnans)


# In[6]:


# 도로폭
print(pd_data['도로폭'].unique())
print(pd_data['도로폭'].hasnans)

#결측치 오류치 없음

# 이상치 : upper 보다 큰 값을 np.NaN으로 교체, 후에 dropna() 이용 샘플 삭제.
#print(pd_data['도로폭'].describe())
q1,q3 = pd_data['도로폭'].quantile([0.25,0.75])
iqr = q3 - q1
upper = q3 + 1.5 * iqr
lower = q1 - 1.5 * iqr
print(lower,upper)
filter1 = pd_data['도로폭'] > upper
print(filter1.value_counts())
pd_data.loc[filter1,'도로폭'] = np.NaN


print(pd_data['도로폭'].unique())
print(pd_data['도로폭'].hasnans)


# In[11]:


# 도로차로수
print(pd_data['도로차로수'].unique())
print(pd_data['도로차로수'].hasnans)

# 결측치 : 1개 샘플, dropna()이용 제거
na_filter = pd_data['도로차로수'].isna()
print(na_filter.value_counts())

#오류치 : 60 1개 샘플, -->np.NaN를 대체 후에 dropna() 제거

filter1 = pd_data['도로차로수'] == 60
print(filter1.value_counts())
pd_data.loc[filter1,'도로차로수'] = np.NaN

# 이상치: 없음
print(pd_data['도로차로수'].unique())
print(pd_data['도로차로수'].hasnans)


# In[17]:


# 보차분리여부
print(pd_data['보차분리여부'].unique())
print(pd_data['보차분리여부'].hasnans)

# 결측치 : ' ' 1개 샘플 np.NaN으로 대체 후에 dropna()로 제거
na_filter = pd_data['보차분리여부'] == ' '
print(na_filter.value_counts())
pd_data.loc[na_filter,'보차분리여부'] = np.NaN

#오류치, 이상치 없음
print(pd_data['보차분리여부'].unique())
print(pd_data['보차분리여부'].hasnans)


# In[20]:


pd_data_f = pd_data.dropna()
print(pd_data.shape)
print(pd_data_f.shape)

