#!/usr/bin/env python
# coding: utf-8

# In[137]:


#reference: https://www.geeksforgeeks.org/python-program-for-quicksort/
#python prog for quickSort
# mylist->list to be sorted, low->starting index, high-> ending index
from random import randint
def partition_random(mylist, low, high):
    i = (low - 1) # first high element
    #pivot = mylist[high] # always choosing the last index as pivot a design choice
    pivotindex = randint(low,high)
    pivot = mylist[pivotindex]
    
    #print(pivot)
    for j in range (low, high+1):
            if mylist[j] < pivot: #curr element smaller then the pivot
                    i += 1  #increment index of smaller element
                    mylist[i], mylist[j] = mylist[j], mylist[i] 
                    if i == pivotindex: # if first high was pivot and it got swapped
                        pivotindex = j # new location for pivot
    #print('first high = ', i)
    #print('trying to exchange index ', i+1, 'and index ', pivotindex)
    mylist[i+1], mylist[pivotindex] = mylist[pivotindex], mylist[i+1] # swap pivot with first high element at the last to put pivot in the right place
    return (i+1)
    
def partition(mylist, low, high):
    i = (low - 1) 
    pivot = mylist[high] # always choosing the last index as pivot a design choice
    for j in range (low, high):
            if mylist[j] < pivot: #curr element smaller then the pivot
                    i += 1  #increment index of smaller element
                    mylist[i], mylist[j] = mylist[j], mylist[i] 
                    
    mylist[i+1], mylist[high] = mylist[high], mylist[i+1]
    return (i+1)
    
# fun to implement quicksort, pi is partioning index
def quickSort(mylist, low, high):
    if low < high:
    
        pi = partition(mylist, low, high)
   #sorting left and right of the partion
        quickSort(mylist, low, pi-1) 
        quickSort(mylist, pi+1, high) 


# In[138]:


mylist = [1,3,10,11,7,9,1,2,3,-1,0,13,2]
n = len(mylist)
quickSort(mylist, 0, n-1)
print(mylist)


# In[139]:


from tokenize import generate_tokens
import re
import sys
import time

sys.setrecursionlimit(10**6)
sorttimes = [0]*10
for repeat in range(10):
    mylist = []

    file = open ('pride-and-prejudice.txt','r')
    line = file.readline()
    while (line!=''):
        array = re.findall('[a-zA-Z0-9]+', line) # regular expression matching
        length = len(array)
        for i in range(length):
            mylist.append(array[i]) #add word to list
        line = file.readline()
    print(len(mylist))
    n = len(mylist)
    t1 = time.time_ns()
    quickSort(mylist, 0, n-1)
    t2 = time.time_ns()
    sorttimes[repeat] = t2-t1
    print(repeat)


# In[140]:


print(mylist[0:100])


# In[141]:


import statistics
print(statistics.mean(sorttimes))
print(statistics.stdev(sorttimes))


# In[59]:


sorttimes


# In[81]:


from random import randint
testing = [0]*1000
for i in range(1000):
    testing[i] = randint(0,10)


# In[82]:





# In[ ]:




