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
blue_text = Fore.CYAN


# Main Class
class ChatBot:
    """
    This class represents the chat bot and contains the following methods:
    # __init__(self): Placeholder and data holding attributes.
    # get_name(self): Gets the name of the user.
    # validate_name(self, value): Validates the name to contain at least
    3 characters and no numbers.
    # get_user_input(self): Takes the user question.
    # validate_inpu(self, values): validates so that user enters at least
    10 characters or if the user writes "exit".
    # get_response(self, user_input): takes user_input and sends it via API
    to OpenAI for a response.
    # chat_log(self, user_input, response): Takes the arguments and store them
    together with a timestamp in a nested list in the list called "data" as
    well as increasing entries variable with 1 to keep track of number of
    questions and responses.
    # store_data(self, data): Function for taking the nested questions/answers
    lists and storing them in a Google Spreadsheet.
    # chat_main(self): Also takes the "exit" command and pulls out the
    nested lists for the user to see before asking wether the user wants
    to save them or not.
    """
    def __init__(self):
        """
        Holds the variables necessary to run the ChatBot.
        """
        self.data = []
        self.entries = 0
        self.name = ""

    def get_name(self):
        """
        Get user name.
        """
        while True:
            try:
                self.name = input(f'{Style.BRIGHT}{green_text}Please enter '
                                  f'your name:\n{reset_all}')
                if self.validate_name(self.name):
                    break
            except ValueError:
                pass

    def validate_name(self, value):
        """
        Validates that user enters at least 3 characters and no numbers.
        """
        try:
            if value.isdigit():
                raise ValueError(f'{Style.BRIGHT}{red_text}No, no numbers '
                                 f'allowed unless you are a Star Wars droid.'
                                 f'\n Sorry Elon Musk{reset_all}')
            elif len(value) < 3:
                raise ValueError(f"Please enter at least 3 letter as a name")
        except ValueError as e:
            print(f"\n{Style.BRIGHT}{red_text}Invalid data: {e}"
                  f"{Style.BRIGHT}{red_text}. Please try again.{reset_all}\n")
            return False
        return True

    def get_user_input(self):
        """
        Takes question input from the user.
        """
        while True:
            user_input = input(f"\n{Style.BRIGHT}{green_text}Please enter your"
                               " question, and"
                               f" sorry my circuits are a bit"
                               f"{red_text} BURNT{green_text}"
                               " out at the moment, "
                               f"so I will not{yellow_text} REMEMBER "
                               f"{green_text}your previous question.\n"
                               f'Again if you would like to leave the program,'
                               f' just type{red_text}'
                               f' "exit"{reset_all}.\n')

            if self.validate_input(user_input):
                print(f'\n{Style.BRIGHT}{yellow_text}Please wait'
                      f' a minute.\n{reset_all}')
                break
        return user_input

    def validate_input(self, values):
        """
        Raises valueError if there aren't more than 10 characters
        in user question.
        """
        try:
            if values.lower() == "exit":
                print(f'\n{Style.BRIGHT}{green_text} We are exiting the'
                      f' terminal'
                      f' for you {self.name}{reset_all}')
                return True  # "exit" to end the loop
            elif len(values) < 10:
                raise ValueError(f'More than '
                                 f'10 characters'
                                 f' required, you provided {len(values)}')
        except ValueError as e:
            print(f'{Style.BRIGHT}{red_text}Invalid data: {e},'
                  f' please try again.{reset_all}')
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
            print(f"{Style.BRIGHT}{red_text}Something went wrong:\n\n"
                  f" {str(e)}.\n\nPlease try again.{reset_all}")

    def chat_log(self, user_input, response):
        """
        Adds name, question, response & a timestamp in a nested list.
        """
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
                answer = input(f"\n{Style.BRIGHT}{green_text}Would you"
                               " like to save your chat-log?"
                               f"(y/n): \n{reset_all}").lower()
                if answer == 'y':
                    for sublist in self.data:
                        log.append_row(sublist)
                    print(f"{Style.BRIGHT}{green_text}ok, we"
                          f" saved it for you.{reset_all}\n")
                    self.data.clear()
                    return False
                elif answer == 'n':
                    print(f"{Style.BRIGHT}{green_text}Ok, "
                          f"we did not save it.{reset_all}\n")
                    reduction = len(self.data)
                    self.entries -= reduction
                    self.data.clear()
                    break
                else:
                    raise ValueError("Please answer with 'y' or 'n'.")
            except ValueError as e:
                print(f"{Style.BRIGHT}{red_text}\nBrain Error:"
                      f"{str(e)}\n{reset_all}")

    def chat_main(self):
        """
        Back bone of the ChatBot. Running the different methods.
        """
        while True:
            user_input = self.get_user_input()
            if user_input.lower() == "exit":
                print(f"{Style.BRIGHT}{green_text}This is"
                      f" your chat log: \n")
                for row in self.data:
                    print(f'{Style.BRIGHT}{blue_text}')
                    print(row)
                    print(f'{reset_all}')
                self.store_data(self.entries)
                print(f"{Style.BRIGHT}{green_text}What would"
                      f" you like to do now?{reset_all}")
                chat_or_log()
                break
            else:
                response = self.get_response(user_input)
                print(f"{Style.BRIGHT}{yellow_text}ChatGPT:"
                      f"{reset_all} ", response)
                self.chat_log(user_input, response)


