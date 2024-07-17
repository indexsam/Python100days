#!/usr/bin/env python

import smtplib

my_email = "obadanindexsam@gmail.com"
password = "xxxxxxxxxxxxx"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="obadansam@gmail.com", msg="Hello")
connection.close()

print("successful!!")
