#!/usr/bin/env python
# coding: utf-8

# In[7]:


from math import ceil, floor
#Python prog to implement mergesort
#define fnc mergersort
def mergeSort(mylist):
    if len(mylist) > 1:
        mid = floor(len(mylist)/2)   #middle of the list
        LH = mylist[:mid]   #left half
        RH = mylist[mid:]  #right half
        mergeSort(LH)
        mergeSort(RH)
        
        i = 0
        j = 0
        k = 0
         
        #reference https://www.geeksforgeeks.org/merge-sort/ 

        while i < len(LH) and j < len(RH):
            if LH[i] < RH[j]: 
                mylist[k] = LH[i] 
                i+= 1
            else: 
                mylist[k] = RH[j] 
                j+= 1
                
            k+= 1
         #loop to check if element is left               
                
        while i < len(LH): 
            mylist[k] = LH[i] 
            i+= 1
            k+= 1

        while j < len(RH): 
            mylist[k] = RH[j] 
            j+= 1
            k+= 1
        return mylist
            
#mylist = [8,4,1,2,9,5,3]
#print(mylist)


# In[8]:


from tokenize import generate_tokens
import re
import time
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
    t1 = time.time_ns()
    mergeSort(mylist)
    t2 = time.time_ns()
    sorttimes[repeat] = t2-t1
    print(repeat)


# In[3]:



   


# In[4]:


print(mylist[0:1000])


# In[10]:


import statistics
print(statistics.mean(sorttimes))
print(statistics.stdev(sorttimes))


# In[ ]:




