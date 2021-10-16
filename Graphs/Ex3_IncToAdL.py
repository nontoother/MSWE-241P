from collections import defaultdict


def convert(Imat):
    AdL = defaultdict(list)
    nedges = len(Imat[0])
    nvertices = len(Imat)
    for e in range(nedges):
        vertices = [v for v in range(nvertices) if Imat[v][e] == 1]
        print(vertices)
        AdL[vertices[0]].append(vertices[1])
        AdL[vertices[1]].append(vertices[0])

    return AdL


Imat = [[1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 1]]

print(convert(IMAT))