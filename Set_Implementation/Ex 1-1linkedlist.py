# Exercise 1
# Implement set as linkedlist


from Set_Implementation.set_class import LinkedlistSet
import re
import time
import matplotlib.pyplot as plt


addtime = []
sizeovertime = []
searchtime = []

S = LinkedlistSet()
file = open('pride-and-prejudice.txt', 'r')
line = file.readline()
while line:
    array = re.findall('[a-zA-Z0-9]+', line)  # regular expression matching
    length = len(array)
    for i in range(length):
        start = time.time_ns()
        S.add(array[i])  # add word to set
        t1 = time.time_ns()
        addtime.append(t1 - start)
        sizeovertime.append(S.size())

    line = file.readline()

file.close()

file1 = open('words-shuffled.txt', 'r')
line = file1.readline()

Count = 0

notfoundset = LinkedlistSet()
while line:
    array = re.findall('[a-zA-Z0-9]+\'?[a-z]*', line)
    length = len(array)
    for i in range(length):
        start = time.time_ns()
        foundOutput = S.contains(array[i])
        t2 = time.time_ns()
        searchtime.append(t2 - start)
        if (foundOutput == False):
            Count += 1
            notfoundset.add(line)
    line = file1.readline()
print(Count)
file1.close()

notfoundset.printSet()

meansearchtime = float(sum(searchtime) / S.size())

plt.plot(sizeovertime, addtime)
plt.xlabel('number of words already inserted')
plt.ylabel('time in ns to insert a new word')
plt.show()

bestsearchtime = min(searchtime)
worstsearchtime = max(searchtime)
print('average search time = ', meansearchtime)
print('best search time = ', bestsearchtime, 'for index ', searchtime.index(bestsearchtime))
print('worst search time =', worstsearchtime, 'for index ', searchtime.index(worstsearchtime))
