# Happy Number Checker

## Description

Happy Number Checker is a Python function designed to verify if a given integer is a happy number or not. A happy number is defined as a number that eventually reaches 1 when replaced by the sum of the square of its digits repeatedly. For instance, the number 45 is a happy number because 4^2 + 5^2 equals 19, then 1^2 + 9^2 equals 82, then 8^2 + 2^2 equals 68, and finally 6^2 + 8^2 equals 100, which is not a happy number.

## Features

- Takes an integer as input
- Returns a boolean value indicating whether the input number is a happy number or not

## Installation

To use this function, simply copy the `check_happy_number` function from the script and paste it into your Python environment. There are no specific installation requirements for this function as it is a standalone piece of code.

## Usage

You can call the `check_happy_number` function with an integer as an argument. Here is an example:

```python
print(check_happy_number(45)) # Outputs: True
print(check_happy_number(44)) # Outputs: False
```

In the above example, the function returns `True` for the number 45 as it is a happy number, and `False` for the number 44 as it is not a happy number.
