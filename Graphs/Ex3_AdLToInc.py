class edges:
    def __init__(self, n):
        self.matrix = [[0 for _ in range(2)] for _ in range(n)]

    def add(self, edgename, p1, p2):
        self.matrix[edgename][0] = p1
        self.matrix[edgename][1] = p2

    def contain(self, p1, p2):
        if [p1, p2] in self.matrix or [p2, p1] in self.matrix:
            return True
        else:
            return False

    def print(self):
        print(self.matrix)


def convert(adl, nedge):
    myedge = edges(nedge)
    n = 0
    for i in adl:
        for j in adList[i]:
            if n <= nedge and not myedge.contain(i, j):
                myedge.add(n, i, j)
                n += 1

    myedge.print()
    vertice = len(adl)
    Incmat = [[0] * n for i in range(vertice)]
    for edgename, point in enumerate(myedge.matrix):
        v = int(point[0])
        c = int(point[1])
        Incmat[v][edgename] = 1  # first vertex
        Incmat[c][edgename] = 1  # second vertex
    return Incmat


adList = {0: [1, 2], 2: {0, 1, 3}, 1: [2, 3, 4, 0], 4: [1, 3], 3: [1, 2, 4]}
nedge = 0
for i in adList:
    for j in adList[i]:
        nedge += 1

nedge /= 2
print(convert(adList, int(nedge)))