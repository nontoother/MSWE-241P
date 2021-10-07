#!/usr/bin/env python
# coding: utf-8

# In[72]:


run TreeSet


# In[92]:


# convert adjacency list into incidence matrix
# input adjacency list
def convertAdListToIncMat(adList):
    edges = mySet()
    for v in adList: #adList is a dictionary with vertice numbers as keys
        conn_vert = adList[v] #connected vertices
        for c in conn_vert:
            if v<c:
                edgename = str(v)+str(c)
            elif c<v:
                edgename = str(c) + str(v)
            else:
                print('self loop found. Not supported')
                return None
            edges.add(edgename)
    numedges = edges.size()
    numvertices = len(adList)
    AllEdgeNames = edges.returnSet()
    
    IncMat = [[0]*numedges for i in range(numvertices)]
    for j,edgename in enumerate(AllEdgeNames):
        v = int(edgename[0])
        c = int(edgename[1])
        IncMat[v][j] = 1 #first vertex
        IncMat[c][j] = 1 #second vertex
    return IncMat


# In[96]:


adList = {0:[1,5], 1:[0,2], 2:[1,3], 3:[2,4], 4:[3,5], 5:[4, 0]}
Imat = convertAdListToIncMat(adList)
print(adList)


# In[102]:


adList = {0:[1,2], 2:{0,1,3}, 1:[2,3,4,0], 4:[1,3], 3:[1,2,4]}
Imat = convertAdListToIncMat(adList)
print(adList)


# In[103]:


for i in range(len(Imat)):
    print(Imat[i])


# In[135]:


print(Imat)


# In[122]:


AdjList = {0: [1,2], 1: [0, 2, 3, 4], 2: [1, 0, 3], 3: [1, 2, 4], 4: [1, 3]}


# In[136]:


NewAdList = {0: [1, 2], 1: [0, 2, 3, 4], 2: [0, 1, 3], 3: [2, 1, 4], 4: [1, 3]}


# In[137]:


print(NewAdList)


# In[ ]:




