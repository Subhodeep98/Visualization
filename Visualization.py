#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt #seaborn is based on graph 
sns.set(color_codes=True) #Adds nice background to graphs
get_ipython().run_line_magic('matplotlib', 'inline')
#tell Python to actually display the graphs


# In[23]:


auto=pd.read_csv('Automobile.csv')
auto.head() #Top 5


# In[24]:


auto.tail() #Last 5


# In[18]:


sns.displot(auto['highway_mpg'])


# In[22]:


sns.displot(auto['city_mpg'],kde=True,rug=True) #KDE= Kernel Density estimation(gives connection points)
                                                  #Rug= Line bars at the bottom of the graph showcasing the repeatation


# In[20]:


sns.jointplot(auto['engine_size'],auto['horsepower']) #Jointplot creates scatterplot pf 2 variables along with histogram 
                                                     # 1=X, 2=Y


# In[21]:


#Hex plot
sns.jointplot(auto['engine_size'],auto['horsepower'],kind='hex') #Kind- gives a particular shape 


# In[9]:


#2D Curve
sns.jointplot(auto['engine_size'],auto['horsepower'],kind="kde")


# In[10]:


#Pairwise plot. It creates a Matrix of axes and shows the relationship for each pair of column in data frame 
#It also draws histogram of each variable on the diagonal axis

sns.pairplot(auto[['normalized_losses','engine_size','horsepower']])


# In[11]:


#Plotting a Categorical data,adjust position using jitters

sns.stripplot(auto['fuel_type'],auto['horsepower'],jitter=False) #False- Gives a overview without getting into the details


# In[12]:


sns.stripplot(auto['fuel_type'],auto['horsepower'],jitter=True) #True-Gives an overall estimation and detail of the data.


# In[13]:


#Swarmplot
sns.swarmplot(auto['fuel_type'],auto['horsepower'])


# In[14]:


#Box Plot- this kind of box plot shows 3 quartiles values along with extreme values. It depicts- Outliers,Mean,

sns.boxplot(auto['number_of_doors'],auto['horsepower'])


# In[25]:


sns.boxplot(auto['number_of_doors'],auto['horsepower'],hue=auto['fuel_type'])


# In[26]:


sns.barplot(auto['body_style'],auto['horsepower'],hue=auto['fuel_type'])


# In[27]:


sns.barplot(auto['body_style'],auto['horsepower'])


# In[28]:


#Countplot
sns.countplot(auto['body_style'])


# In[ ]:




