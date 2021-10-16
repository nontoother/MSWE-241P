import re
import time
import statistics


def selectionsort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[i]:
                min_index = j
        if i != min_index:
            nums[i], nums[min_index] = nums[min_index], nums[i]
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
    selectionsort(L)
    t2 = time.time_ns()
    sort_time[repeat] = t2 - t1
    print(repeat)


print(sort_time)
print(statistics.mean(sort_time))
print(statistics.stdev(sort_time))