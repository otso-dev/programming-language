## file 입출력 연습

```python
csv_data = []
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

def road_avg(target_list):
    for i,n in enumerate(target_list):
        if n >100:
            target_list[i] = n/100
    print(sum(target_list)/ len(target_list))

with open('전국보행자전용도로표준데이터.csv') as f:
    for line in f:
        csv_data.append(my_split(line))
print(csv_data[:5])
index = csv_data[0].index('보행자전용도로폭')
doro_list =[]
for i in csv_data[1:]:
    doro_list.append(i[index])

for i,n in enumerate(doro_list):
    doro_list[i] = float(n)
road_avg(doro_list)

```
