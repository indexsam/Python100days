#!/usr/bin/env python

from tkinter import *
from tkinter import messagebox
import random
# import pyperclip

# PS> pyinstaller  --onefile --noconsole main.py  (create exec file) https://www.youtube.com/watch?v=bEBMo52OCis

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    let = [random.choice(letters) for _ in range(nr_letters)]
    num = [random.choice(numbers) for _ in range(nr_numbers)]
    sym = [random.choice(symbols) for _ in range(nr_symbols)]
  
    password_list = let + num + sym
    random.shuffle(password_list)

    pwd = ''.join(password_list)

    password_entry.insert(0, pwd)
    
    # pyperclip.copy(pwd)

# print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():

    website = site_entry.get()
    email_username = name_entry.get()
    password = password_entry.get()

    if len(website) ==0 or len(password) ==0:
        messagebox.showinfo(message= "All fields must be filled!!")
    else:
        isOK = messagebox.askokcancel(title= website, message =f"Email: {email_username} \n Password: {password} ")

        if isOK:
            with open("./saved_password.txt", "a") as file:
                file.write(f"{website} | {email_username} | {password} \n")
                name_entry.delete(0,END)
                site_entry.delete(0,END)
                password_entry.delete(0,END)  # delete beginning to end 
                name_entry.insert(0, "example@email.com")
                site_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

site_label = Label(text="Website:")
site_label.grid(column=0, row=1)

site_entry = Entry(width=40)
site_entry.grid(column=1, row=1, columnspan=2)
site_entry.focus()

name = Label(text="Email/Username:")
name.grid(column=0, row=2)

name_entry = Entry(width=40)
name_entry.grid(column=1, row=2, columnspan=2)
name_entry.insert(0, "example@email.com") # END will be the very last xter


password = Label(text="Password:")
password.grid(column=0, row=3)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

gen = Button(text="Generate", command=generate)
gen.grid(column=2, row=3)

add = Button(text="Add", width=35, command=save_data)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()
