#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

url = 'https://www4.stat.ncsu.edu/~boos/var.select/diabetes.tab.txt'
pd_data = pd.read_csv(url,sep = '\t')
print(pd_data)
print(pd_data.shape)


# In[4]:


_, axe = plt.subplots()
axe.plot(pd_data['BMI'])
axe.plot(pd_data['BP'])


# In[28]:


# normalization : (x - x_min)/(x_max - x_min)
# standardlization을 따르지 않을때.

pd_data['BMI'].describe()
bmi_min = pd_data['BMI'].min()
bmi_max = pd_data['BMI'].max()
pd_data['BMI_norm'] = pd_data['BMI'].apply(lambda x : (x - bmi_min)/(bmi_max-bmi_min))


bp_min = pd_data['BP'].min()
bp_max = pd_data['BP'].max()
pd_data['BP_norm'] = pd_data['BP'].apply(lambda x: (x - bp_min)/(bp_max - bp_min))

_, axe = plt.subplots()
axe.plot(pd_data['BMI_norm'])
axe.plot(pd_data['BP_norm'],color = 'green')

print(pd_data['BMI_norm'].describe())


# In[27]:


# standardilzation : (x-x_mean)/x_std
# -데이터 분포가 노멀커브(벨커브)를 따를 떄.

pd_data['BMI'].describe()
bmi_mean = pd_data['BMI'].mean()
bmi_std = pd_data['BMI'].std()
pd_data['BMI_stand'] = pd_data['BMI'].apply(lambda x : (x - bmi_mean)/(bmi_std))

bp_mean = pd_data['BP'].mean()
bp_std = pd_data['BP'].std()
pd_data['BP_stand'] = pd_data['BP'].apply(lambda x: (x - bp_mean)/(bp_std))

_, axe = plt.subplots()
axe.plot(pd_data['BMI_stand'])
axe.plot(pd_data['BP_stand'],color = 'green')
print(pd_data['BP_stand'].describe())


# In[25]:


pd_data

