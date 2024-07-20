#!/usr/bin/env python


import requests
# https://pixe.la/

'''
CREATE USER POST
'''

user_token = "abrakadabraski"
user_name = "indexsam"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
 "token": user_token,
 "username": user_name,
 "agreeTermsOfService":"yes", 
  "notMinor":"yes",

}


# step 1 done

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)


# step 2
'''
CREATE GRAPH  (POST)
'''

graph_endpoint = f"{pixela_endpoint}/{user_name}/graphs"

graph_params ={
 "id": "graph1",
 "name": "Cycling graph",
  "unit":"Km",
  "type": "float",
  "color": "momiji",

}

headers = {

"X-USER-TOKEN": user_token,
}

# Done!

# response = requests.post(graph_endpoint, json=graph_params, headers=headers)
# print(response.text)



'''
INSERT
'''
# Next!
import datetime as dt

data = dt.datetime.now()
year = str(data.year)
month = str(data.month)
day = str(data.day)

amend ="0"
if len(month) == 1:
    month= amend + month
if len(day) == 1:
    day = amend + day


# DATE = year + month + day

#  OR  (single line)

DATE = data.strftime("%Y%m%d")

graph_id="graph1"

post_endpoint = f"{graph_endpoint}/{graph_id}"

post_params ={
 "date": DATE,
 "quantity": "45.7",
}

#response = requests.post(post_endpoint, json=post_params, headers=headers)
#print(response.text)

'''
UPDATE
'''


update_params={
 "quantity": "12.38",

}



update_endpoint = f"{post_endpoint}/{DATE}"
#response = requests.put(update_endpoint, json=update_params, headers=headers)
#print(response.text)


'''
DELETE
'''

delete_endpoint = update_endpoint
#response = requests.delete(delete_endpoint, headers=headers)
#print(response.text)
