import random

def number_guessing_game():
    
    number_to_guess = random.randint(1, 50)

    print(f"Debug: The number to guess is {number_to_guess}")
    
    
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")
    
    while True:
        try:
            
            guess = int(input("Enter your guess: "))
            
            
            attempts += 1

            
            if guess < number_to_guess:
                print("Too Low!")
            elif guess > number_to_guess:
                print("Too High!")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts!")
                break  
        except ValueError:
            print("Invalid input. Please enter a valid number.")


number_guessing_game()
