#!/usr/bin/env python
# coding: utf-8

# In[18]:


#python program to implement insertion sort
def insertionSort(L):
    for index in range(1,len(L)):

        current = L[index]
        position = index

        while position>0 and L[position-1]>current:
            L[position]=L[position-1]
            position = position-1

        L[position]=current

L = [2,8,3,5,6,1,2,5]
insertionSort(L)
print(L)



# In[19]:


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
    S = insertionSort(L)
    t2 = time.time_ns()
    sorttimes[repeat] = t2-t1
    print(repeat)


# In[12]:





# In[20]:


print(L [0:1000])


# In[21]:


import statistics
print(statistics.mean(sorttimes[0:6]))
print(statistics.stdev(sorttimes[0:6]))


# In[24]:


sorttimes[0:6]


# In[ ]:




