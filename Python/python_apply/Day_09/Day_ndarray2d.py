#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a1 = np.array([[1,2,3],[10,20,30]])
print(a1)
print(a1.ndim)
print(a1.shape)
print(a1.size)


# In[ ]:


a2 = np.arange(20).reshape(4,5) # n차원 array을 만드는 method
print(a2)
print(a2.shape)


# In[ ]:


a3 = a2.flatten() # deep copy
a3[3] = 100
print(a3)
print(a2)
a4 = a2.ravel() # shallow copy
a4[3] = 200
print(a4)
print(a2)


# In[ ]:


a2 = np.arange(20).reshape(4,5)
print(a2)
#print(a2[1])
#print(a2[1,2])
#print(a2[:1])
#print(a2[:,1:4])
#print(a2[:,1:4:2])
#print(a2[1,:])
#print(a2[1:3,:])
print(a2[::2,1:4])


# In[ ]:


print(a2)
#print(a2.shape) # axis
#print(a2.sum())
#print(a2.sum(axis = 0))
#print(a2.sum(axis = 1))


# In[46]:


print(a2, a2.shape)
a3 = a2.T# 축변환
print(a3, a3.shape)


# In[49]:


print(a2, a2.shape)
a3 = np.moveaxis(a2,[0],[1])
print(a3, a3.shape)


# In[63]:


a10 = np.arange(5,20).reshape(3,5)

# shape (3,5) 의 2차원 ndarray로 만들기.
print(a10[::,2:4])
a11 = a10[::,2:4]
print(a11.sum(axis = 0))
print(np.mean(a11, axis = 0))


# In[71]:


a1 = np.arange(0,10).reshape(2,5)
a2 = np.arange(100,110).reshape(2,5)
print(a1)
print(a2)
a3 = np.concatenate((a1,a2),axis=1)
print(a3)
a4 = np.hstack((a1,a2))
print(a4)
a5 = np.vstack((a1,a2))
print(a5)


# In[86]:


print(a4)
a6 = np.hsplit(a4,5)
print(a6)


# In[82]:


a7 = a4.T
print(a7)
a8 = np.vsplit(a7,5)


# In[88]:


a2 = np.arange(20).reshape(4,5)
print(a2)
filter1 = a2[:,0]%10 == 5
print(a2[filter1])

