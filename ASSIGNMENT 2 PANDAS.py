#!/usr/bin/env python
# coding: utf-8
# Import the necessary libraries

# In[1]:


import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep='|')


# In[2]:


# Assign it to a variable called users and use the 'user_id' as index


# In[3]:


users=df
users.set_index('user_id', inplace=True)


# In[4]:


users


# In[5]:


#See the first 10 and last 10 entries


# In[6]:


first_10=users.head(10)
last_10=users.tail(10)
total_entries=pd.concat([first_10,last_10])
total_entries


# In[7]:


#What is the number of observations in the dataset?


# In[8]:


print(f'No. of observation: {len(users)}')


# In[9]:


#What is the number of columns in the dataset?


# In[10]:


print(f'No. of Columns:{len(users.columns)} ')


# In[11]:


#Print the name of all the columns.


# In[12]:


users.columns


# In[13]:


#How is the dataset indexed?


# In[14]:


users.index


# In[15]:


#What is the data type of each column?


# In[16]:


users.info()


# In[17]:


#Print only the occupation column


# In[18]:


users['occupation']


# In[19]:


#How many different occupations are in this dataset?


# In[20]:


users['occupation'].nunique()


# In[21]:


#What is the most frequent occupation?


# In[22]:


users['occupation'].mode()


# In[23]:


#DataFrame Info.


# In[24]:


users.info()


# In[25]:


#Describe all the columns


# In[26]:


users.describe(include='all')


# In[27]:


#Summarize only the occupation column


# In[28]:


users['occupation'].value_counts()


# In[29]:


#What is the mean age of users?


# In[30]:


users['age'].mean()


# In[31]:


#What is the age with least occurrence?


# In[32]:


users['age'].min()

