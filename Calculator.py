import math

class AdvancedCalculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero."

    def power(self, x, y):
        return x ** y

    def square_root(self, x):
        return math.sqrt(x)

    def logarithm(self, x, base):
        return math.log(x, base)

# Create an instance of the AdvancedCalculator class
calculator = AdvancedCalculator()

while True:
    print("\nAdvanced Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == '8':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4', '5', '6', '7','8','9']:
        x = float(input("Enter the first number: "))

        if choice != '6':  # Square root only requires one input
            y = float(input("Enter the second number: "))

        if choice == '+':
            result = calculator.add(x, y)
            print("Result:", result)
        elif choice == '-':
            result = calculator.subtract(x, y)
            print("Result:", result)
        elif choice == '*':
            result = calculator.multiply(x, y)
            print("Result:", result)
        elif choice == '/':
            result = calculator.divide(x, y)
            print("Result:", result)
        elif choice == '^':
            result = calculator.power(x, y)
            print("Result:", result)
        
           
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
