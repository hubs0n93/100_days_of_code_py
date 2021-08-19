import requests
from datetime import datetime
import time
import smtplib

# connection SMTP:
my_email = 'boobis0093@gmail.com'
password = "Boobis00"
# geographical coordinates for Cracow
MY_LAT = 50.06140
MY_LNG = 19.93658


def main():
    # Get ISS position:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if ISS is above you. Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT + 5) > iss_latitude > (MY_LAT - 5) and (MY_LNG + 5) > iss_longitude > (MY_LNG - 5):

        # input to https://api.sunrise-sunset.org/json
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LNG,
            "formatted": 0,
        }
        # get actual time, and sunrise/sunset hours:
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 2

        time_now = datetime.now().hour

        # Check if it is dark:
        if sunset < time_now or time_now < sunrise:
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs='hubertskalon@gmail.com',
                    msg="Subject:International Space Station \n\nLook up"
                )

        else:
            pass

    else:
        print("I am waiting 60s and reconnect")
        time.sleep(60)
        main()


main()
