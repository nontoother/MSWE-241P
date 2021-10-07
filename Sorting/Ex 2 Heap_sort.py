#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Python prog to implement Heapsort
def heapify(arry, n, i): 
    largest = i # set largest as root
    lft = 2 * i + 1     # left = 2*i + 1 
    rgt = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists, greater than root
    if (lft < n and arry[i] < arry[lft]): 
        largest = lft 
  
    # See if right child of root, greater than root 
    if (rgt < n and arry[largest] < arry[rgt]): 
        largest = rgt 
  
    
    if (largest != i): 
        arry[i],arry[largest] = arry[largest],arry[i] # swap 
  
        # Heapify the root. 
        heapify(arry, n, largest) 

def heapSort(arry): 
    n = len(arry) 
  
    # Build a heap. 
    for i in range(n, -1, -1): 
        heapify(arry, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arry[i], arry[0] = arry[0], arry[i] # swap 
        heapify(arry, i, 0) 


# In[9]:


arry = [4, 10, 3, 5, 1]  
heapSort(arry)  
print (arry)


# In[10]:


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
    S = heapSort(L)
    t2 = time.time_ns()
    sorttimes[repeat] = t2-t1
    print(repeat)


# In[4]:


import time
sorttimes = [0]*10
for repeat in range(10):
    t1 = time.time_ns()
    S = heapSort(L)
    t2 = time.time_ns()
    sorttimes[repeat] = t2-t1
    print(repeat)


# In[11]:


print(L [0:1000])


# In[12]:


import statistics
print(statistics.mean(sorttimes))
print(statistics.stdev(sorttimes))


# In[ ]:




