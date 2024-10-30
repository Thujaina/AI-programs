# debug_example.py
import pdb

def calculate_square(number):
    result = number ** 2  # Corrected code to square the number
    return result

def main():
    num = 5
    pdb.set_trace()  # Start debugging here
    squared = calculate_square(num)
    print(f"The square of {num} is {squared}")

if __name__ == "__main__":
    main()

#output

> <string>(11)main()
(Pdb) c
The square of 5 is 25

[Program finished]