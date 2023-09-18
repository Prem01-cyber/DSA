#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s1,s2 = s.split(" ")    
    s1=s1[0].upper()+s1[1:]
    s2=s2[0].upper()+s2[1:]
    return s1+" "+s2

def solve2(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

if __name__ == '__main__':

    s = input()

    result = solve2(s)
