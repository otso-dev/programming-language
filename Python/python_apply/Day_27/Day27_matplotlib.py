#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fig,axe = plt.subplots()
#axe.plot(np.linspace(-1,1,10),np.sin(np.linspace(-1,1,10)))
axe.plot(np.sin(np.linspace(-10,10,1000)))

ax1 = fig.add_axes([0.2,0.5,0.2,0.3])
ax1.plot([1,2,3,4,5])


# In[26]:


flg1 = plt.figure()
flg1.add_subplot(1,3,1)
flg1.add_subplot(2,3,5)
flg1.add_subplot(3,3,9)


# In[29]:


flg1 = plt.figure(layout='tight')
flg1.add_subplot(3,2,1)
flg1.add_subplot(3,2,2)
flg1.add_subplot(3,1,2)
flg1.add_subplot(3,1,3)

