#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mlxtend


# In[2]:


from mlxtend.frequent_patterns import apriori 


# In[11]:


dataset = [['Drink', 'Nuts', 'Diaper'],

      ['Drink', 'Coffee', 'Diaper'],

      ['Drink', 'Diaper', 'Eggs'],

      ['Nuts', 'Eggs', 'Milk'],

      ['Nuts', 'Coffee', 'Diaper', 'Eggs', 'Milk'],
       ['Tea','Apples','Juice']]


# In[12]:


dataset


# In[13]:


import pandas as pd

from mlxtend.preprocessing import TransactionEncoder



TranEncod = TransactionEncoder()

te_ary = TranEncod.fit(dataset).transform(dataset)

df = pd.DataFrame(te_ary, columns=TranEncod.columns_)


# In[14]:


df


# In[16]:


apriori(df, min_support=0.4,use_colnames=True)


# In[17]:


frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)

frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))

frequent_itemsets


# In[18]:


frequent_itemsets[ (frequent_itemsets['length'] == 2) &

          (frequent_itemsets['support'] >= 0.35) ]


# In[19]:


frequent_itemsets[ frequent_itemsets['itemsets'] == {'Diaper', 'Drink'} ]


# In[20]:


dataset1 = [[11,12,15],
            [12,14],
            [12,13],
            [11,12,14],
            [11,13],
            [12,13],
            [11,13],
            [11,12,13,15],
            [11,12,13]]


# In[21]:


dataset1


# In[22]:


TranEncod = TransactionEncoder()

te_ary1 = TranEncod.fit(dataset1).transform(dataset1)

df1 = pd.DataFrame(te_ary1, columns=TranEncod.columns_)


# In[23]:


df1


# In[24]:


apriori(df1, min_support=0.2,use_colnames=True)


# In[ ]:




