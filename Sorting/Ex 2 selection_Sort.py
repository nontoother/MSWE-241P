#!/usr/bin/env python
# coding: utf-8

# In[23]:


def selection_sort(L):
    indexing_length = range(0, len(L)-1)
    
    for i in indexing_length:
        min_value = i
    
        for j in range (i+1, len(L)):
            if L[j] < L [min_value]:
                min_value = j
        if min_value != i:
            L[min_value], L[i] = L[i], L[min_value]
    return L


# In[24]:


from tokenize import generate_tokens
import re
import time
sorttimes = [0]*10
for repeat in range(10):
    L = []

    file = open ('pride-and-prejudice.txt','r')
    line = file.readline()
    while (line!=''):
        array = re.findall('[a-zA-Z0-9]+', line) # regular expression matching
        length = len(array)
        for i in range(length):
            L.append(array[i]) #add word to list
        line = file.readline()
    print(len(L))

    t1 = time.time_ns()
    selection_sort(L)
    t2 = time.time_ns()
    sorttimes[repeat] = t2-t1
    print(repeat)


# In[22]:


L = [3,8,4,1,5,2]
selection_sort(L)
print(L)
selection_sort(L)


# In[13]:


print(repeat)


# In[14]:


print(L [0:1000])


# In[26]:


import statistics
print(statistics.mean(sorttimes[0:6]))
print(statistics.stdev(sorttimes[0:6]))


# In[25]:


sorttimes[0:6]


# In[ ]:




