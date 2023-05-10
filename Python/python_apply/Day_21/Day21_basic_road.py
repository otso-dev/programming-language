#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

pd_rawdata = pd.read_csv('전국일방통행도로표준데이터.csv',encoding='cp949')

col_select = ['시도명','지정사유','지정연도','도로폭','도로차로수','보차분리여부']
pd_data = pd_rawdata[col_select]


# In[2]:


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


# In[3]:


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


# In[4]:


#지정연도
print(pd_data['지정연도'].unique())
print(pd_data['지정연도'].hasnans)

# 결측치
na_filter = pd_data['지정연도'].isna()
print(na_filter.value_counts())
pd_data.loc[na_filter,'지정연도'] = 0

print(pd_data['지정연도'].unique())
print(pd_data['지정연도'].hasnans)


# In[5]:


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


# In[6]:


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


# In[7]:


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


# In[8]:


pd_data_f = pd_data.dropna()
print(pd_data.shape)
print(pd_data_f.shape)


# In[9]:


filename = '전국일방통행도로표준데이터(정제완료).csv'
pd_data_f.to_csv(filename,index=False)


# In[ ]:


with open('전국일반통행도로표준데이터(정제완료).pickle','wb') as f:
    pickle.dump(pd_data,f)

