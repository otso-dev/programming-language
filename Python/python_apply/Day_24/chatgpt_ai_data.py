#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

# 데이터
year = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
dev = [14124, 15720, 16457, 18617, 20805, 25133, 30566]
consult = [55280, 55850, 58894, 61290, 65412, 76999, 86335]
sales = [64151, 65977, 68179, 75778, 82364, 97891, 114071]

# 시계열 그래프
plt.plot(year, dev, label='Data Development')
plt.plot(year, consult, label='Data Consulting')
plt.plot(year, sales, label='Data Sales')
plt.xlabel('Year')
plt.ylabel('Market Size')
plt.title('Data Industry Market Size')
plt.legend()
plt.show()

# 파이 차트
total_market = sum(dev) + sum(consult) + sum(sales)
market_share = [sum(dev)/total_market, sum(consult)/total_market, sum(sales)/total_market]
labels = ['Data Development', 'Data Consulting', 'Data Sales']
plt.pie(market_share, labels=labels, autopct='%1.1f%%')
plt.title('Data Industry Market Share')
plt.show()

