#!/usr/bin/env python
# coding: utf-8

# #### heatmap
# - 지자체명vs. 공원구분
# - 평균 공원면적

# In[6]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import matplotlib.ticker as ticker

current_font_list = matplotlib.rcParams['font.family']

font_path = "C:/Windows/Fonts/H2GTRE.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()

matplotlib.rcParams['font.family'] = [font]+current_font_list


# In[7]:


pd_data=pd.read_csv('park.csv')
pd_data


# In[8]:


fig1 = plt.figure(figsize=(15,10))
a = fig1.add_subplot()
g1 = pd_data.groupby(['지자체명','공원구분'])
df_group=g1.mean()
df_group_pv=df_group.reset_index().pivot('지자체명','공원구분','공원면적')
sns.heatmap(df_group_pv,linewidths=0.5,annot=True,fmt=".0f",ax=a,linecolor='black',cmap='crest')


# In[18]:


fig2 = plt.figure(figsize=(15,10))
a = fig2.add_subplot()
g2 = pd_data.groupby(['지자체명','공원구분'])
df_group=g2.count()
df_group_pv=df_group.reset_index().pivot('지자체명','공원구분','공원명')
sns.heatmap(df_group_pv.fillna(0.0),linecolor='black',linewidths=0.5,cmap='RdYlGn_r',annot=True,fmt='.0f')

