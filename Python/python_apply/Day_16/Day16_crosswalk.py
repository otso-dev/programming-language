#!/usr/bin/env python
# coding: utf-8

# #### 전국횡단보도표준데이터
#  1. 횡단보도 연장, 녹색신호시간 : 상관도
#  2. 자전거 횡단도 겸용 비율 (전체 대비)
#  3. 차로수별 자전거 횡단도 카운트/비율
#  4. 차로수별 보행자 신호등 유무 카운트/비율
#  5. 차로수별 음향신호기설치 유무 카운트/비율
# 
# 화면 출력
# 1. 상관도 수치
# 2. 비율 수치
# 3 ~ 5. 카운트, 비율

# In[62]:


csv_data = []
with open('전국횡단보도표준데이터.csv') as f:
    for line in f:
        csv_data.append(my_split(line[:-1]))
csv_data = np.array(csv_data[1:])
print(csv_data.shape)
for e in enumerate(csv_data[0]):
    print(e)


# In[142]:


# 횡단보도 연장과 녹색신호시간 상관도
filter1 = (csv_data[:,13] != '') & (csv_data[:,17]!='') & (csv_data[:,13]!= '0') & (csv_data[:,17]!= '0') & (csv_data[:,13]<100)
suv_data = csv_data[filter1]
dt_data = suv_data[:,13].astype(np.float64)
gt_data = suv_data[:,17].astype(np.float64)
np.set_printoptions(precision=10,suppress=True)
print(np.corrcoef(dt_data,gt_data))
_, axe = plt.subplots()
axe.scatter(dt_data,gt_data)


# In[127]:


# 자전거 횡단도 겸용 비율 (전체 대비)
filter1 = csv_data[:,7] != ' '
bike_data = csv_data[filter1]
val, cnt = np.unique(bike_data[:,7], return_counts=True)
print(val,cnt)
total = np.sum(cnt)
bike_y = cnt[1]*100/total
bike_n = cnt[0]*100/total

print('자전거 횡단도 겸용비율',val[1],bike_y)
print('자전거 횡단도 겸용비율',val[0],bike_n)


# In[134]:


#  차로수별 자전거 횡단도 카운트/비율  차로수별 보행자 신호등 유무 카운트/비율  차로수별 음향신호기설치 유무 카운트/비율
#  차로수 11      자전거횡단도 7 보행자신호 14 음향신호기 16
filter1 = (csv_data[:,7] != ' ') & (csv_data[:,11] != ' ') & (csv_data[:,14]!= ' ') & (csv_data[:,17] != ' ') & (csv_data[:,7] != '') & (csv_data[:,11] != '') & (csv_data[:,14]!= '') & (csv_data[:,17] != '')
sub_data = csv_data[filter1]
car_bike = sub_data[:,[11,7]]

pass1 = dict()
for num,yn in car_bike:
    if num in pass1.keys():
        pass1[num].append(yn)
    else:
        pass1[num] = [yn]

pass2 = []
for e in pass1:      #dict 순환시 key값으로 순환이 된다.
    val,cnt = np.unique(pass1[e],return_counts=True)
    y,ratio = 0,0
    if 'Y' in val:
        y = cnt[val == 'Y']
    ratio = y*100/np.sum(cnt)
    pass2.append((int(e),float(ratio)))
    
    #print(pass2)
np.set_printoptions(precision=3,suppress=True)#numpy 소수점 제거
pass3 = sorted(pass2,key=lambda x : x[0])
pass3 = np.array(pass3)
print(pass3)


# In[15]:


import numpy as np
import matplotlib.pyplot as plt

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

def split_len(data_list):
    len_list=[]
    for e in data_list:
        len_list.append(len(e))
    print(set(len_list))
    if len(set(len_list))>1:
        for i in set(len_list):
            print(i, len_list.count(i))
    return set(len_list)

