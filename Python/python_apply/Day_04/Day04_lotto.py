#!/usr/bin/env python
# coding: utf-8

# In[73]:


csv_data =[]
with open('lott.csv') as f:
    for line in f:
        csv_data.append(line[:-1].split(','))
        #csv_data.append(line.replace('\n','').split(','))
#print(csv_data)
int(csv_data[0][-1])
# for i in csv_data:
#     print(i)
#     for e, e_i in enumerate(i):
#         print(e, e_i)
num_list = []


# In[18]:


for e in csv_data:
    for i, e_i in enumerate(e):
        e[i] = int(e_i)
        
print(csv_data[:3])
        


# In[69]:


import math
def mean(num_list): # 평균
    return sum(num_list)/len(num_list)
def mean_2(num_list):
    sum_value = 0
    for i in num_list:
        sum_value += i
    return sum_value/len(num_list)
def medain(num_list): # 중앙값
    num_list.sort()
    if len(num_list) % 2 == 0:
        i = len(num_list)//2    #medain_value1 = num_list[int(len(num_list)/2) - 1]
                                #medain_value2 = num_list[int(len(num_list)/2)]
        return (num_list[i] + num_list[i - 1])/2 #(medain_value1 + medain_value2) / 2
    else:
        i = (len(num_list))//2
        return num_list[i] #내가 한 방법->num_list[int(len(num_list)/2)]
    
def dev(num_list): # 편차
    m = mean(num_list)
    return [x-m for x in num_list]

def var(num_list): # 분산
    n = len(num_list)
    d = dev(num_list)
    return sum([x * x for x in d])/(n - 1) # 전체를 다룰때는 -1을 안하고 샘플을 가져와서 했을때는 -1을 해준다.

def stdev(num_list): #표준편차
    return math.sqrt(var(num_list))

game1 = csv_data[0]
game2 = csv_data[1]
print(game1)
print(mean(game1))

print(medain(game1[1:]))
print(medain(game1))
#[5, 17, 26, 27, 35, 38, 1]

assert medain([5, 17, 26, 27, 35, 38, 1]) == 26 # 테스트할때 쓰는 키워드 assert
assert medain([5, 17, 26, 27, 35, 38]) == 26.5

print(dev(game1))
print(var(game1))
print(stdev(game1))


# In[59]:


# in-place 원본 값 자체가 바뀌는 것
list_a = [5, 17, 26, 27, 35, 38, 1]
print(sorted(list_a))
print('after sorted:', list_a)

list_a.sort()
print(list_a)


# In[61]:


# reference
list_a = [5, 17, 26, 27, 35, 38, 1]
list_b = list_a #shallow copy, 얕은복사
print('list_a:',list_a)
print('list_b:',list_b)
list_a[0] = 100
list_b[1] = 50
print('list_a:',list_a)
print('list_b:',list_b)


# In[62]:


# reference
list_a = [5, 17, 26, 27, 35, 38, 1]
list_b = []
for i in list_a:
    list_b.append(i)# deep copy, 깊은 복사
    
print('list_a:',list_a)
print('list_b:',list_b)
list_a[0] = 100
list_b[1] = 50
print('list_a:',list_a)
print('list_b:',list_b)


# In[7]:


help(str)

