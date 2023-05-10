#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[14]:


# index

df1 = pd.DataFrame({
    'Key': ['K0','K1','K2','K3'],
    'A': ['A0','A1','A2','A3'],
    'B': ['B0','B1','B2','B3'],
}, index = [5,6,7,8])
print(df1)
#print(df1.index)
#df1.index = [0,1,2,3]
#print(df1)
# df1.index = df1['Key']
# df1.drop('Key',axis = 1, inplace = True)
# print(df1)
df1.set_index('Key',inplace=True)
print(df1)

df1.reset_index(inplace = True)
print(df1)

df1.set_index(['Key','A'],inplace=True)
print(df1)
#print(df1.loc[('K0','A0'),:])
print(df1.loc['K0',:])

# df1.reset_index(level = 0,inplace=True)
# print(df1)


# In[35]:


df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)


df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)


df3 = pd.DataFrame(
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    },
    index=[8, 9, 10, 11],
)


frames = [df1, df2, df3]
df2.index=[3,4,5,6]
df3.index=[6,7,8,9]
#result = pd.concat(frames, axis = 1,join = 'outer')
#result = pd.concat([df1,df2], axis = 1, join = 'inner')
#result = pd.concat([df1,df2], axis = 1, join 'outer')
#result = pd.concat([df1,df2])

result = pd.concat(frames, keys=['one','two','three'])
print(result)
print(result.loc[('two',4),'C'])


# In[37]:


left = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)


right = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)


result = pd.merge(left, right, on="key")
print(right)
print(left)
print(result)

