import requests
from twilio.rest import Client
import os

api_key = os.environ["api_key"]
account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]

my_lat = 37.170052
my_lon = 33.222092

params = {
    "lat": my_lat,
    "lon": my_lon,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}
response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=params)
response.raise_for_status()
weather_data = response.json()
weather_hourly = weather_data["hourly"]

for i in range(12):
    if weather_hourly[i]["weather"][0]["id"] < 600 or 615 <= weather_hourly[i]["weather"][0]["id"] <= 616:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="It's going to rain today. Remember to bring an ☔️",
            from_="+15674093831",
            to=os.environ["my_phone"]
        )
        print(message.status)
        break
