from Set_Implementation.set_class import LinkedlistSet
import re
import time
import matplotlib.pyplot as plt


addtime = []
sizeovertime = []
searchtime = []

S = LinkedlistSet()
file = open('pride-and-prejudice.txt', 'r')
lines = file.readlines()
for line in lines:
    array = re.findall('[a-zA-Z0-9]+', line)
    length = len(array)
    for i in range(length):
        start = time.time_ns()
        S.add(array[i])
        t1 = time.time_ns()
        addtime.append(t1 - start)
        sizeovertime.append(S.size())

file.close()
print(S.size())

file1 = open('words-shuffled.txt', 'r')
lines = file1.readlines()

Count = 0

notfoundset = LinkedlistSet()
for line in lines:
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
    # line = file1.readline()
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
