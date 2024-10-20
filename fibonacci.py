# Recursive function for Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example: Find Fibonacci of 4
n = 4
print(f"Fibonacci of {n} is {fibonacci(n)}")
