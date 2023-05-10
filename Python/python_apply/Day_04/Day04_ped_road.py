#!/usr/bin/env python
# coding: utf-8
# %%

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
    len_list = []
    for e in data_list:
        len_list.append(len(e))
    print(set(len_list))
    if len(set(len_list))>1:
        for i in set(len_list):
            print(i, len_list.count(i))
def mean(number_list):
    return sum(number_list)/len(number_list)


# %%


csv_data=[]
with open('전국보행자전용도로표준데이터.csv') as f:
    for line in f:
        csv_data.append(my_split(line))
        #csv_data.append(line.split(','))
i = csv_data[0].index('보행자전용도로폭')

width_list = []
for e in csv_data[1:]:
    width_list.append(float(e[i]))

mean(width_list)


# %%


split_len(csv_data)

