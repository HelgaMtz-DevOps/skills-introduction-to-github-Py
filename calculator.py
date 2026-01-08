#!/usr/bin/env python3
"""
Basic Calculator App
This is a simple command-line calculator that performs basic arithmetic operations.
"""


def add(x, y):
    """Add two numbers."""
    return x + y


def subtract(x, y):
    """Subtract two numbers."""
    return x - y


def multiply(x, y):
    """Multiply two numbers."""
    return x * y


def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


def get_number(prompt):
    """Get a valid number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def display_menu():
    """Display the calculator menu."""
    print("\n" + "=" * 40)
    print("         BASIC CALCULATOR")
    print("=" * 40)
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("=" * 40)


def main():
    """Main function to run the calculator."""
    while True:
        display_menu()
        
        choice = input("\nEnter choice (1/2/3/4/5): ").strip()
        
        if choice == '5':
            print("\nThank you for using the calculator. Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select a valid option (1-5).")
            continue
        
        # Get numbers from user
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        # Map choices to operations and symbols
        operations = {
            '1': (add, '+'),
            '2': (subtract, '-'),
            '3': (multiply, '*'),
            '4': (divide, '/')
        }
        
        # Perform calculation based on choice
        try:
            func, operation = operations[choice]
            result = func(num1, num2)
            print(f"\nResult: {num1} {operation} {num2} = {result}")
        
        except ValueError as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
