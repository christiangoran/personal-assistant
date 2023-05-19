import json
import requests
import gspread
import openai
import datetime
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

def get_user_input():
    """
    Get question input from the user
    """
    while True:
        user_input = input("Please enter your question: ")

        if validate_input(user_input):
            print('\nPlease wait a minute.\n')
            break

    return user_input

def validate_input(values):
    """
    Inside the try, Raises valueError if there aren't more than 10 characters.
    """
    try:
        if values.lower() == "exit":
            print(f'We are exiting the terminal for you {name}')
            return True  # "exit" to end the loop
        elif len(values) < 10:
            raise ValueError(
                f'More than 10 characters required, you provided {len(values)}'
            )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.')
        return False

    return True 

def get_response(user_input):
    """
    Takes the user_input, enters it into a variable 'completion'
    toghether with other directives for chatGPT
    """

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "assistant", "content": user_input}]
    )

    if completion.choices:
        return completion.choices[0].message.content
    else:
        return "Something went wrong, please try again."

def validate_name(value):
    try:
        if value.isdigit():
            raise ValueError(f'No, no numbers allowed unless you are a Star Wars droid')
        elif len(value) < 3:
            raise ValueError(f"Please enter at least 3 letter as a name.")
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again.")
        return False

    print(f'\nWelcome {value}, go ahead and ask your question.\n') 
    print('The question should containt at least 10 characters')
    print('and if you would like to leave the program, just type "exit.\n')
    print('\n     Enjoy!      \n\n')
    return True

def get_name():
    while True:
        try:
            name = input('Please enter your name: ') 
            if validate_name(name):
                return name
        except ValueError:
            pass       

def chat_log(user_input, response):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log.append_row([timestamp, name, user_input, response])

def main():
   
    user_input = get_user_input()
    response = get_response(user_input)
    print("ChatGPT: ", response)
    chat_log(user_input, response)
 
print('\nWelcome to my chat terminal\n')     
name = get_name()        
main()
# Exit loop