# File manipulating Class
class FileVault:
    """
    This class is useed to manipulate logs and its only method right now is:
    # manipulate_logs(): Is used when the user want to pull out the
    current sessions questions and answers from the Google spreadsheet.
    The user can choose to delete them or leave them in the Google Spreadsheet.
    """
    @staticmethod
    def manipulate_logs():
        """
        Here the user has the option to remove the stored logs from the cloud.
        """
        if bot.entries == 0:
            print(f"{Style.BRIGHT}{yellow_text}Sorry, but you do not have"
                  f" anything in your chat logs.")
            print(f"Let's get you over to the chat terminal to"
                  f" change that!{reset_all}")
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
                    choice = input(f"\n{Style.BRIGHT}{green_text}Do you"
                                   f" want to{Style.BRIGHT}{red_text} "
                                   "erase log?"
                                   f"{Style.BRIGHT}{green_text} y/n"
                                   f" \n{reset_all}").lower()
                    if choice == 'y':
                        print(f"\n{Style.BRIGHT}{red_text}erasing..."
                              f"{reset_all}\n")
                        row_count = len(log_rows)
                        start_row = total_rows - row_count + 1
                        log.delete_rows(start_row, total_rows)
                        print(f'{Style.BRIGHT}{green_text}{row_count} '
                              'logs deleted')
                        bot.entries = 0
                        chat_or_log()
                        return True
                    elif choice == 'n':
                        print(f"\n{Style.BRIGHT}{green_text}We will"
                              " keep the log for you!\n")
                        chat_or_log()

                    else:
                        raise ValueError("Pay attention! Please choose"
                                         "'y' or 'n'.")
                except ValueError as e:
                    print(f"\n{Style.BRIGHT}{red_text}Brain Error: "
                          f"{str(e)}{reset_all}\n")


def rainbow_text(text):
    """
    Sprinkles a little bit of fairy dust on the project
    in the form of rainbow text being typed out.
    """
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN,
              Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    colored_chars = [colors[i % len(colors)] +
                     char for i, char in enumerate(text)]
    return "".join(colored_chars)


def chat_or_log():
    """
    Main menu.
    """
    while True:
        try:
            choice = input(f"\n{Style.BRIGHT}{green_text}Press (c) to use"
                           f" the chat bot \nor press (l)"
                           f"to access your chat log: \n{reset_all}").lower()
            if choice == 'c':
                print(f'\n{Style.BRIGHT}{green_text}Ok, then chat bot it '
                      'is!\n')
                print('The question should contain at least 10 characters')
                print(f'and if you would like to leave the program, just'
                      f' type{Style.BRIGHT}{red_text} "exit"{reset_all}.\n')
                print(f'\n  {Style.BRIGHT}{yellow_text}    Enjoy!    '
                      f'{reset_all}    \n\n')
                bot.chat_main()
                return True
            elif choice == 'l':
                print(f"\n{Style.BRIGHT}{green_text}Ok, "
                      f"let's pull out your log!\n")
                vault.manipulate_logs()

            else:
                raise ValueError("Sorry, wrong input. Please choose"
                                 "'c' or 'l'.")
        except ValueError as e:
            print(f"\n{Style.BRIGHT}{red_text}Error: "
                  f"{str(e)}\n{reset_all}")


# Start here
def startup():
    """
    Initial startup function.
    """
    text = "\n Beep beep pot\nWelcome to my...\n"
    rainbow = rainbow_text(text)

    for char in rainbow:
        print(char, end="", flush=True)
        time.sleep(0.01)

    print(pyfiglet.figlet_format("Chat-Bot", font="big"))
    bot.get_name()
    print(f'{Style.BRIGHT}{green_text}\nHello {bot.name}'
          ' what would you like to do?\n')
    chat_or_log()


vault = FileVault()
bot = ChatBot()
startup()
