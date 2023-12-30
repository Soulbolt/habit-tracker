import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME= os.getenv("USERNAME")
TOKEN= os.getenv("TOKEN")

""" To Create a User
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)
"""

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "drawing",
    "unit": "day",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create Graph
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()
# Add a pixel to the graph
ADD_PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/graph1/add"
add_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}
# response =  requests.post(url=ADD_PIXEL_ENDPOINT, headers=headers, json=add_pixel)
# print(response.text)
update_pixel = {
    "quantity": "20",
}
UPDATE_PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/graph1/{today.strftime("%Y%m%d")}"
# response = requests.put(url=UPDATE_PIXEL_ENDPOINT, headers=headers, json=update_pixel)
# print(response.text)

DELETE_PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/graph1/{today.strftime("%Y%m%d")}"
response = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=headers)
print(response.text)
