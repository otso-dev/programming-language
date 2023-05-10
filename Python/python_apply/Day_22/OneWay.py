#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd_raw = pd.read_csv('전국일방통행도로표준데이터.csv', encoding='cp949')

#print(pd_raw[pd_raw['시도명']=='10'])

col_select = ['시도명', '지정사유', '지정연도', '도로폭', '도로차로수', '보차분리여부']
pd_data = pd_raw[col_select]


# In[2]:


def df_check(df):
    print(df.shape)
    print(df.dtypes)
    return df.shape[0]

total_count = df_check(pd_data)


# In[3]:


# 시도명
print(pd_data['시도명'].unique())
print(pd_data['시도명'].hasnans)

# 결측치: 없음

# 오류치 10-->'강원도'
#print(pd_data[pd_data['시도명']=='10'])
#pd_data.loc[:, '시도명'] = pd_data.loc[:, '시도명'].replace('10', '강원도')
filter1 = pd_data['시도명']=='10'
pd_data.loc[filter1, '시도명'] = '강원도'

# 이상치: 없음


# In[4]:


# 지정사유
print(pd_data['지정사유'].unique())
print(pd_data['지정사유'].hasnans)

# 결측치: '사유불분명' 으로 기재.
na_filter = pd_data['지정사유'].isna()
print(na_filter.value_counts())
pd_data.loc[na_filter, '지정사유'] = '사유불분명'

# 오류치: '원활' 이 들어간 사유는 '통행원활'로 정정
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
    
pd_data.loc[:, '지정사유'] = pd_data.loc[:, '지정사유'].apply(e1)

print(pd_data['지정사유'].unique())
print(pd_data['지정사유'].hasnans)

# 이상치: 없음


# In[5]:


#지정연도
print(pd_data['지정연도'].unique())
print(pd_data['지정연도'].hasnans)

#결측치
na_filter = pd_data['지정연도'].isna()
print(na_filter.value_counts())
#print(pd_raw.loc[na_filter, :])
#filter1 = pd_data['지정연도']==2017
#print(pd_raw.loc[filter1,:])
pd_data.loc[na_filter, '지정연도'] = 0.0

print(pd_data['지정연도'].unique())
print(pd_data['지정연도'].hasnans)


# In[6]:


#도로폭
print(pd_data['도로폭'].unique())
print(pd_data['도로폭'].hasnans)

# 결측치: 없음

# 오류치: 없음

# 이상치: np.NaN 값으로 대체 후, dropna()사용해 제거
print(pd_data['도로폭'].describe())
q1, q3 = pd_data['도로폭'].quantile([.25, .75])
iqr = q3 - q1
upper = q3 + 1.5*iqr
lower = q1 - 1.5*iqr
print(iqr, upper, lower)
filter1 = pd_data['도로폭']>upper
print(filter1.value_counts())
pd_data.loc[filter1, '도로폭']=np.NaN


print(pd_data['도로폭'].unique())
print(pd_data['도로폭'].hasnans)


# In[7]:


# 도로차로수
print(pd_data['도로차로수'].unique())
print(pd_data['도로차로수'].hasnans)

# 결측치: dropna() 이용 샘플 삭제
na_filter = pd_data['도로차로수'].isna()
print(na_filter.value_counts())

# 오류치: np.NaN으로 대체, dropna() 이용 샘플 삭제
pd_data['도로차로수'].value_counts()
filter1 = pd_data.loc[:, '도로차로수']==60
pd_data.loc[filter1, '도로차로수'] = np.NaN

print(pd_data['도로차로수'].unique())
print(pd_data['도로차로수'].hasnans)


# In[8]:


# 보차 분리여부
print(pd_data['보차분리여부'].unique())
print(pd_data['보차분리여부'].hasnans)

# 결측치: ' ' 값 np.NaN으로 변경, 차후 dropna()이용해 삭제
empty_filter = pd_data.loc[:, '보차분리여부']== ' '
print(empty_filter.value_counts())
print(pd_data['보차분리여부'].value_counts())

print(pd_raw[empty_filter])
pd_data.loc[empty_filter, '보차분리여부']=np.NaN


# In[9]:


pd_data = pd_data.dropna()
df_check(pd_data)


# In[11]:


# csv
pd_data.to_csv('전국일방통행도로표준데이터_pass1.csv')

#pickle
with open('전국일방통행도로표준데이터_pass1.pickle', 'wb') as f:
    pickle.dump(pd_data, f)
    


# In[ ]:





# In[4]:


df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])

print(df.apply(np.sqrt))
print(df)

