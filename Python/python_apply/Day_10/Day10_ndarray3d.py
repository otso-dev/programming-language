#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
a1 = np.arange(30).reshape(3,5,2)
print(a1,a1.shape)
a2=np.sum(a1,axis = 0)
print(a2,a2.shape)


# In[5]:


a3 = np.sum(a1,axis = 2)
print(a3, a3.shape)


# In[6]:


a4 = np.sum(a1, axis = 1)
print(a4,a4.shape)


# In[19]:


from matplotlib import image
image = image.imread('cat.jpg')
print(image.shape)


# In[29]:


import matplotlib.pyplot as plt
_, axe = plt.subplots()
axe.imshow(image)


# In[22]:


image2 = np.moveaxis(image,[2],[0]) # 축을 움직임
print(image2.shape)

