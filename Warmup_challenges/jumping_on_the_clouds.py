#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.

import math
import os
import random
import re
import sys

# thunderclouds 1 must be avoided
# can jump 1 or 2 clouds 
# return the minimum number of jumps required to win the game
def jumpingOnClouds(c):
    # Write your code here
    jumps = 0
    i = 0

    while i < len(c) -1:
        if i+2 < len(c) and c[i+2] == 0:
            i += 2
            jumps += 1
        elif i+1 < len(c) and c[i+1] == 0:
            i += 1
            jumps += 1
        else:
            continue
    return jumps

if __name__ == '__main__':
    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)