# numpy
> NumPy는 과학 컴퓨팅 및 데이터 분석에 널리 사용되는 Python 라이브러리입니다. 동종 데이터의 다차원 컨테이너인 배열에 대한 지원과 배열에서 선형 대수 및 통계 연산과 같은 수학적 연산을 수행하는 함수를 제공합니다. 또한 NumPy는 SciPy, Matplotlib 및 Pandas와 같은 다른 인기 있는 Python 라이브러리와 통합되어 데이터 과학 및 과학 컴퓨팅을 위한 강력한 도구가 됩니다. 배열 기능 외에도 NumPy에는 난수 생성, C/C++ 및 Fortran 코드 통합 도구, 희소 배열 작업 도구와 같은 기능이 포함되어 있습니다.

## numpy 쓰기

```python
import numpy as np

a1 = np.array([1,2,3,4,5])
print([1,2,3,4,5])
print(a1)
print(type(a1))

a2 = np.arange(10)
print(a2)

# 100 아래의 3의 배수
a3 = np.arange(0,100,3)
print(a3)

# 1에서부터 10아래 0.5씩 증가하는 숫자. stop = 0.5 -> numpy는 소수점이 되지만 그냥 python에서는 불가능
a4 = np.arange(1.3,10,0.5)
print(a4)

a5 = np.linspace(0,10,3) # 0 과 10사이의 n개의 숫자를 주는 함수
print(a5)

!pip install numpy

a6 = np.zeros(5)
print(a6)

a7 = np.ones(5, dtype = np.int64) # datatype을 바꾸는 것
print(a7)
a7.astype(np.float64) # 만들어진 것을 datatpye을 바꿀때
# array안에 있는 datatype은 list와 달리 똑같은 type만 들어가야한다.

lista = [1,2,3.5,4.2]
a8 = np.array(lista)
print(a8)
listb = [1,2,'abc','def']
a9 = np.array(listb)
print(a9)
#a9.astype(np.int64)

# numpy는 for문을 알아서 써주는 method가 많다.
print(a8.dtype)
print(a8.ndim) # 몇차원의 array인지 알려주는 method
print(a8.shape) # array의 차원마다 모양(길이)를 알려주는 method tuple형태로 반환함
print(a8.size) # array안의 모든 데이터 갯수를 알려주는 method

print(a8.itemsize) #array의 datatype의 size를 알려주는 method
print(a8.data) # 

a10 = np.arange(10,100,5)
print(a10)
# 특정index
print(a10[2])
# start , stop
print(a10[5:])
print(a10[0:3])
# start, stop, step
print(a10[6:20:2])

a10 = np.arange(10,100,5)
print(a10)
print(a10[[1,3,7]]) # numpy는 index의 값을 이용해 list로 받을 수 있음

# list10 = [x for x in range(10,100,5)]
# print(list10)
#print(list10[[1,2,3]]) -> list는 못함


a10 = np.arange(10,100,5)
print(a10)
print(a10[a10 % 10 == 5]) # 조건식을 줄 수 도 있다. 해당 조건에 맞는 index를 list로 반환함

x = (a10 % 10 == 5)
print(x)
print(x.shape)
print(a10.shape)
print(a10[x])

lista = [x for x in range(5)]
listb = [x for x in range(10,15)]
print(lista)
print(listb)
print(lista+listb)
print(lista-listb)

a1 = np.arange(5)
a2 = np.arange(10,15)
print(a1)
print(a2)
print(np.concatenate((a1,a2))) #2개의 array를 합칠 때
print('sum',a1+a2) # python list와 달리 array + 는 각 요소를 더해서 반환한다.(사칙연산 가능) -> 두개이상의 array를 사칙연산을 할려면 size가 같아야한다.
print('sub',a1-a2)
print('mul',a1*a2)
print('div',a1/a2)
```
## numpy 활용

```python
import numpy as np
import math
def dist_np(p1,p2): 
    return math.sqrt(sum((p2-p1) **2))
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

csv_data = []
with open ('전국자동차정비업체표준데이터.csv') as f:
    for line in f:
        csv_data.append(my_split(line))

loc_list = []
for e in csv_data[1:]:
    loc_list.append(e[4:6])

for e in loc_list:
    for i, v in enumerate(e):
        try:
            e[i] = float(v)
        except:
            e[i] = 0.0
print(loc_list[:3])
dist_np([35.1531,129.0596], )

target_p = np.array([35.1531,129.0596])
dist_list = []
for i, p2 in enumerate(loc_list):
    try:
        dist_list.append([i,dist_np(target_p,np.array(p2))])
    except:
        dist_list.append([i,100.0])
#print(dist_list[:3])

r = sorted(dist_list, key = lambda x : x[1])
#print(r[:5])
for x in r[:5]:
    print(csv_data[x[0]])
```
