#!/usr/bin/env python
# coding: utf-8

# # 시도별 화재사건 현황분석
# - 2010~2021년 시도별 건수
# - 사건 건수와 사망자 상관관계
# - 2021년 기준 재산 피해가 가장 높은 시도

# In[1]:


from google.colab import drive
drive.mount('/content/drive')


# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


get_ipython().system('sudo apt-get install -y fonts-nanum')
get_ipython().system('sudo fc-cache -fv')
get_ipython().system('rm ~/.cache/matplotlib -rf')


# In[ ]:


plt.rc('font', family='NanumBarunGothic')


# In[ ]:


pd_data = pd.read_csv('/content/drive/MyDrive/코리아_IT/데이터분석/시도별_화재발생_현황_총괄__20230307152937.csv', encoding = 'cp949')
pd_data.head()


# In[ ]:


pd_data.sort_values('행정구역별', inplace=True)
#print(pd_data.head())
print(pd_data.groupby('행정구역별')['시점'].count())
#print(pd_data['시점'].value_counts())


# In[ ]:


filter1 = pd_data['행정구역별'] == '세종특별자치시'
pd_data[filter1].sort_values('시점')


# 세종시가 2012년 부터 정식으로 출범하였기에 2010,2011년의 자료가 없다.<br>
# 그러한 상황을 고려하여 2012년 부터 2021년까지의 사건을 기준으로 한다.

# ## 시도별 사건 총 합산

# In[ ]:


filter2 = pd_data['시점'] > 2011
df1 = pd_data[filter2]
df1.sort_values(['행정구역별','시점'], inplace=True)
numbers = [(lambda x: x)(i) for i in range(len(df1))]
print(numbers)
df1.index = numbers
df1.head(12)


# In[ ]:


df1.loc[0, '사망 (명)']

for i in range(len(df1)):
    if '-' in df1.loc[i, '사망 (명)']:
        df1.loc[i, '사망 (명)'] = '0'

df1 = df1.astype({'사망 (명)' : 'int'})
df1


# In[ ]:


list_value = list(df1.groupby('행정구역별')['건수 (건)'].sum().values)
print(len(list_value))
list_index = list(df1.groupby('행정구역별')['건수 (건)'].sum().index)
print(len(list_index))
list_death = list(df1.groupby('행정구역별')['사망 (명)'].sum().values)


#g1 = df1.groupby('행정구역별')
#g1['건수 (건)', '사망 (명)'].sum()


# In[ ]:


event1 = pd.DataFrame(zip(list_index,list_value,list_death))
event1.columns = ['행정구역', '건수', '사망자']
event1.sort_values('건수',ascending=False, inplace=True)
numbers = [(lambda x: x)(i) for i in range(len(event1))]
print(numbers)
event1.index = numbers
event1


# In[ ]:


lista = list(event1['건수'])
print(lista)


# In[ ]:


fig = sns.catplot(data=event1, kind='bar', x="행정구역", y="건수")
fig.fig.set_size_inches(20,6)


# In[ ]:


df1.columns


# In[ ]:


sns.heatmap(df1[['건수 (건)', '사망 (명)', '부상 (명)', '재산피해(계) (천원)', '부동산 (천원)','동산 (천원)' ]].corr(),
            annot=True, cmap='YlOrRd')


# In[ ]:


colors = sns.color_palette('pastel')[0:5]


# In[ ]:


plt.pie(list_value, labels = list_index, radius = 4.0 , textprops ={"fontsize":15},startangle = 270, colors = colors, autopct='%.0f%%')
plt.show()


# In[ ]:


sns.lineplot(data=df1, x=df1[filter2]['시점'], y=df1[filter2]['사망 (명)'])


# ## 총인구대비 사망자 비율 시각화

# In[ ]:


# 총 인구 대비 사망자비율

human = pd.read_csv('/content/drive/MyDrive/코리아_IT/데이터분석/시도별_주민등록_인구현황_20230308152235.csv',encoding='cp949')
human.rename(columns={'행정구역명':'행정구역'}, inplace=True)
human


# In[ ]:


event1


# In[ ]:


event1.loc[0,'행정구역'][0:2]


# In[ ]:


for i in range(len(event1)):
    if event1.loc[i, '행정구역'] == '경상남도':
        event1.loc[i, '행정구역'] ='경남'
    elif event1.loc[i, '행정구역'] == '경상북도':
        event1.loc[i, '행정구역'] ='경북'
    else:
        event1.loc[i, '행정구역'] = event1.loc[i,'행정구역'][0:2]

event1


# In[ ]:


df2 = pd.merge(event1, human, on="행정구역")
df2


# In[ ]:


df2['인구대비사망자'] = df2['사망자']/df2['총인구']*100


# In[ ]:


df2.sort_values('인구대비사망자',ascending=False, inplace=True)
numbers = [(lambda x: x)(i) for i in range(len(df2))]
print(numbers)
df2.index = numbers
df2


# 순수 사망자 수를 따지면 경기, 서울, 경남 순이며 <br>
# 인구대비사망자 비율을 보았을 때 강원, 경남, 제주 순이다. <br>
# 그렇다면 사망자 수와 인구수와의 상관관계를 살펴보겠다.

# In[ ]:


fig = sns.catplot(data=event1, kind='bar', x="행정구역", y="사망자")
fig.fig.set_size_inches(20,6)


# In[ ]:


fig = sns.catplot(data=df2, kind='bar', x="행정구역", y="인구대비사망자")
fig.fig.set_size_inches(20,6)


# 인구가 많을 수록 사망자가 많다는 상관관계를 얻어내었다.

# In[ ]:


sns.heatmap(df2[['사망자', '총인구']].corr(),
            annot=True, cmap='YlOrRd')


# In[ ]:


pd_data.head()


# In[ ]:


fig = sns.catplot(data=pd_data, x = '행정구역별', y = '부상 (명)', hue='시점' ,dodge=True, kind='swarm')
fig.fig.set_size_inches(20,6)


# In[ ]:


sns.pairplot(pd_data, hue='시점')


# In[ ]:




