#!/usr/bin/env python
# coding: utf-8

# In[4]:


import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[5]:


df_tips = sns.load_dataset('tips')
print(df_tips)


# In[24]:


#hue, style, size
#sns.relplot(data=df_tips, x='total_bill',y='tip',hue='sex',style='smoker',size='size')
# row, col
sns.relplot(data=df_tips, x='total_bill',y='tip',col='sex',row='smoker',size='size',hue='size')


# In[30]:


x=sns.relplot(data=df_tips, x='total_bill',y='tip',kind='line')
print(x.figure,type(x.figure))
x.figure.set_facecolor('gray')

print(x.axes,type(x.axes[0][0]))


# In[29]:


fig1 = plt.figure()
a = fig1.add_subplot()
#sns.scatterplot(data=df_tips,x='total_bill',y='tip',hue='smoker',ax=a)
sns.lineplot(data=df_tips,x='total_bill',y='tip',hue='smoker',ax=a)


# In[45]:


sns.displot(data=df_tips, x= 'total_bill')
#sns.displot(data=df_tips, x= 'total_bill',hue = 'time',kind='kde')
#sns.displot(data=df_tips, x= 'total_bill',hue = 'time',kind='ecdf')
#sns.displot(data=df_tips, x='time')
# sns.catplot(data=df_tips,x='time')


# In[ ]:




