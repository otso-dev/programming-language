# 파일 입출력

```python
data_list = []

# -> == f.close() # file을 open을 하면 반드시 file을 close를  해야한다. comma seperated values -> comma(,)로 구분한 파일, encoding = '인코딩할 유형'
with open('부산광역시_노인복지관 현황_20230101.csv',encoding = 'cp949') as f:
    for line in f:
        data_list.append(line.split(','))
data_list = data_list[1:]
gu_list = []
for i in data_list:
    adrress = i[2]
    adrress_list = adrress.split()
    gu_list.append(adrress_list[1])

print(gu_list.index('다대로'))
print(gu_list)
gu_list[21] = '사하구'

gu_set = set(gu_list)
for i in gu_set:
    print(i,gu_list.count(i))
    
gu_key = []
gu_value = []
for i in gu_set:
    gu_key.append(i)
    gu_value.append(gu_list.count(i))
gu_di = dict(zip(gu_key,gu_value))
print(gu_di)

def fn10(x):
    return x[1]
#print(gu_di.items())
d1_sorted = dict(sorted(gu_di.items(),key = fn10, reverse = False))#dict(sorted(사용할 di,기준이될 key값,정렬순서))
print(d1_sorted)

```

## 

```python

```
