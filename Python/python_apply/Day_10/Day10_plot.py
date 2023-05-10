#!/usr/bin/env python
# coding: utf-8

# In[38]:


import matplotlib.pyplot as plt
import numpy as np
import math
#plt.plot(np.arange(10))
_, axe = plt.subplots() #fig 도화지, axe 그래프 하나
x = np.arange(10)
y = x*5+10
print(x)
print(y)
axe.plot(x,y)


# In[35]:


#x = np.arange(10)
x = np.linspace(2,4,10)
y = 2*(x*x)+5
print(y)
_,axe = plt.subplots()
axe.plot(x,y)


# In[94]:


print(np.pi)
print(np.exp(5))
# 변수
mu = 0
sig = 1
pi = np.pi
u = np.mean(x)
x = np.linspace(-5,5,100)
y = 1/sig*np.sqrt(2*pi)
y = y * np.exp(-((x-mu)**2/(2*sig**2)))
_,axe = plt.subplots()
axe.plot(x,y)


# In[82]:


mu = 0
sig = 1
x = np.linspace(-5,5,100)
y = []
for v in x:
    y.append(0.5*(1+math.erf((v-mu)/(sig*math.sqrt(2)))))
_,axe = plt.subplots()
axe.plot(x,y)

