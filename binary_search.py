#requst: list is sorted
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
