import requests
from twilio.rest import Client

key ="583cd7be18fca053c286e1cf1313"
endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "AC7745fadf580fd3ed2a203fa0bd381da9"
auth_token = "a0d5355e401dcc164662f7108ffcd72f"

weather_params = {
    "lat": -4.066000,
    "lon":39.674490,
    "appid": key,
    "cnt": 4,
}
response = requests.get(endpoint, params=weather_params)
response.raise_for_status()
actual_weather_data = response.json()

will_rain = False
for hourly_data in actual_weather_data["list"]:
    condition_code = hourly_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+13342039257',
        body="It's going to rain today. Carry an umbrella!",
        to='+254742845184',
    )
    print(message.status)
