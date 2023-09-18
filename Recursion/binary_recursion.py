# When a function calls itself, it is called recursion.
# Binary recursion is when a function calls itself twice.

def binary_sum(sequence):
    """Return the sum of the sequence"""
    if len(sequence) == 1:
        return sequence[0]
    else:
        mid = len(sequence) // 2
        return binary_sum(sequence[:mid]) + binary_sum(sequence[mid:])
    

# Non recursive Implementation of binary search
def binary_search(sequence, target):
    """Return true if target is found in the sequence"""
    low = 0
    high = len(sequence) - 1
    while low <= high:
        mid = low+high//2
        if sequence[mid] == target:
            return True
        elif sequence[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Recursive Implementation of binary search
def binary_search(sequence, target, low, high):
    """Return true if target is found in the sequence"""
    if low > high:
        return False
    else:
        mid = low + high // 2
        if sequence[mid] == target:
            return True
        elif sequence[mid] < target:
            return binary_search(sequence, target, mid+1, high)
        else:
            return binary_search(sequence, target, low, mid-1)