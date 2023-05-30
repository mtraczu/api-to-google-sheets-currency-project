import os
from datetime import datetime
import pytz
import requests
import time

# Environment Variables
API_KEY = os.environ["API_KEY"]
API_GET_ENDPOINT = os.environ["API_GET_ENDPOINT"]
API_POST_ADDRESS = os.environ["SHEET_POST_ADDRESS"]
SHEET_NAME = os.environ["SHEET_NAME"]


def check_time(date):
    minutes = date[-2:]
    return minutes == "00" or minutes == "30"


def wait_minutes(date):
    minutes = date[-2:]
    if int(minutes) in range(0, 31):
        return (30 - int(minutes)) * 60
    elif int(minutes) in range(31, 61):
        return (60 - int(minutes)) * 60


def get_values():
    global date_time
    global API_KEY
    params = {
        "currency": "EURUSD",
        "date_time": date_time,
        "api_key": API_KEY
    }
    response = requests.get(API_GET_ENDPOINT, params=params)
    response.raise_for_status()
    return response.json()


def post_values(data):
    global today_date
    sheet_inputs = {
        SHEET_NAME: {
            "date": today_date,
            "currency": data["currency"],
            "open": data["open"],
            "low": data["low"],
            "high": data["high"],
            "close": data["close"]
        }}
    sheet_response = requests.post(url=API_POST_ADDRESS, json=sheet_inputs)
    sheet_response.raise_for_status()
    # print(sheet_response.text)


while True:
    date_time = datetime.now(pytz.timezone('GMT')).strftime(f"%Y-%m-%d-%H:%M")
    today_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if check_time(date_time):
        data = get_values()
        post_values(data)
        print("Inserted")
        time.sleep(60)
    else:
        print(f"Waiting {int(wait_minutes(date_time)/60)} minutes")
        wait_time = wait_minutes(date_time)
        time.sleep(wait_time)
