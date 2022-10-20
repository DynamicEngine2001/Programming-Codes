#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('Ecommerce Purchases')
data


# In[3]:


data.head(10)


# In[4]:


data.tail(10)


# In[5]:


data.dtypes


# In[6]:


data.isnull()


# In[7]:


data.columns


# In[8]:


len(data.columns)


# In[9]:


len(data)


# In[10]:


data.info()


# In[11]:


data.columns


# In[13]:


data['Purchase Price'].max()


# In[14]:


data['Purchase Price'].min()


# In[16]:


# AVERAGE PURCHASE PRICE

data['Purchase Price'].mean()


# In[17]:


#HOW MANY PEOPLE HAS FRENCH AS THEIR LANGUAGE

data[data['Language']=='fr']


# In[18]:


len(data[data['Language']=='fr'])


# In[19]:


data[data['Language']=='fr'].count()


# In[24]:


#JOB TITLE CONTAINS ENGINEER 

data[data['Job'].str.contains('engineer', case = False)]




# In[25]:


len(data[data['Job'].str.contains('engineer', case = False)])


# In[26]:


# FIND EMAIL OF THE PERSON WITH THE FOLLOWING ADRESS 132.207.160.22

data.columns


# In[36]:


data[data['IP Address']=="132.207.160.22"]['Email']


# In[42]:


#How many people have mastercard as their credit card provider and made a purchase above 50

data[(data['CC Provider']=="Mastercard") & (data['Purchase Price']>50)]


# In[44]:


len(data[(data['CC Provider']=="Mastercard") & (data['Purchase Price']>50)])
data[(data['CC Provider']=="Mastercard") & (data['Purchase Price']>50)].count


# In[46]:


# FIND EMAIL OF THE PERSON WITH TH FOLL CREDIT NUMBER 4664825258997302

data.columns


# In[56]:


data[data['Credit Card']==4664825258997302]['Email']


# In[57]:


# HOW MANY PEOPLE pURCHASE DURING AM AND HOW MANY DURING PM

data.columns


# In[61]:


data['AM or PM'].value_counts()


# In[63]:


#HOW MANY PEOPLE HAVE A CREDIT CARD THAT WILL EXPIRE IN 2020

data['CC Exp Date']


# In[77]:


def fun():
    count = 0
    for date in data['CC Exp Date']:
        if date.split('/')[1] == '20':
            count = count + 1
    print(count)
        
    


# In[78]:


fun()


# In[83]:



len(data[data['CC Exp Date'].apply(lambda x: x[3:]=='20')])


# In[84]:


#TOP 5 MOST POPULAR EMAIL PROVIDER

list1 = []
for email in data['Email']:
    list1.append(email.split('@')[1])


# In[97]:


data['popular'] = list1


# In[102]:


data['popular'].value_counts().head(5)


# In[104]:


data['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)


# In[ ]:




