#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import math
def dist_np(p1,p2): 
    return math.sqrt(sum((p2-p1) **2))
def my_split(s):
    block_start = False
    start_index = 0
    ret_list=[]
    for i, c in enumerate(s):
        if block_start==False:
            if c==',':
                ret_list.append(s[start_index:i])
                start_index=i+1
            elif c=='"':
                block_start=True
                start_index = i
        else:
            if c=='"':
                block_start=False
    if s[-1]!=',':
        ret_list.append(s[start_index:])
    return ret_list


# In[2]:


csv_data = []
with open ('전국자동차정비업체표준데이터.csv') as f:
    for line in f:
        csv_data.append(my_split(line))


# In[8]:


loc_list = []
for e in csv_data[1:]:
    loc_list.append(e[4:6])

for e in loc_list:
    for i, v in enumerate(e):
        try:
            e[i] = float(v)
        except:
            e[i] = 0.0
print(loc_list[:3])
dist_np([35.1531,129.0596], )


# In[17]:


target_p = np.array([35.1531,129.0596])
dist_list = []
for i, p2 in enumerate(loc_list):
    try:
        dist_list.append([i,dist_np(target_p,np.array(p2))])
    except:
        dist_list.append([i,100.0])
#print(dist_list[:3])

r = sorted(dist_list, key = lambda x : x[1])
#print(r[:5])
for x in r[:5]:
    print(csv_data[x[0]])

