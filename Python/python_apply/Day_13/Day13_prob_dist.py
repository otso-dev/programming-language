#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#확률분포

# 동전을 던져 나올수 있는 경우의 확률분포
# 앞 1/2, 뒤 1/2

# 동전을 두번 던져 나올수 잇는 경우의 확률분포
#(앞,앞) (앞,뒤) (뒤,앞) (뒤,뒤)
# 1/4     1/4    1/4     1/4
# 앞의 값을 1, 뒤의 값을 0 일때의 분포
#    2,    1,     0
# 1/4     2/4    1/4


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
def fact(n):
    ret = 1
    while n>1:
        ret *= n
        n -= 1
    return ret

def fact_r(n):
    if n==2:
        return n
    return fact_r(n-1)*n

def perm_f(n, r):
    return fact(n)/fact(n-r)

def combi_f(n, r):
    return fact(n)/(fact(n-r)*fact(r))

def count_with_replacement_order(pool, sel_count):  # all
    if sel_count == 1:
        return len(pool), [[x] for x in pool]
    a, b = count_with_replacement_order(pool, sel_count-1)
    r = []
    for x in pool:
        for b_i in b:
            r.append(b_i+[x])
    return len(r), r    

def perm_pool(pool, r):
    if r == 1:
        return len(pool), [[x] for x in pool]
    ret = []
    for x in pool:
        pool_copy = [y for y in pool]
        pool_copy.remove(x)
        a, b = perm_pool(pool_copy, r-1)
        for b_i in b:
            ret.append(b_i+[x])
    return len(ret), ret

def combi_pool(pool, r):
    a , b = perm_pool(pool, r)
    r = []
    for b_i in b:
        r.append(set(b_i))
    f = []
    for r_i in r:
        if r_i not in f:
            f.append(r_i)
    return len(f), f

def normal(x, mu=0, sigma=1):
    return (1/np.sqrt(2*np.pi)*sigma) * np.exp(-0.5*(((x-mu)/sigma)**2))


# In[3]:


x = count_with_replacement_order([1,0],2)
print(x)
x_array = np.array(x[1])
print(x_array)
x_array1 = np.sum(x_array,axis=1)
x_array2 = np.unique(x_array1,return_counts = True)
print(x_array2[0])
print(x_array2[1]/len(x_array1))

_,axe = plt.subplots()
axe.plot(x_array2[0],x_array2[1]/len(x_array1))


# In[4]:


# 확률변수 [주사위를 3번던져 나온 숫자의 합]의 확률분포
tot, counts = count_with_replacement_order([1,2,3,4,5,6],3)
#print(tot,counts)
counts_array = np.array(counts)
counts_array1 = np.sum(counts_array,axis=1)
counts_array2 = np.unique(counts_array1,return_counts=True)
print(counts_array2[0])
print(counts_array2[1])
_,axe = plt.subplots()
axe.plot(counts_array2[0],counts_array2[1]/tot)


# In[5]:


# 동전을 10번 던져(앞1,뒤0) 나올수 있는 합의 확률분포
tot,counts = count_with_replacement_order([1,0],10)

counts_array = np.array(counts)
pass1 = np.sum(counts_array,axis=1)
pass2 = np.unique(pass1,return_counts = True)

print(pass2[0])
print(pass2[1])
_,axe = plt.subplots()
axe.plot(pass2[0],pass2[1]/tot)


# In[6]:


#통계검증
# 동정을 던져, 앞면이 나오면 100원을 주고,
# 뒷면이 나오면 100원을 받기로 함

# 앞면이 8번나옴.
# 친구: 동전이 조작되지 않음.   <-- 귀무가설
# 나 : 동전이 아무래도 조작인것 같다. <-- 대립가설
# 유의 수준 5%에서 결정하자.

print(pass2)
count2 = pass2[1]
print(count2)
print(np.sum(count2[-3:])/tot) # <--  p-value

# 만약 p-value가 합의한 유의수준 5%보다 클 경우
# 발생가능한 일반적인 케이스이므로,
# 귀무가설을 수용,
# 만약 p-value가 합의한 유의수준 5%보다 작을 경우
# 희귀한 케이스에 속하므로,
# 귀무가설을 기각, 대립가설을 채택


# In[7]:


# 주사위를 5번 던졌을때,
# - 합이 25가 될 확률
# - 합이 25보다 크면, 100원을 받기로 하였다. 합이 25보다 클 확률은(25 불포함)


tot, counts = count_with_replacement_order([x for x in range(1,7)],5)
counts = np.array(counts)
pass1 = np.sum(counts,axis=1)
pass2 = np.unique(pass1,return_counts=True)
v = pass2[0]
prob = pass2[1]/tot
print('값:',v,'확률:',prob)
assert np.sum(prob) == 1.0

index_25 = v==25
print('25필터:',v[index_25])
print('확률',prob[index_25])

index_25H = v >25
print('25보다 큰 것: ',v[index_25H])
print('확률:',prob[index_25H])
print('합:',np.sum(prob[index_25H]))
_, axe = plt.subplots()
axe.plot(v,prob)


# In[10]:


xs = np.linspace(0,35,100)
#xs = np.linspace(-5,5,100)
mu = np.mean(pass1)
sig = np.std(pass1)
print(mu,sig)
print(pass1)

from scipy import stats


_,axe = plt.subplots()
axe.plot(xs,stats.norm.pdf(xs,loc = mu,scale=sig))
axe.plot(v,prob)


# In[9]:


get_ipython().system('pip install scipy')


# In[ ]:




