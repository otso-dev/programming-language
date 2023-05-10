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

csv_data = []
with open('전국건강증진센터표준데이터.csv') as f:
    for line in f:
        csv_data.append(line.split(','))

len_list = []
for e in csv_data:
    len_list.append(len(e))
print(set(len_list))

doctor_index = csv_data[0].index('의사수')
print(doctor_index)

for i,e in enumerate(csv_data[0]):
    print(i,e)
    

doctor_count = []
for e in csv_data[1:]:
    doctor_count.append(e[doctor_index])
print(doctor_count)
print('centor_count: ', len(doctor_count))
print('centor with no doctor: ',doctor_count.count('0'))

for i,c in enumerate(doctor_count):
    try:
        doctor_count[i] = int(c)
    except:
        doctor_count[i] = 0
print('total doctor count: ',sum(doctor_count))

for i, c in enumerate(doctor_count):#index 값이 필요할 때 enumerate를 쓴다.
    print('index: ',i,'value',c)



