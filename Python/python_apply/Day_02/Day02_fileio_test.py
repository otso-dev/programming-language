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
data_list = []
with open('전국건강증진센터표준데이터.csv',encoding = 'cp949') as f:
    for line in f:
        data_list.append(line.split(','))
data_list = data_list[1:]
#print(data_list)
adrress =[]
for i in data_list:
    adrress.append(i[2]) 

do_list = []
#print(adrress.index(''))
del adrress[132]
for i in adrress:
    do = i
    do = do.split()
    do_list.append(do[0])

do_set = set(do_list)

do_key =[]
do_value =[]
for i in do_set:
    do_key.append(i)
    do_value.append(do_list.count(i))
    
du_di = dict(zip(do_key,do_value))

du_sort = dict(sorted(du_di.items(), key = lambda x: x[1], reverse = True))
print(du_sort)
# -


