#!/usr/bin/env python
# coding: utf-8

# In[4]:


# python list
lista = []
print(lista)

lista.append('a')
print(lista)


# In[14]:


# numpy ndarray
import numpy as np
array1 = np.array(lista)
array2 = np.array([1,2,3,4])
array3 = np.array([x for x in range(5)])

#array1.append('c')
#print(array1,type(array1))
#print(array3)
print(array3[[1,4]])
print(array3[array3%3==0])
print(array3[array3>2])


# In[18]:


# for , if
# for i in array3:
#     print(i)
    
for i in range(5):
    if i > 2:
        print(i)


# In[26]:


#function
def function_name(n):
    return n*10
return_value = function_name(20)
print('return_value:',return_value)

assert function_name(100) == 1000


# In[42]:


import random

random.seed(123) #랜덤 값을 설정할 수 있음
    
listb=[]
for i in range(10):
    listb.append(random.randint(0,100))
print(listb)
listc = [random.randint(0,100) for _ in range(10)]
print(listc)
# listb에서 50보다 큰 것.
listb_np = np.array(listb)
listb_np[listb_np>50]

