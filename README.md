# Beep Beep Pot - My ChatBot!

The ChatBot app was created as a Porfolio Project #3 (Python Essentials) for Diploma in Full Stack Software Development at Code Institute. It allows the user to ask questions about anything to the my very own Chatbot (API connected ChatGPT 🤫). The questions and answers are stored locally during the session and the user also has the option to store the chat logs in a Google Spreadsheet.

![Here is a live version of my project](https://chat-boot.herokuapp.com/)

![Welcome text](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/start.png)



## Table of content
1. [Project](#project)
    * [Strategy/Scope](#strategyscope)
    * [Site owner goals](#site-owner-goals)
    * [External user's goal](#external-users-goal)
2. [User Experience UX/UI)](#user-experience-uxui)
    * [Colour Scheme](#colour-scheme)
3. [Logic and features](#logic-and-features)
    * [Python logic](#python-logic)
    * [Database structure](#database-structure)
    * [Features](#features)
    * [Main Menu](#main-menu)
    * [ChatBot](#chatbot)
    * [Store Logs](#store-logs)
    * [Access Logs](#access-logs)
4. [Technology](#technology)
    * [Software used](#software-used)
    * [Python libraries/modules](#python-librariesmodules)
5. [Testing](#testing)
    * [Accessibility](#accessibility)
    * [Validation](#validation)
    * [Manual testing](#manual-testing)
    * [Bugs/known issues](#bugsknown-issues)
6. [Deployment](#deployment)
    * [Git and GitHub](#git-and-github)
    * [Deployment to Heroku](#deployment-to-heroku)
7. [Possible future developments](#possible-future-developments)
8. [Credits](#credits)
    * [Code](#code)
    * [Learning Resources](#learning-resources)
    * [Acknowledgments](#acknowledgments)


## Project
### Strategy/Scope
I wanted to take the opportunity to dive into the world of LLM's and to use the time to learn a bit more about how to implement it into my own projects. 
ChatBot allows the user to use my application to ask whatever question they may have, and get intelligent responses via API from OpenAi's ChatGPT. Furthermore the user has the option to store the questions and answers from the current session into a Google Spreadsheet and to access and delete them if the user wants.

To achieve the strategy goals I implemented the following fueatures:
- Clean user interface for easier navigation and readability
- Use of colors in terminal to increase readbility
- A quick and smooth connection to database with Google
- A well designed terminal display for best experience

### Site owner goals
My goal as a developer for this project is to:
- Create an application that has a real life usage
- Create an application that is intuitive
- Create an application that is easy and fun to use
- Create an application that give clear and proper feedback for both valid and invalid input
- Create an application that is free from bugs
- An above all create an application that works as a good foundation for further improvements as the developers knowledge of both programming in general and knowledge of the OpenAi library increases.

### External user's goal
As a user of the application I would like to:
- Immediately understand what the application should be used for
- To understand how the application works without great effort
- To easily access the features of the application
- To receive feedback when input is given
- To be able to exit
- Have a fun experience while using the program
- No bug encounters

## User Experience UX/UI
### Colour Scheme
The closest I came to design of the project were color text selection with the help of colorama library:
- **Red** - Generally used for error messages
- **Yellow** - Used for ChatGPT and highlighted messages
- **Teal** - Used for log entries
- **Green** - Used for general text
- **White** - Used for standard chat en input prompts

Terminal outputs are displayed in high-contrast colours over black background for better readability and accesibillity. 


## Logic and features
### Python Logic

I have programmed according to OOP and the two classes I created is the ChatBot class and the FileVault class. When the chat is chosen an instance of the ChatBot class is created, and when the user want to access the logs in the Google spreadsheet the FileVault class is used.

A flow diagram of the logice for the ChatBot application was created with the use of ![Draw.io](https://app.diagrams.net/)
![Flow chart diagram](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/chatbot-flowchart.png)
You find the PNG version [here](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/chatbot-flowchart.png)

### Database Structure

#### Google API
Google Sheets services is used to store project's database in the spreadsheet. There is one worksheet called log that is used to store the timestamp of a question, user name, question and answer.

![Google Spreadsheet chat log](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/chatlog.png)

#### ChatGPT Integration
This project integrates OpenAI's language model, ChatGPT, for its core functionality. 

Method: get_response

The get_response method is the core of the interaction with the OpenAI API. It takes user input as an argument and sends it to the ChatGPT model for processing.

The function begins by creating a ChatCompletion object using the openai.ChatCompletion.create method. This method takes two parameters: the model to be used (in this case, "gpt-3.5-turbo") and a list of messages. In our case, the list of messages only contains one message, which is the user's input, and it is assigned the role of "assistant".

The ChatCompletion.create method sends a POST request to the OpenAI API, which processes the user's input and generates a response. The response is returned as a ChatCompletion object.

If the ChatCompletion object contains choices (i.e., generated responses), the function returns the content of the first choice. If no choices are generated (which could happen if there's an issue with the input or the API), the function returns a default error message.

In case of any exceptions during the process, such as network issues or API errors, the function catches the exception and prints an error message, along with the exception details. This helps in debugging and understanding what went wrong during the interaction with the API.


### Features

#### Welcome Text & Name Input
- Start screen of the application starts with rainbow colored welcome text being printed out followed by an ASCII logo.
- User is thereafter asked to enter their name.
- 
![Welcome](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/start.png)


- Input is validated and needs to be at least three letters long.
- 
![Wrong name length](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/invalidname2.png)

#### Main Menu
After name is entered, the user come to the main menu with two options to select.
1. Using the ChatBot by pressing "c"
2. or accessing their log by pressing "l"

![Welcome *name*](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/Screenshot%202023-05-27%20at%2023.47.01.png)

- Input is validated

![Wrong main menu input](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/mainmenuerror.png)

#### ChatBot
If user selects "c" the ChatBot function starts.

![ChatBot](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/okchatbot.png)

The user receives some further instructions before being able to enter a question.

![Further instructions](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/instructionprompt.png)

And then after a valid question is entered.

![Question & Response](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/questionresponse.png)

#### Store Logs
When the user types "exit", the chatbot loop is broken and the user is presented with the questions and answers stored from his current session together with username and timestamp.

![Do you want to save these logs?](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/log.png)

User is asked if the logs should be saved.

![Save?](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/wanttosave.png)

And is "y" is selected, the logs are stored.

![Saved](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/savedit.png)

#### Access Logs
If user selects to access logs from the main menu with "c", FileVault starts.
If logs are empty a notification saying so appears before taking the user to the ChatBot.

![No logs](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/sorrybutnologs.png)

And if there are any logs saved they will be retrieved and written out in the terminal.

![log retrieval](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/%20storedlog.png)

And asked wether the user wants to erase or not. If wrong input is entered an error message appears.

![Erase or not? y/n](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/wanttoerase.png)

If user selects "y"

![Logs are erased](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/erasing-logs.png)

## Technology

### Languages used
- [Python](https://www.python.org/) - High-Level, general-purpose programming language.
- [Markdown](https://en.wikipedia.org/wiki/Markdown) - Markup language used to write README.md and TESTING.md

### Software used
- ![GitHub](https://github.com/) - GitHub is used to store repository for the code after being pushed from Git
- ![Git](https://git-scm.com/) - Git was used for version control by utilizing the CodeAnywhere terminal to commit to Git and Push to GitHub
- ![CodeAnywhere](https://app.codeanywhere.com/) - Was used as IDE for priting the app.
- ![Heroku](https://heroku.com/) - Online app used for deployment of project.
- ![Google Sheets API](https://developers.google.com/sheets/api) - This was used to connect with the database where the spreadsheet is located.
- ![Open Ai's ChatGPT](https://chat.openai.com) - Used for generating the responses for my ChatBot.
- ![Draw.io](https://app.diagrams.net/) - Used to create the flow chart diagram.
- [WebAIM](https://webaim.org/resources/contrastchecker/) - online tool to check colour contrast/accesibility.
- [CI Python Linter](https://pep8ci.herokuapp.com/) - Code Institute online python code validataor.

### Python libraries/modules
- ![gspread](https://docs.gspread.org/) - Used for cotron of Google Sheets API.
- ![openai](https://pypi.org/project/openai/) - Used to interact with OpenAI's machine learning models.
- ![datetime](https://pypi.org/project/DateTime/) - Used for the chat log timestamps.
- ![colorama](https://pypi.org/project/colorama/) - Used to create colorful terminal outputs.
- ![time](https://docs.python.org/3/library/time.html) - Used to create the letter printout in the initial part of the program execution.
- ![pyfiglet](https://pypi.org/project/pyfiglet/) - Used to create ASCII text.
- ![os](https://docs.python.org/3/library/os.html) - Used for my clear screen function to delay the screen being cleared to give the user time to read the terminal prompt before a new one appears.

## Testing
### Accessibility
![WebAIM](https://webaim.org/resources/contrastchecker/) was used to check color contrast of terminal colours. All colors passed the test to a satisfactory level.
![Green](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/contrast-green.png)
![Teal](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/contrast-teal.png)
![Yellow](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/contrast-yellow.png)
![Red](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/contrast-red.png)

### Validation
**PEP8**

![PEP8CI](https://pep8ci.herokuapp.com/) Was used to lint the code. All modules are clear and no errors were found. The run.py code was showing a few warning regarding whitespaces and code over 80 characters in length. Nothing that affected functionalities and code was interpreted as intended.
![Linter validation](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/pep8ci.png)

### Manual testing

- Detailed manual testing procedure can be found in [TESTING.md file](https://github.com/christiangoran/personal-assistant/blob/main/TESTING.md)

### Bugs/Known Issues
- While developing the FileVault section, particularly the functionality to erase chat logs from the Google spreadsheet, I encountered a perplexing issue. Despite my code executing without any apparent errors, no log rows were being deleted from the spreadsheet. After investing a significant amount of time, I realized that the commands were not automatically identifying the last row with data. Instead, they were starting from the absolute last row, such as row 999, regardless of whether it contained any data. In hindsight, pretty obvious.
   - Solution was to add "get_all_values()" that retrieves the cells with data in them.

- I did not manage to find a way to wrap ChatGPT's answer within 80 characters, so there is an overflow that can break in the middle of words at the moment.


## Deployment
### Git and GitHub
1. ![Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template) was used to create the GitHub public repository ![GitHub Personal Assistant](https://github.com/christiangoran/personal-assistant) In template repository I clicked on "use this template" --> "create new repository", I chose repository name and clicked on the green button "Create repository from template".

I cloned repository to ![CodeAnywhere](https://app.codeanywhere.com/) and used this IDE for coding.

I developed programm, often commiting changes using terminal commands:

    git add .
    git commit -m "Whatever changes I made"
    git push

I made sure that all my libraries and packages are listed in requirements.txt.

When program was ready for further deployment I visited heroku.com website to deploy on heroku.

### Deployment to Heroku
1. I visited [https://heroku.com/](https://heroku.com/) and opened dashboard. Then I clicked button "New" and selected "Create new app" button.

2. I entered my app name as "chat-boot" since "personal-assistant" was not available, chose region to Europe and clicked on "Create app" button

3. The next step was to go to "Deploy" tab and then to "Deployment method" section to authorize and connect my GitHub account.

4. Upon succesfull connection I selected main branch from "personal-assistant" repository.

5. Then I went to "Settings" tab...

6. ... and next to "Buildpacks" section. In the next step I added pyhton and nodejs buildpacks. Order here is very important.

7. In the next step I went to "Config Vars" section and added KEY "CREDS" - That matches my credentials in the project.

9. I added key "PORT" with value "8000" and save changes.

6. In the next step I went back to "Deploy" tab and decided to use manual deploy.

7. The link to my deployed app was shown on screen: [https://chat-boot.herokuapp.com/](https://chat-boot.herokuapp.com/)

<br>

During the deployment I noticed that the program was running extremely slow, or mostly hardly starting up at all. After trying to find a solution to the problem without success I removed the entire project from Heroku and re-deployed it. This time it worked like a charm 👌🏼

## Possible Future Developments
If I would have had more time I would have:
- Added more extensive log retrieving functions. I had already a version up and running where the user could access their logs based on their name as keyword. Therefore being able to bring out logs from not only current session but all sessions under the same user name.
- More specific log deletion where the user can select wether they would like to delete all the logs under their name or only todays logs. This was also working besides the little detail that the logs were not actually deleted from the Google Spreadsheet. Due to lack of time I had to revert back to a more scaled down version of log manipulation.

The fact that the ChatBot does not have a memory was a choice I did for financial reasons. The requests being sent to OpenAi are "token" based, meaning they are built up by the use of characters in combination with one another, so it is more complex thatn to say 1 token is 1 character, but the number of tokens being sent of to OpenAi also increases the cost of each request. Therefore I chose not to include each increasing number of questions and answers with the requests.

Future development will include a model of the ChatGPT with trained with custom data, and is the original reason for me to create this foundation of a project. With this, the need for including a memory to the chatbot will be necessary.

## Credits
### Code
- Google Sheets API connection method is taken from Love Sandwiches CI Project and gspread documentation 
- Line 70 - 98 have been created with the code from Love Sandwiches as a template.

### Learning Resources
- [Code Institute course and learning platform](https://codeinstitute.net/)
- [W3Schools](https://www.w3schools.com/python/default.asp)
- [StackOverflow](https://stackoverflow.com/)
- [Google Sheets API documentation](https://developers.google.com/sheets/api/quickstart/python)
- [Gspread documentation](https://docs.gspread.org/en/v5.7.0/)
- [OpenAI Repository](https://github.com/openai/openai-python)
- [ChatGPT Youtube tutorial](https://www.youtube.com/watch?v=c-g6epk3fFE)
- [freecodecamp.org](https://www.youtube.com/watch?v=uRQH2CFvedY&t=649s)

### Acknowledgments

-   My Mentor Gareth McGirr for valuable feedback and guidance throughout the project.
-   Code Institute Slack Community for being invaluable knowledge base.
-   Special thanks to class mates @Katerina and @Starhigh for taking the time to look through the app and give feedback. 
