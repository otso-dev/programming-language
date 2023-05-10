#!/usr/bin/env python
# coding: utf-8

# In[48]:


import pickle
csv_data = []
line_no = 0
with open('국적별_외국인_현황_20230207163531.csv') as f:
    for line in f:
        line_no = line_no + 1
        if line_no == 2:
            continue
        t = line[:-1].split(',')
        del t[1]
        csv_data.append(t)

for e in csv_data:
    e[0] = e[0].strip('"')
for e in csv_data[1:]:
    for i , value in enumerate(e[1:]):
        e[i+1] = int(value)
print(csv_data[:3])

with open('2020_10-2022_11.pickle','wb') as f:
    pickle.dump(csv_data,f)


# In[54]:


#print(csv_data[:10])

def get_numbers(data_list,year,month):
    for e in data_list:
        if '{}.{}'.format(year,month) in e:
            return e
    return None

count_list = get_numbers(csv_data,2022,11)
count_list = count_list[1:]
country_list = csv_data[0][1:]
print(count_list,len(count_list))
print(country_list)

percent_list = []
for n in count_list:
    percent_list.append((n*100)/sum(count_list))

count_dict = dict(sorted(zip(country_list, count_list),key = lambda x : x[1], reverse = True))
percent_dict = dict(sorted(zip(country_list,percent_list),key = lambda x : x[1],reverse = True ))
print(count_dict)
print(percent_dict)


# In[106]:


total_count = [0] * len(country_list)
for e in csv_data[1:]:
    for i , n in enumerate(e[1:]):
        total_count[i] = total_count[i] + n

for i ,total in enumerate(total_count):
    total_count[i] = total_count[i]/len(csv_data[1:])
print(total_count)

count_dict = dict(sorted(zip(country_list, total_count),key = lambda x : x[1], reverse = True))
#percent_dict = dict(sorted(zip(country_list,percent_list),key = lambda x : x[1],reverse = True ))
print(count_dict)
#print(percent_dict)


# In[108]:


s = 'mystring\n'
print(s[:-1])


# In[ ]:


list_t = [0] * 2
print(list_t)


# In[111]:


print(csv_data[0][1:])

