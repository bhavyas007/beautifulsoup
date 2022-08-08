#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[15]:


page=requests.get("https://www.sciencedirect.com/journal/artificial-intelligence")


# In[16]:


page


# In[23]:


soup=BeautifulSoup(page.content,'html.parser')


# In[24]:


soup


# In[29]:


# paper title
title= []
for i in soup.find_all('p',class_="sc-orwwe2-5 jUaFts"):
    title.append(i.text)

title


# In[27]:


# authors
authors= soup.select("div.editor-info-container")


# In[28]:


authors

