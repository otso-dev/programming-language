#!/usr/bin/env python
# coding: utf-8

# ### 자동차 연비 데이터 정제
# uci repo  
# url : https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data
# * requests 패키지 이용 데이터 로딩
# * 최대한 많이 정제
# * 배기량 연비
# * 연비 index = 0
# * 배기량 index = 2

# In[95]:


#자동차의 연비 데이터
import requests
import math
def mean(num_list): # 평균
    return sum(num_list)/len(num_list)

def dev(num_list): # 편차
    m = mean(num_list)
    return [x-m for x in num_list]

def var(num_list): # 분산
    n = len(num_list)
    d = dev(num_list)
    return sum([x * x for x in d])/(n - 1)

def stdev(num_list): #표준편차
    return math.sqrt(var(num_list))

def covar(list_1,list_2): # 공분산
    n = len(list_1)
    list_1_dev = dev(list_1)
    list_2_dev = dev(list_2)
    return sum(x * y for x, y in zip(list_1_dev,list_2_dev))/(n-1)

def corel(list_1,list_2): # 상관도 (-1 ~ 1)
    return covar(list_1, list_2)/(stdev(list_1)*stdev(list_2))


# In[ ]:


x = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data')


# In[81]:


pass1 = x.text.split('\n') # 한 줄씩 나누자 pass1의 목적 
#print(len(pass1))
pass2 = [] # 각 샘플(줄)별 숫자부분, 차명 부분 분리, split('\t') pass2의 목적
for line in pass1:
    pass2.append(line.split('\t'))
pass3 = [] # 숫자 부분 분리. split()
for e in pass2:
    try:
        y = e[0].split()
        y.append(e[1])
        pass3.append(y)
    except:
        pass


# In[82]:


pass4 = [] #float으로 형변환, 차명 " 제거
for e in pass3:
    for i, e_i in enumerate(e[:-1]):
        try:
            e[i] = float(e_i)
        except:
            e[i] = 0.0
        e[-1] = e[-1].strip('"')


# In[103]:


#print(pass3)
mpg_list=[]  # 연비
disp_list=[] # 배기량
weight_list=[]
for e in pass3:
    mpg_list.append(e[0])
    disp_list.append(e[2])
    weight_list.append(e[4])


# In[105]:


# 연비: 평균, 표준편차
print('연비 평균: {}\t연비 표준편차: {}'.format(mean(mpg_list),stdev(mpg_list)))
# 배기량: 평균, 표준편차
print('배기량 평균: {}\t배기량 표준편차: {}'.format(mean(disp_list),stdev(disp_list)))
# 차체중량
print('차체중량 평균: {}\t차체중량 표준편차: {}'.format(mean(weight_list),stdev(weight_list)))


# In[106]:


print('연비와 배기량 상관도: {}'.format(corel(mpg_list,disp_list)))
print('연비와 차체중량 상관도: {}'.format(corel(mpg_list,weight_list)))


# In[ ]:




