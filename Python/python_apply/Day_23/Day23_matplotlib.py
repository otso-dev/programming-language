#!/usr/bin/env python
# coding: utf-8

# In[38]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


# In[29]:


xs = np.linspace(0,50,100)
ys = np.sin(xs)
# print(xs)
# print(ys)

figure, axe = plt.subplots()
figure.set_facecolor('gray')
figure.suptitle('Figure1')
figure.supxlabel('Figure1_x')
figure.supylabel('Figure1_y')
figure.text(0.5,0.7,'test')
figure.set_size_inches(15,4.8)
axe.plot(xs,ys)
axe.set_title('my axe title')
axe.set_xlabel('axe_x')
axe.set_ylabel('axe_y')
axe.set_xlim(0,30)
axe.set_ylim(0,1)
axe.set_xticks(np.linspace(0,30,5))
axe.set_xticklabels(list('abcde'))


# In[37]:


fig,axes = plt.subplots(2,3,sharey=True,figsize=(15,7))
axes[0,0].plot(xs,ys)


# In[43]:


#fig1 = matplotlib.figure.Figure(figsize=[15,7])
fig1 = plt.figure(figsize = [15,7])

a = fig1.add_axes([0,0,1,1])
a.plot(xs,ys)

b = fig1.add_axes([0,0, 0.5,0.5])
b.plot(xs,ys)


# In[44]:


fig2 = plt.figure(figsize=(15,7))
a = fig2.add_subplot(2,1,1)
b = fig2.add_subplot(2,2,3)
c = fig2.add_subplot(2,2,4)


# In[56]:


fig3 = plt.figure(figsize=(15,7))
a = fig3.add_subplot(3,2,1)
b = fig3.add_subplot(3,2,2)
c = fig3.add_subplot(3,1,2)
d = fig3.add_subplot(3,2,5)
f = fig3.add_subplot(3,2,6)

fig3.savefig('fig.png')

