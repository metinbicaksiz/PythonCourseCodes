import requests
import os
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "metinbicaksiz"
PASSWORD = "jflasjfslk;"
GRAPH_ID = "graph-1"
user_params = {
    "token": PASSWORD,
    "username": "metinbicaksiz",
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}

graph_params = {
    "id":GRAPH_ID,
    "name":"metin-cycling",
    "unit":"km",
    "type":"float",
    "color":"ajisai"
}
headers = {
    "X-USER-TOKEN": PASSWORD
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=pixela_endpoint, json=user_params)
# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": "10.5"
}   

pixel_creation = requests.post(url=pixel_creation_endpoint, headers=headers, json=pixel_data)
# print(pixel_creation.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

new_pixel_data = {
    "quantity": "8.5"
}

# update_pixel = requests.put(url=update_pixel_endpoint, headers=headers, json=new_pixel_data)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
delete_pixel = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(delete_pixel.text)
