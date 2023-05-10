#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math
x1 = 3
y1 = 10
x2 = 5
y2 = 25
a = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(a)
def dist(p1,p2):
    print('x',(p2[0]-p1[0]),(p2[0]-p1[0])**2)
    print('y',((p2[1]-p1[1])),(p2[1]-p1[1])**2)
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
b = dist([x1,y1],[x2,y2])
print(b)
def dist_np(p1,p2): 
    return math.sqrt(sum((p2-p1) **2))
c = dist_np(np.array([x1,y1]),np.array([x2,y2]))
print(c)
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
        


# In[41]:


csv_data = []
with open ('전국자동차정비업체표준데이터.csv') as f:
    for line in f:
        csv_data.append(my_split(line))
pass1 = []
pass2 = []
print(csv_data[0].index('자동차정비업체명'))
for i in csv_data[1:]:
    pass1.append(i[4:6])
    pass2.append(i[0])

for e in pass1:
    for i , n in enumerate(e):
        try:
            e[i] = float(n)
        except:
            e[i] = 0.0

p1 = [35.1531,129.0596]
dist_list = []
for i in range(len(pass1)):
    dist_list.append(dist_np(np.array(p1),np.array(pass1[i])))


# In[44]:


index_list = []
for i , n in enumerate(dist_list):
    index_list.append([i,n])
#print(index_list[:3])

