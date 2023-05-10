#!/usr/bin/env python
# coding: utf-8

# ### 전국공인중개사사무소표준데이터
#  - 공인중개사 / 개업공인중개사 비율
#  - 공제미가입 중개사 count, 전체 대비 비율
#  - OO공인중개... 중 흔한 상호면
#  - OO공인중개... 가 아닌것은 따로 저장

# In[167]:


import mymodule as md
import re

def mystrip(s):
    remove_after = ['공인중개사']
    s = re.sub(r"\s","",s)
    for c in remove_after:
        if c in s:
            s = s[:s.index(c)]
        elif c not in s:
            s = s
    return s
s = '착한공인중개사사무소'
s1 = '더오름'
s2 = '행복 공인중개사 사무소'
assert mystrip(s) == '착한'
assert mystrip(s1) == '더오름'
assert mystrip(s2) == '행복'


# In[77]:


csv_data = []
with open('전국공인중개사사무소표준데이터.csv') as f:
    for line in f:
        csv_data.append(md.my_split(line))
print(csv_data[0].index('중개사무소명'))
print(csv_data[0].index('개업공인중개사종별구분'))
print(csv_data[0].index('공제가입유무'))

realtor_list = []
deduction_list = []
realtor_name_list = []
for i in csv_data[1:]:
    realtor_list.append(i[2])
    deduction_list.append(i[7])
    realtor_name_list.append(i[0])


# In[79]:


realtor_set = set(realtor_list)
deduction_set = set(deduction_list)
realtor_count = []
deduction_count = []
for i in realtor_set:
    realtor_count.append(realtor_list.count(i))
    
for i in deduction_set:
    deduction_count.append(deduction_list.count(i))
    
di_realtor = dict(zip(realtor_set,realtor_count))
di_deduction = dict(zip(deduction_set,deduction_count))
print('공인중개사비율: {}'.format(di_realtor['공인중개사']/len(realtor_list)*100))
print('개업공인중개사: {}'.format(di_realtor['개업공인중개사']/len(realtor_list)*100))
print('법인: {}'.format(di_realtor['법인']/len(realtor_list)*100))
print('가입한 공인중개사: {}'.format(di_deduction['Y']/len(deduction_list)*100))
print('미가입한 공인중개사: {}'.format(di_deduction['N']/len(deduction_list)*100))


# In[164]:


name_pass1 = []
name_pass2 = []
name_pass3 = []
for i in realtor_name_list:
    if '공인중개사' in i:
        name_pass1.append(i)
    else:
        name_pass2.append(i)

for i in name_pass1:
    name_pass3.append(mystrip(i))

name_set = set(name_pass3)
name_count = []
for i in name_set:
    name_count.append((i,name_pass3.count(i)))
di_name = sorted(name_count, key = lambda x : x[1], reverse = True)

print('흔한상호명 : ', di_name[:10])
print('안흔한 상호명 : ',di_name[-5:])
print('공인중개사가... 아닌 것:',name_pass2[:3])

