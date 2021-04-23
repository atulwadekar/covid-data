#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[3]:


df = pd.read_csv('us-counties.csv')


# In[4]:


df.head()


# In[5]:


df.shape


# In[6]:


df.date.min()


# In[7]:


df_by_state = df.groupby('state').agg({'cases':np.sum})


# In[8]:


df_by_state.shape


# In[9]:


df_by_state.head()


# In[10]:


plt.figure(figsize=(10,8))
plt.bar(df_by_state.index, df_by_state['cases'])
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.25)


# In[ ]:




