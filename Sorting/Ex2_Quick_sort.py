import re
import time
import sys
import statistics


def quicksort(nums, left, right):
    if left < right:
        idx = partition(nums, left, right)
        quicksort(nums, left, idx-1)
        quicksort(nums, idx+1, right)
    return nums


def partition(nums, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if nums[i] < nums[pivot]:
            nums[i], nums[index] = nums[index], nums[i]
            index += 1
        i += 1
    nums[pivot], nums[index-1] = nums[index-1], nums[pivot]
    return index - 1


sys.setrecursionlimit(10**6)
sort_time = [0]*10
for repeat in range(10):
    L = []
    file = open('pride-and-prejudice.txt', 'r')
    lines = file.readlines()
    for line in lines:
        array = re.findall("[0-9a-zA-Z]+", line)
        length = len(array)
        for i in range(length):
            L.append(array[i])
        # line = file.readline()

    print(len(L))
    t1 = time.time_ns()
    quicksort(L, 0, len(L)-1)
    t2 = time.time_ns()
    sort_time[repeat] = t2 - t1
    print(repeat)


print(sort_time)
print(statistics.mean(sort_time))
print(statistics.stdev(sort_time))