#!/usr/bin/env python
# coding: utf-8

# In[2]:


csv_data =[]
with open('lott.csv') as f:
    for line in f:
        csv_data.append(line[:-1].split(','))
print(csv_data[:3])
int(csv_data[0][-1])


# In[68]:


# 빈도수 mode: 숫자별 카운트 (몇번이나 나왔나)
# 회차별 - 평균값, 표준편차
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

def KEY(x):
    
lotto_list = []

for e in csv_data:
    for i , e_i in enumerate(e):
        lotto_list.append(int(e_i))
        e[i] = int(e_i)
lotto_set = set(lotto_list)
mode_list =[]

for i in lotto_set:
    mode_list.append(lotto_list.count(i))
mode = dict(zip(lotto_set,mode_list))
mode = dict(sorted(mode.items(), key = KEY, reverse = True))
print(mode)

for i in range(0,len(csv_data)):
    pass
    #print(i+1,'회차 평균 값:', mean(csv_data[i]),'표준편차 :', stdev(csv_data[i]))
# 빈도수 /value값 다 더함  X 100
all_value = (sum(mode_list))
for i in lotto_set:
    print(i,(mode_list[i - 1]/all_value) * 100)

