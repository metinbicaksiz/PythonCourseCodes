import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_Key = os.environ.get("OWN_KEY")
account_sid = "ACa87511577d893049859fa7ea2109015f"
auth_token = os.environ.get("AUTH_TOKEN")


weather_params = {
    "lat": 49.248810,
    "lon": -122.980507,
    "cnt": 4,
    "appid": API_Key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
# code = data["list"][0]["weather"][0]["id"]
will_rain = False
for hour_data in data["list"]:
    condition_code =hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It will rain! Take an umbrella! ☂️",
        from_="+15513683527",
        to="+17789512912",
    )
    print(message.status)
else:
    print("No Rain")