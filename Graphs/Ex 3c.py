#!/usr/bin/env python
# coding: utf-8

# In[9]:



from collections import defaultdict
def convertIncMatToAdjList(Imat):
    numvertices = len(Imat) 
    numedges = len(Imat[0])
    AdjList = defaultdict(list)
    for e in range(numedges):
        vertices = [v for v in range(numvertices) if Imat[v][e]==1] # create list of two vertices which connect with the edge
        print(vertices)
        AdjList[vertices[0]].append(vertices[1])
        AdjList[vertices[1]].append(vertices[0])
    return AdjList


# In[10]:


Imat = [[1, 1, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1]]


# In[11]:


AdjList = convertIncMatToAdjList(Imat)
print(AdjList)


# In[ ]:




