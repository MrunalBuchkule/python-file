
def fibonacci_loop(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def fibonacci_recursion(n, fib_sequence=None):
    if fib_sequence is None:
        fib_sequence = []
    
    if n <= 0:
        return fib_sequence
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        if len(fib_sequence) < 2:
            fib_sequence = [0, 1]
        else:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fibonacci_recursion(n - 1, fib_sequence)

def main():
    try:
        
        n = int(input("Enter the number of terms in the Fibonacci sequence: "))

        if n <= 0:
            print("Please enter a positive integer.")
        else:
            
            fib_loop = fibonacci_loop(n)
            print(f"Fibonacci sequence using for loop: {fib_loop}")

            
            fib_recursion = fibonacci_recursion(n)
            print(f"Fibonacci sequence using recursion: {fib_recursion}")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")


main()
