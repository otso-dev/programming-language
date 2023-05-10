#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd

pd_data = pd.read_csv('전국평생학습강좌표준데이터.csv',encoding='cp949')
drop_list=['교육시작시각','교육종료시각','강좌내용','운영기관전화번호']
pd_data.drop(drop_list,axis = 1,inplace = True)
# for e in enumerate(pd_data.columns):
#     print(e)
print(pd_data.dtypes)


# In[17]:


for col_name in pd_data.columns:
    if '일자' in col_name:
        pd_data[col_name]=pd_data[col_name].astype(np.datetime64,copy = False)
    elif ('구분' in col_name) or ('여부' in col_name) or ('코드' in col_name):
        pd_data[col_name] = pd_data[col_name].astype('category')
        
print(pd_data.dtypes)


# In[30]:


t = []
for col_name in pd_data.columns:
    if pd_data[col_name].hasnans == True:
       # print(col_name)
        cnt_s = pd_data[col_name].isna().value_counts()
        cnt = cnt_s.to_numpy()
        t.append([col_name,cnt[0],cnt[1]])
    #print(pd_data[col_name].isna().value_counts)
#print(t)
t = np.array(t)
missing_df = pd.DataFrame(t[:,1:],index=t[:,0],columns=['value_count','NaN_count'])
#missing_df.index = missing_df['col_name']
missing_df


# In[33]:


f1 = pd_data['운영요일'].isna()
#pd_data['운영요일'][f1]
pd_data['운영요일'].value_counts()

# 운영요일별 카운트시 운영요일을 특정할 수 없으므로,
# 삭제 조치하도록 함


# In[53]:


pd_data['교육장소'].value_counts()

# 교육방법 구분이 온라인으로 되어있을 경우, 온라인으로 결치를 대체
# 그렇지 않을경우, 삭제.
pd_data['교육방법구분'].value_counts()
filter1 = pd_data['교육장소'].isna()
#print(pd_data['교육방법구분'][filter1].value_counts())

filter2 = pd_data['교육방법구분'] == '온라인'
pd_data['교육장소'][filter2] = '온라인'
pd_data['교육장소'].isna().value_counts()

# 접수시작/종료일자 결측치
# 교육방법 구분이 온라인을 되어있을 경우 1월1일 부터 12월 31까지의 값으로 대체
# 그렇지 않을경우, 삭제


# In[54]:


for i in range(pd_data.shape[0]):
    row = pd_data.iloc[i,:]
    if (row['교육장소'] == np.NaN) and (row['교육방법구분']=='온라인'):
        row['교육장소'] = '온라인'


# In[35]:


pd_data['선정방법구분'].value_counts()
# 결측치 삭제


# In[ ]:




