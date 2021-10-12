from collections import defaultdict


def convert(matrix):
    AdL = defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                AdL[i].append(j)

    return AdL


AdM = [[1, 0, 0],[0, 1, 0],[0, 1, 1]]
print(convert(AdM))