#!/usr/bin/env python
# coding: utf-8

# # 상관도 분석: UCI Repo Adult 데이터
# * age/ capital gain 상관도
# * hours-per-week/capital gain 상관도

# In[21]:


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


# In[54]:


import requests
x = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data')


# In[64]:


pass1 = x.text.split('\n')
pass2 = []
for line in pass1:
    pass2.append(line.split(','))

for e in pass2:
    for i , v in enumerate(e):
        try:
            e[i] = int(v)
        except:
            pass
age_list = []
capital_list = []
capital_loss_list = []
hours_week_list = []
for i in pass2:
    try:
        age_list.append(i[0])
        capital_list.append(i[10])
        hours_week_list.append(i[12])
        capital_loss_list.append(i[11])
    except:
        pass

age_list = age_list[:-2]


# In[66]:


print('age와 capital gain 상관도: \t{}'.format(corel(age_list,capital_list)))
print('hours-per-week와 capital gain 상관도: \t{}'.format(corel(hours_week_list,capital_list)))
print('age와 capital loss 상관도: \t{}'.format(corel(age_list,capital_loss_list)))
print('미국 자본이득 평균 : {}'.format(mean(capital_list)))
print('미국 자본손실 평균 : {}'.format(mean(capital_loss_list)))


# In[ ]:




