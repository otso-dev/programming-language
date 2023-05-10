#!/usr/bin/env python
# coding: utf-8
# %%

# ### 전국육교정보데이터
# * 제가각 계산시 결측지 있는 샘플은 버림.
# 
# - 내진설계된 육교 퍼센트
# - 안전등급별 육교갯수, 비율
# - 육교가 만들어진 연도 vs 장애인편의시설간 상관관계
#     - 연도, 장애인편의시설 갖춘 육교의 갯수/해당연도 건설 육고 갯수
# 
# - 길이가 가장 긴 육교(육교연장)
# - 가장 튼튼한 육교(허용통행하중)
# - 가장 높은 육교(통행제한 높이)
# 
# - 육교연장,허용통해하중,통행제한 높이에 대해 최대,최소값,평균,표준편차

# %%


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


# %%


import numpy as np
import matplotlib.pyplot as plt

csv_data = []
with open('전국육교정보표준데이터.csv') as f:
    for line in f:
        csv_data.append(my_split(line[:-1]))
np_data = np.array(csv_data)
for e in enumerate(np_data[0]):
    print(e)


# %%


pass1 = np_data[20:,20]
pass1_filter = pass1[:] !=' '
pass2 = pass1[pass1_filter]
key,value = np.unique(pass2,return_counts = True)
print(key)
print('N의 비율:',value[0]/len(pass2)*100)
print('Y의 비율:',value[1]/len(pass2)*100)


# %%


pass1 = np_data[21:,21]
pass1_filter = pass1[:] != ' '
pass2 = pass1[pass1_filter]
key,value = np.unique(pass2,return_counts=True)
print(key)
print(key[0],value[0],'비율: ',value[0]/len(pass2)*100)
print(key[1],value[1],'비율: ',value[1]/len(pass2)*100)
print(key[2],value[2],'비율: ',value[2]/len(pass2)*100)
print(key[3],value[3],'비율: ',value[3]/len(pass2)*100)
print(key[4],value[4],'비율: ',value[4]/len(pass2)*100)


# %%


# 7 9 10
pass1 = np_data[7:,7]
pass2 = np_data[9:,9]
pass3 = np_data[10:10]
filter1 = pass1[:] != ' '
filter2 = pass2[:] != ' '
filter3 = pass3[:] != ' '
pass1_filter = pass1[filter1]
pass2_filter = pass2[filter2]
pass3_filter = pass3[filter3]
try:
    pass1_filter.astype(np.int64)
except:
    pass

pass1_filter

