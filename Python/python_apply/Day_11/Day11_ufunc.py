#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
a1 = np.arange(30).reshape(5,6)
print(a1)
print('np.sum: ', np.sum(a1,axis=1))
#print(np.add.reduce(a1,axis = 1,where = a1%2 == 0))
#print(np.add.accumulate(a1,axis=0))
print(np.add.reduceat(a1,[0,2,4], axis = 1))
print(np.add.at(a1,[0,2,4],100)) # in-place
print(a1)


# In[18]:


a2 = np.arange(10)
a3 = np.arange(100,110)
print(a2)
print(a3)
print(np.add.outer(a2,a3))

