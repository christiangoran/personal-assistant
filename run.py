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

"""
def get_response(user_input):

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "assistant", "content": user_input}]
    )

    if completion.choices:
        return completion.choices[0].message.content
    else:
        return "Something went wrong, please try again."


response = get_response(user_input)


print(response)

"""

def get_user_input():
    """
    Get question input from the user
    """
    while True:
        print('Question should contain at least 10 characters.')

        user_input = input("Please enter your question: ")

        if validate_input(user_input):
            print('\nPerfect! Please wait a minute and you will get a response.')
            break

    return user_input

def validate_input(values):
    """
    Inside the try, Raises valueError if there aren't more than 10 characters.
    """
    try:
        if len(values) < 10:
            raise ValueError(
                f'More than 10 characters required, you provided {len(values)}'
            )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.')
        return False

    return True 

get_user_input()
# get_response(user_input)

# Exit loop

# Add queries and answers to google chatlog

