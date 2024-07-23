#!/usr/bin/env python

import requests


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        code = "TESTING"
        return code


def get_token():
    client_id ="xxxxxxxxxxxxxxxxxxxxxxx"
    client_secret="xxxxxxxxxxxxxxxxxx"
    token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
    headers= {
     "Content-Type": "application/x-www-form-urlencoded"
     }
    token_params = {
      "grant_type": "client_credentials",
      "client_id": client_id,
      "client_secret": client_secret,

    }

    response = requests.post(token_endpoint, data=token_params, headers=headers)
    response.raise_for_status()
    return response.text


# data = get_token()
token = data["access_token"]
validity_period = math.ceil(data["expires_in"]/60)
now_time = datetime.now().strftime("%X")
print("Token expires in {validity_period} mins!!")
print("Current time is : {now_time}")



def find_iata(token, city):
    
    headers = {

   "Authorization": f"Bearer {token}"
    }

    query = {
            "keyword": f"Paris",
            "max": "2",
            "include": "AIRPORTS",
        }

    Endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

    response = requests.get(Endpoint,
            headers=headers,
            params=query)


    response.raise_for_status()
    print(response.text)



