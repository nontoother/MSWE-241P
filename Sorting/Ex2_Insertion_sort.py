import re
import time
import statistics


def insertionsort(nums):
    for i in range(len(nums)):
        idx = i - 1
        cur = nums[i]
        while idx >= 0 and nums[idx] > cur:
            nums[idx+1] = nums[idx]
            idx -= 1
        nums[idx+1] = cur
    return nums


sort_time = [0]*5
for repeat in range(5):
    L = []
    file = open('pride-and-prejudice.txt', 'r')
    lines = file.readlines()
    for line in lines:
        array = re.findall("[0-9a-zA-Z]+", line)
        length = len(array)
        for i in range(length):
            L.append(array[i])

    print(len(L))
    t1 = time.time_ns()
    insertionsort(L)
    t2 = time.time_ns()
    sort_time[repeat] = t2 - t1
    print(repeat)


print(sort_time)
print(statistics.mean(sort_time))
print(statistics.stdev(sort_time))