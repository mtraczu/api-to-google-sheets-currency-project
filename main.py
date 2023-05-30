import os

# Environment Variables

API_KEY= os.environ["API_KEY"]
API_GET_ENDPOINT = os.environ["API_GET_ENDPOINT"]
API_POST_ADDRESS = os.environ["SHEET_POST_ADDRESS"]
SHEET_NAME = os.environ["SHEET_NAME"]

print(API_KEY)
print(API_GET_ENDPOINT)
print(API_POST_ADDRESS)
print(SHEET_NAME)
