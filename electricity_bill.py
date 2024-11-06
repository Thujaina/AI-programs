# Python program to calculate electricity bill

def calculate_bill(units):
    if units <= 100:
        # First 100 units at rate of Rs. 3 per unit
        bill = units * 3
    elif units <= 200:
        # Next 100 units at rate of Rs. 5 per unit
        bill = (100 * 3) + (units - 100) * 5
    else:
        # Above 200 units at rate of Rs. 8 per unit
        bill = (100 * 3) + (100 * 5) + (units - 200) * 8
    return bill

# Input from user
units_consumed = int(input("Enter the number of units consumed: "))
bill_amount = calculate_bill(units_consumed)

print(f"Electricity Bill: Rs. {bill_amount}")