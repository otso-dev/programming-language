#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

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


# In[ ]:


# 주사위를 3번 던져 나올수 있는 모든 경우의 수 : 6**3
# --> with replacement

# 1에서부터 6까지 숫자가 적힌 공이 든 박스에서 3개의 공을 꺼낼때 
# 나올수 있는 모든 경우의 수 : 6 * 5 * 4
# --> without replacement

# 1에서부터 6까지 숫자가 적힌 공이 든 박스에서 3개의 공을 꺼내면서
# 꺼낸공을 다시 집어넣고, 섞어서 뽑았을 때 나올수 있는 모든 경우의 수 : 6**3
# --> with replacement


# In[ ]:


# permutation (순열) : (a, b, c),(b, c, a) -> (순열에서는)다른 것으로 취급함, 순서의 개념

# 1에서부터 6까지 숫자가 적힌 공이 든 박스에서 2개의 공을 꺼낼때 
# 나올수 있는 모든 경우의 수 : 6 * 5
# --> without replacement

# n = 6
# r = 2

#n!/(n-r)!


# In[ ]:


# combination(조합) : (a, b, c),(b, c, a) -> (조합에서는)같은것 으로 취급함, 순서의 개념없음.

# 1에서부터 6까지 숫자가 적힌 공이 든 박스에서 2개의 공을 꺼냈을때
# '다른구성'으로 나올수 있는 모든 경우의 수 : 
# --> without replacement

#permutatin(순열)에서 구성이 같은 것을 제외 -> combination(조합)
#n = 6
#r = 2
#combination = permutatin(n,r)/r!


# In[17]:


# 재귀함수 :자기 자신을 부르는(사용하는) 함수
#     - 탈출조건이 중요!
def fact_r(n):
    if n == 2:
        return n
    return fact_r(n-1)*n

def fact(n):
    ret = 1
    while n > 1:
        ret *= n
        n -= 1
    return ret
def fact_np(n):
    #return np.arange(2,n+1).prod()
    return np.multiply.reduce(np.arange(2,n+1))

#6!=6*5*4*3*2*1 = 6*5!
def perm(n,r):
    return fact_r(n)/fact_r(n-r)

def combi(n,r):
    return perm(n,r)/fact_r(r)
assert fact(6) == fact_np(6)
assert perm(6,2) == 30.0
assert perm(6,3) == 120.0
assert combi(6,2) == 15.0


# In[20]:


#count_with_replacement_order(list('abcdef'), 3)
#perm_pool(list('abcdef'),3)
combi_pool(list('abcdef'),3)

