# A program that finds the minimum and maximum values in a list using recursion
def min_max(sequence):
    if len(sequence) == 1:
        return sequence[0], sequence[0]
    else:
        return min(sequence[0], min_max(sequence[1:])[0]), max(sequence[0], min_max(sequence[1:])[1])
    
# Recursive function to compute the integer part of the base-two logarithm of n using only addition and integer division
def find_log(num, log_val):
    if num == 1:
        print(f"The value of log is {log_val}")
        return log_val
    else:
        print(f"The value of log is {log_val}")
        return find_log(num//2, log_val+1)
    
# find_log(16, 0)
# find_log(8, 1)
# find_log(4, 2)
# find_log(2, 3)
# find_log(1, 4) -> 4

# Recursive function to compute the product of two positive integers, m and n, using only addition and subtraction
def product(m, n, value=0):
    if n == 0:
        return value
    else:
        return product(m, n-1, value+m)
    
# product(5,3)
# product(5,2,5)
# product(5,1,10)
# product(5,0,15) -> 15
    
# Check if string is palindrome using recursion
def palindrome_check(string):
    if len(string) == 1:
        return True
    else:
        return string[0] == string[-1] and palindrome_check(string[1:-1])
    
# palindrome_check("racecar")
# palindrome_check("aceca")
# palindrome_check("cec")
# palindrome_check("e") -> True

# Recursive function that rearranges a sequence of integer values so that all the even values appear before all the odd values
def even_odd(sequence, even=[], odd=[]):
    if len(sequence) == 0:
        return even + odd
    else:
        if sequence[0] % 2 == 0:
            even.append(sequence[0])
        else:
            odd.append(sequence[0])
        return even_odd(sequence[1:], even, odd)
    
# even_odd([1,2,3,4], [], [])
# even_odd([2,3,4], [], [1])
# even_odd([3,4], [2], [1])
# even_odd([4], [2], [1,3])
# even_odd([], [2,4], [1,3]) -> [2,4,1,3]

# Fibanocci series of a number entered by the user
def fibanocci(num):
    if num <= 1:
        return 1
    else:
        return fibanocci(num-1) + fibanocci(num-2)

# fibanocci(5)
# fibanocci(4) + fibanocci(3)
# fibanocci(3) + fibanocci(2) + fibanocci(2) + fibanocci(1)
# fibanocci(2) + fibanocci(1) + fibanocci(1) + fibanocci(0) + fibanocci(1) + fibanocci(0) + 1
# fibanocci(1) + fibanocci(0) + 1 + 1 + 0 + 1 + 0 + 1
# 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 -> 8

# Recursive function to demonstrate Ackermann's function
# Ackermann's function is a recursive mathematical algorithm that can be used to compute the value of a function
# For example, the value of ackermann(3, 4) is 125
def ackermann(m, n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))

