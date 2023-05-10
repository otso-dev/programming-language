#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.set_printoptions(precision=5,suppress=True)


# In[5]:


def read_data():
    raw_data = []
    with open('가스공급량_20230217170922.csv') as f:
        for line in f:
            raw_data.append(line[:-1].split(','))
    np_data= np.array(raw_data [2:])
    np_data= np_data[:,2:].astype(np.int64)
    return np_data

def get_corr(np_data):
    by_year = np.add.reduceat(np_data,np.arange(0,130,12))
    return np.corrcoef(by_year[:,1], by_year[:,5])


# In[7]:

if __name__ == '__main__':
	d = read_data()
	out = get_corr(d)
	print(out)
