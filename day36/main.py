#!/usr/bin/env python

import requests
STOCK_API = "GXPHxxxxxxxxxxxxxxxx"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API ="6faxxxxxxxxxxxxxc7"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


from twilio.rest import Client

def send_sms(msg):
    account_sid = 'Axxxxxxxxxxxxxxxxxxxxxxb0'
    auth_token = '34xxxxxxxxxxxxxxxxxxxxxxf65'


    client = Client(account_sid, auth_token)

    message = client.messages.create(
                        from_='+12513166402',
                          to='+2347068000524',
                         body=msg)


parameters ={
  "function":"TIME_SERIES_DAILY",
  "symbol":STOCK_NAME,
  "apikey": STOCK_API,
  
}
response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
data = data["Time Series (Daily)"]
list_dict = [value for key, value in data.items()] 
print("Yesterday closing pirce: " , list_dict[0]["4. close"])



print("Day before yesterday's closing price: ", list_dict[1]["4. close"])


ytd = list_dict[0]["4. close"]
dbytd = list_dict[1]["4. close"]
print ("A difference of : ", abs(float(ytd) - float(dbytd)))



diff = abs(float(ytd) - float(dbytd))
add =  float(ytd) + float(dbytd)
pdiff = (diff/ (add*0.5)) *100
print("With a percentage difference of : ", pdiff )


first_3art =[]

if pdiff > 4:    # >5
    print("Getting News....!!")
    parameters = {
     "qInTitle":COMPANY_NAME,
     "apiKey": NEWS_API,
     }
    response = requests.get(NEWS_ENDPOINT, params=parameters )
    response.raise_for_status()
    data =  response.json()
    first_3art = data["articles"][:3]
    #print(first_3art)
else:
    print("No Worries!!")


if  first_3art:
    new_info =[{"Headline":info["title"], "Brief": info["description"]} for info in first_3art]
    print("")
    print(new_info)
    # optional for loop comes here to send the 3 messages. But to save cost, we send  just the firts one at index 0
    print("")
    message = f"TLSA: M-:{round(pdiff)}%\nHeadline:  {new_info[0]['Headline']} \nBrief:  {new_info[0]['Brief']}"
    print(message)
    #send_sms(message)



"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

