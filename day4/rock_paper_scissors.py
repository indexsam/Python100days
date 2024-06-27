#!/usr/bin/env python

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]


quit =''
while(quit!='q'):

  try:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    if user_choice not in [0,1,2]:
      print("You typed an invalid number, you lose!")

    else:
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_images[computer_choice])

        if computer_choice == user_choice:
          print("It's a draw")
        elif user_choice == 0 and computer_choice == 2:
          print("You win!")
        elif user_choice == 0 and computer_choice == 1:
          print("You lose")
        elif user_choice == 1 and computer_choice == 0:
          print("You win!")
        elif user_choice == 1 and computer_choice == 2:
          print("You lose")
        elif user_choice == 2 and computer_choice == 0:
          print("You lose!")
        elif user_choice == 2 and computer_choice == 1:
          print("You win")
  except ValueError:
    print("Numbers only!!!!")
  quit = input("Press 'q' to QUIT or any other key to continue!! ").lower()
