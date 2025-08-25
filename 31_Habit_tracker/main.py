import requests
import os

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "metinbicaksiz"
PASSWORD = os.environ.get("PASSWORD")
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
pixel_data = {
    "date": "20250823",
    "quantity": "11.5"
}   

pixel_creation = requests.post(url=pixel_creation_endpoint, headers=headers, json=pixel_data)
print(pixel_creation.text)