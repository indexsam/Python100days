#!/usr/bin/env python

'''
Create a letter using starting_letter.txt 
for each name in invited_names.txt
Replace the [name] placeholder with the actual name.
Save the letters in the folder "ReadyToSend".

'''
letter_path = "./Input/letters/starting_letter.txt"
names_path = "./Input/Names/invited_names.txt"
save_path = "./Output/ReadyToSend/"

def Read_letter(path):
    with open(path) as file:
        data = file.read()
    return data

letter = Read_letter(letter_path)

def Get_names(path):
    names =[]
    with open(path) as file:
        data2 = file.readlines()
        for d in data2:
            names.append(d.strip())
    return names 

name_list = Get_names(names_path)

def Save_letters(path, allnames, doc):
    for name in allnames:
        new_doc= doc.replace('[name]', name)
        with open(path + f'/{name}.txt', 'w') as file:
            file.write(new_doc)

Save_letters(save_path, name_list, letter)
print("Successful!!! All mails are ready!")
