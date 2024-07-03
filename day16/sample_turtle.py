#!/usr/bin/env/ python

from turtle import Turtle, Screen
tim = Turtle()

tim.shape("turtle")
tim.color("coral")

my_screen = Screen()
my_screen.setup(width = 500, height=500)
print(my_screen.canvheight) # default = 300
my_screen.exitonclick()
my_screen.title("my turtle")


# from prettytable import Prettytable.

# tab = PrettyTable()

# tab.add_column('header', [list of rows]

# print(tab)
