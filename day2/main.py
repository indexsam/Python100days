#!/usr/bin/env python

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or  15? "))
number = int(input("How many people to split the bill? "))
amount = (total + tip)/number
print("Each person should pay: ${:.2f}".format(amount))

