import random

def number_guesser():
    print("Welcome to the Number Guessing Game..")
    
    
    min_range = int(input("Enter the minimum value of the range: "))
    max_range = int(input("Enter the maximum value of the range: "))
    

    answer = random.randint(min_range, max_range)
    
    print(f"Try to guess the correct number it!")

    chances = 0 

    while True:
        guess = int(input("Enter your guess: "))
        chances += 1
        
        if guess == answer:
            print(f"Congratulations! You've guessed the  correct number")
            break
        elif guess > answer:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")

# Directly call the number_guesser function
number_guesser()
