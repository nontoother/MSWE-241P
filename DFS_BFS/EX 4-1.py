#!/usr/bin/env python
# coding: utf-8

# In[39]:


adj_list = {
    "A":["B", "E"],
    "B":["A", "F", "C"],
    "C":["B", "G", "D"],
    "D":["C", "H"],
    "E":["A", "F", "I"],
    "F":["B", "E", "J", "G"],
    "G":["C", "F", "K", "H"],
    "H":["D", "G", "L"],
    "I":["E", "J", "M"],
    "J":["F", "I", "N", "K"], 
    "K":["G", "J", "O", "L"],
    "L":["H", "K", "P"], 
    "M":["I", "J", "N"],
    "N":["M", "J", "O"], 
    "O":["N", "K", "P"],
    "P":["O", "K", "L"]
}
adj_list


# In[65]:


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
            
        def BFS(self, startnode):
            #BFS implementation
            from queue import Queue
            visited = {}
            level = {} #distance dict
            parent = {}
            bfs_traversal_nodes =[]
            queue = Queue()

            for node in adj_list.keys():
                visited[node] = False
                parent[node] = None
                level[node] = -1 #initialization 
            queue.put(startnode)
            while (not queue.empty()):
                currentnode = queue.get()
                self.process(currentnode)
                visited[currentnode] = True
                bfs_traversal_nodes.append(currentnode)
                
                if parent[currentnode]:
                    level[currentnode]  = level[parent[currentnode]] + 1
                else:
                    level[currentnode] = 0
                neighbors = list(self.adj_list[currentnode]) # copy list into another list without changing the existing list
                neighbors.sort()
                print('currentnode = ', currentnode)
                print('adj_list is ', self.adj_list[currentnode])
                print('neighbors = ', neighbors)
                for nextnode in neighbors:
                    if (visited[nextnode]==False):
                        visited[nextnode] = True
                        queue.put(nextnode)
                        parent[nextnode] = currentnode
            return (bfs_traversal_nodes, level, parent)
        
        def process(self, node):
            print(node)


# In[66]:


nodes = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]
all_edges = {
    ("A","B"),("B","C"),("C","D"),("D","H"),("C","G"),("B","F"),("A","E"),("E","F"),("F","G"),("G","H"),("H","L"),("G","K"),("F","J"),("E","I"),("I","J"),("J","K"),("K","L"),("L","P"),("K","O"),("J","N"),("I","M"),("M","N"),("N","O"),("O","P")
}
graph = Graph(nodes)
#graph.print_adj_list()

for u,v in all_edges:
    graph.add_edge(u,v)
graph.print_adj_list()
bfs_order, level, parent = graph.BFS('A')
print(bfs_order)


# In[67]:


print(level)


# In[ ]:




