import json
import requests
import gspread
import openai
from google.oauth2.service_account import Credentials

f = open('creds.json', 'r')
gpt_creds = json.load(f)
gpt_api = gpt_creds['gpt_api']

openai.api_key = gpt_api

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("chat-log")

log = SHEET.worksheet("log")

data = log.get_all_values()

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "assistant", "content": "When did the Vietnam war end?"}]
)

print(completion)