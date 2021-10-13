from collections import defaultdict
from queue import Queue


class Graph:
    def __init__(self):
        # self.node = nodes
        self.Adl = defaultdict(list)

    def add(self, p1, p2):
        self.Adl[p1].append(p2)
        self.Adl[p2].append(p1)

    def print(self):
        for i in sorted(self.Adl):
            print(i, "->", self.Adl[i])

    def DFS(self, StartNode):
        stack = []
        stack.append(StartNode)
        visited = set()
        res = []
        while stack:
            cur = stack.pop()
            if cur not in visited:
                res.append(cur)
            visited.add(cur)

            neighbors = sorted(self.Adl[cur], reverse=True)
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)

        return res

    def BFS(self, StartNode):
        queue = Queue()
        queue.put(StartNode)
        visited = set()
        res = []
        while not queue.empty():
            cur = queue.get()
            if cur not in visited:
                res.append(cur)
            visited.add(cur)

            neighbors = sorted(self.Adl[cur])
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.put(neighbor)

        return res