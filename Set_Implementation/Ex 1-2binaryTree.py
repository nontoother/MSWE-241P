#!/usr/bin/env python
# coding: utf-8
# Exercise 1
# Implement set as Binary tree
from Set_Implementation.set_class import TreeSet
import re
import time
import statistics

TEST_NUMBER = 2

addtime = [[] for _ in range(TEST_NUMBER)]
sizeovertime = [[] for _ in range(TEST_NUMBER)]
searchtime = [[] for _ in range(TEST_NUMBER)]

for repeat in range(TEST_NUMBER):

    S = TreeSet()
    file = open('pride-and-prejudice.txt', 'r')
    line = file.readline()
    while line:
        array = re.findall('[a-zA-Z0-9]+', line)  # regular expression matching
        length = len(array)
        for i in range(length):
            start = time.time_ns()
            S.add(array[i])  # add word to set
            t1 = time.time_ns()
            addtime[repeat].append(t1 - start)
            sizeovertime[repeat].append(S.size())

        line = file.readline()

    file.close()

    file1 = open('words-shuffled.txt', 'r')
    line = file1.readline()

    Count = 0

    notfoundset = TreeSet()
    while line:
        array = re.findall('[a-zA-Z0-9]+\'?[a-z]*', line)
        length = len(array)
        for i in range(length):
            start = time.time_ns()
            foundOutput = S.contains(array[i])
            t2 = time.time_ns()
            searchtime[repeat].append(t2 - start)
            if (foundOutput == False):
                Count += 1
                notfoundset.add(line)
        line = file1.readline()
    print(Count)


notfoundset.printSet()


meanaddtimes = [0] * len(addtime[0])
stdaddtimes = [0] * len(addtime[0])

for w in range(len(addtime[0])):
    times = [addtime[i][w] for i in range(TEST_NUMBER)]
    meanaddtimes[w] = statistics.mean(times)
    stdaddtimes[w] = statistics.stdev(times)


meansearchtimes = [0] * len(searchtime[0])
stdsearchtimes = [0] * len(searchtime[0])

for w in range(len(searchtime[0])):
    times = [searchtime[i][w] for i in range(TEST_NUMBER)]
    meansearchtimes[w] = statistics.mean(times)
    stdsearchtimes[w] = statistics.stdev(times)
globalmeansearchtime = statistics.mean(meansearchtimes)
bestmeansearchtime = min(meansearchtimes)
worstmeansearchtime = max(meansearchtimes)
print('average search time =', globalmeansearchtime)
print('best search time =', min(meansearchtimes), 'for index ', meansearchtimes.index(bestmeansearchtime))
print('worst search time =', worstmeansearchtime, 'for index ', meansearchtimes.index(worstmeansearchtime))