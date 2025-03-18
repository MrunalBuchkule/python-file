def basic_math_operations():
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        
        
        if num2 != 0:
            division = num1 / num2
        else:
            division = "Error! Division by zero is not allowed."
        
        
        print(f"\nResults:")
        print(f"Addition: {num1} + {num2} = {addition}")
        print(f"Subtraction: {num1} - {num2} = {subtraction}")
        print(f"Multiplication: {num1} * {num2} = {multiplication}")
        print(f"Division: {num1} / {num2} = {division}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

basic_math_operations()
