![Welcome text](https://github.com/christiangoran/personal-assistant/blob/main/assets/readmefiles/welcome.png)

The ChatBot app was created as a Porfolio Project #3 (Python Essentials) for Diploma in Full Stack Software Development at Code Institute. It allows the user to ask questions about anything to the my very own bot. The questions and answers are stored locally during the session and the user also has the option to store the chat logs in a Google Spreadsheet 

## Table of content
1. [Project](#project)
    * [Strategy/Scope](#strategy-scope)
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
### Software used
### Python libraries/modules

## Testing
### Acceissibility
### Validation
PEP8
### Bugs/Known Issues

## Deployment
### Git and GitHub
### Deployment to Heroku

## Possible Future Developent

## Credits
### Code
### Media
### Aknowledgements
