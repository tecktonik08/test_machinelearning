#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle


# In[5]:


favorite_load = pickle.load(open('./saves/favorite_save.pkl','rb'))
print(favorite_load)


# In[6]:


type(favorite_load)


# In[7]:


favorite_load['tiger']


# 

# In[9]:


autompg_lr = pickle.load(open('./saves/autompg_lr.pkl', 'rb'))
autompg_lr


# In[10]:


type(autompg_lr)


# In[12]:


autompg_lr.predict([[3504.0, 8]])


# In[ ]:




