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

# +
list_a = [i for i in range(10)]
list_b = [i for i in range(100,110)]
print(list_a)
print(list_b)

# in list에 값이 있는지 확인
if 10 not in list_a:
    print('True')
else:
    print('False')
    
# concat 여러개의 리스트를 합 칠때
list_c = list_a + list_b
print(list_c)

# * 
print(list_a * 2) # 2 * list_a




# +
#indexing
list_d = list('abcdefghicjklmn')
print(list_d)
print(list_d[3])
print(list_d[3:6])
print(list_d[3:10:2])

print(len(list_d))
print(min(list_d))
print(max(list_d))

c_index = list_d.index('c',3, 10)
print(c_index)
#list_d[c_index] = 'x'
#print(list_d)

print('count:', list_d.count('c'))

# +
s = 'While The Python Language Reference describes the exact syntax and semantics of the Python language, this library reference manual describes the standard library that is distributed with Python. It also describes some of the optional components that are commonly included in Python distributions.'
list_char = list(s) # lower()-> 문자열을 다 소문자로 바꾸는 함수
set_char = set(list_char)
print(set_char)

exclude_list = [',',' ','.']
for i in set_char:
    if i not in exclude_list:
        print(i,list_char.count(i))
# -

help(list)

# +
list_a = [1,2,3]
list_b = list('abc')
print(list_a)
print(list_b)

d2 = dict(zip(list_b, list_a))
print(d2)
print(d2.items())

d3 = dict([('a', 1), ('b', 2), ('c', 3)])

print(d3)
print(d3['c'])
print(d3.get('x'))
d3['y'] = 15
print(d3)

# +
for i in d3:
    print(i,d3[i])
    
print(d3.keys())
print(d3.values())

for i in d3.values():
    print(i)
d3['y'] = 20
print(d3)
