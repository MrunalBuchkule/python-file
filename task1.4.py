
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursion(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)


def main():
    try:
        
        number = int(input("Enter a number to calculate its factorial: "))
        
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
        
            fact_loop = factorial_loop(number)
            fact_recursion = factorial_recursion(number)
            
            
            print(f"Factorial of {number} using for loop is: {fact_loop}")
            print(f"Factorial of {number} using recursion is: {fact_recursion}")
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


main()
