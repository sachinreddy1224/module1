#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
cric_data=np.loadtxt("cric.tsv",skiprows=1)
cric_data


# In[5]:


np.mean(cric_data)


# In[11]:


Sachin = cric_data[:,1]
Dravid = cric_data[:,2]
India = cric_data[:,3]


# In[13]:


def stats(x):
    a = np.mean(x)
    print("mean is:",a)
    b = np.median(x)
    print("median is:",b)


# In[14]:


stats(Sachin)


# In[16]:


stats(Dravid)


# In[17]:


stats(India)

