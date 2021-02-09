#!/usr/bin/env python
# coding: utf-8

# In[6]:


def conform(fav):
    fav=42
    return(fav)
    


# In[9]:


if __name__== "__main__":
    print('Welcome!')
    fav=7
    ## fav = conform(fav)     will give original number -> 42
    print("My favorite # is", fav)


# In[10]:


student={'A':28,'B':25,'C':32,'D':25}
def test(student):
    new={'E':30,"F":28}
    student.update(new)
    print("inside the function",student)
    return
test(student)
print("outside the function",student)


# In[20]:


class student:
    def __init__(self, name):
        self.name=name
        self.course_list= []
    def add(self, new_course):
        self.course_list.append(new_course)
        
std=student("malik")
txt = input("type your name here")
std.add(txt)
print(std.course_list)


# In[22]:


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)        
        
class Professor(Person):
    def __init__(self, fname, lname):
        self.department= 'IS'
        Person.__init__(self, fname, lname)
mhd = Professor("Mh","AS")
mhd.printname()
print(mhd.department)


# In[ ]:




