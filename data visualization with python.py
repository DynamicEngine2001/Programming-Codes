#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd


# In[7]:


from matplotlib import pyplot as plt


# In[7]:


x = [1,4,8]
y = [2,4,9]
z = [2,4,0]
plt.plot(x,y)
plt.plot(y,z)
plt.title("Test plot")
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend(["This is y", "This is z"])
plt.show()


# In[9]:


sample_data = pd.read_csv('sample_data.csv')


# In[10]:


sample_data


# In[11]:


type(sample_data)


# In[13]:


sample_data.column_c


# In[14]:


#retrieving specific  value
sample_data.column_c.iloc[2]


# In[21]:


plt.plot(sample_data.column_a,sample_data.column_c)
plt.plot(sample_data.column_a,sample_data.column_b)
plt.show()


# In[22]:


plt.plot(sample_data.column_a,sample_data.column_c,'o')
plt.plot(sample_data.column_a,sample_data.column_b,'o')
plt.show()


# In[32]:


data=pd.read_csv('countries.csv')


# In[33]:


data


# In[36]:


#compare the population growth in USA and China


# In[39]:


US = data[data.country == 'United States']


# In[40]:


US


# In[41]:


china = data[data.country == 'China']


# In[49]:


china


# In[51]:


plt.plot(US.year, US.population / 10**6)
plt.plot(china.year, china.population / 10**6)
plt.legend(['United States','China'])
plt.xlabel('year')
plt.ylabel('population')
plt.show()


# In[53]:


US.population


# In[55]:


US.population/US.population.iloc[0] * 100


# In[57]:


#Showing population growth
plt.plot(US.year, US.population/US.population.iloc[0] * 100)
plt.plot(china.year, china.population/china.population.iloc[0] * 100)
plt.legend(['United States','China'])
plt.xlabel('year')
plt.ylabel('population growth(first year=100')
plt.show()


# In[ ]:




