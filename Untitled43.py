#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Write a python program to scrape the details of top publications from Google Scholar 
from bs4 import BeautifulSoup
import requests


# In[2]:


page= requests.get("https://scholar.google.com/citations?view_op=top_venues&hl=en")


# In[3]:


page


# In[5]:


soup=BeautifulSoup(page.text,'html.parser')


# In[6]:


soup


# In[7]:


rank=soup.select("td.gsc_mvt_p")


# In[8]:


rank


# In[10]:


import pandas as pd


# In[11]:


df=pd.DataFrame(rank)


# In[12]:


df


# In[15]:


# Publication
publication=soup.select('td.gsc_mvt_t')


# In[16]:


publication


# In[17]:


df1=pd.DataFrame(publication)


# In[18]:


df1


# In[22]:


# h5 Index
index=soup.select("td.gsc_mvt_n")


# In[23]:


index

