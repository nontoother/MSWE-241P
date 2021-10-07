#!/usr/bin/env python
# coding: utf-8
# Exercise 1
# Implement set as Hash table


class HashTable(object):

    def __init__(self):
        self.maxLength = 30000
        self.length = 0
        self.table = [None] * self.maxLength

    def length(self):
        return self.length

    # reference: http://cseweb.ucsd.edu/~kube/cls/100/Lectures/lec16/lec16-15.html
    def hashing(self, key):
        keystr = str(key)  # make sure key is converted to string, even if integers
        keylen = len(keystr)
        x = 31
        hashval = 0
        for i in range(keylen):
            hashval = x * hashval + ord(keystr[i])  # Honer's rule to compute the polynomial

        return hashval % self.maxLength

    def insert(self, key):
        hashval = self.hashing(key)
        initial_pos = hashval
        cur_pos = hashval
        while (True):
            if self.table[cur_pos]:  # something exists at this location
                if self.table[cur_pos] == key:  # duplicate
                    return False
                else:
                    cur_pos += 1  # linear probing
            else:
                self.table[cur_pos] = key  # add key when nothing found at cur_pos
                self.length += 1
                return True

            if cur_pos == initial_pos:  # if one cycle done, then break
                print('hashtable is full. increase space')
                return False

    def contains(self, key):
        hashval = self.hashing(key)
        initial_pos = hashval
        cur_pos = hashval
        while (True):
            if self.table[cur_pos]:  # something exists at this location
                if self.table[cur_pos] == key:  # found key/value
                    return True
                else:
                    cur_pos += 1  # keep linear probing
            else:
                return False  # nothing found at this location. key absent

            if cur_pos == initial_pos:  # if one cycle done, then break
                print('hashtable is full. increase space')
                return False

    def printHashTable(self):
        for i in range(self.maxLength):
            if self.table[i]:
                print(self.table[i], end=" ")

    def mySet(self, key, value):
        self.length += 1
        self.key = self.key(key)

    def get(self, key):
        index = self.findNumber(key)
        return self.table[index][1]

    def delNumber__(self, key):
        index = self.findNumber(key)
        self.table[index] = None

    def incr_key(self, key):
        return (key + 1) % self.max_length


class mySet:
    def __init__(self):
        self.sizeOfset = 0
        self.dataset = HashTable()

    def add(self, value):
        self.dataset.insert(value)
        self.sizeOfset = self.dataset.length

    def contains(self, value):
        return self.dataset.contains(value)

    def size(self):
        return self.dataset.length

    def printSet(self):
        self.dataset.printHashTable()


S = mySet()
print(S.dataset)


import re
import time

addtime = [[] for i in range(100)]  # array of 10x7105
sizeovertime = [[] for i in range(100)]
searchtime = [[] for i in range(100)]
N = 5
for repeat in range(N):

    S = mySet()
    file = open('pride-and-prejudice.txt', 'r')
    line = file.readline()
    while line:
        # array = line.split()
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
    # S.printSet()

    file1 = open('words-shuffled.txt', 'r')
    line = file1.readline()

    Count = 0

    notfoundset = mySet()
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
S.sizeOfset


import statistics

meanaddtimes = [0] * len(addtime[0])
stdaddtimes = [0] * len(addtime[0])

for w in range(len(addtime[0])):
    times = [addtime[i][w] for i in range(N)]
    meanaddtimes[w] = statistics.mean(times)
    stdaddtimes[w] = statistics.stdev(times)


meansearchtimes = [0] * len(searchtime[0])
stdsearchtimes = [0] * len(searchtime[0])

for w in range(len(searchtime[0])):
    times = [searchtime[i][w] for i in range(N)]
    meansearchtimes[w] = statistics.mean(times)
    stdsearchtimes[w] = statistics.stdev(times)
globalmeansearchtime = statistics.mean(meansearchtimes)
bestmeansearchtime = min(meansearchtimes)
worstmeansearchtime = max(meansearchtimes)
print('average search time = ', globalmeansearchtime)
print('best search time = ', min(meansearchtimes), 'for index ', meansearchtimes.index(bestmeansearchtime))
print('worse search time =', worstmeansearchtime, 'for index ', meansearchtimes.index(worstmeansearchtime))