def linear_search(lst, val):
    for i, v in enumerate(lst):
        if v == val:
            return i
        else:
            return None

#complex: O(n)