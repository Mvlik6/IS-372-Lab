#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[2]:


x = np.linspace(0, 10, 100)
fig = plt.figure()
plt.plot(x, np.sin(x),'-')
plt.plot(x, np.cos(x), '--')


# In[6]:


from sklearn import datasets
iris= datasets.load_iris()
df= pd.read_csv(iris.filename)
df.head(5)
#df.tail(5)


# In[7]:


df.describe()


# ## Excercise 1.1

# In[10]:


dfs=pd.read_csv('C:\\Users\\Mvlik\\anaconda3\\lib\\site-packages\\sklearn\\datasets\\data\\iris.csv'
           , delimiter = ',', header =0, 
           names=['sepal length (cm)', 'sepal width (cm)','petal length (cm)'
             , 'petal width (cm)', 'Variety'] )
                           
dfs.head()


# ## Excersice 1.2

# In[19]:


print(dfs.info())


# ## Excersice 2.2

# In[12]:


print(dfs.shape)
print(dfs["Variety"].value_counts())
dfs["Variety"].hist()


# In[13]:


for ojha, feature in enumerate(list(dfs.columns)[:-1]):
    fg = sns.FacetGrid(dfs, hue='Variety', height=5)
    fg.map(sns.distplot, feature).add_legend()
    plt.show


# ## 3.1.2 Box Plots

# In[24]:


sns.boxplot(x='Variety', y='petal length (cm)', data=dfs)
plt.show()


# In[5]:


sns.violinplot(x='Variety',y='petal length (cm)', data=dfs)
plt.show()


# In[6]:


dfs.plot(kind='scatter',x='sepal length (cm)',y='sepal width (cm)',c='g')
plt.show()


# In[18]:


sns.set_style("whitegrid");
sns.FacetGrid(dfs, hue="Variety", height=10)     .map(plt.scatter, "petal length (cm)", "sepal length (cm)")     .add_legend();
plt.show();


# In[17]:


sns.set_style("whitegrid");
sns.pairplot(dfs,vars = iris.feature_names,hue='Variety', diag_kind = 'kde',
            plot_kws = {'alpha': 0.6, 's': 80,'edgecolor': 'k'},size=2)
plt.show()


# In[ ]:




