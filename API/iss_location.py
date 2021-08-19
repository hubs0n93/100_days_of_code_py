import requests # HTTP requests python

# get response from url=https://...
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# raise error when error 404 occur (connection error)
response.raise_for_status()

data = response.json()

print(data)
print("***********")
for row in data:
	print(row)

longitude = data["iss_position"]['longitude']
latitude = data["iss_position"]['latitude']
iss_position = (longitude, latitude)

print(iss_position)