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
csv_data = []
with open('전국건강증진센터표준데이터.csv', encoding = 'cp949') as f:
    for line in f:
        csv_data.append(line.split(','))
print(csv_data[0:3])


# -

name_list = []
for e in csv_data[1:]:
    if len(e[2])>0:
        name_list.append(e[2].split()[0])
        #print(e[2].split()[0])
   #print(e[2].split()[0])
   #print(e[2].split())
print(name_list)
    

for n in name_list:
    if n[0] == '"':
        print(n[1:])
    else:
        print(n)

for i, n in enumerate(name_list):
    name_list[i] = n.lstrip('"')
    #print(n.lstrip('"'))
print(name_list[:10])

#name_set = set(name_list)
for n in set(name_list):
    print(n,name_list.count(n))


# +
#lambda x : x[1]
def sort_key(x):
    return x[1]
#빈도수 dictionary 반환
def unique_count(raw_list,sort = False,sort_judgment = False):
    raw_key = []
    raw_value = []
    for i in set(raw_list):
        raw_key.append(i)
        raw_value.append(raw_list.count(i))
    raw_list = dict(zip(raw_key,raw_value))
    if sort == True:
        raw_list = dict(sorted(raw_list.items(),key = sort_key,reverse = sort_judgment))
    return raw_list
        
print(unique_count(name_list,True, True))
print(unique_count(name_list,True))
print(unique_count(name_list))
# -

help(sorted)
