#!/usr/bin/env python
# coding: utf-8

# ### 데이터산업의 기술등급별 데이터직무 인력현황
# * 데이터 직무별 axe 생성
#     - x축 : 시점
#     - y축 : 업종(2개)
#    
# * 하나의 figure에, 총 8개 axe가 바둑판 형식으로 배치되는 형태(4col X 2rows) figure사이즈는 각자 알아서
# * title 표시

# In[18]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.animation
from matplotlib import font_manager, rc



# In[ ]:


current_font_list = matplotlib.rcParams['font.family']

font_path = "C:/Windows/Fonts/H2GTRE.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()

matplotlib.rcParams['font.family'] = [font]+current_font_list

print(matplotlib.rcParams['font.family'])


# In[9]:


pd_raw = pd.read_csv('데이터산업의_기술등급별_데이터직무_인력_현황_20230303160442.csv',encoding='cp949')

col_select = ['데이터직무별(1)','시점','데이터 처리 및 관리 솔루션 개발·공급업','데이터 구축 및 컨설팅 서비스업']
pd_data = pd_raw[col_select]
pd_data.columns = ['데이터직무별','시점','데이터처리','데이터구축']


# In[12]:


fig,axe = plt.subplots(2,4,figsize=(25,10))
fig.suptitle('Data job manpower status',fontsize = 20)

for i in range(8):
    sub_data = pd_data.iloc[4*i:4*(i+1)]
    t = sub_data['데이터직무별']
    x = sub_data['시점']
    y_1 = sub_data['데이터처리']
    y_2 = sub_data['데이터구축']
    axe[i//4,i%4].set_title(t[i*4])
    axe[i//4,i%4].plot(x,y_1, 'go--',color = 'black',label = 'data processing',linestyle='-.',linewidth = 3)
    axe[i//4,i%4].plot(x,y_2,'ro--',color = 'red',label = 'data construction',linestyle='-.',linewidth = 3)
    axe[i//4,i%4].legend()
    axe[i//4,i%4].set_xticks(x)
    axe[i//4,i%4].set_xlabel('year')
    axe[i//4,i%4].set_ylabel('Number of people')
    axe[i//4,i%4].set_yticks(np.linspace(1000,23000,5))

fig.savefig('data.png')


# In[ ]:





# In[ ]:




