#!/usr/bin/env python

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"    # https://colorhunt.co/
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps =0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer) # var timer used after being set to global
    canvas.itemconfig(timer_text, text="00:00") # timer_text was the varaible  is was assigned to, needed for reconfig
    tick_label.config(text="")
    timer_label.config(text="Timer")
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60
    
    if reps % 8 ==0:
        timer_label.config(text="Break", fg=RED)
        count_down(long)
    elif reps % 2 ==0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >0:
        timer = window.after(1000, count_down, count-1) # 1000 -> 1sec, count_down (recursive call)  asigned to var timer for cancel purpose
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✓"
        tick_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW) # sets the window bg color and the padding for the content of the window.

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # size the pic and  set bg color for pic and zero border for pix
img = PhotoImage(file="tomato.png") # get the pic
canvas.create_image(100, 112, image=img) # x, y pos for image

timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")) # set the time text in the pic
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

tick_label = Label(fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)




window.mainloop()
