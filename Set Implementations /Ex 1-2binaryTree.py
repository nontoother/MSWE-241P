#!/usr/bin/env python
# coding: utf-8
# Exercise 1
# Implement set as Binary tree


class Node:
    def __init__(self, value):
        self.leftchild = None
        self.rightchild = None
        self.value = value

    def children(self):
        children = []
        if (self.leftchild):
            children = self.leftchild
        if (self.rightchild):
            if not children:
                children = self.rightchild
            else:
                children[1] = self.rightchild
        return children


class Tree:

    def __init__(self):
        self.root = None
        self.sizeOfTree = 0

    def add(self, cNode, value):
        if cNode is None:
            self.root = Node(value)
            self.sizeOfTree += 1
        elif (value < cNode.value):
            if cNode.leftchild:
                self.add(cNode.leftchild, value)
            else:
                cNode.leftchild = Node(value)
                self.sizeOfTree += 1
                return True

        elif (value > cNode.value):
            if cNode.rightchild:
                self.add(cNode.rightchild, value)
            else:
                cNode.rightchild = Node(value)
                self.sizeOfTree += 1
                return True
        else:
            return False

    def contains(self, cNode, value):
        if cNode is None:
            return False
        elif (value < cNode.value):
            if (cNode.leftchild):
                return self.contains(cNode.leftchild, value)
            else:
                return False
        elif (value > cNode.value):
            if cNode.rightchild:
                return self.contains(cNode.rightchild, value)
            else:
                return False
        else:
            return True

    def printTree(self, cNode):
        if cNode is None:
            return
        else:
            print(cNode.value, end=' ')
            self.printTree(cNode.leftchild)
            self.printTree(cNode.rightchild)


class mySet:
    def __init__(self):
        self.sizeOfset = 0
        self.dataset = Tree()

    def add(self, value):
        self.dataset.add(self.dataset.root, value)
        self.sizeOfset = self.dataset.sizeOfTree

    def contains(self, value):
        return self.dataset.contains(self.dataset.root, value)

    def size(self):
        return self.sizeOfset

    def printSet(self):
        self.dataset.printTree(self.dataset.root)


S = mySet()
print(S.dataset)

import re
import time
TEST_NUMBER = 2
addtime = [[] for i in range(TEST_NUMBER)]  # array of 10x7105
sizeovertime = [[] for i in range(TEST_NUMBER)]
searchtime = [[] for i in range(TEST_NUMBER)]

for repeat in range(TEST_NUMBER):

    S = mySet()
    file = open('pride-and-prejudice.txt', 'r')
    line = file.readline()
    while line != '':
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

    notfoundset = mySet()
    while (line != ''):
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


import statistics

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
print('average search time = ', globalmeansearchtime)
print('best search time = ', min(meansearchtimes), 'for index ', meansearchtimes.index(bestmeansearchtime))
print('worse search time =', worstmeansearchtime, 'for index ', meansearchtimes.index(worstmeansearchtime))