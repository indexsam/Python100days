#!/usr/bin/env python

dict_morse ={

'A':'.-',
'B':'-...',
'C':'-.-.',
'D':'-..',
'E':'.',
'F':'..-.',
'G':'--.',
'H':'....',
'I':'..',
'J':'.---',
'K':'-.',
'L':'.-..',
'M':'--',
'N':'-.',
'O':'---',
'P':'.--.',
'Q':'--.-',
'R':'.-.',
'S':'...',
'T':'-',
'U':'..-',
'V':'...-',
'W':'.--',
'X':'-..-',
'Y':'-.--',
'Z':'--..',
'0':'-----',
'1':'.----',
'2':'..---',
'3':'...--',
'4':'....-',
'5':'.....',
'6':'-....',
'7':'--...',
'8':'---..',
'9':'----.',

}

text = input("Enter your message: ")
text_list=[]
for i, in text:
    i = i.upper()
    text_list.append(dict_morse.get(i," "))

# print(text_list)
print("Morse Code")
print(''.join(text_list))
