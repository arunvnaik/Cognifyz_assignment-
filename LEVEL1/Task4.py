def calculator():
   
    num1 = float(input("Enter a number: "))
    
    
    while True:
        operator = input("Enter an operator (+, -, *, /, %): ").strip()
        if operator in ['+', '-', '*', '/', '%']:
            break
        else:
            print("Invalid operator! Please enter one of the following: +, -, *, /, %.")
    
    
    num2 = float(input("Enter another number: "))

    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error! Division by zero."
    elif operator == '%':
        result = num1 % num2
    
    return f"The result of {num1} {operator} {num2} is: {result}"

# Example usage:
print(calculator())
