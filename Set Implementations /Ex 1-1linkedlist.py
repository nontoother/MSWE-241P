# Exercise 1
# Implement set as linkedlist
# Node Class


class Node():
    # Function to initialise the node
    def __init__(self, value):
        self.value = value
        self.next = None


class mySet():
    def __init__(self):
        self.head = None
        self.sizeOfSet = 0

    # adds value to linkedlist if value not already in linkedlist
    # returns 1 if value added, or returns 0 if value already present
    def add(self, value):
        curr = self.head

        # base case if self.head == 0
        if curr == None:
            newNode = Node(value)
            self.head = newNode
            self.sizeOfSet = self.sizeOfSet + 1
            return True

        reachedEndOfList = False
        while (curr.value != value):
            temp = curr.next
            if temp == None:  # reached end of linkedlist
                reachedEndOfList = True
                break
            else:
                curr = temp  # go forward

        if reachedEndOfList:  # value not found. insert value here
            newNode = Node(value)
            curr.next = newNode
            self.sizeOfSet = self.sizeOfSet + 1
            return True
        else:  # found existing element with value in linkedlist
            return False

    def contains(self, value):
        curr = self.head

        # base case if self.head == 0
        if curr == None:
            return False

        reachedEndOfList = False
        while (curr.value != value):
            temp = curr.next
            if temp == None:  # reached end of linkedlist
                reachedEndOfList = True
                break
            else:
                curr = temp  # go forward

        if reachedEndOfList:  # value not found. insert value here
            return False
        else:  # found existing element with value in linkedlist
            return True

    # funion of sets
    def find_union(lst1, lst2):
        result_lst = list(set(lst1) | set(lst2))
        return result_lst

    def printSet(self):
        curhead = self.head
        print(end='\n')

        while (curhead):
            print(curhead.value, end=' ')
            curhead = curhead.next
        print('\n')

    def size(self):
        return self.sizeOfSet

import re
import time

addtime = [[] for i in range(100)]  # array of 10x7105
sizeovertime = [[] for i in range(100)]
searchtime = [[] for i in range(100)]

for repeat in range(100):
    S = mySet()
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
    file1.close()


notfoundset.printSet()
print(Count)
print(S.size())


import statistics

meanaddtimes = [0] * len(addtime[0])
stdaddtimes = [0] * len(addtime[0])

for w in range(len(addtime[0])):
    times = [addtime[i][w] for i in range(100)]
    meanaddtimes[w] = statistics.mean(times)
    stdaddtimes[w] = statistics.stdev(times)

import time

start = time.time()
print('A')
print(time.time() - start)
import timeit

g = timeit.timeit('print(\'A\')', number=1)
print('g = ', g * 1e9)


import re

string = "Hi! can I get a 7up, please? I need 2: great, thanks! John's not in today."
splitsent = re.findall('[a-zA-z0-9]+', string)
print(splitsent)


meansearchtimes = [0] * len(searchtime[0])
stdsearchtimes = [0] * len(searchtime[0])

for w in range(len(searchtime[0])):
    times = [searchtime[i][w] for i in range(100)]
    meansearchtimes[w] = statistics.mean(times)
    stdsearchtimes[w] = statistics.stdev(times)
globalmeansearchtime = statistics.mean(meansearchtimes)
bestmeansearchtime = min(meansearchtimes)
worstmeansearchtime = max(meansearchtimes)
print('average search time = ', globalmeansearchtime)
print('best search time = ', min(meansearchtimes), 'for index ', meansearchtimes.index(bestmeansearchtime))
print('worse search time =', worstmeansearchtime, 'for index ', meansearchtimes.index(worstmeansearchtime))