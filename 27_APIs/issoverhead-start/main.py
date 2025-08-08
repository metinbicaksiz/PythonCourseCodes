import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "metinbicaksiz@gmail.com"
PASSWORD = ""

MY_LAT = 49.248810 # Your latitude
MY_LONG = -122.980507 # Your longitude

def is_issOverHead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT -5 <= iss_latitude <= MY_LAT+5 and MY_LONG -5 <= iss_longitude <= MY_LONG+5:
        return True
    return None


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
}

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if sunset <= time_now <= sunrise:
        return True
    return None

if is_issOverHead() and is_night():
    time.sleep(3600)
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(MY_EMAIL, PASSWORD)
    connection.send_message(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject:Look up\n\nThe ISS is above you."
    )
