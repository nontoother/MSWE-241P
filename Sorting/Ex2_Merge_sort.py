import re
import time
import statistics


def mergesort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left, right = nums[:mid], nums[mid:]
    res = []
    left = mergesort(left)
    right = mergesort(right)
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    while left:
        res.append(left.pop(0))
    while right:
        res.append(right.pop(0))

    return res


sort_time = [0]*10
for repeat in range(10):
    L = []
    file = open('pride-and-prejudice.txt', 'r')
    line = file.readline()
    while line:
        array = re.findall("[0-9a-zA-Z]+", line)
        length = len(array)
        for i in range(length):
            L.append(array[i])
        line = file.readline()

    print(len(L))
    t1 = time.time_ns()
    mergesort(L)
    t2 = time.time_ns()
    sort_time[repeat] = t2 - t1
    print(repeat)


print(sort_time)
print(statistics.mean(sort_time))
print(statistics.stdev(sort_time))