#!/usr/bin/env python
# coding: utf-8

# In[101]:


import re

csv_data=[]
with open('전국건강증진센터표준데이터.csv', encoding='cp949') as f:
    for line in f:
        start = -1
        for i, c in enumerate(line):
            if start !=1 and c=='"':
                start = 1
            if start==1 and c==',':
                line[i]='+';
            if start ==1 and c=='"':
                start = -1
        csv_data.append(line.split('",'))
        
print(csv_data[:3])
print(len(csv_data[0]))


# In[78]:


# replacing.
s='맞춤형건강클리닉,건강증진,인천광역시 연수구 함박뫼로 13,인천광역시 연수구 청학동 465-4,37.41913159,126.6711606,"치매검진, 당뇨.고혈압 상담 및 검사, 뇌경색.심뇌혈관질환, 정신건강 상담",09:00,18:00,"일요일, 공휴일",30,0,5,0,0,0,검사전날 오후8시 전까지 식사마치고 검사당일 아침 금식,032-749-8104,맞춤형건강클리닉,032-749-8122,인천광역시 연수구 보건소,2021-10-25,3520000,인천광역시 연수구'

start = False
s_list=list(s)
for i, c in enumerate(s_list):
    if start==False and c=='"':
        start = True
    elif start == True and c==',':
        s_list[i]='+'
    elif start == True and c=='"':
        start = False
s = ''.join(s_list)
len(s.split(','))


# In[ ]:


def replace_inblock(s):
    start = False
    s_list=list(s)
    for i, c in enumerate(s_list):
        if start==False and c=='"':
            start = True
        elif start == True and c==',':
            s_list[i]='+'
        elif start == True and c=='"':
            start = False
    return ''.join(s_list)


# In[105]:


#reading pattern
s='맞춤형건강클리닉,건강증진,인천광역시 연수구 함박뫼로 13,인천광역시 연수구 청학동 465-4,37.41913159,126.6711606,"치매검진, 당뇨.고혈압 상담 및 검사, 뇌경색.심뇌혈관질환, 정신건강 상담",09:00,18:00,"일요일, 공휴일",30,0,5,0,0,0,검사전날 오후8시 전까지 식사마치고 검사당일 아침 금식,032-749-8104,맞춤형건강클리닉,032-749-8122,인천광역시 연수구 보건소,2021-10-25,3520000,인천광역시 연수구'

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
print(ret_list)
print(len(ret_list))


# In[112]:


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


# In[111]:


csv_data=[]
with open('전국건강증진센터표준데이터.csv', encoding='cp949') as f:
    for line in f:
        csv_data.append(my_split(line))
print(len(csv_data[0]))
print(csv_data[0])


# In[110]:


len_list=[]
for e in csv_data:
    len_list.append(len(e))
print(set(len_list))

