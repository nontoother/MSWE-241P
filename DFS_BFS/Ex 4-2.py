#!/usr/bin/env python
# coding: utf-8

# In[29]:


class Graph:
        def __init__(self,Nodes):
            self.nodes = Nodes
            self.adj_list = {}
            
            for node in self.nodes:
                self.adj_list[node] = []
                
        def print_adj_list(self):
                for node in self.nodes:
                        print(node, "->", self.adj_list[node])
                        
        def add_edge(self, u, v):
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
       
        def DFS(self, startnode):
            processed = {} # means has been poppped out of stack at least once
          
            dfs_traversal_nodes =[]
            #create stack for DFS
            stack = []
            for node in self.adj_list.keys():
                processed[node] = False
            
            #push the current node
            stack.append(startnode)
            while len(stack) != 0:
                currentnode = stack.pop()
                if not processed[currentnode]: # skip all operations if node is already processed by some other route before
                    processed[currentnode] = True
                
                    self.process(currentnode)
                    dfs_traversal_nodes.append(currentnode)

                    neighbors = list(self.adj_list[currentnode]) # copy list into another list without changing the existing list
                    neighbors.sort(reverse = True)

                    #print('currentnode = ', currentnode)
                    #print('adj_list is ', self.adj_list[currentnode])
                    #print('neighbors = ', neighbors)
                    for nextnode in neighbors:
                        if (processed[nextnode]==False):
                            stack.append(nextnode)
            return dfs_traversal_nodes
        
        def process(self, node):
            pass
            #print(node)


# In[31]:


nodes = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]
all_edges = {
    ("A","B"),("B","C"),("C","D"),("D","H"),("C","G"),("B","F"),("A","E"),("E","F"),("F","G"),("G","H"),("H","L"),("G","K"),("F","J"),("E","I"),("I","J"),("J","K"),("K","L"),("L","P"),("K","O"),("J","N"),("I","M"),("M","N"),("N","O"),("O","P")
}
graph = Graph(nodes)
#graph.print_adj_list()

for u,v in all_edges:
    graph.add_edge(u,v)
graph.print_adj_list()
dfs_order = graph.DFS('A')
print('dfs order = ',dfs_order)


# In[ ]:




