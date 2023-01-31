# python

## python변수와 자료형
```python
a = 10
b = 10.5
c = 'abcd'
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(a + b)
//python은 자료형 type이 없음
//데이터를 집어 넣을때 python이 변수에 자동으로 지정됨



# list, tuple, set, dictionary -> python은 기본적으로 자료형으로 쓰인다.
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
```

## list
모든 데이터타입을 넣을 수 있다.
## tuple
list와 같이 모든 데이터타입을 넣을 수 있지만 tuple은 한번 만들면 수정이 불가능하다.
## set
set안에 중복된 값을 넣으면 알아서 중복된 값을 지워준다.
## dictionary
map과 똑같은 구조를 가지고 있다. 

## if, for, list
tap의 간격이 중요함
```java
a = 5
if a > 5:
    print('greater than 10')
elif a==5:
    print('is five')
else:
    print('not greater than 10')
```
