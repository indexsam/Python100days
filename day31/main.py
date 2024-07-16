#!/usr/bin/env python

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME="Ariel"

from tkinter import *

import random
import pandas as pd


try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df= pd.read_csv("./data/french_words.csv")


dict_list = df.to_dict(orient='records')




#-----------------------Random choice-----------------------------#
def Ychoice():
    global card_english

    for i, value in enumerate(dict_list):
        if value['English'] == card_english:
            del dict_list[i]
    
    dat = pd.DataFrame(dict_list)
    dat.to_csv("./data/words_to_learn.csv", index=False)
    Xchoice()
#-------------------------Random choice for X button---------------#
def Xchoice():
    global card_english, flip_timer
    window.after_cancel(flip_timer)

    dict_choice = random.choice(dict_list)
    card_french = dict_choice['French']
    card_english = dict_choice['English']
    canvas.itemconfig(title_text, text=f"French", fill="black")
    canvas.itemconfig(word_text, text=f"{card_french}", fill="black")
    canvas.itemconfig(canvas_img, image=front_img)

    filp_timer = window.after(3000,func=change)

    
'''
if dict_choice was set to global,
then:

instead of the 1st 5 lines in Ychoice(),

Beta:
dict_list.remove(dict_choice)

syntax. list.remove('value')

'''

#------------------------------------------------------------------#
def change():
    canvas.itemconfig(title_text, fill="white", text=f"English")
    canvas.itemconfig(word_text, fill="white", text=f"{card_english}")
    canvas.itemconfig(canvas_img, image=back_img)
    
    


window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=change)


canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
canvas_img = canvas.create_image(400, 263)
canvas.grid(row=0, column=0, columnspan=2)

back_img = PhotoImage(file="./images/card_back.png")


title_text = canvas.create_text(400,131, text="", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400,263, text="", font=(FONT_NAME, 60, "bold"))


x_image = PhotoImage(file="./images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, command=Xchoice)
x_button.grid(column=0, row=1)

y_image = PhotoImage(file="./images/right.png")
y_button =Button(image= y_image, highlightthickness=0, command=Ychoice)
y_button.grid(column=1, row=1)


Xchoice()


window.mainloop()
