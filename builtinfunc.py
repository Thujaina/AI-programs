# Sample data: a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter: Keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4, 6, 8, 10]
# Sample data: a list of numbers
numbers = [1, 2, 3, 4, 5]

# Map: Square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
from functools import reduce

# Sample data: a list of numbers
numbers = [1, 2, 3, 4, 5]

# Reduce: Calculate the product of all numbers
product = reduce(lambda x, y: x * y, numbers)

print(product)  # Output: 120


