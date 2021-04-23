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


df_ny = df[df['state'] == 'Michigan']


# In[6]:


#df_ny['year'], df_ny['month'], df_ny['day'] = zip(*df_ny['date'].map(lambda x: (x.strftime('%Y'), x.strftime('%B'), x.strftime('%d'))))
df_ny['year-month'], df_ny['day'] = zip(*df_ny['date'].map(lambda x: (x.strftime('%Y-%B'), x.strftime('%d'))))


# In[7]:


df_ny.head()


# In[8]:


df_ny_counties = df_ny.groupby(['county', 'year-month']).agg({'cases':np.max})


# In[9]:


df_ny_counties = df_ny.groupby(['county', 'year-month']).agg({'cases':np.max, 'deaths': np.max})


# In[10]:


df_ny_counties.head()


# In[11]:


df_ny_sum = df_ny_counties.groupby('year-month').agg({'cases':np.sum})


# In[12]:


df_ny_sum = df_ny_counties.groupby('year-month').agg({'cases':np.sum, 'deaths':np.sum})


# In[13]:


df_ny_sum.head()


# In[14]:


pd.to_datetime(df_ny_sum.index)


# In[15]:


df_ny_sum.index = pd.to_datetime(df_ny_sum.index)


# In[16]:


df_ny_sum.sort_index(inplace=True)


# In[17]:


df_ny_sum.index = df_ny_sum.index.strftime('%Y-%B')


# In[18]:


df_ny_sum


# In[19]:


#df_ny_sum[df_ny_sum.index == pd.to_datetime(df_ny_sum.index).sort_values()]


# In[20]:


df_ny_sum.head()


# In[21]:


#df_ny_sum.index = pd.to_datetime(df_ny_sum.index).sort_values()


# In[26]:


plt.figure(figsize=(8,6))
plt.plot(df_ny_sum.index, df_ny_sum['cases'], label='Cases')
plt.plot(df_ny_sum.index, df_ny_sum['deaths'], label='Deaths')
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.25)
plt.legend(loc='best')


# In[23]:


plt.figure(figsize=(10,8))
plt.plot(df_ny.groupby('county').agg({'cases':np.sum}).index, df_ny.groupby('county').agg({'cases':np.sum})['cases'])
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.25)


# In[24]:


df_ny.groupby('county').agg({'cases':np.sum})


# In[ ]:




