#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


url = 'https://www4.stat.ncsu.edu/~boos/var.select/diabetes.tab.txt'
pd_data = pd.read_csv(url,sep='\t')
print(pd_data)


# In[18]:


_, axe = plt.subplots()
axe.hist(pd_data['BMI'], bins = 10, linewidth=1.5,edgecolor="black",label = 'BMI')
axe.legend()
axe.set_xlabel('BMI')
axe.set_ylabel('number of people')


# In[22]:


_, axe = plt.subplots()
axe.boxplot(pd_data['AGE'])
print(pd_data['AGE'].describe())


# In[29]:


_,axe = plt.subplots()
axe.pie(pd_data['SEX'].value_counts())

