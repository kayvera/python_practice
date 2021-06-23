# must be sorted

import math


def binarySearch(array, value):
    start = 0
    end = len(array) - 1
    middle = math.floor((start+end)/2)
    while not(array[middle] == value):
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start + end) / 2)
        print(start, middle, end)
    if array[middle] == value:
        return middle
    else:
        return -1


custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]
binarySearch(custArray, 15)
