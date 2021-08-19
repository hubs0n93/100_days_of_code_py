import requests
import smtplib
import os

# go to terminal, "set"
# set NAME=value (this command add variable to env)
# to get this value
# klucz = os.environ.get("DUPA")


my_email = 'boobis0093@gmail.com'
password = "Boobis00"

api_key = "10000f9ea2d22c34b441345d87d0af6c" #https://home.openweathermap.org/api_keys

MY_LAT = 50.06140
MY_LNG = 19.93658
parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}


response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

print(data)
# list for next 12 hours with weather forecast
all_day_hours = data["hourly"][:12]

is_rain = False
for weather in all_day_hours:
    # weather["weather"][0] -> dict
    if weather["weather"][0]["id"] < 700:
        is_rain = True
    else:
        pass

if is_rain:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        # makes connection secure
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='hubertskalon@gmail.com',
            msg="Subject: Rain\n\nTake an umbrella"
        )
    with smtplib.SMTP('smtp.gmail.com') as connection:
        # makes connection secure
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='anastazia2048@gmail.com ',
            msg="Subject: Rain\n\nkroolys bedzie dzisiej lolo, dzis kurde bedzie deszcz"
        )