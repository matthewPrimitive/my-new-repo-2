 (a non-negative integer). The function accepts the number as an argument.

def factorial(n): 
    if n < 0: 
        return 0
    elif n == 0 or n == 1: 
        return 1
    else: 
        return n * factorial(n - 1)