import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    if n == 0 or n == 1:
        return 0
    else:
        if ar[0] in ar[1:]:
            index = ar.index(ar[0], 1)
            ar.pop(index)
            ar.pop(0)
            return 1 + sockMerchant(n-2, ar)
        else:
            ar.pop(0)
            return sockMerchant(n-1, ar)

if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)