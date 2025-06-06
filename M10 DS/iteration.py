def factorial_iterative(n):
    """Calculate factorial using an iterative loop."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
number = int(input("Enter a number to find its factorial: "))
fact = factorial_iterative(number)
print(f"Factorial of {number} is {fact}")
