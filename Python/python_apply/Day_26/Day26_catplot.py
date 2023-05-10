#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd_tips = sns.load_dataset('tips')


# In[18]:


#sns.catplot(data=pd_tips, x='day',y='total_bill',hue='smoker',dodge=True,kind='point')
#sns.catplot(data=pd_tips, x='day',y='total_bill',jitter=0.2,hue='smoker',dodge=True)
sns.relplot(data=pd_tips, x='day',y='total_bill')


# In[29]:


sns.catplot(data=pd_tips, x='total_bill',y='day',hue='smoker',dodge=True,kind="violin",split=True,inner='stick')
sns.catplot(data=pd_tips, x='day',y='total_bill',hue='smoker',dodge=True,kind="swarm")
sns.catplot(data=pd_tips, x='day',y='total_bill',hue='smoker',dodge=True,kind="boxen")
sns.catplot(data=pd_tips, x='day',hue='smoker',dodge=True,kind="count")
sns.catplot(data=pd_tips, x='day',y='total_bill',hue='smoker',dodge=True,kind="box")


# In[30]:


g=sns.catplot(data=pd_tips, x='total_bill',y='day',hue='smoker',dodge=True,kind="violin",split=True)
sns.swarmplot(data=pd_tips, x= 'total_bill',y='day',color='k',size=3,ax=g.ax)


# In[31]:


#pandas에도 plot기능이 있음
pd_tips.plot(x='day',y='total_bill')

