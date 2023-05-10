#!/usr/bin/env python
# coding: utf-8

# ### 전국육교정보데이터
# * 제가각 계산시 결측지 있는 샘플은 버림.
# 
# - 내진설계된 육교 퍼센트
# - 안전등급별 육교갯수, 비율
# - 육교가 만들어진 연도 vs 장애인편의시설간 상관관계
#     - 연도, 장애인편의시설 갖춘 육교의 갯수/해당연도 건설 육고 갯수
# 
# - 길이가 가장 긴 육교(육교연장)
# - 가장 튼튼한 육교(허용통행하중)
# - 가장 높은 육교(통행제한 높이)
# 
# - 육교연장,허용통해하중,통행제한 높이에 대해 최대,최소값,평균,표준편차

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

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


# In[9]:


csv_data = []
with open('전국육교정보표준데이터.csv') as f:
    for line in f:
        csv_data.append(my_split(line[:-1]))
#print(csv_data[:3])
#split_len(csv_data)
for e in enumerate(csv_data[0]):
    print(e)
np_data = np.array(csv_data)
print(np_data.shape)


# In[24]:


# 내진설계
sub_data = np_data[1:,20]
#print(sub_data[:3])

val,cnt=np.unique(sub_data,return_counts = True)
print(val,count)
print((cnt[1:]*100)/np.sum(cnt[1:]))

filter1 = sub_data!=' '
sub_data_f = sub_data[filter1]
val,cnt = np.unique(sub_data_f,return_counts = True)
print(val,cnt)
print(cnt*100/np.sum(cnt))


# In[45]:


# 안전등급별 육교 갯수
sub_data = np_data[1:, 21]
filter1 = np_data[:,21] == '불량'
val,cnt = np.unique(sub_data,return_counts = True)
print(val,cnt)
val2 = np.expand_dims(val,1)
cnt2 = cnt[:,np.newaxis]
cnt_percent = cnt*100/np.sum(cnt)
cnt_percent2 = np.expand_dims(cnt_percent,1)
np.concatenate((val2,cnt2,cnt_percent2),1)

np_data[filter1]


# In[67]:


# 육교연장,허용통행하중,통행제한높이: 최소,최대,평균,표준편차
#sub_data = np_data[:,7:11]
print(np_data[0,7:11])
for i in range(7,11):
    print('***',np_data[0,i])
    sub_data = np_data[1:,i]
    filter1 = (sub_data!='') & (sub_data!='0') & (sub_data!='0.0')
    #print(np.unique(sub_data[filter1]))
    sub_data_f = sub_data[filter1].astype(np.float64)
    #print(sub_data_f)
    print('최소',np.min(sub_data_f))
    print('최대',np.max(sub_data_f))
    print('평균',np.mean(sub_data_f))
    print('표준편차',np.std(sub_data_f))
    
filter2 = (np_data[:,8] == '150.0') | (np_data[:,8]=='150')
np_data[filter2]


# In[77]:


# 준공연도별과 장애인편의 시설 여부의 상관관계
sub_data = np_data[1:,[14,19]]
#print(sub_data)
#np.unique(sub_data[:,0])
#np.unique(sub_data[:,1]) 결측치 찾기
filter1 = sub_data[:,1]!=''
sub_data = sub_data[filter1]

year_yn = []
for yn,ymd in sub_data:
    yr = ymd.split('-')[0]
    year_yn.append(yr+'-'+yn)
    #print(yn,ymd)
#print(year_yn)
year_yn = np.array(year_yn)
val,cnt = np.unique(year_yn,return_counts=True)
print(val,cnt)


# - 방법  
# ### pass1
# {
#     year: [y,n,....]
# }
# ### pass2
# [
#     [year,y_count,ratio]
# ]

# In[89]:


sub_data = np_data[1:,[14,19]]
filter1 = sub_data[:,1]!=''
sub_data = sub_data[filter1]

pass1 = dict()
for yn,ymd in sub_data:
    yr = ymd.split('-')[0]
    if yr in pass1.keys():
        pass1[yr].append(yn)
    else:
        pass1[yr] = [yn]
        
#print(pass1)

pass2 = []
for yr in pass1:      #dict 순환시 key값으로 순환이 된다.
    val, cnt = np.unique(pass1[yr],return_counts=True)
    y, ratio = 0, 0
    if 'Y' in val:
        y = cnt[val == 'Y']
    ratio = y*100/np.sum(cnt)
    pass2.append((int(yr),int(y),float(ratio)))
#print(pass2)
np.set_printoptions(precision=3,suppress=True)#numpy 소수점 제거
pass3 = sorted(pass2,key=lambda x : x[0])
pass3 = np.array(pass3)
print(pass3)


# In[91]:


_,axe = plt.subplots()
axe.plot(pass3[:,0],pass3[:,2])


# In[95]:


#print(pass3)
filter1 = pass3[:,0]>=1990
pass4 = pass3[filter1]
print(pass4)
print(np.corrcoef(pass4[:,0],pass4[:,2]))


# In[110]:


# iqr, outliers(이상치)
#이상치 -> 값이 있지만 값이 이상한 것
i = 7
print('***',np_data[0,i])
sub_data = np_data[1:,i]
filter1 = (sub_data!='') & (sub_data!='0') & (sub_data!='0.0') # 결측치 제거
#print(np.unique(sub_data[filter1]))
sub_data_f = sub_data[filter1].astype(np.float64)

#print(sub_data_f)
# print('최소',np.min(sub_data_f))
# print('최대',np.max(sub_data_f))
# print('평균',np.mean(sub_data_f))
# print('표준편차',np.std(sub_data_f))
print('중앙값:',np.median(sub_data_f))
print('quantile:',np.quantile(sub_data_f,[.25,.5,.75]))
q25,q50,q75 = np.quantile(sub_data_f,[.25,.5,.75])
iqr = q75 - q25
print('iqr:',iqr)
print('upper:',q75+1.5*iqr) # 95.0
print('lower:',q25-1.5*iqr) # -9.0





'''
------------------q25-------------------q50------------------q75-------------------
q25-1.5*iqr(하한선)                                               q75+1.5*iqr(상한선)

'''

upper = q75+1.5*iqr
sub_data_cut = sub_data_f[sub_data_f<upper]
val, cnt = np.unique(sub_data_cut,return_counts = True) # 육교연장 값의 분포

_, axe = plt.subplots()
axe.scatter(val,cnt)


# In[116]:


upper = q75+1.5*iqr
sub_data_cut = sub_data_f[sub_data_f<upper]

h_cnt, h_bins = np.histogram(sub_data_cut,bins = 20) #float형을 칸으로 구분해서 리턴하는 함수.
print(h_cnt,h_bins)

val, cnt = np.unique(sub_data_cut,return_counts = True) # 육교연장 값의 분포

_, axe = plt.subplots()
#axe.scatter(val,cnt)
axe.plot(np.arange(20),h_cnt)


# In[117]:


_, axe = plt.subplots()
axe.scatter(pass4[:,0],pass4[:,2])

