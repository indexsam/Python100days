#!/usr/bin/env python

import smtplib
import datetime as dt
import random
import pandas as pd

my_email = "obadanindexsam@gmail.com"
password = "xxxxxxxx"  # set password before running



list_letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
letter = random.choice(list_letters)

with open(f"./letter_templates/{letter}") as file:
    message = file.read()



def send_mail(email, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email, 
                    msg=f"Subject: Birthday Wishes\n\n{message}")


    print("Mail sent successfully!!")


df = pd.read_csv("./birthdays.csv")

now= dt.datetime.now()

this_month= now.month
this_day = now.day

new_df = df[(df["month"]==this_month) & (df["day"]==this_day)]


if not new_df.empty:
    recipients = [{'name':row["name"], 'email':row["email"]} for index, row in new_df.iterrows()]

    for data in recipients:
        msg = message.replace("[NAME]", data['name'] )
        send_mail(data['email'], msg)
else:
    print("Nobody celebrating birthday today!! ")


