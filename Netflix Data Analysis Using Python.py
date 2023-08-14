#!/usr/bin/env python
# coding: utf-8

# # Netflix Data Analysis Using Python

# The Netflix data set has the information about the Tv shows & Movies available on Netflix till 2021.
# 
# The Data set available from Flexible which is a Third Party which engine , and available on Kaggle data set for free.

# ### Import library

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings



# ### Uploading Csv File 

# In[3]:


df = pd.read_csv(r"E:\NETFLIX MOVIES AND TV SHOWS CLUSTERING.csv")


# ### Data Processing

# In[4]:


df.head()


# In[6]:


df.tail()


# ### Show total no. of row and column

# In[7]:


df.shape


# ### Show the no of each columns

# In[9]:


df.columns


# ### Data type of each column

# In[10]:


df.dtypes


# ### Show unique value in each columns

# In[12]:


df['country'].unique()


# ### Show total no. of unique value from whole DataFrame

# In[13]:


df.nunique()


# #### Show the count, mean , median, Quartile etc..

# In[17]:


df.describe(include='all')


# ### Show all the unique values with their count

# In[18]:


df['country'].value_counts()


# ### show how many null values

# In[20]:


df.isnull().sum()


# ### Show the DataType of each columns

# In[21]:


df.info()


# ### Is there any Null Value present in any column ? Show with Heatmap

# In[23]:


sns.heatmap(df.isnull())


# ### For "ZoZo" : what is the show case Id and who is the director of the show ?

# In[24]:


df.head()


# In[29]:


df[df['title'].str.contains("Zozo")]


# ### In which year highest no. of Tv Shows and Movies were released ?

# In[30]:


df.head()


# In[31]:


df.dtypes


# ### First convert the data type of column Release_Date ? Using to_datetime

# In[41]:


df['N_Date'] = pd.to_datetime(df['date_added'])


# In[42]:


df


# In[43]:


df['N_Date'].dt.year.value_counts()


# ##### BarGraph

# In[44]:


df['N_Date'].dt.year.value_counts().plot(kind = 'bar')


# #### How many Movies & Tv shows are in the dataset ? Show with bar Graph

# In[50]:


df.groupby('type').type.count()


# In[51]:


df.groupby('type').type.count().plot(kind='bar')


# ### Show all the movies that were Released in 2010 ?

# In[52]:


df.head()


# In[53]:


df['year'] = df['N_Date'].dt.year


# In[56]:


df[(df['type'] == 'Movie') & (df['year'] == 2010)]


# #### Show only Titles of ALL Tv shows that were released in Pakistan only ?

# In[59]:


df[(df['type'] == 'TV Show') & (df['country'] == 'Pakistan')]


# ### Show top 10 Director , Who gave the Highest Number of Tv Shows & Movies to Netflix ?

# In[60]:


df['director'].value_counts().head(10)


# ### Show all the records were "type" is "Movie" and listed_in is "Horror Movies" or 'country' is 'United Kingdom'. 

# In[61]:


df[(df['type'] == 'Movie') & (df['listed_in'] == "Horror Movies")]


# ### What are the different rating defined by the Netflix ?

# In[62]:


df.head(2)


# In[63]:


df.rating.unique()


# ### What  is the maximum duration of Netflix on Tv Show ?

# In[64]:


df.head(1)


# In[65]:


df['duration'].unique()


# The duration column has 2 type values one is int and other is object . seprate both the values using "str.split" function
# 
# 

# In[66]:


df[['minutes' , 'Unit']] = df['duration'].str.split(" " , expand = True)


# In[67]:


df.head(1)


# In[69]:


df.minutes.max()


# ### How we can sort the dataset by year

# In[70]:


df.sort_values(by='year').head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




