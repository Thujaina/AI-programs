import random

number = random.randint(1, 100)
attempts = 0

print("Guess the number (between 1 and 100):")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess == number:
        print(f"Correct! You guessed it in {attempts} tries.")
        break
    elif guess < number:
        print("Too low.")
    else:
        print("Too high.")
