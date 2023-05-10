#!/usr/bin/env python
# coding: utf-8

# #### 전국평생학습강좌표준데이터
# - drop : 교육시작시각,교육종료시각,강좌내용,운영기관전화번호
# - columm 별 적절한 dtype 지정 - > astype (원본값 수정방법, 1: 현재값 업데이트, 2: astype의 키워드 옵션사용)
#     * 수치값 : np.int64 / np.float64
#     * 종류를 구분하는 문자열(label): category
#     * 날짜 : np.datetime64
#     * 이외 : object
# - 전체 DataFrame에 대한 describe 결과보기(describe 키워드 옵션 --> Documentation 참조)
# - 항목(columm)별 결측지/오류치/이상치 갯수 파악

# In[20]:


import numpy as np
import pandas as pd

pd_data = pd.read_csv('전국평생학습강좌표준데이터.csv',encoding='cp949')

#pd_data.drop(['교육시작시각','교육종료시각','강좌내용','운영기관전화번호'],axis = 1,inplace=True)
pd_data.head()
pd_data.dtypes


# In[29]:


pd_data[['교육시작일자','교육종료일자','접수시작일자','접수종료일자','데이터기준일자']].astype(np.datetime64,copy=False)


# In[31]:


day = pd_data['운영요일'].astype('category')
#day
day_f = pd.DataFrame({'label':day,'codes':day.cat.codes})
day_f


# In[42]:


print(pd_data.describe(exclude=np.int64))
print(pd_data.describe(exclude=object))


# In[44]:


pd_data['교육종료일자'].hasnans

