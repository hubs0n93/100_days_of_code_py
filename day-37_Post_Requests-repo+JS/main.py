import requests
from datetime import datetime

USERNAME = "hubson93"
TOKEN = "lkj435sdlkj34"
GRAPH = "graph1"


# --------------------- FIRST STEP - create account ----------------------#
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "lkj435sdlkj34",
    "username": "hubson93",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # setting up the user in pixela
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# ---------------------------- SECOND - create a graph ---------------------------------#
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH,
    "name": "hubson_mindset",
    "unit": "times",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# # send request
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# ------------------------ THIRD - create a pixel ---------------------------#
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
# format date - strftime for formatting
today = datetime.now().strftime("%Y%m%d")

post_pixel_config = {
    "date": "20210801",
    "quantity": "5",
}
# #send request
response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
print(response.text)


# ----------------------- UPDATE PIXEL or DELETE PIXEL --------------------------------------#
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{20210511}"
update_pixel_config = {
    "quantity": "25",
}
# ********** UPDATE *********** #

# # Send request
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

# ********** DELETE *********** #
# Send request
# response = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(response.text)
