#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
a = np.arange(15).reshape(3,5)
a


# In[ ]:


help(range)


# In[18]:


print (np.array([6, 4, 6, 0, 2]))


# In[21]:


print('Create a 2D array by passing a list of lists into array().')
A = np.array([[1, 2, 3],[4, 5, 6]])
print(A)

print('Access elements of the array with brackets')
print(A[0, 1],A[1, 2])

print('the elements of a 2D array are 1D arrays')
print(A[0])


# In[29]:


def dotArray(X,Y):
    Z=np.dot(X,Y)
    print(Z)

X = np.array([[3, -1, 4],[1, 5, -9]])

Y = np.array([[2, 4, -5 ,6],[-1, 7, 9, 3], [3, 2, -7, -2]])

dotArray(X,Y)


# In[30]:


print('Addition concatentates lists together ')
print([1, 2, 3] + [4, 5, 6])

print('Multiplication concatenates a list with itself a given number of times')
print([1, 2, 3] * 4)


# In[36]:


G = np.array([3, -4, 1])
H = np.array([5, 2, 3])

print(G+10)
print(H*4)
print(G+H)
print(G*H)


# In[40]:


print(A.ndim)
print(A.shape)
print(A.size)
print(A.dtype)


# In[50]:


x = np.arange(10)
print(x)

print(x[3])
print(x[:4])
print(x[4:])
print(x[4:8])


# In[52]:


x=np.array([[0,1,2,3,4],[5,6,7,8,9]])
print (x[1,2])

print(x[:,2:])


# In[56]:


x=np.arange(0,50,10)
index = np.array([3,1,4])
print(x[index])

mask = np.array([True,False,False,True,False])
print(x[mask])


# In[62]:


from sklearn import datasets

iris = datasets.load_iris()
print(iris.filename)


# In[68]:


iris_data = np.genfromtxt('C:\\Users\\Mvlik\\anaconda3\\lib\\site-packages\\sklearn\\datasets\\data\\iris.csv'
                         , delimiter =",", skip_header=1)
#print(iris_data)

print("mean of {} os {}".format(iris.feature_names[0], iris_data[:,0].mean()))


# In[72]:


iris_data[:,2].mean()


# In[73]:


iris_data[:,2].std()


# In[74]:


iris_data[:,2].min()


# In[75]:


iris_data[:,2].max()


# In[76]:


iris_data[:,2].var()


# In[ ]:




