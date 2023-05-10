#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
pd_data = pd.read_csv('데이터산업_시장규모_20230306152834.csv',encoding='cp949')
current_font_list = matplotlib.rcParams['font.family']

font_path = "C:/Windows/Fonts/H2GTRE.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()

matplotlib.rcParams['font.family'] = [font]+current_font_list


# In[37]:


fig = plt.figure(layout = 'tight',figsize=(6.4*2,4.8))
line_axe = fig.add_subplot(2,1,1)
col_names = pd_data.columns
line_params = ['ro-','g^--','bv:']
# line_axe.set_ylabel('단위 : 억원')
# line_axe.set_title('2015 ~ 2021 산업별 시장 규모')
line_axe.set(title= '2015 ~ 2021 산업별 시장 규모', ylabel = '억원')
for i in range(1,4):   
    #line_axe.plot(pd_data['시점'],pd_data[col_names[i]],line_params[i-1])
    line_axe.plot('시점',col_names[i],line_params[i-1],data=pd_data)
    
pie2015_axe = fig.add_subplot(2,3,4)
pie2015_axe.set_title('2015 구성비',y = -0.1)
pie2015_axe.pie(pd_data.iloc[0,1:])


pie2021_axe = fig.add_subplot(2,3,5)
pie2021_axe.set_title('2021 구성비',y = -0.1)
pie2021_axe.pie(pd_data.iloc[-1,1:],labels = (list('abc')),autopct='%.2f',radius = 1.5)
fig.legend(loc = "lower right")

