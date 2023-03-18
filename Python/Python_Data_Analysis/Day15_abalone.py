#!/usr/bin/env python
# coding: utf-8

# #### 전복
# 1. [함수]requests 패키지를 이용해 데이터 가져와서 ndarray로 변환.
# 2. [함수]성별이 'M'인 데이터를 필터, Length와 Diameter 간 상관도를 반환
# 3. __name__ 값이 __main__ 이면, 1,2 함수를 실행, 2번 함수의 반환 값을 프린트. 

# In[2]:


import requests
import numpy as np
import matplotlib.pyplot as plt


# In[58]:


def data_get():
    sub_data = []
    data = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data')
    raw_data = data.text.split('\n')
    #print(raw_data)
    for line in raw_data:
        sub_data.append(line.split(','))
    np_data = np.array(sub_data[:-1])
    filter1 = np_data[:,0] == 'M'
    sub_data = np_data[filter1]
    filter_data = sub_data[:,[1,2]].astype(np.float64)
    return filter_data

def len_dia_corr(sub_data):
    return np.corrcoef(sub_data[:,0],sub_data[:,1])

if __name__ == '__main__':
    data = data_get()
    out = len_dia_corr(data)
    print(out)


