#!/usr/bin/env python
# coding: utf-8

# ### 전국로컬푸드인증
# - csv 파일 수동 다운로드하여 작업
# - ndarray 사용가능 (문자열 데이터 타입)
# 
# * 인기품목 top 10 (품목명 카운트)
# * dictionary -> {군단위지역명 : [품목명]}
# * dictionary -> {품목명 : [군단위지역명]}
# * csvfile -> 전국로컬푸드인증정보표준데이터.csv
# * 파일명 : 이름_localfood

# In[2]:


import numpy as np
import re

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


# In[19]:


csv_data = []
with open('전국로컬푸드인증정보표준데이터.csv') as f:
    for line in f:
        csv_data.append(my_split(line))

itemIndex = csv_data[0].index('품목명')
localIndex = csv_data[0].index('관리기관명')
item_pass1 = []
local_pass1 = []
for i in csv_data[1:]:
    item_pass1.append(i[itemIndex].replace('"','').replace('(',',').replace(')','').replace(',','+').split('+'))
    local_pass1.append(i[localIndex])
for i in item_pass1:
    for e , s in enumerate(i):
        i[e] = s.strip()
        if '외' in s and '참외' not in s:
            i[e] = re.sub(r'[0-9]|외|품목','',s)

    
item_pass2 = []
for i in item_pass1:
    for e, s in enumerate(i):
        item_pass2.append(i[e])


# In[20]:


item_set = set(item_pass2)
item_count = []
for i in item_set:
    item_count.append(item_pass2.count(i))

item_di = dict(zip(item_set,item_count))
item_di = sorted(item_di.items(), key  = lambda x:x[1], reverse = True)
print(item_di[:10])


# In[22]:


address_item = {}
for i, address in enumerate(local_pass1):
    if address not in address_item:
        address_item[address] = [item_pass2[i]]
    else:
        address_item[address].append(item_pass2[i])
print(address_item)


# In[16]:


item_pass2 = set(item_pass2)
item_address = {}
for i, item in enumerate(item_pass2):
    if item not in item_address:
        item_address[item] = [local_pass1[i]]
    else:
        item_address[item].append(local_pass1[i])
print(item_address)

