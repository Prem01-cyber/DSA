# If a recursive function calls itself once we call it linear recursion
# These recursive calls are called as activations
# The activation of a recursive function is a stack frame
# The stack frame is a frame in the call stack

def linear_sum(sequence, n):
    """Return the sum of the first n numbers of sequence"""
    if n == 0:
        return 0
    else:
        return linear_sum(sequence, n - 1) + sequence[n - 1]
    

def reverse(sequence, start, stop):
    """Reverse elements in implicit slice sequence[start:stop]"""
    if start < stop - 1:
        sequence[start], sequence[stop - 1] = sequence[stop - 1], sequence[start]
        reverse(sequence, start + 1, stop - 1)

def power(base, index):
    """Return the value of base**index"""
    if index == 0:
        return 1
    else:
        return base * power(base, index - 1)

