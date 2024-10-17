#default argument program
def greet(name="Friend"):
    print(f"Hello, {name}!")

# Calling the function
greet()          # Uses default argument "Friend"
greet("Alice")   # Passes explicit argument "Alice"

#keyword argument program
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Calling the function using keyword arguments
greet(name="Alice", age=20)
greet(age=25, name="Bob")  # Order doesn't matter with keyword arguments

#arbitary argument program
def print_numbers(*args):
    for number in args:
        print(number, end=' ')
    print()

# Calling the function with a different number of arguments
print_numbers(10, 20, 30)    # Prints: 10 20 30
print_numbers(5, 15)         # Prints: 5 15
