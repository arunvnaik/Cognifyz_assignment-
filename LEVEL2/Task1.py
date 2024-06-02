import random

answer = random.randint(1, 100)
print("Try to guess the number between 1 and 100.")

chances = 0  # Initialize the chance counter

while True:
    guess = int(input("Enter your guess: "))
    chances += 1
    
    if guess == answer:
        print(f"You guessed it in {chances} attempts!")
        break
    elif guess > answer:
        print("Go lower")
    else:
        print("Go higher")
