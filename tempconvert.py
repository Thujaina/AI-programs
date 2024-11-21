# temperature_converter.py
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

# main.py
from temperature_converter import celsius_to_fahrenheit, fahrenheit_to_celsius

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    try:
        choice = int(input("Enter your choice (1 or 2): "))
        if choice == 1:
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius):.2f}°F.")
        elif choice == 2:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit):.2f}°C.")
        else:
            print("Invalid choice! Please choose 1 or 2.")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()