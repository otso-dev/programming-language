# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import sys
print(sys.version)



# +
a = 10
b = 10.5
c = 'abcd'
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(a + b)

del c
# -

print(c)

# +
# list, tuple, set, dictionary
list1 = [1,2,3,4]
print(list1)
print(type(list1))

list2 = [1,10.5,'abc',False,[1,2,3,4],{1,2,3,4}]
print(list2)
print(type(list2))

tuple1 = (1,2,3,4)
print(tuple1)
print(type(tuple1))

set1 = {1,2,3,4}
print(set1)

list2 = [1,2,3,4,4,5,5,5]
set2 = {1,2,3,4,4,5,5,5}
print(list2)
print(set2)

d1 = {'1':1, 'b':2,'c':3}
print(type(d1))
print(d1)
# -

a = 5
if a > 5:
    print('greater than 10')
elif a>3:
    print('greater than 3')
elif a==5:
    print('is five')
else:
    print('not greater than 10')

for _ in range(4):# _ 변수없이 순환
    print('message')

# +
a = range(0,50,3)# start, stop
print(a)
print(type(a))

for i in a:
    print(i)



# +
# 100에서 500미만 5의 배수
list1 = []
for i in range(100,500,5):
    list1.append(i)

print(list1)
# -

list2 = [x * 10 for x in range(100,500,5)]
print(list2)

# +
a = 0
b = 0
c = 0
for i in range(0,100):
    if i % 3 == 0 or i % 5 == 0:
        a += i
print(a)

list_3 = [x for x in range(0,100,3)]
list_5 = [x for x in range(0,100,5)]


list_3_a = []
for i in list_3:
    if i % 5 > 0:
        list_3_a.append(i)
print(list_3_a)
for i in list_3_a:
    b = b+i
for i in list_5:
    b = b+i
print(b)

set1 = list_3 + list_5
set1 = set(set1)
set1 = list(set1)
for i in range(0,len(set1)):
    c += set1[i]
print(c)

# -

list_3 = [i for i in range(0,100,3)]
list_5 = [i for i in range(0,100,5)]
print(list_3 + list_5)

# +
list_all = []
for i in list_3:
    list_all.append(i)
for i in list_5:
    list_all.append(i)
print(list_all)
set1 = set(list_all)
print(set1)

s = 0
for i in set1:
   s = s + i
print(s)
print(sum(set1))

# +
list_a = []
for i in range(0,100):
    if i % 3 == 0 or i % 5 == 0:
        list_a.append(i)
    
print(list_a)
print(sum(list_a))
# -

list_a = [i for i in range(0,100) if i % 3 == 0 or i % 5 == 0]
print(sum(list_a))
