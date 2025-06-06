from functools import reduce

def factorial_iterative(n):
    """Iterative approach to calculate factorial."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """Recursive approach to calculate factorial."""
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_functional(n):
    """Functional approach to calculate factorial."""
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

# Test the functions
number = 5
print("Factorial of", number, "using Iterative approach:", factorial_iterative(number))
print("Factorial of", number, "using Recursive approach:", factorial_recursive(number))
print("Factorial of", number, "using Functional approach:", factorial_functional(number))
