# Factorial function
def factorial_recursive(n):
    """Calculates the factorial of a number recursively
    
    complexity: O(n)
    """
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)
    
def factorial_iterative(n):
    """Calculates the factorial of a number iteratively
    
    Complexity: O(n)
    """
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Fibonacci function
def fibonacci_recursive(n):
    """Calculates the nth Fibonacci number recursively"""
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    
def fibonacci_iterative(n):
    """Calculates the nth Fibonacci number iteratively
    
    Complexity: O(n)
    """
    if n <= 1:
        return n
    else:
        previous = 0
        current = 1
        for i in range(2, n+1):
            previous, current = current, previous + current
        return current
    
# Ruler function
def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length (followed by optional label)"""
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    """Draw tickk interval based on a central tick length"""
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_ruler(num_inches, major_length):
    """Draw ruler with given number of inches, major tick length"""
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))