import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap = 0
    i = 0
    while i < len(arr):
        if arr[i] != i+1:
            temp = arr[i]
            arr[i], arr[temp-1] = arr[temp-1], arr[i]
            swap += 1
        else:
            i += 1
    return swap

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)