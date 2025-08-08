import requests
from datetime import datetime


# ISS API
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# long = response.json()["iss_position"]["longitude"]
# latd = response.json()["iss_position"]["latitude"]


# Sunset / Sunrise API
parameters = {
    "lat": 49.248810,
    "lng": -122.980507,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters )
response.raise_for_status()
data = response.json()["results"]["sunrise"]
sunset = response.json()["results"]["sunset"]
sunrise_split = data.split("T")[1].split(":")[0]
sunset_split = sunset.split("T")[1].split(":")[0]
print(sunrise_split)
print(sunset_split)

time_now = datetime.now()
print(time_now.hour)
