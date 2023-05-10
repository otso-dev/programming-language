#!/usr/bin/env python
# coding: utf-8

# ## Kosis 부산광역시 가스사용량
# 
# - 년도별 도시가스/프로판 판매량 비율
# 
# - 년도별 도시가스, 년도별 프로판 사용량 상관도
# 
# - 도시가스
#   * 년도별 겨울(10,11,12,1,2,3)평균사용량/ 비겨울(4,5,6,7,8,9) 평균사용량
#   * -> ttest(평균 사용량에 차이가 있는가.)
#   * 같은 분석을 프로판/부탄 가스를 대상으로도 실행.
#   
#  

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.set_printoptions(precision=5,suppress=True)

def my_split(s):
    block_start = False
    start_index = 0
    ret_list=[]
    for i, c in enumerate(s):
        if block_start==False:
            if c==',':
                ret_list.append(s[start_index:i])
                start_index=i+1
            elif c=='"':
                block_start=True
                start_index = i
        else:
            if c=='"':
                block_start=False
    if s[-1]!=',':
        ret_list.append(s[start_index:])
    return ret_list

def split_len(data_list):
    len_list=[]
    for e in data_list:
        len_list.append(len(e))
    print(set(len_list))
    if len(set(len_list))>1:
        for i in set(len_list):
            print(i, len_list.count(i))
    return set(len_list)


# In[3]:


csv_data = []
with open('가스공급량_20230217170922.csv') as f:
    for line in f:
        csv_data.append(line[:-1].split(','))


t = set()
for e in csv_data:
    t.add(len(e))
print(t)
np_data = np.array(csv_data[2:])
np_data = np_data[:,2:].astype(np.int64)
print(np_data[:3])


# In[4]:


#print(np_data.shape)
#print(np.arange(0,130,12))
by_year = np.add.reduceat(np_data,np.arange(0,130,12))
print(by_year[:3])
total_gas = by_year[:,1] + by_year[:,3]
ln_gas = by_year[:,1]/total_gas
lp_gas = by_year[:, 3]/total_gas


_, axe = plt.subplots()
#axe.plot(np.arange(2010,2021), by_year[:,3])  # 년도별 도시가스 총 사용량
axe.plot(np.arange(2010,2021), by_year[:,1])
#axe.plot(np.arange(2010,2021), by_year[:,1]/12)  # 년도별 도시가스 평균 사용량

 # 년도별 도시가스+프로판 사용량 대비, 도시가스 사용량 비율
#axe.plot(np.arange(2010,2021),ln_gas)

#axe.plot(np.arange(2010,2021),lp_gas)


# In[10]:


print(np.corrcoef(by_year[:,1], by_year[:,5]))
_, axe = plt.subplots()
print(by_year[:,1].shape)
print(by_year[:,5].shape)
axe.scatter(by_year[:,1],by_year[:,5])


# In[6]:


#print(np_data[:10])
by_season = np.add.reduceat(np_data[3:], np.arange(0,130,6))
#print(by_season[:3])
summers_sum = by_season[::2]
winters_sum = by_season[1::2]
print(summers_sum[:2])
print(winters_sum[:2])


# In[7]:


# 2010 여름 평균 사용량 : 프로판 가스
lp_gas2010_summer = np_data[3:9,3]
print(lp_gas2010_summer)
#print(summers_sum[0])
#print(np_data[3:9])

# 2010 - 2011 겨울 평균 사용량 : 프로판 가스
lp_gas2010_winter = np_data[9:15,3]
print(lp_gas2010_winter)
#print(winters_sum[0])
#print(np_data[9:15])


#ttest 귀무가설
# - 두개의 mean 값은 같은 모집단에서 나온것.
# - 두개의 mean 같을 같은 것으로 보아야 한다.
stats.ttest_ind(lp_gas2010_summer,lp_gas2010_winter)


# In[8]:


# 2011년 여름  , 2011-2012년 겨울 도시가스 사용량 ttest_ind
ln_gas2011_summer = np_data[15:21,1]
print(ln_gas2011_summer)
ln_gas2011_winter = np_data[21:27,1]
stats.ttest_ind(ln_gas2011_summer,ln_gas2011_winter)


# In[9]:


_,axe = plt.subplots()
year = 2010
gas_index = 1
for i in range(0,10,2):
    j = 3+6*i
    summer = np_data[j:j+6]
    winter = np_data[j+6:j+12]
    axe.plot(np.arange(3,9),summer[:,gas_index])
    axe.plot(np.arange(9,15),winter[:,gas_index])

