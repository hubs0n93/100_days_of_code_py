import requests

MY_LAT = 50.06140
MY_LNG = 19.93658

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
# take time from dict, after that split with T, take from list position [1], split again ":", take [0]
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)