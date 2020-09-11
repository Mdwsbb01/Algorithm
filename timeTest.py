from timeConsuming import *

@timeConsuming
def linear_search(lst, val):
    for i, v in enumerate(lst):
        if v == val:
            return i
        else:
            return None

@timeConsuming
def binary_search(lst, val):
    left = 0
    right = len(lst) - 1
    while left <= right:                  #target value exist in the range
        mid = (left + right) // 2
        if lst[mid] == val:
            return mid
        elif lst[mid] > val:              #the value exists and in the left side
            right = mid - 1
        else:                             #value in the right side
            left = mid + 1
    else:
        return None

lst = list(range(1000000))
linear_search(lst, 983344)
binary_search(lst, 983344)