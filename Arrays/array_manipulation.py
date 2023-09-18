#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    arr = [0] * n
    for a,b,k in queries:
        arr[a-1:b] = [x+k for x in arr[a-1:b]]
    return max(arr)

def arrayManipulation(n, queries):
    arr = [0] * n+1
    for a,b,k in queries:
        arr[a-1] += k
        arr[b] -= k
    
    max_value = 0
    current_value = 0

    for i in range(n):
        current_value += arr[i]
        max_value = max(max_value, current_value)

    return max_value

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)