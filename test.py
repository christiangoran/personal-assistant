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

red_text = Fore.RED
green_text = Fore.GREEN
reset_all = Style.RESET_ALL
yellow_text = Fore.YELLOW
blue_text = Fore.BLUE

class ChatBot:
    def __init__(self):
        self.data = []
        self.entries = 0
        self.name = ""
    

    def get_name(self):
        """
        Get user name
        """
        while True:
            try:
                self.name = input('Please enter your name:\n')
                if self.validate_name(self.name):
                    break
            except ValueError:
                pass


    def validate_name(self, value):
        """
        Validates that user enters at least 3 characters
        and no numbers.
        """
        try:
            if value.isdigit():
                raise ValueError(f'{reset_all}No, no numbers allowed unless you'
                                f' are a{Style.BRIGHT}{yellow_text} Star Wars'
                                f'droid.{Style.BRIGHT}{red_text}'
                                f' Sorry Elon Musk!{reset_all}')
            elif len(value) < 3:
                raise ValueError(f"Please enter at least 3 letter as a name.")
        except ValueError as e:
            print(f"\nInvalid data: {e}. Please try again.\n")
            return False
        return True


    def get_user_input(self):
        """
        Get question input from the user
        """
        while True:
            user_input = input(f"\n{reset_all}Please enter your question, and"
                               f" sorry my circuits are a bit"
                               f"{Style.BRIGHT}{red_text} BURNT{reset_all}"
                               " out at the moment, so I will not"
                               f"{Style.BRIGHT}{green_text} REMEMBER{reset_all}"
                               " your previous question.\n")

            if self.validate_input(user_input):
                print('\nPlease wait a minute.\n')
                break
        return user_input


    def validate_input(self, values):
        """
        Raises valueError if there aren't more than 10 characters in user question.
        """
        try:
            if values.lower() == "exit":
                print(f'\n{Style.BRIGHT}{green_text} We are exiting the terminal'
                      f' for you {self.name}{reset_all}')
                return True  # "exit" to end the loop
            elif len(values) < 10:
                raise ValueError(f'More than {Style.BRIGHT}{red_text}'
                                f'10{reset_all} characters'
                                f' required, you provided {len(values)}')
        except ValueError as e:
            print(f'Invalid data: {e}, please try again.')
            return False
        return True


    def get_response(self, user_input):
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


    def chat_log(self, user_input, response):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = [timestamp, self.name, user_input, response]
        self.data.append(entry)
        self.entries += 1


    def store_data(self, data):
        """
        The user is presented with the option to store the questions
        and answers from the last session in the cloud.
        """
        while True:
            try:
                answer = input("\nWould you like to save your chat-log?"
                               "(y/n): \n").lower()
                if answer == 'y':
                    for sublist in self.data:
                        log.append_row(sublist)
                    print("ok, we saved it for you.\n")
                    self.data.clear()
                    return False
                elif answer == 'n':
                    print("Ok, we did not save it.\n")
                    reduction = len(self.data)
                    self.entries -= reduction
                    self.data.clear()
                    break
                else:
                    raise ValueError("Please answer with 'y' or 'n'.")
            except ValueError as e:
                print(f"\nBrain Error: {str(e)}\n")


    def chat_main(self):
        while True:
            user_input = self.get_user_input()
            if user_input.lower() == "exit":
                print("This is your chat log: \n")
                for row in self.data:
                    print(f'{Style.BRIGHT}{blue_text}')
                    print(row)
                    print(f'{reset_all}')
                self.store_data(self.entries)
                print(f"What would you like to do now?")
                chat_or_log()
                break
            else:
                response = self.get_response(user_input)
                print(f"{Style.BRIGHT}{yellow_text}ChatGPT:{Style.BRIGHT}{blue_text} ", response)
                print(f"{reset_all}")
                self.chat_log(user_input, response)

    
class FileVault:
    """
    This class is useed to manipulate logs
    """
    @staticmethod
    def manipulate_logs():
        """
        Here the user has the option to remove the stored logs from the cloud.
        """
        if bot.entries == 0:
            print(f"{Style.BRIGHT}{yellow_text}Sorry, but you do not have"
                f"anything in your chat logs.")
            print(f"Let's get you over to the chat terminal to"
                  f"change that!{reset_all}")
            bot.chat_main()
        else:
            print(f"You have {bot.entries} stored: ")
            log_rows = log.get_all_values()[-bot.entries:]
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
                        bot.entries = 0
                        chat_or_log()
                        return True
                    elif choice == 'n':
                        print("\nWe will keep the log for you!\n")
                        chat_or_log()

                    else:
                        raise ValueError("Pay attention! Please choose"
                                        "'y' or 'n'.")
                except ValueError as e:
                    print(f"\nBrain Error: {str(e)}\n")


 #_-----------------------------   

def rainbow_text(text):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN,
              Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    colored_chars = [colors[i % len(colors)] +
                     char for i, char in enumerate(text)]
    return "".join(colored_chars)

def chat_or_log():
    """
    Main menu
    """
    while True:
        try:
            choice = input(f"\n{Style.BRIGHT}{green_text}Press (c) to use"
                           f" the chat bot \nor press (l)"
                           f"to access your chat log: \n{reset_all}").lower()
            if choice == 'c':
                print(f'\n{reset_all}Ok, then chat bot it is!\n')
                print('The question should contain at least 10 characters')
                print(f'and if you would like to leave the program, just'
                      f' type{Style.BRIGHT}{red_text} "exit"{reset_all}.\n')
                print(f'\n  {Style.BRIGHT}{yellow_text}    Enjoy!    '
                      f'{reset_all}    \n\n')
                bot.chat_main()
                return True
            elif choice == 'l':
                print("\nOk, let's pull out your log!\n")
                vault.manipulate_logs()

            else:
                raise ValueError("Sorry, wrong input. Please choose"
                                 "'c' or 'l'.")
        except ValueError as e:
            print(f"\nError: {str(e)}\n")    

#---.. Start here
def startup():
    text = "\n Beep beep pot\nWelcome to my...\n"
    rainbow = rainbow_text(text)

    for char in rainbow:
        print(char, end="", flush=True)
        time.sleep(0.01)

    print(pyfiglet.figlet_format("Chat-Bot", font="big"))
    bot.get_name()
    print(Fore.GREEN + f'\nHello {bot.name} what would you like to do?\n')
    chat_or_log()

vault = FileVault()
bot = ChatBot()
startup() 