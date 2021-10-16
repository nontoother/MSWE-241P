import re
import time
import statistics


def heapify(nums, i):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    length = len(nums)
    if left < length and nums[left] > nums[largest]:
        largest = left
    if right < length and nums[right] > nums[largest]:
        largest = right

    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, largest)


def heapSort(nums):
    length = len(nums)
    for i in range(length//2, -1, -1):
        heapify(nums, i)

    return nums


sort_time = [0] * 10
for repeat in range(10):
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
    heapSort(L)
    t2 = time.time_ns()
    sort_time[repeat] = t2 - t1
    print(repeat)

print(sort_time)
print(statistics.mean(sort_time))
print(statistics.stdev(sort_time))