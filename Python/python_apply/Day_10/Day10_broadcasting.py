#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
a1 = np.arange(10)
a2 = np.arange(100,110)
print(a1,a2)
print(a1+a2)
a3 = np.array([5]*10)
print(a3)
print(a1+a3)
print(a1+5)


# In[7]:


# f(x) = 3x+5
# x = 0 에서 100사이 짝수 일때 f(x)의 합
x = np.arange(0,101,2)
print(x)
print(sum(3*x+5))


# In[14]:


a2 = np.arange(30).reshape(5,6)
print(a2)
a3 = np.arange(6)
print(a3)
a4 = np.arange(100,130).reshape(5,6)
print(a4)


# In[9]:


print(a2+100)


# In[15]:


print(a2+a4)
# a2 : (5,6)
# a3 : (6,)
# a4 : (5,6)


# In[16]:


a10 = np.arange(3*5*7*8).reshape(3,5,7,8)
print(a10.shape)
# 스칼라
# (8,)
# (7,8)
# (5,7,8)
# (3,5,7,8)


# In[38]:


a15 = np.arange(15).reshape(5,3)
# axis1의 3개의 값 중 
# - 첫번째는 곱하기 2
# - 두번째는 곱하기 10
# - 세번째는 곱하기 12
# axis 1을 따라 합계 구하기

# 풀이
x = np.array([2,10,12])
print(x,x.shape)
print(a15*x)
print(np.sum(a15*x,axis=1))

