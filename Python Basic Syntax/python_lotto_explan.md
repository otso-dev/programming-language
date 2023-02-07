# lotto 풀이

```python
import math
def mean(num_list): # 평균
    return sum(num_list)/len(num_list)

def dev(num_list): # 편차
    m = mean(num_list)
    return [x-m for x in num_list]

def var(num_list): # 분산
    n = len(num_list)
    d = dev(num_list)
    return sum([x * x for x in d])/(n - 1)

def stdev(num_list): #표준편차
    return math.sqrt(var(num_list))

csv_data =[]
with open('lott.csv') as f:
    for line in f:
        csv_data.append(line[:-1].split(','))
print(csv_data[:3])
int(csv_data[0][-1])

# enumerate를 이용한 방법
for game in csv_data:
    for i , num in enumerate(game):
        game[i] = int(num)
print(csv_data[:3])

# range 방법
for i in range(len(csv_data)):
    for j in range(len(csv_data)):
        csv_data[i][j] = int (csv_data[i][j])


# flat
lotto_num_flat = []
for game in csv_data:
    lotto_num_flat = lotto_num_flat + game
print(lotto_num_flat[:20])

lott_num_flat2 = []
for i in range(len(csv_data)):
    for j in range(len(csv_data[i])):
        lott_num_flat2.append(csv_data[i][j])
print(lott_num_flat2[:20])

lotto_num_domain = list(set(lotto_num_flat)) # domain 하나의 변수가 가질 수 있는 범위의 총합
lotto_num_freq = []
for num in lotto_num_domain:
    x = lotto_num_flat.count(num)
    lotto_num_freq.append(x)
#print(lotto_num_domain[:10])
#print(lotto_num_freq[:10])

dict_freq = dict(zip(lotto_num_domain,lotto_num_freq))
dict_freq = dict(sorted(dict_freq.items(), key = lambda x : x[1], reverse = True)) 
print(dict_freq)

x = list(dict_freq.keys())
print(x[:6])
# mode = 43


num_freq2 =[0] * 45 # 1 ~ 45를 담을 박스를 생성한다고 생각

for i in range(len(csv_data)):
    for j in range(len(csv_data[i])):
        n = csv_data[i][j] #이중 for문을 돌면서 값을 하나씩 꺼냄
        num_freq2[n-1] = num_freq2[n-1] + 1 # 그 값을 index로 활용하면서 같은 값이 나올때 마다 +1씩 카운트를 셈
print(num_freq2[:10])

for i, game in enumerate(csv_data):
    print('회차:{}, 평균 {}, 표준편차: {}'.format(i+1,mean(game),stdev(game)))
```
