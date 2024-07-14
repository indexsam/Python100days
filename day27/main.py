#!/usr/bin/env python

from tkinter import *

windows = Tk()
windows.title("Miles to kilometer converter")
windows.config(padx=20, pady=20)

def convert():
    miles = float(miles_input.get())
    km = miles * 1.609
    result_label.config(text=str(round(km,2)))


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)
miles_input.focus()

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

equal_label = Label(text= "is equal to")
equal_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

kilo_label = Label(text="Km")
kilo_label.grid(column=2, row=1)

calc_btn = Button(text="Calculate", command=convert)
calc_btn.grid(column=1, row=2)


windows.mainloop()
