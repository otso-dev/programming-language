#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
import numpy as np
import matplotlib.pyplot as plt

with open('iris_ndarray.pickle','rb') as f:
    iris_np = pickle.load(f)

sepal_length = iris_np[:,0]
sepal_width = iris_np[:,1]
sepal_ratio = sepal_length/sepal_width
#print(sepal_ratio)
petal_length = iris_np[:,2]
petal_width = iris_np[:,3]
petal_ratio = petal_length/petal_width
#print(petal_ratio)
#print(np.divide(iris_np[:,0],iris_np[:,1]))
#print(np.divide(iris_np[:,2],iris_np[:,3]))

print(sepal_ratio.shape)
sepal_ratio_2d = np.expand_dims(sepal_ratio,1)

# 축 추가 다른 방법
petal_ratio_2d = petal_ratio[:,np.newaxis]


concat_result = np.concatenate((sepal_ratio_2d,petal_ratio_2d),axis = 1)
print(concat_result[:5])


# In[2]:


_, axe = plt.subplots()
#scatter 점으로 표현
axe.set_xlim(0,8) #x 값 고정
axe.set_ylim(0,3.0)# y 값 고정
filter_class0 = iris_np[:,-1] == 0.0
iris_np_class0 = iris_np[filter_class0]

filter_class1 = iris_np[:,-1] == 1.0
iris_np_class1 = iris_np[filter_class1]

filter_class2 = iris_np[:,-1] == 2.0
iris_np_class2 = iris_np[filter_class2]

#print(filter1)
axe.scatter(iris_np_class0[:,2],iris_np_class0[:,3]) # class 0만 플롯, bool list를 이용 필터링
axe.scatter(iris_np_class1[:,2],iris_np_class1[:,3])
axe.scatter(iris_np_class2[:,2],iris_np_class2[:,3])

#knn 알고리즘
#k-Nearest Neighbor


# In[21]:


def kNN_predict(iris_np_data,petal_length,petal_width): # k = 5
#(150,2) (2,)
    sub_data = iris_np_data[:,2:4]
    target_np = np.array([petal_length,petal_width])
    print(sub_data.shape)
    print(target_np.shape)
    #print(target_np - sub_data)      # [5.0 1.5] - [1.4 2.0]
    #print((target_np - sub_data)**2) # [a b] [a**2 b**2]
    #print(np.sum((target_np - sub_data)**2,axis = 1))
    dist = np.sqrt(np.sum((target_np - sub_data)**2,axis = 1))
    print(dist[:3],len(dist))
    class_np = iris_np_data[:,-1]
    print(class_np[:3], len(class_np))
    
    dist_1 = np.expand_dims(dist,1)
    class_np_1 = np.expand_dims(class_np,1)
    print(dist_1.shape)
    print(class_np_1.shape)
    r = np.concatenate((dist_1,class_np_1),axis = 1)
    print(r.shape)
    r = sorted(r, key = lambda x : x[1] , reverse = True)
    print(r[:10])
    #r1 = np.sqrt((target_np - sub_data)**2)
    #print(r1)
    
kNN_predict(iris_np,5.0,1.5) # 거리가 가장 가까운 5개 샘플기록 반환

