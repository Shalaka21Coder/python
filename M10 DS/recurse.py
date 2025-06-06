def factorial_recursive(n):
    """Calculate factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage
number = int(input("Enter a number to find its factorial: "))
result = factorial_recursive(number)
print(f"Factorial of {number} is {result}")
