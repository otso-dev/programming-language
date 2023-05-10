#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import numpy as np

def my_sq_prod(python_list):
    return_list = []
    for number in python_list:
        return_list.append(number**2)
    return math.prod(return_list)

assert my_sq_prod([1,2,3]) == 36


# In[2]:


def my_sq_prod3(numpy_ndarray):
    values = numpy_ndarray**2
    result = 1
    for number in values:
        result *= number
    return result

assert my_sq_prod([4,5,6]) == 14400


# In[3]:


def score_check():
    score = 0

    if my_sq_prod([1,2,3])==36:

        score += 30

    print(score)


# In[4]:


if __name__ == '__main__':
    score_check()


# In[5]:


import numpy as np

import pandas as pd

import random

 

random.seed(123)

pd_iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

pd_iris.columns = ['petal_length', 'petal_width', 'sepal_length', 'sepal_width', 'class']


# In[6]:


rand_axis0 = [random.randint(0,150) for _ in range(5)]

rand_axis1 = [random.randint(0, 4) for _ in range(5)]

pd_iris.iloc[rand_axis0, rand_axis1] = np.NaN

rand_axis0 = [random.randint(0,150) for _ in range(5)]

rand_axis1 = [random.randint(0, 4) for _ in range(5)]

pd_iris.iloc[rand_axis0, rand_axis1] = 123.4 + random.randint(0,4)/10

df1 = pd.DataFrame(np.arange(100, 120).reshape(4,5), dtype='str')


# In[7]:


pd_iris['petal_length'].isna().value_counts()
for i in pd_iris['petal_length']:
    pass
#     print(i)
# print(pd_iris['petal_length'].describe())
q1, q3 = pd_iris['petal_length'].quantile([0.25,0.75])
iqr = q3 - q1
upper = q3 + 1.5 * iqr
lower = q1 - 1.5 * iqr

filter1 = pd_iris['petal_length'] > upper
pd_filter = pd_iris[filter1]
# pd_filter.value_counts()
pd_iris['petal_length']=pd_iris['petal_length'].dropna()


# In[11]:


pd_iris['petal_length'].dropna().mean()


# In[33]:


df1.columns = ['petal_length', 'petal_width', 'sepal_length', 'sepal_width', 'class']
df_combine = pd.concat([pd_iris,df1],ignore_index=True)
print(df_combine.shape)


# In[32]:




