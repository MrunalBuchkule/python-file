def calculator():
    while True:
        try:
            
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            
            addition = num1 + num2
            subtraction = num1 - num2
            multiplication = num1 * num2
            division = num1 / num2 if num2 != 0 else "Error! Division by zero."
            modulus = num1 % num2 if num2 != 0 else "Error! Modulus by zero."
            exponentiation = num1 ** num2

        
            print(f"\nResults:")
            print(f"Addition: {num1} + {num2} = {addition}")
            print(f"Subtraction: {num1} - {num2} = {subtraction}")
            print(f"Multiplication: {num1} * {num2} = {multiplication}")
            print(f"Division: {num1} / {num2} = {division}")
            print(f"Modulus: {num1} % {num2} = {modulus}")
            print(f"Exponentiation: {num1} ** {num2} = {exponentiation}")
            
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        
    
        another_calculation = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        
        if another_calculation != "yes":
            print("Goodbye!")
            break


calculator()
