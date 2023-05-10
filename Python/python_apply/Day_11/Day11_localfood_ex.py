#!/usr/bin/env python
# coding: utf-8

# * 강사코드

# In[73]:


import pickle
import numpy as np

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

def process_product_names(s):
    r = []
    remove_after = ['(','외',]
    split_at = ['+',',']
    for c in remove_after:
        if c in s:
            if s != '참외':
                s = s[:s.index(c)]
    for c in split_at:
        if c in s:
            r = r + s.split(c)
    for c in s:
        if c == '"':
            s=s.strip('"')
    if len(r) == 0:
        r.append(s)
    return r

sample1 = 'productA+productB'
sample2 = 'productA,productB'
sample3 = 'product(A+B)'
sample4 = 'product외 abc'
sample5 = 'product'
sample6 = '참외'
sample7 = '"product'
sample8 = 'product"'
assert process_product_names(sample1)== ['productA','productB']
assert process_product_names(sample2)== ['productA','productB']
assert process_product_names(sample3)== ['product']
assert process_product_names(sample4)== ['product']
assert process_product_names(sample5)== ['product']
assert process_product_names(sample6)== ['참외']
assert process_product_names(sample7)== ['product']
assert process_product_names(sample8)== ['product']


# In[4]:


raw_data = []
with open('전국로컬푸드인증정보표준데이터.csv') as f:
    for line in f:
        raw_data.append(my_split(line[:-1]))
print(raw_data[:3])


# In[22]:


for e in enumerate(raw_data[0]):
    pass
    ##print(e)

# dict만드는 또다른 방법
#     if v[0] in fw_area_name:
#         i = fw_area_name.index(v[0])
#         fw_products[i].append(v[1])
#     else:
#         fw_area_name.append(v[0])
#         fw_products.append([v[1]])


# In[12]:


np_data = np.array(raw_data)
#print(np_data.shape)
np_data = np_data[:,4:9]
print(np_data.shape)
print(np_data[0])


# In[57]:


area_name_list =[]
product_list = []
all_data = []
for sample in np_data[1:]:
    area_name = ''
    for i in sample[:-1]:
        i = i.strip(' "')
        if len(i)>0:
            area_name = ' '.join(i.split()[:2])
            #area_name_list.append(area_name)
            break
    #product_list.append(process_product_names(sample[-1]))
    for p in process_product_names(sample[-1]):
        all_data.append([area_name,p])
        

#print(area_name_list[:3], len(area_name_list))
#print(product_list[:3], len(product_list))


# In[78]:


#print(all_data[:3])
fw_dict = dict()
re_dict = dict()
fw_area_name = []
fw_products = []
for v in all_data:
    if v[0] not in fw_dict.keys():
        if v[1] is not None:
            fw_dict[v[0]] = [v[1]]
    else:
        fw_dict[v[0]].append(v[1])
    if v[1] not in re_dict.keys():
        if v[0] is not None:
            re_dict[v[1]] = {v[0]}
    else:
        re_dict[v[1]].add(v[0])
# print(fw_area_name[:3], len(fw_area_name))
# print(fw_products[:3],len(fw_products))
#print(fw_dict)
#print(re_dict)


# In[33]:


sample_text = np_data[2][0]
sample_text.split()[:2]
' '.join(sample_text.split()[:2])


# In[79]:


p_list = []
for v in all_data:
    p_list.append(v[1])
p_set = set(p_list)
count_list = []
for v in p_set:
    count_list.append((v, p_list.count(v)))
x = sorted(count_list,key=lambda x : x[1], reverse = True)
print(x[:10])

