# Manual testing of validation and functionalities

The testing was ongoing during development and the thousands of times that the code has ben executed to test various lines of code. Manual testing was done to check all inputs and features. <br>
Spelling and typo errors were fixed during the development.


## Name Input
Method for validating name is validate_name()

| What is being tested | Input  | Expected response | Result  |
|---|---|---|---|
|  Please enter your name | less than 3 characters   |Wrong input | Pass
|  Please enter your name | numbers input   |Wrong input | Pass
|  Please enter your name | Write in a 3 letters or more | Valid input | Pass


## Main Menu

|  What is being tested  | Input  | Expected response  | Result
|---|---|---|---|
|  Press C or L to access chat or log | "space"  | Error: Wrong input  | Pass
|  Press C or L to access chat or log | "a"  | Error: Wrong input  | Pass
|  Press C or L to access chat or log | number  | Error: Wrong input  | Pass
|  Press C or L to access chat or log | "c"  | Valid Input, user starts ChatBot | Pass
|  Press C or L to access chat or log | "l"  | Valid Input, user starts FileVault | Pass

## ChatBot

|  What is being tested  | Input  | Expected response  | Result
|---|---|---|---|
|  Question, minimum 10 characters | Less than 10 characters  | Invalid Data  | Pass
|  Question, minimum 10 characters | "Space"  | Invalid Data  | Pass
|  Question, minimum 10 characters | Input with 10 characters or more  | Valid data  | Pass
|  Question, minimum 10 characters | "exit" | Exits the ChatBot question prompt  | Pass



## Saving Log

|  What is being tested  | Input  | Expected response  | Result
|---|---|---|---|
|  Do the right number logged of Q&A's appear | 5 Q&A's  | 5 logged Q&A's with timestap and name  | Pass
|  Question if I would like to save my log, y/n | "space"  | Wrong input  | Pass
|  Question if I would like to save my log, y/n | any character besides "y" or "n"  | Wrong input  | Pass
|  Question if I would like to save my log, y/n | "y"  | Log saved!  | Pass
|  Question if I would like to save my log, y/n | "n | Log is not saved  | Pass


## FileVault

|  What is being tested  | Input  | Expected response  | Result
|---|---|---|---|
|  When no Q&A's are saved | None | Used is transferred to ChatBot | Pass
|  When there is a Google Spreadsheet log | None | Log entries appears | Pass
|  Would you like to erase these logs? y/n | "space" | Wrong input | Pass
|  Would you like to erase these logs? y/n | any letter except y/n | Wrong input | Pass
|  Would you like to erase these logs? y/n | y | Log erased from spreadsheet | Pass
|  Would you like to erase these logs? y/n | n | Log untouched | Pass

