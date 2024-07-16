#!/usr/bin/env python

import pandas

'''
THE TASK BEGINS HERE!!!!!

'''
df = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:  {"A": "Alfa", "B": "Bravo"}

nato_dict = {row.letter:row.code for index, row in df.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

'''
Manage error with a loop using recursion

'''

def generate():

    name = input("Enter your name: ").strip().upper()
    try:
        print([ nato_dict[i] for i in name ])
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate()   # the magic lies here


generate()
