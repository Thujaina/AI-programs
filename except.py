import random
import statistics

def perform_calculations():
    try:
        # Prompt user for input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform division
        division_result = num1 / num2
        print(f"Division result: {division_result}")

        # Generate a random list of integers
        random_numbers = [random.randint(1, 100) for _ in range(10)]
        print("Random list of numbers:", random_numbers)

        # Calculate statistics on the random list
        mean_value = statistics.mean(random_numbers)
        median_value = statistics.median(random_numbers)
        variance_value = statistics.variance(random_numbers)
        print("Mean of random numbers:", mean_value)
        print("Median of random numbers:", median_value)
        print("Variance of random numbers:", variance_value)

        # Additional arithmetic operations
        addition_result = num1 + num2
        multiplication_result = num1 * num2
        print(f"Addition result: {addition_result}")
        print(f"Multiplication result: {multiplication_result}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed. Please enter a non-zero second number.")
    
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    
    finally:
        print("Calculations complete. Thank you for using our calculator.")

# Run the function
perform_calculations()
