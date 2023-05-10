#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

pd_data = pd.read_csv('전국푸드트럭허가구역표준데이터.csv',encoding='cp949')


# In[17]:


for i in enumerate(pd_data.columns):
    pass
    #print(i)
print(pd_data.shape)
num_descr_df = pd_data.describe()
#print(num_descr_df.columns)
#print(pd_data.columns)
lista = list(pd_data.columns)
for e in list(num_descr_df.columns):
    lista.remove(e)
print(len(pd_data.columns),len(lista))
#print(pd_data.dtypes)
#pd_data[lista].describe()



# In[24]:


x = pd_data['허가구역운영시작일자'].astype(np.datetime64)
# print(x.dt.year)
# print(x.dt.month)
# print(x.dt.day)
#print(x.dt.day + 5)


# In[39]:


#pd_data['허가구역휴무일'].value_counts()
x=pd_data['허가구역휴무일'].astype('category')
#print(x)
#print(x.cat.codes)
df1 = pd.DataFrame({'label':x,'code':x.cat.codes})
df1.sort_values(['code','label'],ascending=False)


# In[3]:


national_site_count = pd_data.shape[0]
print(national_site_count)
pd_data['시도명'].value_counts()


# In[9]:


#print(pd_data['시도명'].describe())
#print(pd_data['푸드트럭운영대수'].describe())
print(pd_data[['시도명','푸드트럭운영대수']].describe())


# In[5]:


pd_data['푸드트럭운영대수'].sum()


# In[6]:


sub_data = pd_data[['시도명','푸드트럭운영대수']]
sub_data.groupby('시도명').sum()


# In[58]:


def myfn(x):
    #print(x,type(x))
    #np.sum(x['푸드트럭운영대수'])*100
    return np.sum(x)*100

sub_data = pd_data[['시도명','푸드트럭운영대수']]
#print(sub_data)
g1 = sub_data.groupby('시도명')
# g1.sum()
# g1.count()
# g1.std()
# g1.describe()
# g1.aggregate([np.sum,np.mean,np.std])
# g1.aggregate(lambda x : np.sum(x)*100)
# g1.apply(lambda x : np.sum(x)*100)
# g1.aggregate(myfn)
#g1.apply(myfn)


# In[62]:


x=pd_data['푸드트럭운영대수']
x.replace(np.NaN,0.0)

