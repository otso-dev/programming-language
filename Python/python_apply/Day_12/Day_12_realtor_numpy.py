#!/usr/bin/env python
# coding: utf-8

# In[9]:


import mymodule as md
import numpy as np


# In[10]:


csv_data = []
with open('전국공인중개사사무소표준데이터.csv') as f:
    for line in f:
        csv_data.append(md.my_split(line[:-1]))

#assert len(md.split_len(csv_data)) == 1
np_data = np.array(csv_data)
for e in enumerate(np_data[0]):
    print(e)


# In[11]:


btypes = np_data[1:,2]
#print(btypes[:3])
btype_name, btype_count = np.unique(btypes,return_counts = True) # set과 같은 기능,count도 가능하다.
print(btype_name)
print(btype_count)
print(btype_count*100/sum(btype_count))


# In[12]:


y_n = np_data[1:,7]
np.unique(y_n, return_counts = True)


# In[13]:


names = np_data[1:,0]
name_head = []
else_list = []
for n in names:
    n = n.replace(' ','')
    if '공인중개사' in n:
        name_head.append(n[:n.index('공인중개사')])
    else:
        else_list.append(n)


# In[7]:


s = 'abc 공인중개사'
s = s.replace(' ','')
#s.index('공인중개사')
#s[:s.index('공인중개사')]
print(s)


# In[22]:


name, name_count = np.unique(name_head,return_counts=True)
names = sorted(zip(name,name_count),key = lambda x:x[1],reverse = True)
#print(names[:10])
#print(names[-5:])

else_name = []
else_list2 = []
for n in else_list:
    n = n.replace(' ','')
    if '부동산중개' in n:
        else_name.append(n[:n.index('부동산중개')])
    else:
        else_list2.append(n)
        
else_name, else_name_count = np.unique(else_name,return_counts=True)
else_names = sorted(zip(else_name,else_name_count),key=lambda x:x[1],reverse=True)

print(else_names[:10])       

