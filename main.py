import os
from datetime import datetime
import pytz
import requests
# Environment Variables

API_KEY= os.environ["API_KEY"]
API_GET_ENDPOINT = os.environ["API_GET_ENDPOINT"]
API_POST_ADDRESS = os.environ["SHEET_POST_ADDRESS"]
SHEET_NAME = os.environ["SHEET_NAME"]


date_time = datetime.now(pytz.timezone('GMT')).strftime(f"%Y-%m-%d-%H:%M")
today_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


params = {
    "currency": "EURUSD",
    "date_time": date_time,
    "api_key": API_KEY
}

response = requests.get(API_GET_ENDPOINT, params=params)
response.raise_for_status()
data = response.json()

print(data)