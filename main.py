import os
from dotenv import load_dotenv
import requests

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

response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
print(response.text)
