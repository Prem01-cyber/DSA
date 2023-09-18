import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    string_len = len(s)
    num_a = s.count('a')
    num_a *= n // string_len
    remainder = n % string_len
    num_a += s[:remainder].count('a')
    return num_a


if __name__ == '__main__':

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)