#!/usr/bin/env python

import turtle
import pandas as pd

screen = turtle.Screen()
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
'''
def click_fn(x,y):
    print(x,y)

turtle.onscreenclick(click_fn)
'''
obj = turtle.Turtle()

data = pd.read_csv("50_states.csv")

guess =0
correct_states =[]
while guess < 50:

    state = screen.textinput(title= f"states {len(correct_states)}/50", prompt="Enter a state in America")

    if state is not None:
        state = state.strip().title()
        if  state in data['state'].to_list():
            state_data = data[data['state']== state].reset_index()
            obj.hideturtle()
            obj.penup()
            obj.goto(int(state_data.iloc[0]['x']) ,int(state_data.iloc[0]['y']))
            obj.write(state_data.iloc[0][ 'state'])
            correct_states.append(state)
    else:
        break


    guess +=1

missing_states = data[~data['state'].isin(correct_states)]
missing_states.to_csv("states_to_learn.csv", index=False)


turtle.mainloop()

