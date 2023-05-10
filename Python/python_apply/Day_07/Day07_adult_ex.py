#!/usr/bin/env python
# coding: utf-8

# In[19]:


import math
def mean(num_list): # 평균
    return sum(num_list)/len(num_list)

def dev(num_list): # 편차
    m = mean(num_list)
    return [x-m for x in num_list]

def var(num_list): # 분산
    n = len(num_list)
    d = dev(num_list)
    return sum([x * x for x in d])/(n - 1)

def stdev(num_list): #표준편차
    return math.sqrt(var(num_list))

def covar(list_1,list_2): # 공분산
    n = len(list_1)
    list_1_dev = dev(list_1)
    list_2_dev = dev(list_2)
    return sum(x * y for x, y in zip(list_1_dev,list_2_dev))/(n-1)
def corel(list_1,list_2): # 상관도 (-1 ~ 1)
    return covar(list_1, list_2)/(stdev(list_1)*stdev(list_2))


# In[1]:


import requests
x = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data')


# In[13]:


pass1 = x.text.split('\n')
age_list = []
cap_gain_list = []
hours_per_week_list = []
for e in pass1:
    try:
        t = e.split(',')
        if len(t)<5:
            continue
        age_list.append(t[0])
        cap_gain_list.append(t[10])
        hours_per_week_list.append(t[12])
    except:
        print(e,type(e))
        


# In[14]:


print(len(age_list))
print(len(cap_gain_list))
print(len(hours_per_week_list))


# In[15]:


age_list = [int(i) for i in age_list]
cap_gain_list = [int(i) for i in cap_gain_list]
hours_per_week_list = [int(i) for i in hours_per_week_list]


# In[20]:


print('age vs. cap gain:',corel(age_list,cap_gain_list))
print('hours per week vs. cap gain: ',corel(hours_per_week_list,cap_gain_list))
print('age vs. hours per week:',corel(age_list,hours_per_week_list))

