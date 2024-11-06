def calculator(num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            else:
                 return num1 / num2
        else:
            return "Error: Invalid operator entered."

def main():
    try:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
    except ValueError:
        print("Error: Invalid input. Please enter numerical values.")
        return

    operator = input("Enter an operator (+, -, *, /): ")

    result = calculator(num1, num2, operator)
    print(f"result: {result}")

if __name__ == "__main__":
    main()


