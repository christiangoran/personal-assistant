![Welcome text](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/welcome.png)

The ChatBot app was created as a Porfolio Project #3 (Python Essentials) for Diploma in Full Stack Software Development at Code Institute. It allows the user to ask questions about anything to the my very own bot. The questions and answers are stored locally during the session and the user also has the option to store the chat logs in a Google Spreadsheet 

## Table of content
1. [Project](#project)
    * [Strategy/Scope](#strategyscope)
    * [Site owner goals](#site-owner-goals)
    * [External user's goal](#external-users-goal)
2. [User Experience (UX/UI)](#user-experience-ux-ui)
    * [Colour Scheme](#colour-scheme)
3. [Logic and features](#logic-and-features)
    * [Python logic](#python-logic)
    * [Database structure](#database-structure)
    * [Features](#features)
    * [Main Menu](#main-menu)
    * [ChatBot](#chatbot)
    * [Store Logs](#store-logs)
    * [Access Logs](#access-logs)
    * [Exit](#exit)
4. [Technology](#technology)
    * [Software used](#software-used)
    * [Python libraries/modules](#python-libraries-modules)
5. [Testing](#testing)
    * [Accessibility](#accessibility)
    * [Validation](#validation)
    * [Manual testing](#manual-testing)
    * [Bugs/known issues](#bugs-known-issues)
6. [Deployment](#deployment)
    * [Git and GitHub](#git-and-github)
    * [Deployment to Heroku](#deployment-to-heroku)
7. [Possible future development](#possible-future-development)
8. [Credits](#credits)
    * [Code](#code)
    * [Media](#media)
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

### Site owners goals
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

## User Experience (UX)
### Colour Scheme
As this is not the usual front end project, the colors selected were:
- Red
- Yellow
- Blue
- Green

Terminal outputs are displayed in high-contrast colours over black background for better readability and accesibillity. 


## Logic and features
### Python Logic
A flow diagram of the logice for the ChatBot application was created with the use of ![Draw.io](https://app.diagrams.net/)
![Flow chart diagram](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/chatbot-flowchart.png)
You find a PDF version [here](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/chatbot-flowchart.png)

### Database Structure
Google Sheets services is used to store project's database in the spreadsheet. There is one worksheet called log that is used to store the timestamp of a question, user name, question and answer.

![Google Spreadsheet chat log](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/chatlog.png)


### Features

#### Welcome Text & Name Input
- Start screen of the application starts with rainbow colored welcome text being printed out followed by an ASCII logo.
- User is thereafter asked to enter their name.
![Welcome](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/welcome.png)


- Input is validated and needs to be at least three letters long.
![Wrong name length](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/wrongnamelength.png)

#### Main Menu
After name is entered, the user come to the main menu with two options to select.
1. Using the ChatBot by pressing "c"
2. or accessing their log by pressing "l"
![Main menu](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/mainmenu.png)

- Input is validated
![Wrong main menu input](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/wrongmenuinput.png)

#### ChatBot


#### Store Logs
#### Access Logs
#### Exit

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

### Python libraries/modules
- ![gspread](https://docs.gspread.org/) - Used for cotron of Google Sheets API.
- ![openai](https://pypi.org/project/openai/) - Used to interact with OpenAI's machine learning models.
- ![datetime](https://pypi.org/project/DateTime/) - Used for the chat log timestamps.
- ![colorama](https://pypi.org/project/colorama/) - Used to create colorful terminal outputs.
- ![time](https://docs.python.org/3/library/time.html) - Used to create the letter printout in the initial part of the program execution.
- ![pyfiglet](https://pypi.org/project/pyfiglet/) - Used to create ASCII text.

## Testing
### Acceissibility
### Validation
**PEP8**

![PEP8CI](https://pep8ci.herokuapp.com/) Was used to lint the code. All modules are clear and no errors were found. The run.py code was showing a few warning regarding whitespaces and code over 80 characters in length. Nothing that affected functionalities and code was interpreted as intended.
![Linter validation](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/pep8ci.png)

### Bugs/Known Issues

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
The deployment to Heroku was made with the help of the Code Institute Love Sandwiches walkthrough video.
- Buildpacks Python and Nodejs was added.
- CREDS and & PORT 8000 added to my Config Vars

After a name was selected I deployed the project.

During the deployment however I noticed that the program was running extremely slow, or mostly hardly starting up at all. After trying to find a solution to the problem without success I removed the entire project from Heroku and re-deployed it. This time it worked like a charm 👌🏼

## Possible Future Developent
If I would have had more time I would have:
- Added more extensive log retrieving functions. I had already a version up and running where the user could access their logs based on their name as keyword. Therefore being able to bring out logs from not only current session but all sessions under the same user name.
- More specific log deletion where the user can select wether they would like to delete all the logs under their name or only todays logs. This was also working besides the little detail that the logs were not actually deleted from the Google Spreadsheet. Due to lack of time I had to revert back to a more scaled down version of log manipulation.

The fact that the ChatBot does not have a memory was a choice I did for financial reasons. The requests being sent to OpenAi are "token" based, meaning they are built up by the use of characters in combination with one another, so it is more complex thatn to say 1 token is 1 character, but the number of tokens being sent of to OpenAi also increases the cost of each request. Therefore I chose not to include each increasing number of questions and answers with the requests.

Future development will include a model of the ChatGPT with trained with custom data, and is the original reason for me to create this foundation of a project. With this, the need for including a memory to the chatbot will be necessary.

## Credits
### Code
### Media
### Aknowledgements
