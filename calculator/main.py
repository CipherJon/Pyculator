"""
Main calculator application.
This module provides a command-line interface for performing various mathematical operations.
"""

import os
from typing import List, Tuple
from calculator.operations import (
    add, subtract, multiply, divide, power,
    square_root, percentage, modulo, absolute
)

def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_number(prompt: str) -> float:
    """
    Get a valid number from user input.
    
    Args:
        prompt (str): The prompt to display to the user
        
    Returns:
        float: The valid number entered by the user
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def display_menu() -> None:
    """Display the calculator menu."""
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")
    print("8. Modulo")
    print("9. Absolute Value")
    print("h. Show History")
    print("c. Clear Screen")
    print("q. Quit")

def perform_operation(choice: str, history: List[Tuple[str, float]]) -> None:
    """
    Perform the selected mathematical operation.
    
    Args:
        choice (str): The operation choice
        history (List[Tuple[str, float]]): List to store calculation history
    """
    try:
        if choice == '1':  # Add
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
            history.append((f"{num1} + {num2}", result))
            
        elif choice == '2':  # Subtract
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
            history.append((f"{num1} - {num2}", result))
            
        elif choice == '3':  # Multiply
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
            history.append((f"{num1} * {num2}", result))
            
        elif choice == '4':  # Divide
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
            history.append((f"{num1} / {num2}", result))
            
        elif choice == '5':  # Power
            num1 = get_number("Enter base number: ")
            num2 = get_number("Enter exponent: ")
            result = power(num1, num2)
            print(f"Result: {num1} ^ {num2} = {result}")
            history.append((f"{num1} ^ {num2}", result))
            
        elif choice == '6':  # Square Root
            num = get_number("Enter number: ")
            result = square_root(num)
            print(f"Result: √{num} = {result}")
            history.append((f"√{num}", result))
            
        elif choice == '7':  # Percentage
            num1 = get_number("Enter number: ")
            num2 = get_number("Enter total: ")
            result = percentage(num1, num2)
            print(f"Result: {num1} is {result}% of {num2}")
            history.append((f"{num1}% of {num2}", result))
            
        elif choice == '8':  # Modulo
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            result = modulo(num1, num2)
            print(f"Result: {num1} % {num2} = {result}")
            history.append((f"{num1} % {num2}", result))
            
        elif choice == '9':  # Absolute
            num = get_number("Enter number: ")
            result = absolute(num)
            print(f"Result: |{num}| = {result}")
            history.append((f"|{num}|", result))
            
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def show_history(history: List[Tuple[str, float]]) -> None:
    """
    Display the calculation history.
    
    Args:
        history (List[Tuple[str, float]]): List of calculation history
    """
    if not history:
        print("No calculations in history.")
        return
    
    print("\nCalculation History:")
    for i, (operation, result) in enumerate(history, 1):
        print(f"{i}. {operation} = {result}")

def main() -> None:
    """Main calculator function."""
    history: List[Tuple[str, float]] = []
    
    print("Welcome to the Advanced Calculator!")
    print("Type 'h' for help or 'q' to quit.")
    
    while True:
        display_menu()
        choice = input("\nSelect operation: ").lower()
        
        if choice == 'q':
            print("Thank you for using the calculator!")
            break
        elif choice == 'h':
            show_history(history)
        elif choice == 'c':
            clear_screen()
        elif choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            perform_operation(choice, history)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()