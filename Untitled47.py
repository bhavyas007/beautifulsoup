#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[18]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi")


# In[19]:


page


# In[20]:


soup=BeautifulSoup(page.text,"html.parser")


# In[21]:


soup


# In[22]:


team= soup.select("span.table-body__logo-text")


# In[23]:


team


# In[24]:


import pandas as pd


# In[25]:


df=pd.DataFrame(team)


# In[26]:


df


# In[27]:


rating=soup.select("td.table-body__cell u-text-right rating")


# In[28]:


rating


# In[33]:


batsman= soup.select("td.table-body__cell name")


# In[34]:


batsman

