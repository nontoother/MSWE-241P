#!/usr/bin/env python
# coding: utf-8

# In[2]:


#python graph to converst adjacency matrix to adj list
from collections import defaultdict 

def convert(a):
    Adlist = defaultdict(list)
    for i in range(len(a)):
        for j in range (len(a[i])):
                        if a[i][j] == 1:
                            Adlist[i].append(j)
    return Adlist

#print adj list

    for i in Adlist:
        print(i, end = " ")
        for j in Adlist[i]:
            print("-> {}", format(j), end = " ")


# In[5]:


a = [[1, 0, 0],[0, 1, 0],[0, 1, 1]]
Adlist = convert(a)


# In[6]:


print(Adlist)


# In[11]:


Adlist[0]


# In[ ]:




