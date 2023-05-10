#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd

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

result = pd.concat(frames, axis=0, keys=['one', 'two', 'three'])
print(result)


# In[18]:


df4 = pd.DataFrame(
    {
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    },
    index=[2, 3, 6, 7],
)


result = pd.concat([df1, df4], axis=0, join='outer')
print(result)


# In[ ]:





# In[23]:


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
result = pd.concat((left, right), axis=1)
print(result)


# In[26]:


left.index = left['key']
print(left)

right.index = right['key']
print(right)

result = pd.concat((left, right), axis=1)
print(result)


# In[50]:


x = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)
print(x)
x.index = x['key']
print(x)
x.drop('key', axis=1, inplace=True)
print(x)
x.reset_index(inplace=True)
print(x)
x.set_index('key', inplace=True)
print(x)
x.reset_index(inplace=True)
print(x)
x.set_index(['key', 'C'], inplace=True)
print(x)
print(x.loc[('K0', 'C0'),:])


# In[53]:


print(x)
x.reset_index(level=1)


# In[59]:


s1 = pd.Series(['K{}'.format(i) for i in range(5)], name='K')
s2 = pd.Series(['A{}'.format(i) for i in range(5)], name='A')
s3 = pd.Series(['B{}'.format(i) for i in range(5)], name='B')
df1 = pd.DataFrame()
df1['K'] = s1
df1['A'] = s2
df1['B'] = s3
print(df1)


# In[ ]:





# In[69]:


df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)

df2 = pd.DataFrame()
start_i = 4
for n in list('ABCD'):
    tr = range(start_i, start_i+4)
    ts = pd.Series(['{}{}'.format(n, x) for x in tr], index=[x for x in tr])
    print(ts)
    df2[n] = ts
print(df1)
print(df2)

