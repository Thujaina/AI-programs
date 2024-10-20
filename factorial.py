# Recursive function for factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Example: Find factorial of 4
n = 4
print(f"Factorial of {n} is {factorial(n)}")
