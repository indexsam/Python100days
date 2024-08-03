from flask import Flask

import random

number = random.randint(0,9)

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Guess a number between 0 and 9<h1/>\
           <img  src='https://media.giphy.com/media/EsOAahQCW3dk1MZmQV/giphy.gif?cid=790b7611fcm7i07m39scuew4ztu28izfrubpcvbhiet046d9&ep=v1_gifs_search&rid=giphy.gif&ct=g'/>"

@app.route("/<int:guess>")
def guess_number(guess):
    if guess == number:
        return "<h1 style='color:green'>You found Me !!<h1/>\
               <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=350 height=350 />"
    elif guess > number:
        return "<h1 style='color:red'>Too high, Try again!!<h1/>\
               <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=350 height=350 />"
    else:
        return "<h1 style='color:blue'>Too low, Try again!!<h1/>\
               <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=350  height=350 />"

if __name__=="__main__":
    app.run(debug=True)