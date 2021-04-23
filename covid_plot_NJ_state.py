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


df['date'] = pd.to_datetime(df['date'])


# In[5]:


df_nj = df[df['state'] == 'New Jersey']


# In[6]:


df_nj.head()


# In[7]:


#df_nj['year'], df_nj['month'], df_nj['day'] = zip(*df_nj['date'].map(lambda x: (x.strftime('%Y'), x.strftime('%B'), x.strftime('%d'))))
df_nj['year-month'], df_nj['day'] = zip(*df_nj['date'].map(lambda x: (x.strftime('%Y-%B'), x.strftime('%d'))))


# In[8]:


df_nj.head()


# In[9]:


df_nj_counties = df_nj.groupby(['county', 'year-month']).agg({'cases':np.max})


# In[10]:


df_nj_counties = df_nj.groupby(['county', 'year-month']).agg({'cases':np.max, 'deaths': np.max})


# In[11]:


df_nj_counties.head()


# In[12]:


df_nj_sum = df_nj_counties.groupby('year-month').agg({'cases':np.sum})


# In[13]:


df_nj_sum = df_nj_counties.groupby('year-month').agg({'cases':np.sum, 'deaths':np.sum})


# In[14]:


df_nj_sum.head()


# In[15]:


pd.to_datetime(df_nj_sum.index)


# In[16]:


df_nj_sum.index = pd.to_datetime(df_nj_sum.index)


# In[17]:


df_nj_sum.sort_index(inplace=True)


# In[18]:


df_nj_sum.index = df_nj_sum.index.strftime('%Y-%B')


# In[19]:


df_nj_sum


# In[20]:


#df_nj_sum[df_nj_sum.index == pd.to_datetime(df_nj_sum.index).sort_values()]


# In[21]:


df_nj_sum.head()


# In[22]:


#df_nj_sum.index = pd.to_datetime(df_nj_sum.index).sort_values()


# In[23]:


plt.figure(figsize=(8,6))
plt.plot(df_nj_sum.index, df_nj_sum['cases'], label='Cases')
plt.plot(df_nj_sum.index, df_nj_sum['deaths'], label='Deaths')
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.25)
plt.legend(loc='best')


# In[24]:


plt.figure(figsize=(10,8))
plt.plot(df_nj.groupby('county').agg({'cases':np.sum}).index, df_nj.groupby('county').agg({'cases':np.sum})['cases'])
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.25)


# In[25]:


df_nj.groupby('county').agg({'cases':np.sum})


# In[ ]:




