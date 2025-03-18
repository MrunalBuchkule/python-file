import random

def get_factors(number):
    """Returns a list of factors of the given number."""
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def number_guessing_game():
    
    number_to_guess = random.randint(1, 100)
    
    
    max_attempts = 10
    attempts = 0
    
    print("Welcome to the Enhanced Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while attempts < max_attempts:
        try:
            
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
            attempts += 1
            
            
            if guess < number_to_guess:
                print("Too Low!")
            elif guess > number_to_guess:
                print("Too High!")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts!")
                return 

            
            if attempts == 5:
                factors = get_factors(number_to_guess)
                hint_factor = random.choice(factors)
                print(f"Hint: The number is divisible by {hint_factor}")
            
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print(f"Sorry! You've used all {max_attempts} attempts. The number was {number_to_guess}.")


number_guessing_game()
