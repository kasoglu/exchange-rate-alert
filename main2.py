import requests
from twilio.rest import Client

VIRTUAL_TWILIO_NUMBER = "Your Virtual Twilio Number"
VERIFIED_NUMBER = "Your Own Phone Number Verified With Twilio"

CRYPTO_ENDPOINT = "https://www.alphavantage.co/query"
APIKEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"


crypto_params = {
    "function": "CURRENCY_EXCHANGE_RATE",
    "from_currency": "EUR", # You can change the currency you want to rate here
    "to_currency": "TRY", # You can change the currency you want to rate here
    "apikey": APIKEY,
}
response = requests.get(CRYPTO_ENDPOINT, params=crypto_params)
data = response.json()["Realtime Currency Exchange Rate"]
data_list = [value for (key, value) in data.items()]

parite = f"{data_list[0]}/{data_list[2]}"
name = f"{data_list[1]}"
exchange_rate = f"{data_list[4]}"
# bid_rate = f"{data_list[7]}"
# ask_rate = f"{data_list[8]}"


client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

message = client.messages.create(
    body=f"{parite}\n{exchange_rate}",
    from_= VIRTUAL_TWILIO_NUMBER,
    to = VERIFIED_NUMBER,
    )
