#!/usr/bin/env python

from art import logo
import os
import sys

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

def clear():
    os.system('clear')

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  
  if input ("Press 'q' to Quit the application or any key proceeed...! " ).lower()=='q':
    sys.exit(0)
  else:
    num1 = float(input("Number: "))
    for symbol in operations:
      print(symbol)
    should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to clear: ").lower() == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()
