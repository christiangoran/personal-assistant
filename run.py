import json
import requests
import gspread
import openai
import datetime
import colorama
import time
import pyfiglet
from colorama import Fore, Back, Style, init
from google.oauth2.service_account import Credentials

colorama.init()

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

data = []
entries = 0

red_text = Fore.RED
green_text = Fore.GREEN
reset_all = Style.RESET_ALL
yellow_text = Fore.YELLOW
blue_text = Fore.BLUE

def get_name():
    """
    Get user name
    """
    while True:
        try:
            name = input('Please enter your name:\n') 
            if validate_name(name):
                return name
        except ValueError:
            pass     

def validate_name(value):
    """
    Validates that user enters at least 3 characters
    and no numbers.
    """
    try:
        if value.isdigit():
            raise ValueError(f'{reset_all}No, no numbers allowed unless you are a'
                             f'{Style.BRIGHT}{yellow_text} Star Wars droid.'
                             f'{Style.BRIGHT}{red_text} Sorry Elon Musk!{reset_all}')
        elif len(value) < 3:
            raise ValueError(f"Please enter at least 3 letter as a name.")
    except ValueError as e:
        print(f"\nInvalid data: {e}. Please try again.\n")
        return False
    return True  

def get_user_input():
    """
    Get question input from the user
    """
    while True:
        user_input = input(f"\n{reset_all}Please enter your question, and sorry my circuits are a bit"
                           f"{Style.BRIGHT}{red_text} BURNT{reset_all} out at the"
                           " moment, so I will not"
                           f"{Style.BRIGHT}{green_text} REMEMBER{reset_all}"
                           " your previous question.\n")

        if validate_input(user_input):
            print('\nPlease wait a minute.\n')
            break
    return user_input

def validate_input(values):
    """
    Raises valueError if there aren't more than 10 characters in user question.
    """
    try:
        if values.lower() == "exit":
            print(f'\n{Style.BRIGHT}{green_text} We are exiting the terminal for you {name}{reset_all}')
            return True  # "exit" to end the loop
        elif len(values) < 10:
            raise ValueError(
                f'More than {Style.BRIGHT}{red_text} 10{reset_all} characters required, you provided {len(values)}'
            )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.')
        return False
    return True 

def get_response(user_input):
    """
    Takes the user_input, enters it into a variable 'completion'
    toghether with other directives for chatGPT and sends it of
    for a reply.
    """
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "assistant", "content": user_input}]
        )
        if completion.choices:
            return completion.choices[0].message.content
        else:
            return "Something went wrong, please try again."
    except Exception as e:
        return f"Something went wrong:\n\n {str(e)}.\n\nPlease try again."        

def chat_log(user_input, response):
    """
    Adds question and reply together with name and timestamp as a nested list to 
    the data-list and adds 1 to the entries variable to keep count of the 
    number of questions that has been asked.
    """
    global entries
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = [timestamp, name, user_input, response]
    data.append(entry)
    entries += 1
   
def store_data(data):
    """
    The user is presented with the option to store the questions and answers from
    the last session in the cloud.
    """
    global entries
    while True:
        try:
            answer = input("\nWould you like to save your chat-log? (y/n): \n").lower()
            if answer == 'y':
                for sublist in data:
                    log.append_row(sublist)
                print("ok, we saved it for you.\n")
                data.clear()
                return False
            elif answer == 'n':
                print("Ok, we did not save it.\n")
                reduction = len(data)
                entries -= reduction
                data.clear()
                break
            else:
                raise ValueError("\Wrong input. Please answer with 'y' or 'n'.")
        except ValueError as e:
            print(f"\nError: {str(e)}\n")

def manipulate_logs():
    """
    Here the user has the option to remove the stored logs from the cloud.
    """
    global entries
    if entries == 0:
        print(f"{Style.BRIGHT}{yellow_text}Sorry, but you do not have anything in your chat logs.")
        print(f"Let's get you over to the chat terminal to change that!{reset_all}")
        chat_main()
    else:
        print(f"You have {entries} stored: ")
        log_rows = log.get_all_values()[-entries:]
        total_rows = len(log.get_all_values())
        print('---------------')
        for row in log_rows:
            print(f'{Style.BRIGHT}{blue_text}')
            print(row)
            print(f'{reset_all}')  
        print('---------------') 
        
        while True:
            try:
                choice = input("\nDo you want to erase log? y/n \n").lower()
                if choice == 'y':
                    print("\nerasing...\n")
                    row_count = len(log_rows)
                    start_row = total_rows - row_count + 1
                    log.delete_rows(start_row, total_rows) 
                    print(f'{row_count} logs deleted') 
                    entries = 0
                    chat_or_log()
                    return True
                elif choice == 'n':
                    print("\nWe will keep the log for you!\n")
                    chat_or_log()

                else: 
                    raise ValueError("Sorry, wrong input. Please choose 'c' or 'l'.")
            except ValueError as e:
                print(f"\nError: {str(e)}\n") 

def chat_main():
    """
    Function that runs the whole chat aspect of the program.
    """
    while True:
        user_input = get_user_input()
        if user_input.lower() == "exit":
            print("This is your chat log: ")
          #  print(data)
            for row in data:
                print(f'{Style.BRIGHT}{blue_text}')
                print(row)
                print(f'{reset_all}')  
            store_data(data)  
            print(f"{Style.BRIGHT}{green_text}What would you like to do now?")
            chat_or_log()
            break
        else:
            response = get_response(user_input)
            print(f'{Style.BRIGHT}{green_text}')
            print("ChatGPT: ", response)
            print(f'{reset_all}')
            chat_log(user_input, response)

def chat_or_log():
    """
    Main menu
    """
    while True:
        try:
            choice = input(f"\n{Style.BRIGHT}{green_text}Press (c) to use the chat bot \nor press (l)"
                           f"to access your chat log: \n{reset_all}").lower()
            if choice == 'c':
                print(f'\n{reset_all}Ok, then chat bot it is!\n')
                print('The question should contain at least 10 characters')
                print(f'and if you would like to leave the program, just type{Style.BRIGHT}{red_text} "exit"{reset_all}.\n')
                print(f'\n  {Style.BRIGHT}{yellow_text}    Enjoy!  {reset_all}    \n\n')
                chat_main()
                return True
            elif choice == 'l':
                print("\nOk, let's pull out your log!\n")
                manipulate_logs()

            else: 
                raise ValueError("Sorry, wrong input. Please choose 'c' or 'l'.")
        except ValueError as e:
            print(f"\nError: {str(e)}\n")   

# --------------------------------------
# Initial code
# --------------------------------------

def rainbow_text(text):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    colored_chars = [colors[i % len(colors)] + char for i, char in enumerate(text)]
    return "".join(colored_chars)

text = "\n Beep beep boot\nWelcome to my...\n"
rainbow = rainbow_text(text)

for char in rainbow:
    print(char, end="", flush=True)
    time.sleep(0.01)

print(pyfiglet.figlet_format("Chat\nBoot", font = "isometric3"))
name = get_name()        
print(Fore.GREEN + f'\nHello {name} what would you like to do?\n')
chat_or_log()   