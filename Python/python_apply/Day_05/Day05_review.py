#!/usr/bin/env python
# coding: utf-8

# In[13]:


# data type
# int(), float(), bool(), str() -> ()붙이면 data type casting

try:
    a = [20.5,'10.5']
    for i in a:
        int(i)
except:
    print(i)
#a = [20.5,'10.5']
a ='string'
if isinstance(a,type([])):
    print('datatype:list')
elif isinstance(a,type('')):
    print('datatype:str')
# list [], tuple (), set, dictionary {}


# In[44]:


# dictionary : key value
dict1 = {'a': 1, 'b': 2, 'c': 3}

key_list = list('xyz')
value_list = [10,20,30]
x = zip(key_list,value_list) # [('x',10),('y',20),('z',30)]
dict2 = dict(x)
print(dict2)

print(dict2['x'])
print(dict2.get('x'))

dict2['y'] = 50
print(dict2)

dict2['newkey'] = 1234
print(dict2)

key_list = dict2.keys()
value_list = dict2.values()
print(key_list)
print(value_list)
print(dict2.items()) # zip한 상태

for e in dict2: # key value 같이 조회하기 (dict)
    print(e, dict2[e])


# In[14]:


# if: - else:
# if: -elif: - else:
if '':
    print('True')
else:
    print('False') # 0, ''비어있는 문자열/list안에 데이터 값이


# In[19]:


# for - range() / list; enumerate()
list_a = list('abcde')
for i ,c in enumerate(list_a):
    print(i,c)
# while - 조건
while len(list_a) > 1:
    list_a.remove(list_a[-1])
print(list_a)


# In[27]:


# function, class
def myfunction1(n):
    print('myfunction1',n)
    return n*5

class myclass:
    def __init__(self): #construct
        pass
    def mymethod1(self):
        print('mymethod1')
class myclass2(myclass):
    def __init__(self):
        print('const')
    def __del__(self):
        print('dest')
    def __str__(self):
        return 'myclass2'
    
x = myclass2() #const
print('===========') 
print(x) # str
print('===========')
del x # dest


# In[32]:


# file read
with open('lott.csv') as f:
    for line in f:
        pass
       # print(line)
        
# file write
with open('test.txt','w') as f: # 'w'; mode : 'w'rite / 'r'ead, 'b'inary -> 2진형태
    for i in range(3, 10):      # 'wb' write binary   
        f.write('test string{}\n'.format(i))


# In[35]:


import pickle
list_a = list('abcd')

# write
with open('pickle_test.pickle','wb') as f:
    pickle.dump(list_a, f)
    
# read
with open('pickle_test.pickle', 'rb') as f:
    list_b = pickle.load(f)
print(list_b)

