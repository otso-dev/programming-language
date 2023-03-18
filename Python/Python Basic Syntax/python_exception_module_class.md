## exception
```python
# 형변환이 가능한 것만 형변환 시킴
a = 'abc'
print(a)
print(type(a))

#exception 예외처리
x = []
try:
    #b = float(a)
    print(x[0])
except ValueError:
    b = -1
except IndexError:
    print('IndexError')
print(b)
print(type(b))
```
## casting
```python
data_list = []
with open('전국건강증진센터표준데이터.csv') as f:
    for line in f:
        data_list.append(line.split(','))
data_list = data_list[1:]
#print(data_list)
#print(len(data_list))
centor_list = []
doctor_list = []
for i in data_list:
    centor_list.append(i[0])
    doctor_list.append(i[11])

#print(doctor_list)

total_doctor = 0
for i in doctor_list:
    total_doctor += int(i)
centor_set = set(centor_list)
total_centor = len(centor_list)
di_list = dict(zip(centor_list,doctor_list))

zero_centor = 0
for i in doctor_list:
    if int(i) == 0:
        zero_centor += 1
    
print(total_centor,'-> 총 센터 갯수','\n',zero_centor,'-> 의사가 없는 센터 갯수\n',total_doctor,'-> 총 의사명 수')
    
```

## module

```python
import random #random 전체를 가져옴
random.randrange(0,100,2)

from random import randrange as rr #random에서 import를 randrange만 가져와서 쓰겠다.
rr(0,100,3)

import random as rand # random을 as로 rand바꿔서 쓰겠다.

import mymodule as module
module.myfn1('my module import')
```

## class

```python
# python은 java와 같이 소멸자를 따로 할 필요가 없음
class myclass:
    myvar1 = 10 # class 내부안에서 쓸 수 있는 변수
    myvar2 = 'abc'
    
    def __init__(self,a = 0,b = 'aaa'): # __는 class내부에서 쓰는 메소드
        self.myvar1 = a
        self.myvar2 = b
    
    def mymethod1(self, n):
        print(self.myvar1 * n,self.myvar2)
    
    def __str__(self):
        return 'myclass: {},{}'.format(self.myvar1, self.myvar2)

a = myclass(100,'def')
print(a)
print(type(a))
a.mymethod1(5)

class myclass2(myclass): # class명(상속받을 class명)
    pass
b = myclass2(1)
b.mymethod1(10)
```
## list를 상속받은 myclass
remove_all 메소드를 만들어서 씀
```python  
class mylist(list):
    def remove_all(self,target_value):
        while target_value in self:
            self.remove(target_value)
        return self
mylist_1 = mylist(list('abccdc'))
mylist_1.append(1)
mylist_1.append(2)
print(mylist_1)
print(mylist_1.remove_all('c'))
```
