#!/usr/bin/env python
# coding: utf-8

# In[117]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[118]:


pip install seaborn


# In[119]:


import seaborn as sns


# In[120]:


data = pd.read_csv('adult.csv')


# In[121]:


data


# In[122]:


data.head(10)


# In[123]:


data.tail()


# In[124]:


# FIND SHAPE OF DATASET

data.shape


# In[125]:


# GETTING INFO ABOUT DATASET

print('Number of rows: ', data.shape[0])
print('Number of columns: ', data.shape[1])


# In[126]:


data.info()


# In[127]:


# fetch ramdom samples from dataset(50%)
   
data1 = data.sample(frac=0.50, random_state = 111)
data1


# In[128]:


# check null values in dataset

data.isnull().sum(axis=1)


# In[129]:


sns.heatmap(data.isnull())


# In[130]:


# PERFORM DATA CLEANING [REPLACE ? WITH NAN]

data.tail()


# In[131]:


data.isin(['?']).sum()


# In[132]:


data.columns


# In[ ]:





# In[133]:


data['workclass'] = data['workclass'].replace('?',np.nan)
data['occupation'] = data['occupation'].replace('?',np.nan)
data['native-country'] = data['native-country'].replace('?',np.nan)


# In[134]:


data.isnull().sum()


# In[135]:


data.isin(['?']).sum()


# In[136]:


sns.heatmap(data.isnull())


# In[137]:


# drop all the missing values

per_missing = data.isnull().sum()*100/len(data)


# In[138]:


per_missing


# In[139]:


data.dropna(how='any',inplace=True)
data.shape


# In[140]:


48842 - 45222


# In[141]:


#check for duplicate data and drop them

dup = data.duplicated().any()


# In[142]:


print("Are there any duplicated values in the data ", dup)


# In[143]:


data = data.drop_duplicates()


# In[144]:


data.shape


# In[145]:


45222 - 45175


# In[146]:


# GET OVERALL STATISTICS ABOUT THE  DATAFRAME

data.describe(include = 'all')


# In[147]:


data.columns


# In[148]:


data['education'].unique()


# In[149]:


data['educational-num'].unique()


# In[150]:


# DROP THE COLUMNS EDUCATIONAL NUM, CAPITAL LOSS AND CAPITAL GAIN

data = data.drop(['educational-num','capital-gain', 'capital-loss' ],axis=1)


# In[151]:


data.columns


# In[152]:


#UNIVARIATE ANALYSIS
## WHAT IS THE DISTRIBUTION OF AGE COLUMN
 
data['age'].describe()    


# In[153]:


data['age'].hist()


# In[154]:


# FIND TOTAL NUMBER OF PERSONS HAVING AGE BETWEEN 17 TO 48(INCLUSIVE )USING BETWEEN METHOD

sum((data['age']>=17) & (data['age']<=48))


# In[155]:


sum(data['age'].between(17,48))


# In[156]:


#WHAT IS THE DISTRIBUTION OF WORKCLASS COLUMN

data.columns


# In[157]:


data['workclass'].describe()


# In[158]:


plt.figure(figsize=(10,10))
data['workclass'].hist()


# In[ ]:





# In[159]:


# HOW MANY PERSON HAVING BACHELORS OR MASTERS DEGREE

data.columns


# In[160]:


filter1 = data['education']=='Bachelors'
filter2 = data['education']=='Masters'


# In[161]:


len(data[filter1 | filter2])


# In[162]:


sum(data['education'].isin(['Bachelors','Masters']))


# In[164]:


data.columns


# In[169]:


# BIVERATE ANALYSIS

sns.boxplot(x ='income',y ='age', data = data)


# In[170]:


#REPLACE SALARY VALUES(<=50k & >50k) as 0 and 1

data['income'].unique()


# In[172]:


data['income'].value_counts()


# In[174]:


def salary_data(sal):
    if sal=='<=50k':
        return 0
    else:
        return 1


# In[175]:


data['Encoded salary'] = data['income'].apply(salary_data)


# In[176]:


data.head()


# In[ ]:




