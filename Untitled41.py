#!/usr/bin/env python
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup
import requests


# In[5]:


page= requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")


# In[6]:


page


# In[7]:


soup= BeautifulSoup(page.text,"html.parser")


# In[8]:


soup


# In[9]:


top_team=soup.select("span.u-hide-phablet")


# In[10]:


top_team


# In[22]:


import pandas as pd


# In[23]:


df=pd.DataFrame(top_team)


# In[24]:


df


# In[18]:


rating=soup.select("td.table-body__cell u-text-right rating")


# In[19]:


rating


# In[13]:


import pandas as pd


# In[14]:


ds=pd.DataFrame(rating)


# In[15]:


ds

