#!/usr/bin/env python3
"""
Demo Python application with intentional errors for GitHub Actions failure demonstration
"""

import sys
import os
import nonexistent_module  # This import will fail

# Syntax error: inconsistent indentation
def broken_function():
  if True:
      print("Inconsistent indentation")
    print("This line has wrong indentation")  # IndentationError

# Logic errors
def calculate_average(numbers):
    if len(numbers) == 0:
        return sum(numbers) / len(numbers)  # Division by zero
    return sum(numbers) / len(numbers)

# Type errors
def process_data(data):
    # This will fail if data is not a string
    return data.upper() + 123  # TypeError: can only concatenate str (not "int") to str

# Undefined variable usage
def use_undefined_variable():
    print(undefined_variable)  # NameError: name 'undefined_variable' is not defined
    return some_other_undefined_var

# Import error - trying to use something that doesn't exist
def use_missing_import():
    return nonexistent_module.some_function()

# File operation errors
def read_nonexistent_file():
    with open('nonexistent_file.txt', 'r') as f:  # FileNotFoundError
        return f.read()

# Main function with multiple error calls
def main():
    print("Starting demo application with intentional errors...")
    
    # These function calls will cause various types of failures
    broken_function()
    calculate_average([])
    process_data(123)
    use_undefined_variable()
    use_missing_import()
    read_nonexistent_file()

if __name__ == "__main__":
    main()