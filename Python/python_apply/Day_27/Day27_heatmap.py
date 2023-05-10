#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
glue = sns.load_dataset("glue").pivot("Model","Task","Score")
sns.heatmap(glue)


# In[3]:


df = sns.load_dataset("glue")
print(df)

