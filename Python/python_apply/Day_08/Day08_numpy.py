#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[9]:


a1 = np.array([1,2,3,4,5])
print([1,2,3,4,5])
print(a1)
print(type(a1))


# In[13]:


a2 = np.arange(10)
print(a2)


# In[19]:


# 100 아래의 3의 배수
a3 = np.arange(0,100,3)
print(a3)

# 1에서부터 10아래 0.5씩 증가하는 숫자. stop = 0.5 -> numpy는 소수점이 되지만 그냥 python에서는 불가능
a4 = np.arange(1.3,10,0.5)
print(a4)


# In[20]:


a5 = np.linspace(0,10,3) # 시작 과 끝 사이의 n개의 숫자를 주는 함수
print(a5)


# In[24]:


a6 = np.zeros(5)
print(a6)

a7 = np.ones(5, dtype = np.int64) # datatype을 바꾸는 것
print(a7)
a7.astype(np.float64) # 만들어진 것을 datatpye을 바꿀때
# array안에 있는 datatype은 list와 달리 똑같은 type만 들어가야한다.


# In[28]:


lista = [1,2,3.5,4.2]
a8 = np.array(lista)
print(a8)
listb = [1,2,'abc','def']
a9 = np.array(listb)
print(a9)
#a9.astype(np.int64)


# In[37]:


# numpy는 for문을 알아서 써주는 method가 많다.
print(a8.dtype)
print(a8.ndim) # 몇차원의 array인지 알려주는 method
print(a8.shape) # array의 차원마다 모양(길이)를 알려주는 method tuple형태로 반환함
print(a8.size) # array안의 모든 데이터 갯수를 알려주는 method

print(a8.itemsize) #array의 datatype의 size를 알려주는 method
print(a8.data) # array의 메모리위치를 알려줌


# In[46]:


a10 = np.arange(10,100,5)
print(a10)
# 특정index
print(a10[2])
# start , stop
print(a10[5:])
print(a10[0:3])
# start, stop, step
print(a10[6:20:2])


# In[49]:


a10 = np.arange(10,100,5)
print(a10)
print(a10[[1,3,7]]) # numpy는 index의 값을 이용해 list로 받을 수 있음

# list10 = [x for x in range(10,100,5)]
# print(list10)
#print(list10[[1,2,3]]) -> list는 못함


# In[53]:


a10 = np.arange(10,100,5)
print(a10)
print(a10[a10 % 10 == 5]) # 조건식을 줄 수 도 있다. 해당 조건에 맞는 index를 list로 반환함

x = (a10 % 10 == 5)
print(x)
print(x.shape)
print(a10.shape)
print(a10[x])


# In[60]:


lista = [x for x in range(5)]
listb = [x for x in range(10,15)]
print(lista)
print(listb)
print(lista+listb)
print(lista-listb)


# In[66]:


a1 = np.arange(5)
a2 = np.arange(10,15)
print(a1)
print(a2)
print(np.concatenate((a1,a2))) #2개의 array를 합칠 때
print('sum',a1+a2) # python list와 달리 array + 는 각 요소를 더해서 반환한다.(사칙연산 가능) -> 두개이상의 array를 사칙연산을 할려면 size가 같아야한다.
print('sub',a1-a2)
print('mul',a1*a2)
print('div',a1/a2)

