#!/usr/bin/env python
# coding: utf-8

# ### 데이터 산업별 시장규모
#      * 데이터 산업별 시장규모 성창추이 ->line
#      * 2015,2021년도 산업별 비율 ->pie

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
pd_data = pd.read_csv('데이터산업_시장규모_20230306152834.csv',encoding='cp949')


# In[2]:


current_font_list = matplotlib.rcParams['font.family']

font_path = "C:/Windows/Fonts/H2GTRE.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()

matplotlib.rcParams['font.family'] = [font]+current_font_list


# In[13]:


def myfn1(x):
    if 'e' in x:
        return x.split(' ')[0]
    else:
        return x
pd_data['시점'] = pd_data['시점'].apply(myfn1)
print(pd_data['시점'])


# In[24]:


fig1 = plt.figure(figsize=(15,10))
all_data = fig1.add_subplot(2,1,1)
x = pd_data['시점']
y1 = pd_data['데이터 처리 및 관리 솔루션 개발·공급업']
y2 = pd_data['데이터 구축 및 컨설팅 서비스업']
y3 = pd_data['데이터 판매 및 제공 서비스업']
all_data.plot(x,y1,color = 'red',label = '데이터 처리 및 관리',linewidth = 3)
all_data.plot(x,y2,color = 'black',label = '데이터 구축 및 컨설팅',linewidth = 3,linestyle='--')
all_data.plot(x,y3,color = 'green',label = '데이터 판매 및 제공',linewidth = 3,linestyle='-.')
all_data.set_title('데이터 산업별 시장규모 성창추이(2015~2021)')
all_data.legend()

filter1 = pd_data['시점'] == '2015'
data_15 = pd_data[filter1]
total_15 = data_15['데이터 처리 및 관리 솔루션 개발·공급업'].sum() + data_15['데이터 구축 및 컨설팅 서비스업'].sum() + data_15['데이터 판매 및 제공 서비스업'].sum()
data_sol = data_15['데이터 처리 및 관리 솔루션 개발·공급업'].sum()
data_con = data_15['데이터 구축 및 컨설팅 서비스업'].sum()
data_sales = data_15['데이터 판매 및 제공 서비스업'].sum()
share = [data_sol/total_15,data_con/total_15,data_sales/total_15]
labels = ['데이터처리 및 관리', '데이터 구축 및 컨설팅', '데이터 판매']
pie_15 = fig1.add_subplot(2,2,3)
pie_15.pie(share,labels=labels,autopct='%1.1f%%')
pie_15.set_title('2015년도 데이터 산업 비율')


filter1 = pd_data['시점'] == '2021'
data_21 = pd_data[filter1]
total_21 = data_21['데이터 처리 및 관리 솔루션 개발·공급업'].sum() + data_21['데이터 구축 및 컨설팅 서비스업'].sum() + data_21['데이터 판매 및 제공 서비스업'].sum()
data21_sol = data_21['데이터 처리 및 관리 솔루션 개발·공급업'].sum()
data21_con = data_21['데이터 구축 및 컨설팅 서비스업'].sum()
data21_sales = data_21['데이터 판매 및 제공 서비스업'].sum()
share21 = [data21_sol/total_15,data21_con/total_15,data21_sales/total_15]
labels = ['데이터처리 및 관리', '데이터 구축 및 컨설팅', '데이터 판매']
pie_21 = fig1.add_subplot(2,2,4)
pie_21.pie(share21,labels=labels,autopct='%1.1f%%')
pie_21.set_title('2021년도 데이터 산업 비율')


# In[15]:


fig1.savefig('데이터 산업별 시장규모.png')

