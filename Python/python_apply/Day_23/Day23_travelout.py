#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd_data = pd.read_csv('내국인출국교통수단별_20230303141138.csv',encoding='cp949',header = 1)
pd_data.columns = ['시점','공항','항구']
print(pd_data)


# In[8]:


sub_data2022 = pd_data.tail(12)
print(sub_data2022)
print(sub_data2022.describe())

for n in ['공항','항구']:
    value_min = sub_data2022[n].min()
    value_max = sub_data2022[n].max()
    value_mean = sub_data2022[n].mean()
    value_std = sub_data2022[n].std()
    sub_data2022[n+'_norm'] = sub_data2022[n].apply(lambda x : (x-value_min)/(value_max - value_min))
    sub_data2022[n+'_std'] = sub_data2022[n].apply(lambda x : (x-value_mean)/value_std)

def normal(pd_data,x):
    min_x = pd_data[x].min()
    max_x = pd_data[x].max()
    pd_data[x+'_norm'] = pd_data[x].apply(lambda x :(x-min_x)/(max_x-min_x))
    return pd_data[x+'_norm']

def std(pd_data,x):
    x_mean = pd_data[x].mean()
    x_std = pd_data[x].std()
    pd_data[x+'_std'] = pd_data[x].apply(lambda x: (x-x_mean)/x_std)
    return pd_data[x+'_std']


_,axe = plt.subplots()
axe.plot(sub_data2022['공항_norm'])
axe.plot(sub_data2022['항구_norm'])


# In[19]:


# normalization
_,axe = plt.subplots()
axe.plot(normal(sub_data2022,'공항'))
axe.plot(normal(sub_data2022,'항구'))

#standardlization
_,axe = plt.subplots()
axe.plot(np.arange(1,13),std(sub_data2022,'공항'))
axe.plot(np.arange(1,13),std(sub_data2022,'항구'))


# In[41]:


#print(pd_data)
for i in range(8):
    #print(i,12*i,12*(i+1))
    sub_data = pd_data.iloc[12*i:12*(i+1)]
    
    for n in ['공항','항구']:
        normal(sub_data,n)
        std(sub_data,n)
    
    fig,axe = plt.subplots(1,3)
    fig.set_figwidth(6.4*3)
    
    axe[0].plot(np.arange(1,13),sub_data['공항'])
    axe[0].plot(np.arange(1,13),sub_data['항구'])
    axe[0].set_title('{}_raw'.format(2015+i))
    
    axe[1].plot(np.arange(1,13),sub_data['공항_norm'])
    axe[1].plot(np.arange(1,13),sub_data['항구_norm'])
    axe[1].set_title('{}_norm'.format(2015+i))
    
    axe[2].plot(np.arange(1,13),sub_data['공항_std'])
    axe[2].plot(np.arange(1,13),sub_data['항구_std'])
    axe[2].set_title('{}_std'.format(2015+i))


# In[ ]:





# In[ ]:




