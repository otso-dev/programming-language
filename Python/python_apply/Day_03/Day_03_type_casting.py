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

# +
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
    
