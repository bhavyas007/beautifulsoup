#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Write a python program to display all the header tags from wikipedia.org.
from bs4 import BeautifulSoup
import requests
import re


# In[2]:


page=requests.get("https://en.wikipedia.org/wiki/Main_Page")


# In[3]:


page


# In[4]:


soup=BeautifulSoup(page.content)
soup


# In[5]:


bs=BeautifulSoup(page.text,'html.parser')


# In[6]:


titles= bs.find_all(['h1','h2','h3','h4','h5','h6'])


# In[7]:


print("Displaying all header tags: ",*titles, sep="\n\n")


# In[8]:


#Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
page= requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")


# In[9]:


page


# In[10]:


soup=BeautifulSoup(page.text,"html.parser")


# In[11]:


soup


# In[12]:


top_movies=soup.select('td.titleColumn')


# In[13]:


top_movies


# In[31]:


ratings = [b.attrs.get('data-value')
        for b in soup.select('td.posterColumn span[name=ir]')]


# In[32]:


ratings


# In[33]:


list=[]


# In[34]:


for index in range(0, len(top_movies)):
    movie_string = top_movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    data = {"movie_title": movie_title,
            "rating": ratings[index],
            "year": year
            }
    list.append(data)


# In[35]:


for movie in list:
    print(movie['movie_title'], '('+movie['year'] +')', movie['rating'])


# In[36]:


import pandas as pd


# In[37]:


df=pd.DataFrame(list)


# In[38]:


df


# In[39]:


df.iloc[0:100,0:3]


# In[40]:


# top 100 Indian movies
page=requests.get("https://www.imdb.com/list/ls056092300/")


# In[41]:


page


# In[42]:


soup=BeautifulSoup(page.text,'html.parser')


# In[43]:


soup


# In[44]:


top_movies=soup.select("h3.lister-item-header")


# In[45]:


top_movies


# In[85]:


df1=pd.DataFrame(top_movies)


# In[86]:


df1


# In[87]:


df1.iloc[:,3]


# In[67]:


rating=soup.select('span.ipl-rating-star small')


# In[68]:


rating


# In[61]:


df=pd.DataFrame(rating)


# In[62]:


df


# In[74]:


page1= requests.get("https://presidentofindia.nic.in/former-presidents.htm")


# In[75]:


page1


# In[76]:


soup=BeautifulSoup(page1.content)


# In[77]:


soup


# In[78]:


bs=BeautifulSoup(page1.text,'html.parser')


# In[79]:


bs


# In[80]:


president=bs.select("div.presidentListing")


# In[81]:


president


# In[82]:


term = soup.select("p")


# In[83]:


term


# In[90]:


df=pd.DataFrame(president)


# In[91]:


df


# In[92]:


df1=pd.DataFrame(term)


# In[93]:


df1

