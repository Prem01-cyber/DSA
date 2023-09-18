# Binary Search is used for sorting
# It is a divide and conquer algorithm
# It is a recursive algorithm

# Linear Search
# General idea:
# 1. Start at the beginning of the list
# 2. Compare the target value to each element in the list
# 3. If the target value is found, stop
# 4. If the target value is not found, move to the next element in the list
# 5. If the target value is not found and there are no more elements in the list, stop

# Worst case: O(n)
# Best case: O(1)

# Bad on large lists
# Complexity: O(n)
# Doesn't matter if the list is sorted or not

def linear_search(sequence, value):
    for index, item in enumerate(sequence):
        if item == value:
            return index
    return None
    

# Binary Search
# General idea:
# 1. Check the middle element
# 2. If the middle element is the target, stop
# 3. If the target is less than the middle element, recursively search the left half
# 4. If the target is greater than the middle element, recursively search the right half

# Worst case: O(log n)
# Best case: O(1)

# Complexity: O(log n)
# Requires the list to be sorted
# Works efficiently on large lists

def binary_search(sequence, value):
    low = 0
    high = len(sequence) - 1
    while low <= high:
        mid = (low + high) // 2
        if sequence[mid] == value:
            return mid
        elif sequence[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return None