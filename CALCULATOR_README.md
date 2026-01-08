# Basic Calculator App

A simple command-line calculator application written in Python that performs basic arithmetic operations.

## Features

- **Addition**: Add two numbers
- **Subtraction**: Subtract two numbers
- **Multiplication**: Multiply two numbers
- **Division**: Divide two numbers with zero-division protection
- **User-friendly interface**: Interactive menu-driven interface
- **Input validation**: Handles invalid inputs gracefully
- **Error handling**: Proper error messages for edge cases

## Requirements

- Python 3.x

## Usage

Run the calculator from the command line:

```bash
python3 calculator.py
```

### How to Use

1. When the calculator starts, you'll see a menu with operation options:
   - 1: Add
   - 2: Subtract
   - 3: Multiply
   - 4: Divide
   - 5: Exit

2. Enter the number corresponding to your desired operation

3. Enter the first number when prompted

4. Enter the second number when prompted

5. The result will be displayed

6. The menu will appear again for another calculation, or choose 5 to exit

### Example Session

```
========================================
         BASIC CALCULATOR
========================================
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
========================================

Enter choice (1/2/3/4/5): 1
Enter first number: 15
Enter second number: 7

Result: 15.0 + 7.0 = 22.0
```

## Functions

The calculator includes the following functions:

- `add(x, y)`: Returns the sum of x and y
- `subtract(x, y)`: Returns the difference of x and y
- `multiply(x, y)`: Returns the product of x and y
- `divide(x, y)`: Returns the quotient of x and y (raises ValueError if y is 0)

## Error Handling

- **Invalid input**: If you enter non-numeric values, the calculator will prompt you to enter a valid number
- **Division by zero**: If you attempt to divide by zero, the calculator will display an error message
- **Invalid menu choice**: If you select an invalid option, you'll be prompted to choose again

## License

This project is open source and available under the MIT License.
